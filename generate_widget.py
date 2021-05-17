import tkinter as tk
import tkinter.ttk #コンボボックスを扱うライブラリ

#各ウィジェットを生成する関数

def generate_label_widget(window, text, x, y, fg="black"):
    label = tk.Label(window, text=text, fg=fg)
    label.place(x=x, y=y)
    return label

def generate_entry_widget(window, width, x, y, show=None):
    entry = tk.Entry(window, width=width, show=show)
    entry.place(x=x, y=y)
    return entry

def generate_combobox_widget(window, state, values, text, x, y, width=None):
    combobox = tk.ttk.Combobox(window, state=state, values=values, text=text, width=width)
    combobox.place(x=x, y=y)
    return combobox

def generate_spinbox_widget(window, state, from_, to, increment, x, y, width):
    spinbox = tkinter.ttk.Spinbox(window, state=state, from_=from_, to=to, increment=increment)
    spinbox.place(x=x, y=y, width=width)
    return spinbox

def generate_message_widget(window, text, width, bg, x, y):
    message = tkinter.Message(window, width=width, bg=bg, text=text)
    message.place(x=x, y=y)
    return message

def generate_button_widget(window, text, command, bg, height, width, x, y):
    btn = tk.Button(window, text=text, command=lambda: command, bg=bg, height=height, width=width)
    btn.place(x=x, y=y) #新規登録ボタンを配置
    return btn
