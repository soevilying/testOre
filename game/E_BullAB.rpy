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
                    "Ты вытаскиваешь меч и бросаешься в атаку.\n(Нанесенный урон- [red_damage]hp)"
            elif True:
                $ qty = red_damage*2
                $ wolf_hp -= red_damage*2
                if wolf_hp <= 0:
                    pass
                elif True:
                    "Ты вытаскиваешь меч и бросаешься в атаку.\n{b}{color=#ffd65c}(Критический урон! -[qty]hp){/color}"

        if res == "Подчиниться":
            e "Я больше не могу драться.."
            "Враг слишком силен."
            "Тебя сбивают с ног."
            jump battle_bullAB_lose
        if res == "Флиртовать":
            $ Random = renpy.random.randint(1, 4)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "Ты принимаешь ряд поз с уверенной улыбкой."
                "Враг заинтригован вашими движениями."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "Ты дразнишь своего противника, атакуя его в лоб."
                "Чувственно потирая соски, промежность и слегка поглаживая ягодицы."
                "Твой противник тяжело дышит, сжимая свою очевидную эрекцию."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "Ты чувственно потираешь промежность, позволяя своему члену немного приподняться, прежде чем показать свой член врагу."
                "Похоть наполняет твоего противника, он обездвижен мощным желанием вашего члена."
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "Ты принимаешь ряд поз с уверенной улыбкой."
                    "Враг застает тебя врасплох и отбрасывает назад. Ты едва держишься на ногах."
                elif Random == 2:
                    "Ты дразнишь своего противника, атакуя его в лоб."
                    "Чувственно потирая соски, промежность и слегка поглаживая ягодицы."
                    "Враг игнорирует твои попытки соблазнить его."
                elif True:
                    "Ты чувственно потираешь промежность, позволяя своему члену немного приподняться, прежде чем показать свой член врагу."
                    "Враг в ярости от твоих действий."
            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                "Бык падает на колени, его твердый член пульсирует и течет по всему полю боя."
                jump battle_bullAB_win
            elif True:
                pass
        if res == "Бандаж":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Бандаж* [Zalt.heal]hp восстановлено"
        if res == "Зелье здоровья":
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
                $ Foe.bullab = 3
                hide bullw
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item
                hide slime
                jump forest_map0
            elif True:
                "Побег не удался!"
                pass
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_bullAB_win
        $ Random = renpy.random.randint(1, 6)
        if Random <= 2:
            $ wolf_damage = renpy.random.randint(15, 30)
            $ Zalt.lust += wolf_damage
            "Мускус воина-быка землистый и мощный."
            "Твоя промежность нагревается."
            "Бык-воин" "Тебе это нравится, хммм? Подчинись сейчас же, и я дам тебе то, что ты хочешь!"
        elif True:
            $ Random = renpy.random.randint(1, 80)
            if Random <= Battle.dodge:
                "Бык-воин" "РРРРРРРРРР! {i}*Монстр бьет тебя*{/i}"
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(30, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Бык-воин" "РРРРРРРРРР! {i}*Монстр бьет тебя*{/i}"

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_bullAB_win
        elif True:

            jump battle_bullAB_win

    elif Zalt.hp <= 0:
        "Кулак вражеского быка с силой ударяет тебя в живот."
        "Твое тело на секунду сжимается, и ты шатаешься на ногах."
        jump battle_bullAB_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
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
        "Бык-воин" "Эх...!"
        hide bullw with dissolve

        "Бык Б" "Как ты можешь...!"
        "Еще одна атака быка!"
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
        "Бык А" "Раргх! Как ты смеешь! Мы это запомним."
        "Бык Б" "На этот раз мы позволили тебе победить."
        "Бык А" "Ты не сможешь уничтожить всех нас, когда мы доберемся до остальных наших братьев."
        e 9 "О боже, с двумя я справлюсь, но с целым племенем? Не хочу испытывать судьбу."
        "Ты чувствуешь себя сильнее, когда побеждаешь двух сильных врагов."
        "{b}{color=#19c22a}<[name] набираешь 1 уровень!>{/color}"
        $ Zalt.points = Zalt.points +1
        "Ты бежишь туда, откуда пришел."
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
    "Бык хватает тебя за шею и швыряет на землю, как тряпичную куклу."
    "Тебе удается подтянуться, но все силы покинули твое тело."
    "Ты бежишь обратно к тропе, с которой пришел."
    $ Foe.bullab = 3
    $ Zalt.hp = 1
    jump forest_map0
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
