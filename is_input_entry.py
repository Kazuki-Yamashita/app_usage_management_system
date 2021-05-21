import show_message as mes #メッセージボックスを表示するモジュール


#入力欄に入力されているか判定する関数
def is_input_entry_login(lab, id, password, lab_list, window):

    #研究室を選択していない場合
    if not lab:
        mes.error("研究室・ゼミを選択してください", window)
        return False
    #選択した研究室・ゼミが選択した学部の研究室一覧に含まれない場合
    elif lab not in lab_list:
        mes.error("選択した学部と研究室・ゼミが一致していません", window)
        return False
    #IDを入力していない場合
    elif not id and password:
        mes.error("IDを入力してください", window)
        return False
    #パスワードを入力していない場合
    elif not password and id:
        mes.error("パスワードを入力してください", window)
        return False
    #ID、パスワードどちらも入力していない場合
    elif not id and not password:
        mes.error("IDおよびパスワードを入力してください", window)
        return False
    else:
        return True

#研究室の選択が適切かどうか判定する関数
def is_select_lab(window, lab, lab_list):
    
    #研究室を選択していない場合
    if not lab:
        mes.error("研究室・ゼミを選択してください", window)
        return False
    #選択した学部と研究室・ゼミが一致しない場合
    elif lab not in lab_list:
        mes.error("選択した学部と研究室・ゼミが一致していません", window)
        return False
    else:
        return True
