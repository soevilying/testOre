

label T_basement:
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Map.basement == 1:
        $ Map.basement = 2
    elif True:
        pass
    window hide None
    stop music fadeout 1
    scene basement 1 with dissolve
    play music "music/drip.ogg"
    if Meko.meet == 0:
        jump meko_meet
    elif True:
        pass
    call screen basement with dissolve
    window show None
    show screen days
    stop music fadeout 1
    if _return == 'tavern':
        scene tavern 1 with dissolve
        play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
        play Snow "music/char_snow.ogg"
        play Hakan "music/char_hakan.ogg"
        play Witer "music/char_witer.ogg"
        play Chet "music/char_chet.ogg"
        play Thane "music/thane.ogg"
        jump map1
    if _return == 'Meko_talk':
        jump meko_meet
        return
    if _return == 'Witer_sw':
        jump Witer_sw
        return

    if _return == 'WaH':
        scene basement 1 with dissolve
        if Hakan.quest == 7:
            "As you approach Hakan and Witer's room door."
            "You hear a loud snore vibrating through the door."
            e 6 "Guess Hakan is still out cold, best not to disturb him."
        elif True:
            "The door is locked."
            "There’s a faint earthy odour that reminds you of Witer."
            "This must be the room he shares with Hakan."
            "Best not to invade their privacy."
        jump T_basement

    return
screen basement:

    imagemap:
        idle 'basement ground'
        hover 'basement hover'





















        vbox:
            xalign 0.32 ypos 0.65
            if Snow.basement >= 2:
                imagebutton:
                    idle "NPC/meko01.png"
                    hover "NPC/meko02.png"

                    action Return("Meko_talk")
            else:
                pass

        vbox:
            xalign 0.21 ypos 0.62
            if Witer.sleep == 3 and Time.hours == 3:
                imagebutton:
                    idle "NPC/witer03.png"
                    hover "NPC/witer04.png"

                    action Return("Witer_sw")
            else:
                pass


        hotspot (611, 193, 339, 117) action Return("tavern")

        hotspot (1820, 526, 99, 465) action Return("WaH")


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
