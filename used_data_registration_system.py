import sqlite3
import connect_db as conDB #DBへ接続するモジュール


#使用歴をDBに登録する関数
def used_data_registration(undergraduate, lab, id, name, name_ruby, start_time, finish_time, using_second_time, memo):
    return_db = conDB.connect_usage_db(undergraduate)
    cur = return_db[0]
    conn = return_db[1]

    #使用開始時間を文字列に変換
    reg_start_time = start_time.isoformat(' ', timespec='seconds')
    #使用終了時間を文字列に変換
    reg_finish_time = finish_time.isoformat(' ', timespec='seconds')

    #研究室のテーブルが存在しない場合、テーブルを作成
    create_sql = 'CREATE TABLE IF NOT EXISTS {}(id text, name text, name_ruby text, start_time, finish_time, using_time, memo text)'.format(lab)
    cur.execute(create_sql) #研究室のテーブルを作成

    #以下、データを追加するSQL文
    sql = 'INSERT INTO {} values (?,?,?,?,?,?,?)'.format(lab)
    #追加するデータをリスト化
    data = [id, name, name_ruby, reg_start_time, reg_finish_time, using_second_time, memo]

    try: #DBへデータを追加
        cur.execute(sql, data)
    except:
        return False

    conn.commit() #データベースへの反映
    cur.close()
    conn.close() #データベースを閉じる
