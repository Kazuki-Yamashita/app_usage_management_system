import tkinter as tk #GUI作成のためのライブラリ
import convert_widget_state as conWid #ウィジェットを無効化するモジュール


#検索結果の削除ボタンを押した際の処理
def btn_del_result(result_label, search_user_undergraduate_combobox,
        btn_search_name_undergraduate, lab_combobox, btn_exe_search, btn_del):

    #検索結果を表示するラベルを削除
    result_label.destroy()

    #検索結果の削除ボタンを無効化
    to_disabled_widget_list = [btn_del]
    conWid.to_disabled_widget(to_disabled_widget_list)

    #学部選択ボタン、検索ボタンを有効化
    to_normal_widget_list = [btn_search_name_undergraduate, btn_exe_search]
    conWid.to_normal_widget(to_normal_widget_list)

    #学部のコンボボックス、研究室・ゼミのコンボボックスを有効化(読み取りのみ)
    to_readonly_widget_list = [search_user_undergraduate_combobox, lab_combobox]
    conWid.to_readonly_widget(to_readonly_widget_list)
