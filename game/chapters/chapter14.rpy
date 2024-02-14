label stage_chapter14:

    if (number_stages_completed_in_quest["chapter1"] == 4):

        $ quick_menu = False

        show screen mid_text("You enter the Ayumi room.")
        scene black
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1411 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        ayumi "[mc_name]!!\nFinally, you're here. Hurry up, we've already started with Yuno!"
        yuno "It's you again, newcomer?"

        show chap1412 with dissolve

        ayumi "Well, why newcomer? [mc_name] has a name! And it is..."

        show chap1413 with dissolve

        ayumi "Well, you understood what I meant."

        show chap1414 with dissolve

        yuno "Ha-ha-ha... I get it, I get it."
        mc "Whose room is this?"

        menu:
            "Yours, Ayumi?":
                $ ayumiaff += 1
                show screen affection_hint_plus("+1 to relationship with Ayumi!") with moveintop
                pause 1.0
                hide screen affection_hint_plus with moveouttop
                show chap1415_1 with dissolve
                ayumi "Hehe~ You guessed."
            "Well, i think your room would look different, Ayumi.":
                show chap1415_2 with dissolve
                ayumi "But no! This is mine!!"

        mc "What does yours look like, Fujivara-sama?"

        show chap1416 with dissolve

        ayumi "Fujivara-sama?!"
        ayumi "Did you tell him that, Yuno-chan?"

        show chap1417 with dissolve

        yuno "No, it was his choice."

        menu:
            "Stay silent.":
                $ yunoaff = yunoaff
            "But you introduced yourself to me that way...":
                $ yunoaff -= 1
                show screen affection_hint_minus("-1 to relationship with Yuno!") with moveintop
                pause 1.0
                hide screen affection_hint_minus with moveouttop
        
        show chap1418 with dissolve

        ayumi "Well, let's not dwell on it. Maybe it will improve your relationship!"
        ayumi "Alright, are we ready?"

        show chap1419 with dissolve

        yuno "Honestly, I don't see the point in preparing. I didn't fail due to lack of preparation."

        menu:
            "Sorry, Fujivara-sama.":
                $ yunoaff += 1
                show chap14110 with dissolve
                show screen affection_hint_plus("+1 to relationship with Yuno!") with moveintop
                pause 1.0
                hide screen affection_hint_plus with moveouttop
                ayumi "But it's not your fault, [mc_name]!"
            "Stay silent.":
                $ yunoaff = yunoaff
                show chap14110 with dissolve
        
        ayumi "Okay! I don't want to hear anything, let's get ready!"

        $ quick_menu = False

        show screen mid_text("You and Ayumi with Yuno help are preparing for the exam.") with fade
        scene black
        pause 3.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap14111 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        yuno "Bla-bla-bla... Alright, that's enough."

        show chap14112 with dissolve

        ayumi "You're right, especially since we have a whole day!"

        show chap14113 with dissolve

        yuno "Are you planning to prepare tomorrow? I don't know about you, but I'm out."
        mc "How about a joint walk then?"

        show chap14114 with dissolve

        ayumi "That's a great idea!!"

        show chap14115 with dissolve

        ayumi "But what if I fail again..."
        mc "And where are Rei and Akane? Maybe they'll join us too."

        show chap14116 with dissolve

        yuno "See, Ayumi-chan, you don't need to worry, the newcomer quickly found a replacement for you."
        yuno "It's strange that he even suggested it, considering how well he can spend time with Ishito."

        menu:
            "Stay silent.":
                $ ayumiaff = ayumiaff
                show chap14117_1 with dissolve
            "I don't understand what you're talking about. I just want to have a good time":
                $ ayumiaff += 1
                show screen affection_hint_plus("+1 to relationship with Ayumi!") with moveintop
                pause 1.0
                hide screen affection_hint_plus with moveouttop
                show chap14117_2 with dissolve

        show chap14118 with dissolve

        ayumi "No, Yuno-chan! I'll go too!!"

        show chap14119 with dissolve

        ayumi "Besides, it wouldn't be nice to refuse you, [mc_name]!"

        show chap14120 with dissolve

        yuno "And you're not against if Takahashi and Ishito join us?"

        show chap14121 with dissolve

        ayumi "Me?"
        ayumi "I'm all for it."

        $ quick_menu = False

        show screen mid_text("You go to the kitchen, where you find Akane and Rei.") with fade
        scene black
        pause 3.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1421 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        yuno "And here they are... Alright, newcomer, go ahead."

        show chap1422 with dissolve

        mc "Ishito-chan, Takahashi-chan! I have a proposal..."
        mc "How about going for a walk tomorrow?"

        rei "Hm, sounds like a good idea... What do you think, Akane?"

        show chap1423 with dissolve

        akane "No, I have things to do."

        menu:
            "Then... can we reschedule for another day?":
                $ ayumiaff -= 1
                $ akaneaff += 1
                show screen affection_hint_minus("-1 to relationship with Ayumi!") with moveintop
                pause 1.0
                hide screen affection_hint_minus with moveouttop
                show screen affection_hint_plus("+1 to relationship with Akane!") with moveintop
                pause 1.0
                hide screen affection_hint_plus with moveouttop
                show chap1424_1 with dissolve
            "Stay silent.":
                $ ayumiaff = ayumiaff
                $ akaneaff = akaneaff
                show chap1424_2 with dissolve

        akane "And besides, I'm not a fan of this.\nIt tires me."

        show chap1425 with dissolve

        yuno "There you go, it's a hint for a romantic meeting, as I said, Ayumi."

        show chap1426 with dissolve

        akane "A hint for what? Don't make me laugh, Fujivara-san."

        show chap1427 with dissolve

        ayumi "Alright, enough!"

        show chap1428 with dissolve

        ayumi "So, [mc_name], where are we going?"

        menu:
            "Maybe you should choose?":
                $ ayumiaff += 1
                show screen affection_hint_plus("+1 to relationship with Ayumi!") with moveintop
                pause 1.0
                hide screen affection_hint_plus with moveouttop
            "Well, I don't know any suitable places here":
                $ ayumiaff = ayumiaff

        show chap1429 with dissolve

        ayumi "Hm... How about the park?"
        ayumi "Or maybe to the playground?"

        show chap14210 with dissolve

        yuno "Let's go to Dead or Alive."

        show chap14211 with dissolve

        ayumi "Well, as always..."
        ayumi "But fine, what about you, Takahashi-chan?"

        show chap14212 with dissolve

        rei "Not a bad place.\nI agree."

        $ quick_menu = False

        show screen mid_text("You say goodbye to everyone and go to home.") with fade
        scene black 
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        $ quest_next_stage(id = "chapter1")
        $ quick_menu = False
        call change_location("house") from _call_change_location
        call wait(6) from _call_wait_4
        if(not quest_start(id = "newyear2024")):
            $ log_error("The quest newyear2024 has not started", renpy.get_filename_line())

    return