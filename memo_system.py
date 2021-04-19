import tkinter as tk
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import used_data_registration_system as regUsed #使用歴をDBに記録するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール
import close_memo_window as cloMemo #備考記入画面を閉じようとした際の処理
import btns_memo_window as btnsMemo #備考記入画面のボタンのコマンドを記述


def memo(selected_undergraduate, selected_lab, input_ID, user_name, user_name_ruby,
 start_using_datetime, finish_using_datetime, using_second_time):
    memo_window = mw.make_window("備考記入画面", '647x400')

    #備考記入画面への注意事項の文字を表示
    caution = genWid.generate_label_widget(memo_window,
     "この画面への入力時間は測定時間に含まれません。正確に記入してください", 20, 7, "red")
    caution["font"] = ("", 12, "bold")

    precautions_text = "※ ガラスセル等、備品を破損した\n 場合も記入してください"
    precautions = genWid.generate_label_widget(memo_window, precautions_text, 470, 80)

    memo_text = tk.Text(memo_window, state='disabled') #備考を記入するテキストボックスを作成
    memo_text.place(x=20, y=80, width=450, height=250) #テキストボックスを配置

    var = tk.IntVar(master=memo_window) #ラジオボタンのチェックを調べる変数
    var.set(0)
    #「異常なし」の場合のラジオボタン、配置、コマンド指定
    radio_btn_OK = tk.Radiobutton(memo_window, value=0, variable=var, text='異常ありませんでした')
    radio_btn_OK.place(x=20, y=30)
    radio_btn_OK["command"] = lambda: btnsMemo.text_off(memo_text)

    #「不具合あり」の場合のラジオボタンを生成、配置、指定
    radio_btn_notOK = tk.Radiobutton(memo_window, value=1, variable=var,
     text='不具合がありました　（以下の欄にその内容を書き込んでください）')
    radio_btn_notOK.place(x=20, y=50)
    radio_btn_notOK["command"] = lambda: btnsMemo.text_on(memo_text)

    global checked_btn

    def memo_finish(): #「記入終了」ボタンを押した際、以下のことが実行される
        checked_btn = var.get() #どのラジオボタンがチェックされているかを取得
        global memo_confirmation, memo
        memo_confirmation = None
        if checked_btn == 0 and memo_text.get("1.0","end-1c"):
            mes.error("異常がない場合、テキストを削除してください", memo_window)
        elif checked_btn == 1 and not memo_text.get("1.0","end-1c"):
            mes.error("不具合があった場合、内容を記述してください", memo_window)
        else:
            #メモ記入の最終確認画面を表示
            memo_confirmation = mes.askokcancel("メモ最終確認", "これで記入しますか？", memo_window)

        if memo_confirmation: #「OK」を選択した場合
            memo = memo_text.get("1.0","end-1c") #メモの内容を取得

            try: #DBへ記録
                regUsed.used_data_registration(selected_undergraduate, selected_lab,
                 input_ID, user_name, user_name_ruby, start_using_datetime,
                  finish_using_datetime, using_second_time, memo)
                mes.info("使用歴 記録完了","記録が完了しました", memo_window)
                memo_window.destroy() #備考記入画面を閉じる
            except: #何らかの理由で記録できなかった場合
                mes.error("使用歴を記録できませんでした。", memo_window)

    #メモ記入終了のボタンを生成、配置、コマンド指定
    btn_finish_memo = tk.Button(memo_window, text="記入終了", bg='green', height=2, width=7)
    btn_finish_memo.place(x=400,y=340)
    btn_finish_memo["command"] = memo_finish

    #テキスト削除ボタンを生成、配置、コマンド指定
    btn_text_delete = tk.Button(memo_window, text="記入内容を削除", height=2, width=12)
    btn_text_delete.place(x=20,y=340)
    btn_text_delete["command"] = lambda: btnsMemo.text_delete(memo_window, memo_text, var)

    #備考記入画面を閉じようとしたときに記入するように注意する
    memo_window.protocol('WM_DELETE_WINDOW', func=lambda: cloMemo.close_memo_window(memo_window))
    memo_window.mainloop()
