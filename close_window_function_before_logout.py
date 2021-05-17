import show_message as mes #メッセージボックスを表示するモジュール

#ログアウト画面を閉じようとした場合の処理
def close_root_window(btn_select_undergraduate, open_result, root):
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
