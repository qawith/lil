define dr_current_next_value = 0

screen menu_tile(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

    label title

screen close_button(screen_to_hide_name, x, y):

    imagebutton:
        xpos x ypos y
        idle 'gui/exit_cross.png'
        action [
            Hide(screen_to_hide_name),
        ]
        if renpy.variant("pc"):
            focus_mask True
        at dr_close_button_transform

screen back_button(screen_to_hide_name, screen_to_show_name, x, y):

    imagebutton:
        xpos x ypos y
        idle 'gui/back_button.png'
        action [
            Hide(screen_to_hide_name), ToggleScreen(screen_to_show_name), With(dissolve)
        ]
        if renpy.variant("pc"):
            focus_mask True
        at dr_close_button_transform