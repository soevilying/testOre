label battle_bullAB:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 120
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 20

    $ Map.good_battle = True
    $ Battle.holyfcd = 0
    stop music
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    jump battle_bullAB_loop


label battle_bullAB_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show bullw at center
    play music "<loop 4.6903>music/forest_fight_small.ogg"





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
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-20), Zalt.ATK)
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
            jump battle_bullAB_lose
        if res == "Flirt":
            $ Random = renpy.random.randint(1, 4)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You strike a series of poses with a confident smile."
                "The enemy is intrigued by your movements."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You tease your opponent by attacking them head on."
                "Rubbing them sensually on their nipples, crotch, and lightly fingering their backsides."
                "Your opponent is panting heavily, clutching his obvious erection."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You rub your crotch sensually, letting your cock chub up a bit before flashing your dickhead at the enemy."
                "Lust fills your opponent, he is immobilized by powerful desire for your cock."
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You strike a series of poses with a confident smile."
                    "The enemy catches you by surprise and throws you back. You barely land on your feet."
                elif Random == 2:
                    "You tease your opponent by attacking them head on."
                    "Rubbing them sensually on their nipples, crotch, and lightly fingering their backsides."
                    "The enemy ignores your attempts to seduce him."
                elif True:
                    "You rub your crotch sensually, letting your cock chub up a bit before flashing your dickhead at the enemy."
                    "The enemy is enraged by your actions."
            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                "The bull falls to his knees, his hard cock throbs and leaks pre all over the battlefield."
                jump battle_bullAB_win
            elif True:
                pass
        if res == "Bind up":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Bind up* [Zalt.heal]hp restored"
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
                $ Foe.bullab = 3
                hide bullw
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item
                hide slime
                jump forest_map0
            elif True:
                "Escape failed!"
                pass
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_bullAB_win
        $ Random = renpy.random.randint(1, 6)
        if Random <= 2:
            $ wolf_damage = renpy.random.randint(15, 30)
            $ Zalt.lust += wolf_damage
            "The bull warrior's musk is earthy and potent."
            "Your crotch warms up."
            "Bull warrior" "You like that, hmmm? Submit now and I'll give you something fun!"
        elif True:
            $ Random = renpy.random.randint(1, 80)
            if Random <= Battle.dodge:
                "Bull warrior" "RrrrrRRrrrr! {i}*The monster hits you*{/i}"
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(30, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Bull warrior" "RrrrrRRrrrr! {i}*The monster hits you*{/i}"

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_bullAB_win
        elif True:

            jump battle_bullAB_win

    elif Zalt.hp <= 0:
        "The enemy bull’s fist slams hard onto your gut."
        "Your body spasms for a second and you are left wobbling on your feet."
        jump battle_bullAB_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_bullAB_lose
    elif True:
        jump battle_bullAB_loop


label battle_bullAB_win:


    $ Foe.bullab = Foe.bullab+1
    if Foe.bullab <=1:
        stop music fadeout 3
        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item
        "Bull warrior" "Egh..!"
        hide bullw with dissolve

        "Bull B" "How can you...!"
        "Another bull attack!"
        jump battle_bullAB
    elif True:
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
        play music "music/forest_fight_small_end.ogg" noloop
        pause 1
        hide bullw with slow_dissolve

        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item
        "Bull A" "Rargh! How dare you! We’ll remember this."
        "Bull B" "We let you win this time."
        "Bull A" "You won’t be able to take all of us down when we get the rest of our brothers."
        e 9 "Oh boy, two I can handle, but a whole tribe? Don’t want to push my luck."
        "You feel empowered from taking down two strong foes."
        "{b}{color=#19c22a}<[name] gains 1 lv-points!>{/color}"
        $ Zalt.points = Zalt.points +1
        "You run back the way you came from."
        $ Foe.bullab = 3
        jump forest_map0
    return
label battle_bullAB_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    hide bullw with dissolve
    "The bull grabs you by the neck and tosses you towards the ground like a rag doll."
    "You manage to pull yourself back up, but all the strength has been sapped from your body."
    "You make a run for it back to the path you came from."
    $ Foe.bullab = 3
    $ Zalt.hp = 1
    jump forest_map0
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
