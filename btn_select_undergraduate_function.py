import usage_management_system_base_infomation_YMK as info #基本情報を提供するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール


#学部選択ボタンを押した際に実行される関数
def select_undergraduate(undergraduate_combobox, window):
    selected_undergraduate = undergraduate_combobox.get() #選択した学部を取得

    if not selected_undergraduate: #学部を選択していない場合
        mes.error("学部を選択してください", window)
        return False
    else:#学部を選択している場合
        info.offer_lab_list(selected_undergraduate) #選択した学部の研究室情報を取得
        lab_list = info.choices_lab #選択した学部の研究室一覧を代入

        #研究室選択の文字とコンボボックスを生成
        genWid.generate_label_widget(window, "研究室・ゼミ : ", 50, 90)
        lab_combobox = genWid.generate_combobox_widget(window, "readonly", lab_list, "研究室選択", 130, 90)

    return selected_undergraduate, lab_combobox
