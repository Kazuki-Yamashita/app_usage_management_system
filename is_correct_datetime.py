import datetime
import show_message as mes #メッセージボックスを表示するモジュール

#使用歴検索おいて、年月日の入力が適切かどうか判定する関数
def is_correct_datetime(window, spin_start_year, combo_start_month, combo_start_day,
 spin_finish_year, combo_finish_month, combo_finish_day):

    #各入力欄に入力された文字をリスト化(for文で使用するため)
    datetime_int_list = [spin_start_year, combo_start_month, combo_start_day,
     spin_finish_year, combo_finish_month, combo_finish_day]

    #年月日の入力が適切かどうか判定(不適切ならFalse)
    for int_list in datetime_int_list:
        try:
            is_int = int(int_list.get())
        except:
            mes.error("年月日に不適切な入力があります！", window)
            return False

    #入力された文字を数値型に変換して取得
    search_start_year = int(spin_start_year.get())
    search_start_month = int(combo_start_month.get())
    search_start_day = int(combo_start_day.get())
    search_finish_year = int(spin_finish_year.get())
    search_finish_month = int(combo_finish_month.get())
    search_finish_day = int(combo_finish_day.get())

    td_1d = datetime.timedelta(days=1) #1日分の時間をリストに格納

    #検索開始の年月日が存在するか判定
    try:
        start_time = datetime.datetime(search_start_year,
         search_start_month, search_start_day)
    except: #日付が存在しない場合
        mes.error("検索開始の日時が存在しません", window)
        return False

    #検索終了の年月日が存在するか判定
    try:
        finish_time = datetime.datetime(search_finish_year, search_finish_month,
         search_finish_day)
    except: #日付が存在しない場合
        mes.error("検索終了の日時が存在しません", window)
        return False

    #検索期間が逆転している場合(検索開始日時が検索終了日時よりも後の場合)
    if start_time > finish_time:
        mes.error("検索期間が適切ではありません", window)
        return False

    #検索終了期間に1日分追加して更新
    finish_time = finish_time + td_1d

    return start_time, finish_time
