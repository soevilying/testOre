label battle_lizad_spy:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 150
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ Battle.holyfcd = 0
    $ Map.good_battle = True
    stop music








    jump battle_lizad_spy_loop


label battle_lizad_spy_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show lizardw at center
    play music "<loop 12.6082>music/forest_fight_friend.ogg"





    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Святой Кулак":
            $ red_damage = renpy.random.randint(Zalt.MATK*2, int((Zalt.MATK*2.5)+10))
            $ wolf_hp -= red_damage
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            $ Battle.holyfcd = 3
            $ Random = renpy.random.randint(1, 3)
            if wolf_hp <= 0:
                pass
            elif True:
                if Random == 1:
                    "Ты бросаешься вперед и наносишь удар по врагу."
                elif Random == 2:
                    "Ты бьешь врага своим Святым Кулаком."
                elif True:
                    "С молниеносной скоростью ты поражаешь врага Святым Кулаком."
                " (Нанесенный урон - [red_damage]hp)"

        if res == "Предметы":
            $ Zalt.hp = min(Zalt.hp +5, Zalt.maxhp)
            $ cookies_left -= 1
            "*Глоток* 5hp восстановлено"

        if res == "Атака":
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-20), Zalt.ATK)
            $ Random = renpy.random.randint(0, 100)
            if Random >= Zalt.CRIT:
                $ wolf_hp -= red_damage
                if wolf_hp <= 0:
                    pass
                elif True:
                    "Ты выхватываешь меч и бросаешься в атаку.\n(Нанесенный урон- [red_damage]hp)"
            elif True:
                $ qty = red_damage*2
                $ wolf_hp -= red_damage*2
                if wolf_hp <= 0:
                    pass
                elif True:
                    "Ты выхватываешь меч и бросаешься в атаку.\n{b}{color=#ffd65c}(Критический урон! -[qty]hp){/color}"

        if res == "Подчиниться":
            e "Я больше не могу драться.."
            "Враг слишком силен."
            "Тебя сбивают с ног."
            jump battle_lizad_spy_lose
        if res == "Флиртовать":
            $ Random = renpy.random.randint(1, 7)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You successfully jump behind the lizard and plunge your hands down his loincloth."
                "You find his thin slit and gently massage its entrance before jumping away."
                "The lizard is confused and breathing heavily."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You tease the lizard by playing with your nipples and motioning him to join you."
                "The lizard darts his tongue out with a lewd smile, you can tell he wants more."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You strike a series of poses with a confident smile."
                "He gasps loudly and grabs his groin as though trying to hide it from view."
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You successfully jump behind the lizard and plunge your hands down his loincloth."
                    "You find his thin slit and gently massage its entrance before jumping away."
                    "The lizard growls angrily at you and swats his spear at you."
                elif Random == 2:
                    "You tease the lizard by playing with your nipples and motioning him to join you."
                    "He spits on the ground and angrily cuts the air with his dagger."
                elif True:
                    "You strike a series of poses with a confident smile."
                    "He ignores your seduction."
            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                jump battle_lizad_spy_win
            elif True:
                pass
        if res == "Бандаж":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Бандаж* [Zalt.heal]hp восстановлено"
        if res == "Зелье Здоровья":
            $ Zalt.heal = 60
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ jane_inv.drop(hp_potion)
            "*Зелье здоровья* [Zalt.heal]hp восстановлено"
        if res == "Зелье маны":
            $ Zalt.heal = 60
            $ Zalt.mp = min(Zalt.mp+Zalt.heal, Zalt.maxmp)
            $ jane_inv.drop(mp_potion)
            "*Зелье маны* [Zalt.heal]mp восстановлено"
        if res == "Сбежать":
            "You can't run!"
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_lizad_spy_win

        $ Random = renpy.random.randint(1, 4)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The spy cuts you with his dagger."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(15, 45)
                $ Zalt.hp -= wolf_damage
                "The spy cuts you with his dagger. It burns deep into your flesh."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The lizard spy plunges his spear into your arm."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(30, 60)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The lizard spy plunges his spear into your arm."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1





    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_lizad_spy_win
        elif True:

            jump battle_lizad_spy_win

    elif Zalt.hp <= 0:
        jump battle_lizad_spy_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_lizad_spy_lose
    elif True:
        jump battle_lizad_spy_loop


label battle_lizad_spy_win:
    play music "music/forest_fight_friend_end.ogg" noloop
    pause 1
    hide lizardw with slow_dissolve
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    "With a powerful punch you knock the lizard off his feet."
    "His spear is sent flying to the side."
    "He picks himself up and pants heavily as blood gushes out his nose."
    "Lizard spy" "Raarrgghhh!"
    "He picks up his dagger in front of him."
    "You brace for another attack."
    play sound "music/blood.ogg"
    "But instead the lizard plunges his blade deep into his stomach and slashes it across."
    e 5 "What?"
    "Even more blood bursts out of his wound."
    "The colour in his eyes seem to fade as they roll back and the lizard collapses onto the ground. "
    "Lizard spy" "Clar...ise...Mi...a, I...am...sorry."
    "His body writhers on the ground for a few seconds."
    "You’re left dumbfounded and frozen in place by what you saw."
    "Slowly, you approach his still body and with trembling hands you test his pulse."
    "Nothing."
    "You take a deep breath and tell yourself to steel your heart."
    play sound "music/blood.ogg"
    "With held breath you get down and make quick work of and pull out his heart."
    play sound "music/heartbeat.ogg"
    e 9 "What the heck!"
    "You nearly drop the organ in your hand."
    "Its weak beats fades slowly in your grasp."
    "You hastily stuff it in your bag."
    e 13 "...Time to get back to the bull village."
    $ jane_inv_K.take(Lizard_heart)
    if Nauxus.meet == 3:
        $ Nauxus.meet = 4
    $ Thane.quest = 4
    $ Foe.spydie = 1
    jump forest_map

    return
label battle_lizad_spy_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    hide lizadw with dissolve
    "You move in to strike the enemy spy on the head."
    "But he dodges and swiftly plunges his dagger through your heart. "
    play sound "music/blood.ogg"
    "The pain... you wonder where the pain is."
    play sound "music/blood.ogg"
    show red2 at center with dissolve
    "But just before it hits you the spy is holding your heart out in front of him."
    scene black with vslow_dissolve
    "You fall back spluttering blood onto the ground and all fades to nothingness."
    "{b}{color=#c22719}<GAME OVER>{/color}"
    menu:
        "New game" if True:
            return
        "No!" if True:
            jump forest_map
    stop music
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
