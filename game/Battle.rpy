define RR = Character('Red Hood', color="#CD0000")
define TT = Character('mr.Wolf', color="#B5B5B5")

screen simple_stats_screen:
    frame:
        xalign 0.02 yalign 0.95
        xminimum 220 xmaximum 220
        has vbox
        text "[name]" size 22 xalign 0.5
        null height 5
        text "HP" size 16
        hbox:
            bar:
                xmaximum 130
                value Zalt.hp
                range Zalt.maxhp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None

            null width 5


            text "[Zalt.hp] / [Zalt.maxhp]" size 16
        text "MP" size 16
        hbox:

            bar:
                xmaximum 130
                value Zalt.mp
                range Zalt.maxmp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None


            null width 5


            text " {color=#0080c0}[Zalt.mp] / [Zalt.maxmp]{/color}" size 16
        text "LUST" size 16
        hbox:

            bar:
                xmaximum 130
                value Zalt.lust
                range Zalt.maxlust
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None


            null width 5


            text "[Zalt.lust] / [Zalt.maxlust]" size 16


    frame:
        xalign 0.5 yalign 0.01
        xminimum 250 xmaximum 250
        has vbox
        hbox:
            text "HP" size 28 xalign 0.5
            null height 5
            bar:
                xmaximum 130
                value wolf_hp
                range wolf_max_hp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None

            null width 5

            text "[wolf_hp] / [wolf_max_hp]" size 16
        hbox:
            if Battle.flirt == True:
                text "LUST" size 14 xalign 0.5
                null height 5
                bar:
                    xmaximum 130
                    value wolf_lust
                    range wolf_max_lust
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[wolf_lust] / [wolf_max_lust]" size 16
            else:
                pass


screen battle_menu:
    vbox:
        xalign 0.3 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Submit" action Return("Submit") yminimum 40
                else:
                    textbutton "Submit" action None yminimum 40
    vbox:
        xalign 0.4 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Skill" action Show("battle_skill") yminimum 40
                else:
                    textbutton "Skill" action None yminimum 40
    vbox:
        xalign 0.5 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Attack" action Return("Attack") yminimum 40
                else:
                    textbutton "Attack" action None yminimum 40
    vbox:
        xalign 0.6 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Items" action Show("battle_item") yminimum 40
                else:
                    textbutton "Items" action None yminimum 40
    vbox:
        xalign 0.7 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Escape" action Return("Escape") yminimum 40
                else:
                    textbutton "Escape" action None yminimum 40




screen battle_skill:
    vbox:
        xalign 0.4 ypos 0.7
        frame:
            textbutton "Skill" action Hide("battle_skill") yminimum 40
    vbox:
        xalign 0.4 ypos 0.6
        hbox:
            frame:
                if players_turn and Zalt.mp>=20:
                    textbutton "Bind up" action Return("Bind up") yminimum 40
                else:
                    textbutton "Bind up" action None yminimum 40
            frame:
                if Battle.holyfcd == 0:
                    if players_turn and Zalt.mp>=20 and Battle.holyf == True:
                        textbutton "Holy Fist" action Return("Holy Fist") yminimum 40
                    elif players_turn and Zalt.mp<20 and Battle.holyf == True:
                        textbutton "Holy Fist" action None yminimum 40
                    else:
                        textbutton "-" action None yminimum 40
                else:
                    if players_turn and Zalt.mp>=20 and Battle.holyf == True:
                        textbutton "Holy Fist(2CD)" action None yminimum 40
                    elif players_turn and Zalt.mp<20 and Battle.holyf == True:
                        textbutton "Holy Fist(2CD)" action None yminimum 40
                    else:
                        textbutton "-" action None yminimum 40
            frame:
                if players_turn and Battle.flirt == True:
                    textbutton "Flirt" action Return("Flirt") yminimum 40
                else:
                    textbutton "-" action None yminimum 40

screen battle_item:
    vbox:
        xalign 0.6 ypos 0.7
        frame:
            textbutton "Items" action Hide("battle_item") yminimum 40
    vbox:
        xalign 0.6 ypos 0.6
        hbox:

            frame:
                if players_turn and jane_inv.qty(hp_potion) >= 1:
                    textbutton "Hp potion" action Return("Hp potion") yminimum 40
                else:
                    textbutton "-" action None yminimum 40
            frame:
                if players_turn and jane_inv.qty(mp_potion) >= 1:
                    textbutton "Mp potion" action Return("Mp potion") yminimum 40
                else:
                    textbutton "-" action None yminimum 40
label battle_game_1:

    $ wolf_max_hp = 400
    $ wolf_hp = wolf_max_hp
    $ players_turn = False


    $ Battle.holyfcd = 0

    scene forest light
    $ renpy.music.set_volume(0.2, 0, channel = "music")

    play music"music/rainy.mp3"
    stop Chan1 fadeout 5
    stop Chan2 fadeout 10
    stop Chan3 fadeout 5
    "It’s difficult to see outside the tavern, everything is blanketed by grey fog."
    "Your only source of light is the moon and the glow of the tavern."
    play sound"music/snap.mp3"
    "Snap!"
    "Your ears pick up the sound of twigs breaking."
    play sound"music/foot2.ogg"
    "Something is moving about in front of you."
    e 5 "Who’s there?"
    "No answer."
    "You draw your sword and inch closer and closer towards the forest."
    "The air is suddenly silent, but you can feel a presence looking at you."
    "Something bursts out of the trees."
    play sound"music/roar.ogg"
    show skull at center with fade
    "A hulking black figure with a skull for a head."
    "It roars at you."
    "The monster raises its massive hand and slams it hard to the ground. "
    "You manage to jump back in time and ready a fighting stance. "
    "It does not look happy that it missed."
    "Here it comes."
    hide skull
    $ renpy.music.set_volume(1, 0.5, channel = "music")
    jump battle_1_loop


label battle_1_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show skull at center
    play music "<loop 12.4405>music/forest_fight_strong2.ogg"





    while (wolf_hp > 0) and (Zalt.hp > 0):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Holy Fist":
            $ red_damage = renpy.random.randint(Zalt.MATK*2, int((Zalt.MATK*2.5)+10))
            $ wolf_hp -= red_damage
            $ Zalt.mp = min(Zalt.mp -30, Zalt.maxmp)
            $ Battle.holyfcd = 3
            " (Damage dealt wip - [red_damage]hp)"

        if res == "Items":
            $ Zalt.hp = min(Zalt.hp +5, Zalt.maxhp)
            $ cookies_left -= 1
            "*Drink* 5hp restored"

        if res == "Attack":
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-20), Zalt.ATK)
            $ Random = renpy.random.randint(0, 100)
            if Random >= Zalt.CRIT:
                $ wolf_hp -= red_damage
                "You draw your sword and lunge in for an attack.\n(Damage dealt- [red_damage]hp)"
            elif True:
                $ qty = red_damage*2
                $ wolf_hp -= red_damage*2
                "You draw your sword and lunge in for an attack.\n{b}{color=#ffd65c}(Critical damage! -[qty]hp){/color}"


        if res == "Submit":
            "I can't fight anymore.."
            jump battle_1_lose

        if res == "Bind up":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Bind up* [Zalt.heal]hp restored"
        if res == "Escape":
            $ Random = renpy.random.randint(1, 3)
            if Random == 1:
                "Escape failed!"
                pass
            elif Random == 2:
                "Escape failed!"
                pass
            elif True:
                "Escape failed!"
                pass
        elif True:
            pass

        $ Random = renpy.random.randint(1, 100)
        if Random <= Battle.dodge:
            "???" "RrrrrRRrrrr! {i}*The monster hits you*{/i}"
            "But you dodged his attack!"
        elif True:
            $ wolf_damage = renpy.random.randint(15, 20)
            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
            "???" "RrrrrRRrrrr! {i}*The monster hits you*{/i}"
        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_1_lose
        elif True:

            "???" "RrrrrRRrrrr!"
            jump battle_1_win

    elif Zalt.hp <= 0:
        jump battle_1_lose
    elif True:

        jump battle_1_loop


label battle_1_win:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    play music "music/forest_fight_boss_end.ogg" noloop
    "The skull demon buckles and stumbles backwards. {p}It roars and flees into the forest."
    "It seems he dropped something"
    e 1 "What's this?"
    "You get 300 coins"
    "You feel empowered from taking down an enemy that was almost impossible to defeat."
    "{b}{color=#19c22a}<[name] gains 5 lv-points!>{/color}"
    $ Zalt.points = Zalt.points +5
    $ jane_inv.take(coin,300)
    $ Zalt.tut_win = True
    jump map0

    return
label battle_1_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    e 5 " He’s too strong… what is this power?"
    "A figure rushes pass you, it’s Snow!"
    "He wields a sword like yours and jumps at the monster."
    "His strike lands and cuts the demon across the chest. "
    "The skull demon buckles and stumbles backwards. {p}It roars and flees into the forest."
    s "Come on kid, it’s over."
    $ Zalt.tut_win = False
    jump map0
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
