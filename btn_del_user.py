import usage_management_system_base_infomation as info #基本情報を含むモジュール
import login_certification_system as logCe #ログイン認証を行うモジュール
import delete_user_from_DB as delUserDB #DBからユーザーを削除するモジュール
import is_input_entry as isInp #入力項目にすべて入力しているか判定するモジュール
import is_able_login as abLogin #ログイン可能か判定するモジュール
import btn_select_undergraduate_function as btnUnder #学部選択ボタンを押した際に実行される処理
import show_message as mes #メッセージボックスを表示するモジュール

#「登録者の削除」ボタンを押した際の処理
def delete_user_btn(window, del_txt_id, del_txt_password,
 delete_user_undergraduate_combobox):

      input_ID = del_txt_id.get() #入力したユーザーIDを取得
      input_password = del_txt_password.get() #入力したパスワードを取得

      #選択した学部を取得
      delete_user_undergraduate = delete_user_undergraduate_combobox.get()
      #選択した学部の研究室一覧を取得(リスト)
      lab_list = info.offer_lab_list(delete_user_undergraduate)

      #学部を選択していない場合
      if not delete_user_undergraduate:
          mes.error("学部を選択してください", window)
          return

      try: #研究室のコンボボックスが表示されていない状態で検索ボタンを押したか判定
          btnUnder.delete_user_lab_list
      except: #研究室一覧が取得されていない(学部を選択していない)場合
          mes.error("研究室・ゼミを選択してください", window)
          return

      #選択した研究室を取得
      delete_user_lab = btnUnder.lab_combobox_delete_user.get()

      #入力欄への入力が適切か判定(True or False)
      is_input = isInp.is_input_entry_login(delete_user_lab, input_ID,
       input_password, lab_list, window)

      #入力が適切な場合(True)
      if is_input:
          #ログイン認証を行う
          result_login = abLogin.is_able_login(window, delete_user_undergraduate,
           delete_user_lab, input_ID, input_password)

          #ログインできた場合(True)
          if result_login:
              #削除する登録者の名前を取得して代入
              delete_user_name = logCe.name
              #削除の最終確認で表示するメッセージ
              message = "本当に登録者を削除しますか？\n ID : " + input_ID + "\n name : " + delete_user_name
              #削除の最終確認画面
              delete_user_confirmation = mes.askokcancel("登録者削除 最終確認", message, window)

          #「OK」を押した場合
          if delete_user_confirmation:
              #削除を実行
              delete_ornot = delUserDB.delete_user_from_DB(delete_user_undergraduate, delete_user_lab, input_ID)

              #削除に成功した場合(True)
              if delete_ornot:
                  mes.info("登録者削除 完了", "登録者の削除を完了しました", window)
                  #画面を消す
                  window.destroy()

              #削除に失敗した場合(False)
              else:
                  mes.error("登録者の削除に失敗しました", window)
                  return
