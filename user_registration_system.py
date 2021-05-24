import tkinter as tk #GUI作成のためのライブラリ
import make_window as mw #ウィンドウを作成するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import usage_management_system_base_infomation as info #基本情報を提供するモジュール
#利用登録画面の学部選択ボタンを押した際の処理を記述
import btn_select_undergraduate_in_user_registration as btnUnderInReg

#メイン画面で「新規登録」ボタンを押した際の処理
def user_registration(main_window):
    #新規登録を行うかの確認画面
    user_registration_confirm = mes.askyesno("新規登録確認", "利用者の新規登録をしますか？", main_window)

    #新規登録確認で「いいえ」を押した場合
    if not user_registration_confirm:
        return
    #新規登録確認で「はい」を押した場合
    else:
        #ウィンドウの作成
        user_registration_confirm = mw.make_window("新規登録画面", '614x380')
        #文字の表示
        genWid.generate_label_widget(user_registration_confirm, "名前 (漢字 等) : ", 22, 20)
        genWid.generate_label_widget(user_registration_confirm, "名前 (フリガナ) : ", 25, 60)
        genWid.generate_label_widget(user_registration_confirm, "学部 : ", 71, 100)
        genWid.generate_label_widget(user_registration_confirm, "研究室・ゼミ : ", 37, 140)
        genWid.generate_label_widget(user_registration_confirm, "登録するユーザID : ", 14, 180)
        genWid.generate_label_widget(user_registration_confirm, "設定するパスワード : ", 10, 220)
        genWid.generate_label_widget(user_registration_confirm, "パスワード確認用 : ", 17, 260)
        #名前の書式について記載するメッセージを表示
        genWid.generate_message_widget(user_registration_confirm,
         "※名前の入力について\n姓と名の間は、半角スペースを1つ\n入れてください", 200, "white", 340, 10)

        #名前、フリガナの入力欄を生成
        input_user_name = genWid.generate_entry_widget(user_registration_confirm, 30, 120, 20)
        input_user_name_ruby = genWid.generate_entry_widget(user_registration_confirm, 30, 120, 60)

        #学部のコンボボックス生成
        user_reg_undergraduate_combobox = genWid.generate_combobox_widget(user_registration_confirm,
         "readonly", info.undergraduate_list, "学部入力", 120, 100)

        #研究室表示ボタンを生成、配置、コマンド指定
        btn_reg_undergraduate = tk.Button(user_registration_confirm, text="学部の研究室・\nゼミを表示")
        btn_reg_undergraduate.place(x=280, y=90)
        btn_reg_undergraduate['command'] = lambda: btnUnderInReg.btn_undergraduate_in_user_registration(
         user_registration_confirm, input_user_name, input_user_name_ruby, user_reg_undergraduate_combobox)

    user_registration_confirm.mainloop()
