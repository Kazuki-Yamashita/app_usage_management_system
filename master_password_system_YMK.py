import tkinter as tk #GUI作成のためのライブラリ
import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import usage_management_system_base_infomation_YMK as info #基本情報を含むモジュール
import delete_lab_system_YMK as delLab #研究室・ゼミを削除するモジュール
import change_master_password_system_YMK as chaPass #マスターパスワードの変更を行うモジュール

def make_error(contents): #エラーを表示する関数
    tk.messagebox.showerror("エラー",contents, parent=master_window)

def master(master_function):
    global master_window
    master_window = tk.Tk()
    master_window.title("マスターパスワード ログイン画面")
    master_window.geometry('350x217')

    password_label = tk.Label(master_window, text="マスターパスワード : ")
    password_label.place(x=20, y=30)
    input_password = tk.Entry(master_window, width=30, show='*')
    input_password.place(x=120, y=33)

    def login_master(): #「マスターログイン」ボタンを押した際の処理
        input_master_password = input_password.get() #入力したパスワードを取得
        info.offer_master_password() #設定されているマスターパスワードを取得
        try:
            login_master_password = info.master_password_list[0] #登録されているマスターパスワードを取得
        except: #初回のみ
            login_master_password = "master_initial-password_YMK"

        if input_master_password == login_master_password: #入力したマスターパスワードが正しい場合
            tk.messagebox.showinfo("マスターログイン 完了", "マスターパスワードでログインしました！", parent=master_window)
            master_window.destroy()
            if master_function == "del_lab": #使用する機能が、研究室・ゼミの削除の場合
                delLab.delete_lab() #研究室・ゼミの削除画面を表示
            if master_function == "change_master_password": #使用する機能が、マスターパスワードの変更の場合
                chaPass.change_master_password(login_master_password) #マスターパスワードの変更画面を表示
        else:
            make_error("マスターパスワードが違います")
            return

    btn_login = tk.Button(master_window, text="マスターログイン", command=login_master, height=2, width=10) #検索ボタンの生成
    btn_login.place(x=140, y=120) #検索ボタンの配置

    master_window.mainloop() #表示
