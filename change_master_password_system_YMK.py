import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import change_master_password_in_DB_YMK as chaPassDB
import show_message as mes #メッセージボックスを表示するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール


def change_master_password(login_master_password):
    global change_master_password_window
    change_master_password_window = tk.Tk()
    change_master_password_window.title("マスターパスワード 変更画面")
    change_master_password_window.geometry('360x190')

    genWid.generate_label_widget(change_master_password_window, "新しいマスターパスワード : ", 20, 30)
    new_input_password = genWid.generate_entry_widget(change_master_password_window, 30, 150, 30, "*")

    genWid.generate_label_widget(change_master_password_window, "新しいマスターパスワード : \n(確認用)", 20, 70)
    new_input_confirm_password = genWid.generate_entry_widget(change_master_password_window, 30, 150, 70, "*")

    master_caution = genWid.generate_label_widget(change_master_password_window, "設定するマスターパスワードは25文字以上にしてください", 20, 110)
    master_caution["bg"] = "white"

    def conn_change_master_password(): #変更ボタンを押した際の処理
        new_master_password = new_input_password.get() #新しいマスターパスワードを取得
        new_confirm_master_password = new_input_confirm_password.get() #新しいマスターパスワード(確認用)を取得

        if new_master_password != new_confirm_master_password: #新しいマスターパスワードと確認用が異なる場合
            mes.error("新しく設定するマスターパスワードが、確認用と一致していません", change_master_password_window)
            return
        elif len(new_master_password) < 25: #新しく設定するマスターパスワードが25文字以下の場合
            mes.error("設定するマスターパスワードは、25文字以上にしてください", change_master_password_window)
            return
        else:
            #マスターパスワード変更の確認画面
            change_master_password_confirm = mes.askokcancel("マスターパスワード変更 確認画面", "本当にマスターパスワードを変更しますか？", change_master_password_window)
            if change_master_password_confirm == True: #「OK」を押した場合
                #DBのマスターパスワードを変更する
                change_master_password_ornot = chaPassDB.change_master_password_DB(login_master_password, new_master_password)
                if change_master_password_ornot == False:
                    mes.error("マスターパスワードの変更に失敗しました", change_master_password_window)
                    return
                else:
                    mes.info("マスターパスワード 変更完了", "マスターパスワードを変更しました", change_master_password_window)
                    change_master_password_window.destroy()

    btn_change_master_password = tk.Button(change_master_password_window, text="変更する", command=conn_change_master_password, height=2, width=10)
    btn_change_master_password.place(x=150, y=140)

    change_master_password_window.mainloop()
