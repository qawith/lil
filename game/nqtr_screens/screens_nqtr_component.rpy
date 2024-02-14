screen wait_button(small = False):
    imagebutton:
        idle '/gui/interface/wait.webp'
        focus_mask True
        action [
            With(Dissolve(0.25)),
            Call("after_return_from_room_navigation", label_name_to_call = "wait"),
        ]
        if renpy.variant("pc"):
            tooltip _("Wait")
        at nqtr_button_action_transform

screen character_icon_screen(icon):
    if icon:
        imagebutton:
            idle icon
            focus_mask True
            action []
            at dr_small_face_transform

screen time_text(tm, show_wait_button = False):
    hbox:
        align (0.5, 0.01)
        vbox:
            align (0.5, 0.01)
            spacing 20
            text "[tm.hour]:00":
                xalign (0.5)
                size gui.nqtr_hour_text_size
                drop_shadow [(2, 2)]
            text tm.weekday_name:
                xalign (0.5)
                size gui.dr_normal_text_size
                drop_shadow [(2, 2)]
                line_leading -16

        if (show_wait_button):

            use wait_button(small = True)

screen action_button(act):
    imagebutton:
        idle act.button_icon
        hover act.button_icon_selected
        focus_mask True
        action [
            With(Dissolve(0.25)),
            Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
        ]
        if renpy.variant("pc"):
            tooltip act.name
        at nqtr_button_action_transform

screen action_picture_in_background(act):
    imagebutton:
        align (act.xalign, act.yalign)
        idle act.picture_in_background
        hover act.picture_in_background_selected
        focus_mask True
        action [
            With(Dissolve(0.25)),
            Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
        ]
        if renpy.variant("pc"):
            tooltip act.name
        at nqtr_button_action_picture_transform

screen action_talk_button(conversation, background):
    if not conversation.is_hidden(flags = flags, check_if_has_icon = False):
        frame:
            xysize (gui.nqtr_button_action_size, gui.nqtr_button_action_size)
            background None

            imagebutton:
                align (0.5, 0.0)
                if conversation.is_button:
                    idle conversation.button_icon
                    hover conversation.button_icon_selected
                else:
                    idle gui.default_talk_button_icon
                focus_mask True
                action [
                    SetVariable('current_conversation_character', conversation.character),
                    SetVariable('conversation_image', background),
                    With(Dissolve(0.25)),
                    Call("after_return_from_room_navigation", label_name_to_call = conversation.label_name),
                ]
                at nqtr_button_action_transform
                if renpy.variant("pc"):
                    tooltip _("Talk")

            use character_icon_screen(conversation.character_icon)

screen location_button(location):
    if (location.map_id == cur_map_id and not location.is_hidden(flags = flags)):
        vbox:
            align (location.yalign, location.xalign)
            imagebutton:
                if location.is_picture_in_background:
                    idle location.picture_in_background
                    selected_idle location.picture_in_background_selected
                    selected_hover location.picture_in_background_selected
                selected location == cur_location
                sensitive not location.is_hidden(flags)
                focus_mask True
                action [
                    SetVariable('cur_location', location),
                    With(Dissolve(0.25)),
                    Call("after_return_from_room_navigation", label_name_to_call = "change_location"),
                ]
                at nqtr_button_location_transform

            # Locations name
            text location.name:
                size 10
                drop_shadow [(2, 2)]
                outlines [(1, "#000000", 0, 0, 0, 0)]
                xalign 0.5
                text_align 0.5
                line_leading 0
                line_spacing -2

screen map_button(map_id, map, align_value, rotation):
    if not map.is_hidden(flags = flags, check_if_has_icon = False):
        zorder 2
        hbox:
            align align_value
            imagebutton:
                idle "gui triangular_button"
                focus_mask True
                sensitive not map.is_disabled(flags)
                action [
                    SetVariable('cur_map_id', map_id), 
                    With(Dissolve(0.25)),
                    Call("after_return_from_room_navigation", label_name_to_call = "set_image_map"),
                ]
                if renpy.variant("pc"):
                    tooltip map.name
                at nqtr_button_map_transform(rotation)

screen map(maps, cur_map_id):
    $ map_id_north = maps[cur_map_id].map_id_north
    $ map_id_south = maps[cur_map_id].map_id_south
    $ map_id_east = maps[cur_map_id].map_id_east
    $ map_id_west = maps[cur_map_id].map_id_west

    # North map
    if not isNullOrEmpty(map_id_north):
        use map_button(map_id = map_id_north, map = maps[map_id_north], align_value = (0.5, 0.1), rotation = 270)
    # South map
    if not isNullOrEmpty(map_id_south):
        use map_button(map_id = map_id_south, map = maps[map_id_south], align_value = (0.5, 0.99), rotation = 90)
    # West map
    if not isNullOrEmpty(map_id_west):
        use map_button(map_id = map_id_west, map = maps[map_id_west], align_value = (0.001, 0.5), rotation = 180)
    # East map
    if not isNullOrEmpty(map_id_east):
        use map_button(map_id = map_id_east, map = maps[map_id_east], align_value = (0.999, 0.5), rotation = 0)

screen room_button(room, cur_room, i, find_ch = False):
    # If the Locations where I am is the same as the Locations where the room is located
    if (room.location_id == cur_location.id and room.is_button != None and not room.is_hidden(flags)):
        vbox:
            frame:
                xysize (gui.nqtr_button_action_size, gui.nqtr_button_action_size + gui.dr_little_text_size)
                background None

                # Room icon
                imagebutton:
                    align (0, - 0.15)
                    if room.is_button:
                        idle room.button_icon
                    selected_idle room.button_icon_selected
                    selected_hover room.button_icon_selected
                    selected (True if cur_room and cur_room.id == room.id else False)
                    sensitive not room.is_disabled(flags)
                    focus_mask True
                    action [
                        SetVariable('prev_room', cur_room),
                        SetVariable('cur_room', room),
                        With(Dissolve(0.25)),
                        Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
                    ]
                    at nqtr_button_room_transform

                # Character icon
                if find_ch:
                    hbox:
                        align (0.5, 0.6)
                        for comm in commitments_in_cur_location.values():
                            # If it is the selected room
                            if room.id == comm.room_id:
                                use character_icon_screen(comm.character_icon)

                # Room name
                text room.name:
                    ypos 120
                    align (0.6, 0.5)
                    size 14
                    drop_shadow [(2, 2)]
                    text_align 0.5
                    line_spacing 2

        key str(i) action [
            SetVariable('prev_room', cur_room),
            SetVariable('cur_room', room),
            With(Dissolve(0.25)),
            Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
        ]

screen affection_bar(aff, afflvl):

    bar:
        xsize 1200
        ysize 150
        xpos 431
        ypos 820
        if afflvl == 0:
            value AnimatedValue(value = aff, range = 10)
        elif afflvl == 1:
            value AnimatedValue(value = aff - 10, range = 15)
        elif afflvl == 2:
            value AnimatedValue(value = aff - 25, range = 20)
        elif afflvl == 3:
            value AnimatedValue(value = aff - 45, range = 25)
        elif afflvl == 4:
            value AnimatedValue(value = aff - 70, range = 30)
        left_bar Frame("gui/affection/bar/left.webp", 10, 10)
        right_bar Frame("gui/affection/bar/right.webp", 10, 10)

    fixed:
        text "Affection\nlevel:" text_align 0.5 xpos 255 ypos 675 size 30 outlines [ (4, "#000", 0, 0), (4, "#000", 0, 0) ]
        image "gui/affection/bar/heart.webp" xpos 260 ypos 755
        text "[afflvl]" text_align 0.5 xpos 330 ypos 820 size 90 outlines [ (6, "#000", 0, 0), (6, "#000", 0, 0) ]

screen affection_main():

    frame:
        xsize 1600 ysize 900
        align(.5, .75)

        hbox spacing 20:
            text "Ayumi" outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ] text_align 0.5 xpos 170 ypos 335
            text "Akane" outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ] text_align 0.5 xpos 305 ypos 335
            text "Yuno" outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ] text_align 0.5 xpos 445 ypos 335
            text "Rei" outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ] text_align 0.5 xpos 615 ypos 335
            text "Akira" outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ] text_align 0.5 xpos 775 ypos 335

        hbox spacing 30:
            xpos 100 ypos 30

            imagebutton xsize 250 ysize 300:

                idle "gui/affection/icons/small_ayumi.webp" 
                hover "gui/affection/icons/small_ayumi_hovered.webp"

                action [With(dissolve), Hide("affection_main"), ToggleScreen("affection_ayumi")]

            imagebutton:

                idle "gui/affection/icons/small_akane.webp" xsize 250 ysize 300
                hover "gui/affection/icons/small_akane_hovered.webp"
                
                focus_mask True
                action [With(dissolve), Hide("affection_main"), ToggleScreen("affection_akane")]

            imagebutton:

                idle "gui/affection/icons/small_yuno.webp" xsize 250 ysize 300
                hover "gui/affection/icons/small_yuno_hovered.webp"
                
                focus_mask True
                action [With(dissolve), Hide("affection_main"), ToggleScreen("affection_yuno")]

            imagebutton:

                idle "gui/affection/icons/small_rei.webp" xsize 250 ysize 300
                hover "gui/affection/icons/small_rei_hovered.webp"
                
                focus_mask True
                action [With(dissolve), Hide("affection_main"), ToggleScreen("affection_rei")]

            imagebutton:

                idle "gui/affection/icons/small_akira.webp" xsize 250 ysize 300
                hover "gui/affection/icons/small_akira_hovered.webp"
                
                focus_mask True
                action [With(dissolve), Hide("affection_main"), ToggleScreen("affection_akira")]

screen affection_ayumi():
        
    frame:
        xsize 1600 ysize 900
        align(.5, .75)

        fixed:
            add "gui/affection/icons/big_ayumi.webp" xpos 30 ypos 30
            text "{b}Kurosawa Ayumi{/b}" xalign 0.7 ypos 30 size 40 outlines [ (4, "#000", 0, 0), (4, "#000", 0, 0) ]
            text "Kurosawa Ayumi - a naive, friendly, and\nsincere girl with great optimism. She's always\non a positive wave, cheerful, and energetic,\nmaking her a spark among friends.\nAyumi is a regular visitor to the manga club,\nwhere she dragged the main character." xpos 465 ypos 90 line_spacing 10 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]
            text "Ayumi is curently located:" xalign 0.73 ypos 485 size 30 outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ]
            if tm.hour >= 7 and tm.hour < 9:
                text "Dormitory" xalign 0.68 ypos 530 size 25 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]


    use affection_bar(ayumiaff, ayumiafflvl)
    use back_button("affection_ayumi", "affection_main", 1730, 160)

screen affection_akane():

    frame:
        xsize 1600 ysize 900
        align(.5, .75)

        fixed:
            add "gui/affection/icons/big_akane.webp" xpos 30 ypos 30
            text "{b}Ishito Akane{/b}" xalign 0.7 ypos 30 size 40 outlines [ (4, "#000", 0, 0), (4, "#000", 0, 0) ]
            text "Ishito Akane - a girl with a stable and\ncomfortable life but an indifferent attitude\ntowards many things. She is a member of the\n\"Going home\" club. Akane doesn't enjoy\ncommunicating with others much because it\nexhausts her, but she's always ready to help\nwhen needed. Her indifferent attitude towards\nlife is often a mask hiding a vulnerable and\nsensitive soul." xpos 465 ypos 90 line_spacing 10 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]
            text "Akane is curently located:" xalign 0.73 ypos 485 size 30 outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ]
            if tm.hour >= 7 and tm.hour < 9:
                text "Dormitory" xalign 0.68 ypos 530 size 25 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]

    
    use affection_bar(akaneaff, akaneafflvl)
    use back_button("affection_akane", "affection_main", 1730, 160)

screen affection_yuno():

    frame:
        xsize 1600 ysize 900
        align(.5, .75)

        fixed:
            add "gui/affection/icons/big_yuno.webp" xpos 30 ypos 30
            text "{b}Fujivara Yuno{/b}" xalign 0.7 ypos 30 size 40 outlines [ (4, "#000", 0, 0), (4, "#000", 0, 0) ]
            text "Fujivara Yuno is a yandere who participates in\ntrack and field. She strives to be the leader\nin everything, refusing to acknowledge her\nwrongdoing. Anyone in close proximity to her\nfalls under herinfluence, and she always seeks\nto control the situation. Yuno typically keeps\nher relationships with others to a minimum,\nnot accepting anyone into her inner circle\nexcept for her sole friend, Ayumi Kurosawa,\nwho nis entirely opposite to her." xpos 465 ypos 90 line_spacing 10 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]
            text "Yuno is curently located:" xalign 0.73 ypos 485 size 30 outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ]
            if tm.hour >= 7 and tm.hour < 9:
                text "Dormitory" xalign 0.68 ypos 530 size 25 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]


    use affection_bar(yunoaff, yunoafflvl)
    use back_button("affection_yuno", "affection_main", 1730, 160)

screen affection_rei():

    frame:
        xsize 1600 ysize 900
        align(.5, .75)

        fixed:
            add "gui/affection/icons/big_rei.webp" xpos 30 ypos 30
            text "{b}Takahashi Rei{/b}" xalign 0.7 ypos 30 size 40 outlines [ (4, "#000", 0, 0), (4, "#000", 0, 0) ]
            text "Takahashi Rei is a mysterious girl, little is\nknown about her, creating a certain aura and\nmystique that captures the attention of the\nprotagonist. She always stays in the shadows,\navoiding unnecessary attention, but her\npresence has a distinct effect on others. Rei\nis a truly enigmatic figure, and her choice to\nbe friends with Akane Ishito may indicate her\nreserved nature and a need for a more\ncomfortable environment." xpos 465 ypos 90 line_spacing 10 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]
            text "Rei is curently located:" xalign 0.73 ypos 485 size 30 outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ]
            if tm.hour >= 7 and tm.hour < 9:
                text "Rei room at dormitory" xalign 0.68 ypos 530 size 25 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]
  
    use affection_bar(reiaff, reiafflvl)
    use back_button("affection_rei", "affection_main", 1730, 160)

screen affection_akira():

    frame:
        xsize 1600 ysize 900
        align(.5, .75)

        fixed:
            add "gui/affection/icons/big_akira.webp" xpos 30 ypos 30
            text "{b}Kato Akira{/b}" xalign 0.7 ypos 30 size 40 outlines [ (4, "#000", 0, 0), (4, "#000", 0, 0) ]
            text "Kato Akira is a charismatic teacher who always\nlooks elegant and stylish. Possessing sharp\nintellect and extensive knowledge, she has\nbecome one of the favorite educators among\nstudents. In addition to her work, Akira finds\ntime to attend the tea appreciation club,\nwhere she indulges in the flavors and aromas\nof various teas, discussing culture and art\nwith other club members." xpos 465 ypos 90 line_spacing 10 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]
            text "Akira is curently located:" xalign 0.73 ypos 485 size 30 outlines [ (3, "#000", 0, 0), (3, "#000", 0, 0) ]
            if tm.hour >= 7 and tm.hour < 9:
                text "School" xalign 0.61 ypos 530 size 25 outlines [ (2, "#000", 0, 0), (2, "#000", 0, 0) ]

    use affection_bar(akiraaff, akiraafflvl)
    use back_button("affection_akira", "affection_main", 1730, 160)


