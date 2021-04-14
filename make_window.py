import tkinter as tk

def make_window(title, size):
    window = tk.Tk() #ウィンドウの作成
    window.title(title) #ウィンドウのタイトル
    window.geometry(size) #ウィンドウの大きさを指定

    return window
