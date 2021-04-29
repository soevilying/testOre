label battle_GhostC:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 130
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    $ Battle.holyfcd = 0
    $ Map.good_battle = True
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    $ GhostC_round = 0
    stop music
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    if Map.castle_ghost == 44:
        scene castle 3
        "???" "Дай мне свой..."
    elif Map.castle_ghost == 35:
        scene castle 5
        "???" "Помоги...мне"
    elif Map.castle_ghost == 61:
        scene prison 5
        "???" "Пожалуйста...больше не надо, больше не надо."
    elif Map.castle_ghost == 62:
        scene prison 5
        "???" "Ха-ха-ха-ха! Беги!"






    jump battle_GhostC_loop



label battle_GhostC_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    if Map.castle_ghost == 44:
        show castle_ghost1 with vslow_dissolve:
            zoom 0.8
            xalign 0.5 yalign 0.45
    elif Map.castle_ghost == 35:
        show castle_ghost with vslow_dissolve:
            zoom 0.8
            xalign 0.5 yalign 0.45
    elif Map.castle_ghost == 61:
        show castle_ghost1 with vslow_dissolve:
            zoom 0.8
            xalign 0.5 yalign 0.45
    elif Map.castle_ghost == 62:
        show castle_ghost with vslow_dissolve:
            zoom 0.8
            xalign 0.5 yalign 0.45

    play music "<loop 12.4405>music/forest_fight_strong2.ogg"





    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Святой Кулак":
            $ red_damage = renpy.random.randint(Zalt.MATK*2, int((Zalt.MATK*2.5)+15))
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
            "Ты размахиваешь мечом, но он не может повредить призраку."

        if res == "Подчиниться":
            e "Я больше не могу драться.."
            "Враг слишком силен."
            "Тебя сбивают с ног."
            jump battle_GhostC_lose

        if res == "Бандаж":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Бандаж* [Zalt.heal]hp восстановлено"
        if res == "Флиртовать":
            "Ты не можешь соблазнить неживое существо."
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
                hide castle_ghost1
                hide castle_ghost
                if Map.castle_ghost == 44:
                    jump castle_map
                elif Map.castle_ghost == 35:
                    jump castle_map
                jump castle_prison
            elif True:
                "Побег не удался!"
                pass
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_GhostC_win
        $ Random = renpy.random.randint(1, 3)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Длинная рука призрака вытягивается вперед и хватает большой кусок дерева."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Длинная рука призрака вытягивается вперед и хватает большой кусок дерева."
                "Он безжалостно бьет тебя оружием."
        elif Random == 2:
            $ wolf_damage = renpy.random.randint(20, 40)
            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
            "Фантом издает пронзительный визг, от которого очень больно ушам."
        elif True:

            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Фантом образует шар темной энергии."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Фантом образует шар темной энергии и бьет вас им прямо в грудь."
        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_GhostC_win
        elif True:

            jump battle_GhostC_win

    elif Zalt.hp <= 0:
        "Враг слишком силен."
        "Тебя сбивают с ног."
        jump battle_GhostC_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_GhostC_lose
    elif True:
        jump battle_GhostC_loop


label battle_GhostC_win:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    play music "music/forest_fight_boss_end.ogg" noloop
    hide castle_ghost
    "Ты наносишь мощный удар, заставляя фантома кричать и съеживаться, как высохший фрукт. Его форма сжимается и исчезает из поля зрения."
    "Ты получаешь эктоплазму и 200 EXP."
    $ Zalt.exp = min(Zalt.exp+200, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    $ jane_inv_M.take(ectoplasm,1)
    $ Zalt.A_exp = Zalt.A_exp + 20*Zalt.A_exp_lv
    $ PPEXP = 20*Zalt.A_exp_lv
    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
    if Map.castle_ghost == 44:
        $ Map.castle_44 = 2
        $ Map.castle_20 = 1
        jump castle_map
    elif Map.castle_ghost == 35:
        $ Map.castle_35 = 2
        "Когда фантом исчезает с твоего пути, ты можешь войти в комнату."
        "На полу какой-то странный узор. "
        e 5 "Это что, какой-то демонический круг?"
        "Случайные предметы помещаются по кругу."
        "Череп, кинжал и несколько зелий."
        e 13 "Поговорим о том, что беспокоит."
        "Ты забираешь зелья и выбегаешь из комнаты."
        "Ты находишь одну бутылку зелья здоровья и одну бутылку зелья маны"
        $ jane_inv.take(hp_potion,1)
        $ jane_inv.take(mp_potion,1)
        jump castle_map
    elif Map.castle_ghost == 61:
        scene prison 5 with slow_dissolve
        e 13 "Отлично, значит, теперь я должен быть осторожен с неодушевленными предметами?"
        "Ты смотришь на оставшиеся полки в комнате."
        "Стоит ли их проверять?"
        menu:
            "Да" if True:
                "Ты сглатываешь и направляешься к следующей полке в другом конце комнаты."
                "В конце концов, ты не авантюрист, если не рискуешь."
                "Ты делаешь шаг вперед, и полка перед тобой превращается в призрак."
                "Он мчится к вам с пронзительным визгом."
                $ Map.castle_ghost = 62
                $ Map.castle_prison_6 = 2
                jump battle_GhostC
            "Нет" if True:
                $ Map.castle_prison_6 = 2
                e 13 "Нет, это ненужный риск."
                e 1 "В любом случае, в этой комнате я уже все осмотрел. "
                jump castle_prison
    elif Map.castle_ghost == 62:
        $ Map.castle_prison_6 = 3
        "Здесь ты ничего не находишь."
        e 13 "Все сгнило давным-давно."
        jump castle_prison
    jump castle_map


    return
label battle_GhostC_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    scene black
    stop music
    hide castle_ghost
    "Фантом безумно смеется и поднимается в воздух."
    "Его форма расширяется в черное облако, как будто кто-то уронил одну черную чернильную каплю в воду."
    "Бежать некуда, темная туча опускается на тебя и душит."
    "Ты борешься и пытаешься попасть в облако, но ничего не происходит."
    "По мере того как все меньше и меньше воздуха попадает в твои легкие, зрение начинает расплываться."
    "Облако поднимает твое тело вверх, а затем опускает его."
    scene black with vslow_dissolve
    "Последнее, что ты помнишь, - это ощущение падения в темную яму, пока не потеряешь сознание."
    "Когда ты просыпаешься, ты уже не в замке."
    $ Zalt.hp = 1
    $ Zalt.cor = min(Zalt.cor+1,100)
    $ Zalt.Dungeon_leave = True
    jump castle_map
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
