import datetime #日時を取得するライブラリ
import generate_widget as genWid #ウィジェット生成するモジュール

#現在の日時を表示する関数
def now_time(window, string, str_x, str_y, time_x, time_y):
    now_time = datetime.datetime.now()
    display_now_time = (str(now_time.year) + "年" + str(now_time.month) + "月" + str(now_time.day) +
     "日\n" + str(now_time.hour) + "時" + str(now_time.minute) + "分")
    #文字を表示
    genWid.generate_label_widget(window, string, str_x, str_y)
    #時刻を表示
    genWid.generate_label_widget(window, display_now_time, time_x, time_y)
