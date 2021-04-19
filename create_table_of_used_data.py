import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import tkinter.filedialog as fd
import csv
import tkinter as tk
import tkinter.messagebox
import show_message as mes #メッセージボックスを表示するモジュール


def create_table(data, search_used_data_window): #使用歴を表として出力する関数
    df = pd.DataFrame(data) #データフレーム作成
    df.columns = ['id','名前','フリガナ','使用開始日時','使用終了日時','使用時間(s)','備考']
    print(df)
    """
    df.to_csv("output_file.csv", encoding="shift_jis", index=False) #csvファイルとして出力
    """

    file = fd.asksaveasfilename(initialfile="data", defaultextension=".csv", title="名前を付けて保存")

    if file:
        df.to_csv(file, encoding="shift_jis", index=False)
        mes.info("使用歴の出力 完了", "使用歴をCSVで出力しました", search_used_data_window)
        #tk.messagebox.showinfo("使用歴の出力 完了", "使用歴をCSVで出力しました")
    else:
        return False
