label Room1_check:
    scene tavern 1
    if Items.key1==False:
        play sound "music/door.mp3"
        jump Room1
    elif True:
        play sound "music/door.mp3"
        jump Room1


label Room1:
    if Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bombt == 6 and Quest.fes_end == -1:
        $ Quest.fes_end = 0
        $ Time.festival_day = Time.days
    $ renpy.music.set_volume(0.3, 1, channel = "music")
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    $ Zalt.public = False
    scene room 1
    if Map.yourroom == 0:
        "This is your room."
        "Whenever you rest in your bed you can spend the experience points you gain to level up."
        "As you level up you gain lvl-points which you can spend to raise HP/MP or ability levels."
        "Spend them wisely, and good night."
        $ Map.yourroom = 1

    call screen Room1
    window hide None
    window show None
    if _return == 'stat-points':
        "You can use {color=#19c22a}5 {/color} lv-points to increase one stat point you want."
        "Or you can also use {color=#19c22a}3 {/color} lv-points to increase 10 HP and 10 MP."
        "You have {color=#19c22a}[Zalt.points]{/color} lv-point now."
        menu:
            "Get 10 MaxHP+10 MaxMP" if Zalt.points >= 3:
                $ Zalt.points = Zalt.points -3
                $ Zalt.maxhp = Zalt.maxhp +10
                $ Zalt.maxmp = Zalt.maxmp +10
                jump Room1
            "Get stat point" if Zalt.points >= 5:
                menu:
                    "Strength" if Zalt.str <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.str = Zalt.str +1
                        $ Zalt.ATK = Zalt.ATK +3
                        "Your {color=#19c22a}STR{/color} now increase to {b}{color=#19c22a}[Zalt.str]{/color}."
                        jump Room1
                    "Agile" if Zalt.agi <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.agi = Zalt.agi +1
                        $ Zalt.ATK = Zalt.ATK +1
                        $ Zalt.CRIT = Zalt.CRIT +2
                        $ Battle.dodge = Battle.dodge +2
                        "Your {color=#19c22a}Agi{/color} now increase to {b}{color=#19c22a}[Zalt.agi]{/color}."
                        jump Room1
                    "Intelligence" if Zalt.int <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.int = Zalt.int +1
                        $ Zalt.maxmp = Zalt.maxmp +10
                        $ Zalt.MATK = Zalt.MATK + 3
                        "Your {color=#19c22a}INT{/color} now increase to {b}{color=#19c22a}[Zalt.int]{/color}."
                        "Your {color=#19c22a}MaxMp{/color} now increase to {b}{color=#19c22a}[Zalt.maxmp]{/color}."
                        jump Room1
                    "Endurance" if Zalt.end <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.end = Zalt.end +1
                        $ Zalt.maxhp = Zalt.maxhp +20
                        "Your {color=#19c22a}END{/color} now increase to {b}{color=#19c22a}[Zalt.end]{/color}."
                        "Your {color=#19c22a}MaxHp{/color} now increase to {b}{color=#19c22a}[Zalt.maxhp]{/color}."
                        jump Room1
                    "Charm" if Zalt.cha <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.cha = Zalt.cha +1
                        "Your {color=#19c22a}CHA{/color} now increase to {b}{color=#19c22a}[Zalt.cha]{/color}."
                        jump Room1
                    "Leave" if True:
                        jump Room1
            "Exchange 3 AP to 1 lv-point" if Zalt.AP >= 3:
                "{b}{color=#19c22a}You get 1 lv-point.{/color}."
                $ Zalt.AP = Zalt.AP -3
                $ Zalt.points = Zalt.points +1
                jump Room1
            "Leave" if True:
                jump Room1

    if _return == 'outroom':
        if Items.nude == False:
            jump map1
        elif True:
            scene black
            e 7 "....No,I don't think it's a good idea to being nude in public."
            jump Room1
    if _return == 'Rest':
        menu:
            "Rest" if True:
                scene black
                "You sleep for 3 hours, feel refreshed and full of energy."
                "HP and MP have been restored half of the maximum."
                $ Zalt.hp = min(Zalt.hp+Zalt.maxhp/2, Zalt.maxhp)
                $ Zalt.mp = min(Zalt.mp+Zalt.maxmp/2, Zalt.maxmp)
                $ Time.hours = Time.hours+3

                jump Room1
            "Rest until evening" if Time.hours >= 6 and Time.hours <15:
                scene black
                "You sleep until evening, feel refreshed and full of energy."
                "HP and MP have been restored to maximum."
                $ Zalt.hp = Zalt.maxhp
                $ Zalt.mp = Zalt.maxmp

                $ Time.hours = 18
                $ Time.mins = 0

                jump Room1

            "Sleep" if Time.hours < 6 or Time.hours >=21:
                scene black
                if NPC.weird_dream == 0 and Items.em >= 2:
                    $ NPC.weird_dream = 1
                    jump Room1_dream
                "You sleep until morning, feel refreshed and full of energy."
                "HP and MP have been restored to maximum."
                $ Zalt.hp = Zalt.maxhp
                $ Zalt.mp = Zalt.maxmp
                if Time.hours >=21:
                    $ Time.days = Time.days+1
                    $ Time.hours = 6
                    $ Time.mins = 30
                elif True:
                    $ Time.hours = 6
                    $ Time.mins = 30

                jump Room1
            "Level up" if Zalt.exp >= Zalt.maxexp and Zalt.lv < Zalt.maxlv:
                $ Zalt.exp = Zalt.exp - Zalt.maxexp
                $ Zalt.maxexp = Zalt.lv*250+100*(Zalt.lv-1)
                $ Zalt.lv = Zalt.lv+1
                $ Zalt.points = Zalt.points+1
                $ Zalt.points1 = Zalt.points1+1
                "After taking a short break to reflect on your battles, you feel stronger."
                "{b}{color=#19c22a}[name]'s level increases to [Zalt.lv].{/color}"
                $ Random = renpy.random.randint(1, 2)
                if Random == 2:
                    "{b}{color=#19c22a}[name]'s Hp increase 5 points.{/color}"
                    $ Zalt.maxhp = Zalt.maxhp +5
                elif True:
                    "{b}{color=#19c22a}[name]'s Mp increase 5 points.{/color}"
                    $ Zalt.maxmp = Zalt.maxmp +5
                "{b}{color=#19c22a}[name]'s ATK increase 2 points.{/color}"
                "{b}{color=#19c22a}[name]'s MATK increase 1 points.{/color}"

                $ Zalt.ATK = Zalt.ATK +2
                $ Zalt.MATK = Zalt.MATK +1


                jump Room1
            "Leave" if True:
                jump Room1

    if _return == 'eyvind_solo':
        scene room 1
        if persistent.CG_eyvind_solo:
            "Do you want to skip the scene?"
            menu:
                "Yes" if True:
                    "Slowly, you drift off to sleep."
                    $ Zalt.lust = 0
                    $ Time.mins = Time.mins+15
                    jump Room1
                "No" if True:
                    pass
        "A strong wave of heat washes over your body."
        "You place a hand over your chest and you feel your heart beating like a storm."
        e 11 "Ugh, I can’t... I can’t hold it in anymore."
        "From just placing your hand over your chest,{p}you start to massage your pecs."
        "You shudder and gasp from the touch.{p}Your loins feel heavy and tighten against your loincloth."
        "You tear away your loincloth exposing your throbbing dick.{p}With your cock in your hand you fall onto your bed."
        "You pant loudly while your hand rubs along your hot shaft."
        "This isn’t the first time you’ve jerked off, but you’ve never felt so horny in so long."
        "Your balls... your balls feels so full."
        "You grab the orbs dangling between your thighs and give them a good squeeze."
        e 11 "Hngh..."
        "Your thumb caresses the tip of your cock, smearing it with hot translucent pre. Perfect for lube."
        "You smear the pre along your cock while steadily jerking your cock."
        "A soft gasp escape your mouth."
        "Your whole body tenses as your dick pulsates from every rub."
        "Your right leg shakes and twitches a bit."
        "Gritting your teeth you pump your cock even faster."
        "You feel the pressure building inside your dick."
        e 4 "Fuck!"
        "Beads of sweat form around your forehead and your body is mind numbingly warm."
        "You pant louder and louder until..."
        "Your cock fires a hot wad of cum right onto your face."
        "Your cumshots splatter around your pecs and stomach."
        "When you finally stop cumming your body sinks into the bed."
        "The afterglow blankets you filling you with sweet warmth."
        "Slowly, you drift off to sleep."
        $ persistent.CG_eyvind_solo = True
        $ Zalt.lust = 0
        $ Time.mins = Time.mins+15
        jump Room1

        return


label Room1_dream:
    "You’re sitting in front of a dining table with a rich buffet of food and drinks spread out in front of you."
    "The insides of your mouth is wet with saliva."
    "You aren’t sure where to begin."
    "Then, the scene flashes white."
    "Now you have a half eaten pancake in front of you."
    "???" "How are you enjoying the food?"
    e 0 "It’s all good. I’ve never had so much good food before."
    "The pancake is extra fluffy and tastes great with the honey on top of it."
    "There’s an odd aftertaste, something almost fruity, but you didn’t mind it."
    "???" "I’m glad to hear that."
    "???" "Please eat as much as you like, I’ll make sure you are well taken care of."
    "Dark tendrils form in the corner of your eyes."
    e 0 "What? What’s going on?"
    "Then darkness takes you."
    play music [ "<silence 1.0>", "music/castle.ogg" ] fadeout 1
    scene prison 3 with slow_dissolve
    "You awaken staring at the ceiling."
    "Your vision is hazy, and no matter how hard you struggle you cannot move your limbs."
    "Moving your head up you can see your hands and legs are tied to a stone tablet."
    e 0 "Help! Someone please, help!"
    "The light on the ceiling swirls and breaks off into four torches held by cloaked figures."
    "Bright yellow eyes then peer out from the darkness of the figure’s cloaks."
    "Terror strikes your heart, you don’t know who these figures are, or what they want."
    e 0 "Let me go! Let me go!"
    "They won’t stop looking at you."
    e 0 "No! Stay back! Stay back!"
    e 0 "Someone please help!"
    "Their faces keep getting closer, and closer, until-"
    stop music fadeout 1
    scene room 1 with slow_dissolve
    e 9 "NO!" with vpunch
    "You awaken upright with cold sweat drenched throughout your body."
    e 13 "Nothing, thank goodness."
    e 9 "That dream... that was insane."
    "Every detail of that dream is etched into your memory."
    "The tightness of the ropes on your wrists, the coldness of the stone slab you were laid on, even the taste of the pancake in your mouth."
    e 13 "Either I’m really stressed out or that dream was no ordinary dream."
    "You stand up from the bed and get dressed."
    "Choosing to not think too much about one bad dream."
    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
    $ Zalt.hp = Zalt.maxhp
    $ Zalt.mp = Zalt.maxmp
    if Time.hours >=21:
        $ Time.days = Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
    elif True:
        $ Time.hours = 6
        $ Time.mins = 30

    jump Room1
screen Room1:

    imagemap:
        idle 'room 1'
        hover 'room 1hover'


    frame:
        xalign 0.81 ypos 0.84
        imagebutton:
            idle "UI/outdoor01.png"
            hover "UI/outdoor02.png"

            action Return("outroom")
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
    frame:
        xalign 0.89 ypos 0.72
        imagebutton:
            idle "UI/sleep01.png"
            hover "UI/sleep02.png"

            action Return("Rest")
    if Zalt.lust >= 40:
        frame:
            xalign 0.97 ypos 0.60
            imagebutton:
                idle "UI/love01.png"
                hover "UI/love02.png"

                action Return("eyvind_solo")
    if Zalt.points >= 1 or Zalt.AP != 0:
        frame:
            xalign 0.97 ypos 0.72
            imagebutton:
                idle "UI/lv01.png"
                hover "UI/lv02.png"

                action Return("stat-points")

    else:
        pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
