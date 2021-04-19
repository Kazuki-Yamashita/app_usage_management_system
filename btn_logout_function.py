import datetime #日時を取得するライブラリ
import math #数学関数のライブラリ
import show_message as mes #メッセージボックスを表示するモジュール
import memo_system as memo #備考記入、DBへの記録を含むモジュール


def logout(open_result, selected_undergraduate, selected_lab, input_ID, user_name, user_name_ruby, start_using_datetime, root): #ログアウトボタンを押した際、以下のことが実行される
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
