import sqlite3
import connect_db as conDB #DBへ接続するモジュール

#利用者情報を格納しているDBのリスト(学部ごと)
db_list = ('user_db_science.db', 'user_db_engineering.db','user_db_agriculture.db',
 'user_db_fisheries.db', 'user_db_medicine.db', 'user_db_dentistry.db',
  'user_db_low_and_literature.db', 'user_db_education.db')
all_user_id_list = [] #登録されている全利用者を格納するリスト
all_table_list = [] #登録されている全研究室を格納するリスト
search_user_name_list = [] #研究室検索において、該当する学部の研究室を格納するリスト

#新規登録の際に使用する関数
def confirm_available_id(reg_id): #登録するIDがすでに存在するか確かめる関数
    for db in db_list: #学部ごとのデータベースを順に処理
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        table_list = [] #table_listを初期化
        table_sql = "SELECT name FROM sqlite_master WHERE TYPE='table'" #データベースのテーブル名を取得するSQL文
        for table in cur.execute(table_sql): #テーブル名を取得
            real_table = table[0] #テーブル名をタプルから抽出
            table_list.append(real_table) #table_listに追加(学部ごとにリセット)

        for now_table_list in table_list: #各テーブルのIDを取得
            for id in cur.execute('SELECT id from {}'.format(now_table_list)): #テーブルのIDを取得
                real_id = id[0] #IDをタプルから抽出
                all_user_id_list.append(real_id) #all_user_id_listに追加

        cur.close()
        conn.close()

    if reg_id in all_user_id_list: #登録しようとするIDがすでに存在した場合
        return False
    else:
        return True


#研究室一覧をDBから抽出する関数
def confirm_reged_lab(reg_lab):
    for db in db_list: #学部ごとのデータベースを順に処理
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        table_list = [] #table_listを初期化

        #データベースのテーブル名を取得するSQL文
        table_sql = "SELECT name FROM sqlite_master WHERE TYPE='table'"
        for table in cur.execute(table_sql): #テーブル名を取得
            real_table = table[0] #テーブル名をタプルから抽出
            all_table_list.append(real_table) #all_table_listに追加

        cur.close()
        conn.close()

    #新規登録者の研究室がすでに登録されている場合
    if reg_lab in all_table_list:
        return True
    else:
        return False


#ログインする際にIDが存在するか確認する関数
def exist_id(input_ID, undergraduate, lab):
    lab_id_list = [] #該当する研究室のIDを格納するリスト
    return_db = conDB.connect_user_db(undergraduate)
    cur = return_db[0]
    conn = return_db[1]
    cur = conn.cursor()

    search_id_sql = ('SELECT id from {}'.format(lab))
    for id in cur.execute(search_id_sql):
        real_id = id[0]
        lab_id_list.append(real_id)

    #入力したIDが存在しない場合
    if input_ID not in lab_id_list:
        return False
    else:
        return True

    cur.close()
    conn.close()
