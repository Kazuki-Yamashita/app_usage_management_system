import tkinter as tk #GUI作成のためのライブラリ
import usage_management_system_base_infomation as info
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール
#利用登録画面の学部選択ボタンを押した際の処理を記述
import btn_select_undergraduate_in_user_registration as btnUnderInReg

#メイン画面で「新規登録」ボタンを押した際の処理
def registration(root):
    #新規登録を行うかの確認画面
    registration_confirm = mes.askyesno("新規登録確認", "利用者の新規登録をしますか？", root)
    if not registration_confirm: #新規登録確認で「いいえ」を押した場合
        return
    else: #新規登録確認で「はい」を押した場合
        root.withdraw() #メイン画面を消す
        registration_window = mw.make_window("新規登録画面", '614x380')
        #文字の表示
        genWid.generate_label_widget(registration_window, "名前 (漢字 等) : ", 32, 20)
        genWid.generate_label_widget(registration_window, "名前 (フリガナ) : ", 35, 60)
        genWid.generate_label_widget(registration_window, "学部 : ", 81, 100)
        genWid.generate_label_widget(registration_window, "研究室・ゼミ : ", 47, 140)
        genWid.generate_label_widget(registration_window, "登録するユーザID : ", 24, 180)
        genWid.generate_label_widget(registration_window, "設定するパスワード : ", 20, 220)
        genWid.generate_label_widget(registration_window, "パスワード確認用 : ", 27, 260)
        #名前の書式について記載するメッセージ
        genWid.generate_message_widget(registration_window,
         "※名前の入力について\n姓と名の間は、半角スペースを1つ\n入れてください", 200, "white", 340, 20)

        #名前、フリガナの入力欄
        input_user_name = genWid.generate_entry_widget(registration_window, 30, 130, 20)
        input_user_name_ruby = genWid.generate_entry_widget(registration_window, 30, 130, 60)

        global reg_undergraduate_combo
        #学部のコンボボックス
        reg_undergraduate_combo = genWid.generate_combobox_widget(registration_window,
         "readonly", info.undergraduate_list, "学部入力", 130, 100)

        #学部選択ボタン
        btn_reg_undergraduate = tk.Button(registration_window, text="学部の研究室・ゼミを表示") #学部選択ボタンを生成
        btn_reg_undergraduate.place(x=290, y=100) #学部生成ボタンを配置
        btn_reg_undergraduate['command'] = lambda: btnUnderInReg.btn_undergraduate_in_user_registration(
         registration_window, input_user_name, input_user_name_ruby, reg_undergraduate_combo)

    registration_window.mainloop()
