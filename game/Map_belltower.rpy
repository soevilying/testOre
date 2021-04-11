label belltower_map0:
    stop music
    stop Thane
    stop Chan1
    stop Chan2
    $ renpy.music.set_volume(1, 1, channel = "Chan1")
    play Chan1[ "<silence 0.5>", "music/btower.ogg" ]fadein 3
    if Map.bt0 == 0:
        scene black with vslow_dissolve
        if Zalt.A_lv >2:
            "You enter a new dungeon, your Adventure LV set back to 2."
            $ Zalt.A_lv = 2
        "You enter the top of the clocktower."
        "The moment your feet meet the floor, a thick plume of dust shoots up into the air. "
        scene belltower 2 with vslow_dissolve
        "You cough and cover your nose."
        "Waving away the dust, you look around for a way down. "
        $ Map.bt0 = 1
    pause 0.5
    jump belltower_map


label belltower_map:
    stop music
    $ Zalt.dungeon = True
    $ config.rollback_enabled = False
    $ renpy.music.set_pause(False, channel='Chan1')
    window hide None
    if Zalt.Dungeon_leave:
        jump cave_leave
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Zalt.A_exp >= 100:
        $ Zalt.A_exp = Zalt.A_exp -100
        $ Zalt.A_lv = min(Zalt.A_lv + 1, 5)
        $ Zalt.AP = Zalt.AP +1
        "You get one AP, you have [Zalt.AP] now."
        "Your A-LV now is [Zalt.A_lv]"


    if Zalt.A_lv == 5:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 4:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 3:
        $ Zalt.A_exp_lv = 2
    elif Zalt.A_lv == 2:
        $ Zalt.A_exp_lv = 1.5
    elif Zalt.A_lv == 1:
        $ Zalt.A_exp_lv = 1.2
    elif True:
        $ Zalt.A_exp_lv = 1

    if Map.bt2 == 2:
        scene belltower 1 with dissolve
    elif True:
        scene belltower 2 with dissolve
    call screen belltower_map with dissolve
    if _return == 'exit':
        $ Time.mins = Time.mins +10
        "You grabbed the rope and climbed up."
        jump Cave_map0
        return
    if _return == 'point 1':
        $ Time.mins = Time.mins +10
        "You peer through the large hole in the middle of the room."
        "Down below lies the bell you saw earlier. "
        e 1 "That thing looked closer before."
        e 13 "Hmm..."
        e 1 "Jumping down isn’t going to be an option. "
        "Just then you spot a partition on the floor just across from you."
        "You head over to open it to find a ladder leading down."
        "The ladder looks and feels old, but you rather take a chance going down than stay up in this blistering humid room any longer."
        "You head down the ladder."
        $ Map.bt1 = 2
        $ Map.bt2 = 1
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump belltower_map
    if _return == 'point 2':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "On your way down the stone spiral stairway you stop on your tracks as the view in front of you enthralls you. "
        "The entire landscape is bathed in ice cold light. "
        scene belltower 1 with vslow_dissolve
        "Up ahead a majestic structure beckons your adventurer’s soul. "
        e 9 "Is that a castle? All this time all of this has been beneath the forest? "
        "You take a minute to absorb the view before continuing your walk downwards."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.bt2 = 2
        $ Map.bt3 = 1
        jump belltower_map

    if _return == 'point 3':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "You climb down to a lower floor."
        "There’s nothing inside here, but it does lead to a flight of stone stairs that will take you even further downwards. "
        scene black with slow_dissolve
        "You descend further."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.bt3 = 2
        $ Map.bt4 = 1
        $ Map.bt5 = 1
        jump belltower_map


    if _return == 'point 4':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.bt4bell == 0:
            "You head all the way down, the heat from the poorly ventilated clocktower has you drenched in sweat."
            "Here lies the bell that used to be on top of this clocktower."
            "You approach it and place your hand on its cool metal surface."
            e 1 "What’s that?"
            "Just behind the bell you see what looks like a collection box."
            e 1 "What are the chances there’d be some coin in there?"
            e 1 "If only this bell wasn’t in the way."
            e 13 "The gap is too small for me to squeeze through."
            e 1 "But if I’m strong enough I should be able to pull the bell a bit to the side for me to fit."
            "Do you want to try to move the bell?"
            $ Map.bt4bell = 1
            jump belltower_bell
        elif Map.bt4bell == 1:
            "The bell is still there."
            "Do you want to try to move the bell?"
            jump belltower_bell
        elif Map.bt4bell == 2:
            "There is only one clock here."
            jump belltower_map
        label belltower_bell:
            menu:
                "Yes" if True:
                    if Zalt.str >= 6:
                        e 12 "Hrgh!"
                        "{b}{color=#19c22a}<Strength Check success>{/color}"
                        $ Map.bt4bell = 2
                        "You grab the bell by the sides and pull as hard as you can to the left."
                        "The bell refuses to move."
                        "You clutch the side of the bell harder, and with a mighty roar you focus all your strength into your arms and legs."
                        "Slowly, the metal barrier begins to move."
                        "You hear the sound of wood breaking in front of you as the bell moves but you pay it no heed and pull harder."
                        "Once the bell moves aside you have enough space to pass through."
                        "You jump over the trench in the floor you made and make your way to the box."
                        "With your sword, you break open the box."
                        "You get 138 coins."
                        $ jane_inv.take(coin,138)
                        $ Zalt.A_exp = Zalt.A_exp + 30*Zalt.A_exp_lv
                        $ PPEXP = 30*Zalt.A_exp_lv
                        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                        jump belltower_map
                    elif True:
                        e 12 "Hrgh!"
                        "{b}{color=#c22719}<Strength Check failed>{/color}"
                        "You grab the bell by the sides and pull as hard as you can to the left."
                        "The bell refuses to move."
                        "Try as you can the stubborn hunk of metal just won’t budge."
                        jump belltower_map
                "No" if True:
                    jump belltower_map
    if _return == 'point 5':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "You exit the clocktower. "
        e 5 "Wow."
        "You stand in awe at your surroundings."
        "Everything is bathed in a gentle blue glow."
        "Looking up, you can see the walls of this entire cave are lined with glowing fungus and moss."
        "To your right is the mighty structure you saw from before; it’s a castle."
        "Its rooftops extend upward, almost touching the ceiling of the cave."
        "The wall that surrounds the castle is in disarray."
        "There are cracks that run along it, scars from a previous battle."
        "You notice that a few feet in front of you is the edge of a cliff."
        "Wherever you are, you best mind your step."
        "You take out Flo’s gloves and sniff it to make sure you’re on the right track."
        "His scent leads you straight forward."
        $ Map.bt5 = 2
        $ Map.bt6 = 1
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump belltower_map

    if _return == 'point 6':

        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.bt6 == 1:
            e 13 "This doesn’t look right at all."
            "Flo’s scent although faint seems to be coming from across the abyss."
            "You get as close as you can to the edge of the cliff and peer downwards."
            "All you can see is the broken remains of a city."
            e 1 "Is he somewhere down there? "
            "You turn towards the castle."
            e 13 "If he is, there has to be a way down from that castle."
            "You draw your sword and head into the castle grounds."
            $ Map.bt6 = 2
            $ Map.bt7 = 1
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            jump belltower_map
        elif True:
            "Flo’s scent although faint seems to be coming from across the abyss."
            e 13 "If he is, there has to be a way down from that castle."
            jump belltower_map

    if _return == 'point 7':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "You freeze at the sight of a pile of skulls and bones gathered into a pile."
        "Approaching the pile, the skulls are covered in a thick layer of dust and cobwebs."
        "The fur down your back stands on end and you turn towards the castle entrance."
        "Clutching your fists you will yourself to move forward. "
        $ Map.bt7 = 2
        $ Map.bt8 = 1
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump belltower_map

    if _return == 'point 8':
        if Map.bt8 == 1:
            $ Time.mins = Time.mins +10
            "You reach the entrance to the castle."
            "Taking a minute you observe the grand archway above you."
            "The sheer size of this building is overwhelming as though a looming presence is watching you."
            $ Map.bt8 = 2
            jump belltower_map
        elif Map.bt8 == 2:
            jump castle_map0
        elif True:
            jump belltower_map


screen belltower_map:
    imagemap:
        if Map.bt2 == 2:
            idle 'belltower_map1'
            hover 'belltower_map1'
        else:
            idle 'belltower_map'
            hover 'belltower_map'


        vbox:
            xalign 0.66 ypos 0.055
            imagebutton:
                idle "UI/up button1.png"
                hover "UI/up button2.png"

                action Return("exit")
        vbox:
            xalign 0.64 ypos 0.13
            if Map.bt1 ==1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 1")
            else:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"

        vbox:
            xalign 0.56 ypos 0.22
            if Map.bt2 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 2")
            elif Map.bt2 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.585 ypos 0.28
            if Map.bt3 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 3")
            elif Map.bt3 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.6 ypos 0.72
            if Map.bt4 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 4")
            elif Map.bt4 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.53 ypos 0.75
            if Map.bt5 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 5")
            elif Map.bt5 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.41 ypos 0.9
            if Map.bt6 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 6")
            elif Map.bt6 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 6")
            else:
                pass
        vbox:
            xalign 0.505 ypos 0.686
            if Map.bt7 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 7")
            elif Map.bt7 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.42 ypos 0.62
            if Map.bt8 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 8")
            elif Map.bt8 ==2:
                imagebutton:
                    idle "UI/left button1.png"
                    hover "UI/left button2.png"
                    action Return("point 8")
            else:
                pass

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
