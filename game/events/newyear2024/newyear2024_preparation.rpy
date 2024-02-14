label stage_newyear2024_invitation:

    if (number_stages_completed_in_quest["newyear2024"] == 0):

        show newyear2024_11 with fade

        $ quick_menu = True

        ayumi "Hey, [mc_name]! I've been thinking, and I've got this fantastic idea for New Year's Eve!"
        mc "Oh, really? What's the plan?"

        show newyear2024_12 with dissolve

        ayumi "Well, my parents are away, and I thought, why not throw a New Year's party right here at our place?"
        mc "That sounds like a great idea! But, um, isn't organizing a party a lot of work?"

        show newyear2024_13 with dissolve

        ayumi "It is, but that's where you come in! I was hoping you'd help me set everything up. You're so good at this kind of stuff."
        mc "Me? Well, I'm flattered. But why not ask others too?"

        show newyear2024_14 with dissolve

        ayumi "Because you're special, [mc_name]. I know you'll make this celebration unforgettable."
        mc "Alright, Ayumi. I'm in. Let's make it the best New Year's ever!"

        show newyear2024_15 with dissolve

        ayumi "Yes! You won't regret it, I promise. We'll create memories to last a lifetime."

        jump stage_newyear2024_preparation

    return

label stage_newyear2024_preparation:

    $ quick_menu = False

    show screen mid_text("You share a moment of excitement and begin discussing plans for the party") with fade
    scene black
    pause 3.0
    show screen mid_text("After this you went to Ayumi's place.") with fade
    pause 3.0
    show screen mid_text(f"Ayumi and {mc_name} are at the house, getting it ready for the New Year's celebration.") with fade
    pause 3.0
    show screen mid_text("The air is filled with excitement and the promise of a memorable night.") with fade
    pause 3.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_16 with Fade(0.0, 0.0, 0.5)

    $ quick_menu = True

    ayumi "This is going to be amazing, [mc_name]! Thanks for helping me with all of this."
    mc "Of course, Ayumi. I'm glad to be a part of it. Where do we start?"

    $ quick_menu = False

    show screen mid_text("You enter the living room") with fade
    scene black
    pause 3.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_17 with Fade(0.0, 0.0, 0.5)

    $ quick_menu = True

    ayumi "Let's start with the tree and decorations."

    show newyear2024_18 with dissolve

    ayumi "You know, my parents agreed to let us use this place. They're away for the holidays."
    mc "Really? That's generous of them. What made them say yes?"

    show newyear2024_19 with dissolve

    ayumi "I might have mentioned how much this celebration means to me and that I've got an amazing friend helping out."
    
    $ quick_menu = False

    show screen mid_text("You two starts decorating") with fade
    pause 3.0
    scene black
    show screen mid_text("As they finish up the decorations, Ayumi takes a moment to express her gratitude.") with fade
    pause 3.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_110 with Fade(0.0, 0.0, 0.5)

    $ quick_menu = True

    ayumi "Thanks for being here, [mc_name]. It means a lot to me."
    mc "I wouldn't miss it for the world. Now, let's make this place shine!"

    $ quick_menu = False

    show screen mid_text("The two friends share a moment of accomplishment as they step back to admire their handiwork.") with fade
    scene black
    pause 3.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_111 with Fade(0.0, 0.0, 0.5)

    $ quick_menu = True

    mc "Maybe we can relax and watch a movie together?"

    show newyear2024_112 with fade

    ayumi "Oh, that's a great idea."
    mc "Sure, you get to pick the movie!"

    show newyear2024_113 with dissolve

    ayumi "i know one. This movie better be good! I heard it has great reviews."
    mc "Yeah, it should be interesting. Let's hope it's not too intense."

    $ quick_menu = False

    show screen mid_text("Ayumi chose a movie, and you started watching it.") with fade
    scene black
    pause 3.0
    show screen mid_text("The movie has entered an adult scene.") with fade
    pause 3.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_114 with Fade(0.0, 0.0, 0.5)

    thinking "What movie is this... Did Ayumi choose it?"

    show newyear2024_115 with fade

    thinking "Oh... What is going on... I probably need to hug her too."
    thinking "Or... do something better."

    menu:
        "Put a hand on her waist.":
            $ quick_menu = False
            show screen mid_text("You put your hand on her waist.") with fade
            scene black
            pause 3.0
            show screen mid_text("She looks at you and smiles.") with fade
            pause 3.0
            hide screen mid_text with Fade(0.5, 0.0, 0.0)
        "Put a hand on her breasts.":
            show screen mid_text("Don't rush.\nTry one more time with another choice.") with fade
            scene black
            pause 3.0
            hide screen mid_text with Fade(0.5, 0.0, 0.0)
            jump stage_newyear2024_preparation

    show newyear2024_116 with Fade(0.0, 0.0, 0.5)

    thinking "Wow, she's so sweet..."

    menu:
        "Start kissing her.":
            show screen mid_text("She didn't resist.") with fade
            scene black
            pause 3.0
            hide screen mid_text with Fade(0.5, 0.0, 0.0)
        "Put a hand on her butt.":
            show screen mid_text("Don't rush.\nTry one more time with another choice.")
            scene black
            pause 3.0
            hide screen mid_text with Fade(0.5, 0.0, 0.0)
            jump stage_newyear2024_2

    show newyear2024_117 with Fade(0.0, 0.0, 0.5)

    thinking "It's clear from her face that she wants more."

    show screen mid_text("While you were kissing, things escalated much further...") with fade
    scene black
    pause 3.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)
    show newyear2024_ayumi_handjob with Fade(0.0, 0.0, 0.5)
    pause 15.0
    menu:
        "Continue":
            stop music fadeout 2.0
            show newyear2024_ayumi_cowgirl with fade
            play sound rei_main
            queue sound rei_main
            queue sound rei_main
            queue sound rei_main
            queue sound rei_main
            pause 15.0
            menu:
                "Continue...":
                    stop sound fadeout 0.5
                    show newyear2024_118 with fade
                    "AYUMI-I, are you here?"
                    ayumi "Oh god, that's my parents..."
                    mc "W-WWHAT?"
                    show screen mid_text("As her parents arrived to see what you had done there...") with fade
                    scene black
                    pause 3.0
                    show screen mid_text("We had to gather ourselves without finishing the deed completely...") with fade
                    pause 3.0
                    show screen mid_text("After that, nothing happened, but I hope that someday we will continue...") with fade
                    pause 3.0
                    hide screen mid_text with fade
                    call change_location("house") from _call_change_location_3
                    call new_day() from _call_new_day_3
                    play music bgm

    $ quest_next_stage(id = "newyear2024")
    $ quick_menu = False

    return                  


    
