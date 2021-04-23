label battle_gargoyle:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 250
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 99

    $ Map.good_battle = True
    $ Battle.holyfcd = 0
    stop Chan1
    stop Chan2
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    stop music
    scene caveruin 1n with slow_dissolve


label battle_gargoyle_loop:



    show screen simple_stats_screen
    show screen battle_menu
    show gargoyle at center
    play music "<loop 4.6903>music/forest_fight_small.ogg"





    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Святой Кулак":
            $ red_damage = renpy.random.randint(int((Zalt.MATK*2)+5), int((Zalt.MATK*3)+10))
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
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-40), Zalt.ATK-10)
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
            jump battle_gargoyle_lose
        if res == "Флиртовать":
            $ Random = renpy.random.randint(1, 5)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "Ты хвалишь горгулью за ее горячие, хорошо вырезанные мышцы."
                "Горгулья качает головой, но вы замечаете, что его дыхание становится более поверхностным и быстрым."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "Ты проскальзываешь ближе к горгулье и прижимаешься к нему всем телом, твоя выпуклость трется о промежность горгульи."
                "Горгулья рычит и сжимает свою набедренную повязку, очертания эрекции горгульи становятся более заметными."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "Ты посылаешь воздушный поцелуй вражеской горгулье."
                "Горгулья рычит и сжимает свою набедренную повязку, очертания эрекции горгульи становятся более заметными."
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "Ты хвалишь горгулью за ее горячие, хорошо вырезанные мышцы."
                    "Горгулья игнорирует твои движения и наносит мощный удар."
                elif Random == 2:
                    "Ты проскальзываешь ближе к горгулье и прижимаешься к нему всем телом, твоя выпуклость трется о промежность горгульи."
                    "Горгулья в ярости! Он хватает тебя за руку и с силой швыряет о стену."
                elif True:
                    "Ты посылаешь воздушный поцелуй вражеской горгулье. "
                    "Горгулья ничего не чувствует и издает пронзительный визг. "
            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                if Map.caj3g == 1:
                    jump battle_gargoyle_sex0
                if Map.ca18garg == 0 and Map.ca3garg == False:
                    jump battle_gargoyle_win
                label battle_gargoyle_sex0:
                    "Горгулья медленно приближается к тебе."
                    "Его лицо покраснело, и его твердый член выскользнул из щели, потянув за собой длинный поток предварительной спермы."
                    "Ты держишь свой меч наготове к следующей атаке."
                    "Затем с громким стуком горгулья садится на все четыре."
                    e 0 "Что это?"
                    "Горгулья" "Ты победил... ты...сильнее... дай... милосердие... дай... тепло."
                    "Похотливая горгулья поворачивается и подставляет тебе свою задницу."
                    menu:
                        "Спариться с ним" if True:
                            if persistent.CG_gargoyle_win == True:
                                $ persistent.CG_gargoyle_win = False
                            jump battle_gargoyle_sex
                        "Уйти" if True:
                            if Map.caj3g == 1:
                                "Ты получаешь блестящий мох и 300 EXP."
                                $ jane_inv_M.take(moss)
                                $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                                $ Map.caj3g = 0
                                jump Cave_map_ferryman
                            if Map.ca3garg:
                                "Земля была усыпана блестящим мхом, упавшим с горгульи."
                                "Ты думаешь, что он будет полезен."
                                "Ты получаешь блестящий мох и 300 EXP."
                                $ jane_inv_M.take(moss)
                                $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                                $ Map.ca3garg = False
                                scene cave 1 with dissolve
                                "Теперь ты можешь спокойно прочитать остальную часть текста."
                                "Руководствуясь мужеством наших павших, которые боролись за свою свободу в Царстве Аплистии."
                                "Остальная часть текста не читается."
                                e 13 "Королевство? Это место не похоже на то, что оно было заселено так давно."
                                e 1 "Может быть, Фло там?"
                                $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
                                $ PPEXP = 50*Zalt.A_exp_lv
                                "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                                $ Map.ca3 = 4
                                jump Cave_map
                            jump Cave_map
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
            "Ты убегаешь."
            hide screen simple_stats_screen
            hide screen battle_menu
            hide screen battle_skill
            hide screen battle_item
            if Map.caj3g == 1:
                jump Cave_map_ferryman
            jump Cave_map
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_gargoyle_win
        $ Random = renpy.random.randint(1, 5)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Горгулья ударяет кулаком в землю, высокие торчащие каменные шипы вырастают из земли и врезаются в тебя."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(25, 45)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Горгулья ударяет кулаком в землю, высокие торчащие каменные шипы вырастают из земли и врезаются в тебя."
        elif Random == 2:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Горгулья произносит заклинание на неизвестном языке."
                "Каменный шип пронзает твою тень, ты застигнут врасплох, и атака пронзает твою руку. "
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 45)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Горгулья произносит заклинание на неизвестном языке."
                "Каменный шип пронзает твою тень, ты застигнут врасплох, и атака пронзает твою руку. "
        elif Random == 3 or Random == 4:
            "Горгулья топает ногами, и из-под нее расползается зеленый мох."
            "Голубые цветы мгновенно появляются на вершине мха."
            "Ты поднимаешь меч перед лицом, готовый защититься от того, что произойдет дальше."
            "Цветы взрываются, и воздух наполняется мощным и опьяняюще сладким запахом."
            "Запах возбуждает тебя, и ты чувствуешь, как горят твои щеки. "
            $ wolf_damage = renpy.random.randint(6, 12)
            $ Zalt.lust += wolf_damage
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Враг прыгает в воздух и наносит мощный удар, который пробивает твою защиту."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 45)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Враг прыгает в воздух и наносит мощный удар, который пробивает твою защиту."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1





    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_gargoyle_win
        elif True:

            jump battle_gargoyle_win

    elif Zalt.hp <= 0:
        jump battle_gargoyle_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_gargoyle_lose
    elif True:
        jump battle_gargoyle_loop


label battle_gargoyle_win:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_small_end.ogg" noloop
    pause 1
    hide gargoyle with slow_dissolve

    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    if Map.caj3g == 1:
        "Горгулья отшатывается назад и падает на колени."
        "Тяжело дыша, горгулья рассекает землю, разбрызгивая грязь и пыль, чтобы заслонить тебе обзор."
        "Как только он очистится, горгульи нет."
        "Горгулья сбежала."
        "Только земля была усыпана блестящим мхом, упавшим с горгульи."
        "Ты думаешь, что он будет полезен."
        "Ты получаешь блестящий мох и 300 EXP."
        $ jane_inv_M.take(moss)
        $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        $ Map.caj3g = 0
        jump Cave_map_ferryman
    if Map.ca18garg0:
        if Map.ca18garg == 0:
            $ Map.ca18garg = Map.ca18garg + 1
            $ wolf_hp = wolf_max_hp
            $ wolf_lust = 0
            "Поражение первой горгульи приводит в ярость вторую. Он налетает и вцепляется когтями тебе в грудь."
            "Ты успешно блокируешь атаку своим мечом."
            e 0 "Принеси!"
            jump battle_gargoyle_loop
        if Map.ca18garg == 1:
            "Ты получаешь два блестящих мха и 600 EXP."
            $ jane_inv_M.take(moss,2)
            $ Zalt.exp = min(Zalt.exp+600, Zalt.maxlv*250+100*(Zalt.maxlv-1))
            $ Map.ca18 = 4
            $ Map.ca19 =1

            $ Zalt.A_exp = Zalt.A_exp + 100*Zalt.A_exp_lv
            $ PPEXP = 100*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            jump Cave_map

    $ jane_inv_M.take(moss)
    $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    if Map.ca3garg:
        $ Map.ca3garg = False
        scene cave 1 with dissolve
        "Теперь ты можешь спокойно прочитать остальную часть текста."
        "Руководствуясь мужеством наших павших, которые боролись за свою свободу в Царстве Аплистии."
        "Остальная часть текста не читается."
        e 13 "Королевство? Это место не похоже на то, что оно было заселено так давно."
        e 1 "Может быть, Фло там?"
        $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
        $ PPEXP = 50*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.ca3 = 4
        jump Cave_map
    jump Cave_map
    return

label battle_gargoyle_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    hide gargoyle with dissolve

    stop music
    if persistent.CG_gargoyle_lose == True:
        "Вы хотите пропустить сцену?"
        menu:
            "Да" if True:
                "Горгулья уходит и оставляет тебя на твоем месте до конца ночи."
                "Твоя единственная компания-это разные жуки, которые ползают вокруг, иногда даже ползают по твоему лицу, единственное утешение в том, что вы ничего не чувствуете."
                "Как только окаменение проходит, и ты падаешь на землю измученный и голый."
                "Ты берешь свое снаряжение и выбираешься из пещеры."
                "Спасибо, что ты выжил."

                if Time.hours >=6:
                    $ Time.days = Time.days+1
                    $ Time.hours = 6
                    $ Time.mins = 30
                elif True:
                    $ Time.hours = 6
                    $ Time.mins = 30

                $ Zalt.hp = min(Zalt.hp+Zalt.maxhp/2, Zalt.maxhp)
                $ Zalt.mp = min(Zalt.mp+Zalt.maxmp/2, Zalt.maxmp)
                if jane_inv.qty(coin) != None:
                    $ qty = int(jane_inv.qty(coin)*0.2)
                    $ jane_inv.drop(coin,qty)
                $ Zalt.cor = min(Zalt.cor+2,100)
                $ Zalt.Dungeon_leave = True
                if Map.caj3g == 1:
                    $ Map.caj3g = 0
                    jump Cave_map_ferryman
                if Map.ca3garg:
                    $ Map.ca3garg = False
                if Map.ca18garg0:
                    $ Map.ca18garg0 = False


                jump Cave_map
            "Нет" if True:
                pass
    "Горгулья пропускает удар и случайно падает на землю."
    "Ты обрушиваешь свой меч на голову существа, но земляной столб вырывается из земли и выбивает меч из твоих рук."
    hide gargoyle with dissolve
    "Потеряв равновесие, ты падаешь назад; горгулья прижимает тебя к земле."
    "Его руки крепко сжимают твои плечи, когда он кружит тебя по земле. "
    "Каждый раз, когда ты ударяешься о землю, все больше и больше твоей энергии уходит, оставляя тебя ошеломленным."
    "Последний бросок заставляет тебя упасть на землю, а горгулья прижимает к земле за плечи."
    "Он наваливается на тебя всем телом, и тяжесть его тела выбивает воздух из твоих легких."
    "Глубокий рокот исходит из его груди прямо перед тем, как он поднимает тебя с земли, и медвежьей хваткой обнимает тебя."
    scene black
    show garg lose1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos -0.8 ypos 0
        zoom 1.2
        linear 20.0 xpos 0 ypos -250
    e 0 "А-а-а!"
    "Острая, скручивающая боль распространяется из твоих рук, когда ты пытаешься вырваться из хватки горгульи."
    "Горгулья издает пронзительный визг и сжимает свои бицепсы еще сильнее, полностью блокируя твои руки. "
    "Он подносит свои острые как бритва когти к твоему горлу и проводит воображаемую линию поперек твоего горла. "
    "Горгулья" "Шшш."
    "Горгулья открывает рот и позволяет своему длинному влажному языку коснуться твоих щек."
    "Ты вздрагиваешь, и твои ноги дрожат от того, что теплая промежность становится все теплее и задевает твой зад."
    e 0 "Стой, что ты?"
    show garg lose1 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "В тебе не осталось сил бороться."
    "Горгулья издает гортанный смешок и начинает ласкать твою правую грудь одной рукой, а другой проводит пальцами по твоим бокам."
    "Твое лицо кривится и искажается, как голем обращается с твоим телом."
    "Его пальцы глубоко зарываются в твой мех, расчесывая его острыми когтями."
    "Его правая рука скользит по твоему твердому прессу. Нижняя челюсть дрожит от прикосновения. "
    "Любое ментальное сопротивление оказывается бесполезным, поскольку твое тело-раб мясистых, но ловких пальцев горгульи."
    "Через твои связанные руки, прижатые к животу горгульи, ты удивляешься, что его тело очень похоже на твое."
    "Горгулья снова воркует тебе в ухо и взмахом руки срезает набедренную повязку."
    show garg lose2 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Твой полутвердый член вываливается наружу, и ты издаешь тихий вздох."
    "Горгулья" "Ммм."
    "Вибрация груди горгульи отдается эхом в твоей спине, твои щеки краснеют в ответ."
    "Его голос намекает, что ему нравится то, что он видит. "
    "Рука, которая держит твою правую грудь, движется на юг, в то время как другая рука обхватывает ваши яйца и ласкает их."
    "Его широкая ладонь холодна на ощупь."
    "Ты стонешь, когда он перекладывает твои яички с одного пальца на другой. "
    "Твой член начинает напрягаться, и ты чувствуешь, что становишься все свободнее и горячее."
    "Горгулья" "Тепло...хорошо. "
    "Горгулья" "Я хочу еще!"
    e 0 "Чт-"
    show garg lose3 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    e 0 "Какого черта ты делаешь?"
    "Горгулья подхватывает тебя под зад и поднимает."
    "Другой рукой он удерживает твои руки на месте, все, что ты можешь сделать, это махать ногами в воздухе."
    "Твой похититель смеется и отшвыривает тебя одной рукой, как будто ты ничего не весишь."
    "Каждый раз, когда твоя задница слегка опускается, ты чувствуешь, как твердая как камень эрекция горгульи ударяется о твою ягодицу. "
    "Горгулья прижимает тебя к своей обнаженной груди. Его драконья голова упирается тебе в горло."
    "Он тяжело дышит тебе в шею. Его дыхание горячее и пахнет землей."
    with flashbulb
    show garg lose4 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Без предупреждения горгулья погружает весь свой член тебе в задницу"
    "Нарастающая боль, извергающаяся из твоей задницы, заставляет твои глаза закрыться. "
    "Твои пальцы ног изгибаются и дергаются, но это только заставляет тебя погрузить член горгульи глубже внутрь себя."
    "Твоя грудь вздымается, когда ты изо всех сил пытаешься привыкнуть к пульсирующему члену, пронзающему твою задницу."
    "Его теплое тело заполняет стенки твоей задницы, смазывая его член и облегчая тебе восприятие всей его длины."
    "Постепенно боль тает, и вы плаваете в блаженной эйфории."
    "Твой член твердеет, и капли смазки стекают по стволу. "
    "Твои тихие всхлипы сопровождаются шлепающими звуками, когда член горгульи вырывается и снова входит в тебя."
    show garg lose5 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Горгулья" "Да, волк крепкий!"
    "Горгулья неумолимо вонзает в тебя свой член."
    "Оставляя тебя в оцепенении, пока он скачет на твоей упругой заднице, как дикий зверь в жару."
    "Твоя челюсть отвисает, и ты взвизгиваешь с каждым сильным толчком, не желая, чтобы полнота внутри твоей задницы прекратилась. "
    "Горгулья" "Хороший волк. Издавай больше звуков."
    "Твой собственный член подпрыгивает вверх и вниз, разбрызгиваясь по всей земле."
    "Его хватка на твоих руках и на твоих икрах становится все крепче. Нет никакого спасения."
    "Каждый раз, когда его член касается твоего места, ты откидываешь голову назад, ты скулишь и стонешь."
    "Твои похотливые звуки бодрят горгулью."
    "Его рот сжимает твою шею и кусает, пока он энергично трахает твою задницу."
    e 0 "Черт! Черт!"
    "Ты чувствуете, как внутри твоих яиц нарастает давление. Ты уже близко."
    "Горгулья" "Гах!"
    "Горгулья стискивает зубы и издает приглушенный рев, когда его член извергается и горячая сперма заполняет твои внутренности."
    "От одной только силы его непрекращающегося оргазма на глаза наворачиваются слезы. "
    "Ты больше не можешь этого выносить, твои пальцы поджимаются, и ты кончаешь так же сильно. "
    with flashbulb
    e 0 "Кончаю!"
    with flashbulb
    show garg lose6 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Струйка белой горячей спермы вылетает из твоего члена и брызгает в добрых футах от вас двоих."
    "Все твое тело содрогается, когда потоки спермы вытекают из твоей задницы, не в силах удержать проливное количество спермы, затыкающей твою задницу."
    "Кажется, прошла целая вечность, прежде чем вы оба наконец перестали кончать."
    "Ваши горячие обнаженные тела прижимаются друг к другу, и вы оба тяжело дышите."
    "Жужжание вашего оргазма, должно быть, все еще продолжается, потому что вы не чувствуете пальцев ног."
    "Мои пальцы?"
    show garg lose7 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Горгулья вытаскивает свой член из твоей задницы, ты представляешь себе его член полностью мокрым от спермы, судя по тому, сколько он выгрузил внутри тебя."
    e "Что?"
    "Покалывание распространяется от пальцев ног к остальной части стопы."
    "Ты смотришь вниз, и, к твоему ужасу, твои ноги превращаются в камень."
    "Несмотря на все усилия сдвинуть ноги, они не сдвинулись ни на дюйм."
    "Горгулья" "Ты,камень."
    "Ты борешься с крепкой хваткой горгульи, но усилия тщетны, оставляя только следы ожогов на суставах."
    "Все, что ты можешь сделать, это с ужасом наблюдать, как окаменение продолжается."
    show garg lose8 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    e 0 "Нет, нет, нет, не делай этого!"
    "Горгулья" "Ш-ш-ш ... Нет, Превращайся в камень. Хорошо."
    "Окаменение распространяется быстрее, пока вся твоя нога не становится пепельно-серой. "
    "Твоя способность говорить поглощена надвигающимся страхом, распространяющимся по всему телу."
    "Горгулья" "Тепло...холодно."
    show garg lose9 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Твои зрачки пульсируют, а сердце колотится."
    "Ты буквально кричишь в ужасе внутри своей головы, как ты умоляешь Божественных Существ, чтобы это не было концом."
    "Всего за несколько минут окаменение поглощает большую часть тебя, и ты теряешь все чувства ниже шеи."
    "Горгулья продолжает баюкать твое каменное тело, как драгоценное домашнее животное, поглаживая твой каменный зад."
    "Весь процесс, кажется, ускоряется после того, как проходит твоё сердце."
    show garg lose10 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Ты можешь только хныкать, как испуганный щенок, когда всё остальное превращается в камень."
    hide garg lose10 with slow_dissolve
    "..."
    "......"
    "Несмотря на то, что ты превратился в камень, вой ум все еще работает."
    "Горгулья запросто может разнести тебя на куски, и на этом все закончится, но вместо этого он ставит тебя на землю."
    "Горгулья" "Тепло,черт,хорошо."
    "Ты слышишь, как горгулья проводит острым когтем по твоему каменному лицу. Потом он целует тебя в щеку."
    "И ты слышишь,как он хватает твою сумку на земле. Затем ты слышишь, как он жует."
    "Горгулья" "Восхитительно."
    "Горгулья уходит и оставляет тебя на твоем месте до конца ночи."
    "Твоя единственная компания-это разные жуки, которые ползают вокруг, иногда даже ползают по твоему лицу, единственное утешение в том, что ты ничего не чувствуешь."
    "Как только окаменение проходит, и ты падаешь на землю измученный и голый."
    "Ты берешь свое снаряжение и выбираешься из пещеры."
    "Спасибо, что ты выжил."

    if Time.hours >=6:
        $ Time.days = Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
    elif True:
        $ Time.hours = 6
        $ Time.mins = 30

    $ Zalt.hp = min(Zalt.hp+Zalt.maxhp/2, Zalt.maxhp)
    $ Zalt.mp = min(Zalt.mp+Zalt.maxmp/2, Zalt.maxmp)
    $ qty = int(jane_inv.qty(coin)*0.2)
    $ jane_inv.drop(coin,qty)
    $ Zalt.lust = 0
    $ persistent.CG_gargoyle_lose = True
    $ Zalt.cor = min(Zalt.cor+2,100)
    $ Zalt.Dungeon_leave = True
    if Map.caj3g == 1:
        $ Map.caj3g = 0
        jump Cave_map_ferryman
    if Map.ca3garg:
        $ Map.ca3garg = False
    if Map.ca18garg0:
        $ Map.ca18garg0 = False

    jump Cave_map

label battle_gargoyle_sex:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    hide gargoyle with dissolve
    if persistent.CG_gargoyle_win == True:
        "Вы хотите пропустить сцену?"
        menu:
            "Да" if True:
                if Map.caj3g == 1:
                    "Не желая рисковать, когда он проснется, ты хватаешь свои вещи и отрезаешь кусочек мха, растущего на крыльях горгульи."
                    "Ты получаешь блестящий мох и 300 EXP."
                    $ Zalt.lust = 0
                    $ jane_inv_M.take(moss)
                    $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                    $ Map.caj3g = 0
                    jump Cave_map_ferryman
                if Map.ca18garg0:
                    $ Map.ca18garg0 = False
                    "Ты получаешь два блестящих мха и 600 EXP."
                    $ jane_inv_M.take(moss,2)
                    $ Zalt.exp = min(Zalt.exp+600, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                    $ Map.ca18 = 4
                    $ Map.ca19 =1

                    $ Zalt.A_exp = Zalt.A_exp + 100*Zalt.A_exp_lv
                    $ PPEXP = 100*Zalt.A_exp_lv
                    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                    jump Cave_map
                "Не желая рисковать, когда он проснется, ты хватаешь свои вещи и отрезаешь кусочек мха, растущего на крыльях горгульи."
                "Ты получаешь блестящий мох и 300 EXP."
                $ Zalt.lust = 0
                $ jane_inv_M.take(moss)
                $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))

                if Map.ca3garg:
                    $ Map.ca3garg = False
                    scene cave 1 with dissolve
                    "Теперь ты можешь спокойно прочитать остальную часть текста."
                    "Руководствуясь мужеством наших павших, которые боролись за свою свободу в Царстве Аплистии."
                    "Остальная часть текста не читается."
                    e 13 "Королевство? Это место не похоже на то, что оно было заселено так давно."
                    e 1 "Может быть, Фло там?"
                    $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
                    $ PPEXP = 50*Zalt.A_exp_lv
                    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                    $ Map.ca3 = 4
                    jump Cave_map
                jump Cave_map
            "Нет" if True:
                pass
    scene black
    show garg win1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos -0.8 ypos 0
        zoom 1.2
        linear 20.0 xpos 0 ypos -250
    "Такого предложения еще никогда не было. "
    "Горгулья издает слабый стон и поднимает хвост, чтобы показать свою тугую дырочку."
    "Ты не можешь отрицать, что зрелище перед тобой выглядит дразнящим."
    "Убрав меч в ножны, ты опускаешь факел, чтобы забрать свой приз."
    "Ты снимаешь набедренную повязку и прижимаешься всем телом к спине горгульи."
    "Горгулья" "Ах!"
    "Крылья горгульи отклоняются в сторону, освобождая место для всей твоей формы, и она издает гортанный скулеж."
    show garg win1 with slow_dissolve:
        xpos 0.05 ypos -0.02
        zoom 1.05
    e 0 "Иди сюда, ты. Ты ведь этого хочешь, не так ли?"
    "Ты держишь горгулью за шею и поворачиваешь ее лицом к себе."
    "Горгулья" "Да... тепло хорошо."
    e 0 "Тепло, значит, ты хочешь, чтобы мой теплый член был внутри тебя? Наполнить тебя?"
    "Горгулья скулит громче."
    "Ты наклоняешься и хватаешь теплое фаллическое мясо между ног горгульи."
    "Его член заполняет всю твою руку и возбужденно пульсирует, когда ты медленно его растираешь."
    "Горгулья" "Теплее... лучше... мне хочется тепла."
    e 0 "О, я заставлю тебя почувствовать тепло. Чувствуешь, как он трется об тебя?"
    "Ты скользишь своим членом по промежности горгульи."
    "Медленно, позволяя ему почувствовать твердость твоего члена, прижимающегося к его коже."
    "Горгулья" "Черт... дай мне... теплый член!"
    e 0 "Ш-ш-ш. Я собираюсь не торопиться."
    "Со звериным рычанием ты крепко сжимаешь член горгульи, заставляя его скулить, как зверя в жару."
    "Зверь пытается повернуть голову ближе к тебе, вы оба смотрите друг другу в глаза, ваши губы почти соприкасаются."
    "Ты пытаешься правильно расположиться, но твой член скользит по его заднице, размазывая его дырочку своим пре."
    "Отпустив его член, ты хватаешь свою пульсирующую член и направляешь ее в ожидающее отверстие горгульи."
    "Горгулья" "Гах... толстая!"
    show garg win2 with slow_dissolve:
        xpos 0.05 ypos -0.02
        zoom 1.05
    "Горгулья закрывает глаза и тяжело стонет."
    "Маленькие струйки слюны капают из его рта, когда ты толкаешь свой член глубже в него."
    "Его тугая задница сопротивляется твоей мясистой дубине."
    "Ты ворчишь, хватаешь горгулью за шею и что-то шепчешь ему на ухо."
    e 0 "Не сопротивляйся этому, просто дыши и прими это, большой мальчик."
    "Горгулья издает глубокий стон, но ты чувствуешь, как твой твердый член все глубже входит в него."
    e 0 "Ммм, да, у тебя горячая тугая попка. Ты чувствуешь это внутри себя?"
    "Горгулья" "Да...тепло хорошо."
    "Ты слышишь звук капающей воды, разбрызгивающейся по полу пещеры, когда продолжаешь дрочить член горгульи."
    "Твоя рука тянется вниз и обхватывает его член, размазывая пре по всем пальцам и вдоль его твердого ствола."
    "Горгулья закрывает рот и скрипит зубами, но ты все равно слышишь его приглушенные стоны."
    "Ты оттягиваешь горгулью назад за шею, вжимая свой член глубже в него."
    "Огромное давление нарастает внутри твоих яиц. Все, что ты хочешь, это трахнуть горгулью так сильно, как только сможешь."
    show garg win3 with slow_dissolve:
        xpos 0.05 ypos -0.02
        zoom 1.05
    "Ты хватаешь горгулью за шею и безжалостно колотишь его в зад."
    "Внутренности его задницы смазаны твоим протекающим членом и распыляются внутри него."
    "Твоя грудь горит жаром похоти, колотя и колотя по заднице горгульи."
    "То, как его задница трясутся при каждом толчке, и сотрясающие землю стоны горгульи заводят тебя."
    "Тепло исходит от ваших соединенных тел, согревая холодное тело горгульи под тобой."
    "Его член в твоих руках тверд, как камень, выкачающий лужу смазки на пол."
    "Горгулья" "Мне хочется кончить!"
    "Стиснув зубы, задница горгульи крепче сжимает твой член."
    e 0 "Бери, бери!"
    "Горгулья" "Да! Тепло!"
    "Ваши толчки начинают замедляться, а колени подгибаются."
    e 0 "Черт, я уже близко!"
    "Горгулья" "Га-а-а-а!"
    e 0 "Я кончаю!"
    with flashbulb
    "Горгулья ревет вам в уши, когда вы оба выпускаете свое семя."
    with flashbulb
    show garg win4 with slow_dissolve:
        xpos 0.05 ypos -0.02
        zoom 1.05
    "Яркие огни вспыхивают перед твоими глазами, и вся комната вращается, в то время как волна за волной спермы заполняет дыру горгульи."
    "Твоя рука липкая от спермы горгульи."
    "И вскоре ты чувствуешь, что твои руки немеют."
    e 0 "Воух, воу."
    "Ты быстро выбрасываешь его сперму из своей руки."
    "Горгулья стонет и закрывает глаза. "
    "Осторожно ты кладешь его голову на землю и вытаскиваешь свой сдувшийся член из его задницы."
    hide garg win4 with slow_dissolve
    "Горгулья" "Теплая..."
    "В свете факела ты видишь, как горгулья улыбается."
    "Не желая рисковать, когда он проснется, ты хватаешь свои вещи и отрезаешь кусочек мха, растущего на крыльях горгульи."
    $ persistent.CG_gargoyle_win = True
    if Map.caj3g == 1:
        "Ты получаешь блестящий мох и 300 EXP."
        $ Zalt.lust = 0
        $ jane_inv_M.take(moss)
        $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        $ Map.caj3g = 0
        jump Cave_map_ferryman
    if Map.ca18garg0:
        $ Map.ca18garg0 = False
        "Ты получаешь два блестящих мха и 600 EXP."
        $ jane_inv_M.take(moss,2)
        $ Zalt.exp = min(Zalt.exp+600, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        $ Map.ca18 = 4
        $ Map.ca19 =1

        $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
        $ PPEXP = 50*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump Cave_map
    if Map.ca3garg:
        $ Map.ca3garg = False
        scene cave 1 with dissolve
        $ Zalt.lust = 0
        "Ты получаешь блестящий мох и 300 EXP."
        $ jane_inv_M.take(moss)
        $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        "Теперь ты можешь спокойно прочитать остальную часть текста."
        "Руководствуясь мужеством наших павших, которые боролись за свою свободу в Царстве Аплистии."
        "Остальная часть текста не читается."
        e 13 "Королевство? Это место не похоже на то, что оно было заселено так давно."
        e 1 "Может быть, Фло там?"
        $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
        $ PPEXP = 50*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.ca3 = 4
        jump Cave_map

    jump Cave_map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
