init -1:
    define gui.dr_multiplicateur = config.screen_height/1080
    default gui.dr_moblile_zoom = 1

    if renpy.variant("pc"):
        $ gui.dr_moblile_zoom = 1
    else:
        $ gui.dr_moblile_zoom = 1.5

    # text
    define gui.dr_little_text_size = convert_to_int(18 * gui.dr_multiplicateur)
    define gui.dr_normal_text_size = convert_to_int(24 * gui.dr_multiplicateur)
    define gui.dr_big_normal_text_size = convert_to_int(28 * gui.dr_multiplicateur)
    define gui.nqtr_hour_text_size = convert_to_int(60 * gui.dr_multiplicateur)
    # image
    define gui.nqtr_button_action_size = convert_to_int(120 * gui.dr_multiplicateur)
    define gui.dr_small_face_size = convert_to_int(60 * gui.dr_multiplicateur)
    define gui.nqtr_button_room_size = convert_to_int(204 * gui.dr_multiplicateur)
    define gui.nqtr_button_location_size = convert_to_int(90 * gui.dr_multiplicateur)
    define gui.dr_small_menu_size = convert_to_int(80 * gui.dr_multiplicateur * gui.dr_moblile_zoom)
    define gui.nqtr_button_map_size = convert_to_int(50 * gui.dr_multiplicateur)
    define gui.dr_close_button_size = convert_to_int(35 * gui.dr_multiplicateur)
    # drawer
    define gui.dr_drawer_ypos = convert_to_int(170 * gui.dr_multiplicateur)
    define gui.dr_drawer_xpos = convert_to_int(80 * gui.dr_multiplicateur)
    define gui.dr_drawer_ysize = convert_to_int(850 * gui.dr_multiplicateur)
    define gui.dr_drawer_xsize = convert_to_int(400 * gui.dr_multiplicateur)
    # nqtr menu_memo
    define gui.nqtr_menu_memo_image_ysize = convert_to_int(400 * gui.dr_multiplicateur)
    define gui.nqtr_menu_memo_image_xsize = convert_to_int(800 * gui.dr_multiplicateur)
    define gui.nqtr_menu_memo_frame_xsize = convert_to_int(1190 * gui.dr_multiplicateur)
    define gui.nqtr_menu_memo_frame_ysize = convert_to_int(400 * gui.dr_multiplicateur)
    # ds userinfo
    define gui.ds_userinfo_textdistance_xsize = convert_to_int(250 * gui.dr_multiplicateur)
    # Ren'Py Layered Image Masks
    define gui.sprite_size = 640
    define gui.sprite_elaborate_size = 700
    define gui.sprite_size_x = 1138
    define gui.sprite_size_padding_x = convert_to_int((gui.sprite_size_x - gui.sprite_elaborate_size) / 2)