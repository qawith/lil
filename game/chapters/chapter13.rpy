label stage_chapter13:

    if (number_stages_completed_in_quest["chapter1"] == 3):

        $ quick_menu = False

        show screen mid_text("It took you 6 minutes to reach the school and change.") with fade
        pause 5.0
        show screen mid_text("You saw your classmates and ran towards them.") with fade
        pause 5.0
        hide screen mid_text with Fade(0.0, 0.0, 0.5)

        show chap1311 with Fade(0.5, 0.0, 0.0)

        stop music fadeout 2.0
        play music school

        $ quick_menu = True

        mc "Phew... Barely made it on time..."
        mc "How are you guys? Ready for the exam?"

        show chap1312 with dissolve

        rei "We were starting to think you wouldn't show up..."
        rei "And as for the exam, what do you think? We've been helping you prepare; how could we not be ready?"

        show chap1313 with dissolve

        akane "Especially in biology... Rei and I are the best at it."
        mc "Interesting, who among you knows it better..?"

        menu:

            "Well, I think it's you!":
                $ reiaff -= 1
                $ akaneaff += 1
                show chap1314_1 with dissolve
                show screen affection_hint_minus("-1 to relationship with Rei!") with moveintop
                pause 1.0
                hide screen affection_hint_minus with moveouttop
                show screen affection_hint_plus("+1 to relationship with Akane!") with moveintop
                pause 1.0
                hide screen affection_hint_plus with moveouttop
                rei "We'll have to check that.."

            "*remain silent*":
                show chap1314_2 with dissolve
                rei "We'll have to check that.."
        
        show chap1315 with dissolve

        akane "I don't want to waste time on this, honestly."

        show chap1316 with dissolve

        rei "Then let's see who performs better on the test!"

        menu:
            "Shall we go then?":
                show chap1317_1 with dissolve
                pause 2.0

            "I'm curious and want to watch":
                show chap1317_2 with dissolve
                pause 2.0
            
        $ quick_menu = False

        stop music fadeout 2.0

        show screen mid_text("Everyone went to the classroom together...") with fade
        scene black
        pause 5.0
        hide screen mid_text with Fade(0.0, 0.0, 0.5)

        play music bgm

        show chap1321 with Fade(0.5, 0.0, 0.0)

        $ quick_menu = True

        thinking "Darn, I don't remember anything."
        thinking "Guess I'll have to use Akane's notes after all."

        show chap1322 with dissolve

        yuno "Finally decided to show up? Tell me, what's the answer to the third question."
        mc "Wait, don't we have different questions? What is it?"
        yuno "About..."

        show chap1323 with fade

        akira "Fujivara-chan! You know the rules!"
        mc "Sorry, Kato-sensei... It's my fault... I was cheating."

        show chap1324 with dissolve

        akira "[mc_name]? Well, the rules are the same for everyone!"
        akira "Submit your work. I'll inform you about the retake."

        $ quick_menu = False

        show screen mid_text("Everyone is shocked in front of the school...") with fade
        scene black
        pause 5.0
        show screen mid_text("Ayumi looks extremely upset...") with fade
        pause 5.0
        show screen mid_text("Rei starts the conversation") with fade
        pause 5.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1331 with Fade(0.0, 0.0, 0.5)

        stop music fadeout 2.0
        play music school

        $ quick_menu = True

        rei "So, what happened, Ayumi-chan?"

        show chap1332 with dissolve

        ayumi "It's just awful..."
        ayumi "Because I came in late yesterday, I didn't have time to prepare."

        show chap1333 with dissolve

        ayumi "I only answered two questions... I have to retake the test."

        show chap1334 with dissolve

        akane "Well, I answered everything. Finally, I can relax a bit."

        show chap1335 with dissolve

        rei "Agreed. I've been waiting for these holidays for so long... Too bad it's only a week."

        menu:
            "Well, you know my situation anyway..":
                show chap1336_1 with dissolve
                yuno "Don't worry... I'm retaking it too!"

            "I'll retake it because of someone...":
                $ yunoaff -= 1
                show chap1336_2 with dissolve
                yuno "Oh, come on! Don't worry... I'm retaking it too!"
                show screen affection_hint_minus("-1 to relationship with Yuno!") with moveintop
                pause 1.0
                hide screen affection_hint_minus with moveouttop

        show chap1337 with dissolve

        yuno "Maybe I don't like people much, but I have honor. That's why I didn't cheat."

        show chap1338 with dissolve

        ayumi "So, what do you think about studying together? [mc_name], are you okay with that?"

        menu: 
            "Of course!":
                $ ayumiaff += 1
                show chap1339_1 with dissolve
                pause 1.0
                show screen affection_hint_plus("+1 to relationship with Ayumi!") with moveintop
                pause 1.0
                hide screen affection_hint_plus with moveouttop

            "I'm okay with it, but it would be nice if Ishito and Takahashi helped us!":
                $ choosevar = 2
                $ akaneaff += 1
                $ reiaff += 1
                show chap1339_2 with dissolve
                pause 1.0
                show screen affection_hint_plus("+1 to relationship with Akane and Rei!") with moveintop
                pause 1.0
                hide screen affection_hint_plus with moveouttop
            
        $ quick_menu = False
    
        show screen mid_text("You talked a bit more and said goodbye to everyone before going home...") with fade
        scene black
        pause 3.0
        hide screen mid_text with fade

        stop music fadeout 2.0
        play music bgm

        $ quest_next_stage(id = "chapter1")
        $ quick_menu = False
        call wait(3) from _call_wait_3

    return
