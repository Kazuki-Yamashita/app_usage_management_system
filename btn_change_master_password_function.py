import change_master_password_in_DB as chaPassDB
import show_message as mes #メッセージボックスを表示するモジュール


#マスターパスワードの変更ボタンを押した際の処理
def conn_change_master_password(
window, previous_master_password, new_password, confirm_password):

    #新しいマスターパスワードを取得
    new_master_password = new_password.get()
    #新しいマスターパスワード(確認用)を取得
    new_confirm_master_password = confirm_password.get()

    #新しいマスターパスワードと確認用が異なる場合
    if new_master_password != new_confirm_master_password:
        mes.error("新しく設定するマスターパスワードが、確認用と一致していません", window)
        return

    #新しく設定するマスターパスワードが25文字以下の場合
    elif len(new_master_password) < 25:
        mes.error("設定するマスターパスワードは、25文字以上にしてください", window)
        return
    else:
        #マスターパスワード変更の確認画面を表示
        change_master_password_confirm = mes.askokcancel(
         "マスターパスワード変更 確認画面", "本当にマスターパスワードを変更しますか？",
          window)

        #「OK」を押した場合
        if change_master_password_confirm:
            #DBのマスターパスワードを変更する
            change_master_password_ornot = chaPassDB.change_master_password_DB(
             previous_master_password, new_master_password)

            #マスターパスワードの変更に失敗した場合
            if not change_master_password_ornot:
                mes.error("マスターパスワードの変更に失敗しました", window)
                return
            #成功した場合
            else:
                mes.info("マスターパスワード 変更完了", "マスターパスワードを変更しました", window)
                window.destroy()
