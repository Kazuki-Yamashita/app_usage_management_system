import tkinter as tk
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import tkinter.ttk #コンボボックスを扱うライブラリ
import used_data_registration_system_YMK as regUsed #使用歴をDBに記録するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール


def close_memo_window(): #備考記入画面を閉じようとした場合の処理
    mes.error("「記入終了」ボタンを押してください", memo_window)

def memo(selected_undergraduate, selected_lab, input_ID, user_name, user_name_ruby, start_using_datetime, finish_using_datetime, using_second_time):
    global memo_window
    memo_window = mw.make_window("備考記入画面", '647x400')

    caution = genWid.generate_label_widget(memo_window, "この画面への入力時間は測定時間に含まれません。正確に記入してください", 20, 7, "red") #備考記入画面への注意事項のラベルを生成
    caution["font"] = ("", 12, "bold")

    memo_text = tk.Text(memo_window, state='disabled') #備考を記入するテキストボックスを作成
    memo_text.place(x=20, y=80, width=450, height=250) #テキストボックスを配置

    memo_window.protocol('WM_DELETE_WINDOW', close_memo_window) #備考記入画面を閉じようとしたときに記入するように注意する

    precautions_text = "※ ガラスセル等、備品を破損した\n 場合も記入してください"
    precautions = genWid.generate_label_widget(memo_window, precautions_text, 470, 80)

    def text_off(): #「異常なし」のボタンを押した場合
        memo_text['state'] = 'disabled' #テキストに書き込めない状態にする
    def text_on(): #「不具合あり」のボタンを押した場合
        memo_text['state'] = 'normal' #テキストに書き込める状態にする
    def text_delete():
        memo_delete_confirmation = mes.askokcancel("テキストの削除", "入力した内容を全て削除しますか？", memo_window) #入力内容を削除するかの確認画面の表示
        if memo_delete_confirmation == True: #「OK」を押した場合
            text_on() #テキストを編集可能にする
            memo_text.delete("1.0",tk.END) #内容を全て削除する
            if var.get() == 0: #削除した際に「異常なし」を選んでいた場合
                text_off() #テキストを編集不可にする

    var = tk.IntVar(master=memo_window) #チェックの有無を調べる変数
    var.set(0)
    rb_OK = tk.Radiobutton(memo_window, value=0, variable=var, text='異常ありませんでした', command=text_off) #「異常なし」の場合のラジオボタン
    rb_OK.place(x=20, y=30) #配置
    rb_notOK = tk.Radiobutton(memo_window, value=1, variable=var, text='不具合がありました　（以下の欄にその内容を書き込んでください）', command=text_on) #「不具合あり」の場合のラジオボタン
    rb_notOK.place(x=20, y=50) #配置

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
            memo_confirmation = mes.askokcancel("メモ最終確認", "これで記入しますか？", memo_window) #メモ記入の最終確認画面を表示

        if memo_confirmation == True: #「OK」を選択した場合
            memo = memo_text.get("1.0","end-1c") #メモの内容を取得

            try: #DBへ記録
                regUsed.used_data_registration(selected_undergraduate, selected_lab, input_ID, user_name, user_name_ruby, start_using_datetime, finish_using_datetime, using_second_time, memo)
                mes.info("使用歴 記録完了","記録が完了しました", memo_window)
                memo_window.destroy() #備考記入画面を閉じる
            except: #何らかの理由で記録できなかった場合
                mes.error("使用歴を記録できませんでした。", memo_window)

    btn_finish_memo = tk.Button(memo_window,text="記入終了", command=memo_finish, bg='green', height=2, width=7) #メモ記入終了のボタンを生成
    btn_finish_memo.place(x=400,y=340) #メモ記入終了のボタンを配置
    btn_text_delete = tk.Button(memo_window, text="削除", command=text_delete, height=2, width=7) #テキスト削除ボタンを生成
    btn_text_delete.place(x=20,y=340) #テキスト削除ボタンの配置
    memo_window.mainloop()
