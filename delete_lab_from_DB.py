import sqlite3
import connect_db as conDB #DBへ接続するモジュール

#登録者を削除する関数
def delete_lab_from_DB(undergraduate, lab):
    #DBへ接続
    return_db = conDB.connect_db(undergraduate, "user")
    cur = return_db[0]
    conn = return_db[1]

    sql = 'DROP TABLE {}'.format(lab)

    try:
        cur.execute(sql) #テーブルの削除を実行
        cur.execute('VACUUM') #使用していないDBの領域を解放
    except:
        return False

    conn.commit() #データベースへの反映
    cur.close()
    conn.close() #データベースを閉じる

    return True
