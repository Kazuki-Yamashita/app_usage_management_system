import tkinter as tk #GUI作成のためのライブラリ
import usage_management_system_base_infomation as info #基本情報を含むモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール
import btn_select_undergraduate_function as btnUnder #学部選択ボタンを押した際に実行される処理
import radio_button_command_in_search_usage_data as rdBtnCom #使用歴検索のラジオボタンのコマンドを記述
import btn_search_usage_data as btnSeaData #使用歴検索の検索ボタンのコマンドを記述
import generate_strings_in_search_usage_data as indiStr #文字を表示する処理をまとめて記述

#メニューバーから「使用履歴の検索」を選択した際の処理
def search_used_data():
    search_used_data_window = mw.make_window("使用履歴 検索画面", '500x310')

    #学部の文字とコンボボックスを生成
    search_lab_undergraduate_combobox = genWid.generate_combobox_widget(
        search_used_data_window, "readonly", info.undergraduate_list, "学部選択", 110, 20)

    #文字を表示
    indiStr.indicate_strings(search_used_data_window)

    #月、日の選択肢を設定
    choice_month = list(range(1,13))
    choice_day = list(range(1,32))

    #年月日の選択欄を生成
    spin_start_year = genWid.generate_spinbox_widget(search_used_data_window, "disabled",
     2021, 2100, 1, 130, 160, 60)
    combo_start_month = genWid.generate_combobox_widget(
        search_used_data_window, "disabled", choice_month, "開始月", 240, 160, 6)
    combo_start_day = genWid.generate_combobox_widget(
        search_used_data_window, "disabled", choice_day, "開始日", 350, 160, 6)

    spin_finish_year = genWid.generate_spinbox_widget(search_used_data_window, "disabled",
     2021, 2100, 1, 130, 220, 60)
    combo_finish_month = genWid.generate_combobox_widget(
        search_used_data_window, "disabled", choice_month, "終了月", 240, 220, 6)
    combo_finish_day = genWid.generate_combobox_widget(
        search_used_data_window, "disabled", choice_day, "終了日", 350, 220, 6)

    #期間指定の有無を調べる
    val = tk.StringVar(master=search_used_data_window)
    val.set("no")

    #「期間を指定しない」ラジオボタンの生成、配置、コマンド指定
    rb_not_designate = tk.Radiobutton(search_used_data_window, variable=val, value="no",
     text='期間を指定しない(すべての使用歴を検索)')
    rb_not_designate.place(x=120, y=100)
    rb_not_designate["command"] = lambda: rdBtnCom.designate_search_span("not_disignate",
     spin_start_year, combo_start_month, combo_start_day,
     spin_finish_year, combo_finish_month, combo_finish_day)

    #「期間を指定する」ラジオボタンの生成、配置、コマンド指定
    rb_designate = tk.Radiobutton(search_used_data_window, variable=val, value="yes", text='期間を指定する')
    rb_designate.place(x=120, y=130)
    rb_designate["command"] = lambda: rdBtnCom.designate_search_span("disignate",
     spin_start_year, combo_start_month, combo_start_day,
     spin_finish_year, combo_finish_month, combo_finish_day)

    #学部選択ボタンの生成、配置、コマンド指定
    btn_search_name_undergraduate = tk.Button(search_used_data_window, text='学部の研究室・ゼミを表示')
    btn_search_name_undergraduate.place(x=300, y=20)
    btn_search_name_undergraduate["command"] = lambda: btnUnder.select_undergraduate(
    search_lab_undergraduate_combobox, search_used_data_window, 110, 60)

    #検索ボタンの生成、配置、コマンド指定
    btn_exe_search = tk.Button(search_used_data_window, text="検索", height=2, width=7)
    btn_exe_search.place(x=210, y=260)
    btn_exe_search["command"] = lambda: btnSeaData.btn_search_usage_data(search_used_data_window,
     search_lab_undergraduate_combobox, val, spin_start_year, combo_start_month, combo_start_day,
      spin_finish_year, combo_finish_month, combo_finish_day)

    search_used_data_window.mainloop()
