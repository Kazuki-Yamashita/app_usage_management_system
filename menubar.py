import tkinter as tk #GUI作成のためのライブラリ
import menubar_function as funMenu #メニューバーを選択した際に実行される関数をまとめたモジュール

def make_menubar(root):
    menubar = tk.Menu() #メニューバーの作成

    menubar_search = tk.Menu(menubar, tearoff=0) #メニューコマンドの作成
    menubar_search.add_command(label="登録者の検索", command=funMenu.menubar_search_user_name) #コマンドの追加
    menubar_search.add_separator()
    menubar_search.add_command(label="使用履歴の検索", command=funMenu.menubar_search_usage_record)
    menubar.add_cascade(label="検索", menu=menubar_search) #バーに表示する文字、コマンドを設定

    menubar_data_management = tk.Menu(menubar, tearoff=0)
    menubar_data_management.add_command(label="登録者の削除", command=funMenu.menubar_delete_user)
    menubar_data_management.add_command(label="研究室・ゼミの削除", command=funMenu.menubar_delete_lab)
    menubar_data_management.add_command(label="マスターパスワードの変更", command=funMenu.menubar_change_master_password)
    menubar.add_cascade(label="データ管理", menu=menubar_data_management)

    root["menu"] = menubar #メニューバーを設置
