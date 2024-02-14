label talk_back_custom:
    
    $ num = renpy.random.randint(1, 7)
    if num == 1:
        mc "OK, I'm off. See you."
    elif num == 2:
        mc "It's getting late. See you."
    elif num == 3:
        mc "Sorry, but I have to go now. Bye."
    elif num == 4:
        mc "Good talk. We should do this more often."
    elif num == 5:
        mc "I just remembered something. Gotta go! Bye."
    elif num == 6:
        mc "I won't keep you any longer. Bye."
    elif num == 7:
        mc "I was supposed to tell you something else.... But I can't remember."
        mc "When it comes back to me I'll let you know, bye."

    if current_conversation_character == ayumi:
        $ del_conversation_choice(choice_character = ayumi, choice_text = _("Good morning! How did you sleep?"))
        $ del_conversation_choice(choice_character = ayumi, choice_text = _("Spend time."))
    elif current_conversation_character == yuno:
        $ del_conversation_choice(choice_character = yuno, choice_text = _("Good morning! How did you sleep?"))
        $ del_conversation_choice(choice_character = yuno, choice_text = _("Spend time."))
    elif current_conversation_character == akane:
        $ del_conversation_choice(choice_character = akane, choice_text = _("Good morning! How did you sleep?"))
        $ del_conversation_choice(choice_character = akane, choice_text = _("Spend time."))
    elif current_conversation_character == rei:
        $ del_conversation_choice(choice_character = rei, choice_text = _("Good morning! How did you sleep?"))
        $ del_conversation_choice(choice_character = rei, choice_text = _("Spend time."))

    $ del num
    return

# Quest "alice"

label stage_talkalice_aboutann:
    show bg alice terrace talk
    mc "Alice, I was thinking of visiting Ann. can you lend me your car?"
    a "Yes, of course. You can find the keys on the keyhole in the hall."
    mc "Thanks!"
    a "Don't ruin it..."
    $ actions["take_key"] = Act(name = _("KEY"),  picture_in_background = "/action-key.webp", label_name = "take_key", room_ids=['lounge'],
        xalign = 608/1920, yalign = 667/1080)

    $ quest_next_stage(id = "ann")
    $ del_conversation_choice(choice_character = a, choice_text = _("About the Ann"))
    return
