import sqlite3
import connect_db as conDB #DBへ接続するモジュール

#登録者を削除する関数
def delete_user_from_DB(undergraduate, lab, id):
    return_db = conDB.connect_user_db(undergraduate)
    cur = return_db[0]
    conn = return_db[1]

    sql = 'DELETE FROM {} WHERE id = ?'.format(lab)
    delete_id = [id]

    try:
        cur.execute(sql, delete_id) #削除を実行
    except:
        return False

    conn.commit() #データベースへの反映
    cur.close()
    conn.close() #データベースを閉じる

    return True
