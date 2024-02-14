## Actions they do are meant to pass time

menu nap:
    "Nap for 3 hours":
        call wait(3) from _call_wait_2
        return
    "Sleep":
        jump sleep
        return
    "Return":
        return

menu sleep:
    "[tm.hour_of_new_day]:00":
        call new_day(is_check_event=True) from _call_new_day
        return
    "9:00":
        call new_day(time_of_new_day = 9, is_check_event=True) from _call_new_day_2
        return
    "Return":
        return

## Various actions

label take_key:
    mc "Are these the car keys?! Well... I should try to access the car!"
    $ set_flags("goout", True)
    $ del actions['take_key']
    $ quest_next_stage(id = "ann")
    return

menu talk_sleep:
    "zZz zZz ..."
    "Try waking up":
        # will lock the room
        a "[mc]!!!! What are you doing?!!"
        a "Get out of here! Now!"
        $ closed_rooms[cur_room.id] = df_routine["alice_sleep"]
        call after_spending_time from _call_after_spending_time_4
        return
    "Leave her alone":
        return

label alice_talk_menu:
    if(current_conversation_character == a):
        mc "Hi [a]"
        a "Hi, can you tell me something?"
    else:
        "Now is busy test later."

    call talk_menu from _call_talk_menu_1



