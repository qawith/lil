style dr_menu_vscroll is vscrollbar:
    xsize 7
    unscrollable 'hide'

init:
    transform nqtr_button_room_transform:
        size (gui.nqtr_button_room_size, gui.nqtr_button_room_size)
        on selected_idle:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 1 alpha 0.9 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 1 alpha 0.9 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.5)
    transform nqtr_button_location_transform:
        size (gui.nqtr_button_location_size, gui.nqtr_button_location_size)
        on selected_idle:
            yanchor 0 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 1 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 1 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform nqtr_button_action_transform:
        size (gui.nqtr_button_action_size, gui.nqtr_button_action_size)
        on selected_idle:
            yanchor 0 alpha 0.7
        on idle:
            yanchor 0 alpha 0.7
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform nqtr_button_action_picture_transform:
        on selected_idle:
            yanchor 0 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform dr_small_face_transform:
        size (gui.dr_small_face_size, gui.dr_small_face_size)
        on selected_idle:
            yanchor 0 alpha 1.0
        on idle:
            yanchor 0 alpha 1.0
        on hover:
            yanchor 1 alpha 0.93
        on selected_hover:
            yanchor 1 alpha 0.93
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform dr_button_menu_transform:
        size (gui.dr_small_menu_size, gui.dr_small_menu_size)
        on selected_idle:
            yanchor 0 alpha 0.4
        on idle:
            yanchor 0 alpha 0.4
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform dr_close_button_transform:
        xanchor 25
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.9)
    transform nqtr_button_map_transform(rotation = 0):
        rotate rotation
        xysize (gui.nqtr_button_map_size, gui.nqtr_button_map_size)
        on selected_idle:
            yanchor 0 alpha 0.6
        on idle:
            yanchor 0 alpha 0.6
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform dr_button_next_transform(rotation = 0):
        rotate rotation
        on idle:
            alpha 0.6 matrixcolor BrightnessMatrix(0)
        on hover:
            alpha 1.0 matrixcolor BrightnessMatrix(0.2)
        on insensitive:
            alpha 0.6 matrixcolor BrightnessMatrix(-0.5)
