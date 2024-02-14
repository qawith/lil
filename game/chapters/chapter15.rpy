label stage_chapter15:

    if (number_stages_completed_in_quest["chapter1"] == 5): 

        stop music fadeout 2.0
        play music school

        show chap1511 with fade

        $ quick_menu = True

        ayumi "And here he is! I told you it's him!"
        ayumi "Hello, [mc_name]!"

        menu:
            "How are you, girls?":
                show chap1512_1 with dissolve
                ayumi "All good, but we've been waiting for you!"

            "How long have you been waiting for me here?":
                show chap1512_2 with dissolve
                "~Well... Just come a bit faster next time, okay?~"

        show chap1513 with dissolve

        yuno "Yeah, next time come on time, or we'll go without you."
        yuno "Although I'm not sure if there will be a next time."

        show chap1514 with dissolve

        ayumi "Of course, there will be! So, shall we go?"

        $ quick_menu = False

        show screen mid_text("We're going to Yuno's place.") with fade
        scene black
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1521 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        menu:
            "Wow, this is a bar!":
                $ yunoaff = yunoaff
            "I didn't think it's some biker hangout.":
                $ yunoaff -= 1
                show screen affection_hint_minus("-1 to Yuno's relationship!") with moveintop
                pause 1.0
                hide screen affection_hint_minus with moveouttop

        show chap1522 with dissolve

        yuno "You thought it was a grocery store?"
        
        show chap1523 with dissolve

        yuno "This is one of the best café-bars in Kyoto!"

        show chap1524 with dissolve

        yuno "Remember, newbie, Fudzivara-sama never chooses anything bad."

        show chap1525 with dissolve

        ayumi "Fudzivara-sama, Fudzivara-sama."
        ayumi "So much self-love in your words."

        show chap1526 with dissolve

        ayumi "But if it weren't for Yuno, I agree with you, this is really a nice place."
        ayumi "Although I don't really like such establishments, this one is one of the best in the city. Odd that it's not well-known among people."

        show chap1527 with dissolve

        yuno "Well, what will we order? Ayumi... I know, strawberry juice. Takahashi, as usual for you?"

        show chap1528 with dissolve

        rei "Yes."

        show chap1529 with dissolve

        yuno "And what about you, newbie?"

        menu:
            "Hmm, i don't know, what do you recommend?":
                $ yunoaff = yunoaff
            "Hmm, let me check.":
                $ yunoaff += 1
                show screen affection_hint_plus("+1 to Yuno's relationship!") with moveintop
                pause 1.0
                hide screen affection_hint_minus with moveouttop

        show chap15210 with dissolve

        yuno "Bla-bla-bla, no time for that. I'll order something to your liking."

        $ quick_menu = False

        show screen mid_text("Yuno ordered a drinks for all of us.") with fade
        scene black 
        pause 2.0
        show screen mid_text("We're take a seat with our order.") with fade
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap15211 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        yuno "So, let's begin?"

        show chap15212 with dissolve

        ayumi "Oh, maybe let's chat a bit more? Otherwise, it will be as always..."
        thinking "As always? What does she mean?"

        show chap15213 with dissolve

        yuno "Well.. Newbie... You from Poland, right?"
        yuno "How i heard, it's a very beautiful country."
        yuno "With good people and good food."

        show chap15214 with dissolve

        yuno "Also with good alcohol traditions."
        yuno "Can you tell us something about it?"
        mc "Oh sheeesh, of course."
        mc "Poland with our vodka and beer is a country of alcohol traditions."
        mc "We drink a lot, but we drink good."
        mc "Our Zubrovka is a mass-destruction weapon. Similar as Soplica, i'll like the Cherry one."

        show chap15215 with dissolve

        yuno "Oh, really? Can i try it someday?"
        mc "Of course, i'll bring you a bottle."
        yuno "Oh, thank you, newbie."
        ayumi "Let's change the topic, okay?"

        $ quick_menu = False

        show screen mid_text("We're talking about different things.") with fade
        scene black
        pause 2.0
        show screen mid_text("At this time, Yuno drinks one shot.") with fade
        pause 2.0
        show screen mid_text("Goes for another one.") with fade
        pause 1.5
        show screen mid_text("Then another...") with fade
        pause 1.5
        show screen mid_text("And again?") with fade
        pause 1.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap15217 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        yuno "Nooow beewbiee... One more?"

        show chap15218 with dissolve

        ayumi "Yuno-chan, you've had enough."

        show chap15219 with dissolve

        yuno "Shush... I'm not talking to you."

        show chap15220 with dissolve

        yuno "Newbiee... I... Thiss... One more, newbie."
        yuno "Fudzivara-sama says you should bring her another one! Newbiee..."

        menu:
            "I don't really...":
                $ yunoaff = yunoaff
            "Well, okay, let's have one more!":
                $ yunoaff += 1
                show screen affection_hint_plus("+1 to Yuno's relationship!") with moveintop
                pause 1.0
                hide screen affection_hint_plus with moveouttop
        
        show chap15221 with dissolve

        yuno "Oh-oh... You're starting to like me, newbiee! But wait... Rei... what do you... what do you say?"

        show chap15222 with dissolve

        rei "Fudzivara-chan, it's really time for us to go."

        show chap15223 with dissolve

        yuno "How boring you are... What if we go to the dorm... continue this there, take some more... and a bit more..."

        show chap15224 with dissolve

        ayumi "Yuno-chan, let's go, please."

        show chap15225 with dissolve

        yuno "Bla-bla-bla... Well, Ayumi-chan, you always listened to me, so now I have to listen to you... because..."
        yuno "Because I have no better friend than... than you, Ayumi!"

        $ quick_menu = False

        show screen mid_text("You leave the bar.") with fade
        scene black
        pause 1.5
        show screen mid_text("You're going to the dorm.") with fade
        pause 2.0
        show screen mid_text("Yuno says that she need a stop..") with fade
        pause 2.0
        show screen mid_text("Ayumi went with Yuno.") with fade
        pause 1.5
        show screen mid_text("Rei wait with you.") with fade
        pause 1.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1531 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        stop music fadeout 2.0
        play music bgm

        menu:
            "Is this something that happens often?":
                $ yunoaff = yunoaff
            "As I understood, this happens quite often.":
                $ yunoaff = yunoaff
        
        show chap1532 with dissolve

        rei "Well, not exactly often, but let's say it's not the first time."
        mc "How often do you all gather like this?"

        show chap1533 with dissolve

        rei "Well... it varies."

        menu:
            "You always answer so dryly...":
                $ yunoaff = yunoaff
            "Do you not like talking to me?":
                $ yunoaff = yunoaff

        show chap1534 with dissolve

        rei "I'm not very fond of interacting with other people, to be honest."
        rei "I mean, I often want to spend time with others, but not necessarily interact with them."
        rei "I prefer listening to people and, strange as it may sound, analyzing their words and behavior."

        show chap1535 with dissolve

        rei "So, don't think that I don't like you or anything. On the contrary, you're a good classmate. And I'd gladly repeat our walk today."
        mc "I'm sure we'll go out again."
        mc "And maybe Ishito will join us."
        mc "By the way, are you best friends with her?"

        show chap1536 with dissolve

        rei "Akane? Well, you could say that. She's probably the only one who doesn't care whether I respond or not."
        rei "I feel comfortable with her, despite her sometimes unbearable attitude towards everything."

        show chap1537 with dissolve

        rei "You might have thought that Akane has a bad opinion of you, but I assure you, that's not the case."
        thinking "Wow, I've never seen Rei so talkative."
        rei "The same goes for Fudzivara. She's just pretending she doesn't like you."
        thinking "And Yuno?!"

        show chap1538 with dissolve

        rei "Well, as for Kurosawa, I think you know what she thinks... Although..."
        rei "I've noticed that Kurosawa and Ishito..."

        show chap1539 with dissolve

        rei "Oh, never mind, they're already back, Fudzivara and Kurosawa..."

        thinking "What did she want to tell me.."

        $ reiaff += 1
        show screen affection_hint_plus("+1 to Rei's relationship!") with moveintop
        pause 1.0
        hide screen affection_hint_plus with moveouttop

        $ quick_menu = False

        show screen mid_text("Yuno and Ayumi back.") with fade
        scene black
        pause 1.5
        show screen mid_text("You all continued walking to the dorm.") with fade
        pause 2.0
        show screen mid_text("Finally, you're at the dorm.") with fade
        pause 1.5
        show screen mid_text("You said goodbye to everyone and went home.") with fade
        pause 2.0
        show screen mid_text("But.. You have a message from Yuno.") with fade
        pause 1.5
        show screen mid_text("That... You need return to her.") with fade
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1541 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = False

        yuno "Newbiee... I'm sorry for today... I was a bit drunk..."
        yuno "Go closer to me, please..."

        show screen mid_text("You're going closer to Yuno.") with fade
        scene black
        pause 1.5
        show screen mid_text("Yuno kiss you...") with fade
        pause 1.5

        show chap1542 with dissolve

        yuno "Bye-bye, newbiee... I'll see you tomorrow..."

        show screen mid_text("She quickly ran to her room...") with fade
        scene black
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        mc "Wait, what?!"

        $ quest_next_stage(id = "chapter1")
        $ quick_menu = False
        call wait(5) from _call_wait_5
        call change_room("corridor") from _call_change_room_3

    return
