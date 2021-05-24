import show_message as mes #メッセージボックスを表示するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import convert_widget_state as conWid #ウィジェットを無効化するモジュール
import is_input_entry #研究室の選択の有無を判定するモジュール
import usage_management_system_base_infomation as info #基本情報を提供するモジュール
import btn_select_undergraduate_function as btnUnder #研究室表示ボタンを押した際に実行される処理


#利用者検索の検索ボタンを押した際の処理
def btn_search_user_name(window, search_user_undergraduate_combobox,
    btn_exe_search, btn_search_user_name_undergraduate, lab_combobox, btn_del):

    display = "" #初期化(空にする)
    search_user_name_dict = {}

    #選択した学部を取得
    search_user_name_undergraduate = search_user_undergraduate_combobox.get()
    #選択した学部の研究室一覧を取得(リスト)
    lab_list = info.offer_lab_list(search_user_name_undergraduate)

    #学部を選択していない場合
    if not search_user_name_undergraduate:
        mes.error("学部を選択してください", window)
        return

    try: #研究室のコンボボックスが表示されていない状態で検索ボタンを押したか判定
        btnUnder.search_user_lab_list
    except: #研究室一覧が取得されていない(学部を選択していない)場合
        mes.error("研究室・ゼミを選択してください", window)
        return


    try: #選択した研究室を取得
        search_user_name_lab = btnUnder.lab_combobox_search_user.get()
    except:
        mes.error("研究室・ゼミを選択してください", window)
        return

    global result_label

    #研究室の選択が適切かどうか判定(True or False)
    is_input_lab = is_input_entry.is_select_lab(window, search_user_name_lab, lab_list)

    #研究室の選択が適切な場合(True)
    if is_input_lab:
        #選択した研究室の利用者の名前とフリガナを取得
        search_user_name_dict = info.offer_user_name(search_user_name_undergraduate, search_user_name_lab)

        #表示する結果を変数に代入
        for disp_id in search_user_name_dict:
            display = display + "・" + str(search_user_name_dict[disp_id]) + "(" + str(disp_id) + ")\n"
        if len(search_user_name_dict) == 0: #登録者がいない場合
            display = "登録されていません"

        #登録者を表示するラベルを生成
        result_label = genWid.generate_label_widget(window, display, 20, 150)
        result_label["bg"] = "white"

        #無効化するウィジェットをリスト化
        disabled_widget_list = [btn_exe_search, search_user_undergraduate_combobox, btn_search_user_name_undergraduate, lab_combobox]
        conWid.to_disabled_widget(disabled_widget_list) #指定したウィジェットを無効化
        #検索結果の削除ボタンを有効化
        conWid.to_normal_widget([btn_del])
