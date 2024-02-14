init -1:
    # Characters
    define mc = Character('[mc_name]')
    define ayumi = Character("Ayumi", color="#6a67aa", icon = "images/icon/ayumi.webp")
    define akane = Character("Akane", color = "#ffffffff", icon = "images/icon/akane.webp")
    define rei = Character("Rei", color = "#7f3f98", icon = "images/icon/rei.webp")
    define yuno = Character("Yuno", color = "#7f3f98", icon = "images/icon/yuno.webp")
    define akira = Character("Akira", color = "#000000ff", icon = "images/icon/akira.webp")
    define thinking = Character("Thinking...")
    # Affection points
    default maxaff = 100
    default ayumiaff = 3
    default akaneaff = 0
    default reiaff = 0
    default yunoaff = 0
    default akiraaff = 0
    default ayumiafflvl = 0
    default akaneafflvl = 0
    default reiafflvl = 0
    default yunoafflvl = 0
    default akiraafflvl = 0

label splashscreen:
    $ show_endmenu_multiply = True
    call screen splash_screen with dissolve

label pleasurescreen:
    call screen pleasure_screen with fade

label start:
    

    init python:
        config.keymap['rollforward'].remove('mousedown_5')
        config.keymap['rollback'].remove('mousedown_4')
        config.keymap['rollforward'].remove('any_KP_PAGEDOWN')
        config.keymap['rollforward'].remove('any_K_PAGEDOWN')
        config.keymap['rollback'].remove('K_AC_BACK')
        config.keymap['rollback'].remove('any_KP_PAGEUP')
        config.keymap['rollback'].remove('any_K_PAGEUP')

    $ quick_menu = False

    python:
        mc_name = renpy.input("Enter your name:\n", length = 32)
        mc_name = mc_name.strip()

        if not mc_name:
            mc_name = "Miłosz"

    show screen mid_text(f"Exchange student from Poland {mc_name}, came to Japan on the recommendation of his old friend, Kurosawa Ayumi.") with fade
    screen black
    pause 5.0
    show screen mid_text("The girl studies at the same university, so she was the one who helped him with the exchange organization.") with fade
    pause 5.0
    show screen mid_text(f"Now {mc_name} wakes up in his new home in Japan and is ready for the first day at the new university.") with fade
    pause 5.0 
    show screen mid_text("He doesn't know anyone yet, except for his old internet friend.") with fade
    pause 5.0
    show screen mid_text("But she promised to introduce him to some of her classmates.") with fade
    pause 5.0
    show screen mid_text("His heart is full of hope and expectations, but he is a little nervous that everything will not go as planned.") with fade
    pause 5.0
    show screen mid_text(f"{mc_name} awaits many interesting adventures and acquaintances in his new life in Japan!") with fade
    pause 5.0
    hide screen mid_text with Fade(0.5, 0.0, 0.0)

    show chap1111 with Fade(0.0, 0.0, 0.5)

    "You wake up from the notification.."

    show chap1112 with fade

    ayumi "“I'm already in the front yard of the school! Waiting for you.”"

    thinking "Need to get ready and run to them."

    $ set_flags("goout", True)

    call change_room(room_id = "my_room") from _call_change_room_2
    $ prev_room = rooms[0]

    if(not quest_start(id = "chapter1")):
        $ log_error("The quest chapter1 has not started", renpy.get_filename_line())

    play music bgm

    call enable_notifyEx from _call_enable_notifyEx
    call after_spending_time from _call_after_spending_time_5
    call screen room_navigation

    return