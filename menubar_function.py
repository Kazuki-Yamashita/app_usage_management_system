import search_user_name_system as sea #研究室ごとに登録者を検索するモジュール
import search_usage_data_system as seaUsage #使用履歴を調べるモジュール
import delete_user_system as delUser #登録者を削除するモジュール
import master_password_system as masPass #マスターパスワードのログイン画面を表示するモジュール

#メニューバーから「登録者の検索」を選択した際の処理
def menubar_search_user_name():
    sea.search_user_name()

#メニューバーから「使用履歴の検索」を選択した際の処理
def menubar_search_usage_record():
    seaUsage.search_used_data()

#メニューバーから「登録者の削除」を選択した際の処理
def menubar_delete_user():
    delUser.delete_user()

#メニューバーから「研究室・ゼミの削除」を選択した際の処理
def menubar_delete_lab():
    master_function = "del_lab"
    masPass.master(master_function)

#メニューバーから「マスターパスワードの変更」を選択した際の処理
def menubar_change_master_password():
    master_function = "change_master_password"
    masPass.master(master_function)
