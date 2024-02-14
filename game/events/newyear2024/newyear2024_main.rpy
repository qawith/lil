label stage_newyear2024_main:

    if not quest_is_completed("newyear2024"):

        $ quick_menu = False

        show screen mid_text("You all met up and went to the house you prepared with Ayumi yesterday.") with fade
        scene black
        pause 2.5
        show screen mid_text("Now you've arrived.") with fade
        pause 1.0
        show screen mid_text("Everyone gathers for New Year's Day. Gifts are exchanged, and the atmosphere is festive.") with fade
        pause 3.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show newyear2024_21 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        ayumi "I hope you all like your gifts! I put a lot of thought into them."
        mc "This is great, Ayumi. Thanks for organizing everything."

        show newyear2024_22 with fade
        pause 2.0

        $ quick_menu = False

        show screen mid_text("As Ayumi hands out gifts, Main Character receives identical presents from Yuno and Akane.") with fade
        scene black
        pause 3.0
        show screen mid_text("They're both small, rectangular boxes.") with fade
        pause 1.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show newyear2024_23 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        yuno "Open it later, when you alone. It's a special gift."

        show newyear2024_24 with dissolve

        akane "Yeah, you'll enjoy it. Trust us."

        $ quick_menu = False

        show screen mid_text("The group shares laughter and stories creating a warm and friendly atmosphere.") with fade
        scene black
        pause 2.5
        show screen mid_text("The night has arrived, and the house is filled with laughter and the aroma of delicious food.") with fade
        pause 2.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show newyear2024_25 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        ayumi "Attention, everyone! Before we dive into this feast, I want to say a few words."
        ayumi "This year has been filled with ups and downs, but tonight, we're here to celebrate the good times and look forward to new beginnings."
        ayumi "Cheers to friendship, love, and a fantastic year ahead!"
        mc "Well said, Ayumi. Let's make this night one to remember."

        $ quick_menu = False
        
        show screen mid_text("As the night progresses, the group enjoys the delicious food, engaging in lively conversations.") with fade
        scene black
        pause 2.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show newyear2024_26 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        akane "This place looks amazing, Ayumi. You really outdid yourself."

        show newyear2024_27 with dissolve

        ayumi "Thanks, Akane! But it wouldn't be half as fun without all of you here."

        show newyear2024_28 with dissolve

        yuno "I must admit, this is more enjoyable than I expected. Good job, Ayumi."

        show newyear2024_29 with dissolve

        ayumi "Wow, thanks, Yuno. I'm glad you're having a good time."

        show newyear2024_210 with dissolve

        rei "Indeed, a well-organized event. I appreciate the effort, Ayumi."

        show newyear2024_211 with dissolve

        ayumi "Well, I had an excellent planning partner. [mc_name] here deserves some credit too."

        show newyear2024_212 with dissolve

        ayumi "By the way, did everyone enjoy the Secret Santa exchange? Any favorite gifts?"

        show newyear2024_213 with dissolve

        mc "I got this fantastic book from Rei. Really thoughtful!"

        show newyear2024_214 with dissolve

        rei "I'm glad you liked it. Books have a way of opening new worlds."

        $ quick_menu = False

        show screen mid_text("The clock ticks closer to midnight, and Ayumi suggests a traditional countdown.") with fade
        scene black
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show newyear2024_215 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        ayumi "Okay, everyone! Let's count down the seconds together. Ten..."
        ayumi "Nine..."
        ayumi "Eight..."

        $ quick_menu = False

        show screen mid_text("As the countdown reaches zero, the room erupts in cheers, hugs, and well-wishes for the coming year.") with fade
        scene black
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show newyear2024_216 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        mc "Happy New Year, everyone!"

        "Happy New Year!"

        $ quick_menu = False

        show screen mid_text("After celebrating, everyone went to their beds. The main character, a guy, slept alone separate from the others.") with fade
        scene black
        pause 3.0
        show screen mid_text("He received a note from Yuno and Akane, on which it was written...") with fade
        pause 2.0
        show screen mid_text("“We'll give you your gift at night when everyone is asleep.”") with fade
        pause 2.0
        show screen mid_text("The main character was very excited and could not wait for the night to come.") with fade
        pause 3.0
        show screen mid_text("And now the time for the gift has come.") with fade
        pause 2.0
        show screen mid_text("Yuno and Akane enter the room half-naked.") with fade
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show newyear2024_217 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        yuno "Happy New Year, [mc_name]."
        yuno "Our gift will be one of the most unforgettable nights of your life…"
        akane "You can be sure of that…"

        $ quick_menu = False

        show screen mid_text("Everything happened so quickly that you didn't even realize...") with fade
        scene black
        pause 3.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        stop music fadeout 2.0
        show newyear2024_yuno_blowjob with Fade(0.0, 0.0, 0.5)
        play sound yuno_blowjob
        queue sound yuno_blowjob
        queue sound yuno_blowjob
        queue sound yuno_blowjob
        queue sound yuno_blowjob
        queue sound yuno_blowjob
        pause 15.0
        menu: 
            "Continue...":
                stop sound fadeout 0.5
                show newyear2024_akane_cowgirl with fade
                play sound akane_main
                queue sound akane_main
                queue sound akane_main
                queue sound akane_main
                queue sound akane_main
                queue sound akane_main
                pause 15.0
                menu: 
                    "Continue...":
                        stop sound fadeout 0.5
                        show newyear2024_yuno_cowgirl with fade
                        play sound yuno_main
                        queue sound yuno_main
                        queue sound yuno_main
                        queue sound yuno_main
                        queue sound yuno_main
                        pause 15.0
                        menu:
                            "Cum inside.":
                                stop sound fadeout 0.5
                                show newyear2024_yuno_climax with fade
                                play sound yuno_climax
                                queue sound yuno_climax
                                queue sound yuno_climax
                                queue sound yuno_climax
                                queue sound yuno_climax
                                pause 10.0
                                menu: 
                                    "Continue...":
                                        stop sound fadeout 0.5
                                        play music bgm
                                        jump stage_newyear2024_pool

    return

