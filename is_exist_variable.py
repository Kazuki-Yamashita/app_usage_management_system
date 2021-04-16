import show_message as mes #メッセージボックスを表示するモジュール


def is_exist_variable(var, message, window):
    try:
        var
    except NameError:
        mes.error(message, window)
        return
