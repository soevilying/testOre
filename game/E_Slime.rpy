label battle_slime:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
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







    "Your follow your nose, lead by the scent of some creature deep in the forest."
    "Pushing through branches and shrub you hear something rustling nearby."
    "A slime lunges at you!"
    jump battle_slime_loop


label battle_slime_loop:



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
            jump battle_slime_lose

        if res == "Bind up":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Bind up* [Zalt.heal]hp restored"
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
                jump forest_map
            elif True:
                "Escape failed!"
                pass
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_slime_win
        $ Random = renpy.random.randint(1, 3)
        if Random <= 1:
            $ wolf_damage = renpy.random.randint(10, 20)
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
                $ wolf_damage = renpy.random.randint(10, 20)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Slime" "RrrrrRRrrrr! {i}*The monster hits you*{/i}"
        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_slime_win
        elif True:

            "Slime" "RrrrrRRrrrr!"
            jump battle_slime_win

    elif Zalt.hp <= 0:
        "The enemy is too strong."
        "You’re knocked onto the ground."
        jump battle_slime_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_slime_lose
    elif True:
        jump battle_slime_loop


label battle_slime_win:
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
    jump forest_map_1

    return
label battle_slime_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    scene black
    stop music
    if Foe.slime == True:
        "Do you want to skip the scene?"
        menu:
            "Yes" if True:
                scene black with dissolve
                "......"
                scene forest 1 with dissolve
                "When you wake up again, you find that some coins is missing."
                "You smile grimly, glad that you're still alive."
                "After cleaning yourself up, you start over again."
                $ Zalt.cor = min(Zalt.cor+1,100)
                if jane_inv.qty(coin) != None:
                    $ qty = int(jane_inv.qty(coin)*0.2)
                    $ jane_inv.drop(coin,qty)
                $ Zalt.lust = 0
                $ Zalt.hp = 1
                jump forest_map_1
            "No" if True:
                pass
    "Your weapon is too far away for you to reach."
    "There’s a strong aura coming from the approaching enemy slime."
    "Digging deep into the dirt you try to pull yourself away from the slime."
    "But your body is too battered to pull you far."
    show slime lose1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos 0 ypos 0
        linear 10.0 xpos -50 ypos -800
    "It taunts you by moving slowly as though it knows you are afraid, but you cannot escape."
    "To your horror its slimy body grabs you by the foot."
    "Somehow, the slime’s movements opens up your loincloth."
    show slime lose1 with slow_dissolve:
        xpos 0.15 ypos -0.05
        zoom 0.65
    "Your privates are exposed and covered in the slime’s gooey body. "
    e "Gragh! Get off! Get off!"
    show slime lose2 with slow_dissolve:
        xpos 0.15 ypos -0.05
        zoom 0.65
    "The texture of the goo, it feels so weird on your body."
    "like someone wrapping your leg in a warm and moist blanket."
    "Arms of slime extend from the slime’s main body."
    "It sticks your hands to the ground."
    "You are unable to break free from its grip."
    "The creature makes its way up your thigh and covers itself around your crotch."
    e "Ah...ahhh...ahh!"
    "This sensation is just too much."
    "You’ve never been touched like this before."
    "The creature begins to jiggle and shake."
    "Everytime it moves it feels like it is tightening its grip around your throbbing cock."
    "Your entire body is heating up."
    "You need to resist the creature’s hold on you but it just feels so good."
    "A hot sensation forms around your butthole, and you scream."
    e "No! Not there!"
    with flashbulb
    show slime lose3 with dissolve:
        xpos 0.15 ypos -0.05
        zoom 0.65
    "The slime forces its way inside your ass."
    "A rush of heat tickles your prostate."
    "Your mind is trapped between wanting more, wanting the slime to make you cum,{p}and the desire to escape from the creature’s grasp."
    show slime lose4 with slow_dissolve:
        xpos 0.15 ypos -0.05
        zoom 0.65
    "The goo is expanding inside your hole,{p}at the same time the slime is stimulating your dick, pumping it furiously."
    "You know the slime is hungry for your essence, and with each passing second it’s getting harder to resist."
    with flashbulb
    e "No... must fight it!"
    e "Too good... I mustn’t give in."
    e "Ohhh!"
    with flashbulb
    with flashbulb
    show slime lose5 with slow_dissolve:
        xpos 0.15 ypos -0.05
        zoom 0.65
    "Unable to resist, you cum inside the goo."
    "With every squirt you can feel your body getting heavier and harder to move."
    "It’s like the slime is sucking the vitality out of your body through your cock."
    hide slime lose5 with slow_dissolve
    "Everything fades to black, and you cannot recall what happens next."

    scene forest 1 with vslow_dissolve
    "When you wake up again, you find that some coins is missing."
    "You smile grimly, glad that you're still alive."
    "After cleaning yourself up, you start over again."
    if jane_inv.qty(coin) != None:
        $ qty = int(jane_inv.qty(coin)*0.2)
        $ jane_inv.drop(coin,qty)
    $ Foe.slime = True
    $ Zalt.lust = 0
    $ Zalt.hp = 1
    $ persistent.CG_goo_lose = True
    $ Zalt.cor = min(Zalt.cor+1,100)
    jump forest_map_1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
