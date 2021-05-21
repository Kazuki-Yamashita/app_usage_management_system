import tkinter as tk #GUI作成のためのライブラリ
import make_window as mw #ウィンドウを作成するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import usage_management_system_base_infomation as info #基本情報を提供するモジュール
import btn_select_undergraduate_function as btnUnder #研究室表示ボタンを押した際に実行される処理
import btn_search_name #利用者検索の検索ボタンを押した際の処理
import btn_del_search_user_result as btnDelRes #利用者検索の削除ボタンを押した際の処理


#利用者を検索する関数
def search_user_name():
    #ウィンドウの作成
    search_name_window = mw.make_window("登録者 検索画面", '485x400')

    #学部の文字とコンボボックスを生成
    genWid.generate_label_widget(search_name_window, "学部 : ", 85, 20)
    search_user_undergraduate_combobox = genWid.generate_combobox_widget(
        search_name_window, "readonly", info.undergraduate_list, "学部選択", 150, 20)

    #研究室・ゼミの文字を生成
    genWid.generate_label_widget(search_name_window, "研究室・ゼミ : ", 50, 60)
    #表示に関する注意書きを表示
    genWid.generate_label_widget(search_name_window, "※一覧が見切れる場合\n　画面を最大化してください", 20, 100)

    #学部選択のボタンを生成、配置、コマンド指定
    btn_search_user_name_undergraduate = tk.Button(search_name_window,
                                            text='学部の研究室・ゼミを表示', state="normal")
    btn_search_user_name_undergraduate.place(x=320, y=20)
    btn_search_user_name_undergraduate["command"] = lambda: btnUnder.select_undergraduate(
                            search_name_window, "search_user", search_user_undergraduate_combobox, 150, 60)

    #検索ボタンを生成、配置、コマンド指定
    btn_exe_search = tk.Button(search_name_window, text="検索", height=2, width=12, state="normal")
    btn_exe_search.place(x=180, y=100)
    btn_exe_search["command"] = lambda: btn_search_name.btn_search_user_name(search_name_window,
     search_user_undergraduate_combobox, btn_exe_search, btn_search_user_name_undergraduate,
      btnUnder.lab_combobox_search_user, btn_del)

    #検索結果の削除ボタンを生成、配置、コマンド指定
    btn_del = tk.Button(search_name_window, text="検索結果をクリア",
     bg="red", height=2, width=12, state="disabled")
    btn_del.place(x=320, y=100)
    btn_del["command"] = lambda: btnDelRes.btn_del_result(btn_search_name.result_label,
     search_user_undergraduate_combobox, btn_search_user_name_undergraduate,
      btnUnder.lab_combobox_search_user, btn_exe_search, btn_del)

    search_name_window.mainloop()
