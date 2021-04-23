label battle_lizardcamp:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 170
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ Battle.holyfcd = 0
    $ Map.good_battle = True
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    stop music








    jump battle_lizardcamp_loop


label battle_lizardcamp_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show lizardw at center
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
            jump battle_lizardcamp_lose
        if res == "Флиртовать":
            $ Random = renpy.random.randint(1, 7)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You successfully jump behind the lizard and plunge your hands down his loincloth."
                "You find his thin slit and gently massage its entrance before jumping away."
                "The lizard is confused and breathing heavily."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You tease the lizard by playing with your nipples and motioning him to join you."
                "The lizard darts his tongue out with a lewd smile, you can tell he wants more."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You strike a series of poses with a confident smile."
                "He gasps loudly and grabs his groin as though trying to hide it from view."
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You successfully jump behind the lizard and plunge your hands down his loincloth."
                    "You find his thin slit and gently massage its entrance before jumping away."
                    "The lizard growls angrily at you and swats his spear at you."
                elif Random == 2:
                    "You tease the lizard by playing with your nipples and motioning him to join you."
                    "He spits on the ground and angrily cuts the air with his dagger."
                elif True:
                    "You strike a series of poses with a confident smile."
                    "He ignores your seduction."
            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                jump battle_lizardcamp_win
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
            "You can't run!"
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_lizardcamp_win
        $ Random = renpy.random.randint(1, 4)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The spy cuts you with his dagger."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(25, 45)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The spy cuts you with his dagger. It burns deep into your flesh."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The lizard spy plunges his spear into your arm."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(25, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The lizard spy plunges his spear into your arm."


        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_lizardcamp_win
        elif True:

            jump battle_lizardcamp_win

    elif Zalt.hp <= 0:
        jump battle_lizardcamp_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_lizardcamp_lose
    elif True:
        jump battle_lizardcamp_loop


label battle_lizardcamp_win:
    if Foe.lizardcamp ==2:
        play music "music/forest_fight_friend_end.ogg" noloop
        pause 1
        hide lizardw with slow_dissolve
        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item
    elif True:
        hide lizardw with dissolve
        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item

    $ Foe.lizardcamp = Foe.lizardcamp+1
    if Foe.lizardcamp ==1:
        "The lizard warrior attempts to escape."
        "You grab his tail and pull him back."
        play sound "music/blood.ogg"
        "With his neck within reach, you slash your blade across, blood spurts out of his neck."
        "His voice becomes an unintelligible garble now as his body slumps to its knees."
        "You plunge your sword through the lizard’s chest effectively ending his life."
        "But the battle is far from over, two of the bulls are groan in pain as the second lizard warrior fires darts onto their necks."
        "The bulls are unable to move."
        "You rush in and block the lizard warrior from dealing the finishing blow."
        jump battle_lizardcamp
    elif True:
        "The lizard warrior loses the strength to stand. He holds onto his spear for support."
        "You approach him with your sword ready."
        "He looks up at you, blood dripping from his skull, the anger in his eyes is palpable. "
        "Second Lizard Warrior" "You’re scum!"
        "You slash your sword with enough force that it slices through his neck, sending his head flying through the air."
        "Silence fills the space."
        "The paralyzed duo from earlier fall to their knees but have regain their ability to move."
        "While the bulls check on each other, you walk over to the remains of the dead lizard warrior holding the stones earlier."
        "Crouching down you rummage through his belongings."
        "You pull out four stones with spiral like carvings around them."
        "First Bull Warrior" "Hey, those are runestones."
        "The bull stands over your shoulder and uses his finger to move the runestones around in the palm of your hand."
        "The other join to see what you’ve found."
        e 1 "Do you think they were planning to use this to set up their campsite?"
        "Second Bull Warrior" "Most definitely, what they say again? "
        "Second Bull Warrior" "Err, you just got to think about who you want to keep out and the stone will glow."
        "Third Bull Warrior" "Give it a try."
        e 1 "Ok, Give me a sec."
        "You concentrate on the idea to keep out those who would hard the bull tribe and its allies. "
        "After a few seconds your hand starts to warm and the stones glow a faint yellow glow."
        "First Bull Warrior" "Is it working?"
        e 1 "One way to find out. You guys dispose of the body, and I’ll plant these stones around."
        "The bulls do as you command and get rid of the lizards’s corpses."
        "It doesn’t take too long for the stones to be placed around the campsite."
        "Second Bull Warrior" "Let’s test it out."
        "First Bull Warrior" "Fine, but you stay far far away from us."
        "First Bull Warrior" "This here is lizard magic, you don’t know what it’ll do."
        "Second Bull Warrior" "You sound like a weak lizard when you say that."
        "The second bull warrior walks out of the range from where you planted the runestones."
        "He draws out his axe and comes charging."
        "Second Bull Warrior: Yargh!"
        "Klunk!" with vpunch
        "He stops dead in his tracks. His face is squished like he is pressing it against a glass wall."
        "Third Bull Warrior" "Huh, the runestones did work. He can’t get in cause he tried to attack us."
        "The second bull warrior pulls himself off the barrier."
        "Second Bull Warrior" "Hey, how do I get in?"
        "Fourth Bull Warrior" "Just stop wanting to hurt us."
        "Second Bull Warrior" "How am I supposed to do that? When he’s laughing his ass off at me?"
        scene black with slow_dissolve
        "You turn to the first bull warrior trying to suppress his laughter but he ends up snorting loudly with his hand over his mouth."
        "This goes on for some time before your team reunites and returns to the bull village."
        hide red1
        hide red2
        jump Axel_camp_end

    return
label battle_lizardcamp_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    if Foe.lizardcamp ==0:

        "Collapsing onto the ground from exhaustion, your enemy swiftly runs back a few feet before drawing their arrow."
        show red1 at center with dissolve
        play sound "music/blood.ogg"
        "Too injured to dodge, you see the tip of the arrow before it hits you dead in the eye."
        "You howl in pain as blood drips down your face."
        "A few more arrows sink into your body with each consecutive shot hurting more than the last."
        show red2 at center with dissolve
        play sound "music/blood.ogg"
        "You look with your only working eye now, as they take their time to nock another arrow."
        "The last thing you see before the world turns black is the lizard letting loose the arrow accompanied by a searing pain in both of your eye sockets."
        scene black with slow_dissolve
        "{b}{color=#c22719}<GAME OVER>{/color}"
        menu:
            "New game" if True:
                return
            "New game" if True:
                return
    elif Foe.lizardcamp ==1:

        "Disarming you with little ease, the lizard warrior pulls out a different blade never seen before."
        show red1 at center with dissolve
        play sound "music/blood.ogg"
        "He slash it across your chest before driving it hard into your abdomen."
        "You stumble backward as you try to apply pressure to your gaping wounds but your body collapses instead."
        "Your skin burns, breathing becomes impossible without feeling immense pain and soon, your whole body twitches uncontrollably as you try your best to fight against the poison."
        "It’s too much to handle as you start foaming at the mouth."
        show red2 at center with dissolve
        "The last thing you see through your bloodied eyes are the bodies of hulking bulls fall before you, receiving the same tainted fate. "
        scene black with slow_dissolve
        "{b}{color=#c22719}<GAME OVER>{/color}"
        menu:
            "New game" if True:
                return
            "New game" if True:
                return
    hide bullw with dissolve

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
