import usage_management_system_base_infomation as info #基本情報を提供するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール


#変数の用意
selected_undergraduate = False
lab_combobox = False

lab_combobox_login = False #ログイン画面の学部
lab_combobox_search_user = False #利用者検索画面の学部
lab_combobox_search_usage_data = False #使用歴検索画面の学部
lab_combobox_delete_user = False #利用者削除画面の学部
lab_combobox_delete_lab = False #研究室・ゼミ削除画面の学部


#研究室表示ボタンを押した際に実行される関数
def select_undergraduate(window, function, undergraduate_combobox, x, y):

    #選択した学部を取得
    selected_undergraduate = undergraduate_combobox.get()

    #学部を選択されていない場合、メッセージを表示
    if not selected_undergraduate:
        mes.error("学部を選択してください", window)
        return

    global login_lab_list, search_user_lab_list, search_usage_data_lab_list, delete_user_lab_list, delete_lab_lab_list
    global lab_combobox_login, lab_combobox_search_user, lab_combobox_search_usage_data, lab_combobox_delete_user, lab_combobox_delete_lab

    if function == "login":
        login_lab_list = info.offer_lab_list(selected_undergraduate)
        lab_combobox_login = genWid.generate_combobox_widget(window,
         "readonly", login_lab_list, "研究室選択", x, y)

    elif function == "search_user":
        search_user_lab_list = info.offer_lab_list(selected_undergraduate)
        lab_combobox_search_user = genWid.generate_combobox_widget(window,
         "readonly", search_user_lab_list, "研究室選択", x, y)

    elif function == "search_usage_data":
        search_usage_data_lab_list = info.offer_lab_list(selected_undergraduate)
        lab_combobox_search_usage_data = genWid.generate_combobox_widget(window,
         "readonly", search_usage_data_lab_list, "研究室選択", x, y)

    elif function == "delete_user":
        delete_user_lab_list = info.offer_lab_list(selected_undergraduate)
        lab_combobox_delete_user = genWid.generate_combobox_widget(window,
         "readonly", delete_user_lab_list, "研究室選択", x, y)

    elif function == "delete_lab":
        delete_lab_lab_list = info.offer_lab_list(selected_undergraduate)
        lab_combobox_delete_lab = genWid.generate_combobox_widget(window,
         "readonly", delete_lab_lab_list, "研究室選択", x, y)
