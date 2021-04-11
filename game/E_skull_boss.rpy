label battle_skull_boss:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 400
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ Battle.holyfcd = 0
    $ Map.good_battle = True
    stop music
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    "The smell is stronger than ever."
    "Its coming from behind a wall of trees blocking your view from what's behind them."
    "You push through."
    "You enter a clearing where the fog is strangely thin around the area"
    show skull at center with fade
    "But there’s no time to observe the area, {p}the massive monster from last night stands before you."
    play sound"music/roar.ogg"
    "It watches you with malicious eyes."
    "You draw your sword ready to fight."
    "The creature charges forward ready to kill!"
    hide skull
    jump battle_skull_boss_loop


label battle_skull_boss_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show skull at center
    play music "<loop 12.4405>music/forest_fight_strong2.ogg"





    while (wolf_hp > 0) and (Zalt.hp > 0):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
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
            "I can't fight anymore.."
            jump battle_skull_boss_lose
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
            $ Random = renpy.random.randint(1, 3)
            if Random == 1:
                "Escape failed!"
                pass
            elif Random == 2:
                "You run away."
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item
                hide slime
                jump forest_map
                pass
            elif True:
                "Escape failed!"
                pass
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_skull_boss_win
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
            jump battle_skull_boss_win
        elif True:

            "???" "RrrrrRRrrrr!"
            jump battle_skull_boss_win

    elif Zalt.hp <= 0:
        jump battle_skull_boss_lose
    elif True:

        jump battle_skull_boss_loop


label battle_skull_boss_win:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_boss_end.ogg" noloop
    pause 1
    hide skull with slow_dissolve
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    play sound "music/roar.ogg"
    "With the battle won,{p}you slash your sword in the air to wipe away the strange black liquid dripping from your blade."
    "As you sheath your sword you take note of your environment."
    "The creature was trying really hard to prevent you from seeing what was behind it."
    "You notice a piece of paper waving about between two-barrel sized boulders."
    "Apprehension makes you approach the boulders with caution, but nothing happens when you hold onto the brown parchment."
    "It feels crinkly and weak to the touch like the paper would tear with the slightest force."
    "You prop your left leg over one of the boulders and push with all your might."
    "The stone moves an inch freeing the paper from its grip."
    "Despite its worn-out condition the words on the paper are still legible."
    "{b}{b}{color=#781312}I can’t tell how long I’ve been in this labyrinth of fog and trees.{/color}"
    "{b}{color=#781312}The fog is playing tricks on me! {/color}"
    "{b}{color=#781312}I swear I saw the trees move and rearranging themselves every time I cut one down.{/color}"
    "{b}{color=#781312}I haven’t had any proper sleep since I left the tavern. {/color}"
    "{b}{color=#781312}That sickening laugh that permeates my dreams, I’m starting to hear it during the day as well.{/color}"
    "{b}{color=#781312}I don’t know if I can turn back to the tavern, none of the paths or trees look recognizable{/color}"
    "{b}{color=#781312}Even the marks I made on the trees have suddenly disappeared.{/color}"
    "{b}{color=#781312}Still, I got to keep going.{/color}"
    "{b}{color=#781312}I just need 3 more pieces of the emblem and he’ll tell me how to leave this place.{/color}"
    "{b}{color=#781312}And destroy the fog once and for all.{/color}"
    "{b}{color=#781312}Those two in the tavern they are conspiring against me.{/color}"
    "{b}{color=#781312}They know how to end this all, they just don’t want to.{/color}"
    "{b}{color=#781312}Glory to the Grand Creator!{/color}"
    "{b}{color=#781312}When I am free of this place I will burn them all to the ground.{/color}"
    "{b}{color=#781312}-P.D.{/color}"
    "A cold shiver runs down your back."
    "You immediately make haste back to the tavern."
    "Snow might know something."
    "<[name] gained 500 EXP.>"
    "<[name] gained 1 Level-up-points.>"
    $ Zalt.points = Zalt.points +1
    $ Zalt.exp = min(Zalt.exp+500, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    $ Map.boss1 = 2
    $ jane_inv_K.take(Skull_emblem)
    $ Items.em =Items.em+1
    jump forest_map_2

    return
label battle_skull_boss_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    "The skulls demon plunges its claws into your chest. "
    show red1 at center with dissolve
    play sound "music/blood.ogg"
    "You hear something break... was it your ribs?"
    "You fall onto the ground a bloodied mess."
    "[name]" "Ahhhhh!!!!"
    "Excruciating pain cripples your body. You can't move."
    play sound "music/blood.ogg"
    "It hurts."
    "The skull demon’s eyes, it looks at you with such terrifying anger."
    "Skull demon" "D..ie...!!"
    show red2 at center with dissolve
    play sound "music/blood.ogg"
    "[name]" "N-!"
    "You feel something go through you again{w}...but where’s the pain?"
    "Everything’s just{w} fading away..."
    "Not like this..."
    scene black with vslow_dissolve
    "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Oh shit, you really killed him.{/color}{/b}"
    "Who is it? Your consciousness is fading, even their voice is barely audible."
    "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Ugh, this isn’t what I want. You stupid skull head!{/color}{/b}"
    "{color=#7d0004}???{/color}" "{b}{color=#7d0004}I have to find some new entertainment now!{/color}{/b}"
    "You can't see and hear anything anymore."
    "It’s over, you fade into the void."
    "{b}{color=#c22719}<GAME OVER>{/color}"
    menu:
        "New game" if True:
            return
        "No!" if True:
            $ Zalt.hp = 1
            jump forest_map0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
