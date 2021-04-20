import show_message as mes #メッセージボックスを表示するモジュール
import used_data_registration_system as regUsed #使用歴をDBに記録するモジュール


#「記入終了」ボタンを押した際に実行される関数
def btn_memo_finish(window, input_memo, var, undergraduate, lab, id,
 user_name, user_name_ruby, start_using_datetime, finish_using_datetime, using_second_time):
    #どのラジオボタンがチェックされているかを取得
    checked_btn = var.get()
    memo_confirmation = False #初期値を設定

    #メモの入力とラジオボタンの選択が適切か判定
    if checked_btn == "OK" and input_memo.get("1.0","end-1c"):
        mes.error("異常がない場合、テキストを削除してください", window)
    elif checked_btn == "not_OK" and not input_memo.get("1.0","end-1c"):
        mes.error("不具合があった場合、内容を記述してください", window)
    else: #適切な場合
        #メモ記入の最終確認画面を表示
        memo_confirmation = mes.askokcancel("メモ最終確認", "これで記入しますか？", window)

    if memo_confirmation: #「OK」を選択した場合(True)
        memo = input_memo.get("1.0","end-1c") #メモの内容を取得

        try: #DBへ記録
            regUsed.used_data_registration(undergraduate, lab, id,
             user_name, user_name_ruby, start_using_datetime, finish_using_datetime,
              using_second_time, memo)
            mes.info("使用歴 記録完了","記録が完了しました", window)
            window.destroy() #備考記入画面を閉じる

        except: #何らかの理由で記録できなかった場合
            mes.error("使用歴を記録できませんでした。", window)
            return
