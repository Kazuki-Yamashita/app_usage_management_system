import re

#新規利用者登録において、入力内容の書式、文字パターンが適切かどうか判定するファイル

#名前のパターンが合っているか判定する関数
def pattern_name(investigate_name):
    #数字、全角アルファベットを含む場合
    if re.search(r'[1-9]|[Ａ-Ｚ]|[ａ-ｚ]',investigate_name):
        return False
    else: #漢字、ひらがな、カタカナ、半角アルファベットが使用可能
        return True

#フリガナのパターンが合っているか判定する関数
def pattern_ruby_name(investigate_ruby_name):
    #数字、ひらがな、半角カタカナ、漢字、全角アルファベットを含む場合
    if re.search(r'[1-9]|[ぁ-ん]|[ｦ-ﾟ]|[一-龥]|[Ａ-Ｚ]|[ａ-ｚ]',investigate_ruby_name):
        return False
    else: #全角カタカナ、半角アルファベットが使用可能
        return True

#IDのパターンが合っているか判定する関数
def pattern_id(investigate_id):
    #入力したパスワードが7文字以下、または17文字以上の場合
    if len(investigate_id)<=7 or len(investigate_id)>=17:
        return False
    #小文字、または大文字のアルファベットを1文字以上含まない場合
    elif not re.search(r'[a-z]+|[A-Z]+',investigate_id):
        return False
    #空白文字を含む場合
    elif re.search(r'\s',investigate_id):
        return False
    #数字を含まない場合
    elif not re.search(r'[1-9]+',investigate_id):
        return False
    #ひらがな、カタカナ、漢字、全角アルファベットを含む場合
    elif re.search(u'[ぁ-んァ-ン]|[ｦ-ﾟ]|[一-龥]|[Ａ-Ｚ]+|[ａ-ｚ]+',investigate_id):
        return False
    else:
        return True

#パスワードのパターンが合っているか判定する関数
def pattern_password(investigate_password):
    #入力したパスワードが7文字以下、または17文字以上の場合
    if len(investigate_password)<=7 or len(investigate_password)>=17:
        return False
    #小文字のアルファベットを1文字以上含まない場合
    elif not re.search(r'[a-z]+',investigate_password):
        return False
    #大文字のアルファベットを1文字以上含まない場合
    elif not re.search(r'[A-Z]+',investigate_password):
        return False
    #空白文字を含む場合
    elif re.search(r'\s',investigate_password):
        return False
    #4つのいずれかの記号を含まない場合
    elif not re.search(r'[-=_@]+',investigate_password):
        return False
    #数字を含まない場合
    elif not re.search(r'[1-9]+',investigate_password):
        return False
    #ひらがな、カタカナ、漢字、全角アルファベットを含む場合
    elif re.search(u'[ぁ-んァ-ン]|[ｦ-ﾟ]|[一-龥]|[Ａ-Ｚ]+|[ａ-ｚ]+',investigate_password):
        return False
    else:
        return True
