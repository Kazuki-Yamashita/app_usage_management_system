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

root = tk.Tk() #ウィンドウの作成
root.title("app 利用管理システム") #ウィンドウのタイトル
root.geometry('485x300') #ウィンドウの大きさを指定

def registrate(): #利用者登録を行うページを開く関数
    regSys.registration(root) #利用者登録を行う関数

def search_user_name_(): #メニューバーから「利用者検索」を選択した際の処理
    sea.search_user_name()

def search_usage_record(): #メニューバーから「使用履歴の検索」を選択した際の処理
    seaUsage.search_used_data()

def delete_user_(): #メニューバーから「登録者の削除」を選択した際の処理
    delUser.delete_user()

def delete_lab_(): #メニューバーから「研究室・ゼミの削除」を選択した際の処理
    master_function = "del_lab"
    masPass.master(master_function)

def master_password(): #メニューバーから「マスターパスワードの変更」を選択した際の処理
    master_function = "change_master_password"
    masPass.master(master_function)

#メニューバーの記述
mbar = tk.Menu() #メニューバーの作成

mcom1 = tk.Menu(mbar, tearoff=0) #メニューコマンドの作成
mcom1.add_command(label="登録者の検索", command=search_user_name_) #コマンドの追加
mcom1.add_separator()
mcom1.add_command(label="使用履歴の検索", command=search_usage_record)
mbar.add_cascade(label="検索",menu=mcom1) #バーに表示する文字、コマンドを設定

mcom2 = tk.Menu(mbar, tearoff=0)
mcom2.add_command(label="登録者の削除", command=delete_user_)
mcom2.add_command(label="研究室・ゼミの削除", command=delete_lab_)
mcom2.add_command(label="マスターパスワードの変更", command=master_password)
mbar.add_cascade(label="データ管理", menu=mcom2)

root["menu"] = mbar #メニューバーを設置

undergraduate_combobox = tk.ttk.Combobox(state="readonly", values=info.undergraduate_list, text="学部選択") #選択した学部のコンボボックス
undergraduate_combobox.place(x=130, y=50) #学部のコンボボックスを配置


def make_error(contents): #エラーを表示する関数
    tk.messagebox.showerror("エラー", contents, parent=root)

def close_root_window(): #ログアウト画面を閉じようとした場合の処理
    if btn_select_undergraduate['state'] == "disabled" and open_result.poll() == None: #学部選択ボタンが無効の場合(つまりログインしている状態の場合)かつ、アプリケーションが起動している場合
        make_error("アプリケーションを終了させた後に\nログアウトしてください") #ログアウトするように注意する(ログアウトしなければ終了できない)
    elif btn_select_undergraduate['state'] == "disabled": #学部選択ボタンが無効の場合(つまりログインしている状態の場合)
        make_error("ログアウトしてください") #ログアウトするように注意する(ログアウトしなければ終了できない)
    else:
        root.destroy() #ログイン、ログアウト画面を閉じる

def switch_button_state(widget): #ウィジェットを無効化する関数
    widget['state'] = "disabled"

def select_undergraduate(): #学部選択ボタンを押した際、以下のことが実行される
    global selected_undergraduate
    selected_undergraduate = undergraduate_combobox.get() #選択した学部を取得
    global lab_list
    global use_excel_file
    use_excel_file = "used_data_education.xlsx"
    if not selected_undergraduate: #学部を選択していない場合
        lab_list = None
        make_error("学部を選択してください")
    else:
        info.offer_lab_list(selected_undergraduate) #選択した学部の研究室情報を取得
        lab_list = info.choices_lab

    if selected_undergraduate: #学部を選択している場合のみ以下の処理を行う
        global lab_combobox
        lab_combobox = tk.ttk.Combobox(state="readonly", values=lab_list, text="研究室選択") #選択した学部の研究室一覧が出るコンボボックス
        lab_combobox.place(x=130, y=90) #研究室一覧のコンボボックスを配置

        def select_lab(): #研究室・ゼミ選択ボタンを押した際、以下のことが実行される
            global selected_lab
            selected_lab = lab_combobox.get() #選択した研究室を取得
            if not selected_lab: #研究室・ゼミを選択していない場合
                make_error("研究室・ゼミを選択してください")
            else: #研究室・ゼミを選択している場合
                tk.messagebox.showinfo("研究室・ゼミ名 選択完了", "研究室・ゼミを選択しました", parent=root)

        global btn_select_lab
        label_lab = tk.Label(text="研究室・ゼミ : ")
        label_lab.place(x=50, y=90)
        btn_select_lab = tk.Button(text="研究室・ゼミを選択",command=select_lab) #研究室・ゼミ選択のボタンを生成
        btn_select_lab.place(x=300, y=90) #研究室・ゼミ選択のボタンを配置

label_undergraduate = tk.Label(text="学部 : ")
label_undergraduate.place(x=85, y=50)
btn_select_undergraduate = tk.Button(text='学部を選択', command=select_undergraduate) #学部選択のボタンを生成
btn_select_undergraduate.place(x=300, y=50) #学部選択のボタンを配置

now_time = datetime.datetime.now()
display_now_time = str(now_time.year) + "年" + str(now_time.month) + "月" + str(now_time.day) + "日\n" + str(now_time.hour) + "時" + str(now_time.minute) + "分" + str(now_time.second) + "秒"
label_time = tk.Label(root,text="現在の時刻 : ")
label_time.place(x=260, y=240)
label_now_time = tk.Label(root,text=display_now_time)
label_now_time.place(x=340, y=240)

#以下IDとパスワードの扱い
label_id = tk.Label(root, text="ユーザーID : ")
label_id.place(x=50,y=150) #ユーザーIDの位置の指定
txt_id = tk.Entry(width=30) #ユーザーIDの入力欄
txt_id.place(x=130,y=150) #ユーザーID入力欄の位置の指定

label_password = tk.Label(root, text="パスワード : ")
label_password.place(x=50, y=190) #パスワードの位置指定
txt_password = tk.Entry(width=30, show='*') #パスワードの入力欄
txt_password.place(x=130, y=190) #パスワードの入力欄の位置の指定


def login(): #ログインボタンを押した際、以下のことが実行される
    global input_ID
    input_ID = txt_id.get() #ユーザーIDを取得して変数に代入
    input_password = txt_password.get() #パスワードを取得して変数に代入
    global start_using_datetime, open_result, user_name, user_name_ruby

    if not input_ID and input_password: #IDを入力していない場合
        make_error("IDを入力してください")
    elif not input_password and input_ID: #パスワードを入力していない場合
        make_error("パスワードを入力してください")
    elif not input_ID and not input_password: #ID、パスワードどちらも入力していない場合
        make_error("IDおよびパスワードを入力してください")
    elif not selected_lab:
        make_error("研究室・ゼミを選択してください")
    elif selected_lab not in lab_list: #選択した研究室・ゼミが選択した学部の研究室一覧に含まれない場合
        make_error("選択した学部と研究室・ゼミが一致していません")
    else:
        #ログイン認証を行う
        exist_id = conid.exist_id(input_ID, selected_undergraduate, selected_lab) #IDが存在しない場合、Falseを代入
        certification = celog.login_certification(input_ID, input_password, selected_undergraduate, selected_lab) #IDとパスワードが一致しない場合、Falseを代入
        if exist_id == False: #入力したIDが存在しない場合
            make_error("IDが存在しません")
        elif certification == False: #ログイン認証できなかった場合
            make_error("IDとパスワードが一致しません")
        else:
            user_name = celog.name #ログインした人の名前を取得
            user_name_ruby = celog.name_ruby #ログインした人の名前のフリガナを取得
            #任意のアプリケーションの絶対パスを入力(先頭の"r"を忘れないこと)
            app_path =r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            try: #外部アプリを起動
                open_result = subprocess.Popen(app_path, shell=True)
            except subprocess.CalledProcessError:
                make_error("アプリケーションの実行に失敗しました")
            start_using_datetime = datetime.datetime.now() #ログインした日時を取得
            display_start_using_date = str(start_using_datetime.year) + '年' + str(start_using_datetime.month) + '月' + str(start_using_datetime.day) + '日' #使用開始の年月日
            display_start_using_time = str(start_using_datetime.hour) + '時' + str(start_using_datetime.minute) + '分' + str(start_using_datetime.second) + '秒' #使用開始の時間

            tk.messagebox.showinfo("ログイン完了", display_start_using_date + "　" + display_start_using_time + "\nログインしました", parent=root) #ログイン完了の画面、日時を表示する
            btn_login.destroy() #「ログイン」ボタンを消す
            btn_new_registration.destroy() #「新規登録」ボタンを消す

            switch_button_state(undergraduate_combobox) #学部選択のコンボボックスを無効化
            switch_button_state(lab_combobox) #研究室・ゼミ選択のコンボボックスを無効化
            switch_button_state(txt_id) #IDの入力欄を無効化
            switch_button_state(txt_password) #パスワードの入力欄を無効化
            switch_button_state(btn_select_undergraduate) #学部選択ボタンを無効化
            switch_button_state(btn_select_lab) #研究室・ゼミ選択ボタンを無効化

def logout(): #ログアウトボタンを押した際、以下のことが実行される
    if open_result.poll() == None: #アプリケーションを終了せずにログアウトしようとした場合
        make_error("アプリケーションを終了してください") #エラーメッセージを表示する
    else:
        finish_using_datetime = datetime.datetime.now() #ログアウトした日時を取得
        using_time = finish_using_datetime - start_using_datetime #使用時間を計算
        using_second_time = using_time.seconds #使用時間を秒単位に変換
        display_using_minute_time = math.floor(using_second_time / 60) #使用時間を分単位に変換(小数点以下は切り捨て)
        display_using_second_time = math.fmod(using_second_time, 60) #使用時間(分)を60で割る

        tk.messagebox.showinfo("ログアウト完了", "ログアウトしました\n" + str(display_using_minute_time) + " 分" + str(display_using_second_time) + " 秒使用しました", parent=root) #ログアウト完了、使用時間を知らせる画面を表示
        root.destroy() #メイン画面を消す

        #備考記入を表示、DBへの記録
        memo.memo(selected_undergraduate, selected_lab, input_ID, user_name, user_name_ruby, start_using_datetime, finish_using_datetime, using_second_time)

btn_logout = tk.Button(text="ログアウト", command=logout, bg='skyblue',height=2, width=7) #ログアウトボタンの生成
btn_logout.place(x=180, y=240) #ログアウトボタンの配置
btn_login = tk.Button(text='ログイン', command=login, bg='red',height=2, width=7) #ログインボタンの生成
btn_login.place(x=180, y=240) #ログインボタンの位置の指定
btn_new_registration = tk.Button(text="新規登録", command=registrate, bg='green', height=2, width=7) #新規登録ボタンを生成
btn_new_registration.place(x=40, y=240) #新規登録ボタンを配置

root.protocol('WM_DELETE_WINDOW', close_root_window) #ログアウト画面を閉じようとした際、ログアウトするよう注意する
root.mainloop() #持続的に表示しておく
