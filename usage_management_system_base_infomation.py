import sqlite3
import datetime
import connect_db as conDB #DBへ接続するモジュール


#学部のリスト
undergraduate_list = ["理学部","工学部","農学部","水産学部","医学部",
"歯学部","法文学部","教育学部"]


#選択した学部の研究室情報を提供する関数
def offer_lab_list(undergraduate, type="normal"):
    choices_lab = []
    choices_lab.clear() #リストの初期化

    #使用履歴の検索の場合
    if type == "usage data":
        return_db = conDB.connect_db(undergraduate, "usage")
    #使用履歴の検索以外の場合
    else:
        return_db = conDB.connect_db(undergraduate, "user")

    if not return_db:
        return False

    cur = return_db[0]
    conn = return_db[1]

    table_sql = "SELECT name FROM sqlite_master WHERE TYPE='table'"
    for table in cur.execute(table_sql): #テーブル名を取得
        real_table = table[0] #テーブル名をタプルから抽出
        choices_lab.append(real_table) #choices_labに追加

    choices_lab.sort()
    return choices_lab

    cur.close()
    conn.close()


#選択した研究室の利用登録者を提供する関数
def offer_user_name(search_undergraduate, search_name_lab):
    #DBへ接続
    return_db = conDB.connect_db(search_undergraduate, "user")
    cur = return_db[0]
    conn = return_db[1]

    user_name_dict = {} #利用者の名前とフリガナを格納する辞書
    user_name_dict.clear()

    name_sql = "SELECT name,id FROM {}".format(search_name_lab)
    for name in cur.execute(name_sql):
        real_name = name[0]
        real_id = name[1]
        user_name_dict[real_id] = real_name #フリガナを辞書のキーに、名前を値に代入

    return user_name_dict

    cur.close()
    conn.close()


#使用歴の情報を提供する関数
def offer_used_data(undergraduate, lab, desig_ornot, start_day, finish_day):
    #DBへ接続
    return_db = conDB.connect_db(undergraduate, "usage")
    cur = return_db[0]
    conn = return_db[1]

    #研究室のテーブルが存在しない場合、テーブルを作成
    create_sql = 'CREATE TABLE IF NOT EXISTS {}(id text, name text, name_ruby text, start_time text, finish_time text, using_time text, memo text)'.format(lab)
    cur.execute(create_sql) #実行
    #使用歴を抽出するSQL文
    sql = "SELECT id, name, name_ruby, start_time, finish_time, using_time, memo FROM {}".format(lab)
    usage_record_list = [] #使用歴リストを格納するリスト

    for record in cur.execute(sql):
        data_list = [] #リストを初期化
        id_data = record[0]
        name_data = record[1]
        name_ruby_data = record[2]
        start_time_data = record[3]
        finish_time_data = record[4]
        using_time_data = record[5]
        memo_data = record[6]

        data_list = [id_data, name_data, name_ruby_data, start_time_data, finish_time_data, using_time_data, memo_data]
        if desig_ornot == "no": #検索期間を指定していない場合
            #1回分の使用履歴のリストを、使用歴をまとめるリストに代入
            usage_record_list.append(data_list)
        elif desig_ornot == "yes": #検索期間を措定している場合
            #DBから抽出した日付の文字列を、日付の型に変換
            datetype_start_time_data = datetime.datetime.strptime(start_time_data, '%Y-%m-%d %H:%M:%S')
            #DBから抽出した日付が検索期間内の場合
            if datetype_start_time_data >= start_day and datetype_start_time_data <= finish_day:
                usage_record_list.append(data_list) #リストに追加

    return usage_record_list

    conn.commit() #データベースへの反映
    cur.close()
    conn.close() #データベースを閉じる


#マスターパスワードの情報を提供する関数
def offer_master_password():
    master_password_list = [] #登録されているマスターパスワードを格納する変数

    db_name = 'master_password_db.db'
    conn = sqlite3.connect(db_name) #マスターパスワードのDBに接続
    cur = conn.cursor()

    #テーブルが存在しない場合、テーブルを作成(初回)
    create_sql = 'CREATE TABLE IF NOT EXISTS master (master_password)'
    cur.execute(create_sql) #実行

    #マスターパスワードを抽出するSQL文
    select_sql = 'SELECT master_password FROM master'

    #登録されているマスターパスワードをDBから抽出
    for password in cur.execute(select_sql):
        master_password_list.append(password[0])

    if not master_password_list: #パスワードが設定されていない場合(初回のみ)
        insert_sql = 'INSERT INTO master values (?)'
        initial_password = ["master_initial-password_YMK"]

        cur.execute(insert_sql, initial_password) #初期のマスターパスワードを設定
        master_password_list.append("master_initial-password_YMK")

    conn.commit() #データベースへの反映
    cur.close()
    conn.close() #データベースを閉じる

    return master_password_list[0]
