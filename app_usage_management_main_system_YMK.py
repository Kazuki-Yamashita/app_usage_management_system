import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import make_window as mw #ウィンドウを作成するモジュール
import menubar #メニューバーを作成しているファイル
import generate_widget as genWid #ウィジェット生成するモジュール
import user_registration_system as regSys #新規利用者登録を行うモジュール
import usage_management_system_base_infomation as info #基本情報を提供するモジュール
import btn_select_undergraduate_function as btnUnder #研究室表示ボタンを押した際に実行される処理
import btn_login_function as btnLogin #ログインボタンを押した際の処理
import display_now_time as dispTime #現在の時刻を表示するモジュール


#任意のアプリケーションの絶対パスを入力(先頭の"r"を忘れないこと)
app_path =r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

#ウィンドウの作成(title, size)
main_window = mw.make_window("app 利用管理システム", '485x300')

#現在の時刻を表示
dispTime.now_time(main_window, "現在の時刻 : ", 260, 240, 340, 240)

#メニューバーを生成
menubar.make_menubar(main_window)

#新規登録ボタンを生成、配置、コマンド指定
btn_user_registration = tk.Button(main_window, text="新規登録", bg='green', height=2, width=7)
btn_user_registration.place(x=40, y=240)
btn_user_registration["command"] = lambda: regSys.user_registration(main_window)

#以下、ログインに関する記述
#文字、学部の一覧が表示されるコンボボックスの生成
genWid.generate_label_widget(main_window, "学部 : ", 85, 50)
login_undergraduate_combobox = genWid.generate_combobox_widget(
            main_window, "readonly", info.undergraduate_list, "学部選択", 130, 50)

#研究室・ゼミ選択の文字を表示
genWid.generate_label_widget(main_window, "研究室・ゼミ : ", 50, 90)

#IDとパスワードの文字と入力欄を生成
genWid.generate_label_widget(main_window, "ユーザーID : ", 50, 150)
txt_id = genWid.generate_entry_widget(main_window, 30, 130, 150)

genWid.generate_label_widget(main_window, "パスワード : ", 50, 190)
txt_password = genWid.generate_entry_widget(main_window, 30, 130, 190, '*')

#研究室表示ボタンを生成、配置、コマンド指定
btn_select_undergraduate = tk.Button(main_window, text='学部の研究室・ゼミを表示')
btn_select_undergraduate.place(x=300, y=50)
btn_select_undergraduate["command"] = lambda: btnUnder.select_undergraduate(
                                        main_window, "login", login_undergraduate_combobox, 130, 90)

#ログインボタンを生成、配置、コマンド指定
btn_login = tk.Button(main_window, text='ログイン', bg='red', height=2, width=7)
btn_login.place(x=180, y=240)
btn_login["command"] = lambda: btnLogin.btn_login(main_window,
    btn_select_undergraduate, btn_login, btn_user_registration, app_path,
    txt_id, txt_password, login_undergraduate_combobox, btnLogin.open_result)

main_window.mainloop() #持続的に表示しておく
