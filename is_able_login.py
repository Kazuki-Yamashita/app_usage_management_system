import show_message as mes #メッセージボックスを表示するモジュール
import confirm_available_id_system_YMK as conid #IDが存在するか調べる
import login_certification_system_YMK as logCe #ログイン認証を行うモジュール


def is_able_login(window, undergraduate, lab, id, password):

    #IDが存在しない場合
    if not conid.exist_id(id, undergraduate, lab):
        mes.error("IDが存在しません", window)
        return False

    #IDとパスワードが一致しない場合
    elif not logCe.login_certification(id, password, undergraduate, lab):
        mes.error("IDとパスワードが一致しません", window)
        return False

    else: #IDが存在し、パスワードも一致する場合
        return True
