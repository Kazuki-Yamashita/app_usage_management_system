import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import datetime
import usage_management_system_base_infomation as info #基本情報を含むモジュール
import create_table_of_used_data as creTable #使用歴の表を作成するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import convert_widget_state as conWid #ウィジェットを無効化するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール


def search_used_data():
    search_used_data_window = mw.make_window("使用履歴 検索画面", '500x310')

    genWid.generate_label_widget(search_used_data_window, "学部 : ", 60, 20)
    search_lab_undergraduate_combobox = genWid.generate_combobox_widget(
        search_used_data_window, "readonly", info.undergraduate_list, "学部選択", 110, 20)

    def select_search_usage_data_undergraduate(): #学部選択ボタンを押した際の処理
        global btn_del, search_undergraduate, lab_combobox, search_lab_list, btn_exe_search
        search_undergraduate = search_lab_undergraduate_combobox.get() #検索する学部を取得
        if not search_undergraduate: #学部を選択していない場合
            mes.error("学部を選択してください", search_used_data_window)
            return
        else:
            info.offer_lab_list(search_undergraduate, "usage data") #選択した学部の研究室情報を取得
            search_lab_list = info.choices_lab #研究室リストを代入

        genWid.generate_label_widget(search_used_data_window, "研究室・ゼミ : ", 25, 60)
        lab_combobox = genWid.generate_combobox_widget(
            search_used_data_window, "readonly", search_lab_list, "研究室選択", 110, 60)

        genWid.generate_label_widget(search_used_data_window, "検索期間 : ", 40, 100)

        choice_month = list(range(1,13))
        choice_day = list(range(1,32))

        spin_start_year = genWid.generate_spinbox_widget(search_used_data_window, "disabled", 2021, 2100, 1, 130, 160, 60)
        combo_start_month = genWid.generate_combobox_widget(
            search_used_data_window, "disabled", choice_month, "開始月", 240, 160, 6)
        combo_start_day = genWid.generate_combobox_widget(
            search_used_data_window, "disabled", choice_day, "開始日", 350, 160, 6)

        spin_finish_year = genWid.generate_spinbox_widget(search_used_data_window, "disabled", 2021, 2100, 1, 130, 220, 60)
        combo_finish_month = genWid.generate_combobox_widget(
            search_used_data_window, "disabled", choice_month, "終了月", 240, 220, 6)
        combo_finish_day = genWid.generate_combobox_widget(
            search_used_data_window, "disabled", choice_day, "終了日", 350, 220, 6)

        genWid.generate_label_widget(search_used_data_window, "検索開始 年月日 : ", 20, 160)
        genWid.generate_label_widget(search_used_data_window, "検索終了 年月日 : ", 20, 220)
        genWid.generate_label_widget(search_used_data_window, "年", 195, 160)
        genWid.generate_label_widget(search_used_data_window, "月", 305, 160)
        genWid.generate_label_widget(search_used_data_window, "日", 415, 160)
        wave_line_label = genWid.generate_label_widget(search_used_data_window, "↓", 260, 185)
        wave_line_label["font"] = 30
        genWid.generate_label_widget(search_used_data_window, "年", 195, 220)
        genWid.generate_label_widget(search_used_data_window, "月", 305, 220)
        genWid.generate_label_widget(search_used_data_window, "日", 415, 220)

        global desig_ornot

        def desig_off(): #期間を指定していない場合
            #年月日を指定するウィジェットを無効化
            to_disabled_widget_list = [spin_start_year, combo_start_month, combo_start_day,
             spin_finish_year, combo_finish_month, combo_finish_day]
            conWid.to_disabled_widget(to_disabled_widget_list)

        def desig_on(): #期間を指定する場合
            #年月日を指定するウィジェットを有効化
            to_normal_widget_list = [spin_start_year, spin_finish_year]
            conWid.to_normal_widget(to_normal_widget_list)

            to_readonly_widget_list = [combo_start_month, combo_start_day, combo_finish_month, combo_finish_day]
            conWid.to_readonly_widget(to_readonly_widget_list)

        val = tk.StringVar(master=search_used_data_window) #期間指定の有無を調べる
        val.set("no")

        rb_not_designate = tk.Radiobutton(search_used_data_window, variable=val, value="no",
         text='期間を指定しない(すべての使用歴を検索)', command=desig_off)
        rb_not_designate.place(x=120, y=100)

        rb_designate = tk.Radiobutton(search_used_data_window, variable=val, value="yes",
         text='期間を指定する', command=desig_on)
        rb_designate.place(x=120, y=130)

        def search_name(): #検索ボタンを押した際の処理
            searching_lab = lab_combobox.get() #検索する研究室を取得
            desig_ornot = val.get()
            td_1d = datetime.timedelta(days=1)

            #検索期間の年月日を取得
            if desig_ornot == "yes": #期間を指定している場合、検索期間の年月日を取得
                search_start_year = int(spin_start_year.get())
                search_start_month = int(combo_start_month.get())
                search_start_day = int(combo_start_day.get())
                search_finish_year = int(spin_finish_year.get())
                search_finish_month = int(combo_finish_month.get())
                search_finish_day = int(combo_finish_day.get())

                global search_start_time, search_finish_time

                try: #検索開始の年月日を日付に変換
                    search_start_time = datetime.datetime(search_start_year, search_start_month, search_start_day)
                except:
                    mes.error("検索開始の日時が存在しません", search_used_data_window)
                    return

                try: #検索終了の年月日を日付に変換
                    search_finish_time = datetime.datetime(search_finish_year, search_finish_month, search_finish_day)
                    search_finish_time = search_finish_time + td_1d #検索終了期間に1日分追加して更新
                except:
                    mes.error("検索終了の日時が存在しません", search_used_data_window)
                    return

                if search_start_time > search_finish_time: #検索期間が逆転している場合(検索開始日時が検索終了日時よりも後の場合)
                    mes.error("検索期間が適切ではありません", search_used_data_window)
                    return
            else: #期間を指定していない場合
                search_start_year = search_start_month = search_start_day = search_finish_year = search_finish_month = search_finish_day = search_start_time = search_finish_time = None

            if not searching_lab: #研究室を選択していない場合
                mes.error("研究室を選択してください", search_used_data_window)
            elif searching_lab not in search_lab_list: #選択した学部と研究室・ゼミが一致しない場合
                mes.error("選択した学部と研究室・ゼミが一致していません", search_used_data_window)
            else:
                try: #選択した研究室の使用履歴を取得(info の、usage_record_list に使用歴が格納される)
                    info.offer_used_data(search_undergraduate, searching_lab, desig_ornot, search_start_time, search_finish_time)
                except:
                    if len(info.usage_record_list) == 0: #使用歴がない場合
                        mes.error("使用歴がありません", search_used_data_window)
                        return
                    else: #何らかの理由で検索できなかった場合
                        mes.error("使用歴の検索に失敗しました", search_used_data_window)
                        return

                try: #使用歴をcsvで出力
                    creTable.create_table(info.usage_record_list, search_used_data_window) #pandasを用いて使用歴の表を作成
                except:
                    mes.error("CSVを出力できませんでした", search_used_data_window)

        btn_exe_search = tk.Button(search_used_data_window, text="検索", command=search_name, height=2, width=7) #検索ボタンの生成
        btn_exe_search.place(x=210, y=260) #検索ボタンの配置
        caution_label = tk.Label(search_used_data_window, text="※「検索」ボタンを押すと\n　ダイアログボックスが表示されます")
        caution_label.place(x=270, y=260)

    btn_search_name_undergraduate = tk.Button(search_used_data_window,text='学部を選択',command=select_search_usage_data_undergraduate) #学部選択のボタンを生成
    btn_search_name_undergraduate.place(x=300, y=20) #学部選択のボタンを配置

    search_used_data_window.mainloop()
