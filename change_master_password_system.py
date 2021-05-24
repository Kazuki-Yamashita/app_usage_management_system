import tkinter as tk #GUI作成のためのライブラリ
import generate_widget as genWid #ウィジェット生成するモジュール
import make_window as mw #ウィンドウを作成するモジュール
#マスターパスワードの変更ボタンを押した際の処理
import btn_change_master_password_function as btnChaMaster


#マスターパスワードの変更画面
def change_master_password(login_master_password):
    change_master_password_window = mw.make_window("マスターパスワード 変更画面", '360x190')

    #新しいマスターパスワードの入力欄を生成
    genWid.generate_label_widget(change_master_password_window,
     "新しいマスターパスワード : ", 20, 30)
    new_input_password = genWid.generate_entry_widget(change_master_password_window,
     30, 150, 30, "*")

    genWid.generate_label_widget(change_master_password_window,
     "新しいマスターパスワード : \n(確認用)", 20, 70)
    new_input_confirm_password = genWid.generate_entry_widget(change_master_password_window,
     30, 150, 70, "*")

    #注意書きのメッセージを表示
    master_caution = genWid.generate_label_widget(change_master_password_window,
     "設定するマスターパスワードは25文字以上にしてください", 20, 110)
    master_caution["bg"] = "white"

    #「変更」ボタンの生成、配置、コマンド指定
    btn_change_master_password = tk.Button(change_master_password_window, text="変更する", height=2, width=10)
    btn_change_master_password.place(x=150, y=140)
    btn_change_master_password['command'] = lambda: btnChaMaster.conn_change_master_password(
     change_master_password_window, login_master_password,
     new_input_password, new_input_confirm_password)

    change_master_password_window.mainloop()
