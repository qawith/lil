init:
    style main_menu_navigation_button is gui_button
    style main_menu_navigation_button_text is gui_button_text

    style main_menu_navigation_button:
        size_group "navigation"
        background Frame("gui/main_menu/button.png", 45, 45)
        xsize 450 ysize 60

    style main_menu_navigation_button_text:
        size 33
        color "#9933ff"
        hover_color "#c184ff"
        insensitive_color "#88888800"
        outlines [ (1, "#3d1466", 1, 1), (1, "#3d1466", 1, 1) ]
        hover_outlines [ (1, "#5b1e99", 1, 1), (1, "#5b1e99", 1, 1) ]
        xalign 0.99
        yalign 0.6

    screen main_menu_navigation():
        vbox:

            style_prefix "main_menu_navigation"
            align (.99, .85)
            spacing 10

            if main_menu:

                textbutton _("Start") action Start()

            else:

                textbutton _("History") action ShowMenu("history")

                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Options") action ShowMenu("preferences")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Main Menu") action MainMenu()

            textbutton _("About") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):

                textbutton _("Quit") action Quit(confirm=not main_menu)