label stage_newyear2024_pool:

    $ quick_menu = False

    show screen mid_text("Waking up in the morning, you can't believe what happened in the past few days.") with fade
    scene black
    pause 5.0
    show screen mid_text("Gathering around the Christmas tree, you all headed to the swimming pool.") with fade
    pause 5.0
    show screen mid_text("The group is enjoying a day by the pool, laughter echoing as they splash around.")
    pause 5.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_31 with Fade(0.0, 0.0, 0.5)

    $ quick_menu = True

    ayumi "Come on, [mc_name]! Join us in the pool! It's so refreshing!"
    mc "Of course!"

    $ quick_menu = False

    show screen mid_text("You jumped into the pool.") with fade
    scene black
    pause 5.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_32 with Fade(0.0, 0.0, 0.5)

    $ quick_menu = True

    akane "This is fantastic! Ayumi, you really outdid yourself."

    show newyear2024_33 with dissolve

    ayumi "It's all for our unforgettable New Year's celebration!"

    $ quick_menu = False

    show screen mid_text("As the group continues to enjoy the pool, Rei approaches the Main Character") with fade
    scene black
    pause 5.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_34 with Fade(0.0, 0.0, 0.5)

    $ quick_menu = True

    rei "Interesting night, wouldn't you say? The choices we make sometimes lead to unexpected turns."
    mc "Yeah, things got a bit unpredictable. What's on your mind?"
    rei "Life is full of surprises. Embrace them, or they might just pass you by."

    $ quick_menu = False

    show screen mid_text("The group spends time at the pool, and eventually, you decide to take a break.") with fade
    scene black
    pause 5.0
    show screen mid_text("You heads to the bathroom and surprised to find Rei there.") with fade
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_35 with Fade(0.0, 0.0, 0.5)

    $ quick_menu = True

    rei "I heard about what you guys did last night.... I have a proposal for you."

    show newyear2024_36 with dissolve

    rei "If you want me to keep quiet about what you did last night with Yuno and Akane..."
    rei "You must repeat it with me here and now…"

    $ quick_menu = False

    show screen mid_text("You shocked by Rei's proposal.") with fade
    scene black
    pause 5.0
    show screen mid_text("But... of course, you agreed.\nYou didn't have a choice.")
    pause 5.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    stop music fadeout 0.5
    
    play sound rei_blowjob
    queue sound rei_blowjob
    queue sound rei_blowjob
    queue sound rei_blowjob
    queue sound rei_blowjob
    queue sound rei_blowjob
    show newyear2024_rei_blowjob with Fade(0.0, 0.0, 0.5)
    pause 15.0
    menu:
        "Continue...":
            stop sound fadeout 0.5
            show newyear2024_rei_doggy with fade
            play sound rei_main
            queue sound rei_main
            queue sound rei_main
            queue sound rei_main
            queue sound rei_main
            queue sound rei_main
            pause 15.0
            menu: 
                "Cum inside...":
                    stop sound fadeout 0.5
                    show newyear2024_rei_climax with fade
                    play sound rei_climax
                    queue sound rei_climax
                    queue sound rei_climax
                    queue sound rei_climax
                    queue sound rei_climax
                    pause 10.0
                    menu:
                        "Continue...":
                            stop sound fadeout 0.5
                            play music bgm
                            show screen mid_text("After that, you all went to the main room, where the whole group was already waiting for you.") with fade
                            scene black
                            pause 5.0
                            hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show newyear2024_37 with Fade(0.0, 0.0, 0.5)

    ayumi "Where were you?"
    mc "I went to freshen up in the shower."
    mc "When I came out, I met Rei there."

    show newyear2024_38 with dissolve

    ayumi "Oh, I see. We're already getting ready to leave."

    show screen mid_text("You chatted for a bit more and then went to get ready to leave.") with fade
    scene black 
    pause 5.0
    show screen mid_text("You thanked everyone for the wonderful New Year celebration and headed home.") with fade
    pause 5.0
    hide screen mid_text with fade

    $ quest_next_stage(id = "newyear2024")
    $ quick_menu = False

    call change_location("house") from _call_change_location_2
    call new_day() from _call_new_day_1

    return