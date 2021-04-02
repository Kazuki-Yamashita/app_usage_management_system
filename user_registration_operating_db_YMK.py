import sqlite3

def registration_user(reg_id, reg_name, reg_ruby_name, reg_undergraduate, reg_lab, password1, reg_time): #データベースの操作を行う
    global conn
    if reg_undergraduate == "理学部": #学部によって扱うデータベースを指定
        db_name = 'user_db_science.db'
    elif reg_undergraduate == "工学部":
        db_name = 'user_db_engineering.db'
    elif reg_undergraduate == "農学部":
        db_name = 'user_db_agriculture.db'
    elif reg_undergraduate == "水産学部":
        db_name = 'user_db_fisheries.db'
    elif reg_undergraduate == "医学部":
        db_name = 'user_db_medicine.db'
    elif reg_undergraduate == "歯学部":
        db_name = 'user_db_dentistry.db'
    elif reg_undergraduate == "法文学部":
        db_name = 'user_db_low_and_literature.db'
    elif reg_undergraduate == "教育学部":
        db_name = 'user_db_education.db'

    conn = sqlite3.connect(db_name) #該当する学部のデータベースに接続
    cur = conn.cursor()

    #テーブル作成のクエリ
    create_sql = 'CREATE TABLE IF NOT EXISTS {}(id text, name text, name_ruby text, undergraduate text, lab_name text, password text, reg_time)'.format(reg_lab)

    #新規の研究室の場合、テーブルを作成
    cur.execute(create_sql)

    #レコード挿入のクエリを作成
    insert_sql = 'INSERT INTO {} values (?,?,?,?,?,?,?)'.format(reg_lab)
    insert_data = [reg_id, reg_name, reg_ruby_name, reg_undergraduate, reg_lab, password1, reg_time]
    #利用者を登録
    try:
        cur.execute(insert_sql, insert_data)
    except: #登録できなかった場合
        return False

    conn.commit() #データベースへの反映
    cur.close()
    conn.close() #データベースを閉じる
