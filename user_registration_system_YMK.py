import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox
import tkinter.ttk
import datetime
import usage_management_system_base_infomation_YMK as info
import is_equal_password as paw #パスワード、名前等、入力内容が適切かどうか判定するモジュール(自作)
import user_registration_operating_db_YMK as opeDB #データベースを操作するモジュール(自作)
import confirm_available_id_system_YMK as conid #データベースに登録するIDがすでに登録されていないか確認するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール
import is_input_entry as isInp #入力項目にすべて入力しているか判定するモジュール
import is_input_entry_reg_user as isInpReg #利用登録の際に入力が適切か判定するモジュール


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
        input_name_entry = genWid.generate_entry_widget(registration_window, 30, 130, 20)
        input_name_ruby_label = genWid.generate_entry_widget(registration_window, 30, 130, 60)

        global input_undergraduate_label
        #学部のコンボボックス
        input_undergraduate_label = genWid.generate_combobox_widget(registration_window, "readonly", info.undergraduate_list, "学部入力", 130, 100)

        def btn_reg_undergraduate(): #学部選択ボタンを押した際の処理
            global reg_undergraduate
            global choices_lab
            reg_undergraduate = input_undergraduate_label.get() #選択した学部を取得
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
                txt_lab_name_label = genWid.generate_combobox_widget(registration_window, "normal", choices_lab, "研究室選択", 130, 140)
                input_txt_id = genWid.generate_entry_widget(registration_window, 30, 130, 180)
                input_new_password = genWid.generate_entry_widget(registration_window, 30, 130, 220, "*")
                input_confirm_password = genWid.generate_entry_widget(registration_window, 30, 130, 260, "*")

                id_format_message = "※IDの書式\n・8~16文字\n・アルファベット、数字を各1文字以上含む\n　(大文字・小文字問わず)\n・ひらがな、カタカナ、漢字、全角アルファベット、数字は不可"
                genWid.generate_message_widget(registration_window, id_format_message, 230, "white", 350, 180)

                password_format_message = "※パスワードの書式(IDの条件、上記3つは同様)\n・大文字・小文字のアルファベットどちらも1文字以上含む\n・ - , = , _ , @ 、いずれかの記号を1つ以上含む"
                genWid.generate_message_widget(registration_window, password_format_message, 230, "white", 350, 290)

                def reg_user(): #利用者登録ボタンを押した際の処理
                    global is_new_lab
                    reg_name = input_name_entry.get() #名前を取得
                    reg_ruby_name = input_name_ruby_label.get() #フリガナを取得
                    reg_undergraduate = input_undergraduate_label.get() #選択した学部を取得
                    reg_lab = txt_lab_name_label.get() #選択した研究室・ゼミを取得
                    reg_id = input_txt_id.get() #IDを取得
                    new_password = input_new_password.get() #設定したパスワードを取得
                    confirm_password = input_confirm_password.get() #確認用のパスワードを取得
                    is_equal_password = paw.equal_password(new_password,confirm_password) #2つのパスワードが一致しているか確認する
                    is_reged_lab = conid.confirm_reged_lab(reg_lab) #研究室がすでに登録されているか判定(登録されていればTrue)
                    is_new_lab = bvar.get() #「新規で研究室を登録」にチェックがついているか調べる

                    #入力が適切か判定(適切であればTrue)
                    result_input = isInpReg.is_input_entry_reg_user(reg_name, reg_ruby_name, reg_lab,
                     choices_lab, is_reged_lab, reg_id, new_password, confirm_password, is_equal_password,
                      is_new_lab, input_new_password, input_confirm_password, registration_window)

                    if result_input: #入力が適切な場合(True)
                        registration_final_confirm = mes.askokcancel("新規利用者登録", "登録しますか？", registration_window) #登録を行うかの最終確認
                        if registration_final_confirm == True: #「OK」を押した場合
                            if conid.confirm_available_id(reg_id) == False: #登録しようとしたIDがすでに登録されていた場合
                                mes.error("このIDは登録できません！", registration_window)
                                return
                            else:
                                reg_time = datetime.datetime.now() #登録した日時を取得
                                try: #データベースへ情報を追加する
                                    registrating = opeDB.registration_user(reg_id, reg_name, reg_ruby_name, reg_undergraduate, reg_lab, new_password, reg_time)
                                    mes.info("登録完了","登録しました", registration_window)
                                    registration_window.destroy()
                                    return
                                except:
                                    mes.error("登録に失敗しました", registration_window)
                                    return
                                #処理終了

                #利用者登録ボタン
                btn_registration = tk.Button(registration_window, text="利用者登録を行う", command=reg_user, bg='skyblue', height=2, width=15) #利用者登録ボタンを生成
                btn_registration.place(x=220, y=300)
                
        #学部選択ボタン
        btn_reg_undergraduate = tk.Button(registration_window, text="学部を選択", command=btn_reg_undergraduate) #学部選択ボタンを生成
        btn_reg_undergraduate.place(x=290, y=100) #学部生成ボタンを配置

    registration_window.mainloop()
