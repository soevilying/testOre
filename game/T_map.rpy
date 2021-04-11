label T_outdoor:
    stop Flo
    stop Ebb
    stop Chet
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    $ Time.mins = Time.mins +5
    window hide None

    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 6 and Time.hours <= 17:
        scene outdoor 1 with dissolve
    elif True:
        scene outdoor 1n with dissolve

    if (Roushk.party == 2 or Roushk.party == 3):
        if Time.days == Roushk.endday and Time.hours >=23:
            jump Roushk_meko_battle_end2
        elif Time.days == Roushk.endday+1 and Time.hours >=0 and Time.hours <6:
            jump Roushk_meko_battle_end2
        elif Time.days >= Roushk.endday +1 and Time.hours >=6:
            jump Roushk_goodbye3
    if Nauxus.meet == 0:
        stop music fadeout 1
        jump Nauxus_meet
    elif True:
        stop music fadeout 1
    if Witer.sleep >= 4 and Witer.sleep <= 5 and Time.hours == 3:
        jump battle_ghost_w
    if (Ebb.tavern == 2 or Time.days >= 30) and Parif.meet == 0:
        if Chet.snowsfood == 0 or Chet.snowsfood ==3:
            $ Parif.meet = 1
            jump Parif_meet
        elif True:
            pass
    if Map.bathroom_openday <= Time.days and Map.bathroom_0 == 3:
        $ Map.bathroom_0 = 4
        if Map.bathroom == "EbbFlo":
            "You are on your way back to the tavern when you notice Witer pulling Hakan by the arm out of the tavern."
            "The red dragon looks like he hasn’t been getting enough sleep."
            e 1 "Guys!"
            "You rush over to talk to them."
            e 1 "What’s this all about Witer?"
            show hakan stand at left with dissolve
            show witer stand at right with dissolve
            w "[name], good you’re here."
            w "Everyone’s meeting at the bath house for the grand opening."
            e 1 "That’s right, it’s today. I nearly forgot."
            w "At least you’re here now."
            w "Unlike someone here who had to be dragged out of bed."
            h "Not so loud, don’t you know what a hangover is."
            w "Don’t you know what drinking in moderation is?"
            w "Now let’s go."
            hide hakan stand at left with dissolve
            hide witer stand at right with dissolve
            "You follow Witer while he drags Hakan by his side."
        elif True:


            "You are approaching the tavern when you notice both Snow and Hakan are leaving it."
            e 5 "Hey!"
            "You run over to them."
            show snow stand at left with dissolve
            show hakan stand at right with dissolve
            e 1 "You guys going somewhere?"
            s "It’s the grand opening of the bath house."
            s "Come on, everyone is going to be there."
            e 5 "Everyone, everyone? Even the eternally asleep friend of Hakan?"
            h "No, we tried to wake him up, but ¶”з†і­ййЏѓгѓ§жЊзј€иЇ."
            e 1 "I’m і­йЋ­йЋ°з­йЋ°†·еџ that guy."
            h "Don’t be, he’s ©ж„­ж†ѕеЁ‘еЏ‰ж†ѕеЁ‘и№­зЇѓж¶”з†·о›§ж¶”, Now come on."
            hide snow stand with dissolve
            hide hakan stand with dissolve
        jump Snow_bathroom_questline

    call screen outdoor with dissolve
    window show None
    show screen days
    if _return == 'tavern':
        scene tavern 1
        $ renpy.music.set_volume(1.0, 0.0, channel = "music")
        play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
        play sound "music/door.mp3"
        play Snow "music/char_snow.ogg"
        play Hakan "music/char_hakan.ogg"
        play Witer "music/char_witer.ogg"
        play Chet "music/char_chet.ogg"
        play Thane "music/thane.ogg"
        jump map1
        return
    if _return == 'exit':
        $ renpy.music.set_volume(1.0, 0.0, channel = "music")
        stop Chet
        jump forest_map0
        return
    if _return == 'barn':
        if Witer.squat == 1 and Time.days > 5 and Time.hours <13 and Time.hours >= 6:
            jump Witer_barn
        elif True:
            jump T_barn

    if _return == 'sign':
        e 1 "Tavern's sign, “Tavern of Spear”."
        jump T_outdoor
        return

    if _return == 'bathhouse':
        if Map.bathroom_0 == 2 and Map.bathroom == "EbbFlo":
            jump Snow_bathroom_questline

        if Map.bathroom_0 == 4:
            if Map.bathroom == "EbbFlo":
                play Ebb "music/char_ebb.ogg"
                play Flo "music/char_flo.ogg"
            jump T_bathhouse0
        elif True:
            "This large building, it has a sign that says it is a bath house."
            "However, try as you can the door does not budge."
            "It's locked."
            jump T_outdoor
        return

    return
screen outdoor:
    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'outdoor ground'
            hover 'outdoor hover'
        else:
            idle 'outdoor groundn'
            hover 'outdoor hovern'





















        vbox:
            xalign 0.52 ypos 0.4
            if Snow.hunt == 2:
                imagebutton:
                    idle "NPC/snow01.png"
                    hover "NPC/snow02.png"

                    action Return("Snow_meet")
            else:
                pass



        hotspot (206, 470, 190, 309) action Return("tavern")

        hotspot (1438, 485, 269, 394) action Return("barn")

        hotspot (64, 408, 145, 128) action Return("sign")

        hotspot (831, 619, 56, 145) action Return("bathhouse")

        hotspot (586, 950, 561, 117) action Return("exit")


    frame:
        xalign 0.97 ypos 0.84
        imagebutton:
            idle "UI/bag01.png"
            hover "UI/bag02.png"

            action Show("bag"),Hide("inventory_screen"),Show("inventory_screen", first_inventory=jane_inv),Show("EWinventory_view_new", inventory=jane_equipment)
    frame:
        xalign 0.89 ypos 0.84
        imagebutton:
            idle "UI/stats01.png"
            hover "UI/stats02.png"

            action Show("stats")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
