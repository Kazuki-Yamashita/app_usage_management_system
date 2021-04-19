import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox
import tkinter.ttk
import datetime
import usage_management_system_base_infomation as info
import confirm_available_id_system as conid #データベースに登録するIDがすでに登録されていないか確認するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール
import is_input_entry as isInp #入力項目にすべて入力しているか判定するモジュール
import is_input_entry_reg_user as isInpReg #利用登録の際に入力が適切か判定するモジュール
import btn_registration_user as btnRegUser #利用登録ボタンを押した際の処理

def registration(root): #メイン画面で「新規登録」ボタンを押した際の処理
    registration_confirm = mes.askyesno("新規登録確認", "利用者の新規登録をしますか？", root) #新規登録を行うかの確認画面
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
        reg_undergraduate_combo = genWid.generate_combobox_widget(registration_window, "readonly", info.undergraduate_list, "学部入力", 130, 100)

        def btn_reg_undergraduate(): #学部選択ボタンを押した際の処理
            global reg_undergraduate
            global choices_lab
            reg_undergraduate = reg_undergraduate_combo.get() #選択した学部を取得
            if not reg_undergraduate: #学部が選択されていない場合
                choices_lab = None
                mes.error("学部を選択してください", registration_window)
                return

            else:
                lab_message = "※研究室・ゼミの選択について\n所属する研究室・ゼミがない場合、直接入力してください。\n名前はローマ字で、(名)_(姓)としてください"
                genWid.generate_message_widget(registration_window, lab_message, 200, "white", 400, 80)

                bvar = tk.BooleanVar(master=registration_window)
                bvar.set(False)
                new_lab = tk.Checkbutton(registration_window, text="新規で研究室を登録", fg="red", variable=bvar)
                new_lab.place(x=400, y=150)

                info.offer_lab_list(reg_undergraduate) #選択した学部の研究室情報を取得
                choices_lab = info.choices_lab

            if reg_undergraduate: #学部が選択されている場合のみ以下の処理を行う
                #「研究室・ゼミ」のコンボボックス
                input_lab_name = genWid.generate_combobox_widget(registration_window, "normal", choices_lab, "研究室選択", 130, 140)
                input_id = genWid.generate_entry_widget(registration_window, 30, 130, 180)
                input_new_password = genWid.generate_entry_widget(registration_window, 30, 130, 220, "*")
                input_confirm_password = genWid.generate_entry_widget(registration_window, 30, 130, 260, "*")

                id_format_message = "※IDの書式\n・8~16文字\n・アルファベット、数字を各1文字以上含む\n　(大文字・小文字問わず)\n・ひらがな、カタカナ、漢字、全角アルファベット、数字は不可"
                genWid.generate_message_widget(registration_window, id_format_message, 230, "white", 350, 180)

                password_format_message = "※パスワードの書式(IDの条件、上記3つは同様)\n・大文字・小文字のアルファベットどちらも1文字以上含む\n・ - , = , _ , @ 、いずれかの記号を1つ以上含む"
                genWid.generate_message_widget(registration_window, password_format_message, 230, "white", 350, 290)

                #利用者登録ボタン
                btn_registration = tk.Button(registration_window, text="利用者登録を行う",
                 bg='skyblue', height=2, width=15) #利用者登録ボタンを生成
                btn_registration.place(x=220, y=300)
                btn_registration["command"] = lambda: btnRegUser.btn_reg_user(
                input_user_name, input_user_name_ruby, reg_undergraduate_combo,
                 input_lab_name, choices_lab, input_id, input_new_password,
                  input_confirm_password, bvar, registration_window)

        #学部選択ボタン
        btn_reg_undergraduate = tk.Button(registration_window, text="学部を選択", command=btn_reg_undergraduate) #学部選択ボタンを生成
        btn_reg_undergraduate.place(x=290, y=100) #学部生成ボタンを配置

    registration_window.mainloop()
    return
