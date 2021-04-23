label battle_bullcamp:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 170
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    $ Map.good_battle = True
    $ Battle.holyfcd = 0
    stop music
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    jump battle_bullcamp_loop


label battle_bullcamp_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show bullw at center

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
            jump battle_bullcamp_lose
        if res == "Флиртовать":
            $ Random = renpy.random.randint(1, 4)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "Ты принимаешь ряд поз с уверенной улыбкой."
                "Враг заинтригован твоими движениями."
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
                "Похоть наполняет твоего противника, он обездвижен мощным желанием твоего члена."
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
                jump battle_bullcamp_win
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
            "*Зелье * [Zalt.heal]mp восстановлено"
        if res == "Сбежать":
            "Ты не можешь бежать!"
            pass
        elif True:
            pass

        if wolf_hp <= 0:
            jump battle_bullcamp_win
        $ Random = renpy.random.randint(1, 80)
        if Random <= Battle.dodge:
            "Бык-воин" "РРРРРРРРРР! {i}*Монстр бьет тебя*{/i}"
            "Но ты увернулся от его атаки!"
        elif True:
            $ wolf_damage = renpy.random.randint(20, 35)
            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
            "Бык-воин" "РРРРРРРРРР! {i}*Монстр бьет тебя*{/i}"

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_bullcamp_win
        elif True:

            jump battle_bullcamp_win

    elif Zalt.hp <= 0:
        "Кулак вражеского быка с силой ударяет тебя в живот."
        "Твое тело на секунду сжимается, и ты остаешься шататься на ногах."
        jump battle_bullcamp_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_bullcamp_lose
    elif True:
        jump battle_bullcamp_loop


label battle_bullcamp_win:
    if Foe.bullcamp ==2:
        play music "music/forest_fight_friend_end.ogg" noloop
        pause 1
        hide bullw with slow_dissolve
        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item
    elif True:
        "Бык-воин" "Эх...!"
        hide bullw with dissolve
    $ Foe.bullcamp = Foe.bullcamp+1
    if Foe.bullcamp ==1:
        "Ты вонзаешь свой клинок в грудь быка."
        play sound "music/blood.ogg"
        "Крича во всю глотку, ты изо всех сил тянешь лезвие, разрубая быка пополам."
        "Он падает на землю-мертвый."
        "С другой стороны, ящерицам удается уничтожить своего врага."
        "Морда быка становится темно-фиолетовой и падает на землю."
        "Он корчится от боли, изо рта вырывается пена, прежде чем все его тело перестает двигаться."
        "Ты кричишь на ящерицу."
        e 1 "Я пойду, чтобы установить последний камень.Оставайтесь здесь,будьте осторожны!"
        "Ты бежишь к последнему месту."
        scene black with dissolve
        "Третья гвардия Ящериц" "Идут еще!"
        play sound "music/foot1.ogg"
        scene forest 6 with dissolve
        "ТЫ ставишь последний камень на его место"
        with flashbulb
        e 9 "А-а-а-а"
        "<Твоё HP превращается в 1>"
        "<Твоё MP превращается в 1>"
        $ Zalt.hp = 1
        $ Zalt.mp = 1
        "Из тумана выбегают еще два быка."
        "Третий Бык-Воин" "Предатель!!"
        "Четвертый Бык-воин" "Давайте возьмем волка!"
        "Ошеломленный и страдающий."
        "Нет времени на передышку, нужно бить быков."
        jump battle_bullcamp
    elif Foe.bullcamp ==2:
        "Еще одна атака быков!!"
        jump battle_bullcamp
    elif True:
        "Твой меч рассекает ему правую руку."
        "По всему его телу капает кровь из ран, которые ты ему нанес, но бык не сдается."
        "Его движения вялые, но он все еще сжимает свое оружие изо всех сил. "
        "Это продолжалось достаточно долго, ты позволил быку поднять топор над головой, прежде чем быстро ударить его в челюсть.."
        "Твой клинок пронзает его череп, и из него вылетает струя крови, ты едва уклоняешься от потока крови."
        "Большой бык с тяжелым стуком падает на землю. "
        "Третий Воин Ящериц" "Берегись [name]."
        e 9 "А?"
        "Ты отскакиваешь в сторону как раз в тот момент, когда мертвое тело другого быка пролетает мимо и приземляется рядом с быком, которого ты только что убил."
        "Первый Воин Ящериц" "Ты там в порядке, [name]?"
        "Ты падаешь на спину, ошеломленный и страдающий от боли."
        "Ящерицы пытаются помочь тебе встать."
        "Второй Воин Ящериц" "Ты обращался с ними как чемпион, но, боже, они выглядели еще более взбешенными, чем когда-либо."
        "Третий Воин Ящериц" "Да, что ты с ними сделал?"
        e 13 "Я не знаю... Послушай, дай мне немного отдохнуть."
        e 1 "Ребята, вы можете что-нибудь сделать с телами?"
        "Первый Воин Ящериц" "Нет проблем, вдвоем мы сможем навести порядок."
        "ТЫ возвращаешься в лагерь и отдыхаешь."
        "Одна за другой ящерицы передвигают мертвое тело. "
        "Трудно сконцентрироваться на текущей задаче, какая-то часть тебя волнуется, если ящерицы узнают, что ты вступил в контакт с племенем быков."
        "Ты бьешь себя по голове, чтобы сосредоточиться, и обнаруживаешь, что они уже установили третий камень, когда ты ушёл."
        "ТЫ переходишь к последней точке и случайно смотришь на первого убитого тобой быка."
        "Его мертвые глаза смотрят на тебя с такой ненавистью и злобой, что тебе приходится отвести взгляд. "
        "После избавления от последнего тела, ящерицы возвращаются."
        "Первый охранник Ящериц" "Как мы вообще узнаем, работает ли эта штука?"
        "Второй охранник Ящериц" "Эй, о чем ты думал, когда использовал эти камни?"
        e 1 "Я просто думал о том, чтобы держать подальше все, что может навредить племени ящериц и их союзникам."
        "Второй стражник Ящериц" "Хм, давай я кое-что попробую. "
        "Ящерица отходит от группы, подальше от того места, где ты установил первые два рунных камня, и подбирает камешек."
        "Он бросает его к твоим ногам, но камешек ударяется о невидимую стену и падает."
        "Две другие ящерицы потрясены увиденным. "
        e 13 "Думаю, это означает, что он работает."
        "Второй охранник ящериц" "Эй, это довольно весело."
        "Он все время находит камешки, чтобы бросить их в невидимый барьер, просто чтобы посмотреть, какой из них, наконец, пройдет."
        "Ты закатываешь глаза и говоришь им, что пора возвращаться в деревню. "
        scene black with slow_dissolve
        hide red1
        hide red2
        "По пути ящерицы делятся с тобой некоторыми из своих отваров, чтобы удалить бычью кровь с меча и с тебя самого."
        "Его не хватило бы на всех, но, надеюсь, ты чист."
        jump Nauxus_camp_end

    return
label battle_bullcamp_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    if Foe.bullcamp ==0:

        "Поскольку твои реакции замедляются из-за нанесенных тебе ранений, воин-бык не тратит времени на поиски выхода."
        "С ревом бык использует тупой набалдашник своего боевого топора и разбивает его о твое колено."
        show red1 at center with dissolve
        play sound "music/blood.ogg"
        "Ты слышишь резкий треск, за которым следует раскалывающая боль, когда ты теряешь равновесие и падаешь с криком."
        show red2 at center with dissolve
        play sound "music/blood.ogg"
        "Когда ты слабо пытаешься подняться с окровавленными руками, ты оглядываешься назад, чтобы увидеть, как враг радостно улыбается, когда он замахивается своим оружием на твое лицо."
        scene black with vslow_dissolve
        "Все становится черным."
        "{b}{color=#c22719}<ИГРА ОКОНЧЕНА>{/color}"
        menu:
            "Новая игра" if True:
                return
            "Новая игра" if True:
                return
    elif Foe.bullcamp ==1 or Foe.bullcamp ==2:
        "Слишком слабый, чтобы сопротивляться, твой враг бьет тебя прямо в грудь, когда ты чувствуешь, что ветер выбивает из тебя."
        "Ты падаешь на спину, ошеломленный и страдающий от боли."
        show red1 at center with dissolve
        play sound "music/blood.ogg"
        "Когда ты пытаетесь подняться, бык не щадит тебя в этот момент, когда он опускает свой топор на твою грудь."
        "Ты дико кричишь, когда изо рта у тебя течет кровь."
        "Кашляя обильным количеством крови, ты изо всех сил пытаешься дышать."
        show red2 at center with dissolve
        play sound "music/blood.ogg"
        "Бык вытаскивает топор из твоей груди только для того, чтобы обрушить его снова, и снова, и снова."
        "Крики о пощаде постепенно искажаются, когда кровь захлебывается."
        scene black with vslow_dissolve
        "Все становится черным."
        "{b}{color=#c22719}<ИГРА ОКОНЧЕНА>{/color}"
        menu:
            "Новая игра" if True:
                return
            "Новая игра" if True:
                return
    hide bullw with dissolve

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
