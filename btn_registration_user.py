import datetime
import is_equal_password as paw #パスワードが確認用と一致しているか判定するモジュール
import is_input_entry_reg_user as isInpReg #利用登録の際に入力が適切か判定するモジュール
import confirm_available_id_system as conid #データベースに登録するIDがすでに登録されていないか確認するモジュール
import user_registration_to_db as regUserdb #データベースを操作するモジュール(自作)
import show_message as mes #メッセージボックスを表示するモジュール


#利用登録ボタンを押した際の処理
def btn_reg_user(user_name, user_ruby_name, reg_undergraduate_combo,
 input_lab_name, choices_lab, input_id, input_new_password,
  input_confirm_password, is_check_new_lab, window):

    reg_name = user_name.get() #名前を取得
    reg_ruby_name = user_ruby_name.get() #フリガナを取得

    reg_undergraduate = reg_undergraduate_combo.get() #選択した学部を取得
    reg_lab = input_lab_name.get() #選択した研究室・ゼミを取得

    reg_id = input_id.get() #IDを取得
    new_password = input_new_password.get() #設定したパスワードを取得
    confirm_password = input_confirm_password.get() #確認用のパスワードを取得

    #2つのパスワードが一致しているか確認する(一致していればTrue)
    is_equal_password = paw.equal_password(new_password, confirm_password)
    #研究室がすでに登録されているか判定(登録されていればTrue)
    is_reged_lab = conid.confirm_reged_lab(reg_lab)
    #「新規で研究室を登録」にチェックがついているか調べる
    is_new_lab = is_check_new_lab.get()

    #入力が適切か判定(適切であればTrue)
    result_input = isInpReg.is_input_entry_reg_user(reg_name, reg_ruby_name, reg_lab,
     choices_lab, is_reged_lab, reg_id, new_password, confirm_password, is_equal_password,
      is_new_lab, window, input_new_password, input_confirm_password)

    #登録しようとしたIDがすでに登録されているか判定
    is_available_id = conid.confirm_available_id(reg_id)
    #登録しようとしたIDがすでに登録されていた場合(False)
    if not is_available_id:
        mes.error("このIDは登録できません！", window)
        return

    if result_input: #入力が適切な場合
        #登録を行うかの最終確認
        registration_final_confirm = mes.askokcancel("新規利用者登録",
         "登録しますか？", window)

        #「OK」を押した場合
        if registration_final_confirm:
            #登録した日時を取得
            reg_time = datetime.datetime.now()

            try: #データベースへ情報を追加する
                registrating = regUserdb.registration_user(reg_id, reg_name,
                 reg_ruby_name, reg_undergraduate, reg_lab, new_password, reg_time)
                #登録完了の画面を表示
                mes.info("登録完了","登録しました", window)
                window.destroy()
                return
            except:
                mes.error("登録に失敗しました", window)
                return
             #処理終了
