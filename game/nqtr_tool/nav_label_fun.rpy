init python:
    from pythonpackages.nqtr.navigation import get_room_by_id
    from pythonpackages.nqtr.navigation import get_location_by_id

default sp_bg_change_room = None
define bg_loc = "location/loc-[tm.timeslot_number].webp"
define block_goout_dialogue = _("Now is not the time to go outside")

label change_room(room_id = None):
    if room_id:
        python:
            new_room = get_room_by_id(room_id = room_id, rooms = rooms)
            prev_room = cur_room
            cur_room = new_room
            del new_room
    if cur_location.id != cur_room.location_id:
        python:
            new_location = get_location_by_id(location_id = cur_room.location_id, locations = locations)
            prev_location = cur_location
            cur_location = new_location
            del new_location
    call after_spending_time(is_check_event=True) from _call_after_spending_time
    return

label change_location(location_id = None, close_map = True):
    if location_id:
        python:
            new_location = get_location_by_id(location_id = location_id, locations = locations)
            prev_location = cur_location
            cur_location = new_location
            del new_location
    call change_room(cur_location.external_room_id) from _call_change_room
    call close_map from _call_close_map
    return

label go_previous_room:
    python:
        temp_room = cur_room
        cur_room = prev_room
        prev_room = temp_room
        del temp_room
    return

label open_map:
    if(not get_flags("goout")):
        "[block_goout_dialogue]"
        return

    if not cur_location:
        call change_room(room_id = cur_room.location_id) from _call_change_room_1
    
    $ cur_map_id = cur_location.map_id

    if (not map_open):
        call set_image_map from _call_set_image_map
        $ map_open = True
        call screen room_navigation
        return

label close_map:
    python:
        map_open = False
    return

label open_inventory:
    if (not inventory_open):
        $ inventory_open = True
        call screen room_navigation
        return

label close_inventory:
    python:
        inventory_open = False
    return

# Is opened in change_room when a room id is in closed rooms
label closed_room_event:
    if renpy.has_label("closed_room_event_custom"):
        call closed_room_event_custom from _call_closed_room_event_custom
    scene expression (bg_loc) as bg
    return

label set_image_map:
    scene expression maps[cur_map_id].background as bg
    return
