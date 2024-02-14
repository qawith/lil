init python:
    from pythonpackages.nqtr.quest import Stage
    from pythonpackages.nqtr.quest import Quest

# if you need a description of the quest that true over time this dictionary seemed to me the best way to do it
default quests_descriptions = {}

define quests = {
    "chapter1": Quest(
        id = "chapter1",
        title = _("Chapter 1"),
        info_image = "location/schoolentrance-1.webp",
        stage_ids = ["chapter11", "chapter12_1", "chapter12_2", "chapter13", "chapter14", "chapter15", "chapter16"], 
        description = _("\n"),
        development = True,
    ),
    "newyear2024": Quest(
        id = "newyear2024",
        title = _("New Year 2024"),
        info_image = "location/schoolentrance-1.webp",
        stage_ids = ["newyear2024_preparation", "newyear2024_main"], 
        description = _("\nHappy New Year 2024!"),
        development = False,
    )
}
define quest_stages = {
    # Quest "chapter1"
    "chapter11" : Stage(quest_id = "chapter1", title = _("\nNew Path, New Friends"), description = _("Go to school. (8:00)"), start_label_name="stagestart_chapter11"),
    "chapter12_1" : Stage(quest_id = "chapter1", title = _("\nOne message that change everything..."), description = _("Wait for Ayumi message.. (next morning)"), start_label_name="stagestart_chapter12_1"),
    "chapter12_2" : Stage(quest_id = "chapter1", title = _("\nJoint Efforts"), description = _("Go to Rei room at dormitory. (10:00)"), start_label_name="stagestart_chapter12_2"),
    "chapter13" : Stage(quest_id = "chapter1", title = _("\nTest Day Troubles"), description = _("Go to school at next day. (8:00)"), start_label_name="stagestart_chapter13"),
    "chapter14" : Stage(quest_id = "chapter1", title = _("\nAiming for Success"), description = _("Go to Ayumi room at dormitory. (10:00)"), start_label_name="stagestart_chapter14"),
    "chapter15" : Stage(quest_id = "chapter1", title = _("\nMemories in the Making"), description = _("Go to park. (15:00)"), start_label_name="stagestart_chapter15"),
    "chapter16" : Stage(quest_id = "chapter1", title = _("\nA Second Chance"), description = _("Go to school at next day. (8:00)"), start_label_name="stagestart_chapter16"),
    # Quest "newyear2024"
    "newyear2024_preparation" : Stage(quest_id = "newyear2024", title = _("\nNew Year Preparation"), description = _("Go to Ayumi room at dormitory. (8:00)"), start_label_name="stagestart_newyear2024_preparation"),
    "newyear2024_main" : Stage(quest_id = "newyear2024", title = _("\nNew Year Day"), description = _("Go to kitchen at dormitory. (10:00)"), start_label_name="stagestart_newyear2024_main"),
}

label stagestart_chapter11:
    $ routine["chapter11"] = Commitment(characters=[ayumi, akane, rei, akira, yuno], hour_start=8, hour_stop=9, location_id="school", room_id="school_entrance", event_label_name="stage_chapter11")
    return

label stagestart_chapter12_1:
    $ routine["chapter12_1"] = Commitment(characters=None, hour_start=7, hour_stop=10, location_id="house", room_id="my_room", event_label_name="stage_chapter12_1")
    return

label stagestart_chapter12_2:
    $ routine["chapter12_2"] = Commitment(characters=[rei], hour_start=9, hour_stop=10, location_id="dormitory", room_id="rei_room", event_label_name="stage_chapter12_2")
    return

label stagestart_chapter13:
    $ routine["chapter13"] = Commitment(characters=[ayumi, akane, rei, akira, yuno], hour_start=8, hour_stop=9, location_id="school", room_id="school_entrance", event_label_name="stage_chapter13")
    return

label stagestart_chapter14:
    $ routine["chapter14"] = Commitment(characters=[ayumi], hour_start=10, hour_stop=11, location_id="dormitory", room_id="ayumi_room", event_label_name="stage_chapter14")
    return

label stagestart_chapter15:
    $ routine["chapter15"] = Commitment(characters=[ayumi, akane, rei, yuno], hour_start=15, hour_stop=16, location_id="park", room_id="park_main", event_label_name="stage_chapter15")
    return

label stagestart_chapter16:
    $ routine["chapter16"] = Commitment(characters=[ayumi], hour_start=8, hour_stop=9, location_id="school", room_id="school_entrance", event_label_name="stage_chapter16")
    return

label stagestart_newyear2024_preparation:
    $ routine["newyear2024_preparation"] = Commitment(characters=[ayumi], hour_start=8, hour_stop=9, location_id="dormitory", room_id="ayumi_room", event_label_name="stage_newyear2024_invitation")
    return

label stagestart_newyear2024_main:
    $ routine["newyear2024_main"] = Commitment(characters=[ayumi], hour_start=10, hour_stop=11, location_id="dormitory", room_id="kitchen", event_label_name="stage_newyear2024_main")