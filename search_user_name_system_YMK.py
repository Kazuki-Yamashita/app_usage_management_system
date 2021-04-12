import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import usage_management_system_base_infomation_YMK as info #基本情報を含むモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import disabled_widget as disWid #ウィジェットを無効化するモジュール
import show_message as mes #メッセージボックスを表示するモジュール


def search_user_name(): #利用者の名前を検索する関数
    global search_name_window
    search_name_window = tk.Tk()
    search_name_window.title("登録者 検索画面")
    search_name_window.geometry('485x400')

    genWid.generate_label_widget(search_name_window, "学部 : ", 85, 20)
    #選択した学部のコンボボックス
    search_lab_undergraduate_combobox = genWid.generate_combobox_widget(
        search_name_window, "readonly", info.undergraduate_list, "学部選択", 150, 20)

    def select_search_name_undergraduate(): #学部選択ボタンを押した際の処理
        global btn_del
        try:
            btn_del #削除ボタンが存在する場合
            mes.error("検索結果をクリアしてください", search_name_window)
        except:
            global search_undergraduate, lab_combobox, search_lab_list, btn_exe_search
            search_undergraduate = search_lab_undergraduate_combobox.get() #検索する学部を取得
            if not search_undergraduate: #学部を選択していない場合
                mes.error("学部を選択してください", search_name_window)
                return
            else:
                info.offer_lab_list(search_undergraduate) #選択した学部の研究室情報を取得
                search_lab_list = info.choices_lab #研究室リストを代入

            genWid.generate_label_widget(search_name_window, "研究室・ゼミ : ", 50, 60)
            lab_combobox = genWid.generate_combobox_widget(
                search_name_window, "readonly", search_lab_list, "研究室選択", 150, 60)

        def search_name(): #検索ボタンを押した際の処理
            genWid.generate_label_widget(search_name_window, "※一覧が見切れる場合\n　画面を最大化してください", 20, 100)
            try: #削除ボタンが存在する場合
                btn_del
                mes.error("検索結果をクリアしてください", search_name_window)
            except:
                global display_label
                display_label = None
                btn_exe_search.destroy() #検索ボタンを削除
                display = "" #初期化(空にする)
                search_name_dict = {}
                searching_lab = lab_combobox.get() #検索する研究室を取得

                if not searching_lab: #研究室を選択していない場合
                    mes.error("研究室を選択してください", search_name_window)
                elif searching_lab not in search_lab_list: #選択した学部と研究室・ゼミが一致しない場合
                    mes.error("選択した学部と研究室・ゼミが一致していません", search_name_window)
                else:
                    info.offer_user_name(search_undergraduate, searching_lab) #選択した研究室の利用者の名前とフリガナを取得
                    search_name_dict.clear() #利用者の名前とフリガナを格納する辞書を初期化(空にする)
                    search_name_dict = info.user_name_dict #利用者の名前とフリガナの辞書を代入

                    for disp_id in search_name_dict:
                        display = display + "・" + str(search_name_dict[disp_id]) + "(" + str(disp_id) + ")\n"
                    if len(search_name_dict) == 0: #登録者がいない場合
                        display = "登録されていません"
                    display_label = genWid.generate_label_widget(search_name_window, display, 20, 150, ) #登録者を表示するラベル
                    display_label["bg"] = "white"

                    btn_exe_search.destroy() #検索ボタンを削除
                    disWid.disabled_widget(search_lab_undergraduate_combobox) #学部のコンボボックスを無効化
                    disWid.disabled_widget(btn_search_name_undergraduate) #学部選択ボタンを無効化
                    disWid.disabled_widget(lab_combobox) #研究室・ゼミのコンボボックスを無効化

                def del_result(): #削除ボタンを押した際の処理
                    if display_label:
                        display_label.destroy() #検索結果を表示するラベルを削除
                    btn_del.destroy() #削除ボタンを削除
                    btn_exe_search = tk.Button(search_name_window, text="検索", command=search_name, height=2, width=12) #検索ボタンの生成
                    btn_exe_search.place(x=180, y=100) #検索ボタンの配置
                    search_lab_undergraduate_combobox['state'] = "readonly" #学部のコンボボックスを選択のみに変更
                    btn_search_name_undergraduate['state'] = "normal" #学部選択ボタンを有効化
                    lab_combobox['state'] = "readonly" #研究室・ゼミのコンボボックスを選択のみに変更

                btn_del = tk.Button(search_name_window, text="検索結果をクリア", command=del_result, bg="red", height=2, width=12)
                btn_del.place(x=180, y=100)

        btn_exe_search = tk.Button(search_name_window, text="検索", command=search_name, height=2, width=12) #検索ボタンの生成
        btn_exe_search.place(x=180, y=100) #検索ボタンの配置

    btn_search_name_undergraduate = tk.Button(search_name_window,text='学部を選択',command=select_search_name_undergraduate) #学部選択のボタンを生成
    btn_search_name_undergraduate.place(x=320, y=20) #学部選択のボタンを配置

    search_name_window.mainloop()
