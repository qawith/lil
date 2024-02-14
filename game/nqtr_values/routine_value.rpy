init python:
    from pythonpackages.nqtr.routine import Commitment
    from pythonpackages.nqtr.conversation import Conversation

define df_routine = {
    "ayumi_morning" : Commitment(
        conversations = [
            Conversation(
                name="ayumi_morning",
                label_name="conversation_start",
                characters=ayumi,
                conversation_background ="ayumi_morning_conversation"
            ),
        ],
        hour_start=7, hour_stop=9,
        location_id="dormitory", room_id="ayumi_room",
        background ="ayumi_morning_routine",
    ),
    "yuno_morning" : Commitment(
        conversations = [
            Conversation(
                name="yuno_morning",
                label_name="conversation_start",
                characters=yuno,
                conversation_background ="yuno_morning_conversation"
            ),
        ],
        hour_start=7, hour_stop=9,
        location_id="dormitory", room_id="kitchen",
        background ="yuno_morning_routine",
    ),
    "akane_morning" : Commitment(
        conversations = [
            Conversation(
                name="akane_morning",
                label_name="conversation_start",
                characters=akane,
                conversation_background ="akane_morning_conversation"
            ),
        ],
        hour_start=7, hour_stop=9,
        location_id="dormitory", room_id="akane_room",
        background ="akane_morning_routine",
    ),
    "rei_morning" : Commitment(
        conversations = [
            Conversation(
                name="rei_morning",
                label_name="conversation_start",
                characters=rei,
                conversation_background ="rei_morning_conversation"
            ),
        ],
        hour_start=7, hour_stop=9,
        location_id="dormitory", room_id="rei_room",
        background ="rei_morning_routine",
    ),
}

label conversation_start:

    if current_conversation_character == ayumi:
        $ add_conversation_choice(choice_character = ayumi, choice_text = _("Good morning! How did you sleep?"), label_name = "ayumi_morning")
        $ add_conversation_choice(choice_character = ayumi, choice_text = _("Spend time."), label_name = "ayumi_spend_time")
    elif current_conversation_character == yuno:
        $ add_conversation_choice(choice_character = yuno, choice_text = _("Good morning! How did you sleep?"), label_name = "yuno_morning")
        $ add_conversation_choice(choice_character = yuno, choice_text = _("Spend time."), label_name = "yuno_spend_time")
    elif current_conversation_character == akane:
        $ add_conversation_choice(choice_character = akane, choice_text = _("Good morning! How did you sleep?"), label_name = "akane_morning")
        $ add_conversation_choice(choice_character = akane, choice_text = _("Spend time."), label_name = "akane_spend_time")
    elif current_conversation_character == rei:
        $ add_conversation_choice(choice_character = rei, choice_text = _("Good morning! How did you sleep?"), label_name = "rei_morning")
        $ add_conversation_choice(choice_character = rei, choice_text = _("Spend time."), label_name = "rei_spend_time")

    call nqtr_talk from _call_nqtr_talk

    return

label ayumi_morning:

    ayumi "I slept well, thank you! And how about you? By the way, what are you doing here?"
    mc "That's great! Today, I woke up earlier and had a good sleep. I thought, why not drop by here!"
    ayumi "Oh, that's a lovely idea! Nice to see you here. Have a great day!"
    mc "You too! See you later!"

    $ del_conversation_choice(choice_character = ayumi, choice_text = _("Good morning! How did you sleep?"))
    $ del_conversation_choice(choice_character = ayumi, choice_text = _("Spend time."))

    return

label ayumi_spend_time:

    mc "Hey, Ayumi! Got a minute?"
    ayumi "Whats up?"
    mc "Nothing much, just thought we could spend some time together."
    ayumi "I would love to spend time with you!" 
    mc "Let's chat like old times."
    show screen mid_text("You spent time with Ayumi.") with fade
    pause 1.0
    hide screen mid_text with fade

    ayumi "Thank you for the time spent! It was really nice talking to you."
    mc "Thank you too! See you later!"

    $ ayumiaff += 1

    show screen affection_hint_plus("+1 to Ayumi's relationship!") with moveintop
    pause 1.0
    hide screen affection_hint_plus with moveouttop

    call hour_change(8) from _call_hour_change

    $ del_conversation_choice(choice_character = ayumi, choice_text = _("Good morning! How did you sleep?"))
    $ del_conversation_choice(choice_character = ayumi, choice_text = _("Spend time."))

    return

label yuno_morning:
    
        yuno "Why are you here?"
        mc "I just wanted to see you."
        yuno "Oh, that's nice of you. I slept well! And how about you?"
        mc "That's great! Today, I woke up earlier and had a good sleep."
        mc "I thought, why not drop by here!"
        yuno "That's nice for me. Can you make me cup of tea? he-he~"
        mc "Oh no-no-no! See you later!"
    
        $ del_conversation_choice(choice_character = yuno, choice_text = _("Good morning! How did you sleep?"))
        $ del_conversation_choice(choice_character = yuno, choice_text = _("Spend time."))
    
        return

label yuno_spend_time:

    mc "Hey, Yuno! Got a minute?"
    yuno "Oh, if you want to spend time with me, make a cup of tea for me! Also you can make one for yourself too!" 
    mc "Okay, I will make one for you and one for me."

    show screen mid_text("You spent time with Yuno over a cup of tea.") with fade
    pause 1.0
    hide screen mid_text with fade

    yuno "Thank you for tea! I love it, also i like to spend time with you."
    mc "Ohh~ Thank you too! See you later!"

    $ yunoaff += 1

    show screen affection_hint_plus("+1 to Yuno's relationship!") with moveintop
    pause 1.0
    hide screen affection_hint_plus with moveouttop

    call hour_change(8) from _call_hour_change_1

    $ del_conversation_choice(choice_character = yuno, choice_text = _("Good morning! How did you sleep?"))
    $ del_conversation_choice(choice_character = yuno, choice_text = _("Spend time."))

    return

label akane_morning:

    akane "Like a log, obviously. What are you doing here so early?"
    mc "Just thought I'd drop by and say hi."
    mc "Plus, I wanted to see if you're alive before our class."
    akane "You're too chipper for this hour. And why would you care if I'm alive or not?"
    mc "Just being a considerate classmate, you know? So, how was your beauty sleep?"
    akane "It was fine. I'm going to go back to sleep now. See you later."
    mc "Okay.. See you later."

    $ del_conversation_choice(choice_character = akane, choice_text = _("Good morning! How did you sleep?"))
    $ del_conversation_choice(choice_character = akane, choice_text = _("Spend time."))

    return

label akane_spend_time:

    mc "Hey, Akane. Got a minute?"
    akane "What do you want?"
    mc "Nothing much, just thought we could spend some time together. Maybe grab a coffee or something."
    akane "Huh, interesting. You're not planning some elaborate prank, are you?"
    mc "Scouts honor, no pranks. Just a chat between friends."
    akane "Fine, whatever."
    
    show screen mid_text("You spent time with Akane.") with fade
    pause 1.0
    hide screen mid_text with fade

    mc "Thanks for the time, Akane. I'll see you later."

    $ akaneaff += 1

    show screen affection_hint_plus("+1 to Akane's relationship!") with moveintop
    pause 1.0
    hide screen affection_hint_plus with moveouttop

    call hour_change(8) from _call_hour_change_2

    $ del_conversation_choice(choice_character = akane, choice_text = _("Good morning! How did you sleep?"))
    $ del_conversation_choice(choice_character = akane, choice_text = _("Spend time."))

label rei_morning:

    rei "Why do you care how I slept?"
    mc "No particular reason. Just making conversation, you know?"
    rei "It was... sufficient. Why do you ask?"
    mc "Just curious. You always seem so composed.. I was wondering if that extends to your sleep too."
    rei "Sleep is a necessity. Composure, on the other hand, is a choice."
    mc "Okay.. So, how was it?"
    rei "Fine, I suppose. I'm going to go back to sleep now. See you later."
    mc "Okay.. See you later."

    $ del_conversation_choice(choice_character = rei, choice_text = _("Good morning! How did you sleep?"))
    $ del_conversation_choice(choice_character = rei, choice_text = _("Spend time."))

    return

label rei_spend_time:

    mc "Hey, Rei. Mind if I join you for a moment?"
    rei "What's on your mind?"
    mc "Just wanted to spend some time together, maybe get to know each other a bit more."
    rei "Why the sudden interest? I don't exactly broadcast my life story."
    mc "Mystery has its charm. I thought we could grab a coffee or something."
    rei "Fine. But keep your questions surface-level. I'm not one for deep conversations."
    mc "Sure, I understand."

    show screen mid_text("You spent time with Rei.") with fade
    pause 1.0
    hide screen mid_text with fade

    mc "Thanks for the time, Rei. I'll see you later."

    $ reiaff += 1

    show screen affection_hint_plus("+1 to Rei's relationship!") with moveintop
    pause 1.0
    hide screen affection_hint_plus with moveouttop

    call hour_change(8) from _call_hour_change_3

    $ del_conversation_choice(choice_character = rei, choice_text = _("Good morning! How did you sleep?"))
    $ del_conversation_choice(choice_character = rei, choice_text = _("Spend time."))

    return