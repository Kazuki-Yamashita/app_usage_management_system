import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import usage_management_system_base_infomation_YMK as info #基本情報を含むモジュール
import delete_lab_system_YMK as delLab #研究室・ゼミを削除するモジュール
import change_master_password_system_YMK as chaPass #マスターパスワードの変更を行うモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール


def master(master_function):
    master_window = mw.make_window("マスターパスワード ログイン画面", '350x217')

    genWid.generate_label_widget(master_window, "マスターパスワード : ", 20, 30)
    input_password = genWid.generate_entry_widget(master_window, 30, 120, 33, "*")

    def login_master(): #「マスターログイン」ボタンを押した際の処理
        input_master_password = input_password.get() #入力したパスワードを取得
        info.offer_master_password() #設定されているマスターパスワードを取得
        try:
            login_master_password = info.master_password_list[0] #登録されているマスターパスワードを取得
        except: #初回のみ
            login_master_password = "master_initial-password_YMK"

        if input_master_password == login_master_password: #入力したマスターパスワードが正しい場合
            mes.info("マスターログイン 完了", "マスターパスワードでログインしました！", master_window)
            master_window.destroy()
            if master_function == "del_lab": #使用する機能が、研究室・ゼミの削除の場合
                delLab.delete_lab() #研究室・ゼミの削除画面を表示
            if master_function == "change_master_password": #使用する機能が、マスターパスワードの変更の場合
                chaPass.change_master_password(login_master_password) #マスターパスワードの変更画面を表示
        else:
            mes.error("マスターパスワードが違います", master_window)
            return

    btn_login = tk.Button(master_window, text="マスターログイン", command=login_master, height=2, width=10) #検索ボタンの生成
    btn_login.place(x=140, y=120) #検索ボタンの配置

    master_window.mainloop() #表示
