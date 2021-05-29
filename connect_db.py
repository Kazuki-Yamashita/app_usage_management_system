import sqlite3
import usage_management_system_base_infomation as info #基本情報を提供するモジュール


user_db_dict = {"理学部":'user_db_science.db', "工学部":'user_db_engineering.db',
 "農学部":'user_db_agriculture.db', "水産学部":'user_db_fisheries.db',
 "医学部":'user_db_medicine.db', "歯学部":'user_db_dentistry.db',
 "法文学部":'user_db_low_and_literature.db', "教育学部":'user_db_education.db'}

usage_db_dict = {"理学部":'usage_record_db_science.db', "工学部":'usage_record_db_engineering.db',
 "農学部":'usage_record_db_agriculture.db', "水産学部":'usage_record_db_fisheries.db',
 "医学部":'usage_record_db_medicine.db', "歯学部":'usage_record_db_dentistry.db',
 "法文学部":'usage_record_db_low_and_literature.db', "教育学部":'usage_record_db_education.db'}

def connect_db(undergraduate, user_or_usage):
    #選択した学部が適切でない場合
    if undergraduate not in info.undergraduate_list:
        return False

    #学部をもとに接続するDBを指定
    if user_or_usage == "user":
        db_name = user_db_dict[undergraduate]
    elif user_or_usage == "usage":
        db_name = usage_db_dict[undergraduate]

    #該当する学部のDBに接続
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    return cur, conn
