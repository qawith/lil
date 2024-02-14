label stage_chapter11:

    if (number_stages_completed_in_quest["chapter1"] == 0):

        stop music fadeout 2.0
        play music school

        show chap1121 with Fade(0.0, 0.0, 0.5)
        pause 3.2

        show chap1122 with fade

        $ quick_menu = True

        ayumi "Hello, [mc_name], it's me, Ayumi!"
        mc "Nice to see you! Strange to meet again after so many years of chatting online.."

        show chap1123 with dissolve

        ayumi "Hehe~ It is indeed strange, but I'm very happy to see you! How are you here? Ready for studying?"
        mc "Your country is just amazing, but there's a lot I don't understand.. It would be good to learn something about the culture and customs.."

        show chap1124 with dissolve

        ayumi "Great!~ I'll help you get used to Japanese culture, and as promised, I'll introduce you to our classmates!"

        show chap1125 with dissolve

        ayumi "Oh, look, my.. I mean, our classmates, Takahashi and Ishito, are standing nearby! Let's go meet them!!"

        $ quick_menu = False
        show screen mid_text("You approach your new classmates...") with fade
        scene black
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1126 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        ayumi "Takahashi-san, Ishito-san!! Meet our new classmate, [mc_name]!"

        menu:

            "Hello, how is it going?":

                $ choosevar = 1

            "Hello, I'm from Poland, hoping to make friends with you all..":

                $ choosevar = 2

        if choosevar == 1:

            show chap1127 with dissolve
            akane "I think exchange students shouldn't stay here for too long."

        elif choosevar == 2:

            $ akaneaff -= 1
            show screen affection_hint_minus("-1 to Akane's relationship!") with moveintop
            pause 1.0
            hide screen affection_hint_minus with moveouttop
            show chap1127 with dissolve
            akane "I don't care where you came from.. I think exchange students shouldn't stay here for too long."

        show chap1128 with dissolve

        ayumi "Akane has always been indifferent to everything, but don't mind her."
        ayumi "We're glad you're with us, and we'll help you feel comfortable in our country."

        show chap1129 with dissolve

        rei "Yes, Ayumi is right. If you have any questions or need help, just ask us."
        thinking "*Wow, Takahashi seems to have some mysterious aura..*"
        mc "Thank you all for the warm welcome. I'm really looking forward to getting to know you."

        show chap11210 with dissolve

        akane "I'm also glad to meet you. Now that we're acquainted, can we move on? I don't want to be late for class."

        $ quick_menu = False
        show screen mid_text("*Akane and Rei head to class*") with fade
        scene black
        pause 2.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)
        
        show chap11211 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        ayumi "Hmmm~ It's strange that Yuno-chan is nowhere to be seen. I asked her to come out here."
        ayumi "By the way, how was your first meeting?"
        mc "I think Ishito doesn't seem very happy about our meeting.."

        show chap11212 with dissolve

        ayumi "Don't mind her; she always acts like that. I also don't get along with her very well."

        show chap11213 with dissolve

        ayumi "Oh~ Look, here comes another classmate!"

        $ quick_menu = False
        show screen mid_text("Yuno approaches you...") with fade
        scene black
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap11214 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        ayumi "Yuno-chan!!"

        menu:

            "Hello, Yuno!":

                $ choosevar = 1

            "Hello, how should I call you?":

                $ choosevar = 2
            
        if choosevar == 1:

            show chap11215 with dissolve
            yuno "For you - Fujivara-san!"
        
        elif choosevar == 2:

            $ yunoaff += 1
            show screen affection_hint_plus("+1 to Yuno's relationship!") with moveintop
            pause 1.0
            hide screen affection_hint_plus with moveouttop
            show chap11215 with dissolve
            yuno "Pf, you don't have to call me formally."


        show chap11216 with dissolve

        ayumi "Oh, stop it! Better tell me, where have you been?"

        show chap11217 with dissolve
        
        yuno "I was summoned to the director's office, so I was late."

        show chap11218 with dissolve

        ayumi "To the director? What happened again?"

        show chap11219 with dissolve

        yuno "I was coming here, and on the stairs, some fool decided to show off. Am I to blame that he couldn't stand on his feet?"

        show chap11220 with dissolve

        ayumi "Did you push him down the stairs?!"

        show chap11221 with dissolve

        yuno "You could call it that, but it doesn't matter. Is this why you called me here, for an introduction?"

        show chap11222 with dissolve

        ayumi "Well, is there anything else needed? "

        show chap11223 with dissolve

        ayumi "This is my old friend, [mc_name], I'm sure you two will get along!"
        mc "I also hope for that!"

        show chap11224 with dissolve

        yuno "Enough talking.. And as for you, Ayumi-chan, it's time you remembered my attitude toward this!"

        show chap11225 with dissolve

        ayumi "~Yuno-chan! Don't be so mean all the time!"

        show chap11226 with dissolve

        ayumi "Alright, time to run to class!"

        $ quick_menu = False
        stop music fadeout 2.0
        play music bgm
        show screen mid_text("*You enter the classroom*") with fade
        scene black
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1131 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        akira "Good morning! I hope you're prepared for class!"

        show chap1132 with dissolve

        ayumi "Kato-sensei! We have a new exchange student - my good friend - [mc_name]!! He.."

        show chap1133 with dissolve

        akira "Stop, Kurosawa-chan, let the newcomer tell us something about himself!"

        show chap1134 with dissolve

        akira "My name is Kato-sensei, I teach biology!"
        akira "Right now, we're studying the regulation of organism functions, and today's topic is immune disorders."
        akira "But first, I want to know something about our newcomer."

        menu:

            "My name is [mc_name], I'm from Poland. Thanks for the warm welcome!":

                $ choosevar = 1

            "Well, Ayumi has already said everything..":

                $ choosevar = 2

        if choosevar == 1:
            $ akiraaff += 1
            show screen affection_hint_plus("+1 to Akira's relationship!") with moveintop
            pause 1.0
            hide screen affection_hint_plus with moveouttop

        elif choosevar == 2:
            $ akiraaff -= 1
            show screen affection_hint_minus("-1 to Akira's relationship!") with moveintop
            pause 1.0
            hide screen affection_hint_minus with moveouttop

        show chap1135 with dissolve

        ayumi "And I introduced him to our classmates!!"

        show chap1136 with dissolve

        akira "Alright, let's continue."
        akira "I'll remind you that this is the last topic, which means we'll have a test next time!"

        scene black with fade

        $ quick_menu = False
        show screen mid_text("*You sit in your place*") with fade
        pause 2.0
        show screen mid_text("*The lesson begins*") with fade
        pause 2.0
        show screen mid_text("...") with fade
        pause 2.0
        show screen mid_text("*The lesson is over*") with fade
        pause 2.0
        show screen mid_text("*You discuss the lesson with new friends on the way out of school*") with fade
        pause 3.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)
        stop music fadeout 2.0

        play music school
        scene chap1141 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        mc "Hey, is there a test for the next time? I've just started!"

        show chap1142 with dissolve

        ayumi "Don't worry, [mc_name]."
        ayumi "I'll help you prepare. If you want, we can meet and go through the material together."

        show chap1143 with dissolve

        rei "It's probably a good idea to let you know that you can rely on us."

        show chap1144 with dissolve

        akane "Or you can do it yourself. There's nothing complicated about biology."

        show chap1145 with dissolve

        yuno "Why are you wasting your time on this greenhorn? Let him figure it out on his own."
        ayumi "Stop it, Yuno-chan, that's not the solution! We'll help you prepare!"

        show chap1146 with dissolve

        ayumi "I'll write to you later, [mc_name]!"

        stop music fadeout 2.0
        scene black with fade

        play music bgm
        call wait(8) from _call_wait
        $ quest_next_stage(id = "chapter1")
        $ quick_menu = False

        return