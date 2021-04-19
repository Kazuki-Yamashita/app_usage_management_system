import tkinter as tk
import show_message as mes #メッセージボックスを表示するモジュール


def text_off(memo): #「異常なし」のボタンを押した場合
    memo['state'] = 'disabled' #テキストに書き込めない状態にする

def text_on(memo): #「不具合あり」のボタンを押した場合
    memo['state'] = 'normal' #テキストに書き込める状態にする

def text_delete(window, memo_text, var):
    #入力内容を削除するかの確認画面の表示
    memo_delete_confirmation = mes.askokcancel("テキストの削除",
     "入力した内容を全て削除しますか？", window)
     
    if memo_delete_confirmation: #「OK」を押した場合
        text_on(memo_text) #テキストを編集可能にする
        memo_text.delete("1.0",tk.END) #内容を全て削除する

        #削除した際に「異常なし」を選んでいた場合
        if var.get() == 0:
            text_off(memo_text) #テキストを編集不可にする
