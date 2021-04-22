
#ウィジェットを無効(disabled)にする関数
def to_disabled_widget(widget_list):
    for widget in widget_list:
        widget['state'] = "disabled"

#ウィジェットを"normal"する関数
def to_normal_widget(widget_list):
    for widget in widget_list:
        widget['state'] = "normal"

#ウィジェットを"readonly"にする関数
def to_readonly_widget(widget_list):
    for widget in widget_list:
        widget['state'] = "readonly"

#ウィジェットを"active"にする関数
def to_active_widget(widget_list):
    for widget in widget_list:
        widget['state'] = "active"
