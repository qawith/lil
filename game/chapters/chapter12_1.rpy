label stage_chapter12_1:

    if (number_stages_completed_in_quest["chapter1"] == 1):

        scene black with fade

        show chap1111 with Fade(0.0, 0.0, 0.5)

        "You wake up from the notification.."

        show chap1112 with fade

        ayumi "“Hello, sorry, but I won't be able to help you with the test preparation."
        ayumi "I have some important matters. However, Rei will help you! I'll write the address of our dormitory below!”"

        $ quest_next_stage(id = "chapter1")
        $ dormitory_open = True