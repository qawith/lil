default prev_room = None
default cur_room = rooms[0]
default prev_location = None
default cur_location = locations[0]
default cur_map_id = cur_location.map_id
default map_open = False
default inventory_open = False
default phone_open = False
default shop_open = False
default info_open = False
default quest_open = False
default dormitory_open = False

# list of closed rooms is checked change_room
# is composed of id = room_id and Commitment()
# expired elements are checked in after_spending_time, if you don't want an expiration: hour_stop = None
# TODO: Wiki
default closed_rooms = {}
