init python:
    from pythonpackages.nqtr.navigation import Room
    from pythonpackages.nqtr.navigation import Location
    from pythonpackages.nqtr.navigation import Map

define rooms = [
    Room(id="my_room", location_id="house", name=_("Your room"), button_icon="icon my room", background ="bg myroom",action_ids = ["sleep","nap",]), 
    Room(id="school_entrance", location_id="school", name=_("School entrance"), button_icon="icon school entrance", background ="bg schoolentrance"),
    Room(id="kitchen", location_id="dormitory", name=_("Kitchen"), button_icon="icon dormitory kitchen", background ="bg dormitorykitchen"),
    Room(id="akane_room", location_id="dormitory", name=_("Akane room"), button_icon="icon akane room", background ="bg akaneroom"),
    Room(id="ayumi_room", location_id="dormitory", name=_("Ayumi room"), button_icon="icon ayumi room", background ="bg ayumiroom"),
    Room(id="rei_room", location_id="dormitory", name=_("Rei room"), button_icon="icon rei room", background ="bg reiroom"),
    Room(id="yuno_room", location_id="dormitory", name=_("Yuno room"), button_icon="icon yuno room", background ="bg yunoroom"),
    Room(id="corridor", location_id="dormitory", name=_("Corridor"), button_icon="icon dormitory corridor", background ="bg dormitorycorridor"),
    Room(id="park_main", location_id="park", name=_("Park"), button_icon="icon park", background ="bg park"),
]

define locations = [
    Location(id ="house", map_id="map", external_room_id="my_room", name=_(" House"), picture_in_background="icon map house", xalign=0.389, yalign=0.491),
    Location(id ="school", map_id="map", external_room_id="school_entrance", name=_(" School"), picture_in_background="icon map school", xalign=0.628, yalign=0.455),
    Location(id ="dormitory", map_id ="map", external_room_id="kitchen", name=_("Dormitory"), picture_in_background="icon map dormitory", xalign=0.575, yalign=0.535),
    Location(id ="park", map_id ="map", external_room_id="park_main", name=_(" Park"), picture_in_background="icon map park", xalign=0.632, yalign=0.6238),
]

define maps = {
    "map": Map(
        name = _("Map"), background = "bg map",
        map_id_north = None,
        map_id_south = None,
        map_id_west = None,
        map_id_east = None,
    ),
}
