# Music ########################################################################

define audio.bgm = "<loop 0>audio/Cappuccino.mp3"
define audio.school = "<loop 0>audio/School.mp3"

# H-scenes voices ##############################################################

define audio.rei_main = "<loop 0>audio/h-scenes/rei_main.wav"
define audio.rei_climax = "<loop 0>audio/h-scenes/rei_climax.wav"
define audio.rei_blowjob = "<loop 0>audio/h-scenes/rei_blowjob.wav"
define audio.akane_main = "<loop 0>audio/h-scenes/akane_main.wav"
define audio.ayumi_main = "<loop 0>audio/h-scenes/ayumi_main.wav"
define audio.yuno_main = "<loop 0>audio/h-scenes/yuno_main.wav"
define audio.yuno_climax = "<loop 0>audio/h-scenes/yuno_climax.wav"
define audio.yuno_blowjob = "<loop 0>audio/h-scenes/yuno_blowjob.wav"

# Rooms ########################################################################
image pre icon my room = Transform("location/myroom-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon my room = LayeredImageMask("pre icon my room",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon school entrance = Transform("location/schoolentrance-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon school entrance = LayeredImageMask("pre icon school entrance",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon dormitory kitchen = Transform("location/dormitorykitchen-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon dormitory kitchen = LayeredImageMask("pre icon dormitory kitchen",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon dormitory corridor = Transform("location/dormitorycorridor-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon dormitory corridor = LayeredImageMask("pre icon dormitory corridor",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon akane room = Transform("location/akaneroom-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon akane room = LayeredImageMask("pre icon akane room",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon ayumi room = Transform("location/ayumiroom-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon ayumi room = LayeredImageMask("pre icon ayumi room",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon rei room = Transform("location/reiroom-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon rei room = LayeredImageMask("pre icon rei room",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon yuno room = Transform("location/yunoroom-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon yuno room = LayeredImageMask("pre icon yuno room",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon park = Transform("location/park-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon park = LayeredImageMask("pre icon park",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
# Map icons ####################################################################
image icon map house = "gui/map/map_house.webp"
image icon map school = "gui/map/map_school.webp"
image icon map dormitory = "gui/map/map_dormitory.webp"
image icon map park = "gui/map/map_park.webp"

# Map bg's #####################################################################
image bg map = "gui/map/map.webp"

# Location bg's ################################################################
image bg myroom = "location/myroom-[tm.timeslot_number].webp"
image bg schoolentrance = "location/schoolentrance-[tm.timeslot_number].webp"
image bg dormitorykitchen = "location/dormitorykitchen-[tm.timeslot_number].webp"
image bg dormitorycorridor = "location/dormitorycorridor-[tm.timeslot_number].webp"
image bg akaneroom = "location/akaneroom-[tm.timeslot_number].webp"
image bg ayumiroom = "location/ayumiroom-[tm.timeslot_number].webp"
image bg reiroom = "location/reiroom-[tm.timeslot_number].webp"
image bg yunoroom = "location/yunoroom-[tm.timeslot_number].webp"
image bg park = "location/park-[tm.timeslot_number].webp"

# Routines #####################################################################

image ayumi_morning_conversation = Movie(play = "images/conversation/ayumi/ayumi_morning.webm", loop = True, size = (1920, 1080))
image ayumi_morning_routine = "images/routine/ayumi/ayumi_morning.webp"
image yuno_morning_conversation = Movie(play = "images/conversation/yuno/yuno_morning.webm", loop = True, size = (1920, 1080))
image yuno_morning_routine = "images/routine/yuno/yuno_morning.webp"
image akane_morning_conversation = Movie(play = "images/conversation/akane/akane_morning.webm", loop = True, size = (1920, 1080))
image akane_morning_routine = "images/routine/akane/akane_morning.webp"
image rei_morning_conversation = Movie(play = "images/conversation/rei/rei_morning.webm", loop = True, size = (1920, 1080))
image rei_morning_routine = "images/routine/rei/rei_morning.webp"

# Events #######################################################################

## New Year 2024 ###############################################################

## Preparation #################################################################

image newyear2024_11 = "images/events/newyear2024/preparation/1.webp"
image newyear2024_12 = "images/events/newyear2024/preparation/2.webp"
image newyear2024_13 = "images/events/newyear2024/preparation/3.webp"
image newyear2024_14 = "images/events/newyear2024/preparation/4.webp"
image newyear2024_15 = "images/events/newyear2024/preparation/5.webp"
image newyear2024_16 = "images/events/newyear2024/preparation/6.webp"
image newyear2024_17 = "images/events/newyear2024/preparation/7.webp"
image newyear2024_18 = "images/events/newyear2024/preparation/8.webp"
image newyear2024_19 = "images/events/newyear2024/preparation/9.webp"
image newyear2024_110 = "images/events/newyear2024/preparation/10.webp"
image newyear2024_111 = "images/events/newyear2024/preparation/11.webp"
image newyear2024_112 = "images/events/newyear2024/preparation/12.webp"
image newyear2024_113 = "images/events/newyear2024/preparation/13.webp"
image newyear2024_114 = "images/events/newyear2024/preparation/14.webp"
image newyear2024_115 = "images/events/newyear2024/preparation/15.webp"
image newyear2024_116 = "images/events/newyear2024/preparation/16.webp"
image newyear2024_117 = "images/events/newyear2024/preparation/17.webp"
image newyear2024_118 = "images/events/newyear2024/preparation/18.webp"

image newyear2024_ayumi_cowgirl = Movie(play = "images/events/newyear2024/webm/ayumi_cowgirl.webm", loop = True, size = (1920, 1080))
image newyear2024_ayumi_handjob = Movie(play = "images/events/newyear2024/webm/ayumi_handjob.webm", loop = True, size = (1920, 1080))

## Main ########################################################################

image newyear2024_21 = "images/events/newyear2024/main/1.webp"
image newyear2024_22 = "images/events/newyear2024/main/2.webp"
image newyear2024_23 = "images/events/newyear2024/main/3.webp"
image newyear2024_24 = "images/events/newyear2024/main/4.webp"
image newyear2024_25 = "images/events/newyear2024/main/5.webp"
image newyear2024_26 = "images/events/newyear2024/main/6.webp"
image newyear2024_27 = "images/events/newyear2024/main/7.webp"
image newyear2024_28 = "images/events/newyear2024/main/8.webp"
image newyear2024_29 = "images/events/newyear2024/main/9.webp"
image newyear2024_210 = "images/events/newyear2024/main/10.webp"
image newyear2024_211 = "images/events/newyear2024/main/11.webp"
image newyear2024_212 = "images/events/newyear2024/main/12.webp"
image newyear2024_213 = "images/events/newyear2024/main/13.webp"
image newyear2024_214 = "images/events/newyear2024/main/14.webp"
image newyear2024_215 = "images/events/newyear2024/main/15.webp"
image newyear2024_216 = "images/events/newyear2024/main/16.webp"
image newyear2024_217 = "images/events/newyear2024/main/17.webp"

image newyear2024_yuno_cowgirl = Movie(play = "images/events/newyear2024/webm/yuno_cowgirl.webm", loop = True, size = (1920, 1080))
image newyear2024_akane_cowgirl = Movie(play = "images/events/newyear2024/webm/akane_cowgirl.webm", loop = True, size = (1920, 1080))
image newyear2024_yuno_blowjob = Movie(play = "images/events/newyear2024/webm/yuno_blowjob.webm", loop = True, size = (1920, 1080))
image newyear2024_yuno_climax = Movie(play = "images/events/newyear2024/webm/yuno_climax.webm", loop = True, size = (1920, 1080))

## Pool ########################################################################

image newyear2024_31 = "images/events/newyear2024/pool/1.webp"
image newyear2024_32 = "images/events/newyear2024/pool/2.webp"
image newyear2024_33 = "images/events/newyear2024/pool/3.webp"
image newyear2024_34 = "images/events/newyear2024/pool/4.webp"
image newyear2024_35 = "images/events/newyear2024/pool/5.webp"
image newyear2024_36 = "images/events/newyear2024/pool/6.webp"
image newyear2024_37 = "images/events/newyear2024/pool/7.webp"
image newyear2024_38 = "images/events/newyear2024/pool/8.webp"

image newyear2024_rei_blowjob = Movie(play = "images/events/newyear2024/webm/rei_blowjob.webm", loop = True, size = (1920, 1080))
image newyear2024_rei_doggy = Movie(play = "images/events/newyear2024/webm/rei_doggy.webm", loop = True, size = (1920, 1080))
image newyear2024_rei_climax = Movie(play = "images/events/newyear2024/webm/rei_climax.webm", loop = True, size = (1920, 1080))

# Chapters #####################################################################

## Chapter 1.1 #################################################################

## 1my_room:

image chap1111 = "images/story/chapter1/chapter11/1my_room/1.jpg"
image chap1112 = "images/story/chapter1/chapter11/1my_room/2.jpg"

## 2school_entrance:

image chap1121 = Movie(size = (1920, 1080), channel = "movie", play = "images/story/chapter1/chapter11/2school_entrance/1.webm", loop = True) 
image chap1122 = "images/story/chapter1/chapter11/2school_entrance/2.jpg"
image chap1123 = "images/story/chapter1/chapter11/2school_entrance/3.jpg"
image chap1124 = "images/story/chapter1/chapter11/2school_entrance/4.jpg"
image chap1125 = "images/story/chapter1/chapter11/2school_entrance/5.jpg"
image chap1126 = "images/story/chapter1/chapter11/2school_entrance/6.jpg" 
image chap1127 = "images/story/chapter1/chapter11/2school_entrance/7.jpg" 
image chap1128 = "images/story/chapter1/chapter11/2school_entrance/8.jpg"
image chap1129 = "images/story/chapter1/chapter11/2school_entrance/9.jpg" 
image chap11210 = "images/story/chapter1/chapter11/2school_entrance/10.jpg" 
image chap11211 = "images/story/chapter1/chapter11/2school_entrance/11.jpg" 
image chap11212 = "images/story/chapter1/chapter11/2school_entrance/12.jpg" 
image chap11213 = "images/story/chapter1/chapter11/2school_entrance/13.jpg" 
image chap11214 = "images/story/chapter1/chapter11/2school_entrance/14.jpg" 
image chap11215 = "images/story/chapter1/chapter11/2school_entrance/15.jpg" 
image chap11216 = "images/story/chapter1/chapter11/2school_entrance/16.jpg" 
image chap11217 = "images/story/chapter1/chapter11/2school_entrance/17.jpg" 
image chap11218 = "images/story/chapter1/chapter11/2school_entrance/18.jpg" 
image chap11219 = "images/story/chapter1/chapter11/2school_entrance/19.jpg" 
image chap11220 = "images/story/chapter1/chapter11/2school_entrance/20.jpg" 
image chap11221 = "images/story/chapter1/chapter11/2school_entrance/21.jpg" 
image chap11222 = "images/story/chapter1/chapter11/2school_entrance/22.jpg" 
image chap11223 = "images/story/chapter1/chapter11/2school_entrance/23.jpg"
image chap11224 = "images/story/chapter1/chapter11/2school_entrance/24.jpg"
image chap11225 = "images/story/chapter1/chapter11/2school_entrance/25.jpg"
image chap11226 = "images/story/chapter1/chapter11/2school_entrance/26.jpg"   

## 3school_classroom:

image chap1131 = "images/story/chapter1/chapter11/3school_classroom/1.jpg"
image chap1132 = "images/story/chapter1/chapter11/3school_classroom/2.jpg"
image chap1133 = "images/story/chapter1/chapter11/3school_classroom/3.jpg"
image chap1134 = "images/story/chapter1/chapter11/3school_classroom/4.jpg"
image chap1135 = "images/story/chapter1/chapter11/3school_classroom/5.jpg"
image chap1136 = "images/story/chapter1/chapter11/3school_classroom/6.jpg"

## 4school_entrance:

image chap1141 = "images/story/chapter1/chapter11/4school_entrance/1.jpg"
image chap1142 = "images/story/chapter1/chapter11/4school_entrance/2.jpg"
image chap1143 = "images/story/chapter1/chapter11/4school_entrance/3.jpg"
image chap1144 = "images/story/chapter1/chapter11/4school_entrance/4.jpg"
image chap1145 = "images/story/chapter1/chapter11/4school_entrance/5.jpg"
image chap1146 = "images/story/chapter1/chapter11/4school_entrance/6.jpg"
image chap1147 = "images/story/chapter1/chapter11/4school_entrance/7.jpg"
image chap1148 = "images/story/chapter1/chapter11/4school_entrance/8.jpg"
image chap1149 = "images/story/chapter1/chapter11/4school_entrance/9.jpg"
image chap11410 = "images/story/chapter1/chapter11/4school_entrance/10.jpg"
image chap11411 = "images/story/chapter1/chapter11/4school_entrance/11.jpg"

## Chapter 1.2 #################################################################

## 1my_room:

## (картинки з Chapter 1.1, 1my_room для зменшення ваги гри)

## 2rei_room:

image chap1221 = "images/story/chapter1/chapter12/2rei_room/1.jpg"
image chap1222 = "images/story/chapter1/chapter12/2rei_room/2.jpg"
image chap1223 = "images/story/chapter1/chapter12/2rei_room/3.jpg"
image chap1224_1 = "images/story/chapter1/chapter12/2rei_room/4_1.jpg"
image chap1224_2 = "images/story/chapter1/chapter12/2rei_room/4_2.jpg"
image chap1225_1 = "images/story/chapter1/chapter12/2rei_room/5_1.jpg"
image chap1225_2 = "images/story/chapter1/chapter12/2rei_room/5_2.jpg"
image chap1226 = "images/story/chapter1/chapter12/2rei_room/6.jpg"
image chap1227 = "images/story/chapter1/chapter12/2rei_room/7.jpg"
image chap1228 = "images/story/chapter1/chapter12/2rei_room/8.jpg"
image chap1229 = "images/story/chapter1/chapter12/2rei_room/9.jpg"

## 3akane_room:

image chap1231 = "images/story/chapter1/chapter12/3akane_room/1.jpg"
image chap1232 = "images/story/chapter1/chapter12/3akane_room/2.jpg"
image chap1233_1 = "images/story/chapter1/chapter12/3akane_room/3_1.jpg"
image chap1233_2 = "images/story/chapter1/chapter12/3akane_room/3_2.jpg"
image chap1234 = "images/story/chapter1/chapter12/3akane_room/4.jpg"
image chap1235 = "images/story/chapter1/chapter12/3akane_room/5.jpg"
image chap1236 = "images/story/chapter1/chapter12/3akane_room/6.jpg"
image chap1237 = "images/story/chapter1/chapter12/3akane_room/7.jpg"

## 4dormitory_kitchen: 

image chap1241 = "images/story/chapter1/chapter12/4dorminity_kitchen/1.jpg"
image chap1242 = "images/story/chapter1/chapter12/4dorminity_kitchen/2.jpg"
image chap1243 = "images/story/chapter1/chapter12/4dorminity_kitchen/3.jpg"
image chap1244 = "images/story/chapter1/chapter12/4dorminity_kitchen/4.jpg"
image chap1245_1 = "images/story/chapter1/chapter12/4dorminity_kitchen/5_1.jpg"
image chap1245_2 = "images/story/chapter1/chapter12/4dorminity_kitchen/5_2.jpg"
image chap1246 = "images/story/chapter1/chapter12/4dorminity_kitchen/6.jpg"
image chap1247 = "images/story/chapter1/chapter12/4dorminity_kitchen/7.jpg"
image chap1248 = "images/story/chapter1/chapter12/4dorminity_kitchen/8.jpg"
image chap1249 = "images/story/chapter1/chapter12/4dorminity_kitchen/9.jpg"
image chap12410 = "images/story/chapter1/chapter12/4dorminity_kitchen/10.jpg"
image chap12411 = "images/story/chapter1/chapter12/4dorminity_kitchen/11.jpg"
image chap12412 = "images/story/chapter1/chapter12/4dorminity_kitchen/12.jpg"
image chap12413 = "images/story/chapter1/chapter12/4dorminity_kitchen/13.jpg"
image chap12414 = "images/story/chapter1/chapter12/4dorminity_kitchen/14.jpg"
image chap12415 = "images/story/chapter1/chapter12/4dorminity_kitchen/15.jpg"
image chap12416 = "images/story/chapter1/chapter12/4dorminity_kitchen/16.jpg"
image chap12417 = "images/story/chapter1/chapter12/4dorminity_kitchen/17.jpg"
image chap12418 = "images/story/chapter1/chapter12/4dorminity_kitchen/18.jpg"
image chap12419 = "images/story/chapter1/chapter12/4dorminity_kitchen/19.jpg"
image chap12420 = "images/story/chapter1/chapter12/4dorminity_kitchen/20.jpg"

## Chapter 1.3 #################################################################

## 1school_entrance:

image chap1311 = "images/story/chapter1/chapter13/1school_entrance/1.jpg"
image chap1312 = "images/story/chapter1/chapter13/1school_entrance/2.jpg"
image chap1313 = "images/story/chapter1/chapter13/1school_entrance/3.jpg"
image chap1314_1 = "images/story/chapter1/chapter13/1school_entrance/4_1.jpg"
image chap1314_2 = "images/story/chapter1/chapter13/1school_entrance/4_2.jpg"
image chap1315 = "images/story/chapter1/chapter13/1school_entrance/5.jpg"
image chap1316 = "images/story/chapter1/chapter13/1school_entrance/6.jpg"
image chap1317_1 = "images/story/chapter1/chapter13/1school_entrance/7_1.jpg"
image chap1317_2 = "images/story/chapter1/chapter13/1school_entrance/7_2.jpg"

## 2school_classroom:

image chap1321 = "images/story/chapter1/chapter13/2school_classroom/1.jpg"
image chap1322 = "images/story/chapter1/chapter13/2school_classroom/2.jpg"
image chap1323 = "images/story/chapter1/chapter13/2school_classroom/3.jpg"
image chap1324 = "images/story/chapter1/chapter13/2school_classroom/4.jpg"
image chap1325 = "images/story/chapter1/chapter13/2school_classroom/5.jpg"

## 3school_entrance:

image chap1331 = "images/story/chapter1/chapter13/3school_entrance/1.jpg"
image chap1332 = "images/story/chapter1/chapter13/3school_entrance/2.jpg"
image chap1333 = "images/story/chapter1/chapter13/3school_entrance/3.jpg"
image chap1334 = "images/story/chapter1/chapter13/3school_entrance/4.jpg"
image chap1335 = "images/story/chapter1/chapter13/3school_entrance/5.jpg"
image chap1336_1 = "images/story/chapter1/chapter13/3school_entrance/6_1.jpg"
image chap1336_2 = "images/story/chapter1/chapter13/3school_entrance/6_2.jpg"
image chap1337 = "images/story/chapter1/chapter13/3school_entrance/7.jpg"
image chap1338 = "images/story/chapter1/chapter13/3school_entrance/8.jpg"
image chap1339_1 = "images/story/chapter1/chapter13/3school_entrance/9_1.jpg"
image chap1339_2 = "images/story/chapter1/chapter13/3school_entrance/9_2.jpg"

## Chapter 1.4 #################################################################

## 1ayumi_room:

image chap1411 = "images/story/chapter1/chapter14/1ayumi_room/1.webp"
image chap1412 = "images/story/chapter1/chapter14/1ayumi_room/2.webp"
image chap1413 = "images/story/chapter1/chapter14/1ayumi_room/3.webp"
image chap1414 = "images/story/chapter1/chapter14/1ayumi_room/4.webp"
image chap1415_1 = "images/story/chapter1/chapter14/1ayumi_room/5_1.webp"
image chap1415_2 = "images/story/chapter1/chapter14/1ayumi_room/5_2.webp"
image chap1416 = "images/story/chapter1/chapter14/1ayumi_room/6.webp"
image chap1417 = "images/story/chapter1/chapter14/1ayumi_room/7.webp"
image chap1418 = "images/story/chapter1/chapter14/1ayumi_room/8.webp"
image chap1419 = "images/story/chapter1/chapter14/1ayumi_room/9.webp"
image chap14110 = "images/story/chapter1/chapter14/1ayumi_room/10.webp"
image chap14111 = "images/story/chapter1/chapter14/1ayumi_room/11.webp"
image chap14112 = "images/story/chapter1/chapter14/1ayumi_room/12.webp"
image chap14113 = "images/story/chapter1/chapter14/1ayumi_room/13.webp"
image chap14114 = "images/story/chapter1/chapter14/1ayumi_room/14.webp"
image chap14115 = "images/story/chapter1/chapter14/1ayumi_room/15.webp"
image chap14116 = "images/story/chapter1/chapter14/1ayumi_room/16.webp"
image chap14117_1 = "images/story/chapter1/chapter14/1ayumi_room/17_1.webp"
image chap14117_2 = "images/story/chapter1/chapter14/1ayumi_room/17_2.webp"
image chap14118 = "images/story/chapter1/chapter14/1ayumi_room/18.webp"
image chap14119 = "images/story/chapter1/chapter14/1ayumi_room/19.webp"
image chap14120 = "images/story/chapter1/chapter14/1ayumi_room/20.webp"
image chap14121 = "images/story/chapter1/chapter14/1ayumi_room/21.webp"

## 2dormitory_kitchen:

image chap1421 = "images/story/chapter1/chapter14/2dormitory_kitchen/1.webp"
image chap1422 = "images/story/chapter1/chapter14/2dormitory_kitchen/2.webp"
image chap1423 = "images/story/chapter1/chapter14/2dormitory_kitchen/3.webp"
image chap1424_1 = "images/story/chapter1/chapter14/2dormitory_kitchen/4_1.webp"
image chap1424_2 = "images/story/chapter1/chapter14/2dormitory_kitchen/4_2.webp"
image chap1425 = "images/story/chapter1/chapter14/2dormitory_kitchen/5.webp"
image chap1426 = "images/story/chapter1/chapter14/2dormitory_kitchen/6.webp"
image chap1427 = "images/story/chapter1/chapter14/2dormitory_kitchen/7.webp"
image chap1428 = "images/story/chapter1/chapter14/2dormitory_kitchen/8.webp"
image chap1429 = "images/story/chapter1/chapter14/2dormitory_kitchen/9.webp"
image chap14210 = "images/story/chapter1/chapter14/2dormitory_kitchen/10.webp"
image chap14211 = "images/story/chapter1/chapter14/2dormitory_kitchen/11.webp"
image chap14212 = "images/story/chapter1/chapter14/2dormitory_kitchen/12.webp"

## Chapter 1.5 #################################################################

## 1city_park:

image chap1511 = "images/story/chapter1/chapter15/1city_park/1.webp"
image chap1512_1 = "images/story/chapter1/chapter15/1city_park/2_1.webp"
image chap1512_2 = "images/story/chapter1/chapter15/1city_park/2_2.webp"
image chap1513 = "images/story/chapter1/chapter15/1city_park/3.webp"
image chap1514 = "images/story/chapter1/chapter15/1city_park/4.webp"

## 2dead_or_alive:

image chap1521 = "images/story/chapter1/chapter15/2dead_or_alive/1.webp"
image chap1522 = "images/story/chapter1/chapter15/2dead_or_alive/2.webp"
image chap1523 = "images/story/chapter1/chapter15/2dead_or_alive/3.webp"
image chap1524 = "images/story/chapter1/chapter15/2dead_or_alive/4.webp"
image chap1525 = "images/story/chapter1/chapter15/2dead_or_alive/5.webp"
image chap1526 = "images/story/chapter1/chapter15/2dead_or_alive/6.webp"
image chap1527 = "images/story/chapter1/chapter15/2dead_or_alive/7.webp"
image chap1528 = "images/story/chapter1/chapter15/2dead_or_alive/8.webp"
image chap1529 = "images/story/chapter1/chapter15/2dead_or_alive/9.webp"
image chap15210 = "images/story/chapter1/chapter15/2dead_or_alive/10.webp"
image chap15211 = "images/story/chapter1/chapter15/2dead_or_alive/11.webp"
image chap15212 = "images/story/chapter1/chapter15/2dead_or_alive/12.webp"
image chap15213 = "images/story/chapter1/chapter15/2dead_or_alive/13.webp"
image chap15214 = "images/story/chapter1/chapter15/2dead_or_alive/14.webp"
image chap15215 = "images/story/chapter1/chapter15/2dead_or_alive/15.webp"
image chap15217 = "images/story/chapter1/chapter15/2dead_or_alive/17.webp"
image chap15218 = "images/story/chapter1/chapter15/2dead_or_alive/18.webp"
image chap15219 = "images/story/chapter1/chapter15/2dead_or_alive/19.webp"
image chap15220 = "images/story/chapter1/chapter15/2dead_or_alive/20.webp"
image chap15221 = "images/story/chapter1/chapter15/2dead_or_alive/21.webp"
image chap15222 = "images/story/chapter1/chapter15/2dead_or_alive/22.webp"
image chap15223 = "images/story/chapter1/chapter15/2dead_or_alive/23.webp"
image chap15224 = "images/story/chapter1/chapter15/2dead_or_alive/24.webp"
image chap15225 = "images/story/chapter1/chapter15/2dead_or_alive/25.webp"

## 3city_park:

image chap1531 = "images/story/chapter1/chapter15/3city_park/1.webp"
image chap1532 = "images/story/chapter1/chapter15/3city_park/2.webp"
image chap1533 = "images/story/chapter1/chapter15/3city_park/3.webp"
image chap1534 = "images/story/chapter1/chapter15/3city_park/4.webp"
image chap1535 = "images/story/chapter1/chapter15/3city_park/5.webp"
image chap1536 = "images/story/chapter1/chapter15/3city_park/6.webp"
image chap1537 = "images/story/chapter1/chapter15/3city_park/7.webp"
image chap1538 = "images/story/chapter1/chapter15/3city_park/8.webp"
image chap1539 = "images/story/chapter1/chapter15/3city_park/9.webp"

## 3dormitory_corridor:

image chap1541 = "images/story/chapter1/chapter15/4dormitory_corridor/1.webp"
image chap1542 = "images/story/chapter1/chapter15/4dormitory_corridor/2.webp"

## Chapter 1.6 #################################################################

## 1school_entrance:

image chap1611 = "images/story/chapter1/chapter16/1school_entrance/1.webp"
image chap1612 = "images/story/chapter1/chapter16/1school_entrance/2.webp"
image chap1613 = "images/story/chapter1/chapter16/1school_entrance/3.webp"
image chap1614 = "images/story/chapter1/chapter16/1school_entrance/4.webp"
image chap1615 = "images/story/chapter1/chapter16/1school_entrance/5.webp"
image chap1616 = "images/story/chapter1/chapter16/1school_entrance/6.webp"
image chap1617 = "images/story/chapter1/chapter16/1school_entrance/7.webp"
image chap1618 = "images/story/chapter1/chapter16/1school_entrance/8.webp"
image chap1619 = "images/story/chapter1/chapter16/1school_entrance/9.webp"

## 2school_corridor:

image chap1621 = "images/story/chapter1/chapter16/2school_corridor/1.webp"
image chap1622 = "images/story/chapter1/chapter16/2school_corridor/2.webp"
image chap1623 = "images/story/chapter1/chapter16/2school_corridor/3.webp"
image chap1624 = "images/story/chapter1/chapter16/2school_corridor/4.webp"
image chap1625 = "images/story/chapter1/chapter16/2school_corridor/5.webp"
image chap1626 = "images/story/chapter1/chapter16/2school_corridor/6.webp"
image chap1627 = "images/story/chapter1/chapter16/2school_corridor/7.webp"
image chap1628 = "images/story/chapter1/chapter16/2school_corridor/8.webp"
image chap1629 = "images/story/chapter1/chapter16/2school_corridor/9.webp"
image chap16210 = "images/story/chapter1/chapter16/2school_corridor/10.webp"

## 3school_classroom: 

image chap1631 = "images/story/chapter1/chapter16/3school_classroom/1.webp"
image chap1632 = "images/story/chapter1/chapter16/3school_classroom/2.webp"

## 4school_entrance:

image chap1641 = "images/story/chapter1/chapter16/4school_entrance/1.webp"
image chap1642 = "images/story/chapter1/chapter16/4school_entrance/2.webp"
