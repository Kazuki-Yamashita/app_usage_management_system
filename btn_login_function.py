import tkinter as tk #GUI作成のためのライブラリ
import datetime #日時を取得するライブラリ
import convert_widget_state as conWid #ウィジェットを無効化するモジュール
import btn_select_undergraduate_function as btnUnder #学部選択ボタンを押した際に実行される処理
import show_message as mes #メッセージボックスを表示するモジュール
import is_input_entry as isInp #入力項目にすべて入力しているか判定するモジュール
import is_able_login as abLogin #ログイン可能か判定するモジュール
import login_certification_system as logCe #ログイン認証を行うモジュール
import start_app #アプリケーションを起動させるモジュール
import btn_logout_function as btnLogout #ログアウトボタンを押した際に実行される処理
import close_window_function_before_logout as cloWin #ログアウト前に画面を閉じようとした際の処理を記述したファイル

#画面の状態を記述
open_result = "before login"

#ログインボタンを押した際に実行される処理
def btn_login(window, btn_select_undergraduate, btn_login,
 btn_new_registration, app_path, id, password, undergraduate_combobox, open_result):

    input_ID = id.get() #入力したユーザーIDを取得
    input_password = password.get() #入力したパスワードを取得
    selected_undergraduate = undergraduate_combobox.get() #選択した学部を取得

    try:
        selected_lab = btnUnder.lab_combobox.get() #選択した研究室を取得
    except: #研究室・ゼミのコンボボックスが生成されていない場合
        selected_lab = False

    try:
        btnUnder.lab_list
    except : #研究室一覧が取得されていない(学部を選択していない)場合
        mes.error("学部を選択してください", window)
        return

    lab_list = btnUnder.lab_list #選択した学部の研究室リスト

    #入力欄への入力が適切か判定(True or False)
    is_input = isInp.is_input_entry_login(selected_lab, input_ID, input_password, lab_list, window)

    #入力が適切な場合(True)
    if is_input:
        #ログイン認証を行う
        result_login = abLogin.is_able_login(window, selected_undergraduate, selected_lab, input_ID, input_password)

        #ログインできた場合(True)
        if result_login:
            user_name = logCe.name #ログインした人の名前を取得
            user_name_ruby = logCe.name_ruby #ログインした人の名前のフリガナを取得

            #アプリを起動
            open_result = start_app.start_app(window, app_path)
            start_using_datetime = datetime.datetime.now() #ログインした日時を取得

            #使用開始の年月日
            display_start_using_date = (
                                        str(start_using_datetime.year)  + '年'
                                      + str(start_using_datetime.month) + '月'
                                      + str(start_using_datetime.day)   + '日'
                                      )
            #使用開始の時間
            display_start_using_time = (
                                        str(start_using_datetime.hour)  + '時'
                                      + str(start_using_datetime.minute)+ '分'
                                      + str(start_using_datetime.second) + '秒'
                                      )

            #ログイン完了の画面、日時を表示する
            mes.info("ログイン完了", display_start_using_date + "　" + display_start_using_time
            + "\nログインしました", window)

            btn_login.destroy() #「ログイン」ボタンを消す
            btn_new_registration.destroy() #「新規登録」ボタンを消す

            #ログイン後、無効化するウィジェットをリストで指定し、無効化
            disabled_widget_list = [undergraduate_combobox, btn_select_undergraduate, btnUnder.lab_combobox, id, password]
            conWid.to_disabled_widget(disabled_widget_list)

            #ログアウトボタンの生成、配置、コマンド指定
            btn_logout = tk.Button(window, text="ログアウト", bg='skyblue', height=2, width=7)
            btn_logout.place(x=180, y=240) #ログアウトボタンの配置
            btn_logout["command"] = lambda: btnLogout.logout(open_result, selected_undergraduate,
                 selected_lab, input_ID, user_name, user_name_ruby, start_using_datetime, window)

    #ログアウト後に画面を閉じようとした際の処理
    window.protocol('WM_DELETE_WINDOW',
     func = lambda: cloWin.close_root_window(btn_select_undergraduate, open_result, window))
