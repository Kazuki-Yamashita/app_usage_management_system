import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import change_master_password_in_DB_YMK as chaPassDB

def make_error(contents): #エラーを表示する関数
    tk.messagebox.showerror("エラー",contents, parent=change_master_password_window)

def change_master_password(login_master_password):
    global change_master_password_window
    change_master_password_window = tk.Tk()
    change_master_password_window.title("マスターパスワード 変更画面")
    change_master_password_window.geometry('360x190')

    new_password_label = tk.Label(change_master_password_window, text="新しいマスターパスワード : ")
    new_password_label.place(x=20, y=30)
    new_input_password = tk.Entry(change_master_password_window, width=30, show='*')
    new_input_password.place(x=150, y=30)

    new_password_confirm_label = tk.Label(change_master_password_window, text="新しいマスターパスワード : \n(確認用)")
    new_password_confirm_label.place(x=20, y=70)
    new_input_confirm_password = tk.Entry(change_master_password_window, width=30, show='*')
    new_input_confirm_password.place(x=150, y=70)

    master_caution = tk.Label(change_master_password_window, text="設定するマスターパスワードは25文字以上にしてください", bg="white")
    master_caution.place(x=20, y=110)

    def conn_change_master_password(): #変更ボタンを押した際の処理
        new_master_password = new_input_password.get() #新しいマスターパスワードを取得
        new_confirm_master_password = new_input_confirm_password.get() #新しいマスターパスワード(確認用)を取得

        if new_master_password != new_confirm_master_password: #新しいマスターパスワードと確認用が異なる場合
            make_error("新しく設定するマスターパスワードが、確認用と一致していません")
            return
        elif len(new_master_password) < 25: #新しく設定するマスターパスワードが25文字以下の場合
            make_error("設定するマスターパスワードは、25文字以上にしてください")
            return
        else:
            change_master_password_confirm = tk.messagebox.askokcancel("マスターパスワード変更 確認画面", "本当にマスターパスワードを変更しますか？", parent=change_master_password_window)
            if change_master_password_confirm == True: #「OK」を押した場合
                change_master_password_ornot = chaPassDB.change_master_password_DB(login_master_password, new_master_password) #DBのマスターパスワードを変更する
                if change_master_password_ornot == False:
                    make_error("マスターパスワードの変更に失敗しました")
                    return
                else:
                    tk.messagebox.showinfo("マスターパスワード 変更完了", "マスターパスワードを変更しました", parent=change_master_password_window)
                    change_master_password_window.destroy()

    btn_change_master_password = tk.Button(change_master_password_window, text="変更する", command=conn_change_master_password, height=2, width=10)
    btn_change_master_password.place(x=150, y=140)

    change_master_password_window.mainloop()
