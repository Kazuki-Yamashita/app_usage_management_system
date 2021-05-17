import subprocess #外部アプリを実行ためのライブラリ
import show_message as mes #メッセージボックスを表示するモジュール

#外部アプリを起動する関数
def start_app(window, path):
    try:
        result = subprocess.Popen(path, shell=True)
        return result
    except subprocess.CalledProcessError:
        mes.error("アプリケーションの実行に失敗しました", window)
        return False
