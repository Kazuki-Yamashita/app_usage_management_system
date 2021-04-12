import subprocess #外部アプリを実行ためのライブラリ
import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import datetime #日時を取得するライブラリ
import math #数学関数のライブラリ
import user_registration_system_YMK as regSys #新規登録を行うモジュール
import usage_management_system_base_infomation_YMK as info #基本情報を含むモジュール
import login_certification_system_YMK as celog #ログイン認証を行うモジュール
import confirm_available_id_system_YMK as conid #IDが存在するか調べる
import search_user_name_system_YMK as sea #研究室ごとに登録者を検索するモジュール
import memo_system_YMK as memo #備考記入、DBへの記録を含むモジュール
import search_usage_data_system_YMK as seaUsage #使用履歴を調べるモジュール
import delete_user_system_YMK as delUser #登録者を削除するモジュール
import master_password_system_YMK as masPass
import generate_widget as genWid #ウィジェット生成するモジュール
import disabled_widget as disWid #ウィジェットを無効化するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import start_app #アプリケーションを起動させるモジュール

root = tk.Tk() #ウィンドウの作成
root.title("app 利用管理システム") #ウィンドウのタイトル
root.geometry('485x300') #ウィンドウの大きさを指定

def registrate(): #利用者登録を行うページを開く関数
    regSys.registration(root) #利用者登録を行う関数

def bar_search_user_name(): #メニューバーから「利用者検索」を選択した際の処理
    sea.search_user_name()

def bar_search_usage_record(): #メニューバーから「使用履歴の検索」を選択した際の処理
    seaUsage.search_used_data()

def bar_delete_user(): #メニューバーから「登録者の削除」を選択した際の処理
    delUser.delete_user()

def bar_delete_lab(): #メニューバーから「研究室・ゼミの削除」を選択した際の処理
    master_function = "del_lab"
    masPass.master(master_function)

def bar_change_master_password(): #メニューバーから「マスターパスワードの変更」を選択した際の処理
    master_function = "change_master_password"
    masPass.master(master_function)

#メニューバーの記述
menubar = tk.Menu() #メニューバーの作成

menubar_search = tk.Menu(menubar, tearoff=0) #メニューコマンドの作成
menubar_search.add_command(label="登録者の検索", command=bar_search_user_name) #コマンドの追加
menubar_search.add_separator()
menubar_search.add_command(label="使用履歴の検索", command=bar_search_usage_record)
menubar.add_cascade(label="検索", menu=menubar_search) #バーに表示する文字、コマンドを設定

menubar_data_management = tk.Menu(menubar, tearoff=0)
menubar_data_management.add_command(label="登録者の削除", command=bar_delete_user)
menubar_data_management.add_command(label="研究室・ゼミの削除", command=bar_delete_lab)
menubar_data_management.add_command(label="マスターパスワードの変更", command=bar_change_master_password)
menubar.add_cascade(label="データ管理", menu=menubar_data_management)

root["menu"] = menubar #メニューバーを設置

#学部の一覧が表示されるコンボボックスの生成
undergraduate_combobox = genWid.generate_combobox_widget(
            root, "readonly", info.undergraduate_list, "学部選択", 130, 50)

def close_root_window(): #ログアウト画面を閉じようとした場合の処理
    #学部選択ボタンが無効の場合(つまりログインしている状態の場合)かつ、アプリケーションが起動している場合
    if btn_select_undergraduate['state'] == "disabled" and open_result.poll() == None:
        #ログアウトするように注意する(ログアウトしなければ終了できない)
        mes.error("アプリケーションを終了させた後に\nログアウトしてください", root)

    #学部選択ボタンが無効の場合(つまりログインしている状態の場合)
    elif btn_select_undergraduate['state'] == "disabled":
        #ログアウトするように注意する(ログアウトしなければ終了できない)
        mes.error("ログアウトしてください", root)
    else:
        root.destroy() #ログイン、ログアウト画面を閉じる

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

now_time = datetime.datetime.now()
display_now_time = (str(now_time.year) + "年" + str(now_time.month) + "月" + str(now_time.day) + "日\n" + str(now_time.hour) +
 "時" + str(now_time.minute) + "分" + str(now_time.second) + "秒")
 
genWid.generate_label_widget(root, "現在の時刻 : ", 260, 240)
genWid.generate_label_widget(root, display_now_time, 340, 240)

#以下IDとパスワードの扱い
genWid.generate_label_widget(root, "ユーザーID : ", 50, 150)
txt_id = genWid.generate_entry_widget(root, 30, 130, 150)

genWid.generate_label_widget(root, "パスワード : ", 50, 190)
txt_password = genWid.generate_entry_widget(root, 30, 130, 190, '*')

def login(): #ログインボタンを押した際、以下のことが実行される
    global input_ID
    input_ID = txt_id.get() #ユーザーIDを取得して変数に代入
    input_password = txt_password.get() #パスワードを取得して変数に代入
    global start_using_datetime, open_result, user_name, user_name_ruby

    if not input_ID and input_password: #IDを入力していない場合
        mes.error("IDを入力してください", root)
    elif not input_password and input_ID: #パスワードを入力していない場合
        mes.error("パスワードを入力してください", root)
    elif not input_ID and not input_password: #ID、パスワードどちらも入力していない場合
        mes.error("IDおよびパスワードを入力してください", root)
    elif not selected_lab:
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
            display_start_using_time = str(start_using_datetime.hour) + '時' + str(start_using_datetime.minute) + '分' + str(start_using_datetime.second) + '秒'

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

def logout(): #ログアウトボタンを押した際、以下のことが実行される
    if open_result.poll() == None: #アプリケーションを終了せずにログアウトしようとした場合
        mes.error("アプリケーションを終了してください", root) #エラーメッセージを表示する
    else:
        finish_using_datetime = datetime.datetime.now() #ログアウトした日時を取得
        using_time = finish_using_datetime - start_using_datetime #使用時間を計算
        using_second_time = using_time.seconds #使用時間を秒単位に変換
        display_using_minute_time = math.floor(using_second_time / 60) #使用時間を分単位に変換(小数点以下は切り捨て)
        display_using_second_time = math.fmod(using_second_time, 60) #使用時間(分)を60で割る

        #ログアウト完了、使用時間を知らせる画面を表示
        mes.info("ログアウト完了", "ログアウトしました\n" + str(display_using_minute_time) + " 分" +
         str(display_using_second_time) + " 秒使用しました", root)

        root.destroy() #メイン画面を消す

        #備考記入を表示、DBへの記録
        memo.memo(selected_undergraduate, selected_lab, input_ID, user_name, user_name_ruby,
         start_using_datetime, finish_using_datetime, using_second_time)

#ログアウトボタンの生成
btn_logout = tk.Button(text="ログアウト", command=logout, bg='skyblue', height=2, width=7)
btn_logout.place(x=180, y=240) #ログアウトボタンの配置
#ログインボタンの生成
btn_login = tk.Button(text='ログイン', command=login, bg='red',height=2, width=7)
btn_login.place(x=180, y=240) #ログインボタンを配置
#新規登録ボタンを生成
btn_new_registration = tk.Button(text="新規登録", command=registrate, bg='green', height=2, width=7)
btn_new_registration.place(x=40, y=240) #新規登録ボタンを配置

root.protocol('WM_DELETE_WINDOW', close_root_window) #ログアウト画面を閉じようとした際、実行される関数を指定
root.mainloop() #持続的に表示しておく
