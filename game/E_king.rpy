label battle_king:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    if Map.castle_king == "knight":
        $ wolf_max_hp = 300
    elif True:
        $ wolf_max_hp = 550
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    scene castle 6
    $ Battle.holyfcd = 0
    $ Map.good_battle = True
    stop music

    jump battle_king_loop

label battle_king_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show king fight at center with dissolve
    stop music
    stop sound
    $ renpy.music.set_pause(False, channel='Chan2')
    $ renpy.music.set_volume(1, 0, channel = "Chan2")
    play Chan2[ "<silence 0.1>", "<loop 34.9983>music/spooky_fight.ogg" ]fadein 3




    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Святой Кулак":
            $ red_damage = renpy.random.randint(int((Zalt.MATK*2.5)+5), int((Zalt.MATK*3)))
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
                    "You unleash Holy Fist."
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
            jump battle_king_lose
        if res == "Флиртовать":
            "You cannot seduce a non-living creature."
        if res == "Бандаж":
            $ Zalt.heal = renpy.random.randint((Zalt.int*3)+25, (Zalt.int*3)+40)
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
            "You can't run!."
        elif True:

            pass
        if wolf_hp <= 0:
            jump battle_king_win

        $ Random = renpy.random.randint(1, 5)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The king slashes your arm."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(40, 60)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The king slashes your arm."
                "His ghostly flame damages you further."
        elif Random == 2:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The king strikes you repeatedly."
                "You manage to parry every strike."
            elif True:
                $ wolf_damage = renpy.random.randint(20, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The king strikes you repeatedly."
                "You manage to parry every strike but he lands a surprise kick that sends you flying towards a pillar."
        elif Random == 3:
            $ wolf_damage = renpy.random.randint(40, 50)
            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
            "The king leaps in front of you and suddenly disappears. "
            "Before you can blink he reappears behind you and you feel like your insides were punched a hundred times."
        elif True:

            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The king stabs you in the shoulder."
                "But you dodged it!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 55)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The king stabs you in the shoulder."
                "It leaves no mark but the pain you feel is very real."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_king_win
        elif True:

            jump battle_king_win

    elif Zalt.hp <= 0:
        jump battle_king_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_king_lose
    elif True:
        jump battle_king_loop


label battle_king_win:
    play Chan2 "music/spooky_fight_end.ogg" noloop
    pause 1
    hide king fight with slow_dissolve
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    play sound "music/body_fall.mp3"
    "You rush in and strike the king’s blade off of his hand."
    "He is taken aback by your strength, giving you the opportunity to grab his blade and ram it right into him."
    "You roar and push the blade all the way through until the hilt meets his chest."
    "As the blade penetrates his back, the king gasps and melts into a puddle of shadows that itself disappears without a trace."
    "You take a minute to collect yourself after the battle."
    "Although shaken, you remind yourself that Flo needs help. "
    "The loud noise of what sounds like gears turning draws your attention."
    "The stone throne in front of you splits into two and opens up a pathway."
    "There is something on the floor."
    show black3 at center
    show swordfragment at center with dissolve
    "It's a .....what's this?"
    "You pick it up."
    "< You get 1000 EXP. >"
    $ Zalt.exp = min(Zalt.exp+1000, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
    $ PPEXP = 50*Zalt.A_exp_lv
    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
    $ jane_inv_K.take(sword_fragment)
    $ Map.castle_42 = 1
    $ Map.castle_41 = 2
    $ Map.castle_prison_7 = 4
    jump castle_map

    return
label battle_king_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    hide king fight at center
    "Your swings have weakened."
    "Every move you make he is able to swipe it off with each."
    "The king throws his sword."
    play sound "music/blood.ogg"
    "It lands right in front of your feet and explodes, unleashing a pillar of blue fire that burns you to cinder."
    scene black with slow_dissolve
    show red2 at center with vslow_dissolve
    "Your screams of pain are drowned out by the roar of the flames."
    "In just seconds nothing remains of you."
    pause 3
    "{b}{color=#c22719}<GAME OVER>{/color}"
    menu:
        "New game" if True:
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
