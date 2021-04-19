import sqlite3

def change_master_password_DB(current_master_password, new_master_password): #DBのマスターパスワードを変更する関数
    db_name = 'master_password_db.db'
    conn = sqlite3.connect(db_name) #マスターパスワードのDBに接続
    cur = conn.cursor()

    #レコードを更新するSQL
    update_sql = 'UPDATE master SET master_password = ? WHERE master_password = ?'
    try:
        cur.execute(update_sql, (new_master_password, current_master_password)) #マスターパスワードを更新
    except:
        return False

    conn.commit() #データベースへの反映
    cur.close()
    conn.close() #データベースを閉じる
