import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox
import tkinter.ttk
import datetime
import usage_management_system_base_infomation_YMK as info
import equal_password_or_not_YMK as paw #パスワード、名前等、入力内容が適切かどうか判定するモジュール(自作)
import user_registration_operating_db_YMK as opeDB #データベースを操作するモジュール(自作)
import confirm_available_id_system_YMK as conid #データベースに登録するIDがすでに登録されていないか確認するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール


def registration(root): #メイン画面で「新規登録」ボタンを押した際の処理
    registration_confirm = mes.askyesno("新規登録確認", "利用者の新規登録をしますか？", root) #新規登録を行うかの確認画面
    if registration_confirm == False: #新規登録確認で「いいえ」を押した場合
        return
    elif registration_confirm == True: #新規登録確認で「はい」を押した場合
        root.withdraw()
        registration_window = tk.Tk() #新規登録画面のウィンドウを生成
        registration_window.title('新規登録画面') #新規登録画面のタイトル
        registration_window.geometry('614x380') #新規登録画面の大きさ
        #文字の表示
        genWid.generate_label_widget(registration_window, "名前 (漢字 等) : ", 32, 20)
        genWid.generate_label_widget(registration_window, "名前 (フリガナ) : ", 35, 60)
        genWid.generate_label_widget(registration_window, "学部 : ", 81, 100)
        genWid.generate_label_widget(registration_window, "研究室・ゼミ : ", 47, 140)
        genWid.generate_label_widget(registration_window, "登録するユーザID : ", 24, 180)
        genWid.generate_label_widget(registration_window, "設定するパスワード : ", 20, 220)
        genWid.generate_label_widget(registration_window, "パスワード確認用 : ", 27, 260)

        genWid.generate_message_widget(registration_window,
         "※名前の入力について\n姓と名の間は、半角スペースを1つ\n入れてください", 200, "white", 340, 20)

        #名前の入力欄
        input_name_entry = genWid.generate_entry_widget(registration_window, 30, 130, 20)
        #名前のフリガナの入力欄
        input_name_ruby_label = genWid.generate_entry_widget(registration_window, 30, 130, 60)

        global input_undergraduate_label
        #学部のコンボボックス
        input_undergraduate_label = genWid.generate_combobox_widget(registration_window, "readonly", info.undergraduate_list, "学部入力", 130, 100)

        def btn_reg_undergraduate(): #学部選択ボタンを押した際の処理
            global reg_undergraduate
            global choices_lab
            reg_undergraduate = input_undergraduate_label.get() #選択した学部を取得

            lab_message = "※研究室・ゼミの選択について\n所属する研究室・ゼミがない場合、直接入力してください。\n名前はローマ字で、(名)_(姓)としてください"
            genWid.generate_message_widget(registration_window, lab_message, 200, "white", 400, 80)

            bvar = tk.BooleanVar(master=registration_window)
            bvar.set(False)
            new_lab = tk.Checkbutton(registration_window, text="新規で研究室を登録", fg="red", variable=bvar)
            new_lab.place(x=400, y=150)

            if not reg_undergraduate: #学部が選択されていない場合
                choices_lab = None
                mes.error("学部を選択してください", registration_window)
            else:
                info.offer_lab_list(reg_undergraduate) #選択した学部の研究室情報を取得
                choices_lab = info.choices_lab

            if reg_undergraduate: #学部が選択されている場合のみ以下の処理を行う
                #「研究室・ゼミ」のコンボボックス
                txt_lab_name_label = genWid.generate_combobox_widget(registration_window, "normal", choices_lab, "研究室選択", 130, 140)

            def btn_reg_lab(): #「研究室・ゼミ」選択ボタンを押した際の処理
                global reg_lab
                reg_lab = txt_lab_name_label.get() #選択した研究室・ゼミを取得
                if not reg_lab:
                    mes.error("研究室・ゼミを選択してください", registration_window)
                else:
                    mes.info("研究室・ゼミ 選択完了", "研究室・ゼミを選択しました", registration_window)

                input_txt_id = genWid.generate_entry_widget(registration_window, 30, 130, 180)
                input_txt_password = genWid.generate_entry_widget(registration_window, 30, 130, 220, "*")
                input_confirm_password = genWid.generate_entry_widget(registration_window, 30, 130, 260, "*")

                id_format_message = "※IDの書式\n・8~16文字\n・アルファベット、数字を各1文字以上含む\n　(大文字・小文字問わず)\n・ひらがな、カタカナ、漢字、全角アルファベット、数字は不可"
                genWid.generate_message_widget(registration_window, id_format_message, 230, "white", 350, 180)

                password_format_message = "※パスワードの書式(IDの条件、上記3つは同様)\n・大文字・小文字のアルファベットどちらも1文字以上含む\n・ - , = , _ , @ 、いずれかの記号を1つ以上含む"
                genWid.generate_message_widget(registration_window, password_format_message, 230, "white", 350, 290)

                def reg_user(): #利用者登録ボタンを押した際の処理
                    global new_lab_ornot
                    reg_name = input_name_entry.get() #名前を取得
                    reg_ruby_name = input_name_ruby_label.get() #フリガナを取得
                    reg_id = input_txt_id.get() #IDを取得
                    password1 = input_txt_password.get() #設定したパスワードを取得
                    password2 = input_confirm_password.get() #確認用のパスワードを取得
                    equal_password_or_not = paw.equal_password(password1,password2) #2つのパスワードが一致しているか確認する
                    reged_lab_ornot = conid.confirm_reged_lab(reg_lab) #研究室がすでに登録されているか判定(登録されていればTrue)
                    new_lab_ornot = bvar.get() #「新規で研究室を登録」にチェックがついているか調べる

                    #以下、登録できるかどうかの判定
                    if not reg_name or not reg_ruby_name or not reg_id or not password1 or not password2: #未入力の項目がある場合
                        mes.error("入力していない項目があります", registration_window)

                    elif reg_lab not in choices_lab and reged_lab_ornot == True: #研究室がすでに登録されていて、選択した学部と研究室・ゼミが不一致の場合
                        mes.error("選択した学部と研究室・ゼミが一致していません", registration_window)

                    elif reged_lab_ornot == False and new_lab_ornot == False: #研究室が登録されておらず、「新規で研究室を登録」にチェックがついていない場合
                        mes.error("新規で研究室を登録する場合、チェックをつけてください", registration_window)

                    elif reged_lab_ornot == True and new_lab_ornot == True: #研究室が登録されていて、「新規で研究室を登録」にチェックがついている場合
                        mes.error("研究室が登録済みの場合、チェックはつけないでください", registration_window)

                    elif equal_password_or_not == False: #一致していない場合
                        mes.error("パスワードが一致していません！", registration_window)
                        input_txt_password.delete(0, tk.END) #入力したパスワードを削除する
                        input_confirm_password.delete(0, tk.END) #入力した確認用パスワードを削除する

                    elif paw.pattern_name(reg_name) == False: #入力した名前の文字が適切でない場合
                        mes.error("名前に使用できない文字があります", registration_window)

                    elif paw.pattern_ruby_name(reg_ruby_name) == False: #名前にフリガナが適切でない場合
                        mes.error("フリガナに使用できない文字があります", registration_window)

                    elif paw.pattern_id(reg_id) == False: #入力したIDが適切でない場合
                        mes.error("IDが適切ではありません", registration_window)
                        input_txt_id.delete(0, tk.END)

                    elif paw.pattern_password(password1) == False: #入力したパスワードが適切でない場合
                        mes.error("パスワードが適切ではありません", registration_window)
                        input_txt_password.delete(0, tk.END) #入力したパスワードを削除する
                        input_confirm_password.delete(0, tk.END) #入力した確認用パスワードを削除する

                    else: #一致している場合
                        registration_final_confirm = mes.askokcancel("新規利用者登録", "登録しますか？", registration_window) #登録を行うかの最終確認
                        if registration_final_confirm == True: #「OK」を押した場合
                            if conid.confirm_available_id(reg_id) == False: #登録しようとしたIDがすでに登録されていた場合
                                mes.error("このIDは登録できません！", registration_window)
                            else:
                                reg_time = datetime.datetime.now() #登録した日時を取得
                                try: #データベースへ情報を追加する
                                    registrating = opeDB.registration_user(reg_id, reg_name, reg_ruby_name, reg_undergraduate, reg_lab, password1, reg_time)
                                    mes.info("登録完了","登録しました", registration_window)
                                    registration_window.destroy()
                                except:
                                    mes.error("登録に失敗しました", registration_window)
                                #処理終了

                btn_registration = tk.Button(registration_window, text="利用者登録を行う", command=reg_user, bg='skyblue', height=2, width=15) #利用者登録ボタンを生成
                btn_registration.place(x=220, y=300) #利用者登録ボタンを配置

            btn_reg_lab = tk.Button(registration_window, text="研究室・ゼミを選択", command=btn_reg_lab) #「研究室・ゼミ」選択ボタンを生成
            btn_reg_lab.place(x=290, y=140) #「研究室・ゼミ」選択ボタンを配置

        btn_reg_undergraduate = tk.Button(registration_window, text="学部を選択", command=btn_reg_undergraduate) #学部選択ボタンを生成
        btn_reg_undergraduate.place(x=290, y=100) #学部生成ボタンを配置

    registration_window.mainloop()
