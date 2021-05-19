import tkinter as tk #GUI作成のためのライブラリ
import usage_management_system_base_infomation as info #基本情報を含むモジュール
import delete_lab_from_DB as delLabDB #DBから研究室・ゼミを削除するモジュール
import btn_select_undergraduate_function as btnUnder #学部選択ボタンを押した際に実行される処理
import show_message as mes #メッセージボックスを表示するモジュール

#研究室・ゼミの削除ボタンを押した際の処理
def btn_delete_lab(window, delete_lab_undergraduate_combobox):
      delete_lab_undergraduate = delete_lab_undergraduate_combobox.get() #学部を取得

      #選択した学部の研究室情報を取得
      info.offer_lab_list(delete_lab_undergraduate)
      lab_list = info.choices_lab #研究室リストを代入

      try: #選択した研究室を取得
          delete_lab_lab = btnUnder.lab_combobox.get()
      except:
          delete_lab_lab = False
          return

      if not delete_lab_lab:
          mes.error("研究室・ゼミを選択してください", window)
          return
      elif delete_lab_lab not in lab_list:
          mes.error("選択した学部と研究室・ゼミが一致していません", window)
          return
      else:
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
