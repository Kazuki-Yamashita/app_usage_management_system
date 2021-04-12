import tkinter.messagebox #メッセージボックスを扱うライブラリ

def error(contents, window):
    tkinter.messagebox.showerror("エラー", contents, parent=window)

def info(title, contents, window):
    tkinter.messagebox.showinfo(title, contents, parent=window)

def askokcancel(title, contents, window):
    ok_cancel = tkinter.messagebox.askokcancel(title, contents, parent=window)
    return ok_cancel

def askyesno(title, contents, window):
    yes_no = tkinter.messagebox.askyesno(title, contents, parent=window)
    return yes_no
