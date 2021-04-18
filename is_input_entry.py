import show_message as mes #メッセージボックスを表示するモジュール


def is_input_entry_login(lab, id, password, lab_list, window):
    if not lab: #研究室を選択していない場合
        mes.error("研究室・ゼミを選択してください", window)
        return False
    elif not id and password: #IDを入力していない場合
        mes.error("IDを入力してください", window)
        return False
    elif not password and id: #パスワードを入力していない場合
        mes.error("パスワードを入力してください", window)
        return False
    elif not id and not password: #ID、パスワードどちらも入力していない場合
        mes.error("IDおよびパスワードを入力してください", window)
        return False
    elif lab not in lab_list: #選択した研究室・ゼミが選択した学部の研究室一覧に含まれない場合
        mes.error("選択した学部と研究室・ゼミが一致していません", window)
        return False
    else:
        return True
