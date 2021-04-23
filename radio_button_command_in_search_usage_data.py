import convert_widget_state as conWid #ウィジェットを無効化するモジュール

def designate_search_span(function, spin_start_year, combo_start_month, combo_start_day,
spin_finish_year, combo_finish_month, combo_finish_day):

    if function == "not_disignate": #期間を指定していない場合
        #年月日を指定するウィジェットを無効化
        to_disabled_widget_list = [spin_start_year, combo_start_month, combo_start_day,
         spin_finish_year, combo_finish_month, combo_finish_day]
        conWid.to_disabled_widget(to_disabled_widget_list)

    elif function == "disignate": #期間を指定する場合
        #年月日を指定するウィジェットを有効化
        to_normal_widget_list = [spin_start_year, spin_finish_year]
        conWid.to_normal_widget(to_normal_widget_list)

        to_readonly_widget_list = [combo_start_month, combo_start_day, combo_finish_month, combo_finish_day]
        conWid.to_readonly_widget(to_readonly_widget_list)
