import tkinter as tk #GUI作成のためのライブラリ
import make_window as mw #ウィンドウを作成するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import usage_management_system_base_infomation as info #基本情報を提供するモジュール
import btn_select_undergraduate_function as btnUnder #研究室表示ボタンを押した際に実行される処理
import btn_del_user #登録情報の削除ボタンを押した際の処理


#登録者を削除する画面
def delete_user():
    delete_user_window = mw.make_window("登録者 削除画面", '500x310')

    #学部選択の文字とコンボボックスを生成、配置
    genWid.generate_label_widget(delete_user_window, "学部 : ", 85, 20)
    delete_user_undergraduate_combobox = genWid.generate_combobox_widget(
        delete_user_window, "readonly", info.undergraduate_list, "学部選択", 150, 20)

    #研究室・ゼミ選択の文字を表示
    genWid.generate_label_widget(delete_user_window, "研究室・ゼミ : ", 50, 60)

    #ID、パスワードの入力欄を生成
    genWid.generate_label_widget(delete_user_window, "ユーザーID : ", 61, 120)
    del_txt_id = genWid.generate_entry_widget(delete_user_window, 30, 150, 120)

    genWid.generate_label_widget(delete_user_window, "パスワード : ", 64, 160)
    del_txt_password = genWid.generate_entry_widget(delete_user_window, 30, 150, 160, "*")


    #学部選択のボタンを生成、配置、コマンド指定
    btn_search_name_undergraduate = tk.Button(delete_user_window, text='学部の研究室・ゼミを表示')
    btn_search_name_undergraduate.place(x=320, y=20)
    btn_search_name_undergraduate['command'] = lambda: btnUnder.select_undergraduate(
     delete_user_window, "delete_user", delete_user_undergraduate_combobox, 150, 60)

    #登録者削除ボタンを生成、配置、コマンド指定
    btn_delete_user = tk.Button(delete_user_window, text='登録情報を削除する', height=2, width=15, bg="red")
    btn_delete_user.place(x=190, y=250)
    btn_delete_user['command'] = lambda: btn_del_user.delete_user_btn(
    delete_user_window, del_txt_id, del_txt_password, delete_user_undergraduate_combobox)

    delete_user_window.mainloop()
