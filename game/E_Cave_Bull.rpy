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
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-30), Zalt.ATK-5)
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
            jump battle_cave_bull_lose

        if res == "Бандаж":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Бандаж* [Zalt.heal]hp восстановлено"
        if res == "Флиртовать":
            "Твои попытки соблазнить врага терпят неудачу, бык слишком охвачен яростью, чтобы даже заметить."

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
            $ Random = renpy.random.randint(1, 2)
            if Random == 1:
                "Ты убегаешь."
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item
                hide slime
                jump Cave_map
            elif True:
                "Побег не удался!"
                pass
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_cave_bull_win
        $ Random = renpy.random.randint(1, 4)
        if Random == 1:
            $ Random = renpy.random.randint(1, 80)
            if Random <= Battle.dodge:
                "Бык взмахивает топором, и тот разбивает ближайший валун."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(30, 55)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Бык взмахивает топором, и тот разбивает ближайший валун, куски камней пролетают мимо и попадают тебе в живот."
        elif Random == 2:
            $ Random = renpy.random.randint(1, 80)
            if Random <= Battle.dodge:
                "Бык пытается схватить тебя за морду."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(40, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Бык хватает тебя за морду."
                "Ты цепляешься за его руку, заставляя его отправить тебя в полет и ударить о стену позади."
        elif True:
            $ Random = renpy.random.randint(1, 80)
            if Random <= Battle.dodge:
                "Бык прижимает тебя плечом к стене."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(25, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Бык прижимает тебя плечом к стене."
        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_cave_bull_win
        elif True:

            jump battle_cave_bull_win

    elif Zalt.hp <= 0:
        "Враг слишком силен."
        "Тебя сбивают с ног."
        jump battle_cave_bull_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
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
        "Бык отшатывается."
        show black2 with dissolve
        hide black2 with dissolve
        "Злой Бык-воин" "Ты больше не возьмешь нас! Ты умрешь, демон!"
        e 9 "Срань господня!"
        show black2 with dissolve
        "Вся фигура воина-быка тает, как слизь, обнажая его скелет."
        "Ты кричишь от ужаса и отскакиваешь."
        show bullwghost at center with vslow_dissolve
        "Эфирная форма самого себя затем окутывает скелет, и воин-бык преобразует себя только теперь с призрачным видом."
        "Глаза других быков светятся призрачной синевой, и с открытыми ртами они издают пронзительный крик."
        "Вы сами будете продолжать борьбу."
        "Бык может быть призраком, но под этой штукой находится физическое тело, в которое можно попасть!"
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
        "Призрачный Бык-Воин" "Наконец-то..."
        scene cave 1 with dissolve
        "Призрачный бык-воин и его собратья исчезают в небытии."
        "Их формы распадаются в пыль, которая исчезает в забвении."
        show black2 with dissolve
        hide black2 with dissolve
        "Затем в одной яркой вспышке света вы оказываетесь перед грудой бычьих скелетов."
        "Случалось ли такое вообще?"
        "В ладони правой руки вы находите немного эктоплазмы."
        "{color=#19c22a}Ты получаешь 4 эктоплазмы и 400 EXP.{/color}"
        e 13 "Мне лучше работать побыстрее, пока Фло так же не закончил."
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
        "Бык сбивает тебя с ног и разбивает тебе лицо тупым концом своего топора."
        scene black with dissolve
        "Все становится черным."
        "Ты просыпаешься за пределами пещеры."
    elif True:
        "Ты не заметил, как призрачный топор призрака опустился низко и ударил тебя по икрам."
        "Холодное лезвие пронзает тебя с легкостью, заставляя упасть."
        e 0 "Подожди, нет!"
        "Но слишком поздно, призрачный бык уже стоит над тобой и обрушивает свой топор прямо на твою голову."
        scene black with dissolve
        "Ты просыпаешься вне пещеры."

    $ Zalt.hp = 1
    $ Zalt.Dungeon_leave = True
    jump Cave_map
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
