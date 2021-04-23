label forest_map:
    hide screen f1_goods
    hide screen f2_goods
    hide screen f3_goods
    hide screen f4_goods
    hide screen f5_goods
    hide screen f6_goods
    window show None
    if renpy.variant("pc"):
        pass
    elif True:
        window hide None
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    stop music
    $ renpy.music.set_volume(0, 3, channel = "Thane")
    $ renpy.music.set_volume(0, 3, channel = "Axel")
    $ renpy.music.set_volume(0, 3, channel = "Snow")
    $ renpy.music.set_volume(0, 3, channel = "Witer")
    $ renpy.music.set_volume(0, 3, channel = "Chet")
    $ renpy.music.set_volume(0, 3, channel = "Hakan")
    $ renpy.music.set_volume(0, 3, channel = "Nauxus")
    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(1, 5, channel = "Chan1")
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_pause(False, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(1, 5, channel = "Chan2")
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(False, channel='Chan2')



    if Roushk.meet == 0 and (Axel.bullkid == 1 or Nauxus.artwork == 1) and Hakan.quest != 7 and Hakan.quest != 8 and Time.event1 != Time.days and Meko.meet >= 1:
        $ Roushk.meet = 1
        jump Roushk_meet
    call screen forest_map with dissolve
    if _return == 'forest_map_1':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        jump forest_map_1
        return
    if _return == 'forest_map_2':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        jump forest_map_2
        return
    if _return == 'forest_map_3':
        $ Time.mins = Time.mins +20
        play sound "music/foot1.ogg"
        play Thane "music/thane.ogg"
        jump forest_map_3
        return
    if _return == 'forest_map_4':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        jump forest_map_4
        return
    if _return == 'river_1':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        jump river_1
        return
    if _return == 'bulltribe_1':
        $ Time.mins = Time.mins +30
        stop Chan1 fadeout 5
        stop Chan2 fadeout 5
        play sound "music/foot1.ogg"
        jump bulltribe_1
        return
    if _return == 'forest_map_exit':
        if Time.hours >= 6 and Time.hours <= 17:
            scene forest 1 with dissolve
        elif True:
            scene forest 1n with dissolve
        play sound "music/foot1.ogg"
        e 1 "The exit is still foggy."
        e 1 "I can't leave now."
        jump forest_map
        return
    if _return == 'map1':
        $ Time.mins = Time.mins +20
        stop Chan1 fadeout 5
        stop Chan2 fadeout 5
        jump T_outdoor
        return
    if _return == 'crossroad':
        $ Time.mins = Time.mins +40
        jump crossroad
        return
    if _return == 'swamp':
        $ Time.hours = Time.hours +1
        play sound "music/foot1.ogg"
        play Nauxus "music/char_nauxus.ogg"
        jump swamp
        return
    if _return == 'lizardtribe':
        $ Time.mins = Time.mins +20
        $ Time.hours = Time.hours +1
        play sound "music/foot1.ogg"
        stop Chan1 fadeout 5
        stop Chan2 fadeout 5
        jump Lizard_tribe_map0
        return
    if _return == 'bullforest':
        $ Time.mins = Time.mins +20
        play sound "music/foot1.ogg"
        jump bullforest
        return
    if _return == 'lakebank':
        $ Time.mins = Time.mins +20
        play sound "music/foot1.ogg"
        jump lake_bank
        return
    if _return == 'deepswamp':
        $ Time.mins = Time.mins +20
        play sound "music/foot1.ogg"
        jump deepswamp
        return

    if _return == 'lakecabin':
        $ Time.mins = Time.mins +40
        play sound "music/foot1.ogg"
        scene black
        jump lakecabin
    if _return == 'cave_entrance':
        $ Time.mins = Time.mins +35
        play sound "music/foot1.ogg"
        scene black
        jump cave_entrance
label deadend:
    jump forest_map
label c_code:
    $ input_code = ""
    $ input_code = renpy.input("You find a magic Patreon cheat! What's the code?",length = 12,exclude = ".?!")


    if not input_code:
        $ input_code = ""

    if input_code.lower() == "winteriscomi":
        label c_code1:
            menu:
                "Get money" if True:
                    "You get 200 coins."
                    $ jane_inv.take(coin,200)
                    jump c_code1
                "Get Exp" if True:
                    menu:
                        "300EXP" if True:
                            "300EXP"
                            $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                        "500EXP" if True:
                            "500EXP"
                            $ Zalt.exp = min(Zalt.exp+500, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                        "1000EXP" if True:
                            "1000EXP"
                            $ Zalt.exp = min(Zalt.exp+1000, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                    jump c_code1
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

                    jump c_code1
                "Unlock gallery" if True:
                    "All gallery unlocked!"
                    $ persistent.CG_lizard_lose = True
                    $ persistent.CG_goo_lose = True
                    $ persistent.CG_bull_lose = True
                    $ persistent.CG_bull_winA = True
                    $ persistent.CG_bull_winB = True
                    $ persistent.CG_tree_lose = True
                    $ persistent.CG_witer_bj = True
                    $ persistent.CG_ghost_lose = True
                    $ persistent.CG_gargoyle_lose = True
                    $ persistent.CG_gargoyle_win = True
                    $ persistent.CG_hakan_ride = True
                    $ persistent.CG_bull_lick = True
                    $ persistent.CG_lizard_win = True
                    $ persistent.CG_roushk_top = True
                    $ persistent.CG_roushk_bottom = True
                    $ persistent.CG_eyvind_sell = True
                    $ persistent.CG_hakan_sixnine = True
                    $ persistent.CG_witer_cowboy = True
                    jump c_code1
                "Уйти" if True:
                    $ input_code = ""
                    jump map1
    elif True:
        "Nope."
    $ input_code = ""
    jump map1

label forest_map0:
    stop music

    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(1, 5, channel = "Chan1")
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(1, 5, channel = "Chan2")
    play Chan1[ "<silence 0.5>", "music/forest_day.ogg" ]fadein 3
    play Chan2[ "<silence 0.5>", "music/forest_night.ogg" ]fadein 3

    $ config.rollback_enabled = True
    jump forest_map

screen forest_map:

    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'forest_map'
            hover 'forest_map1'
        else:
            idle 'forest_mapn'
            hover 'forest_mapn1'
        hotspot (1054, 216, 135, 101) action Return("map1")

        vbox:
            xalign 0.45 ypos 0.35
            imagebutton:
                idle "UI/button1.png"
                hover "UI/button2.png"

                action Return("forest_map_1")
        vbox:
            xalign 0.42 ypos 0.30
            if Snow.meet == True:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("forest_map_2")
            else:
                pass

        vbox:
            xalign 0.62 ypos 0.18
            imagebutton:
                idle "UI/button1.png"
                hover "UI/button2.png"

                action Return("forest_map_exit")
        vbox:
            xalign 0.62 ypos 0.3
            if Snow.hunt == False:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("river_1")
            else:
                pass
        vbox:
            xalign 0.68 ypos 0.45
            if Map.forest3 >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("forest_map_3")
            else:
                pass
        vbox:
            xalign 0.77 ypos 0.43
            if Map.bulltribe >= 1:
                imagebutton:
                    if Time.hours >= 6 and Time.hours <= 17:
                        idle "UI/tribe1.png"
                        hover "UI/tribe2.png"
                    else:
                        idle "UI/tribe1n.png"
                        hover "UI/tribe2n.png"


                    action Return("bulltribe_1")
            else:
                pass
        vbox:
            xalign 0.32 ypos 0.27
            if Hakan.quest >= 4:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("forest_map_4")
            else:
                pass
        vbox:
            xalign 0.32 ypos 0.5
            if Map.swamp >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("swamp")
            else:
                pass
        vbox:
            xalign 0.45 ypos 0.55
            if Snow.hunt == False:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("crossroad")
            else:
                pass
        vbox:
            xalign 0.55 ypos 0.64
            if Map.lakebank == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("lakebank")
            else:
                pass
        vbox:
            xalign 0.2 ypos 0.4
            if Map.lizard >= 1:
                imagebutton:
                    if Time.hours >= 6 and Time.hours <= 17:
                        idle "UI/tribe3.png"
                        hover "UI/tribe4.png"
                    else:
                        idle "UI/tribe3n.png"
                        hover "UI/tribe4n.png"



                    action Return("lizardtribe")
            else:
                pass
        vbox:
            xalign 0.77 ypos 0.61
            if Map.bullforest >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("bullforest")
            else:
                pass
        vbox:
            xalign 0.16 ypos 0.41
            if Map.deepswamp >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("deepswamp")
            else:
                pass
        vbox:
            xalign 0.61 ypos 0.7
            if Map.lakecabin >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"

                    action Return("lakecabin")
            else:
                pass
        vbox:
            xalign 0.65 ypos 0.6
            if Map.cave >= 1:
                imagebutton:
                    idle "UI/down button1.png"
                    hover "UI/down button2.png"

                    action Return("cave_entrance")
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
