import usage_management_system_base_infomation as info #基本情報を提供するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール

#変数の用意
selected_undergraduate = False

#学部選択ボタンを押した際に実行される関数
def select_undergraduate(undergraduate_combobox, window):
    #選択した学部を取得
    selected_undergraduate = undergraduate_combobox.get()

    global lab_list, lab_combobox
    if not selected_undergraduate: #学部を選択していない場合
        mes.error("学部を選択してください", window)
        return False
    else:#学部を選択している場合
        #選択した学部の研究室情報を取得
        info.offer_lab_list(selected_undergraduate)

        #選択した学部の研究室一覧を代入
        lab_list = info.choices_lab

        #研究室・ゼミ選択コンボボックスを生成
        lab_combobox = genWid.generate_combobox_widget(window,
         "readonly", lab_list, "研究室選択", 130, 90)
