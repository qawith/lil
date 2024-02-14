screen splash_screen:

    fixed:
        add Movie(play = "gui/splash/splash_background.webm", loop = True, size = (1920, 1080))
        add "gui/splash/text_splash_background.png" align(.5, .5) xsize 1600 ysize 902

    fixed:
        text "Disclaimer" xalign 0.5 yalign 0.16 size 40 outlines [ (4, "#000", 0, 0), (4, "#000", 0, 0) ]
        vbox area(250, 290, 1500, 752):
            text "   This interactive novel contains scenes of a sexual nature and is intended for individuals who are 18 years old or older, meaning they have the legal right to access adult content.\n\nPlayers who have not reached the age of majority are not recommended to play this novel. We insist that adults use this game responsibly and do not allow minors access to it.\n\nBy playing this interactive novel, you confirm that you are willing to take responsibility for your actions and decisions related to the content of this game." line_spacing 12

    fixed:
        imagebutton:
            xpos 450 ypos 850
            
            idle "gui/splash/splash_button.png"
            hover "gui/splash/splash_button_hovered.png"

            focus_mask True
            action [Hide("splashscreen"), With("fade"), Jump("pleasurescreen")]

        vbox area(490, 875, 404, 104):
            text "I am\n18 years old." line_spacing 12 text_align 0.5

    fixed:
        imagebutton:
            xpos 1050 ypos 850

            idle "gui/splash/splash_button.png"
            hover "gui/splash/splash_button_hovered.png"

            focus_mask True
            action [Quit(), With("fade"), Hide("splashscreen")]

        vbox area(1090, 875, 404, 104):
            text "I am not\n18 years old." line_spacing 12 text_align 0.5
        
        
