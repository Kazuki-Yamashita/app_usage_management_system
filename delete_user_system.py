import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import delete_user_from_DB as delUserDB #DBからユーザーを削除するモジュール
import usage_management_system_base_infomation as info #基本情報を含むモジュール
import confirm_available_id_system as conid #IDが存在するか調べる
import login_certification_system as logCe #ログイン認証を行うモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール


def delete_user(): #登録者を削除する関数
    delete_user_window = mw.make_window("登録者 削除画面", '500x310')

    genWid.generate_label_widget(delete_user_window, "学部 : ", 85, 20)
    delete_user_undergraduate_combobox = genWid.generate_combobox_widget(
        delete_user_window, "readonly", info.undergraduate_list, "学部選択", 150, 20)

    def select_delete_user_undergraduate(): #学部選択ボタンを押した際の処理
        delete_user_undergraduate = delete_user_undergraduate_combobox.get() #検索する学部を取得
        if not delete_user_undergraduate: #学部を選択していない場合
            mes.error("学部を選択してください", delete_user_window)
            return
        else:
            info.offer_lab_list(delete_user_undergraduate) #選択した学部の研究室情報を取得
            lab_list = info.choices_lab #研究室リストを代入

            genWid.generate_label_widget(delete_user_window, "研究室・ゼミ : ", 50, 60)
            lab_combobox = genWid.generate_combobox_widget(delete_user_window, "readonly", lab_list, "研究室選択", 150, 60)

            genWid.generate_label_widget(delete_user_window, "ユーザーID : ", 50, 120)
            del_txt_id = genWid.generate_entry_widget(delete_user_window, 30, 130, 120) #IDの入力欄

            genWid.generate_label_widget(delete_user_window, "パスワード : ", 50, 160)
            del_txt_password = genWid.generate_entry_widget(delete_user_window, 30, 130, 160, "*") #パスワードの入力欄

        def delete_user_btn(): #「登録者の削除」ボタンを押した際の処理
            input_ID = del_txt_id.get() #ユーザーIDを取得して変数に代入
            input_password = del_txt_password.get() #パスワードを取得して変数に代入
            delete_user_undergraduate = delete_user_undergraduate_combobox.get() #検索する学部を再度取得し、更新
            info.offer_lab_list(delete_user_undergraduate) #選択した学部の研究室情報を取得
            lab_list = info.choices_lab #研究室リストを代入
            delete_user_lab = lab_combobox.get() #選択した研究室を取得

            if not input_ID and input_password: #IDを入力していない場合
                mes.error("IDを入力してください", delete_user_window)
            elif not input_password and input_ID: #パスワードを入力していない場合
                mes.error("パスワードを入力してください", delete_user_window)
            elif not input_ID and not input_password: #ID、パスワードどちらも入力していない場合
                mes.error("IDおよびパスワードを入力してください", delete_user_window)
            elif not delete_user_lab:
                mes.error("研究室・ゼミを選択してください", delete_user_window)
            elif delete_user_lab not in lab_list: #選択した研究室・ゼミが選択した学部の研究室一覧に含まれない場合
                mes.error("選択した学部と研究室・ゼミが一致していません", delete_user_window)
            else:
                exist_id = conid.exist_id(input_ID, delete_user_undergraduate, delete_user_lab) #IDが存在しているか判定
                #IDとパスワードが一致しているか判定
                certification = logCe.login_certification(input_ID, input_password, delete_user_undergraduate, delete_user_lab)
                if exist_id == False: #入力したIDが存在しない場合
                    mes.error("IDが存在しません", delete_user_window)
                    return
                elif certification == False: #ログイン認証できなかった場合
                    mes.error("IDとパスワードが一致しません", delete_user_window)
                    return
                else:
                    delete_user_name = logCe.name #削除する登録者の名前を取得して代入
                    message = "本当に登録者を削除しますか？\n ID : " + input_ID + "\n name : " + delete_user_name #削除の最終確認で表示するメッセージ
                    delete_user_confirmation = mes.askokcancel("登録者削除 最終確認", message, delete_user_window) #削除の最終確認画面

                if delete_user_confirmation == True: #「OK」を押した場合
                    #削除を実行
                    delete_ornot = delUserDB.delete_user_from_DB(delete_user_undergraduate, delete_user_lab, input_ID)
                    mes.info("登録者削除 完了", "登録者の削除を完了しました", delete_user_window)
                    delete_user_window.destroy()
                    if delete_ornot == False: #削除に失敗した場合
                        mes.error("登録者の削除に失敗しました", delete_user_window)
                        return

        btn_delete_user = tk.Button(delete_user_window, text='登録情報を削除する', command=delete_user_btn, height=2, width=15, bg="red") #登録者の削除ボタン
        btn_delete_user.place(x=190, y=250)

    btn_search_name_undergraduate = tk.Button(delete_user_window, text='学部を選択', command=select_delete_user_undergraduate) #学部選択のボタンを生成
    btn_search_name_undergraduate.place(x=320, y=20) #学部選択のボタンを配置

    delete_user_window.mainloop()
