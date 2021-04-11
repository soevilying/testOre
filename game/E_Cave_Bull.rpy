label battle_cave_bull:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 120
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    $ Map.good_battle = True
    $ Battle.holyfcd = 0
    stop Chan1
    stop Chan2
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    $ cave_slime_round = 0
    stop music
    scene caveruin 1n
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    jump battle_cave_bull_loop

label battle_cave_bull_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    if Map.ca8bull == 0:
        show bullw at center with dissolve
        play music "<loop 4.6903>music/forest_fight_small.ogg"
    elif True:
        show bullwghost at center with dissolve
        play music "<loop 12.6082>music/forest_fight_friend.ogg"




    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Holy Fist":
            $ red_damage = renpy.random.randint(Zalt.MATK*2, int((Zalt.MATK*2.5)+10))
            $ wolf_hp -= red_damage
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            $ Battle.holyfcd = 3
            $ Random = renpy.random.randint(1, 3)
            if wolf_hp <= 0:
                pass
            elif True:
                if Random == 1:
                    "You dart forward and land a punch on the enemy."
                elif Random == 2:
                    "You hit the enemy with your Holy Fist."
                elif True:
                    "With blazing speed you hit the foe with Holy Fist."
                " (Damage dealt - [red_damage]hp)"

        if res == "Items":
            $ Zalt.hp = min(Zalt.hp +5, Zalt.maxhp)
            $ cookies_left -= 1
            "*Drink* 5hp restored"

        if res == "Attack":
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-30), Zalt.ATK-5)
            $ Random = renpy.random.randint(0, 100)
            if Random >= Zalt.CRIT:
                $ wolf_hp -= red_damage
                if wolf_hp <= 0:
                    pass
                elif True:
                    "You draw your sword and lunge in for an attack.\n(Damage dealt- [red_damage]hp)"
            elif True:
                $ qty = red_damage*2
                $ wolf_hp -= red_damage*2
                if wolf_hp <= 0:
                    pass
                elif True:
                    "You draw your sword and lunge in for an attack.\n{b}{color=#ffd65c}(Critical damage! -[qty]hp){/color}"

        if res == "Submit":
            e "I can't fight anymore.."
            "The enemy is too strong."
            "You’re knocked onto the ground."
            jump battle_cave_bull_lose

        if res == "Bind up":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Bind up* [Zalt.heal]hp restored"
        if res == "Flirt":
            "Your attempts to seduce the enemy fails, the bull is too overcome with rage to even notice."

        if res == "Hp potion":
            $ Zalt.heal = 60
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ jane_inv.drop(hp_potion)
            "*Hp potion* [Zalt.heal]hp restored"
        if res == "Mp potion":
            $ Zalt.heal = 60
            $ Zalt.mp = min(Zalt.mp+Zalt.heal, Zalt.maxmp)
            $ jane_inv.drop(mp_potion)
            "*Mp potion* [Zalt.heal]mp restored"
        if res == "Escape":
            $ Random = renpy.random.randint(1, 2)
            if Random == 1:
                "You run away."
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item
                hide slime
                jump Cave_map
            elif True:
                "Escape failed!"
                pass
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_cave_bull_win
        $ Random = renpy.random.randint(1, 4)
        if Random == 1:
            $ Random = renpy.random.randint(1, 80)
            if Random <= Battle.dodge:
                "The bull swings his axe and it breaks a nearby boulder."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(30, 55)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The bull swings his axe and it breaks a nearby boulder, the pieces of rocks fly by and hit you in the gut."
        elif Random == 2:
            $ Random = renpy.random.randint(1, 80)
            if Random <= Battle.dodge:
                "The bull trys to grab you by the face."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(40, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The bull grabs you by the face."
                "You claw at his hand, forcing him to send you flying and hitting the wall behind."
        elif True:
            $ Random = renpy.random.randint(1, 80)
            if Random <= Battle.dodge:
                "The bull slams you against the wall with his shoulder."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(25, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The bull slams you against the wall with his shoulder."
        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_cave_bull_win
        elif True:

            jump battle_cave_bull_win

    elif Zalt.hp <= 0:
        "The enemy is too strong."
        "You’re knocked onto the ground."
        jump battle_cave_bull_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_cave_bull_lose
    elif True:
        jump battle_cave_bull_loop


label battle_cave_bull_win:

    $ Map.ca8bull = Map.ca8bull +1

    if Map.ca8bull != 2:
        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item
        stop music
        "The bull staggers back."
        show black2 with dissolve
        hide black2 with dissolve
        "Angry Bull Warrior" "You won’t take us again! You die demon!"
        e 9 "Holy crap!"
        show black2 with dissolve
        "The bull warrior’s entire form melts away like goo, revealing its skeletal frame."
        "You scream in terror and leap away."
        show bullwghost at center with vslow_dissolve
        "An ethereal form of itself then envelops the skeleton and the bull warrior reforms itself only now with a ghostly appearance."
        "The eyes of the other bulls glow a haunting blue and with their mouths open they release an ear piercing shriek."
        "You will yourself to continue fighting."
        "The bull might be a ghost but under that thing is a physical body you can hit!"
        hide black2 with dissolve
        $ wolf_hp = wolf_max_hp
        jump battle_cave_bull_loop
    elif True:
        play music "music/forest_fight_friend_end.ogg" noloop
        pause 1
        hide bullwghost with slow_dissolve
        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item
        "Ghost Bull Warrior" "Finally…"
        scene cave 1 with dissolve
        "The ghost bull warrior and his brethren fade into nothingness."
        "Their forms disintegrate into dust that fade into oblivion."
        show black2 with dissolve
        hide black2 with dissolve
        "Then in one bright flash of light you find yourself standing in front of a pile of bull skeletons."
        "Did any of that even happen?"
        "In the palm of your right hand you find some Ectoplasm."
        "{color=#19c22a}You get 4 Ectoplasm and 400 EXP.{/color}"
        e 13 "I better work quick, before Flo ends up like that."
        $ jane_inv_M.take(ectoplasm,4)
        $ Zalt.exp = min(Zalt.exp+400, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        $ Map.ca8 = 4

        scene cave 1 with dissolve
        $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
        $ PPEXP = 50*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump Cave_map


    return
label battle_cave_bull_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    hide bullw
    hide bullwghost
    stop music
    if Map.ca8bull == 0:
        "The bull knocks you to the ground and smashes your face in with the blunt end of his axe."
        scene black with dissolve
        "Everything fades to black."
        "You awaken back outside of the cave."
    elif True:
        "You didn’t see it coming, the ghost’s phantom axe swings low and hits you by the calves."
        "The cold blade cuts through you with ease forcing you to fall."
        e 0 "Wait, no!"
        "But it’s too late, the ghost bull is already standing over you and he brings down his axe right where your head is."
        scene black with dissolve
        "You awaken outside of the cave."

    $ Zalt.hp = 1
    $ Zalt.Dungeon_leave = True
    jump Cave_map
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
