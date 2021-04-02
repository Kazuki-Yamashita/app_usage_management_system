import re

def equal_password(a,b):
    if a == b and a and b:
        return True
    else:
        return False

def pattern_name(investigate_name): #名前のパターンが合っているか判定する関数
    if re.search(r'[1-9]|[Ａ-Ｚ]|[ａ-ｚ]',investigate_name): #数字、全角アルファベットを含む場合
        return False
    else:
        return True #漢字、ひらがな、カタカナ、半角アルファベットが使用可能

def pattern_ruby_name(investigate_ruby_name): #フリガナのパターンが合っているか判定する関数
    if re.search(r'[1-9]|[ぁ-ん]|[ｦ-ﾟ]|[一-龥]|[Ａ-Ｚ]|[ａ-ｚ]',investigate_ruby_name): #数字、ひらがな、半角カタカナ、漢字、全角アルファベットを含む場合
        return False
    else:
        return True #全角カタカナ、半角アルファベットが使用可能

def pattern_id(investigate_id): #idのパターンが合っているか判定する関数
    if len(investigate_id)<=7 or len(investigate_id)>=17: #入力したパスワードが7文字以下、または17文字以上の場合
        return False
    elif not re.search(r'[a-z]+|[A-Z]+',investigate_id): #小文字、または大文字のアルファベットを1文字以上含まない場合
        return False
    elif re.search(r'\s',investigate_id): #空白文字を含む場合
        return False
    elif not re.search(r'[1-9]+',investigate_id): #数字を含まない場合
        return False
    elif re.search(u'[ぁ-んァ-ン]|[ｦ-ﾟ]|[一-龥]|[Ａ-Ｚ]+|[ａ-ｚ]+',investigate_id): #ひらがな、カタカナ、漢字、全角アルファベットを含む場合
        return False
    else:
        return True


def pattern_password(investigate_password): #パスワードのパターンが合っているか判定する関数
    if len(investigate_password)<=7 or len(investigate_password)>=17: #入力したパスワードが7文字以下、または17文字以上の場合
        return False
    elif not re.search(r'[a-z]+',investigate_password):#小文字のアルファベットを1文字以上含まない場合
        return False
    elif not re.search(r'[A-Z]+',investigate_password): #大文字のアルファベットを1文字以上含まない場合
        return False
    elif re.search(r'\s',investigate_password): #空白文字を含む場合
        return False
    elif not re.search(r'[-=_@]+',investigate_password): #4つのいずれかの記号を含まない場合
        return False
    elif not re.search(r'[1-9]+',investigate_password): #数字を含まない場合
        return False
    elif re.search(u'[ぁ-んァ-ン]|[ｦ-ﾟ]|[一-龥]|[Ａ-Ｚ]+|[ａ-ｚ]+',investigate_password): #ひらがな、カタカナ、漢字、全角アルファベットを含む場合
        return False
    else:
        return True
