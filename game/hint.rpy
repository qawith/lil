screen affection_hint_plus(hint_text):

    fixed:
        xsize 400 ysize 150
        xpos 760 ypos 0

        add "gui/hint/affection_hint_plus.webp" 

        text "{color=#000}[hint_text]{/color}": 
            xsize 400 ysize 150 
            align(.5, 0.8) 
            text_align 0.5

screen affection_hint_minus(hint_text):

    fixed:
        xsize 400 ysize 150
        xpos 760 ypos 0

        add "gui/hint/affection_hint_minus.webp" 

        text "{color=#000}[hint_text]{/color}": 
            xsize 400 ysize 150 
            align(.5, 0.8) 
            text_align 0.5

python:

    def hint(text, variant):
        if variant == "minus":
            renpy.show_screen("affection_hint_minus", hint_text=text)
        elif variant == "plus":
            renpy.show_screen("affection_hint_plus", hint_text=text)

        