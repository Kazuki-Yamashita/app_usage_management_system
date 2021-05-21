import tkinter as tk #GUI作成のためのライブラリ
import usage_management_system_base_infomation as info #基本情報を含むモジュール
import delete_lab_from_DB as delLabDB #DBから研究室・ゼミを削除するモジュール
import btn_select_undergraduate_function as btnUnder #研究室表示ボタンを押した際に実行される処理
import show_message as mes #メッセージボックスを表示するモジュール
import is_input_entry #研究室の選択の有無を判定するモジュール


#研究室・ゼミの削除ボタンを押した際の処理
def btn_delete_lab(window, delete_lab_undergraduate_combobox):

    #選択した学部を取得
    delete_lab_undergraduate = delete_lab_undergraduate_combobox.get()
    #選択した学部の研究室一覧を取得(リスト)
    lab_list = info.offer_lab_list(delete_lab_undergraduate)

    #学部を選択していない場合
    if not delete_lab_undergraduate:
        mes.error("学部を選択してください", window)
        return

    try: #研究室のコンボボックスが表示されていない状態で検索ボタンを押したか判定
        btnUnder.delete_lab_lab_list
    except:
        mes.error("研究室・ゼミを選択してください", window)
        return

    #選択した研究室を取得
    delete_lab_lab = btnUnder.lab_combobox_delete_lab.get()

    #研究室の選択が適切かどうか判定(True or False)
    is_input_lab = is_input_entry.is_select_lab(window, delete_lab_lab, lab_list)

    #研究室の選択が適切な場合(True)
    if is_input_lab:
        message = "本当に研究室・ゼミを削除しますか？"
        #研究室・ゼミ削除の確認画面
        delete_lab_confirmation = tk.messagebox.askokcancel("研究室・ゼミ削除 確認画面", message, parent=window)

    if delete_lab_confirmation == True: #「OK」を押した場合
        final_message = "研究室・ゼミを削除した場合、該当する研究室・ゼミの利用登録者の情報も削除されます。\n使用履歴は削除されません"
        #研究室・ゼミ削除の最終確認画面
        delete_lab_final_confirmation = tk.messagebox.askokcancel("研究室・ゼミ削除 最終確認画面", final_message, parent=window)

        #最終確認で「OK」を押した場合
        if delete_lab_final_confirmation == True:
            #研究室・ゼミをDBから削除
            delete_lab_ornot = delLabDB.delete_lab_from_DB(delete_lab_undergraduate, delete_lab_lab)
            if delete_lab_ornot == False: #削除できなかった場合
                mes.error("研究室・ゼミの削除に失敗しました", window)
                return
            else: #削除できた場合
                mes.info("登録者削除 完了", "登録者の削除を完了しました", window)
                window.destroy()
