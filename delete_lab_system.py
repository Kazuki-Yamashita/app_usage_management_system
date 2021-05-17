import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import usage_management_system_base_infomation as info #基本情報を含むモジュール
import delete_lab_from_DB as delLabDB #DBから研究室・ゼミを削除するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール

#研究室の削除画面
def delete_lab():
    delete_lab_window = mw.make_window("研究室・ゼミ 削除画面", '500x310')

    genWid.generate_label_widget(delete_lab_window, "学部 : ", 85, 20)
    search_lab_undergraduate_combobox = genWid.generate_combobox_widget(
                delete_lab_window, "readonly", info.undergraduate_list, "学部選択", 150, 20)

    #学部選択ボタンを押した際の処理
    def select_delete_lab_undergraduate():
        delete_lab_undergraduate = search_lab_undergraduate_combobox.get() #検索する学部を取得
        if not delete_lab_undergraduate: #学部を選択していない場合
            mes.error("学部を選択してください", delete_lab_window)
            return
        else:
            info.offer_lab_list(delete_lab_undergraduate) #選択した学部の研究室情報を取得
            lab_list = info.choices_lab #研究室リストを代入

            genWid.generate_label_widget(delete_lab_window, "研究室・ゼミ : ", 50, 60)
            lab_combobox = genWid.generate_combobox_widget(delete_lab_window, "readonly", lab_list, "研究室選択", 150, 60)

        def delete_lab_btn():
            delete_lab_undergraduate = search_lab_undergraduate_combobox.get() #学部を取得
            info.offer_lab_list(delete_lab_undergraduate) #選択した学部の研究室情報を取得
            lab_list = info.choices_lab #研究室リストを代入
            delete_lab_lab = lab_combobox.get() #選択した研究室を取得

            if not delete_lab_lab:
                mes.error("研究室・ゼミを選択してください", delete_lab_window)
            elif delete_lab_lab not in lab_list:
                mes.error("選択した学部と研究室・ゼミが一致していません", delete_lab_window)
            else:
                message = "本当に研究室・ゼミを削除しますか？"
                #研究室・ゼミ削除の確認画面
                delete_lab_confirmation = tk.messagebox.askokcancel("研究室・ゼミ削除 確認画面", message, parent=delete_lab_window)

            if delete_lab_confirmation == True: #「OK」を押した場合
                final_message = "研究室・ゼミを削除した場合、該当する研究室・ゼミの利用登録者の情報も削除されます。\n使用履歴は削除されません"
                #研究室・ゼミ削除の最終確認画面
                delete_lab_final_confirmation = tk.messagebox.askokcancel("研究室・ゼミ削除 最終確認画面", final_message, parent=delete_lab_window)

                #最終確認で「OK」を押した場合
                if delete_lab_final_confirmation == True:
                    #研究室・ゼミをDBから削除
                    delete_lab_ornot = delLabDB.delete_lab_from_DB(delete_lab_undergraduate, delete_lab_lab)
                    if delete_lab_ornot == False: #削除できなかった場合
                        mes.error("研究室・ゼミの削除に失敗しました", delete_lab_window)
                        return
                    else: #削除できた場合
                        mes.info("登録者削除 完了", "登録者の削除を完了しました", delete_lab_window)
                        delete_lab_window.destroy()

        btn_delete_lab = tk.Button(delete_lab_window, text='研究室・ゼミを削除する', command=delete_lab_btn, height=2, width=18, bg="red")
        btn_delete_lab.place(x=190, y=250)

    #学部選択のボタンを生成、配置、コマンド指定
    btn_search_name_undergraduate = tk.Button(delete_lab_window, text='学部を選択')
    btn_search_name_undergraduate.place(x=320, y=20)
    btn_search_name_undergraduate['command'] = select_delete_lab_undergraduate

    delete_lab_window.mainloop()
