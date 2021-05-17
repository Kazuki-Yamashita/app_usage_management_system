import tkinter as tk #GUI作成のためのライブラリ
import show_message as mes #メッセージボックスを表示するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import usage_management_system_base_infomation as info
import btn_registration_user as btnRegUser #利用登録ボタンを押した際の処理


def btn_undergraduate_in_user_registration(window,
 input_user_name, input_user_name_ruby, reg_undergraduate_combo):
    #選択した学部を取得
    reg_undergraduate = reg_undergraduate_combo.get()
    if not reg_undergraduate: #学部が選択されていない場合
        choices_lab = None
        mes.error("学部を選択してください", window)
        return

    else:
        lab_message = "※研究室・ゼミの選択について\n所属する研究室・ゼミがない場合、直接入力してください。\n名前はローマ字で、(名)_(姓)としてください"
        genWid.generate_message_widget(window, lab_message, 200, "white", 400, 80)

        bvar = tk.BooleanVar(master=window)
        bvar.set(False)
        new_lab = tk.Checkbutton(window, text="新規で研究室を登録", fg="red", variable=bvar)
        new_lab.place(x=400, y=150)

        #選択した学部の研究室情報を取得
        info.offer_lab_list(reg_undergraduate)
        choices_lab = info.choices_lab

    #学部が選択されている場合のみ以下の処理を行う
    if reg_undergraduate:
        #「研究室・ゼミ」のコンボボックス
        input_lab_name = genWid.generate_combobox_widget(window, "normal", choices_lab, "研究室選択", 130, 140)
        input_id = genWid.generate_entry_widget(window, 30, 130, 180)
        input_new_password = genWid.generate_entry_widget(window, 30, 130, 220, "*")
        input_confirm_password = genWid.generate_entry_widget(window, 30, 130, 260, "*")

        id_format_message = "※IDの書式\n・8~16文字\n・アルファベット、数字を各1文字以上含む\n　(大文字・小文字問わず)\n・ひらがな、カタカナ、漢字、全角アルファベット、数字は不可"
        genWid.generate_message_widget(window, id_format_message, 230, "white", 350, 180)

        password_format_message = "※パスワードの書式(IDの条件、上記3つは同様)\n・大文字・小文字のアルファベットどちらも1文字以上含む\n・ - , = , _ , @ 、いずれかの記号を1つ以上含む"
        genWid.generate_message_widget(window, password_format_message, 230, "white", 350, 290)

        #利用者登録ボタンの生成、配置、コマンド指定
        btn_registration = tk.Button(window, text="利用者登録を行う",
         bg='skyblue', height=2, width=15)
        btn_registration.place(x=220, y=300)
        btn_registration["command"] = lambda: btnRegUser.btn_reg_user(
        input_user_name, input_user_name_ruby, reg_undergraduate_combo,
         input_lab_name, choices_lab, input_id, input_new_password,
          input_confirm_password, bvar, window)
