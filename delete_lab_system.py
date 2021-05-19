import tkinter as tk #GUI作成のためのライブラリ
import tkinter.messagebox #メッセージボックスを扱うライブラリ
import usage_management_system_base_infomation as info #基本情報を含むモジュール
import delete_lab_from_DB as delLabDB #DBから研究室・ゼミを削除するモジュール
import generate_widget as genWid #ウィジェット生成するモジュール
import show_message as mes #メッセージボックスを表示するモジュール
import make_window as mw #ウィンドウを作成するモジュール
import btn_select_undergraduate_function as btnUnder #学部選択ボタンを押した際に実行される処理
import btn_del_lab

#研究室の削除画面
def delete_lab():
    delete_lab_window = mw.make_window("研究室・ゼミ 削除画面", '500x310')

    genWid.generate_label_widget(delete_lab_window, "学部 : ", 85, 20)
    delete_lab_undergraduate_combobox = genWid.generate_combobox_widget(
                delete_lab_window, "readonly", info.undergraduate_list, "学部選択", 150, 20)

    genWid.generate_label_widget(delete_lab_window, "研究室・ゼミ : ", 50, 60)

    #学部選択のボタンを生成、配置、コマンド指定
    btn_search_name_undergraduate = tk.Button(delete_lab_window, text='学部を選択')
    btn_search_name_undergraduate.place(x=320, y=20)
    btn_search_name_undergraduate['command'] = lambda: btnUnder.select_undergraduate(
     delete_lab_undergraduate_combobox, delete_lab_window, 150, 60)

    #「研究室・ゼミの削除」ボタンを生成、配置、コマンド指定
    btn_delete_lab = tk.Button(delete_lab_window, text='研究室・ゼミを削除する', height=2, width=18, bg="red")
    btn_delete_lab.place(x=190, y=250)
    btn_delete_lab['command'] = lambda: btn_del_lab.btn_delete_lab(delete_lab_window,
     delete_lab_undergraduate_combobox)

    delete_lab_window.mainloop()
