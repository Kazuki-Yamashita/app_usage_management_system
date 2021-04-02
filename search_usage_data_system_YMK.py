import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import datetime
import usage_management_system_base_infomation_YMK as info #基本情報を含むモジュール
import create_table_of_used_data_YMK as table #使用歴の表を作成するモジュール

def make_error(contents): #エラーを表示する関数
    tk.messagebox.showerror("エラー",contents, parent=search_used_data_window)

def search_used_data():
    global search_used_data_window
    search_used_data_window = tk.Tk()
    search_used_data_window.title("使用履歴 検索画面")
    search_used_data_window.geometry('500x310')

    label_undergraduate = tk.Label(search_used_data_window, text="学部 : ")
    label_undergraduate.place(x=60, y=20)
    search_lab_undergraduate_combobox = tk.ttk.Combobox(search_used_data_window,state="readonly", values=info.undergraduate_list, text="学部選択") #選択した学部のコンボボックス
    search_lab_undergraduate_combobox.place(x=110, y=20) #学部のコンボボックス

    def select_search_usage_data_undergraduate(): #学部選択ボタンを押した際の処理
        global btn_del, search_undergraduate, lab_combobox, search_lab_list, btn_exe_search
        search_undergraduate = search_lab_undergraduate_combobox.get() #検索する学部を取得
        if not search_undergraduate: #学部を選択していない場合
            make_error("学部を選択してください")
            return
        else:
            info.offer_lab_list(search_undergraduate, "usage data") #選択した学部の研究室情報を取得
            search_lab_list = info.choices_lab #研究室リストを代入

        label_lab = tk.Label(search_used_data_window, text="研究室・ゼミ : ")
        label_lab.place(x=25, y=60)
        lab_combobox = tk.ttk.Combobox(search_used_data_window, state="readonly", values=search_lab_list, text="研究室選択") #選択した学部の研究室一覧が出るコンボボックス
        lab_combobox.place(x=110, y=60) #研究室一覧のコンボボックスを配置

        label_time = tk.Label(search_used_data_window, text="検索期間 : ")
        label_time.place(x=40, y=100)

        choice_month = list(range(1,13))
        choice_day = list(range(1,32))

        spin_start_year = tk.ttk.Spinbox(search_used_data_window, state="disabled", from_=2021, to=2100, increment=1)
        spin_start_year.place(x=130, y=160, width=60)
        combo_start_month = tk.ttk.Combobox(search_used_data_window, state="disabled", values=choice_month)
        combo_start_month.place(x=240, y=160, width=60)
        combo_start_day = tk.ttk.Combobox(search_used_data_window, state="disabled", values=choice_day)
        combo_start_day.place(x=350, y=160, width=60)
        spin_finish_year = tk.ttk.Spinbox(search_used_data_window, state="disabled", from_=2021, to=2100, increment=1)
        spin_finish_year.place(x=130, y=220, width=60)
        combo_finish_month = tk.ttk.Combobox(search_used_data_window, state="disabled", values=choice_month)
        combo_finish_month.place(x=240, y=220, width=60)
        combo_finish_day = tk.ttk.Combobox(search_used_data_window, state="disabled", values=choice_day)
        combo_finish_day.place(x=350, y=220, width=60)

        start_label = tk.Label(search_used_data_window, text="検索開始 年月日 : ")
        start_label.place(x=20, y=160)
        finish_label = tk.Label(search_used_data_window, text="検索終了 年月日 : ")
        finish_label.place(x=20, y=220)
        label_year_start = tk.Label(search_used_data_window, text="年")
        label_year_start.place(x=195, y=160)
        label_month_start = tk.Label(search_used_data_window, text="月")
        label_month_start.place(x=305, y=160)
        label_day_start = tk.Label(search_used_data_window, text="日")
        label_day_start.place(x=415, y=160)
        wave_line_label = tk.Label(search_used_data_window, text="↓", font=(30))
        wave_line_label.place(x=260, y=185)
        label_year_finish = tk.Label(search_used_data_window, text="年")
        label_year_finish.place(x=195, y=220)
        label_month_finish = tk.Label(search_used_data_window, text="月")
        label_month_finish.place(x=305, y=220)
        label_day_finish = tk.Label(search_used_data_window, text="日")
        label_day_finish.place(x=415, y=220)

        global desig_ornot

        def desig_off(): #期間を指定していない場合
            #年月日を指定するウィジェットを無効化
            spin_start_year['state'] = 'disabled'
            combo_start_month['state'] = 'disabled'
            combo_start_day['state'] = 'disabled'
            spin_finish_year['state'] = 'disabled'
            combo_finish_month['state'] = 'disabled'
            combo_finish_day['state'] = 'disabled'

        def desig_on(): #期間を指定する場合
            #年月日を指定するウィジェットを有効化
            spin_start_year['state'] = 'normal'
            combo_start_month['state'] = 'readonly'
            combo_start_day['state'] = 'readonly'
            spin_finish_year['state'] = 'normal'
            combo_finish_month['state'] = 'readonly'
            combo_finish_day['state'] = 'readonly'

        val = tk.StringVar(master=search_used_data_window) #期間指定の有無を調べる
        val.set("no")
        rb_not_designate = tk.Radiobutton(search_used_data_window, variable=val, value="no", text='期間を指定しない(すべての使用歴を検索)', command=desig_off)
        rb_not_designate.place(x=120, y=100)
        rb_designate = tk.Radiobutton(search_used_data_window, variable=val, value="yes", text='期間を指定する', command=desig_on)
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
                    make_error("検索開始の日時が存在しません")
                    return

                try: #検索終了の年月日を日付に変換
                    search_finish_time = datetime.datetime(search_finish_year, search_finish_month, search_finish_day)
                    search_finish_time = search_finish_time + td_1d #検索終了期間に1日分追加して更新
                except:
                    make_error("検索終了の日時が存在しません")
                    return

                if search_start_time > search_finish_time: #検索期間が逆転している場合(検索開始日時が検索終了日時よりも後の場合)
                    make_error("検索期間が適切ではありません")
                    return
            else: #期間を指定していない場合
                search_start_year = search_start_month = search_start_day = search_finish_year = search_finish_month = search_finish_day = search_start_time = search_finish_time = None

            if not searching_lab: #研究室を選択していない場合
                make_error("研究室を選択してください")
            elif searching_lab not in search_lab_list: #選択した学部と研究室・ゼミが一致しない場合
                make_error("選択した学部と研究室・ゼミが一致していません")
            else:
                try: #選択した研究室の使用履歴を取得(info の、usage_record_list に使用歴が格納される)
                    info.offer_used_data(search_undergraduate, searching_lab, desig_ornot, search_start_time, search_finish_time)
                except:
                    if len(info.usage_record_list) == 0: #使用歴がない場合
                        make_error("使用歴がありません")
                        return
                    else: #何らかの理由で検索できなかった場合
                        make_error("使用歴の検索に失敗しました")
                        return

                try: #使用歴をcsvで出力
                    table.create_table(info.usage_record_list)
                except:
                    make_error("CSVを出力できませんでした")

        btn_exe_search = tk.Button(search_used_data_window, text="検索", command=search_name, height=2, width=7) #検索ボタンの生成
        btn_exe_search.place(x=210, y=260) #検索ボタンの配置
        caution_label = tk.Label(search_used_data_window, text="※「検索」ボタンを押すと\n　ダイアログボックスが表示されます")
        caution_label.place(x=270, y=260)

    btn_search_name_undergraduate = tk.Button(search_used_data_window,text='学部を選択',command=select_search_usage_data_undergraduate) #学部選択のボタンを生成
    btn_search_name_undergraduate.place(x=300, y=20) #学部選択のボタンを配置

    search_used_data_window.mainloop()
