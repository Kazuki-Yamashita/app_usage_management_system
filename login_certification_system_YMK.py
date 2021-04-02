import sqlite3
import usage_management_system_base_infomation_YMK as info

def login_certification(input_ID, input_password, selected_undergraduate, selected_lab):
    if selected_undergraduate == "理学部": #学部によって扱うデータベースを指定
        db_name = 'user_db_science.db'
    elif selected_undergraduate == "工学部":
        db_name = 'user_db_engineering.db'
    elif selected_undergraduate == "農学部":
        db_name = 'user_db_agriculture.db'
    elif selected_undergraduate == "水産学部":
        db_name = 'user_db_fisheries.db'
    elif selected_undergraduate == "医学部":
        db_name = 'user_db_medicine.db'
    elif selected_undergraduate == "歯学部":
        db_name = 'user_db_dentistry.db'
    elif selected_undergraduate == "法文学部":
        db_name = 'user_db_low_and_literature.db'
    elif selected_undergraduate == "教育学部":
        db_name = 'user_db_education.db'

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    global master_password
    info.offer_master_password() #マスターパスワードをDBから抽出
    try:
        master_password = info.master_password_list[0] #マスターパスワードを取得
    except: #初回のみ
        master_password = "master_initial-password_YMK"

    #入力されたIDが持つパスワードを取得
    select_sql = 'SELECT name, name_ruby, password FROM {} WHERE id = ?'.format(selected_lab) #該当する学部のDBから入力されたIDのパスワードを取得
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
