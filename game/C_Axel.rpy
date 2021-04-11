label Axel_meet:
    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Axel')
    $ renpy.music.set_volume(1, 4, channel = "Axel")

    $ Time.mins = Time.mins +5
    if Quest.campb == 1 and Quest.campl < 3:
        "Стражник кланяется и уходит, оставляя вас с Акселем одних в палатке."
        show axel stand at center with dissolve
        a "Давайте пропустим приветствия."
        a "Я получил известие, что племя ящериц делает свой ход."
        a "Они планируют занять территорию, близкую к нашему племени, и разместить там часть своих войск."
        a "Дерзкие ублюдки эти ящерицы, но надо отдать им должное, это хорошее место."
        e 1 "Так какое это имеет отношение ко мне?"
        a "Проще говоря, ты поведешь группу моих людей в район, который хотят захватить ящеры."
        a "Снесите им головы и убедитесь, что они больше никогда не смогут претендовать на это."
        e 1 "Откуда ты вообще взял эту информацию?"
        e 1 "Быки, конечно, не самые хитрые в этой компании."
        a "Кому нужна скрытность, когда все, что тебе нужно сделать, это переломать несколько костей, и они будут петь для тебя."
        a "Я буду милосердным и справедливым, и позволю тебе принять эту работу или нет."
        a "Меньше всего мне нужен бесполезный воин, работающий против своей воли."
        menu:
            "Да" if True:
                e 1 "Очень хорошо, Вождь Аксель."
                a "Хорошо, если бы только Тэйн мог научиться у тебя паре вещей о том, что не надо так много говорить в ответ."
                a "Я дам тебе время подготовиться, вернешься ко мне, когда будешь готов, и я познакомлю тебя с твоей командой."
                $ Quest.campb = 3
            "Нет" if True:
                e 5 "Мне все еще нужно время, чтобы подумать об этом."
                a "Тогда убирайся с глаз моих, у меня нет времени тратить его на того, кто не будет работать!"
                $ Quest.campb = 2
        if Time.hours >= 6 and Time.hours <= 17:
            scene bulltribe 1 with vslow_dissolve
        elif True:
            scene bulltribe 1n with vslow_dissolve
        e 1 "(Что мне теперь делать? Мне выполнить приказ Акселя?)"
        e 13 "(Если я этого не сделаю, что тогда сделает племя ящериц? Я не совсем его любимый человек на данный момент. )"
        if Quest.campb == 3 or Quest.campl == 3:
            "Ты поворачиваешься, и твой взгляд падает на Тейна, сидящего на его камне."
            e 5 "(Тейн! Может, у него есть другой способ справиться с этим, но действительно ли мне нужна его помощь?)"
            e 1 "(С его участием все может стать сложнее.)"
        elif True:
            "Ты поворачиваешься, и твой взгляд падает на камень, на который обычно садится Тан, но его там нет."
            e 6 "Где он, когда он мне нужен?"
            e 13 "(Не могу дождаться, когда появится Тейн, чтобы решить, что делать. )"
            e 13 "(Я должен сделать свой выбор и рассказать Тейну об этом позже.)"
        hide axel stand
        jump Bull_tribe_map

    if Quest.campb == 2 and Quest.campl < 3:
        show axel stand at center with dissolve
        a "Ты наконец-то решил избавиться от этих ящериц-нарушителей?"
        menu:
            "Да" if True:
                e 1 "Очень хорошо, Вождь Аксель."
                a "Хорошо, если бы только Тэйн мог научиться у тебя паре вещей о том, что не надо так много говорить в ответ."
                a "Я дам тебе время подготовиться, вернешься ко мне, когда будешь готов, и я познакомлю тебя с твоей командой."
                $ Quest.campb = 3
            "Нет" if True:
                e 5 "Мне все еще нужно время, чтобы подумать об этом."
                a "Тогда убирайся с глаз моих, у меня нет времени тратить его на того, кто не будет работать!"
        hide axel stand
        jump Bull_tribe_tent
    if Quest.campb == 3 and Quest.campl < 3:
        show axel stand at center with dissolve
        a "Я так понимаю, ты готов уйти?"
        menu:
            "Да" if True:
                e 1 "Я готов идти."
                "Аксель вызывает еще четырех быков в свою палатку."
                "Им приказано следовать вашим приказам."
                "И по вашим командам команда отправится и достигнет лагеря к 11 часам утра."
                $ Quest.campb = 4
                jump camp_map
            "Нет" if True:
                e 5 "Мне нужно больше времени, чтобы подготовиться."
                a "Аксель вздыхает и отмахивается от тебя разочарованным качанием головой. "
        hide axel stand
        jump Bull_tribe_tent
label Axel_camp_end:

    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Axel')
    $ renpy.music.set_volume(1, 4, channel = "Axel")

    window hide None
    stop music fadeout 1
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    scene bulltent with slow_dissolve
    if Time.bullkid == 9999:
        $ Time.bullkid = Time.days
    if Quest.campb > Quest.campl and Quest.campt >=5:
        $ Time.hours = Time.hours +3
        "Ты ковыляешь вверх по лестнице к палатке Акселя. Боль в глазах и желудке все еще колет при каждом шаге."
        "Когда вы входите в палатку, вы видите четвереньки быков, которые составили вашу команду на коленях в ряд."
        show axel stand at center with dissolve
        "Аксель шагает туда-сюда во время разговора с командой."
        a "То есть, вы говорите, что четверо тренированных бычьих воинов, сбежали, потому что \"гигантский волк\"появился из ниоткуда и начал всех терроризировать."
        "Первый Воин Бык" "Честно, это случилось."
        a "И ты! Где ты был? Почему ты возвращаешься сюда без своей команды."
        "Он указывает на тебя, стоящего у входа в палатку."
        "Быки на коленях поворачиваются к тебе и с удивлением смотрят на тебя."
        "Ты делаешь шаг назад, но говоришь себе не бежать."
        e 13 "Меня вырубило что-то тяжелое, когда я пошёл в разведку впереди."
        e 1 "Когда я проснулся, я был в кустах, а вокруг никого не было."
        "Второй Воин Бык" "Да, похоже, тебя толкнули о камень."
        "Четвёртый Воин Бык" "Видишь ли, гигант волков настоящий, и он слишком силен, чтобы нас победить."
        "Аксель громко кричит, видно, как из его ноздрей вырываются затяжки воздуха."
        hide axel stand with dissolve
        "Он поворачивается и садится на трон, упираясь подбородком в одну руку. "
        a "А как же ящерицы?"
        "Второй Воин Бык" "Я видел, как они сбежали испуганные. Я думаю, что и гигантскому волку они не подошли."
        a "Если там есть такое опасное существо, вы четверо, отправляйтесь в деревню и расскажите всем, чтобы все держались подальше от этого места. "
        "Все четыре быка" "Да, Вождь Аксель!"
        a "После этого вы посетите местного целителя и проверите себя."
        "Воины приветствуют своего вождя и покидают палатку."
        show axel stand at center with dissolve
        "Аксель постукивает по подлокотнику своего трона и бросает на тебя любопытный взгляд."
        a "Таким образом, ни одна из сторон не выигрывает лагерь. Что вы об этом думаете?"
        menu:
            "Молчать" if True:
                e 13 "..."
                a "..."
                a "Хорошо, я позову тебя, когда будет работа."
                "Ты кланяешься и поворачиваешься, чтобы покинуть палатку."
                a "Привет, Блохастик."
                "Ты обращаешься к Вождю."
                a "Ты выглядишь дерьмово, возьми это и принеси лекарство."
                a "Этот волк сделал номер на твоих глазах."
                "Он бросает тебе мешок с монетами."
                "<[name] получено 200 монет>"
                "<[name] получено одно очко повышения уровня.>"
                $ jane_inv.take(coin,200)
                $ Zalt.points = Zalt.points +1
                e 13 "Спасибо."
                "Вы выходите из палатки."
            "Ни один бык не должен был умереть." if True:
                e 1 "Никто не умер, думаю, этого достаточно."
                a "Сейчас? Ну, ящерицы тоже не умерли."
                a "Если бы мы уничтожили их, это могло бы нанести удар по их моральному духу, но ничего не изменилось, и мои люди все еще в опасности."
                a "Ты все еще думаешь, что это хороший конец?"
                e 1 "..."
                e 1 "Что-нибудь еще?"
                a "Только это."
                "Он бросает тебе мешочек с монетами."
                a "Залечи свои раны. Твой взгляд выглядит дерьмово."
                "<[name] получено 200 монет>"
                "<[name] получено одно очко повышения уровня.>"
                $ jane_inv.take(coin,200)
                $ Zalt.points = Zalt.points +1
                e 13 "Спасибо."
                "Вы выходите из палатки."
        $ Quest.campb =6
        $ Quest.campt =6
        $ Quest.camp_a = 2
        jump Bull_tribe_map
    elif Quest.campb < Quest.campl and Quest.campt >=5:
        $ Quest.camp_a = 2
        "Ты осторожно приближаешься к вождю племени быков, который сидит на своем троне и смотрит на землю усталым выражением лица. "
        show axel stand at center with dissolve
        a "Что тебе нужно Блохастик?"
        "Он смотрит на тебя, его глаза горят отблеском опасного воина."
        "Его тело излучает мощную ауру."
        "Твои чувства говорят тебе идти осторожно, он не в хорошем настроении."
        e 1 "Я просто хотел поговорить, могу зайти попозже."
        a "Почему нет? Если увидишь старого быка, который выглядит беспокойным, лучше оставить его в покое, даже не спрашивай, что случилось."
        e 9 "(Как-то неловко.)"
        e 1 "Ладно, что случилось?"
        a "Если бы вы позаботились, наше племя имеет дело с первой попыткой ящериц захватить это место"
        a "Где ты был? Так называемый союзник племени быков.”"
        e 9 "Я-"
        a "Я не хочу этого слышать! Ясно, что тебе предстоит пройти долгий путь, прежде чем ты действительно станешь одним из нас."
        a "Будь моя воля, тебя бы пнули достаточно сильно, и ты полетел бы обратно в таверну за то, как много ты “помог” до сих пор, но мой сын все еще считает тебя достойным."
        a "Честно говоря, я этого не вижу, у тебя нет любви к моему народу."
        a "За это ты никогда не будешь достоин быть нашим союзником."
        "Несмотря на его сопротивление тебе в племени, похоже, что он искренне хочет, чтобы ты им помог."
        "И все же, это тот маршрут, по которому ты хочешь пойти?"
        "Заслуживают ли ящерицы быть уничтоженными?"
        "Как долго ты можешь продолжать играть в посредника, тянуть время?"
        a "Поэтому я решил, что заставлю тебя есть, спать и дышать бычьей культурой и сделаю тебя воином, достойным нашего племени."
        "Ты хочешь отвергнуть все, что предлагает Вождь Аксель, но ты решаешь против этого, опасаясь того, что он сделает в своем разъяренном состоянии."
        "Он поворачивается назад и садится на трон."
        a "Мои рога сейчас практически дымятся, я просто хочу оставить всю эту ящеричную чушь позади."
        a "Говори, Блохастик."
        jump Axel_tribe_talk1
    elif Quest.campl > Quest.campb and Quest.campt <5:
        $ Quest.camp_a = 2
        "Вы слышите громкий разбивающийся звук и гневное мычание изнутри палатки."
        "Ты сглатываешь у входа в палатку Акселя. "
        "Вождь, должно быть, слышал о том, что случилось с его людьми."
        "Вы не решаетесь войти."
        "И все же есть шанс, что он не знает обо всем."
        "В таком случае отдаленность не поможет."
        "Ты сжимаешь зубы и входишь в палатку."
        a "БЛЯТЬ!"
        show axel stand at center with dissolve
        "Бык пнул свой трон на землю."
        a "Какого хуя тебе надо?"
        e 9 "Я-"
        a "Заткнись, я потерял своих людей. Ты хоть понимаешь, что значит потерять свой народ?"
        a "Они были хорошими людьми, у них были семьи, у них были амбиции. Всё, блядь, ушло."
        a "Если, конечно, следующие слова из твоих уст-это то, что ты собираешься помочь справиться с этими подлыми ящерицами."
        a "Я не хочу это слышать! Убирайся!"
        scene bulltribe 1 with dissolve
        "Ты выбегаешь из палатки."
        $ Time.aaxel = Time.days
        jump Bull_tribe_map
    elif Quest.campb > Quest.campl and Quest.campt <5:
        $ Quest.camp_a = 2
        show axel stand at center with dissolve
        "Вождь Аксель стоит перед троном со скрещенными руками и широкой улыбкой на лице."
        a "С возвращением, Блохастик, я впечатлен, ты помог мне остановить ящериц и достал нам непроходимый лагерь."
        e 1 "Новости быстро распространяются."
        a "Отсюда я слышал, как ваша команда радовалась их победе."
        a "Может, ты мне еще пригодишься, Блохастик."
        e 13 "Спасибо, наверное."
        "Аксель бросает тебе мешок с монетами."
        a "Потрать их с умом."
        "<[name] получено 500 монет>"
        "<[name] получено одно очко повышения уровня.>"
        $ jane_inv.take(coin,500)
        $ Zalt.points = Zalt.points +1
        a "И последнее, я думаю, пришло время тебе познакомиться с быками поблизости."
        a "Ты не можешь быть союзником нашего племени, если не знаешь самого племени."
        e 6 "Хорошо?"
        a "Я позову тебя Блохастик, когда придет время. Теперь двигайся, мне нужно бежать в деревню."
        $ Quest.campb =6
        jump Bull_tribe_map

label Axel_tribe_talk:
    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Axel')
    $ renpy.music.set_volume(1, 4, channel = "Axel")

    show axel stand at center with dissolve
    if Quest.bomb_end != 0 or (Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bomb_bull ==2):
        jump Axel_letter
    if Quest.fes_end == 0 and Quest.fesa >= 1:
        jump Axel_festival
    a "Хм, ну, если это не моя личная гончая. Что такое Блохастик?"
    jump Axel_tribe_talk1
label Axel_tribe_talk1:
    if Axel.talktree == 1:
        menu:
            "Спросить о создании нового оружия" if True:
                e 1 "Вождь Аксель, я хотел поговорить с вами об оружии."
                a "А как же Блохастик?"
                e 1 "Ну, я видел, как почти каждый бык-сельчанин носил с собой оружие.."
                a "Тем легче, конечно, защитить себя."
                e 1 "Правда, но что меня действительно интересует, возможно ли мне достать для себя оружие, сделанное быком? "
                a "Интересуешься нашим оружейным делом, малыш."
                a "Не могу сказать, что виню тебя. \nНашего оружия, когда оно будет в правильных руках, будет достаточно, чтобы свергнуть армии. "
                a "Тебе нужно поговорить с владельцем магазина, если тебе нужны его вещи."
                a "Даже я должен играть по его правилам, если речь идет об оружии."
                jump Axel_tribe_talk1
            "Новый тур" if True:
                a "Эй, Блохастик. Насколько ты теперь знаком с деревней?"
                e 6 "Я бы сказал, что уже видел большую часть."
                a "Хм, а что насчет бычьего храма?"
                e 1 "Ну, там есть комната со странной перегородкой."
                a "Да, да. Мы все знаем об этой комнате, \nНо ты видел что-нибудь необычное в округе?"
                a "Возможно, разновидность надгробия."
                e 1 "Нет, раньше не видел."
                a "Ладно, тогда решено. Будь готов, когда я позову."
                a "Мы продолжим экскурсию в какое-нибудь особенное место."
                e 1 "Я всегда к вашим услугам, Вождь Аксель."
                a "И облегчи свой груз, у меня для тебя есть тяжелое оборудование. "
                e 9 "Очень хорошо. "
                jump Axel_tribe_talk1
            "Спросить о повторном браке" if Axel.s <=3:
                e 1 "Вождь Аксель, есть кое-что, о чем я думал, о тебе."
                a "Что такое Блохастик?"
                e 6 "Ты когда-нибудь думал о повторном браке?"
                a "Ха! Есть вопрос, который люди никогда не перестанут задавать. "
                a "Я признаю, что было немного одиноко, когда больше не с кем было делить кровать."
                e 6 "Я имею в виду, я мог бы..."
                a "Нет. Без обид, но ты должен быть чертовым героем в этой деревне, чтобы я подумал о том, чтобы быть с тобой в постели."
                a "Даже тогда я не буду называть нас любовниками."
                a "Просто я не уверен, что получение новой жены будет правильным для нас с Тейном."
                a "Ты видел, что с нами стало."
                a "Если в нашу жизнь войдет еще одна женщина, будет несправедливо, если она пройдет через нашу семейную драму."
                e 13 "Может быть, это больше повод, чтобы уладить дела с Тейном. "
                a "Может быть. Если какая-нибудь женщина захочет такого толстяка, как я."
                e 6 "Поверь мне, ты очень привлекателен."
                a "..."
                a "Ты будешь трахаться практически со всем, что ходит, не так ли?"
                e 5 "... О, посмотрите на время. Я должен вернуться туда."
                jump Axel_tribe_talk1
            "Оставить" if True:


                jump Bull_tribe_tent
    elif True:
        menu:
            "Спросите о тумане" if True:
                e 1 "Вождь Аксель, мне нужно спросить о тумане."
                e 1 "Несмотря на войну, большая угроза заключается в том, что мы застряли здесь с этим туманом, вызывающим чудовищ."
                a "Позволь мне сэкономить твоё время, сказав, что мы ничего не знаем об этом тумане."
                a "Когда туман только появился, мы мало думали об этом, мы чуыствовали туман и раньше.."
                a "Через некоторое время мы поняли, что туман никуда не денется."
                a "Итак, я послал несколько разведчиков, чтобы найти выход из леса, примерно тогда мы связались с таверной, это была только гиена и..."
                a "Как его зовут? Клод? Нет, Сноу."
                a "Туман действительно поднимается в странные моменты, однажды мы собрали всех быков и ящериц у выхода и заставили их уйти в тот момент, когда туман поднимался."
                e 1 "Тогда почему так много вас все еще здесь."
                a "Те, кто остался, сделали это, чтобы защитить деревню и храм."
                a "Предки нашего племени проделали долгий путь, чтобы построить этот дом для нас, мы не дадим туману забрать его у нас без боя."
                e 1 "Так что быки и ящерицы раньше могли работать вместе."
                a "Это было давно."
                a "Потом случились похищения, и прежде чем мы узнали об этом, нас отделил от остального леса туман."
                a "Похищения тогда прекратились, добавив подозрения, что из-за того, что ящерицы не смогли нас найти."
                a "Мы были в безопасности, но мы снова были связаны с остальной частью леса."
                e 13 "Все это может быть просто совпадением. "
                a "Совпадение не объясняет чешую ящерицы и оружие ящерицы, которое мы нашли, когда столкнулись с похитителем."
                a "Это, и ужасная татуировка на его спине. Я никогда этого не забуду."
                e 1 "Ты был там?"
                a "Мое настроение испорчено. Поговорим о чем-нибудь другом."
                jump Axel_tribe_talk1
            "Спросить о доказательствах похищений." if True:
                e 1 "Почему ты так уверен, что кто-то из племени ящериц - похититель."
                a "У нас есть чешуя ящерицы с места преступления, чтобы доказать это, и потому что я чертовски хорошо видел это своими собственными глазами."
                a "Скользкий кусок мусора был пойман с поличным при попытке вломиться в дом ночным патрулем."
                a "Вся деревня выбежала за ящерицей, у него на спине была татуировка."
                a "Я все еще вижу его отвратительную форму, когда вспоминаю ту ночь."
                a "Мы почти загнали эту чертову штуку в угол, но она оказалась сильнее, чем выглядела, и избила большинство из нас, прежде чем убежать во время суматохи."
                e 1 "Если ты знаешь, как выглядит преступник, просто схвати его из деревни ящериц."
                a "Думаешь, я не пытался? Наукс закатил истерику, когда я потребовал, чтобы он выдал преступника."
                a "Он продолжал лгать, что такого не было, и у него хватило наглости бросить обвинение моему племени, и что мой народ похитил их детей."
                a "О, он хорош, когда лжет мне в лицо без малейшего чувства вины."
                "Аксель постукивает по подлокотнику трона."
                a "Я не могу позволить ему выйти сухим из воды, он подвергает жизни опасности, защищая бешеную ящерицу."
                a "Я видел, как семьи разрывались на части из-за потери детей."
                a "Потом я подумал, что если это случится с Тейном, и я просто... Я... Ааа! "
                "Его левая рука сжимается в кулак и с грохотом падает на трон. Удивительно, что трон все еще стоит."
                a "Ни один родитель не должен проходить через что-то вроде потери ребенка."
                a "Я разорву эту проклятую деревню на части, пока мы не найдем эту ящерицу и не заставим его заплатить за свои преступления."
                a "Никто не связывается с племенем быков!"
                "Его переполняет решимость, ты не думаешь, что сможешь убедить Акселя в обратном."
                jump Axel_tribe_talk1
            "Спросить об отношениях Акселя с Тейном." if Axel.s <=3:
                e 6 "Знаешь, ты мог бы дать Тейну шанс стать частью твоих планов."
                e 1 "Я даже не вижу вас двоих в одной комнате половину времени."
                "Аксель насмехается."
                a "И пусть он прочитает мне лекцию о мире, любви и о том, как мне нужно следить за тем, сколько я ем. Пфф. "
                e 1 "Я действительно не понимаю, как вы двое связаны."
                a "Ну, он похож на свою мать."
                a "…"
                a "Он ворчит, как она, плохо готовит, как она, любит смотреть на деревню, как она.… у него даже ее глаза."
                hide axel stand with dissolve
                "Аксель подпирает щеку рукой и глубоко вздыхает."
                e 13 "Похоже, ты скучаешь по ней."
                show axel stand at center with dissolve
                a "Хм, а когда нет?"
                a "Каждый день он напоминает мне о ней, и обещание, которое она заставила меня держать, чтобы защитить его и направлять его, чтобы стать великим быком."
                a "Но мы с ним никогда не поймем друг друга. Мы слишком разные. "
                e 1 "Может быть, пришло время дать ему шанс, эта война уже разлучает вас."
                e 1 "Ты действительно хочешь потерять его навсегда?"
                a "..."
                "Бык подпирает подбородок кулаком и, кажется, обдумывает твои слова."
                jump Axel_tribe_talk1
            "Спросить, что делать ради забавы" if Axel.s <=2:
                e 1 "Здесь действительно не так уж много дел. Что вы, быки, вообще делаете для забавы?"
                a "Что ты имеешь в виду под \"нечего делать?\""
                a "Ты можешь бороться с воинами, можешь побить тренировочные манекены, даже можешь побороть детей на руках, если хочешь."
                e 9 "Почему все в этом списке - просто способ борьбы с кем-то."
                a "Ну, извини, принцесса. Если тебе нужна более изысканная работа,можешь предложить поработать с лавочником, чтобы изготовить несколько топоров для продажи."
                e 8 "Тогда я предпочитаю заниматься борьбой."
                a "Отлично, я просто был в настроении для хорошей драки. Давай."
                e 5 "Что? Здесь? Сейчас?"
                hide axel stand with dissolve
                "Аксель встает с трона и оставляет позади плащ."
                "Он стоит поперек тебя, расставив тяжелые ноги."
                show axel stand at center with dissolve
                a "Ну же, Блохастик, если ты сможешь одолеть меня, то сможешь одолеть и любых ящериц."
                "Ты сглатываешь и снимаешь меч."
                hide axel stand with dissolve
                "Ты держишь руки перед собой, вы оба кружите вокруг пустого пространства, ожидая друг от друга, когда что-то произойдет. "
                a "Ха!" with vpunch
                "Аксель бросается вперед быстрее, чем вы ожидаете."
                "Тебе удается поймать его за руки, но вес его тела в сочетании с его скоростью слишком силен, чтобы ты мог остановиться."
                "Ты падаешь на пол, и Вождь зажимает твое лицо между грудью."
                a "Да, давай толкай сильнее, если не хочешь, чтобы бычья вонь ударила тебе в лицо."
                "Твоя морда погребена под слоями потного жира и мышц, прижимающихся к тебе."
                "Ты сильно стучишь Акселя по спине, умоляя его слезть."
                a "Ха-ха-ха. - Что это? Хочешь еще быка? "
                "Его грудь сгибаются и фиксируют твою морду на месте."
                "Ты не можешь отойти от клешней Акселя."
                "Ты снова стучишь сильнее, твои крики о помощи заглушаются телом Акселя."
                "Хуже того, ты почувствовал, как что-то твердое упирается тебе в промежность и становится все больше, чем больше ты сопротивляешься.."
                e 9 "Бу-ху-ху!"
                "Он освобождает тебя с минуты на минуту. Ты задыхаешься от воздуха, вонь меха Акселя все еще застряла у тебя на носу"
                "Твой отдых не длится долго, он хватает тебя за затылок и толкает вниз."
                "Его ноги качаются через плечо, его бедра сгибаются и загоняют тебя в ловушку между ними."
                e 5 "Нет, нет, подожди!"
                "Аксель смеется и сильно прижимает твою голову к своей выпуклости"
                "Его стояк тычет тебе в глаза, но он толкает тебя дальше вниз, пока ты не окажешься глубоко между его яиц."
                a "Да, это запах быка!"
                "Острый аромат переполняет твои чувства."
                "Все, что ты чувствуешь, - это мускусные яйца Акселя."
                "Твои пинки и извивания не делают ничего, чтобы ослабить хватку его мощных бедер."
                "В конце концов, ты поддаешься усталости и просто упираешься лицом в яйца Акселя."
                "В этот момент он отпускает тебя и оставляет лежать на земле, смеясь от души, когда уходит."
                "Позже ты снова встаешь на ноги и собераешь свой меч и своё самообладание."
                show axel stand at center with dissolve
                a "Готов ко второму раунду?"
                e 9 "Нет!"
                jump Axel_tribe_talk1
            "Оставить" if True:
                jump Bull_tribe_tent

label Axel_bullkid:

    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Axel')
    $ renpy.music.set_volume(1, 4, channel = "Axel")

    window hide None
    stop music fadeout 1
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    scene bulltent with slow_dissolve
    "Inside, Chief Axel is scratching his chin while looking at the tent’s ceiling."
    show axel stand at center with dissolve
    e 1 "You called for me Chief Axel?"
    a "Hmm…"
    "His eyes fall on you, his hand drops onto his chest and he scratches the tuft of fur between his pecs."
    "You avert his powerful gaze."
    "It feels embarrassing the way he looks at you from top to bottom."
    a "Alright,I decided where I want to start with you."
    e 1 "...Pardon?"
    a "I’ve picked where we’re visiting today."
    a "You’re going to get a first hand experience of bull culture."
    e 6 "Bull culture? Aren’t I already experiencing it?"
    a "What by hanging around my son’s big behind every time?"
    a "I’m talking about real culture here, Fleabag. "
    a "Come on! I want to show you a special spot."
    hide axel stand at center with dissolve
    "The chief walks past you and out of the tent."
    $ renpy.music.set_volume(0, 5, channel = "Axel")
    "Mumbling under your breath you reluctantly follow Axel."
    $ renpy.music.set_pause(True, channel='Thane')
    $ renpy.music.set_volume(1, 5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
    $ renpy.music.set_pause(False, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    scene bulltribe 1 with slow_dissolve
    "He leads the way with wide strides."
    "It amazes you how a heavy set bull like him can move so fast. "
    "The two of you reach the open area right across from the general store, where two wooden bull dummies stand beside a wide empty field."
    scene tribe 1 with slow_dissolve
    show axel stand at center with dissolve
    a "Welcome to the training area."
    e 1 "Hmm, ok."
    "In the distance you can see two calves fighting each other with wooden swords."
    a "Take a look at that, makes my heart proud to know the youngins are still training."
    e 6 "Yeah, it’s good to see the kids still can have fun despite the fog."
    a "That’s what we’re all about Fleabag. Resilience."
    hide axel stand at center with dissolve
    "Axel crosses his arms and you both watch side by side as the two youths battle each other. "
    "One of them has the clearer advantage of being bigger and having longer limbs than the other. "
    "He easily dodges the smaller calves attacks."
    "The shorter one whose head barely reaches the taller one’s chest swings his weapon clumsily. "
    "His slow swings and clumsy posture are unlike a young child who just learnt to hold a weapon."
    show axel stand at center with dissolve
    a " This place used to see a whole lot more bulls training here."
    a "Everyone would try their hand to prove themselves here."
    a "If you could beat everyone you had the bragging rights to call yourself the strongest, and to challenge the chief even."
    e 1 "That sounds like you’re putting your job on the line here."
    a "It’s only fair Fleabag, to claim the title of chief you have to show everyone why they should listen to you, and the battlefield accepts all fighting styles. "
    e 1 "So, you actually beat all the bulls in the village before?"
    a "All those that would challenge my claim to the rank of chief. Thane will have to do the same someday…"
    e 1 "You think he can do it? Prove to everyone he can be chief?"
    a "…"
    hide axel stand at center with dissolve
    "The old bull looks on ahead, his eyebrows furrow while he watches the battle in front of him."
    a "I hope so. "
    "Axel shakes his head, and snorts."
    show axel stand at center with dissolve
    a "Here’s something interesting about this place, this is also where we settle most of our disagreements."
    a "You don’t like something about someone, you fight them off here."
    e 1 "Must everything be solved here with fighting?"
    "Just then you hear a loud yell."
    $ renpy.music.set_volume(0.8, 5, channel = "Chan1")
    hide axel stand at center with dissolve
    "Small calf" "I WILL KILL YOU!!"
    show black2
    show bullkid01 at center with dissolve
    "The two calves from earlier are now rolling on the floor."
    "Dust is floating everywhere as the shorter calf relentlessly tries to pound the bigger calf in the face."
    e 9 "Woah, what the heck, we got to stop them. "
    "You rush over to the two calves but Axel stops you by pulling you by the arm."
    a "Just let them fight, that’s how boys settle their problems around here."
    e 12 "Not like this, they’re going to kill each other. Now let's go!"
    "Axel releases his hold and rolls his eyes as he follows you towards the duo."
    hide bullkid01 with dissolve
    hide black2 with dissolve
    "You manage to grab the smaller calf by the armpits and pull him off the other one."
    "Small calf" "I’m going to kill you!"
    "It takes a lot of energy out of you to drag the calf away as he thrashes about."
    "Axel helps the other calf up on his feet."
    "The teenage bull pulls himself up and calmly brushes the dirt off of his face."
    "Small calf" "Die! Just die you stupid jerk!"
    show axel stand at center with dissolve
    a "What’s all this about?"
    "Teenage calf" "Chief Axel, I-I’m sorry for the trouble."
    "Teenage calf" "My little brother is just being a brat."
    "Small calf" "You shut up!" with vpunch
    "Small calf" "Tell him the truth! You horrible, terrible, ass fart!"
    e 5 "Woah, calm down kid."
    "Small calf" "Let me go! He needs to pay for what he did!"
    "Teenage calf" "Oh, quit being so dramatic. I apologized for it already."
    "Teenage calf" "Why can’t you let it go."
    "Small calf" "You know why!"
    "Small calf" "You killed what’s left of mommy! Murderer!"
    a "Enough! Get your tails in line!" with vpunch
    hide axel stand at center with dissolve
    "Chief Axel’s booming voice silences the arguing siblings."
    "Finally, you can let go of the smaller calf."
    "The two young boys lined up in front of Axel."
    "The smaller calf sniffles loudly, fighting back his tears."
    "His shoulders won’t stop trembling. "
    show axel stand at center with dissolve
    a "You, the big brother, explain what’s going on."
    "Taller calf" "My little brother is upset that I broke his toy yesterday by accident."
    "Small calf" "You lie!" with vpunch
    "Small calf" "You did it on purpose, you hated mommy, and wanted to break what she left to me!"
    "Taller calf" "I did not! It was an accident, I didn’t see where you stu- where your toy was!"
    hide axel stand at center with dissolve
    e 9 "Was that toy really important? Can’t your parents replace it?"
    "Small calf" "Mommy’s gone. She left daddy, and left the tribe."
    "The small calf sobs loudly, he doesn’t try to hide his sadness anymore."
    "Small calf" "You always hated her. It’s not fair!"
    "Small calf" "You broke mommy’s gift to me. I hate you! "
    "Taller calf" "What’s it going to take for you to forgive me? If I could have fixed it I would have."
    "Taller calf" "Look we’re causing a lot of trouble to the chief as is."
    "Taller calf" "Quit being such a whiny calf!"
    "Small calf" "Shut up! I don’t want to see you anymore, I hate you, I hate you!"
    show axel stand at center with dissolve
    a "Quiet! I’ve heard enough."
    "The two calves freeze in their spot and look to the chief with frightened eyes."
    a "You, the older brother, I hear you are responsible for breaking your little brother’s prized possession."
    a "Am I right?"
    "Taller calf" "I.. did."
    $ renpy.music.set_volume(0.3, 5, channel = "Chan1")
    a "Then it’s decided, the only way to solve this is for your little brother to exact his vengeance."
    a "As you’ve said little one, he is your brother no more."
    a "I hereby decree a final battle."
    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    e 5 "What final battle? You want them to kill each other?"
    $ renpy.music.set_volume(0.3, 10, channel = "Axel")
    a "No, the small one, you will strike your older brother down, and in doing so ends your ties with him, you two will be brothers no more!"
    e 9 "Just hold it, that’s way too drastic."
    a "Quiet, Fleabag. You wanted an intervention, you got one."
    a "My word is law. Now ready yourselves!"
    "The two smaller bulls look at each other with trepidation."
    "Reluctantly, the taller bull turns to face his sibling. "
    "His little brother looks to the ground with clenched fists and his tears falling to the ground."
    hide axel stand at center with dissolve
    "Axel twists his head to his side, signaling to you to come over."
    "You obey, but you give Axel a long and dark stare, questioning his judgement."
    "The stage falls silent as all eyes are on the two children."
    "Uneasiness fills the pit of your stomach."
    "Small calf" "Yaargh!"
    "The small calf rushes forward his arms in the air, then he throws his punch."
    "Like the wind the punch flies so quickly you can’t catch sight of it."
    $ renpy.music.set_volume(0, 3, channel = "Axel")
    "His big brother flinches and closes his eyes."
    pause 3
    "Everything ends in a blink of an eye. "
    "The little brother’s fist hangs in mid-air just inches away from his big brother’s snout. "
    "His cries cut through the silence, he tries to muster something to say, but all you hear are tears, and the sniffling of a sad child."
    $ renpy.music.set_volume(1, 10, channel = "Axel")
    "Small calf" "I’m sorry… "
    "He sobs."
    "Small calf" "Don’t take my big brother away…"
    "Small calf" "I don’t want to lose anyone anymore."
    "The taller calf opens his eyes and slowly pulls his brother close, letting him cry into fur."
    "Taller calf" "Forgive us chief, for the trouble we caused."
    "Small calf" "I’m sorry…"
    show axel stand at center with dissolve
    a "Tell me, what was the broken toy?"
    "Taller calf" "A small bow our mother made, she gave it to him before she left."
    "Taller calf" "I could fix it with some materials but I don’t have the coins to buy them."
    a "Then take this."
    hide axel stand at center with dissolve
    "Axel hands the older brother a bag of coins."
    show axel stand at center with dissolve
    a "There should be enough there to patch up the bow and to get you two a small snack to share. "
    "Taller calf" "Thank you Chief Axel. Hey, go on, say thanks."
    "Small calf" "Thank you, Chief Axel."
    "The small calf’s eyes are red from all the crying, and his voice is hoarse. "
    "Axel kneels down and wipes the small calf’s face with his cape."
    hide axel stand at center with dissolve
    a "You’re welcome little one. You did a good thing today giving your brother a chance."
    a "That kind of strength at such a young age, I think you’ll go far."
    a "Promise me you’ll try to be kinder to each other."
    "Small calf" "I promise."
    show axel stand at center with dissolve
    a "Good, now go on you two. I’ve got a tour to finish with our friend Brother Fleabag here."
    "Taller calf" "Good bye Chief Axel, Brother Fleabag."
    "Small calf" "Good bye Chief Axel and Brother Fleabag."
    e 8 "Ah."
    hide axel stand at center with dissolve
    "As the children leave, Axel laughs heartily while smacking you in the back three times, you almost fall over from his strong slap."
    "He then leads the way back to his tent, and you follow from behind."
    scene bulltribe 1 with slow_dissolve
    e 1 "Did you know the little brother wouldn’t hit his big brother?"
    a "Like I said the training grounds is where disputes are handled."
    a "All I did was give them a little push in the right direction."
    "Axel throws you a cocky grin."
    e 1 "Your methods are… risky."
    a "Yeah well it gets the job done."
    a "Sometimes you need tough love to get people to be honest about their feelings. "
    a "Action speaks louder than words, that’s something you got to remember Fleabag. "
    e 13 "I’ll keep that in mind. It was nice of you to pay for the calves to fix the toy."
    a "Don’t go spreading it around Fleabag, last thing I need is for my men to think I have gold to give around like leaves. "
    "While Axel walks up ahead, you become aware of his broad back, and you start to see the shadow of a father that the chief is."
    "You wonder if he sees the village as his child as well, and the way he rules is like a father showing his tough love."
    scene tent 1 with slow_dissolve
    show axel stand at center with dissolve
    "The moment you both reach the top of the steps. Axel turns to you with arms crossed."
    a "Alright, that’s the end of the tour for today. Check up with me to see if I’m free for another tour."
    e 1 "I look forward to it."
    a "You better, damn stairs make my thighs burn."
    hide axel stand at center with dissolve
    scene black with slow_dissolve
    "You bow and the bovian chief takes his leave into his tent."
    "<[name] gained one Level-up-point.>"
    $ Zalt.points = Zalt.points +1
    $ Time.hours = Time.hours + 2
    jump Bull_tribe_map

label Axel_letter:
    if Quest.bomba == 1:
        e 1 "Chief Axel."
        show axel stand at center with dissolve
        a "You have some balls to keep me waiting Fleabag."
        e 13 "Right..."
        a "Let's get down to brass tacks."
        a "I have a message that needs to be sent to the lizards. One that can only be sent via a catapult."
        e 1 "A catapult?"
        a "Yes, making weapons is our tribe’s specialty. We scraped what limited materials we could to make it."
        e 1 "I don’t get what kind of message you can send with a catapult?"
        hide axel stand at center with dissolve
        a "They will understand everything, with this."
        show bullbomb at center with slow_dissolve
        "He pulls out from behind his seat what looks like a crudely made spherical bomb wrapped in some kind of paper material, its fuse sticks right up."
        hide bullbomb at center with dissolve
        show axel stand at center with dissolve
        a "Your job is simple, take the bomb to the catapult that’s already set up at the swamp."
        a "One of my men who’s been scouting the area knows the proper trajectory for the bomb to hit their ceremonial stage."
        e 5 "If you needed someone to just deliver something for you I’m sure you have many other options besides me."
        a "You’re a better choice. Faster, smaller, there would be less risk of you getting caught by the lizards."
        e 13 "Still, this is a dangerous move, innocent people could get hurt."
        a "It won't, I know of their ceremonial stage, it is mostly unguarded."
        a "And even if a few lizards are lost that works in our favour."
        hide axel stand at center with dissolve
        "Axel crosses his arms and locks eyes with you. "
        show axel stand at center with dissolve
        a "The lizards brought this upon themselves."
        a "They should consider themselves lucky that they even get a warning shot."
        a "The longer I delay, my men will think I am unfit to lead them in this war."
        a "The lizards already had an upper hand when they sent their spy."
        e 5 "Wait, did the spy take something important?"
        a "It’s not what the spy took, it’s what they left."
        a "It was also Nauxus’s way of saying he could have me killed anytime, and I refuse to have him have the satisfaction thinking I am just a bug dancing on the palm of his hands."
        e 1 "…"
        e 13 "I will need some time to think it over."
        if Quest.campw1 == 4:
            a "Really? After all I just said you’re leaving me with a maybe?"
            a "If Tomahawk was still around I could rely on him to do this."
            a "If you won’t do this job out of respect for me, at least have the decency to respect the dead who you abandoned. "
            a "Now out!"
        elif True:
            a "Really? I just gave a long winded explanation and you’re leaving me with a maybe?"
            a "Tsk, if only Tomahawk isn’t recovering from his freak blow to the head, I could have him do this job, at least he doesn’t need so much convincing."
            a "Now out!"

        hide axel stand at center with dissolve
        "You gulp and leave the tent."
        $ renpy.music.set_pause(True, channel='Thane')
        $ renpy.music.set_pause(True, channel='Axel')
        scene black with dissolve
        "..."
        if Time.hours >= 6 and Time.hours <= 17:
            scene bulltribe 1 with vslow_dissolve
        elif True:
            scene bulltribe 1n with vslow_dissolve

        $ Quest.bomba = 2
        if Quest.bombn == 1:
            e 13 "(So Chief Axel plans to launch an attack on the lizard tribe using a catapult and a bomb."
            e 1 "(Do I want to go through with it?)"
            e 1 "No wait, I need to find out what Nauxus wants first."
        elif True:
            e 13 "Great, so I have one chief that wants to bomb a village, and the other wants to recruit more lizards for his army."
            e 1 "(Do I pick a side or see Thane for his advice?)"
            $ Quest.bombt = 1
            $ Quest.bomb = 2
        jump Bull_tribe_map


    elif Quest.bomba == 2 and Quest.bombn == 2 and Quest.bomb == 2:
        show axel stand at center with dissolve
        a "You ready to send this bomb to those bloody lizards?"
        if Quest.bombt != 3:
            "{b}{color=#ffd65c}<Warning:{p} You can't change your option anymore after this option.>{/color}"
        menu:
            "Yes" if True:
                e 1 "I’m ready."
                $ jane_inv_K.take(real_bomb)
                show bullbomb at center with slow_dissolve
                "Axel hands you the bomb."
                hide bullbomb at center with slow_dissolve
                a "Meet my man at the entrance to the lizard tribe, it’s the swampy area before you enter their village. He knows to expect a delivery."
                a "He’ll hand you your reward as well. Don’t damage the bomb, it’s the only one we are able to make."
                e 1 "Alright. I just need to give the bull the bomb, and I’m done."
                $ Quest.bomba = 3
                $ Quest.bomb = 3
                if Quest.bombt == 3:
                    hide axel stand at center with dissolve
                    scene bulltribe 1 with slow_dissolve
                    "You leave the tent and casually make your way out of the village."
                    stop Axel
                    scene forest 3 with slow_dissolve
                    show bullbomb at left with slow_dissolve
                    show bullbomb2 at right with slow_dissolve
                    "You make sure that you recognize which is the original bomb in your satchel."
                    hide bullbomb2 with slow_dissolve
                    show bullbomb at center with slow_dissolve
                    "Once you are at a decent distance from the bull village and that no one is around you pull out the original bomb."
                    "With your claws you rip through its shell and let loose the explosive powder inside."
                    hide bullbomb at center with slow_dissolve
                    "As long as the powder is not contained in a small space, it should do no harm."
                    "You then rip apart the bomb’s outer body and scatter its ripped remains among the trees."
                    "Now all that’s left is to head to the swamp."
                    $ jane_inv_K.drop(real_bomb)
                    jump forest_map
                elif True:
                    hide axel stand at center with dissolve
                    jump Bull_tribe_tent
            "No" if True:
                e 13 "Not yet, I’m still preparing."
                a "Then don’t waste my time standing here."
                jump Bull_tribe_tent
    elif Quest.bomba == 3 and Quest.bombn == 2 and Quest.bomb == 3:
        a "Get your tail into gear and deliver that bomb to the swamp! Don’t make me tell you again!"
        jump Bull_tribe_tent
    elif Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bomb_bull ==2:
        $ Axel.talktree = 1
        if Quest.bomb_lizard == 3:
            $ Time.bomb = Time.days
        $ Quest.bomb_bull =3
        if Quest.bomb_result == Axel:
            a "I have good news Fleabag."
            a "The bomb hit its target."
            a "Those lizards will probably think twice before they try to make a move on us."
            e 13 "I was just doing my duty, Chief Axel."
            a "Now I’m in the mood to celebrate!"
            e 1 "What do you have in mind?"
            a "The Feast of Fire will come soon. It’ll be the perfect time to rouse the spirits of the bulls."
            e 1 "I’m not familiar with that festival. "
            a "It’s what our people have been doing since the ancient days."
            a "We eat, drink and dance the night away to give thanks to our ancestors."
            e 6 "It sounds like fun, what do you guys usually do?"
            a "Typical celebration stuff, we sing songs from our forefathers and usually the women and children would put on a nice stage show."
            a "You’ll like it. All I have to do is make sure we have enough resources for it."
            a "I’ll call you if we need any help."
            "He leans back against his seat."
            a "Now, I still have some time to kill. Do you need anything Fleabag?"
            jump Axel_tribe_talk1
        elif Quest.bomb_result == Nauxus:
            $ Time.aaxel = Time.days
            if Time.hours >= 6 and Time.hours <= 17:
                scene tribe 1 with vslow_dissolve
            elif True:
                scene tribe 1n with vslow_dissolve
            "You head for the chief’s tent wondering what happened to his plans to attack the lizard village. "
            if Time.hours >= 6 and Time.hours <= 17:
                scene tent 1 with vslow_dissolve
            elif True:
                scene tent 1n with vslow_dissolve
            "Strangely the guards who are usually outside of the tent are nowhere to be found."
            "The moment your hand touches the tent’s door you hear Axel shouting!"
            a "What kind of an imbecile are you?" with vpunch
            a "Don’t you realize how much trouble you got yourself into?"
            a "You’re a fucking traitor now!"
            a "Do you think it’s easy to cover this up?"
            t "I don’t need you to cover anything up!"
            t "I did what I had to do, to stop you from crossing over into becoming a tyrant!"
            a "Why are you being so difficult? This is a war!"
            a "I’m doing what it takes to keep you and the village safe!"
            a "That bomb was a calculated attack, it was just to scare them off our backs!"
            t "You don’t know it would have worked!"
            t "And if I didn’t stop you now, you’re just going to escalate, and escalate!"
            a "Enough! You can plant your ungrateful ass on your rock and sit there until all of this is over! "
            t "I’m a grown bull, you can’t ground me!"
            a "Just watch me, I am chief, my word is law! Thane, as of now your tools will be confiscated and locked away. "
            a "And I’ll make sure if you so much as move from your rock I will come down hard on you like a thunderstorm!"
            t "This isn’t over!"
            show thane stand at center with dissolve
            "Thane suddenly bursts out from the tent forcing you to the side."
            hide thane stand at center with dissolve
            "He doesn’t even notice your presence."
            a "Thane!" with vpunch
            "He ignores his father’s call from the tent and continues walking down the lengthy steps. "
            "You poke your head through the tent’s entrance only to have Axel throw a heavy axe that narrowly misses your head."
            a "Get out!" with vpunch
            "You regret doing that."
            "Best to come back at a later time to talk to Axel and Thane."
            jump Bull_tribe_map0
        elif Quest.bomb_result == Thane:
            $ Time.aaxel = Time.days
            if Time.hours >= 6 and Time.hours <= 17:
                scene tribe 1 with vslow_dissolve
            elif True:
                scene tribe 1n with vslow_dissolve
            "Before you can head over to your meeting spot, a bull warrior stops you."
            "Bull warrior" "Hold it. The chief wants a word with you."
            e 6 "Can’t he wait? I have a meeting with Thane."
            "Bull warrior" "More reason for you to come along. Thane’s with him too."
            "You feel queasy in the stomach. This does not sound good for you or Thane."
            "You follow the warrior to the chief’s tent."
            scene bulltent with vslow_dissolve
            show thane stand1 at left with dissolve
            show axel stand at right with dissolve
            "Thane stands with his hands behind his back while he faces his father."
            "The chief eyes you with the same angry look Nauxus gave you earlier."
            e 1 "Chief Axel."
            a "…"
            hide axel stand at right with dissolve
            "He stands up and passes through you and Thane."
            "Poking his head out through the tent, you can hear him telling the guards outside to have an early break."
            show axel stand at right with dissolve
            a "So, I am not sure if you heard, but the bomb you delivered failed to go off."
            a "Instead, the scout heard sneezing in the distance."
            a "Know anything about that, Fleabag?"
            e 1 "I can’t say. I just dropped the bomb off, the bull checked it and I left."
            a "Really? You didn’t stop anywhere and maybe switched the bombs?"
            e 1 "No."
            "You try to deny it as convincingly as you can."
            "Axel strokes his chin and looks at you suspiciously."
            t "Where’s your proof? If you’re going to accuse people of things, you better have evidence."
            a "Proof?" with vpunch
            "Axel slams his fist on his armchair."
            a "You want proof? I was there when the bomb was made!"
            a "And I am bloody sure I didn’t put sneezing powder in it!"
            "Axel points accusingly at Thane."
            a "There’s only one bull in the whole village that I know who has the skills to make a decoy fast enough. "
            t "…"
            "Axel stands up, and approaches Thane who evades his gaze."
            a "Son, tell me you didn’t have something to do with this."
            t "…"
            a "Thane!"
            e 5 "He didn’t do anything. The bomb was just a dud!"
            t "No, I did it. I switched the bomb when [name] wasn’t looking."
            e 5 "Thane!"
            "The chief’s son looks at you and shakes his head."
            a "You're lying, he put you up to this didn't he?"
            "Axel points at you."
            t "No, ask me a million times and the answer will still stay the same."
            "You stand in shocked silence."
            hide thane stand1 at left with dissolve
            hide axel stand at right with dissolve
            "Thane's father grabs him by the shoulders and shakes him."
            "His nostrils flare up and his eyes bulge out intensly. "
            a "You take it back! Don't you know what you're saying?"
            "Thane pushes his father back with a huff and angrily points at him."
            show thane stand1 at left with dissolve
            show axel stand at right with dissolve
            t "No, never! I couldn't let you go through with your plans. You were going to kill innocent civilians with that thing!"
            a "You foolish calf! I planned everything from the start."
            a "That bomb was supposed to just hit their ceremonial stage, and the only casualties would have been the guards there!"
            t "You don’t know that!"
            t "It still could have hurt innocent bystanders!"
            t "How can you leave something so important to chance?"
            t "What kind of a chief are you?"
            a "Enough Thane! This is beyond selfish even for you!"
            a "Have you no consideration for the lengths I have to go through to keep this under wraps?"
            a "You’re putting yourself in grave danger. If anyone else finds out it’s punishable by banishment!"
            t "I don’t need your protection, father! I don’t need your protection!"
            t "I need you to listen to reason! Stop this pointless war!"
            "Axel clenches his fists and his face flushes red."
            t "I am doing what's right to protect the peace!"
            t "Something you never even tried to do! What kind of a chief does that?"
            "Axel snorts and stomps his hoof against the ground."
            "Thane doesn’t flinch and stands his ground against his father."
            a "Enough of this! We are done talking about this! The bomb was a dud, end of story!"
            "The chief turns to you, his eyes burn with anger and his fists look ready to strike."
            "You hold your breath fearing he will try to silence you after what you’ve heard."
            a "What did I say happened to the bomb mission Fleabag?"
            e 9 "The- the bomb was a dud. Nothing more."
            "Good, and if you so much as breathe a word about what happened here. "
            "Axel cracks his knuckles."
            a "Your head won’t leave this tent."
            "You gulp and nervously nod."
            t "Stop threatening my friend!"
            a " Don’t think you’re out of the woods either boy."
            a "As of now, all of your tools are confiscated, and I will keep a close eye on you."
            a "You so much as sneeze out of line, I’ll send you to the temple until you’re my age!"
            "Thane’s entire body trembles."
            "You can see him gritting his teeth, trying to hold back his tears."
            "You could only imagine what he might be feeling right now."
            t "Then do it! You’ll be happy right?"
            t "Keeping me aside like I’m never there!"
            t "That way you won’t have to look at your pathetic excuse of a son!"
            a "I didn’t say that!"
            t "You didn’t have to!"
            hide thane stand1 at left with dissolve
            "Thane turns away and leaves the tent."
            a "Thane. THANE!"
            hide axel stand at right with dissolve
            "Axel angrily grabs his own horns and lets out a loud grunt."
            "You decide to follow Thane and see if he’s alright."
            jump Thane_tribe_talk
    elif True:
        "U see this mean it's a bug"
        jump Bull_tribe_tent

label Axel_bomb_done:
    if Quest.bombt == 3:
        "As you trudge through the swamp, you’re unsure where exactly you’re supposed to find this bull."
        "Suddenly, a figure emerges from among the mangrove trees. It’s a bull warrior!"
        "Catapult Bull" "Hey, Brother Fleabag. I was told to expect you."
        e 1 "Umm… yeah. Where’s the catapult?"
        "Catapult Bull" "It’s in position. Had to hide it under some leaves and vines."
        "Catapult Bull" "Now give me the bomb, I’ve been here for so long the mosquitoes are having a buffet with my blood."
        show bullbomb2 at center with slow_dissolve
        "You hand the bull the fake bomb."
        hide bullbomb2 with slow_dissolve
        "He holds it close to his snout and eyes it suspiciously."
        "The fur on your back stands up on end. Will he figure out the bomb is a fake?"
        "The bull brings it close to his snout and sniffs it around."
        "Your heart rate starts beating uncomfortably fast."
        "The palms of your hands begin to sweat."
        "His eyes now fall on you."
        "He approaches, closer and closer."
        "And he pulls out a bag of coins."
        "Catapult Bull" "Here, your payment as Chief Axel instructed."
        e 5 "Oh… ok."
        "<[name] gained 250 coins>"
        $ jane_inv.take(coin,250)
        "Catapult Bull" "Yup, now get out of here. I have work to do."
        e 1 "Alright then."
        "You pretend to head off, wiping away your foot prints as you go."
        "Once you’re sure he cannot see you, you leap into the trees. "
        "Staying hidden up above, you follow the bull from behind until he leads you to the catapult."
        "You lay in wait...watching. "
        "The bull arrives at a pile of leaves and vines."
        "He removes them all to reveal a catapult built with random pieces of items from the bull tribe."
        "He places the bomb on the catapult and pulls out a pair of flint and steel."
        "With his tools, he ignites the bomb. The fuse starts burning."
        "He pulls the lever and the catapult launches the bomb into the air. "
        "As the bomb flies, the catapult crumbles away."
        "The bull watches for a few minutes."
        $ jane_inv_K.drop(fake_bomb)
        play sound "music/bomb-small.mp3"
        "A soft pop sound can be heard in the distance, followed by people sneezing."
        "Catapult Bull" "Damn, was that bomb a dud? Chief Axel will not like this."
        "Satisfied that the plan worked, you sneak away and head over to meet Nauxus."
        $ Quest.bombt = 4
        $ Quest.bomba = 4
        jump forest_map
    elif True:
        "As you trudge through the swamp, you’re unsure where exactly you’re supposed to find this bull."
        "Suddenly, a figure emerges from among the mangrove trees. It’s a bull warrior!"
        "Catapult Bull" "Hey, Brother Fleabag. I was told to expect you."
        e 1 "Umm… yeah. Where’s the catapult?"
        "Catapult Bull" "It’s in position. Had to hide it under some leaves and vines."
        "Catapult Bull" "Now give me the bomb, I’ve been here for so long the mosquitoes are having a buffet with my blood."
        show bullbomb at center with slow_dissolve
        "You hand the bull the bomb."
        hide bullbomb with slow_dissolve
        "He sniffs and knocks the bomb as though to inspect it."
        "Catapult Bull" "Alright, looks good."
        "Catapult Bull" "You might not want to be here when this thing is lit, this rudimentary catapult might just break and then we both might lose a limb or two."
        e 13 "Alright, then… Axel mentioned something about collecting my reward from you?"
        "Catapult Bull" "Oh yeah, here."
        "<[name] gained 400 coins>"
        "<[name] gained one Level-up-point.>"
        stop music fadeout 2
        $ jane_inv.take(coin,400)
        $ Zalt.points = Zalt.points +1
        scene black with slow_dissolve
        stop Chan1
        stop Chan2
        "You take your reward, and walk away."
        "You’re careful to distort your footprints left behind on the muddy ground."
        play sound "music/bomb-big.ogg"
        "As you make your way to the entrance of the swamp you hear a loud explosion from behind you, followed by harrowing screams."
        "You hesitate to turn back… but you don’t."
        "Clutching your fists you continue walking."
        "The job is done."
        $ Quest.bombt =5
        $ jane_inv_K.drop(real_bomb)
        $ Quest.bomb_end = 0
        $ Quest.bomba = 4
        $ Quest.bomb_lizard= 2
        $ Quest.bomb_bull= 2
        $ Quest.bomb = 5
        $ Quest.bomb_result = Axel
        $ Nauxus.s = Nauxus.s + 3

        jump forest_map0

label Axel_festival:
    if Quest.fesa ==1:
        "As you approach the tent, you see a female bull talking to Axel."
        "She appears distraught with her unkempt hair and a frantic look in her eyes."
        "Female Bull" "It took everything from the storage unit. We have no food for the festival!"
        a "Was it a lizard?"
        "Female Bull" "No, I don’t think so. Look at this bite mark."
        "She hands Axel something that fits in the palm of the chief’s hand. "
        "The chief holds up a half eaten apple and observes it from every angle."
        a "Did it leave a trail? "
        "Female Bull" "There’s a line of dropped fruits every few steps."
        a "Make sure nobody touches the crime scene."
        a "I'll get someone on it."
        "Axel then turns to you."
        show axel stand at center with dissolve
        a "Fleabag, I hope you’re not making a habit of eavesdropping on people’s conversations."
        e 9 "Never Chief Axel. It was just a coincidence. "
        a "Hpmh, that aside, as you might have overheard, something has stolen the fruits we gathered for the Feast of Fire."
        a "Now I can't imagine something more in the spirit of the festival than you bringing back those stolen delights."
        e 5 "I won’t hold my breath for all of the food to be returned though."
        e 5 "If it’s something that can take all of the fruits that was to feed an entire village."
        e 5 "Then it’s either really big or there’s going to be an army of them."
        a "Use your wits Fleabag, I’d spare you my men but there’s too much to do before the Festival can begin."
        a "Not to mention the amount of damage control that needs to be done."
        a "The kids have been looking forward to the celebration for so long."
        a "I’ll try to hold off on the ceremony until you show up with the fruits. "
        a "Are you ready to take the job? Time is of the essence."
        label Axel_festival_start:
            menu:
                "Yes" if True:
                    e 1 "I’m on it."
                    a "Good, then meet the shopkeeper and tell him I sent you."
                    a "He’ll give you a sack to help carry back the fruits. "
                    a "You’re looking for around 500 pieces of fruit."
                    a "Also,dispose of this while you’re at it."
                    "He hands you the half eaten apple."
                    e 1 "Oh…"
                    e 1 "I’ll hang on to it, in case I have trouble tracking the criminal."
                    a "One last thing before you go… it’s about Thane."
                    if Thane.movein == 0:
                        "Axel hans you a note."
                        "{u}{i}Gone out to hunt. Don’t wait for me.\n——Thane{/i}{/u}"
                        a "We found the note on his rock."
                        a "Did you see him on your way here?"
                        e 1 "Err… no. "
                        a "Hmm, so my ever defiant son wants to skip out on the festival."
                        a "He has no idea how disgraceful this will look with his seat empty."
                        e 1 "Maybe he needs some space after all that’s happened."
                        "Axel crosses his arms."
                        a "Well he can be in a ditch for all I care."
                        a "If he’s going to act like a brat, then it’s better he stays away."
                        a "Now go deal with the fruit thief."
                        "You bow with deference and take your leave."
                    elif True:
                        a "Did he say anything about coming back for the festival?"
                        e 6 "Coming back? I’m not sure I know what you mean Chief Axel."
                        a "Don’t play dumb, I know he’s staying in the tavern."
                        a "I have my sources."
                        e 1 "… Fine, he’s in the tavern and no, he didn’t mention anything about coming back."
                        a "Utterly irresponsible. He has no idea how disgraceful this will be with his seat empty during the ceremony."
                        e 13 "Maybe give him some space, a lot has happened recently."
                        a "He can have all the space he wants."
                        a "He’ll come crawling back once he learns he cannot survive out there without the tribe’s help."
                        a "Now go, this conversation has left a sour taste in my mouth."
                        e 1 "Yes Chief Axel."
                    hide axel stand at center with dissolve
                    $ Quest.fesa = 3
                    if Quest.fesn == 3:
                        scene tribe 1 with slow_dissolve
                        $ renpy.music.set_pause(True, channel='Axel')
                        e 13 "Both villages have been hit by the fruit thief."
                        e 13 "The timing is way too perfect to be coincidental."
                        e 1 "Not to mention…"
                        "You pull out the half eaten fruits you got from both villages."
                        e 1 "The bite marks on these two fruits are identical."
                        e 13 "So, I’m just dealing with one monster. "
                        e 1 "Any path I take to track down the creature won’t matter then."
                        jump Bull_tribe_map0
                    jump Bull_tribe_tent
                "No" if True:
                    e 6 "I still have something to deal with first. "
                    a "Move your ass Fleabag. This festival needs those fruits."
                    $ Quest.fesa = 2
                    hide axel stand at center with dissolve
                    jump Bull_tribe_tent
    elif Quest.fesa ==2:
        show axel stand at center with dissolve
        a "Don’t waste my time, are you going to help find those fruits or not?"
        jump Axel_festival_start
    elif Quest.fesa >=3 and Quest.fesa <=5:
        hide axel stand with dissolve
        "Axel is busy managing the tasks for the festival, he has no time to talk to you."
        jump Bull_tribe_tent
    elif True:
        jump Bull_tribe_tent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
