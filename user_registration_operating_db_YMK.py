import sqlite3
import connect_db as conDB #DBへ接続するモジュール

#データベースの操作を行う
def registration_user(reg_id, reg_name, reg_ruby_name, reg_undergraduate, reg_lab, password1, reg_time):
    #DBへ接続する
    return_db = conDB.connect_user_db(reg_undergraduate)
    cur = return_db[0]
    conn = return_db[1]

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
