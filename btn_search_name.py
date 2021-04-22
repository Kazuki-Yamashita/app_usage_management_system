import usage_management_system_base_infomation as info #基本情報を含むモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import btn_select_undergraduate_function as btnUnder #学部選択ボタンを押した際に実行される処理
import convert_widget_state as conWid #ウィジェットを無効化するモジュール
import show_message as mes #メッセージボックスを表示するモジュール


def btn_search_name(window, search_user_undergraduate_combobox,
    btn_exe_search, btn_search_name_undergraduate, lab_combobox, btn_del):

    display = "" #初期化(空にする)
    search_name_dict = {}

    #選択した研究室を取得
    search_undergraduate = search_user_undergraduate_combobox.get()

    try:
        btnUnder.lab_list
    except: #研究室一覧が取得されていない(学部を選択していない)場合
        mes.error("学部を選択してください", window)
        return

    search_lab_list = btnUnder.lab_list #選択した学部の研究室一覧を代入
    searching_lab = btnUnder.lab_combobox.get() #検索する研究室を取得
    global result_label

    if not searching_lab: #研究室を選択していない場合
        mes.error("研究室を選択してください", window)
    elif searching_lab not in search_lab_list: #選択した学部と研究室・ゼミが一致しない場合
        mes.error("選択した学部と研究室・ゼミが一致していません", window)
    else:
        print(search_undergraduate)
        print(searching_lab)
        info.offer_user_name(search_undergraduate, searching_lab) #選択した研究室の利用者の名前とフリガナを取得
        search_name_dict.clear() #利用者の名前とフリガナを格納する辞書を初期化(空にする)
        search_name_dict = info.user_name_dict #利用者の名前とフリガナの辞書を代入

        for disp_id in search_name_dict:
            display = display + "・" + str(search_name_dict[disp_id]) + "(" + str(disp_id) + ")\n"
        if len(search_name_dict) == 0: #登録者がいない場合
            display = "登録されていません"
        result_label = genWid.generate_label_widget(window, display, 20, 150) #登録者を表示するラベル
        result_label["bg"] = "white"

        #無効化するウィジェットをリスト化
        disabled_widget_list = [btn_exe_search, search_user_undergraduate_combobox, btn_search_name_undergraduate, lab_combobox]
        conWid.to_disabled_widget(disabled_widget_list) #指定したウィジェットを無効化
        #検索結果の削除ボタンを有効化
        conWid.to_normal_widget([btn_del])
