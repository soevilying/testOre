label battle_ghost:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 80
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    $ Map.good_battle = True
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    $ Random = renpy.random.randint(1, 10)
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ Battle.holyfcd = 0
    if Random >= 1 and Random <= 4:
        $ Foe.ghost_type = 1
        "Ты чувствуешь, что за тобой кто-то наблюдает. Из ветки на земле вырастает угрожающий коготь."
        "Она одержима! Палка атакует."
    elif Random >= 5 and Random <= 8:
        $ Foe.ghost_type = 2
        "Ты чувствуешь, что за тобой кто-то наблюдает. К тебе катится камень."
        "Он одержим! Камень атакует."
    elif Random >= 9:
        if jane_inv.qty(hp_potion) >2+Items.pbag_n:
            $ Foe.ghost_type = 1
            "Ты чувствуешь, что за тобой кто-то наблюдает. Из ветки на земле вырастает угрожающий коготь."
            "Она одержима! Палка атакует."
        elif True:
            $ Foe.ghost_type = 3
            "Звук звенящего стекла, кажется, следует за тобой сзади."
            "Ты поворачиваешься и видишь красную бутылку с зельем."
            "Прежде чем ты успеваешь среагировать, на бутылке появляется злобное лицо."
            "Красная бутылка атакует!"
    elif True:
        if jane_inv.qty(mp_potion) >2+Items.pbag_n:
            $ Foe.ghost_type = 2
            "Ты чувствуешь, что за тобой кто-то наблюдает. К тебе катится камень."
            "Он одержим! Камень атакует."
        elif True:
            $ Foe.ghost_type = 4
            "Звук звенящего стекла, кажется, следует за тобой сзади."
            "Ты поворачиваешься и видишь синюю бутылку с зельем."
            "Прежде чем ты успеваешь среагировать, на бутылке появляется злобное лицо."
            "Синяя бутылка атакует!"

    stop music








    jump battle_ghost_loop


label battle_ghost_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    if Foe.ghost_type == 1:
        show ghost 01 at center
    elif Foe.ghost_type == 2:
        show ghost 02 at center
    elif Foe.ghost_type == 3:
        show ghost 03 at center
    elif True:
        show ghost 04 at center

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
            $ wolf_hp -= 0
            "Твой меч пронзает призрачного врага, он кажется незатронутым твоей атакой!"
            e 0 "Мои атаки не работают. Неужели это какой-то непобедимый враг?"

        if res == "Подчиниться":
            e "Я больше не могу драться.."
            "Враг слишком силен."
            "Тебя сбивают с ног."
            jump battle_ghost_lose
        if res == "Флиртовать":
            "Ты пытаешься соблазнить призрака, но у него нет тела, чтобы что-то чувствовать."
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
            "Ты отворачиваешься и бежишь так быстро, как только можешь."
            "Враг не преследует тебя."
            if Witer.sleep == 4:
                $ Witer.sleep = 5
            hide screen simple_stats_screen
            hide screen battle_menu
            hide screen battle_skill
            hide screen battle_item
            stop music fadeout 1
            hide ghost 01 with dissolve
            hide ghost 02 with dissolve
            hide ghost 03 with dissolve
            hide ghost 04 with dissolve
            if Foe.ghostforest == 1:
                jump forest_map_1
            elif Foe.ghostforest == 2:
                jump forest_map_2
            elif True:
                jump forest_map_3
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_ghost_win
        $ Random = renpy.random.randint(1, 4)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Появляется призрачная рука и вцепляется в тебя когтями."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(10, 20)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Появляется призрачная рука и вцепляется в тебя когтями."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Мощная сила отбрасывает тебя назад."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(30, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Мощная сила отбрасывает тебя назад."


        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_ghost_win
        elif True:

            jump battle_ghost_win

    elif Zalt.hp <= 0:
        jump battle_ghost_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_ghost_lose
    elif True:
        jump battle_ghost_loop


label battle_ghost_win:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_small_end.ogg" noloop
    pause 1

    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    hide ghost 01 with dissolve
    hide ghost 02 with dissolve
    hide ghost 03 with dissolve
    hide ghost 04 with dissolve
    "Призрачная фигура исчезает в темноте, предмет, которым она обладала, все еще лежит на земле."
    if Foe.ghost_type == 1:
        "Ты получаешь эктоплазму и палочку."
        $ jane_inv_M.take(stick)
    elif Foe.ghost_type == 2:
        "Ты получаешь эктоплазму и камень."
        $ jane_inv_M.take(rock)
    elif Foe.ghost_type == 3:
        "Ты получаешь эктоплазму и зелье здоровья."
        $ jane_inv.take(hp_potion)
    elif True:
        "Ты получаешь эктоплазму и зелье маны."
        $ jane_inv.take(mp_potion)
    "Ты получаешь 80 EXP."
    $ jane_inv_M.take(ectoplasm,1)
    $ Zalt.exp = min(Zalt.exp+80, Zalt.maxlv*250+100*(Zalt.maxlv-1))

    if Foe.ghostforest == 1:
        jump forest_map_1
    elif Foe.ghostforest == 2:
        jump forest_map_2
    elif True:
        jump forest_map_3

    return
label battle_ghost_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    if Foe.ghostwin == True:
        "Вы хотите пропустить сцену?"
        menu:
            "Да" if True:
                hide ghost 01 with dissolve
                hide ghost 02 with dissolve
                hide ghost 03 with dissolve
                hide ghost 04 with dissolve
                scene black with dissolve
                "......"
                if Foe.ghostforest == 1:
                    scene forest 1n with slow_dissolve
                elif Foe.ghostforest == 2:
                    scene forest 2n with slow_dissolve
                elif True:
                    scene forest 3n with slow_dissolve
                if jane_inv.qty(coin) != None:
                    $ qty = int(jane_inv.qty(coin)*0.2)
                    $ jane_inv.drop(coin,qty)
                    "Когда ты просыпаешься, обнаруживаешь, что потерял <[qty]> монет. Хорошо, что у тебя все еще есть набедренная повязка."
                $ Zalt.lust = 0
                $ Zalt.hp = 1
                $ Zalt.cor = min(Zalt.cor+1,100)
                $ Time.hours = Time.hours+1
                if Foe.ghostforest == 1:
                    jump forest_map_1
                elif Foe.ghostforest == 2:
                    jump forest_map_2
                elif True:
                    jump forest_map_3
            "Нет" if True:
                pass
    "Фантом стреляет фиолетовой молнией и поражает тебя прямо в грудь."
    hide ghost 01 with dissolve
    hide ghost 02 with dissolve
    hide ghost 03 with dissolve
    hide ghost 04 with dissolve
    e 0 "А-а-а!"
    "Ты не можешь пошевелить своим телом! Как тряпичная кукла, твое тело падает на землю."
    "Жгучая боль в груди обжигает, как горячий расплавленный металл, просачивающийся в тебя."
    "Слабый шепот становится громче в твоих ушах, но вокруг тебя никого нет."
    "Затем он говорит."
    "Призрак" "О, черт возьми, да. Я забыл, каково это - иметь тело."
    e 0 "Кто ты? Убирайся из моей головы!"
    "Призрак" "Заткнись, ты, маленькое пятно от мочи. Это тело мое."
    "Ты пытаешься пошевелить пальцами, но что-то не так."
    "Твое тело начинает садиться, и твоя шерсть чернеет, как сама ночь."
    "Вокруг твоих предплечий образуются фиолетовые линии, и все тело излучает пугающую ауру."
    "Твои глаза светятся навязчивым синим цветом, а зрачки становятся красными, как кровь."
    "Призрак" "Это больше похоже на правду."
    "Слова, которые слетают с твоих уст, звучат как твой голос, но они не твои."
    e 0 "Мое тело! Я не могу его контролировать."
    "Твои руки начинают раскачиваться, как будто призрак пытается привыкнуть к тому, как управлять тобой."
    "С каждым взмахом ты все еще можешь чувствовать каждое движение суставов. "
    "Призрак" "У тебя довольно горячее тело с пятнами мочи. Ммм, да, посмотри на эту грудь."
    "Призрак" "Я не могу дождаться, чтобы проверить это и трахнуть всех твоих друзей."
    e 0 "Нет! Убирайся из моего тела, ублюдок."
    "Призрак" "Что еще более важно, ты сам все увидишь."
    "Контролируя твои руки, он тянется к твоей набедренной повязке."
    e 0 "Остановись!"
    scene black
    show ghost lose1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos -0.3 ypos 0
        zoom 1.5
        linear 20.0 xpos 0 ypos -1000
    "Ты пытаешься вырвать контроль у призрака, но это не работает."
    "Он стягивает с тебя набедренную повязку, позволяя твоему твердому члену шлепнуться тебе на бедро."
    show ghost lose1 with slow_dissolve:
        xpos 0.19 ypos -0.05
        zoom 0.86
    "Призрак" "Да, это будет просто замечательно."
    "Он обхватывает твой член и сжимает."
    e 0 "Ах!"
    "Ты это чувствуешь."
    "Крепкая хватка вокруг ствола и жар твоего пульсирующего члена."
    "Призрак манипулирует твоей рукой, чтобы начать ласкать твердый член."
    "Энергично потирая свой член, твое тело содрогается и стонет."
    "Глубокий и отвратительный стон."
    "Ты подносишь другую руку ко рту и жадно сосешь первые три пальца."
    e 0 "Стой, стой, стой! Нет."
    "Призрак продолжает игнорировать твои крики и жадно облизывает твои пальцы."
    "Твой язык вытягивается, как ящерица, и намыливает пальцы в слюне."
    "Призрак" "Да, все смазано для главного события."
    "Призрак" "Мне нужно стараться, чтобы стать самой большой шлюхой в королевстве."
    "Ты толкаешь бедра вперед и поднимаешь ноги, чтобы обнажить свою сморщенную дырочку."
    e 0 "Нет! А-а-а!"
    "Вместе вы оба стонете в унисон, когда засовываете все три пальца в свою дырочку."
    "Все твое тело содрогается, а член дико пульсирует в твоих руках."
    show ghost lose2 with slow_dissolve:
        xpos 0.19 ypos -0.05
        zoom 0.86
    "Призрак" "О, черт возьми, да! Я хочу засунуть столько же членов в свою задницу."
    "Призрак "" Ты можешь это принять, не так ли?"
    "Твой единственный ответ - жалобный стон."
    "Это слишком, как твои пальцы заполняют твои внутренности, практически разрывая тебе дырку, когда твои пальцы безжалостно трахают твою задницу."
    "Другим большим пальцем ты ласкаешь головку своего члена."
    "Тяжело дыша, поток предварительной спермы стекает с кончика и вниз по всему бедру."
    "Ты яростно дергаешь своим членом, создавая давление в своих яйцах."
    "Остановившись как раз тогда, когда ты находишься на грани кульминации."
    "Поддразнивание и окантовка заставляют вас стонать от удовольствия."
    "Призрак" "Черт, я хочу пойти глубже!"
    "Ты задерживаешь дыхание, когда пальцы погружаются еще глубже и ненадолго щекочут твою простату."
    "Призрак" "Да, черт возьми!"
    "Еще больше пре хлещет из твоего члена."
    "Все твое тело горит, и твоя задница болит, когда призрак заставляет тебя трахать себя пальцами все быстрее и быстрее."
    "Стенки твоей жопы сжимают твои влажные пальцы, засасывая их глубже внутрь тебя."
    "С богатым потоком пре, выходящим из вашего члена, твоя рука становится влажной и скользкой."
    "Ты дергаешь себя так, как никогда раньше не дергал."
    "Влага заполняет твою дырочку от траха пальцем, каждый толчок приближает тебя к окончанию."
    "Тяжелые штаны заполняют ночь, и ты скулишь, как щенок."
    "Твое сопротивление призраку, овладевающему тобой, ослабевает, когда ты поддаешься потребности в освобождении."
    with flashbulb
    show ghost lose3 with slow_dissolve:
        xpos 0.19 ypos -0.05
        zoom 0.86
    "С оглушительным воем твои яйца втягиваются, и член взрывает горячую струю спермы по всей траве."
    "Призрак" "Черт!"
    "Оргазм кажется интенсивным, ты не можешь держать глаза открытыми, продолжая стрелять потоками спермы по всему месту."
    show ghost lose4 with slow_dissolve:
        xpos 0.19 ypos -0.05
        zoom 0.86
    "Призрак" "Бухехехехе."
    "Ты сидишь на своем месте измученный и весь в сперме."
    "Часть его стекает на твои пальцы и входит в твою растянутую дырочку."
    "В своем сердце ты чувствуешь самоуверенное удовлетворение, которое испытывает призрак."
    "Его похотливая улыбка появляется на твоем лице, и это вызывает у тебя отвращение до глубины души. "
    e 0 "ТЫ..."
    hide ghost lose4 with slow_dissolve
    "Ты кипишь от ярости!"
    e 0 "ТЫ... УБИРАЙСЯ ИЗ МОЕГО ТЕЛА!"
    with flashbulb
    "Призрак" "Какого черта?"
    "Пурпурное свечение вокруг твоего тела усиливается и ослабевает. "
    "Призрак" "Нет! Нет! Это мое тело!"
    "Благодаря чистой силе воли, власть призрака над тобой ослабевает, и твое тело падает на землю."
    "Ты видишь, как призрачное видение съеживается и сжимается в воздухе."
    "Призрак" "Пошел ты, парень! Я вернусь!"
    "Призрак" "Если не я, то один из нас!"
    "Призрак" "Ты пожалеешь о том дне, когда попытаешься пойти против нас!"
    "Призрак превращается в облачко фиолетового дыма и залетает в твой кошелек, несколько монет оживают, откатываются от тебя и исчезают в темноте."
    "Тьфу."
    "Ты падаешь в обморок."
    if Foe.ghostforest == 1:
        scene forest 1n with slow_dissolve
    elif Foe.ghostforest == 2:
        scene forest 2n with slow_dissolve
    elif True:
        scene forest 3n with slow_dissolve
    $ Foe.ghostwin = True
    if jane_inv.qty(coin) != None:
        $ qty = int(jane_inv.qty(coin)*0.2)
        $ jane_inv.drop(coin,qty)
        "Когда ты просыпаешься, обнаруживаешь, что потерял <[qty]> монет. Хорошо, что у тебя все еще есть набедренная повязка."
    $ Zalt.lust = 0
    $ Zalt.hp = 1
    $ Zalt.cor = min(Zalt.cor+1,100)
    $ persistent.CG_ghost_lose = True
    $ Time.hours = Time.hours+1
    if Foe.ghostforest == 1:
        jump forest_map_1
    elif Foe.ghostforest == 2:
        jump forest_map_2
    elif True:
        jump forest_map_3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
