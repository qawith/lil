init:
    style game_menu_navigation_button is gui_button
    style game_menu_navigation_button_text is gui_button_text

    style game_menu_navigation_button:
        size_group "navigation"
        background Frame("gui/game_menu/button.png", 45, 45)
        xsize 350 ysize 60

    style game_menu_navigation_button_text:
        size 30
        xpos 10
        yalign 0.5
        color "#9933ff"
        hover_color "#c184ff"

    screen game_menu_navigation():
        vbox:

            style_prefix "game_menu_navigation"
            yalign 0.35
            xalign 0.02
            spacing 10

            if not main_menu:

                textbutton _("Main Menu") action MainMenu()

            if main_menu:

                textbutton _("Start") action Start()

            else:

                textbutton _("History") action ShowMenu("history")

                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Options") action ShowMenu("preferences")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            textbutton _("About") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):

                textbutton _("Quit") action Quit(confirm=not main_menu)


        textbutton _("Return") action Return():
            style_prefix "game_menu_navigation"
            yalign 0.95
            xalign 0.02
            
            
        
            