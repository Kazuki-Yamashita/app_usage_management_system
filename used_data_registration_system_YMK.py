import sqlite3
import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ

def used_data_registration(undergraduate, lab, id, name, name_ruby, start_time, finish_time, using_second_time, memo):
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

    reg_start_time = start_time.isoformat(' ', timespec='seconds') #使用開始時間を文字列に変換
    reg_finish_time = finish_time.isoformat(' ', timespec='seconds') #使用終了時間を文字列に変換

    conn = sqlite3.connect(db_name) #該当する学部のデータベースに接続
    cur = conn.cursor()

    #研究室のテーブルが存在しない場合、テーブルを作成
    create_sql = 'CREATE TABLE IF NOT EXISTS {}(id text, name text, name_ruby text, start_time, finish_time, using_time, memo text)'.format(lab)
    cur.execute(create_sql) #研究室のテーブルを作成

    #以下、データを追加するSQL文
    sql = 'INSERT INTO {} values (?,?,?,?,?,?,?)'.format(lab)
    data = [id, name, name_ruby, reg_start_time, reg_finish_time, using_second_time, memo] #追加するデータを指定
    try:
        cur.execute(sql, data) #DBへデータを追加
    except:
        return False

    conn.commit() #データベースへの反映
    cur.close()
    conn.close() #データベースを閉じる
