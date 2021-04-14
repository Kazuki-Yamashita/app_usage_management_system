import subprocess #外部アプリを実行ためのライブラリ
import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import datetime #日時を取得するライブラリ
import math #数学関数のライブラリ
import make_window as mw #ウィンドウを作成するモジュール
import menubar #メニューバーを作成しているファイル
import menubar_function as funMenu #メニューバーを選択した際に実行される関数をまとめたモジュール
import user_registration_system_YMK as regSys #新規登録を行うモジュール
import usage_management_system_base_infomation_YMK as info #基本情報を提供するモジュール
import login_certification_system_YMK as celog #ログイン認証を行うモジュール
import confirm_available_id_system_YMK as conid #IDが存在するか調べる
import generate_widget as genWid #ウィジェット生成するモジュール
import disabled_widget as disWid #ウィジェットを無効化するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import start_app #アプリケーションを起動させるモジュール
import close_window_function_before_logout as cloWin #ログアウト前に画面を閉じようとした際の処理を記述したファイル
import btn_logout_function as btnLogout #ログアウトボタンを押した際に実行される処理

root = mw.make_window("app 利用管理システム", '485x300')

#メニューバーの生成
menubar.make_menubar(root)

open_result = "before login"

#学部の一覧が表示されるコンボボックスの生成
undergraduate_combobox = genWid.generate_combobox_widget(
            root, "readonly", info.undergraduate_list, "学部選択", 130, 50)

def select_undergraduate(): #学部選択ボタンを押した際、以下のことが実行される
    global selected_undergraduate, lab_list
    selected_undergraduate = undergraduate_combobox.get() #選択した学部を取得
    global lab_list
    if not selected_undergraduate: #学部を選択していない場合
        lab_list = None
        mes.error("学部を選択してください", root)
    else:
        info.offer_lab_list(selected_undergraduate) #選択した学部の研究室情報を取得
        lab_list = info.choices_lab

    if selected_undergraduate: #学部を選択している場合のみ以下の処理を行う
        global lab_combobox
        lab_combobox = genWid.generate_combobox_widget(root, "readonly", lab_list, "研究室選択", 130, 90)

        def select_lab(): #研究室・ゼミ選択ボタンを押した際、以下のことが実行される
            global selected_lab
            selected_lab = lab_combobox.get() #選択した研究室を取得
            if not selected_lab: #研究室・ゼミを選択していない場合
                mes.error("研究室・ゼミを選択してください", root)
            else: #研究室・ゼミを選択している場合]
                mes.info("研究室・ゼミ名 選択完了", "研究室・ゼミを選択しました", root)

        global btn_select_lab
        genWid.generate_label_widget(root, "研究室・ゼミ : ", 50, 90)

        btn_select_lab = tk.Button(text="研究室・ゼミを選択", command=select_lab) #研究室・ゼミ選択のボタンを生成
        btn_select_lab.place(x=300, y=90) #研究室・ゼミ選択のボタンを配置

genWid.generate_label_widget(root, "学部 : ", 85, 50)

btn_select_undergraduate = tk.Button(text='学部を選択', command=select_undergraduate) #学部選択のボタンを生成
btn_select_undergraduate.place(x=300, y=50) #学部選択のボタンを配置

#現在の時刻を取得し、表示する文字を作成
now_time = datetime.datetime.now()
display_now_time = (str(now_time.year) + "年" + str(now_time.month) + "月" + str(now_time.day) + "日\n" + str(now_time.hour) +
 "時" + str(now_time.minute) + "分")

#現在の時刻を表示
genWid.generate_label_widget(root, "現在の時刻 : ", 260, 240)
genWid.generate_label_widget(root, display_now_time, 340, 240)

#以下IDとパスワードの文字と入力欄を生成
genWid.generate_label_widget(root, "ユーザーID : ", 50, 150)
txt_id = genWid.generate_entry_widget(root, 30, 130, 150)

genWid.generate_label_widget(root, "パスワード : ", 50, 190)
txt_password = genWid.generate_entry_widget(root, 30, 130, 190, '*')

def login(): #ログインボタンを押した際、以下のことが実行される
    global input_ID
    input_ID = txt_id.get() #ユーザーIDを取得して変数に代入
    input_password = txt_password.get() #パスワードを取得して変数に代入
    selected_lab = lab_combobox.get() #選択した研究室を取得
    global start_using_datetime, open_result, user_name, user_name_ruby

    if not input_ID and input_password: #IDを入力していない場合
        mes.error("IDを入力してください", root)
    elif not input_password and input_ID: #パスワードを入力していない場合
        mes.error("パスワードを入力してください", root)
    elif not input_ID and not input_password: #ID、パスワードどちらも入力していない場合
        mes.error("IDおよびパスワードを入力してください", root)
    elif not selected_lab or not lab_combobox:
        mes.error("研究室・ゼミを選択してください", root)
    elif selected_lab not in lab_list: #選択した研究室・ゼミが選択した学部の研究室一覧に含まれない場合
        mes.error("選択した学部と研究室・ゼミが一致していません", root)
    else:
        #ログイン認証を行う
        exist_id = conid.exist_id(input_ID, selected_undergraduate, selected_lab) #IDが存在しない場合、Falseを代入
        certification = celog.login_certification(input_ID, input_password, selected_undergraduate, selected_lab) #IDとパスワードが一致しない場合、Falseを代入
        if exist_id == False: #入力したIDが存在しない場合
            mes.error("IDが存在しません", root)
        elif certification == False: #ログイン認証できなかった場合
            mes.error("IDとパスワードが一致しません", root)
        else:
            user_name = celog.name #ログインした人の名前を取得
            user_name_ruby = celog.name_ruby #ログインした人の名前のフリガナを取得
            #任意のアプリケーションの絶対パスを入力(先頭の"r"を忘れないこと)
            app_path =r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            #アプリを起動
            open_result = start_app.start_app(root, app_path)
            start_using_datetime = datetime.datetime.now() #ログインした日時を取得

            #使用開始の年月日
            display_start_using_date = (str(start_using_datetime.year) + '年' + str(start_using_datetime.month)
             + '月' + str(start_using_datetime.day) + '日')
            #使用開始の時間
            display_start_using_time = (str(start_using_datetime.hour) + '時' + str(start_using_datetime.minute)
             + '分' + str(start_using_datetime.second) + '秒')

            #ログイン完了の画面、日時を表示する
            mes.info("ログイン完了", display_start_using_date + "　" + display_start_using_time
            + "\nログインしました", root)

            btn_login.destroy() #「ログイン」ボタンを消す
            btn_new_registration.destroy() #「新規登録」ボタンを消す

            disWid.disabled_widget(undergraduate_combobox) #学部選択のコンボボックスを無効化
            disWid.disabled_widget(lab_combobox) #研究室・ゼミ選択のコンボボックスを無効化
            disWid.disabled_widget(txt_id) #IDの入力欄を無効化
            disWid.disabled_widget(txt_password) #パスワードの入力欄を無効化
            disWid.disabled_widget(btn_select_undergraduate) #学部選択ボタンを無効化
            disWid.disabled_widget(btn_select_lab) #研究室・ゼミ選択ボタンを無効化

            #ログアウトボタンの生成
            btn_logout = tk.Button(text="ログアウト", command=lambda: btnLogout.logout(
            open_result, selected_undergraduate, selected_lab, input_ID, user_name, user_name_ruby, start_using_datetime, root),
             bg='skyblue', height=2, width=7)
            btn_logout.place(x=180, y=240) #ログアウトボタンの配置

#ログインボタンの生成
btn_login = tk.Button(text='ログイン', command=login, bg='red',height=2, width=7)
btn_login.place(x=180, y=240) #ログインボタンを配置
#新規登録ボタンを生成
btn_new_registration = tk.Button(text="新規登録", command=lambda: regSys.registration(root), bg='green', height=2, width=7)
btn_new_registration.place(x=40, y=240) #新規登録ボタンを配置

#ログアウト画面を閉じようとした際、実行される関数を指定
root.protocol('WM_DELETE_WINDOW',
 func = lambda: cloWin.close_root_window(btn_select_undergraduate, open_result, root))
root.mainloop() #持続的に表示しておく
