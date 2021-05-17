import re

#設定するパスワードと確認用のパスワードが一致しているか判定する関数
def equal_password(a,b):
    if a == b and a and b:
        return True
    else:
        return False
