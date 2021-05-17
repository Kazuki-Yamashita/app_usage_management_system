import generate_widget as genWid #ウィジェット生成するモジュール

#使用歴検索画面において、文字を表示する処理
def indicate_strings(window):
    genWid.generate_label_widget(window, "学部 : ", 60, 20)
    genWid.generate_label_widget(window, "研究室・ゼミ : ", 25, 60)
    genWid.generate_label_widget(window, "検索期間 : ", 40, 100)
    genWid.generate_label_widget(window, "検索開始 年月日 : ", 20, 160)
    genWid.generate_label_widget(window, "検索終了 年月日 : ", 20, 220)
    genWid.generate_label_widget(window, "年", 195, 160)
    genWid.generate_label_widget(window, "月", 305, 160)
    genWid.generate_label_widget(window, "日", 415, 160)
    wave_line_label = genWid.generate_label_widget(window, "↓", 260, 185)
    wave_line_label["font"] = 30
    genWid.generate_label_widget(window, "年", 195, 220)
    genWid.generate_label_widget(window, "月", 305, 220)
    genWid.generate_label_widget(window, "日", 415, 220)
    genWid.generate_label_widget(window,
    "※「検索」ボタンを押すと\n　ダイアログボックスが表示されます", 270, 260)

    #以下、前述の処理をfor文を利用して書いたもの
    """
    str_lab = ["研究室・ゼミ : ", 25, 60]
    str_search_span = ["検索期間 : ", 40, 100]
    str_search_start = ["検索開始 年月日 : ", 20, 160]
    str_search_finish = ["検索終了 年月日 : ", 20, 220]
    str_start_year = ["年", 195, 160]
    str_start_month = ["月", 305, 160]
    str_start_day = ["日", 415, 160]
    str_finish_year = ["年", 195, 220]
    str_finish_month = ["月", 305, 220]
    str_finish_day = ["日", 415, 220]
    str_btn_info = ["※「検索」ボタンを押すと\n　ダイアログボックスが表示されます", 270, 260]


    str_list = [str_lab, str_search_span, str_search_start, str_search_finish,
     str_start_year, str_start_month, str_start_day,
      str_finish_year, str_finish_month, str_finish_day, str_btn_info]

    for list in str_list:
        genWid.generate_label_widget(window, list[0], list[1], list[2])

    wave_line_label = genWid.generate_label_widget(search_used_data_window, "↓", 260, 185)
    wave_line_label["font"] = 30"""
