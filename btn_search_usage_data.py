import datetime
import usage_management_system_base_infomation as info #基本情報を含むモジュール
import create_table_of_used_data as creTable #使用歴の表を作成するモジュール
import btn_select_undergraduate_function as btnUnder #学部選択ボタンを押した際に実行される処理
import is_correct_datetime as isCorDate #年月日の入力が適切かどうか判定するモジュール
import show_message as mes #メッセージボックスを表示するモジュール

#使用履歴検索の検索ボタンを押した際の処理
def btn_search_usage_data(window, undergraduate_combobox, select_radiobutton,
 spin_start_year, combo_start_month, combo_start_day, spin_finish_year,
  combo_finish_month, combo_finish_day):

    #選択した学部を取得
    search_usage_data_undergraduate = undergraduate_combobox.get()
    #選択した学部の研究室一覧を取得(リスト)
    lab_list = info.offer_lab_list(search_usage_data_undergraduate)


    #学部を選択していない場合
    if not search_usage_data_undergraduate:
        mes.error("学部を選択してください", window)
        return

    try: #研究室のコンボボックスが表示されていない状態で検索ボタンを押したか判定
        btnUnder.search_usage_data_lab_list
    except:
        mes.error("研究室・ゼミを選択してください", window)
        return

    #検索する研究室を取得
    search_usage_data_lab = btnUnder.lab_combobox_search_usage_data.get()

    #以下、ファイル分け可能
    #研究室のコンボボックスが表示されているが、選択せずに検索ボタンを押した場合
    if not search_usage_data_lab:
        mes.error("研究室・ゼミを選択してください", window)
        return

    #選択した学部と研究室・ゼミが一致しない場合
    if search_usage_data_lab not in lab_list:
        mes.error("選択した学部と研究室・ゼミが一致していません", window)
        return

    desig_ornot = select_radiobutton.get() #選択しているラジオボタンを取得

    #期間を指定している場合
    if desig_ornot == "yes":
        #入力した年月日が適切かどうか判定
        datetime_result = isCorDate.is_correct_datetime(window,
         spin_start_year, combo_start_month, combo_start_day,
         spin_finish_year, combo_finish_month, combo_finish_day)

        #入力が適切でない場合、処理を中断
        if not datetime_result:
            return

        #検索期間の開始日と終了日を取得
        search_start_time = datetime_result[0]
        search_finish_time = datetime_result[1]

    #期間を指定していない場合
    else: #検索年月日にNoneを代入
        search_start_time = search_finish_time = None

    #選択した研究室の使用履歴を取得
    try:
        used_record = info.offer_used_data(search_usage_data_undergraduate, search_usage_data_lab, desig_ornot,
         search_start_time, search_finish_time)
    except:
        if len(used_record) == 0: #使用歴がない場合
            mes.error("使用歴がありません", window)
            return
        else: #何らかの理由で検索できなかった場合
            mes.error("使用歴の検索に失敗しました", window)
            return

    #使用歴をcsvで出力
    try: #pandasを用いて使用歴の表を作成
        creTable.create_table(used_record, window)
    except:
        mes.error("CSVを出力できませんでした", window)
