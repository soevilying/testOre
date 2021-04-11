define RR = Character('Red Hood', color="#CD0000")
define TT = Character('mr.Wolf', color="#B5B5B5")

screen simple_stats_screen:
    frame:
        xalign 0.02 yalign 0.95
        xminimum 220 xmaximum 220
        has vbox
        text "[name]" size 22 xalign 0.5
        null height 5
        text "Здоровье" size 16
        hbox:
            bar:
                xmaximum 130
                value Zalt.hp
                range Zalt.maxhp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None

            null width 5


            text "[Zalt.hp] / [Zalt.maxhp]" size 16
        text "Мана" size 16
        hbox:

            bar:
                xmaximum 130
                value Zalt.mp
                range Zalt.maxmp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None


            null width 5


            text " {color=#0080c0}[Zalt.mp] / [Zalt.maxmp]{/color}" size 16
        text "Похоть" size 16
        hbox:

            bar:
                xmaximum 130
                value Zalt.lust
                range Zalt.maxlust
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None


            null width 5


            text "[Zalt.lust] / [Zalt.maxlust]" size 16


    frame:
        xalign 0.5 yalign 0.01
        xminimum 250 xmaximum 250
        has vbox
        hbox:
            text "Здоровье" size 28 xalign 0.5
            null height 5
            bar:
                xmaximum 130
                value wolf_hp
                range wolf_max_hp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None

            null width 5

            text "[wolf_hp] / [wolf_max_hp]" size 16
        hbox:
            if Battle.flirt == True:
                text "Похоть" size 14 xalign 0.5
                null height 5
                bar:
                    xmaximum 130
                    value wolf_lust
                    range wolf_max_lust
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[wolf_lust] / [wolf_max_lust]" size 16
            else:
                pass


screen battle_menu:
    vbox:
        xalign 0.3 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Подчиниться" action Return("Подчиниться") yminimum 40
                else:
                    textbutton "Подчиниться" action None yminimum 40
    vbox:
        xalign 0.4 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Навык" action Show("battle_skill") yminimum 40
                else:
                    textbutton "Навык" action None yminimum 40
    vbox:
        xalign 0.5 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Атака" action Return("Атака") yminimum 40
                else:
                    textbutton "Атака" action None yminimum 40
    vbox:
        xalign 0.6 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Предметы" action Show("battle_item") yminimum 40
                else:
                    textbutton "Предметы" action None yminimum 40
    vbox:
        xalign 0.7 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Сбежать" action Return("Сбежать") yminimum 40
                else:
                    textbutton "Сбежать" action None yminimum 40




screen battle_skill:
    vbox:
        xalign 0.4 ypos 0.7
        frame:
            textbutton "Навык" action Hide("battle_skill") yminimum 40
    vbox:
        xalign 0.4 ypos 0.6
        hbox:
            frame:
                if players_turn and Zalt.mp>=20:
                    textbutton "Перевязка" action Return("Перевязка") yminimum 40
                else:
                    textbutton "Перевязка" action None yminimum 40
            frame:
                if Battle.holyfcd == 0:
                    if players_turn and Zalt.mp>=20 and Battle.holyf == True:
                        textbutton "Святой Кулак" action Return("Святой Кулак") yminimum 40
                    elif players_turn and Zalt.mp<20 and Battle.holyf == True:
                        textbutton "Святой Кулак" action None yminimum 40
                    else:
                        textbutton "-" action None yminimum 40
                else:
                    if players_turn and Zalt.mp>=20 and Battle.holyf == True:
                        textbutton "Святой Кулак(2CD)" action None yminimum 40
                    elif players_turn and Zalt.mp<20 and Battle.holyf == True:
                        textbutton "Святой Кулак(2CD)" action None yminimum 40
                    else:
                        textbutton "-" action None yminimum 40
            frame:
                if players_turn and Battle.flirt == True:
                    textbutton "Флиртовать" action Return("Флиртовать") yminimum 40
                else:
                    textbutton "-" action None yminimum 40

screen battle_item:
    vbox:
        xalign 0.6 ypos 0.7
        frame:
            textbutton "Предметы" action Hide("battle_item") yminimum 40
    vbox:
        xalign 0.6 ypos 0.6
        hbox:

            frame:
                if players_turn and jane_inv.qty(hp_potion) >= 1:
                    textbutton "Зелье Здоровья" action Return("Зелье Здоровья") yminimum 40
                else:
                    textbutton "-" action None yminimum 40
            frame:
                if players_turn and jane_inv.qty(mp_potion) >= 1:
                    textbutton "Зелье Маны" action Return("Заелье Маны") yminimum 40
                else:
                    textbutton "-" action None yminimum 40
label battle_game_1:

    $ wolf_max_hp = 400
    $ wolf_hp = wolf_max_hp
    $ players_turn = False


    $ Battle.holyfcd = 0

    scene forest light
    $ renpy.music.set_volume(0.2, 0, channel = "music")

    play music"music/rainy.mp3"
    stop Chan1 fadeout 5
    stop Chan2 fadeout 10
    stop Chan3 fadeout 5
    "Снаружи таверны трудно что-либо разглядеть, все окутано серым туманом."
    "Твой единственный источник света - луна и сияние таверны."
    play sound"music/snap.mp3"
    "Щелк!"
    "Твои уши улавливают звук ломающихся веток."
    play sound"music/foot2.ogg"
    "Что-то движется перед тобой."
    e 5 "- Кто там?"
    "Ответа не последовало."
    "Ты вытаскиваешь меч и медленно приближаешься к лесу."
    "Воздух внезапно становится тихим, но ты можешь почувствовать чье - то присутствие, смотрящее на тебя."
    "Что-то выскакивает из-за деревьев."
    play sound"music/roar.ogg"
    show skull at center with fade
    "Громадная черная фигура с черепом вместо головы."
    "Он рычит на тебя."
    "Чудовище поднимает свою массивную руку и с силой швыряет ее на землю. "
    "Тебе удается вовремя отскочить назад и подготовить боевую стойку. "
    "Он не выглядит счастливым, что промахнулся."
    "Вот оно."
    hide skull
    $ renpy.music.set_volume(1, 0.5, channel = "music")
    jump battle_1_loop


label battle_1_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show skull at center
    play music "<loop 12.4405>music/forest_fight_strong2.ogg"





    while (wolf_hp > 0) and (Zalt.hp > 0):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Святой Кулак":
            $ red_damage = renpy.random.randint(Zalt.MATK*2, int((Zalt.MATK*2.5)+10))
            $ wolf_hp -= red_damage
            $ Zalt.mp = min(Zalt.mp -30, Zalt.maxmp)
            $ Battle.holyfcd = 3
            " (Damage dealt wip - [red_damage]hp)"

        if res == "Предметы":
            $ Zalt.hp = min(Zalt.hp +5, Zalt.maxhp)
            $ cookies_left -= 1
            "*Напиток* 5 Hp восстановлен"

        if res == "Атака":
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-20), Zalt.ATK)
            $ Random = renpy.random.randint(0, 100)
            if Random >= Zalt.CRIT:
                $ wolf_hp -= red_damage
                "Ты выхватываешь меч и бросаешься в атаку.\n(Damage dealt- [red_damage]hp)"
            elif True:
                $ qty = red_damage*2
                $ wolf_hp -= red_damage*2
                "Ты выхватываешь меч и бросаешься в атаку.\n{b}{color=#ffd65c}(Critical damage! -[qty]hp){/color}"


        if res == "Подчиниться":
            "Я больше не могу драться.."
            jump battle_1_lose

        if res == "Перевязка":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Перевязка* [Zalt.heal]hp restored"
        if res == "Сбежать":
            $ Random = renpy.random.randint(1, 3)
            if Random == 1:
                "Побег не удался!"
                pass
            elif Random == 2:
                "Побег не удался!"
                pass
            elif True:
                "Побег не удался!"
                pass
        elif True:
            pass

        $ Random = renpy.random.randint(1, 100)
        if Random <= Battle.dodge:
            "???" "РррррРРрррр! {i}*Монстр бьет тебя*{/i}"
            "Но ты увернулся от его атаки!"
        elif True:
            $ wolf_damage = renpy.random.randint(15, 20)
            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
            "???" "РррррРРрррр! {i}*Монстр бьет тебя*{/i}"
        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_1_lose
        elif True:

            "???" "РррррРРрррр!"
            jump battle_1_win

    elif Zalt.hp <= 0:
        jump battle_1_lose
    elif True:

        jump battle_1_loop


label battle_1_win:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    play music "music/forest_fight_boss_end.ogg" noloop
    "Демон-череп сгибается и отшатывается назад. {p}Он рычит и убегает в лес."
    "Кажется он что то уронил"
    e 1 "- Что это?"
    "Вы получаете 300 монет"
    "Ты чувствуете себя сильнее, сражаясь с врагом, которого было почти невозможно победить."
    "{b}{color=#19c22a}<[name] gains 5 lv-points!>{/color}"
    $ Zalt.points = Zalt.points +5
    $ jane_inv.take(coin,300)
    $ Zalt.tut_win = True
    jump map0

    return
label battle_1_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    e 5 " Он слишком силен… что это за сила?"
    "Фигура мчится мимо тебя, это Сноу!"
    "Он владеет таким же мечом, как твой, и прыгает на чудовище."
    "Его удар достигает цели и рассекает демона поперек груди. "
    "Демон-череп сгибается и отшатывается назад. {p}Он рычит и убегает в лес."
    s "Давай, малыш, все кончено."
    $ Zalt.tut_win = False
    jump map0
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
