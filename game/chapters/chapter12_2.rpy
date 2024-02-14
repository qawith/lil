label stage_chapter12_2:

    if (number_stages_completed_in_quest["chapter1"] == 2):

        $ quick_menu = False
        show screen mid_text("*after some time you were already in the dormitory*") with fade
        scene black
        pause 5.0
        show screen mid_text("*you knocked on the door*") with fade
        pause 5.0
        show screen mid_text("*you heard a familiar voice*") with fade
        pause 5.0
        hide screen mid_text with fade
        rei "You can come in, the door is open."
        pause 5.0
        show screen mid_text("*you enter and see Rei*") with fade
        pause 5.0
        hide screen mid_text with Fade(0.0, 0.0, 0.5)

        show chap1221 with Fade(0.5, 0.0, 0.0)
        pause 1.0

        rei "Welcome! You can sit down."
        
        show screen mid_text("*you sit at the table*") with fade
        scene black
        pause 5.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1222 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        mc "Wow, your dorm room looks much better than my apartment."

        show chap1223 with dissolve

        rei "Thank you. Did you come to prepare for the test?"
        mc "First, I want to thank you for agreeing to help me."

        menu:

            "Secondly, I would like to learn more about you":
                $ choosevar = 1

            "*stay silent*":
                $ choosevar = 2

        if choosevar == 1:
            show chap1224_1 with dissolve
            rei "I don't think my personality is important for our test preparation."

        elif choosevar == 2:
            show chap1224_2 with dissolve
            rei "And secondly?"

        menu:

            "Well, I would like to know more about you..":
                $ choosevar = 1

            "Oh, never mind.":
                $ choosevar = 2

        if choosevar == 1:
            $ reiaff -= 1
            show screen affection_hint_minus("-1 to relationship with Rei!") with moveintop
            pause 1.0
            hide screen affection_hint_minus with moveouttop
            show chap1225_1 with dissolve
            rei "If you insist, we can start with the fact that I am Takahashi Rei, and we are in the same group."
            rei "And then we can move on to biology."

        elif choosevar == 2:
            show chap1225_2 with dissolve
            rei "Then let's move on to biology!"

        mc "Great! Shall we start checking my knowledge?"

        show chap1226 with dissolve

        rei "Alright, I'll be happy to help you prepare for the test."

        $ quick_menu = False
        show screen mid_text("*a few hours later*") with fade
        pause 5.0
        scene black
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1227 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        rei "Well.. it seems like everything went well, just review those two topics again!"
        
        menu:

            "Where should I look for the necessary information?":
                $ choosevar = 1

            "Thank you very much for your help, but I haven't received textbooks yet.":
                $ choosevar = 2

        if choosevar == 1:

            show chap1228 with dissolve
            rei "I think Akane-chan promised to give you her notes, go to her."

        elif choosevar == 2:

            $ reiaff += 1
            show screen affection_hint_plus("+1 to relationship with Rei!") with moveintop
            pause 1.0
            hide screen affection_hint_plus with moveouttop
            show chap1228 with dissolve
            rei "I think Akane-chan promised to give you her notes, go to her."

        show chap1229 with dissolve

        rei "Her room is across the hall."

        $ quick_menu = False
        show screen mid_text("*you thanked and said goodbye to Rei*") with fade
        scene black
        pause 5.0
        show screen mid_text("*you knocked on the door that according to Rei leads to Akane's room*") with fade
        pause 5.0
        show screen mid_text("*Akane's voice*") with fade
        hide screen mid_text with Fade(0.5, 0.0, 0.0)
        akane "The door is open, come in!"

        show chap1231 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        akane "Hello! Come in."

        show chap1232 with fade

        menu:

            "Excuse me, am I not bothering?":
                $ choosevar = 1

            "Akane-chan! Can I please have your biology notes?":
                $ choosevar = 2

        if choosevar == 1:
            show chap1233_1 with dissolve
            akane "Are you looking for notes? I'll look for them now."

        elif choosevar == 2:
            $ akaneaff += 1
            show screen affection_hint_plus("+1 to relationship with Akane!") with moveintop
            pause 1.0
            hide screen affection_hint_plus with moveouttop
            show chap1233_2 with dissolve
            akane "Oh? Yes, I'll look for them now... and by the way, we usually don't address each other by names."

        $ quick_menu = False
        show screen mid_text("*Akane started looking for notes*") with fade
        scene black
        pause 5.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1234 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        menu:

            "Wow, you have every room here like choirs.. I envy you!":
                $ akaneaff = akaneaff
            
            "Ah, can I join your dorm?":
                $ akaneaff = akaneaff
        
        show chap1236 with fade

        akane "Ha-ha, if only.. We have an elite dorm, you won't find anything like it anywhere else!"
        akane "Where do you live?"
        mc "Oh, I rent a small apartment near the university, but it's much more pleasant here!"
        mc "If you want, you can come to my place, and I'll show you around."

        akane "I.. Wow.."

        show chap1237 with dissolve

        akane "Ha-ha, no.. I already understood what you meant"
        akane "And now I have to prepare for the test."
        pause 2.0
        "*Yuno's voice*"
        yuno "Who's there? Come here.."
        mc "I'll probably go say hello. Thanks for the notes!"

        $ quick_menu = False
        show screen mid_text("*you took the notes, thanked Akane, and went to the kitchen*") with fade
        pause 5.0
        scene black
        show screen mid_text("*there you saw Yuno*") with fade
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1241 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        yuno "It's you, I knew it.. Make me tea, I really want some."

        show chap1242 with dissolve

        yuno "Well, you can drink it yourself!"
        mc "But I'm here for the first time.."

        show chap1243 with dissolve

        yuno "Well, that's it. You don't need sugar."

        show chap1244 with dissolve

        menu:

            "Well, okay, as you say.":
                $ choosevar = 1

            "I actually don't like tea at all, but okay..":
                $ choosevar = 2

        
        if choosevar == 1:

            $ yunoaff += 1
            show screen affection_hint_plus("+1 to relationship with Yuno!") with moveintop
            pause 1.0
            hide screen affection_hint_plus with moveouttop

        elif choosevar == 2:
            $ yunoaff -= 1
            show chap1245_2 with dissolve
            show screen affection_hint_minus("-1 to relationship with Yuno!") with moveintop
            pause 1.0
            hide screen affection_hint_minus with moveouttop

        $ quick_menu = False
        show screen mid_text("*you made tea and sat down at the table*") with fade
        scene black
        pause 5.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1246 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        mc "You never answered me.. How can I address you?"

        show chap1247 with dissolve

        yuno "Address me? Hm.."

        show chap1248 with dissolve

        yuno "Address me.. Fujivara-sama!"

        $ quick_menu = False
        show screen mid_text("*Akane comes out of her room*") with fade
        pause 5.0
        scene black
        show screen mid_text("*and joins the conversation*") with fade
        pause 5.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1249 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        mc "And how about the tea, Fujivara-sama?"

        show chap12410 with dissolve

        akane "Fujivara-sama? Ha-ha-ha, clever, Yuno-san.."

        show chap12411 with dissolve

        yuno "Tch. Ishito-chan, do you want tea too? [mc_name], make some for her too."

        show chap12412 with dissolve

        akane "No, I don't need it."
        akane "And you've settled in nicely."

        $ quick_menu = False
        show screen mid_text("*Ayumi enters the dorm*") with fade
        pause 5.0
        scene black
        show screen mid_text("*looking surprised at the events in the kitchen*") with fade
        pause 5.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap12413 with Fade(0.0, 0.0, 0.5)

        ayumi "Wow, you're all here!! "
        yuno "She's back. Is everything okay?"

        show chap12414 with dissolve

        ayumi "Yes!! And what are you all doing? How was your day? How's the preparation, [mc_name]?"

        show chap12415 with fade

        yuno "I don't know about others, but Ishito-chan seems to have had a good time with the newbie."

        show chap12416 with dissolve

        akane "Well, let's start with the fact that it's not like that."
        akane "And finish with the fact that eavesdropping is rude."
        yuno "Well, whether it's good or not, decide for yourself, and I'll go!"

        $ quick_menu = False
        show screen mid_text("*Yuno went to her room*") with fade
        pause 5.0
        scene black
        show screen mid_text("clearly not in the best mood...") with fade
        pause 5.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap12417 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        ayumi "Well, did you prepare?"
        mc "Yes!"
        
        menu:
            "Especially grateful to Rei for the time spent!":
                $ choosevar = 1
            "Especially grateful to Akane.. I mean, Ishito-chan, for her notes!":
                $ choosevar = 2
                

        if choosevar == 1:
            $ reiaff += 1
            show screen affection_hint_plus("+1 to relationship with Rei!") with moveintop
            pause 1.0
            hide screen affection_hint_plus with moveouttop

        elif choosevar == 2:
            $ akaneaff += 1
            show chap12418 with dissolve
            show screen affection_hint_plus("+1 to relationship with Akane!") with moveintop
            pause 1.0
            hide screen affection_hint_plus with moveouttop

        show chap12419 with dissolve

        akane "And if you use skillful hands and my notes, you can avoid preparing more.."

        show chap12420 with dissolve
        
        ayumi "That's extreme.. Well, [mc_name], it's late, and we have a test tomorrow, see you then!"

        $ quick_menu = False
        show screen mid_text("you think that it's already late and time to say goodbye") with fade
        pause 5.0
        scene black
        show screen mid_text("*After saying goodbye and thanking everyone once again, you went home.*") with fade
        pause 5.0
        hide screen mid_text with fade

        $ chapter12_2_complete = True
        $ quest_next_stage(id = "chapter1")
        call wait(6) from _call_wait_1
        $ quick_menu = False

return
