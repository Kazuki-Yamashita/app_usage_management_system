import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import usage_management_system_base_infomation_YMK as info #基本情報を含むモジュール
import delete_lab_from_DB_YMK as delLabDB #DBから研究室・ゼミを削除するモジュール

def make_error(contents): #エラーを表示する関数
    tk.messagebox.showerror("エラー",contents, parent=delete_lab_window)

def delete_lab():
    global delete_lab_window
    delete_lab_window = tk.Tk()
    delete_lab_window.title("研究室・ゼミ 削除画面")
    delete_lab_window.geometry('500x310')

    label_undergraduate = tk.Label(delete_lab_window, text="学部 : ")
    label_undergraduate.place(x=85, y=20)
    search_lab_undergraduate_combobox = tk.ttk.Combobox(delete_lab_window, state="readonly", values=info.undergraduate_list, text="学部選択") #選択した学部のコンボボックス
    search_lab_undergraduate_combobox.place(x=150, y=20) #学部のコンボボックス

    def select_delete_lab_undergraduate(): #学部選択ボタンを押した際の処理
        delete_lab_undergraduate = search_lab_undergraduate_combobox.get() #検索する学部を取得
        if not delete_lab_undergraduate: #学部を選択していない場合
            make_error("学部を選択してください")
            return
        else:
            info.offer_lab_list(delete_lab_undergraduate) #選択した学部の研究室情報を取得
            lab_list = info.choices_lab #研究室リストを代入

            label_lab = tk.Label(delete_lab_window, text="研究室・ゼミ : ")
            label_lab.place(x=50, y=60)
            lab_combobox = tk.ttk.Combobox(delete_lab_window, state="readonly", values=lab_list, text="研究室選択") #選択した学部の研究室一覧が出るコンボボックス
            lab_combobox.place(x=150, y=60) #研究室一覧のコンボボックスを配置

        def delete_lab_btn():
            delete_lab_undergraduate = search_lab_undergraduate_combobox.get() #学部を取得
            info.offer_lab_list(delete_lab_undergraduate) #選択した学部の研究室情報を取得
            lab_list = info.choices_lab #研究室リストを代入
            delete_lab_lab = lab_combobox.get() #選択した研究室を取得

            if not delete_lab_lab:
                make_error("研究室・ゼミを選択してください")
            elif delete_lab_lab not in lab_list:
                make_error("選択した学部と研究室・ゼミが一致していません")
            else:
                message = "本当に研究室・ゼミを削除しますか？"
                delete_lab_confirmation = tk.messagebox.askokcancel("研究室・ゼミ削除 確認画面", message, parent=delete_lab_window) #研究室・ゼミ削除の確認画面

            if delete_lab_confirmation == True: #「OK」を押した場合
                final_message = "研究室・ゼミを削除した場合、該当する研究室・ゼミの利用登録者の情報も削除されます。\n使用履歴は削除されません"
                delete_lab_final_confirmation = tk.messagebox.askokcancel("研究室・ゼミ削除 最終確認画面", final_message, parent=delete_lab_window) #研究室・ゼミ削除の最終確認画面

                if delete_lab_final_confirmation == True: #最終確認で「OK」を押した場合
                    #研究室・ゼミをDBから削除
                    delete_lab_ornot = delLabDB.delete_lab_from_DB(delete_lab_undergraduate, delete_lab_lab)
                    if delete_lab_ornot == False: #削除できなかった場合
                        make_error("研究室・ゼミの削除に失敗しました")
                        return
                    else: #削除できた場合
                        tk.messagebox.showinfo("登録者削除 完了", "登録者の削除を完了しました", parent=delete_lab_window)
                        delete_lab_window.destroy()

        btn_delete_lab = tk.Button(delete_lab_window, text='研究室・ゼミを削除する', command=delete_lab_btn, height=2, width=18, bg="red")
        btn_delete_lab.place(x=190, y=250)

    btn_search_name_undergraduate = tk.Button(delete_lab_window, text='学部を選択', command=select_delete_lab_undergraduate) #学部選択のボタンを生成
    btn_search_name_undergraduate.place(x=320, y=20) #学部選択のボタンを配置

    delete_lab_window.mainloop()
