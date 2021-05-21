import tkinter as tk #GUI作成のためのライブラリ
import show_message as mes #メッセージボックスを表示するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import usage_management_system_base_infomation as info #基本情報を提供するモジュール
import btn_registration_user as btnRegUser #新規利用者登録ボタンを押した際の処理

#新規利用者登録の研究室表示ボタンを押した際の処理
def btn_undergraduate_in_user_registration(window,
 input_user_name, input_user_name_ruby, user_reg_undergraduate_combobox):
    #選択した学部を取得
    user_reg_undergraduate = user_reg_undergraduate_combobox.get()

    #学部が選択されていない場合
    if not user_reg_undergraduate:
        mes.error("学部を選択してください", window)
        return
    #学部を選択している場合
    else:
        #研究室・ゼミの選択に関するメッセージ
        lab_message = "※研究室・ゼミの選択について\n所属する研究室・ゼミがない場合、直接入力してください。\n名前はローマ字で、(名)_(姓)としてください"
        genWid.generate_message_widget(window, lab_message, 200, "white", 400, 80)

        #研究室の新規登録の有無を調べるチェックボックスの有無を判定する記述
        bvar = tk.BooleanVar(master=window)
        bvar.set(False)
        new_lab = tk.Checkbutton(window, text="新規で研究室を登録", fg="red", variable=bvar)
        new_lab.place(x=400, y=150)

        #選択した学部の研究室情報を取得
        lab_list = info.offer_lab_list(user_reg_undergraduate)

        #「研究室・ゼミ」のコンボボックスを生成
        input_lab_name = genWid.generate_combobox_widget(window, "normal", lab_list, "研究室選択", 130, 140)

        #id、パスワード、パスワード確認用の入力欄を生成
        input_id = genWid.generate_entry_widget(window, 30, 130, 180)
        input_new_password = genWid.generate_entry_widget(window, 30, 130, 220, "*")
        input_confirm_password = genWid.generate_entry_widget(window, 30, 130, 260, "*")

        #idの書式に関するメッセージ
        id_format_message = "※IDの書式\n・8~16文字\n・アルファベット、数字を各1文字以上含む\n　(大文字・小文字問わず)\n・ひらがな、カタカナ、漢字、全角アルファベット、数字は不可"
        genWid.generate_message_widget(window, id_format_message, 230, "white", 350, 180)

        #パスワードの書式に関するメッセージ
        password_format_message = "※パスワードの書式(IDの条件、上記3つは同様)\n・大文字・小文字のアルファベットどちらも1文字以上含む\n・ - , = , _ , @ 、いずれかの記号を1つ以上含む"
        genWid.generate_message_widget(window, password_format_message, 230, "white", 350, 290)

        #利用者登録ボタンの生成、配置、コマンド指定
        btn_registration = tk.Button(window, text="利用者登録を行う", bg='skyblue', height=2, width=15)
        btn_registration.place(x=220, y=300)
        btn_registration["command"] = lambda: btnRegUser.btn_reg_user(
        input_user_name, input_user_name_ruby, user_reg_undergraduate_combobox,
         input_lab_name, input_id, input_new_password,
          input_confirm_password, bvar, window)
