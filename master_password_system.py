import tkinter as tk #GUI作成のためのライブラリ
import generate_widget as genWid #ウィジェット生成するモジュール
import make_window as mw #ウィンドウを作成するモジュール
#マスターログインのログインボタンを押した際の処理
import btn_login_in_master_password as btnMasterLogin


#マスターパスワードのログイン画面
def master(master_function):
    #ウィンドウの作成
    master_window = mw.make_window("マスターパスワード ログイン画面", '350x217')

    #文字と入力欄を生成
    genWid.generate_label_widget(master_window, "マスターパスワード : ", 20, 30)
    input_password = genWid.generate_entry_widget(master_window, 30, 120, 33, "*")

    #マスターパスワードでのログインボタンを生成、配置、コマンド指定
    btn_login = tk.Button(master_window, text="マスターログイン", height=2, width=10)
    btn_login.place(x=140, y=120)
    btn_login['command'] = lambda: btnMasterLogin.login_master(
    master_window, master_function, input_password)

    master_window.mainloop() #表示
