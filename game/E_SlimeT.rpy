label battle_slimeT:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    if Time.hours >= 6 and Time.hours <= 17:
        scene forest 3 with slow_dissolve
    elif True:
        scene forest 3n with slow_dissolve

    $ wolf_max_hp = 50
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ Battle.holyfcd = 0
    $ Map.good_battle = True
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    stop music







    "???" "Aaaaah! Someone help!"
    "Your head turns to the source of the cry."
    "It’s coming from somewhere to the left of the path."
    "Without hesitation you run towards the screaming voice."
    "???" "Help! I can’t move! Help!"
    "You hack and rip through branches with your bare hands until you reach a tall tree bearing bright red fruits on its branches."
    "The voice is coming from behind the tree."
    "You rush over to the other side with your sword drawn."
    "It’s a bull, and he has a bruised leg. Two slimes are climbing his body as you approach."
    "You swing your blade careful to not hit the bull, sending both slimes flying to the side."
    "Their gelatinous bodies reform and one of them lunges at you!"
    jump battle_slime_loopT


label battle_slime_loopT:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show slime at center
    play music "<loop 4.6903>music/forest_fight_small.ogg"





    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False

        if res == "Holy Fist":
            $ red_damage = renpy.random.randint(Zalt.MATK*2, int((Zalt.MATK*2.5)+10))
            $ wolf_hp -= red_damage
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
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
            jump battle_slime_lose2
        if res == "Flirt":
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
                "You can't escape! That bull needs your help!"
                pass
            elif True:
                "You can't escape! That bull needs your help!"
                pass
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_slime_winT
        $ Random = renpy.random.randint(1, 3)
        if Random <= 1:
            $ wolf_damage = renpy.random.randint(3, 5)
            $ Zalt.lust += wolf_damage
            "Slime's mucus is splattered all over you."
            "You feel something hot from your crotch."
            "[name]" "There seems to be something toxic in this mucus..."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Slime" "RrrrrRRrrrr! {i}*The monster hits you*{/i}"
                "But you dodged its attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(5, 15)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Slime" "RrrrrRRrrrr! {i}*The monster hits you*{/i}"
        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_slime_winT
        elif True:

            "Slime" "RrrrrRRrrrr!"
            jump battle_slime_winT

    elif Zalt.hp <= 0:
        "The enemy is too strong."
        "You’re knocked onto the ground."
        jump battle_slime_loseT
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_slime_loseT
    elif True:
        jump battle_slime_loopT


label battle_slime_winT:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_small_end.ogg" noloop
    pause 1
    hide slime with slow_dissolve
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    "Slime crumpled on the floor."
    "You pick up some of the glue."
    "You get a Slime Jewel and 30 exp."
    $ Zalt.exp = min(Zalt.exp+30, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    $ jane_inv_M.take(slime_jewel)
    $ Foe.slimet = Foe.slimet+1
    if Foe.slimet <=1:
        "Another slime attack!"
        $ wolf_hp = wolf_max_hp
        jump battle_slime_loopT
    elif True:
        $ Foe.slimet = 3
        jump Thane_meet

    return
label battle_slime_loseT:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music
    scene black with dissolve
    "Bull" "...No..! Aghhhhh!!"
    "......"
    scene forest 3 with dissolve
    "When you wake up again, you find that some coins is missing."
    "The cow and slime are gone."
    "You have a feeling that you will never see him again."
    e 13 "...."
    if jane_inv.qty(coin) != None:
        $ qty = int(jane_inv.qty(coin)*0.2)
        $ jane_inv.drop(coin,qty)
    $ Zalt.lust = 0
    $ Zalt.hp = 1
    $ Thane.meet = -1
    jump forest_map_3
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
