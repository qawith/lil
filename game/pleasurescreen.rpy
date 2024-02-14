screen pleasure_screen:

    fixed:
        add Movie(play = "gui/splash/splash_background.webm", loop = True, size = (1920, 1080))
        add "gui/splash/text_splash_background.png" align(.5, .5) xsize 1600 ysize 902

    fixed:
        text "Thank you!" xalign 0.5 yalign 0.15 size 40 outlines [ (4, "#000", 0, 0), (4, "#000", 0, 0) ]
        vbox area(250, 225, 1500, 752):
            text "   Dear player,\n\nI want to express my sincere gratitude to you for deciding to join our visual novel. Your support and interest in the game are crucial to me, and I am incredibly pleased that you have dedicated a part of your time and attention to my creation.\n\nIf you have the desire to support me financially, I would be very grateful. Your support will help me develop and improve the game, creating even more engaging and impressive content for you and other players.\n\nYou can support me on Patreon. This will enable me to continue creating the best stories and games for you. Regardless of your decision, I am very thankful for your active participation and interest in my creativity.\n\nBest regards,\nqawith" line_spacing 12

    fixed:
        imagebutton:
            xpos 1250 ypos 850
            

            idle "gui/splash/patreon.png"
            hover "gui/splash/patreon_hovered.png"

            focus_mask True
            action [OpenURL("https://www.patreon.com/LoveinLocker"), Hide("splashscreen"), With("fade"), MainMenu(False, False)]

        vbox area(1365, 890, 404, 104):
            text "PATREON" line_spacing 12 yalign 0 xalign 0.17

    fixed:
        imagebutton:
            xpos 1732 ypos 112

            idle "gui/exit_cross.png"
            at dr_close_button_transform

            focus_mask True
            action [Hide("splashscreen"), With("fade"), MainMenu(False, False)]