def disabled_widget(widget_list): #ウィジェットを無効化する関数
    for widget in widget_list:
        widget['state'] = "disabled"
