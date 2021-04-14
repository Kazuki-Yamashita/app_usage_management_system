import search_user_name_system_YMK as sea #研究室ごとに登録者を検索するモジュール
import search_usage_data_system_YMK as seaUsage #使用履歴を調べるモジュール
import delete_user_system_YMK as delUser #登録者を削除するモジュール
import master_password_system_YMK as masPass #マスターパスワードのログイン画面を表示するモジュール


def menubar_search_user_name(): #メニューバーから「登録者の検索」を選択した際の処理
    sea.search_user_name()

def menubar_search_usage_record(): #メニューバーから「使用履歴の検索」を選択した際の処理
    seaUsage.search_used_data()

def menubar_delete_user(): #メニューバーから「登録者の削除」を選択した際の処理
    delUser.delete_user()

def menubar_delete_lab(): #メニューバーから「研究室・ゼミの削除」を選択した際の処理
    master_function = "del_lab"
    masPass.master(master_function)

def menubar_change_master_password(): #メニューバーから「マスターパスワードの変更」を選択した際の処理
    master_function = "change_master_password"
    masPass.master(master_function)
    
