label battle_bull:
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
    scene forest 3
    stop music
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')






    "Массивная тень преграждает тебе путь."
    "Огромный бык появляется из тумана, размахивая топором."
    "Бык-воин" "Чужак! Я уничтожу тебя!"
    "Бык замахивается на тебя своим оружием."
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    jump battle_bull_loop


label battle_bull_loop:



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
            $ Random = renpy.random.randint(1, 3)
            $ Battle.holyfcd = 3
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
            "*глоток* 5hp восстановлено"

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
                    "Ты вытаскиваешь меч и бросаешься в атаку.\n{b}{color=#ffd65c}(Критический урон! -[qty]hp){/color}"

        if res == "Подчиниться":
            e "Я больше не могу драться.."
            "Враг слишком силен."
            "Тебя сбивают с ног."
            jump battle_bull_lose
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
                "ТЫ дразнишь своего противника, атакуя его в лоб."
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
                "Его воля к борьбе сломлена, он хочет только доставить тебе удовольствие."
                menu:
                    "Трахнуть его" if Zalt.lust >=40:
                        jump battle_bull_sex
                    "Уйти" if True:
                        "Ты решил оставить быка в покое."
                        "Когда ты уходишь, ты слышишь похотливые стоны быка и хлюпающий звук, когда кто-то дрочит."
                        "Ты получаешь 1 пучок меха и 100 EXP."
                        $ jane_inv_M.take(bull_fur)
                        $ Zalt.exp = min(Zalt.exp+100, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                        jump forest_map_3
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
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item
                hide slime
                jump forest_map
            elif True:
                "Побег не удался!"
                pass
        elif True:
            pass

        if wolf_hp <= 0:
            jump battle_bull_win
        $ Random = renpy.random.randint(1, 6)
        if Random <= 3:
            $ wolf_damage = renpy.random.randint(15, 30)
            $ Zalt.lust += wolf_damage
            "Мускус воина-быка землистый и мощный."
            "Твоя промежность нагревается."
            "Бык-воин" "Тебе это нравится, хммм? Подчинись сейчас же, и я дам тебе кое-что веселое!"
        elif True:
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
            jump battle_bull_win
        elif True:

            jump battle_bull_win

    elif Zalt.hp <= 0:
        "Кулак вражеского быка с силой ударяет тебя в живот."
        "Твое тело на секунду сжимается, и ты остаешься шататься на ногах."
        jump battle_bull_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_bull_lose
    elif True:
        jump battle_bull_loop


label battle_bull_win:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_small_end.ogg" noloop
    pause 1
    "Бык-воин" "Эх...!"
    hide bullw with slow_dissolve

    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    "Ты нокаутируешь быка прикладом своего оружия."
    "Ты срезал ему волосы своим мечом."
    "Ты получаешь 1 пучок меха и 100 EXP."
    $ jane_inv_M.take(bull_fur)
    $ Zalt.exp = min(Zalt.exp+100, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    jump forest_map_3

    return
label battle_bull_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    hide bullw with dissolve
    if Foe.bullw == True:
        "Вы хотите пропустить сцену?"
        menu:
            "Да" if True:
                scene black with dissolve
                "......"
                scene forest 3 with dissolve
                "Когда ты просыпаешься снова, то обнаруживаешь, что несколько монет отсутствуют."
                "Ты мрачно улыбаешься, радуясь, что все еще жив."
                "Приведя себя в порядок, ты начинаешь все сначала."
                if jane_inv.qty(coin) != None:
                    $ qty = int(jane_inv.qty(coin)*0.2)
                    $ jane_inv.drop(coin,qty)
                $ Zalt.lust = 0
                $ Zalt.hp = 1
                jump forest_map_3
            "Нет" if True:
                pass
    elif True:
        pass
    "Ты чувствуешь, как бык крепко хватает тебя за голову и разворачивает, чтобы вы не смотрели ему в лицо."
    "Он просовывает руки тебе под правую подмышку и тянет тебя на землю."
    "Его массивное тело падает с тяжелым стуком."
    "Он раздвигает одну из твоих ног над своим бедром, давая ему полный обзор тебя."
    "Бык-воин" "Ты так хорошо пахнешь волком."
    "[name]" "Нхх, отпусти меня!"
    "Его мясистые пальцы обхватывают твою шею."
    "Ты все еще можешь говорить, но ты знаешь, что он тебе позволяет."
    "Если он захочет, он может сломать тебя прямо здесь и сейчас."
    "Бык-воин" "Ш-ш-ш, у меня так давно не было хорошего траха."
    "Бык-воин" "Будь хорошим щенком и дай мне повеселиться."
    "Он отпускает твою шею и прижимается носом к твоей шее."
    "Твое лицо так близко, что ты чувствуешь его горячее дыхание, щекочущее твою шею и поднимающееся к уху."
    "Бык кусает тебя за ухо, и ты стонешь."
    "[name]" "Нет.... Я не должен...."
    "Мускус, который он излучает, такой острый, что от его запаха щиплет нос."
    "Ты пытаешься сопротивляться, но твоё тело предает тебя."
    "Твоя промежность становится теплее и тверже с каждой минутой."
    "Бык-воин" "Давай устроимся поудобнее."
    scene black
    show bull lose1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos 0.1 ypos 0
        zoom 1.2
        linear 100.0 xpos -50 ypos -800
    "Бык срывает с тебя набедренную повязку, освобождая твой стояк."
    "Твой член горяч и лихорадочно пульсирует,возбужденный мощным запахом быка."
    "Он хватает твое мужское достоинство и крепко сжимает."
    "Он кладет большой палец на твой член и вдавливает его в твою щель."
    e "Что ты ... Ай!"
    show bull lose1 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "Твои ноги пытаются извиваться, но их удерживают руки быка."
    "Бык-воин" "Ха! Я люблю, когда ты кричишь."
    show bull lose2 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "Твои глаза расширяются от шока, когда член быка выскальзывает из набедренной повязки и поднимается во весь свой обхват."
    "Бусинки преякулята каскадом падают с кончика бычьего члена."
    "Он хватается за свой член и за твой, как за вязанку хвороста."
    "Бык-воин" "Посмотри на все это мясо."
    e "Что это за хрень?"
    "Бык-воин" "Посмотри хорошенько, маленький волк, потому что он скоро будет в тебе."
    e "Нет, нет. Я не могу вместить все это!"
    "Бык-воин" "Я сделаю его подходящим."
    "Бык ослабляет хватку на твоём члене и трясет своим истекающим членом вокруг твоей дырочки."
    "Его движения неуклюжи, и его пре не помогает."
    "Каждые несколько секунд вы чувствуете, как твоя промежность ударяется о мокрый член быка, прежде чем он ускользнет."
    "Бык-воин" "К черту все это!"
    with flashbulb
    show bull lose3 with dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "Он держит свой член прямо над твоей дырочкой и толкает внутрь."
    "Твоя задница дергается и горит."
    e "ЧЕ-А-А! Он слишком большой!"
    "Бык-воин" "Черт, твоя дырка тугая."
    "Ты чувствуешь огромный взрыв боли, как будто все твое тело разрывается надвое."
    "Его член так глубоко внутри тебя, что ты чувствуешь, как бычьи яйца размером с яблоко шлепают по твоей заднице."
    "Бык тяжело дышит над твоим плечом."
    "Его член продолжает фонтанировать спермой внутри тебя."
    "Бык-воин" "ОООО да, обними мой член своей дырочкой."
    "Он целует тебя, подавляя своим толстым языком."
    show bull lose4 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "Боль, которую вы чувствовали, уступает место волнам удовольствия."
    "Все твое тело расслабляется, позволяя члену быка легко скользить в тебе."
    "Он вытаскивает свой член наполовину и таранит весь ствол обратно в тебя."
    "Сильные руки быка удерживают тебя на месте, когда он начинает вращать бедрами."
    e "А-а-а."
    "С каждым толчком он стреляет все больше пре внутрь тебя."
    "Его хватка так сильна, что ты даже не можешь пошевелиться."
    with flashbulb
    "Он скачет на твоей заднице все быстрее и быстрее."
    "Бык-воин" "Да, сожми мой член своей тугой попкой!"
    "Ты извергаешь пре из своего все еще пульсирующего члена по всему животу."
    "Ты чувствуешь, что твое тело больше не твое, а его."
    "Не успеешь оглянуться, как ты уже оседлаешь массивную булаву быка.,{p}желая большего, желая, чтобы он кончил в тебя и завоевал тебя."
    e "Черт! У меня внутри все горит!"
    "Твои мольбы остаются незамеченными."
    "Бык продолжает трахать тебя все сильнее и сильнее."
    "Он смотрит на тебя одним открытым глазом, он ухмыляется, наблюдая, как твое лицо искажается в разных выражениях похоти."
    "Твой член мучительно болит, отчаянно желая освободить свой груз."
    e "КККК - КОНЧАЮ!"
    with flashbulb
    show bull lose5 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "Горячая струя спермы брызжет из твоего члена."
    "Покрывая травянистое поле своим семенем."
    "Часть его потекла по яйцам быка."
    "Бык-воин" "Черт! Я больше не могу сдерживаться!"
    "Темп быка начинает замедляться."
    "Его яйца прижимаются вплотную к твоей заднице, и ты чувствуешь, как и без того толстый ствол расширяется внутри твоей задницы."
    with flashbulb
    with flashbulb
    show bull lose6 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "Бык выгружает свою сперму внутрь тебя."
    "Когда ты кричишь от удовольствия, твой член снова извергается и выстреливает спермой на морду быка."
    "Потоки спермы наполняют тебя до предела."
    "Твоя попытка удержать все это внутри, но это слишком много спермы."
    "Потоки спермы вытекают из твоей дырочки, как переполненная чашка."
    "Тяжело дыша, бык целует тебя в щеки и стаскивает со своего члена."
    "Следы спермы вытекают из твоей задницы и брызгают на член быка."
    "Он бросает тебя на землю и встает."
    hide bull lose6 with slow_dissolve
    scene forest 3 with slow_dissolve
    "Все болит, особенно твоя дергающаяся задница."
    "Твое сердце болит от всевозможных эмоций,гнева,унижения,похоти, но в основном ты чувствуешь пустоту без члена быка."
    "Большой бык наступает тебе на спину, его член все еще капает спермой на твое обнаженное тело."
    "Он наклоняется над тобой и засовывает средний палец тебе в задницу."
    "Ты громко визжишь."
    "Он вытащил палец с каплей спермы на нем и облизал его дочиста."
    "Бык-воин" "Это был хороший трах."
    "Бык-воин" "Вернись снова волк, я с удовольствием надеру тебе задницу."
    "Ты слышишь, как он уходит, но слишком устал, чтобы догнать его."
    "Твои веки становятся тяжелыми..."
    scene black with vslow_dissolve
    "...{w}..."
    scene forest 3 with vslow_dissolve
    "Когда ты просыпаешься снова, ты обнаруживаешь, что несколько монет отсутствуют."
    "Ты мрачно улыбаешься, радуясь, что все еще жив."
    "Приведя себя в порядок, ты начинаешь все сначала."
    $ Foe.bullw = True
    if jane_inv.qty(coin) != None:
        $ qty = int(jane_inv.qty(coin)*0.2)
        $ jane_inv.drop(coin,qty)
    $ Zalt.lust = 0
    $ Zalt.hp = 1
    $ persistent.CG_bull_lose = True
    jump forest_map_3
    return
label battle_bull_sex:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    hide bullw with dissolve
    "Ты снимаешь набедренную повязку, позволяя своему пухлому полутвердому члену покачиваться у твоих бедер."
    "Бык подползает к тебе и тычется носом в твою мошонку."
    "Его горячее дыхание приятно ощущается на твоем члене."
    "Бычий воин" "Завоюй меня... чемпион."
    "Все, что ему нужно, - это твое мужское достоинство внутри него, его голод по тебе горит в его глазах."
    "Ты позволяешь ему поклоняться твоей мужественности."
    "От прикосновения к твоим яйцам бык жадно обхватывает их."
    "Нежные поглаживания его языка так приятны, что твой член поднимается на всю длину."
    "[name]" "Дай мне эту задницу!"
    scene black
    show bull win1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos 0 ypos 0
        zoom 1.5
        linear 20.0 xpos 0 ypos -1000

    "Ты толкаешь быка в плечо."
    "Его массивное тело падает на землю с легкостью, словно подушка."
    "То, как вздымаются и опускаются его здоровенная грудь, говорит о том, что он тяжело дышит."
    "Его твердый член крепко прижимается к его прессу."
    "Его дубина, как размер, может сбить кого - то с ног, если его ударить с достаточной силой."
    show bull win1 with slow_dissolve:
        xpos 0.2 ypos -0.13
        zoom 0.86
    "[name]" "Ну,чего же ты ждешь?"
    "[name]" "Я сказал, дай мне свою задницу!"
    "Бык сглотнул, но повиновался."
    "Он высоко поднимает ноги, пока его дырочка не задевает твою мошонку."
    "[name]" "Мне нравится то, что я вижу."
    "Ты подходишь к нему и держишь его за бедра, положив свой твердый член на его дырочку."
    "Твой член всего в нескольких дюймах от того, чтобы коснуться бронзовых шаров быка."
    "[name]" "Да, тебе это нравится, не так ли, бык?"
    "Бык-воин" "Да... пожалуйста... он такой теплый... Ты нужен мне внутри."
    "[name]" "Ты ведь девственник на задок, не так ли?"
    "[name]" "Я могу почувствовать, как туго натянута твоя дырочка, просто потершись о нее."
    "Бык задыхается, он делает серьезное лицо, но его пульсирующий член выдает его."
    "[name]" "Бери, большой мальчик!"
    "Ты прижимаешь свою головку к его дырочке. Как только наконечник ломается, бык кричит."
    show bull win2 with slow_dissolve:
        xpos 0.2 ypos -0.13
        zoom 0.86
    "Бык-воин" "А-а-а! Да! Колоти меня своим членом!"
    "Ты застигнут врасплох внезапным изменением настроем быка, но какая-то часть теяб тоже чувствует прилив энергии."
    "[name]" "Да! Возьми его, ты, мускулистая задница."
    "Бык, как по команде, расслабляет мышцы вокруг ануса, позволяя тебе войти глубже."
    with flashbulb
    show bull win3 with dissolve:
        xpos 0.2 ypos -0.13
        zoom 0.86
    "Бык стонет и задыхается, когда ты вонзаешь в него остальную часть своего члена."
    "Его лицо тает, чувствуя твой горячий член внутри себя."
    "Ты рычишь и вскидываешь голову."
    "Твой член покалывает, когда мышцы ануса быка сжимаются вокруг ствола."
    "Бык-воин" "Да! Еще! Еще!"
    show bull win4 with slow_dissolve:
        xpos 0.2 ypos -0.13
        zoom 0.86

    "Потянув свой член наполовину, ты вонзаешь его так сильно, как только можешь."
    "Бык-воин" "Сильнее! Да, не медли, чужак!"
    "Ты вращаешь бедрами, пока не достигаешь знакомого ритма."
    "Каждый толчок твоего члена посылает сигналы экстаза по всему телу."
    "Ты чувствуешь, как каждая клеточка твоего тела превращается в масло."
    "Когда ты трахаешь быка, твой язык вываливается, когда ты тяжело дышишь."
    "Вид перед тобой тоже не так уж плох, каждый раз, когда ты хлопаешь своим членом внутри быка, его грудь подрагивают."
    "Бык-воин" "Трахни меня,да,оххх."
    "Оба ваших тела сгорают от страсти."
    "Похотливый бык брызгает пре по всему лицу и груди."
    "Ты также можешь почувствовать, как ваши пределы достигают своего пика."
    if Zalt.end <= 6:
        "[name]" "РАРРГГГХХХ!"
        "Ты больше не можешь сдерживаться."
        with flashbulb
        show bull win5a with slow_dissolve:
            xpos 0.2 ypos -0.13
            zoom 0.86
        "Твой член извергает свой груз глубоко внутрь быка, каждая часть тела напрягается и онемевает на несколько минут."
        "Потоки горячей спермы заполняют быка."
        "Бык-воин" "Му!"
        hide bull win5a with dissolve
        scene forest 3 with dissolve
        "Тяжело дыша, ты вытаскиваешь свой мягкий член из быка."
        "Струйка спермы тянется вдоль, соединяя твою головку с его дырочкой."
        "Бык не способен достичь кульминации."
        "Он переключает свое внимание на собственный член и начинает дрочить."
        "Если ты рискнешь уйти, он будет слишком занят, чтобы доставлять тебе неприятности. "
        "Ты получаешь 1 пучок меха и 100 EXP."
        $ Zalt.lust = 0
        $ Foe.bullwin = True
        $ jane_inv_M.take(bull_fur)
        $ persistent.CG_bull_winA = True
        $ Zalt.exp = min(Zalt.exp+100, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        jump forest_map_3
    elif True:
        "Бык-воин" "Муууууууууууууу!"
        with flashbulb
        show bull win5b with slow_dissolve:
            xpos 0.2 ypos -0.13
            zoom 0.86
        "Бык издает сокрушительный рев, когда кончает на себя."
        "Он взрывает густую сливочную сперму по всему лицу."
        "Его мускусный аромат наполняет твои ноздри."
        "Его тело содрогается, когда он истекает спермой по всему телу."
        "[name]" "Черт!"
        "Спазматические движения его ануса сжимают хватку вокруг твоего члена."
        "Ты больше не можешь сдерживаться!"
        "[name]" "Я кончаю!"
        with flashbulb
        show bull win6b with vslow_dissolve:
            xpos 0.2 ypos -0.13
            zoom 0.86
        "Твои движения начинают замедляться до полной остановки."
        "Сжимая бедра быка еще крепче, твой член извергает свой груз глубоко внутрь быка."
        "Каждая часть твоего тела напрягается и онемевает на несколько минут."
        "Бык-воин" "ЧЕРТ!"
        "Внезапный взрыв спермы в его прямой кишке приводит в действие бычий член."
        "Он снова кончает на себя. Некоторые из них попадают ему в глаз, заставляя его рычать от боли."
        "Тяжело дыша, ты вытаскиваешь свой мягкий член из дырки быка, струйка спермы тянется вдоль, соединяя твою головку с его дырочкой."
        hide bull win5a with dissolve
        scene forest 3 with dissolve
        "Бык слишком устал и падает."
        "Ты пользуешься шансом уйти."
        "В ближайшее время он не доставит тебе неприятностей."
        "Ты получаешь 1 пучок меха и 100 EXP."
        $ Zalt.lust = 0
        $ Foe.bullwin = True
        $ jane_inv_M.take(bull_fur)
        $ persistent.CG_bull_winB = True
        $ Zalt.exp = min(Zalt.exp+100, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        jump forest_map_3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
