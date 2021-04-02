import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import delete_user_from_DB_YMK as delUserDB #DBからユーザーを削除するモジュール
import usage_management_system_base_infomation_YMK as info #基本情報を含むモジュール
import confirm_available_id_system_YMK as conid #IDが存在するか調べる
import login_certification_system_YMK as celog #ログイン認証を行うモジュール

def make_error(contents): #エラーを表示する関数
    tk.messagebox.showerror("エラー",contents, parent=delete_user_window)

def delete_user(): #登録者を削除する関数
    global delete_user_window
    delete_user_window = tk.Tk()
    delete_user_window.title("登録者 削除画面")
    delete_user_window.geometry('500x310')

    label_undergraduate = tk.Label(delete_user_window, text="学部 : ")
    label_undergraduate.place(x=85, y=20)
    delete_user_undergraduate_combobox = tk.ttk.Combobox(delete_user_window,state="readonly", values=info.undergraduate_list, text="学部選択") #選択した学部のコンボボックス
    delete_user_undergraduate_combobox.place(x=150, y=20) #学部のコンボボックス

    def select_delete_user_undergraduate(): #学部選択ボタンを押した際の処理
        delete_user_undergraduate = delete_user_undergraduate_combobox.get() #検索する学部を取得
        if not delete_user_undergraduate: #学部を選択していない場合
            make_error("学部を選択してください")
            return
        else:
            info.offer_lab_list(delete_user_undergraduate) #選択した学部の研究室情報を取得
            lab_list = info.choices_lab #研究室リストを代入

            label_lab = tk.Label(delete_user_window, text="研究室・ゼミ : ")
            label_lab.place(x=50, y=60)
            lab_combobox = tk.ttk.Combobox(delete_user_window, state="readonly", values=lab_list, text="研究室選択") #選択した学部の研究室一覧が出るコンボボックス
            lab_combobox.place(x=150, y=60) #研究室一覧のコンボボックスを配置

            del_label_id = tk.Label(delete_user_window, text="ユーザーID : ")
            del_label_id.place(x=50,y=120) #ユーザーIDの位置の指定
            del_txt_id = tk.Entry(delete_user_window,width=30) #ユーザーIDの入力欄
            del_txt_id.place(x=130,y=120) #ユーザーID入力欄の位置の指定

            del_label_password = tk.Label(delete_user_window, text="パスワード : ")
            del_label_password.place(x=50, y=160) #パスワードの位置指定
            del_txt_password = tk.Entry(delete_user_window,width=30, show='*') #パスワードの入力欄
            del_txt_password.place(x=130, y=160) #パスワードの入力欄の位置の指定

        def delete_user_btn(): #「登録者の削除」ボタンを押した際の処理
            input_ID = del_txt_id.get() #ユーザーIDを取得して変数に代入
            input_password = del_txt_password.get() #パスワードを取得して変数に代入
            delete_user_undergraduate = delete_user_undergraduate_combobox.get() #検索する学部を再度取得し、更新
            info.offer_lab_list(delete_user_undergraduate) #選択した学部の研究室情報を取得
            lab_list = info.choices_lab #研究室リストを代入
            delete_user_lab = lab_combobox.get() #選択した研究室を取得

            if not input_ID and input_password: #IDを入力していない場合
                make_error("IDを入力してください")
            elif not input_password and input_ID: #パスワードを入力していない場合
                make_error("パスワードを入力してください")
            elif not input_ID and not input_password: #ID、パスワードどちらも入力していない場合
                make_error("IDおよびパスワードを入力してください")
            elif not delete_user_lab:
                make_error("研究室・ゼミを選択してください")
            elif delete_user_lab not in lab_list: #選択した研究室・ゼミが選択した学部の研究室一覧に含まれない場合
                make_error("選択した学部と研究室・ゼミが一致していません")
            else:
                exist_id = conid.exist_id(input_ID, delete_user_undergraduate, delete_user_lab) #IDが存在しない場合、Falseを代入
                certification = celog.login_certification(input_ID, input_password, delete_user_undergraduate, delete_user_lab) #IDとパスワードが一致しない場合、Falseを代入
                if exist_id == False: #入力したIDが存在しない場合
                    make_error("IDが存在しません")
                    return
                elif certification == False: #ログイン認証できなかった場合
                    make_error("IDとパスワードが一致しません")
                    return
                else:
                    delete_user_name = celog.name #削除する登録者の名前を取得して代入
                    message = "本当に登録者を削除しますか？\n ID : " + input_ID + "\n name : " + delete_user_name #削除の最終確認で表示するメッセージ
                    delete_user_confirmation = tk.messagebox.askokcancel("登録者削除 最終確認", message, parent=delete_user_window) #削除の最終確認画面

                if delete_user_confirmation == True: #「OK」を押した場合
                    #削除を実行
                    delete_ornot = delUserDB.delete_user_from_DB(delete_user_undergraduate, delete_user_lab, input_ID)
                    tk.messagebox.showinfo("登録者削除 完了", "登録者の削除を完了しました", parent=delete_user_window)
                    delete_user_window.destroy()
                    if delete_ornot == False: #削除に失敗した場合
                        make_error("登録者の削除に失敗しました")
                        return

        btn_delete_user = tk.Button(delete_user_window, text='登録情報を削除する', command=delete_user_btn, height=2, width=15, bg="red") #登録者の削除ボタン
        btn_delete_user.place(x=190, y=250)

    btn_search_name_undergraduate = tk.Button(delete_user_window, text='学部を選択', command=select_delete_user_undergraduate) #学部選択のボタンを生成
    btn_search_name_undergraduate.place(x=320, y=20) #学部選択のボタンを配置

    delete_user_window.mainloop()
