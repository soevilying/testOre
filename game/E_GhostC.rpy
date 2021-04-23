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
        "???" "Give me your..."
    elif Map.castle_ghost == 35:
        scene castle 5
        "???" "Help...me"
    elif Map.castle_ghost == 61:
        scene prison 5
        "???" "Please...no more, no more."
    elif Map.castle_ghost == 62:
        scene prison 5
        "???" "Hahhaahahhaha! Run!"






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
            "You swing your sword but it cannot hurt the phantom."

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
            "You cannot seduce a non living creature."
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
                "The phantom’s long arm extends forward and it grabs a large chunk of wood."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The phantom’s long arm extends forward and it grabs a large chunk of wood."
                "It beats you relentlessly with the weapon."
        elif Random == 2:
            $ wolf_damage = renpy.random.randint(20, 40)
            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
            "The phantom lets out an ear piercing screech that hurts your ears immensely."
        elif True:

            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The phantom forms a dark energy ball."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The phantom forms a dark energy ball and hits you square in the chest with it."
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
    "You land a powerful blow causing the phantom to scream and shrivel like a dried up fruit. Its form shrinks and disappears from view."
    "You get an ectoplasm and 200 EXP."
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
        "With the phantom out of the way, you are able to enter the room."
        "There’s a strange pattern on the floor. "
        e 5 "Is this some kind of demon circle?"
        "Random items are placed around the circle."
        "A skull, a dagger, and a few potions."
        e 13 "Talk about disturbing."
        "You pick up the potions and bolt out of the room."
        "You find one bottle of HP potion and one bottle of MP potion"
        $ jane_inv.take(hp_potion,1)
        $ jane_inv.take(mp_potion,1)
        jump castle_map
    elif Map.castle_ghost == 61:
        scene prison 5 with slow_dissolve
        e 13 "Great, so I got to be careful of inanimate objects now?"
        "You look at the remaining shelves in the room."
        "Should you check them?"
        menu:
            "Yes" if True:
                "You gulp and towards the next shelf across the room."
                "After all, you can’t be an adventurer if you didn’t take risks."
                "You take a step forward and the shelf in front of you transforms into a phantom."
                "It speeds towards you with an ear piercing screech."
                $ Map.castle_ghost = 62
                $ Map.castle_prison_6 = 2
                jump battle_GhostC
            "No" if True:
                $ Map.castle_prison_6 = 2
                e 13 "No, it’s an unnecessary risk."
                e 1 "This room has been raided anyways. "
                jump castle_prison
    elif Map.castle_ghost == 62:
        $ Map.castle_prison_6 = 3
        "You find nothing here."
        e 13 "Everything rotted a long time ago."
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
    "The Phantom laughs maniacally and ascends into the air."
    "It’s form expands into a black cloud like someone dropped a single black ink drop into water."
    "There’s nowhere to run, the dark cloud descends upon you and suffocates you."
    "You struggle and try to hit the cloud but nothing happens."
    "As less and less air enters your lungs your vision starts to blur."
    "The cloud lifts your body upwards then drops it."
    scene black with vslow_dissolve
    "The last thing you remember is feeling your falling into a dark pit until you pass out."
    "When you reawaken you’re no longer in the castle."
    $ Zalt.hp = 1
    $ Zalt.cor = min(Zalt.cor+1,100)
    $ Zalt.Dungeon_leave = True
    jump castle_map
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
