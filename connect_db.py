import sqlite3

def connect_user_db(undergraduate): #登録者を保管するDBへ接続する関数
    #学部によって扱うデータベースを指定
    if undergraduate == "理学部":
        db_name = 'user_db_science.db'
    elif undergraduate == "工学部":
        db_name = 'user_db_engineering.db'
    elif undergraduate == "農学部":
        db_name = 'user_db_agriculture.db'
    elif undergraduate == "水産学部":
        db_name = 'user_db_fisheries.db'
    elif undergraduate == "医学部":
        db_name = 'user_db_medicine.db'
    elif undergraduate == "歯学部":
        db_name = 'user_db_dentistry.db'
    elif undergraduate == "法文学部":
        db_name = 'user_db_low_and_literature.db'
    elif undergraduate == "教育学部":
        db_name = 'user_db_education.db'

    #該当する学部のDBに接続
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    return cur, conn

def connect_usage_db(undergraduate): #使用歴を保管するDBへ接続する関数
    if undergraduate == "理学部":
        db_name = 'usage_record_db_science.db'
    elif undergraduate == "工学部":
        db_name = 'usage_record_db_engineering.db'
    elif undergraduate == "農学部":
        db_name = 'usage_record_db_agriculture.db'
    elif undergraduate == "水産学部":
        db_name = 'usage_record_db_fisheries.db'
    elif undergraduate == "医学部":
        db_name = 'usage_record_db_medicine.db'
    elif undergraduate == "歯学部":
        db_name = 'usage_record_db_dentistry.db'
    elif undergraduate == "法文学部":
        db_name = 'usage_record_db_low_and_literature.db'
    elif undergraduate == "教育学部":
        db_name = 'usage_record_db_education.db'

    #該当する学部のDBに接続
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    return cur, conn
