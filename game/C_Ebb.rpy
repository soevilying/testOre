Господиномlabel Ebb_meet:
    stop music

    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    $ renpy.music.set_volume(0, 5, channel = "Chan2")

    $ renpy.music.set_pause(False, channel='Ebb')
    $ renpy.music.set_volume(0.8, 6, channel = "Ebb")

    $ Time.mins = Time.mins +5
    if Time.hours >= 6 and Time.hours <= 17:
        scene cabin 1 with slow_dissolve
    elif True:
        scene cabin 1n with slow_dissolve
    if Ebb.meet == 0:
        e 1 "Здрасте?"
        "В комнате беспорядок, здесь только диван, а все остальное выглядит так, как будто торнадо пронесся и все разрушил."
        "???" "ТЫ ПОСМЕЛ ВЕРНУТЬСЯ, ДЕМОН!" with vpunch
        "Из боковой двери появляется взъерошенная косатка, размахивая деревянной битой. "
        e 9 "Ух ты, успокойся. Я не демон!"
        "Ты отступаешь к выходу."
        "???" "Что?"
        show ebb stand at center with dissolve
        "косатка размахивает битой и смотрит на тебя."
        "Твои глаза притягиваются к его широким белым глазным повязкам, которые искажаются, образуя выражение замешательства."
        "Незнакомая косатка" "Мастер Сноу? - Это ты?"
        e 1 "М-м-м, нет.  [name], из таверны."
        hide ebb stand at center with dissolve
        "Услышав ваше представление, косатка опускает биту и поправляет пальто."
        "Затем он пытается поправить отсутствующий галстук, когда понимает, что делает, опускает руки и кланяется."
        show ebb stand at center with dissolve
        "Незнакомая косатка" "Воин из таверны! Пожалуйста, простите мое дурное поведение."
        "Незнакомая косатка" "Для меня было бы честью предложить Господину [name] чашечку чая."
        "Он жестом указывает на потрепанный диван в гостиной."
        "Каким-то образом его серебристый и низкий голос успокаивает."
        "Что делает тебя более осторожной с ним, чем раньше."
        e 1 "Нет, спасибо. Все происходит довольно быстро."
        e 1 "Прежде чем я  что-то от получу от вас, объясните, кто вы и что здесь делаете?"
        eb "Да, я Эбб, дворецкий молодого господина Фло."
        eb "Это наша скромная обитель на время, пока туман не рассеется."
        e 1 "Ты знаешь про таверну?"
        eb "Конечно, это первое место, где мы остановились, когда приехали. Мастер Сноу в добром здравии?"
        e 1 "Да, э-э-э, все в порядке."
        "Ты расслабляешься и убираешь меч в ножны."
        e 1 "Извини, просто надо быть осторожным с новыми лицами."
        eb "Это понятно, пожалуйста, присядьте хотя бы."
        hide ebb stand at center with dissolve
        if Time.hours >= 6 and Time.hours <= 17:
            scene ebbroom 1 with slow_dissolve
        elif True:
            scene ebbroom 1n with slow_dissolve
        "Не чувствуя злобы со стороны косатки, ты следуешь за ним в другую комнату."
        "Ткацкий станок занимает большую часть комнаты, но интерьер намного чище, чем беспорядок, который ты видел до этого."
        "Ты садишься в пустое кресло."
        "В то время как косатка стоит на другом конце комнаты, его руки сложены перед собой."
        "Твое тело тонет в подушках."
        show ebb stand at center with dissolve
        e 1 "Не хотите ли присесть и присоединиться ко мне?"
        eb "Ваше внимание ценно, Мастер [name], но дворецкому было бы неприлично сидеть с гостем."
        eb "Простите мне мою дерзость, но я должен спросить."
        eb "Мастер [name]’s присутствие здесь означает, что таверна решила помочь мне спасти моего Молодого Господина?"
        "Ты вздрагиваешь и смотришь на косатку, приподняв бровь."
        e 1 "Прости,Что? Спасти кого?"
        eb "Я искренне сожалею, но у меня сложилось впечатление, что мастер Сноу послал вас помочь мне с моей проблемой."
        e 1 "Просто начни с самого начала, что все это значит?"
        hide ebb stand at center with dissolve
        "Эбб сжимает руки и идет впереди тебя."
        "Он падает на колени и преклоняется перед тобой."
        "Чопорная и правильная костюм, который он носил, в одно мгновение разбивается вдребезги."
        eb "Пожалуйста, мне нужна помощь, умоляю вас, помогите мне спасти моего Молодого Господина."
        eb "Время на исходе, и я нахожусь в тупике."
        "Ты встаешь и держишь руки перед собой, отчаянно размахивая ими."
        e 5 "Эбб, вставай, я тебя выслушаю, но ты должен объяснить все."
        "Эбб подтягивается. Он все еще сидит на коленях, но его лицо светится надеждой."
        eb "Мастер [name], спасибо. Я не должен позволять отчаянию омрачать мои действия."
        eb "Я все еще должен защищать имя молодого мастера Фло."
        show ebb stand at center with dissolve
        "Эбб делает глубокий вдох, и его лицо снова принимает стоическое выражение."
        eb "Это случилось около недели назад, глубокой ночью, когда я услышал звон разбитого стекла в комнате Молодого Господина."
        eb "Я побежал с дивана в его комнату и увидел, как чудовище схватило перепуганного Молодого Господина за плечо."
        eb "Прежде чем я успел остановить его, существо прыгнуло на меня, я отбивался."
        eb "Мастер Фло звал на помощь, но существо было слишком сильным."
        eb "Он пронесся по гостиной, ломая всю нашу мебель. "
        eb "Сбив меня с ног, он выбежал из дома."
        eb "Я попыталась броситься в погоню, но в итоге сработали ловушки, которые я сама себе поставил."
        eb "Я был тяжело ранен, но сумел доползти до таверны."
        eb "Сноу и Уинтер помогли мне залатать рану, но когда я попросил их помочь спасти Молодого Господина, они отказались.."
        eb "Мастер Сноу отказался, сказав, что для него слишком опасно рисковать жизнью кого-то из таверны."
        e 5 "Это..."
        eb "Все в порядке, я не виню его, я не ожидал, что кто-то рискнет своей жизнью ради возможной самоубийственной миссии."
        hide ebb stand at center with dissolve
        "Эбб закрывает глаза руками и разбито качает головой."
        show ebb stand at center with dissolve
        eb "С каждой минутой мое сердце сжимается от страха перед тем, что случится с Молодым Господином."
        eb "Я пытался искать помощи в другом месте, но быки напали на меня без всякой причины ,а племя ящериц даже не пустило меня поговорить со своим вождем."
        e 1 "..."
        eb "Боже милостивый, как я расскажу его отцу, что подвел его сына?"
        "Обезумевшая косатка трогает твое сердце."
        "Но даже тебе трудно сказать что-то обнадеживающее, потому что ты боишься, что это будут просто пустые обещания, которые сломают его еще больше."
        "Все, что ты знаешь, это то, что он нуждается в помощи, и чем дольше проходит время, тем меньше шансов вернуть его Молодого Господина."
        e 13 "Ты слишком много думаешь Эбб."
        e 13 "Если то, что ты говоришь, правда, то у нас осталось не так уж много времени, чтобы спасти Фло. "
        eb "Ты действительно думаешь, что с ним все будет в порядке?"
        hide ebb stand at center with dissolve
        "Ты смотришь в пол, и нет никакого ответа, который мог бы сделать эту ситуацию менее ужасной."
        show ebb stand at center with dissolve
        e 13 "(Ох [name], Почему ты всегда любишь ввязываться в ненужные неприятности?)"
        e 1 "Оставайся сильным, Эбб, мы будем беспокоиться о его судьбе, когда найдем его."
        e 1 "А пока я помогу тебе вернуть его."
        hide ebb stand at center with dissolve
        "Эбб встает и притягивает тебя к себе, чтобы обнять."
        "Он начинает всхлипывать и сильнее прижимает тебя к своей груди."
        eb "Спасибо... спасибо..."
        e 1 "Эбб, пожалуйста, но нам нужно работать быстро."
        eb "Да, прошу прощения, это было неподобающе для дворецкого."
        "Он вырывается из объятий."
        show ebb stand at center with dissolve
        "Эбб встает, отворачивается и с минуту смотрит в потолок, прежде чем снова повернуться к тебе."
        "Косатка достает из кармана пару черных перчаток и протягивает тебе."
        eb "Это любимые перчатки Молодого Господина, вы можете выследить его по запаху."
        e 1 "Что еще я должен знать о Фло, чтобы выследить его?"
        eb "Это молодая акула, в этом году ей 19."
        eb "Он, вероятно, должен выделиться, если вы его найдете."
        e 1 "Ладно, сиди спокойно, я вернусь с новостями."
        eb "Спасибо Мастер [name], и, пожалуйста, поторопитесь."
        scene black with dissolve
        "Ты киваешь и выбегаешь из хижины, пока не выберешься из леса."
        if Time.hours >= 6 and Time.hours <= 17:
            scene lakecabin 1 with slow_dissolve
        elif True:
            scene lakecabin 1n with slow_dissolve
        e 1 "(Этот туман так много отнял у здешних людей.)"
        e 13 "(Я не могу позволить другому человеку так страдать.Надеюсь, что успею вовремя.)"
        "Ты достаешь пару перчаток и глубоко вдыхаешь запах их владельца."
        "Он пахнет морем, с оттенком пьянящего цветочного запаха."
        "Принюхиваясь, твой нос улавливает след, он ведет к мосту за таверной."
        $ Ebb.meet = 1
        $ Ebb.kidnap = 1
        jump forest_map

label Ebb_talk0:
    show ebb stand at center with dissolve
    if Ebb.necklace == 0 and Map.undercity_auc_start == 1:

        e 1 "Эбб, я нашел Фло."
        eb "Действительно? Где?" with vpunch
        e 13 "Его держат в заложниках как предмет аукциона."
        eb "Предмет аукциона? Что это за демоны?" with vpunch
        e 1 "Буквально демоны, мне нужно выкупить его."
        eb "Подожди, возьми это с собой."
        "Эбб вручает тебе ожерелье."
        e 1 "Что это?"
        eb "Единственный ценный предмет, который у нас есть."
        eb "Это ожерелье из семейной сокровищницы Молодого Господина."
        eb "Может быть, вы сможете продать его, чтобы получить немного монет."
        e 1 "Спасибо, я думаю, это поможет."
        eb "Приведите его домой, [name]."
        $ jane_inv_K.take(ebb_necklace,1)
        $ Ebb.necklace = 1
        hide ebb stand with dissolve
        jump lakecabin_ebbroom
    elif True:
        if Ebb.kidnap == 4:
            eb "Еще раз спасибо Мастер [name]."
        elif True:

            eb "Мастер [name], есть новости о Молодом Господине?"
            e 1 "Пока нет, поиски займут некоторое время."
            eb "А, понятно. Пожалуйста, дайте мне знать, если что-нибудь найдете."
            eb "Чем дольше Молодой Господин отсутствует, тем сильнее болит мое сердце. "
            e 1 "Оставайся сильным, Эбб, мы вернем его."

    hide ebb stand with dissolve
    jump lakecabin_ebbroom

label Ebb_kidnap_end:
    if Time.hours >= 6 and Time.hours <= 17:
        scene lakecabin 1 with vslow_dissolve
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
    elif True:
        scene lakecabin 1n with vslow_dissolve
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
    if Flo.meet == 1:
        "Когда ты стучишь в дверь хижины, то слышишь торопливые шаги Эбба, бегущего к двери."
        play sound "music/door.mp3"
        "Дверь распахивается."
        show flo stand01 with slow_dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        show ebb stand at right with dissolve
        eb "Молодой господин! Вы в безопасности!" with vpunch
        "косатка радостно бросается вперед и хватает Фло на руки, раскачивая акулу из стороны в сторону в крепких объятиях."
        eb "Молодой господин! Я так волновалась."
        "Фло сердито хлопает Эбба по плечу. "
        f "Отпусти меня, ты!" with vpunch
        f "Я не хочу, чтобы меня обнимали!"
        "Эбб делает, как ему приказано, и отпускает Фло. "
        show flo stand01 with slow_dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        show ebb stand at right with dissolve
        f "Хм. "
        "Фло поворачивается к тебе."
        f "Спасибо [name] что касается спасения, то я предоставлю этой косатке вести с вами дела. "
        "Затем он поворачивается к косатке."
        f "Я буду в своей комнате. Мне нужно поспать."
        "Фло протискивается мимо дворецкого и направляется в свою комнату."
        hide flo stand01 with slow_dissolve
        hide ebb stand with dissolve
        pause 2
        play sound "music/door.mp3"
        show ebb stand at center with slow_dissolve
        pause 2
        eb "Пожалуйста, простите... поведение молодого господина."
        eb "На самом деле он очень благородный джентльмен."
        e 1 "Я знаю, что это не мое дело-совать нос в чужие дела, но вы двое будете в порядке?"
        e 13 "Он, похоже, не испытывал особого энтузиазма, возвращаясь сюда."
        eb "..."
        eb "Ну, я думаю, молодой Господин просто в шоке."
        eb "Ему просто нужно немного отдохнуть."
        eb "А теперь, пока я не забыл."
        eb "Здесь не так уж много, но примите это как награду за помощь."

        "<Ты получаешь 500 монет от Эбба>."
        $ jane_inv.take(coin,500)
        "<[name] получил два очка повышения уровня.>"
        $ Zalt.points = Zalt.points +2
        $ Flo.room = 1
        e 1 "Спасибо, я вернусь в таверну."
        e 1 "Вы знаете, где меня найти, если вам что-нибудь понадобится."
        eb "Конечно, еще раз спасибо, Мастер [name]."
        "Ты возвращаешься в таверну измученный сегодняшними событиями."
        jump forest_map0



    elif Flo.meet == -1:

        "Дойдя до хижины Эбба, ты просто стоишь там, потерянный и испуганный."
        "Ты не сдержал своего обещания."
        "Трудно даже постучать в дверь, как будто в твоих венах лед, который душит тебя, но ты прекрасно знаешь, что это чувство вины."
        "Стук. Стук."
        "Эбб открывает дверь."
        play sound "music/door.mp3"
        "Он смотрит на тебя с надеждой, но быстро понимает, что ты один."
        "Его слабая улыбка прерывается, рот слегка приоткрывается."
        show ebb stand at center with slow_dissolve
        eb "Где... где молодой господин?"
        "Его голос срывается ближе к концу, слезы накапливаются в нем."
        pause 3
        e 13 "Я... Мне очень жаль, Эбб."
        pause 3
        eb "Нет... скажи, что это не так. Пожалуйста, скажи, что это не так."
        hide ebb stand at center with slow_dissolve
        "Он хватает тебя за плечо и яростно трясет."
        "По его щекам текут слезы."
        eb "Нет... нет...нет-МОЛОДОЙ ГОСПОДИН!"
        "Его хватка ослабевает, когда он падает на колени и плачет."
        "Ты ничего не можешь сказать."
        eb "Я подвел тебя! Почему, боги, почему? АГГХХХХ!"
        e 9 "Отлив-"
        eb "Нет! Уходите, пожалуйста... просто оставьте меня в покое..."
        play sound "music/door.mp3"
        "Ты опускаешь голову."
        e 13 "Мне очень жаль."
        "С этими словами ты уходишь, и звук слез Эбба эхом разносится по безмолвному лесу, когда ты возвращаешься в таверну."
        $ Ebb.cry = Time.days
        jump saveflo_end
    elif True:
        "bug"

label saveflo_end:
    scene black with dissolve
    $ Ebb.tavern = 1
    $ Zalt.hp = Zalt.maxhp
    $ Zalt.mp = Zalt.maxmp
    if Time.hours >=21:
        $ Time.days = Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
    elif True:
        $ Time.hours = 6
        $ Time.mins = 30
    stop music
    "Чувствуя себя измученным событиями дня, вы сразу же отправляетесь спать."
    pause 3
    "The next day."
    play sound "music/door.mp3"
    pause 1
    scene tavern 1 with slow_dissolve
    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
    "When you reach the foot of the stairs, Witer pulls you to the side."
    show witer stand at center with dissolve
    w "Hey sweetie."
    e 6 "Hey Witer, what’s up?"
    w "I saw you yesterday, and you looked worse than the broken toy my youngest brother found in the dump."
    "You scratch the back of your neck."
    e 6 "It’s not a big deal."
    w "Don’t give me that. We’re in a magical foggy forest full of monsters."
    w "Everything is a big deal."
    e 1 "Well-"
    h "Hey, you asked him yet what’s bugging him?"
    show hakan stand at left with dissolve
    show witer stand at right with dissolve
    "Hakan suddenly appears behind you."
    "Witer puts his hands on his hips and shakes his head at Hakan."
    w "I was just getting to it before you came."
    c "So you know what’s bugging [name] now?"
    "Now Chet pops out from his spandrel and joins in on the conversation."
    e 1 "Ok, who else wants to know what happened to me? "
    "Snow then pops out from under the bar and everyone looks at him."
    s "What? I dropped a spoon, honest."
    e 13 "Alright, everyone gather around. It’s a long story."
    hide hakan stand at left with dissolve
    hide witer stand at right with dissolve
    scene black with vslow_dissolve
    "After everyone gathers, you share with them your whole adventure in the city of demons, the auction, and what happened to Flo."
    pause 3
    scene tavern 1 with slow_dissolve
    if Flo.meet == 1:
        show hakan stand at left with dissolve
        show witer stand at right with dissolve
        w "Wait, wait, wait."
        w "So, there is an actual city full of demons? This is insane!"
        w "What if they come after us? Oh, no."
        h "Then I’ll cut them in half before they even set an inch on tavern grounds."
        h "We’ve got to start having patrols again."
        hide witer stand at right with dissolve
        show snow stand1 at right with slow_dissolve
        s "Agreed, now we know there is a possible threat we have to be prepared."
        s "For all we know they could be the ones behind the fog."
        e 1 "I haven’t got a chance to find out about the fog from them."
        s "Then you’ll have to, somehow."
        s "They’ve let you in, they probably don’t see you as a threat."
        s "Gain their trust, learn what you can about what’s going on with the fog."
        e 1 "I’ll see what I can do."
        s "In the meantime, I’ll set up night time patrols for the rest of us."
        c "We probably should do something about the orca and the shark guy."
        c "It isn’t safe for them to be out there on their own."
        e 1 "I agree, maybe they can stay here?"
        show snow stand1 at right with dissolve
        s "I won’t mind, but I’m running a business."
        s "They’d have to pay for lodgings like anyone else."
        s "[name], you can invite them over. Say I want to talk to them."
        e 6 "Alright."
        jump map1
    elif True:
        "Everyone sits in silence when you tell them that you could not save Flo."
        show hakan stand at left with dissolve
        show snow stand at right with dissolve
        w "[name]..."
        h "Don’t blame yourself Fuzzbutt, you did everything you could."
        e 13 "Did I? I’m more worried about Ebb."
        "Snow puts a hand on your shoulder, and pats you reassuringly. "
        s "Then go to Ebb. We shouldn’t leave him alone at a time like this."
        s "Just as important, we now know there are literal demons walking among us."
        s "This changes things. We need to be more vigilant from here on in."
        s "I’m restarting the night patrol, while [name] learns if these demons have anything to do with the fog."
        e 1 "You’re not really asking me to go back there?"
        s "I am, because it’s the only suspect we have for now. Please, it’s all we have."
        "You close your eyes, and see Flo’s horrified face from before."
        "You breathe deeply."
        e 1 "Ok, I’ll get in and learn what I can."
        s "Good. Then for now, go see Ebb. Convince him to come to the tavern."
        e 1 "Alright."
        hide snow stand at right with dissolve
        hide hakan stand at right with dissolve
        jump map1




    jump map1
label Ebb_hang:
    $ Map.bathroom_0 = 1
    $ Ebb.room = 0
    $ Flo.room = 0
    $ Ebb.tavern = 2
    $ EF.meko = 1
    if Flo.meet == 1:
        $ EF.witer = 1
        $ EF.hakan = 1
        play sound "music/door.mp3"
        "You hurry to the shark and orca’s hut."
        "They are surprised to see you back so soon."
        if Time.hours >= 6 and Time.hours <= 17:
            scene cabin 1 with slow_dissolve
        elif True:
            scene cabin 1n with slow_dissolve
        show flo stand with slow_dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        show ebb stand at right with dissolve
        eb "Master [name], welcome."
        f "[name], what brings you here?"
        e 1 "I’ve got a proposal from Snow."
        e 1 "He wants to invite you guys to stay in the tavern."
        e 1 "We would all be safer together and since the hut has been attacked before it might not be as safe."
        e 6 "And we have a few tavern mates already, everyone is nice."
        f "I take it we won’t be living there for free?"
        e 6 "Yeah... but knowing Snow he lets people stay if they are willing to work."
        eb "I think it would be a great idea, this will give young master the perfect chance to make friends."
        "Flo smacks himself in the forehead with his hand."
        show flo stand01 with dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        f "Orca, please don’t embarrass me."
        eb "..."
        eb "Sorry, young master."
        show flo stand with dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        f "More importantly, I think moving is a good plan."
        f "Give us a few minutes to pack?"
        hide flo stand with dissolve
        hide ebb stand with dissolve
        scene black with slow_dissolve
        "You wait for Ebb and Flo to get their things before heading back to the tavern."
        pause 5
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0, 2, channel = "Chan1")
        scene tavern 1 with slow_dissolve
        play sound "music/door.mp3"
        play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
        "When you reach the tavern, you give the duo a quick introduction of everyone present."
        "Snow warmly greets the duo as well."
        show snow stand at left with dissolve
        show ebb stand at right with dissolve
        eb "The pleasure is ours Master Snow."
        hide ebb stand at right with dissolve

        show flo stand with slow_dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        f "Thank you for offering us shelter, we would be honoured to be among your staff."
        s "So polite for a young shark. Your parents raised you well."
        show flo stand01 with dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        pause 1
        show flo stand with slow_dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        f "Yeah..."
        "The tail fin on Flo’s head starts twitching."
        s "Is something wrong?"
        f "Oh no-"
        hide flo stand with dissolve
        "Flo grabs hold of his tail fin with both hands."
        show flo stand with slow_dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        f "It does that when it’s near a hot spring source, it’s an ability my family has had naturally."
        s "Really? Then that means, there’s a hot spring nearby!"
        f "I think so, it’s very close to get my fin to vibrate like this."
        s "Then I think I have the perfect job for you two."
        s "We’ll go and dig up this hot spring and extend the bath house so that we can fill it with the spring water."
        s "You both can run the bath house business, and I’ll take the payment from the work there as payment for room and board."
        s "Think you can handle running your own bath house business?"
        eb "We would be happy to help."
        show snow laugh at left with dissolve
        s "Great, then you can start with the bath house construction with us."
        s "We’ve got the tools and we can use the man power."
        show flo stand01 with slow_dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        f "Hmm..."
        show snow stand at left with dissolve
        s "Yes Flo?"
        f "Do I at least get my own room?"
        show snow stand1 at left with dissolve
        s "Oh, don’t you want your butler with you at all times?"
        f "Please, it’s bad enough I got to work with him."
        f "I would really appreciate having some privacy."
        "Ebb lowers his head upon hearing his young master does not want to be with him."
        s "No problem, the bath house has enough empty rooms for both of you and the supplies to run the place."
        s "In fact lets get you two to your rooms, and start working."
        hide snow stand1 at left with dissolve
        hide flo stand01 at left with dissolve
        "Snow escorts the both of them to the bath house."
        "Maybe you should ask Snow about the bathroom later."
        play Snow "music/char_snow.ogg"
        play Hakan "music/char_hakan.ogg"
        play Witer "music/char_witer.ogg"
        play Chet "music/char_chet.ogg"
        play Thane "music/thane.ogg"
        $ Map.bathroom = "EbbFlo"
        jump map1
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
        "You reach the hut that Ebb lives in."
        "The door is unlocked so you step in."
        play sound "music/door.mp3"
        if Time.hours >= 6 and Time.hours <= 17:
            scene cabin 1 with slow_dissolve
        elif True:
            scene cabin 1n with slow_dissolve
        e 1 "Ebb? Ebb I came to check- "
        pause 5
        "You could not speak."
        scene black with slow_dissolve
        "The sight before you was a kind of horror that could never be truly understood fully by any living person."
        "It’s the kind of sight that the mind instantly reels back the moment it confronts it."
        "Dozens upon dozens of reasons could be theorized as to how such a tragedy could happen, but none could fully satisfy."
        "It is the kind of tragedy that no one would wish on another person or to the people around them."
        "One could only wish that help was given before such a tragedy befell."
        "But for now, you know this. Ebb ended his life by way of hanging."
        if jane_inv_K.qty(ebb_necklace) == None:
            pass
        elif True:
            $ jane_inv_K.drop(ebb_necklace)
            "You place the necklace the orca gave you inside his grave."
            "It didn’t feel right to hang on to it."
        "After burying his body you leave the hut feeling broken."
        "You cannot recall the walk back to the tavern."
        "Everything is so hazy."
        "Your conscience weighs heavily upon your shoulders."
        pause 5
        scene tavern 1 with slow_dissolve
        "When you arrive at the tavern, you tell everyone what happened."
        "Nothing. Not one of them said anything. "
        "Witer walks over and hugs you."
        "He tries to reassure you that it isn’t your fault, but all you feel is hollow."
        scene black with vslow_dissolve
        "You take a day off from exploring to collect yourself."
        pause 5
        $ Time.days = Time.days+1
        $ Time.days = Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
        "With the time you have, you convince yourself that you need to continue the search for freedom, despite everything."
        "You need to move forward, for those who remain."
        pause 3
        play sound "music/door.mp3"
        scene tavern 1 with slow_dissolve
        play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1

        "When you enter the tavern everyone goes about their business as usual."
        "You are unsure if they are putting up a front to retain some form of normalcy or that one more death means nothing when every day someone is bound to die in this forest."
        "Snow calls you to the counter."
        e 1 "Hello Snow."
        show snow stand1 at center with dissolve
        s "Good to see you are up and about."
        s "There’s something I wanted to share with you."
        s "It’s about the services in the tavern."
        s "With recent events, I think it’s more important now to provide a place for the customers to unwind, and more importantly to not stink up my bar."
        e 6 "Are you talking about a toilet?"
        show snow stand at center with dissolve
        s "No, we already have that. I mean reopening the bath house."
        s "We were fortunate this morning, Witer was helping move out some things from the bath house, mostly junk to be buried. "
        s "While we were digging, Witer actually discovered a source of natural hot spring water."
        s "So it’s been decided that the bath house will be renovated so that everyone can use the hot spring."
        s "Once it's ready, you can be the first customer."
        e 13 "That does sound nice, thanks Snow."
        s "Hey, take it easy kid. You’ve been through a lot lately."
        s "The guys and I talked, and we figure we best keep things normal for you."
        e 1 "I know, just give me some time. I don’t want you guys to worry too much either."
        s "Promise you’ll talk to us if something is bothering you?"
        e 13 "I promise."
        s "Good."
        hide snow stand at center with dissolve
        "Maybe you should ask Snow about the bathroom later."
        play Snow "music/char_snow.ogg"
        play Hakan "music/char_hakan.ogg"
        play Witer "music/char_witer.ogg"
        play Chet "music/char_chet.ogg"
        play Thane "music/thane.ogg"
        $ Map.bathroom = "None"
        jump map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
