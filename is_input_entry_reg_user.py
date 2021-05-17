import tkinter as tk #GUI作成のためのライブラリ
import show_message as mes #メッセージボックスを表示するモジュール
import is_collect_format_string as formatStr #名前、パスワード等の文字列の書式が適切か判定するモジュール

#新規利用登録の際に、入力が適切か判定する関数
def is_input_entry_reg_user(user_name, user_ruby_name, reg_lab,
 choices_lab, is_reged_lab, id, new_password, confirm_password,
 is_equal_password, is_new_lab, window, input_new_password, input_confirm_password):

    #未入力の項目がある場合
    if not user_name or not user_ruby_name or not id or not new_password or not confirm_password:
        mes.error("入力していない項目があります", window)
        return False

    #研究室を選択していない場合
    elif not reg_lab:
        mes.error("研究室を選択してください", window)
        return False

    #研究室がすでに登録されていて、選択した学部と研究室・ゼミが不一致の場合
    elif reg_lab not in choices_lab and is_reged_lab:
        mes.error("選択した学部と研究室・ゼミが一致していません", window)
        return False

    #研究室が登録されておらず、「新規で研究室を登録」にチェックがついていない場合
    elif not is_reged_lab and not is_new_lab:
        mes.error("新規で研究室を登録する場合、チェックをつけてください", window)
        return False

    #研究室が登録されていて、「新規で研究室を登録」にチェックがついている場合
    elif is_reged_lab and is_new_lab:
        mes.error("研究室が登録済みの場合、チェックはつけないでください", window)
        return False

    #パスワードが確認用と一致していない場合
    elif not is_equal_password:
        mes.error("パスワードが一致していません！", window)
        input_new_password.delete(0, tk.END) #入力したパスワードを削除する
        input_confirm_password.delete(0, tk.END) #入力した確認用パスワードを削除する
        return False

    #入力した名前の文字が適切でない場合
    elif not formatStr.pattern_name(user_name):
        mes.error("名前に使用できない文字があります", window)
        return False

    #名前にフリガナが適切でない場合
    elif not formatStr.pattern_ruby_name(user_ruby_name):
        mes.error("フリガナに使用できない文字があります", window)
        return False

    #入力したIDが適切でない場合
    elif not formatStr.pattern_id(id):
        mes.error("IDが適切ではありません", window)
        return False

    #入力したパスワードが適切でない場合
    elif not formatStr.pattern_password(new_password):
        mes.error("パスワードの書式が適切ではありません", window)
        input_new_password.delete(0, tk.END) #入力したパスワードを削除する
        input_confirm_password.delete(0, tk.END) #入力した確認用パスワードを削除する
        return False

    else:
        return True
