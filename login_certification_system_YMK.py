import sqlite3
import usage_management_system_base_infomation_YMK as info
import connect_db as conDB #DBへ接続するモジュール


def login_certification(input_ID, input_password, undergraduate, lab):
    return_db = conDB.connect_user_db(undergraduate)
    cur = return_db[0]
    conn = return_db[1]

    global master_password
    info.offer_master_password() #マスターパスワードをDBから抽出
    try:
        master_password = info.master_password_list[0] #マスターパスワードを取得
    except: #初回のみ
        master_password = "master_initial-password_YMK"

    #該当する学部のDBから入力されたIDのパスワードを取得
    select_sql = 'SELECT name, name_ruby, password FROM {} WHERE id = ?'.format(lab)
    input_ID = [input_ID]
    real_password = None
    global name
    global name_ruby
    for data in cur.execute(select_sql,input_ID):
        name = data[0]
        name_ruby = data[1]
        real_password = data[2]

    #入力されたパスワードと登録されているパスワードが異なり、かつマスターパスワードでもない場合
    if input_password != real_password and input_password != master_password:
        return False

    cur.close()
    conn.close()
