label battle_cave_slime:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 100
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    $ Battle.holyfcd = 0
    stop Chan1
    stop Chan2
    $ Map.good_battle = True
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    $ cave_slime_round = 0
    stop music
    scene caveruin 1n






    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    jump battle_cave_slime_loop



label battle_cave_slime_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show slime at center
    play music "<loop 4.6903>music/forest_fight_small.ogg"





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
            jump battle_cave_slime_lose

        if res == "Бандаж":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Бандаж* [Zalt.heal]hp восстановлено"
        if res == "Флиртовать":
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
            jump battle_cave_slime_win
        $ Random = renpy.random.randint(1, 3)
        if Random <= 1:
            $ wolf_damage = renpy.random.randint(10, 30)
            $ Zalt.lust += wolf_damage
            "Слизь разбрызгана по всему телу."
            "Ты чувствуешь что-то горячее в промежности."
            "[name]" "Кажется, в этой слизи есть что-то ядовитое..."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Слизь" "РРРРРРРРРР! {i}*Монстр бьет тебя*{/i}"
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Слизь" "РРРРРРРРРР! {i}*Монстр бьет тебя*{/i}"
        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_cave_slime_win
        elif True:

            "Слизь" "РРРРРРРРРР!"
            jump battle_cave_slime_win

    elif Zalt.hp <= 0:
        "Враг слишком силен."
        "Тебя сбивают с ног."
        jump battle_cave_slime_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_cave_slime_lose
    elif True:
        jump battle_cave_slime_loop


label battle_cave_slime_win:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_small_end.ogg" noloop
    pause 1
    hide slime with slow_dissolve

    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music
    $ cave_slime_round = cave_slime_round+ 1
    if cave_slime_round != 2:
        "Слизь стекает в трещину в стене и убегает."
        "Нет времени на отдых, товарищ слизи подкрался во время вашего боя и ударил тебя сбоку."
        $ wolf_hp = wolf_max_hp
        jump battle_cave_slime_loop
    elif True:

        "Твое лезвие рассекает тело слизи, разрезая его пополам."
        "С громким шлепком остатки слизи падают на землю и растворяются в громком шипящем звуке. "
        "Ты получаешь 3 камня слизи и 200 exp."
        $ Zalt.exp = min(Zalt.exp+200, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        $ jane_inv_M.take(slime_jewel,3)
        $ Map.ca2 = 1
        $ Map.ca3 = 1
        $ Map.ca4 = 1
        scene cave 1 with dissolve
        $ Zalt.A_exp = Zalt.A_exp + 25*Zalt.A_exp_lv
        $ PPEXP = 25*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump Cave_map


    return
label battle_cave_slime_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    scene black
    stop music
    "Слизь одолевает вас и вырастает до огромных размеров."
    "Ты пытаешься убежать, но существо хватает тебя за руку, и тебя охватывает холодный шок."
    "Это как будто каждая унция энергии внутри вас высасывается."
    "Все становится черным, и ты снова оказываешься за пределами пещеры."
    $ Zalt.hp = 1
    $ Zalt.cor = min(Zalt.cor+1,100)
    $ Zalt.Dungeon_leave = True
    jump Cave_map
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
