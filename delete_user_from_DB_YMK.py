import sqlite3

def delete_user_from_DB(undergraduate, lab, id): #登録者を削除する関数
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

    conn = sqlite3.connect(db_name) #該当する学部のデータベースに接続
    cur = conn.cursor()

    sql = 'DELETE FROM {} WHERE id = ?'.format(lab)
    delete_id = [id]

    try:
        cur.execute(sql, delete_id) #削除を実行
    except:
        return False

    conn.commit() #データベースへの反映
    cur.close()
    conn.close() #データベースを閉じる