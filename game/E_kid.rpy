label battle_kid:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 250
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0
    $ Map.good_battle = True
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    scene prison 2 with slow_dissolve
    $ Battle.holyfcd = 0
    stop music
    scene castle 4 with vslow_dissolve
    "This is a room with just a bucket inside it."
    pause 4
    "Inside one of the buckets, you find a crumpled piece of paper."
    "It reads..."
    "{u}{i}{color=#d41b19}Dear GOD.... Help me, they’re still here!{/i}{/u}{/color}"
    "{u}{i}{color=#d41b19}The children are still here!{/i}{/u}{/color}"
    "{u}{i}{color=#d41b19}I can’t see them, but I can hear them.{/i}{/u}{/color}"
    "{u}{i}{color=#d41b19}Taunting me, laughing at me every minute of the day.{/i}{/u}{/color}"
    "{u}{i}{color=#d41b19}I can’t take it anymore!{/i}{/u}{/color}"
    "{u}{i}{color=#d41b19}They torment me... the voices... they torment me... {/i}{/u}{/color}"
    "{u}{i}{color=#d41b19}Why won’t the LAUGHTER STOP!{/i}{/u}{/color}"
    "{u}{i}{color=#d41b19}I KILLED YOU, I KILLED YOU BOTH.{/i}{/u}{/color}"
    "{u}{i}{color=#d41b19}NOW STAY DEAD!{/i}{/u}{/color}"
    e 9 "What the-"
    "A pair of hands grab you from the ground."
    e 9 "Ahh!" with vpunch
    "You kick the hands away and crawl over to the other side of the small room. "
    "Two pairs of translucent hands suddenly appear and grab at your fur."
    "The sound of children laughing echoes loudly inside the room."
    "You struggle and relentlessly punch the air to try to free yourself from their grasp."
    "Their hold slowly loosens and you are able to free yourself."
    "You draw your blade ready to fight."
    e 9 "Come on out and fight!"
    "From the floor two ghostly figures emerge."
    show kids with vslow_dissolve:
        zoom 0.6
        xalign 0.5 yalign 0.2
    "They are no taller than your hips and they cling to one another with a mysterious smile on their faces."
    "Child" "Let’s play!"
    "Child" "Stay and play with us."

    jump battle_kid_loop

label battle_kid_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show kids:
        zoom 0.6
        xalign 0.5 yalign 0.2
    stop music
    stop sound
    $ renpy.music.set_pause(False, channel='Chan2')
    $ renpy.music.set_volume(1, 0, channel = "Chan2")
    play Chan2[ "<silence 0.1>", "<loop 34.9983>music/spooky_fight.ogg" ]fadein 3




    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Святой Кулак":
            $ red_damage = renpy.random.randint(int((Zalt.MATK*2.1)-10), int((Zalt.MATK*2.5)-10))
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
                    "You unleash Holy Fist."
                elif True:
                    "С молниеносной скоростью ты поражаешь врага Святым Кулаком."
                " (Нанесенный урон - [red_damage]hp)"

        if res == "Предметы":
            $ Zalt.hp = min(Zalt.hp +5, Zalt.maxhp)
            $ cookies_left -= 1
            "*Глоток* 5hp восстановлено"

        if res == "Атака":
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-25), Zalt.ATK-5)
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
            jump battle_kid_lose
        if res == "Флиртовать":
            "You cannot seduce a non-living creature."
        if res == "Бандаж":
            $ Zalt.heal = renpy.random.randint((Zalt.int*3)+25, (Zalt.int*3)+40)
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
            "You can't run!."
        elif True:

            pass
        if wolf_hp <= 0:
            jump battle_kid_win
        $ Random = renpy.random.randint(1, 5)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The ghost’s teddy bear leaps off its arms and disappears. "
                "You can’t see where the bear went."
                "Then, you feel the bear appear behind you and try to bite."
                "You dodged its attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(30, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The ghost’s teddy bear leaps off its arms and disappears. "
                "You can’t see where the bear went."
                "Then, you feel a sharp pain in your right arm."
                "The bear bites you before teleporting back to its owner."
        elif Random == 2 or Random == 3:
            $ wolf_damage = renpy.random.randint(25, 40)
            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
            "The ghosts laugh and both fire a blast of cold air from their mouths."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The ghost holding the pillow tosses it in the air and it grows to the size of a wheelbarrow."
                "But you dodged it!"
            elif True:
                $ wolf_damage = renpy.random.randint(30, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The ghost holding the pillow tosses it in the air and it grows to the size of a wheelbarrow."
                "You’re unable to dodge as it hits you with a powerful force."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_kid_win
        elif True:

            jump battle_kid_win

    elif Zalt.hp <= 0:
        jump battle_kid_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_kid_lose
    elif True:
        jump battle_kid_loop


label battle_kid_win:
    play Chan2 "music/spooky_fight_end.ogg" noloop
    pause 1
    hide kids with slow_dissolve
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    play sound "music/body_fall.mp3"
    "Child" "Dad...where are you?"
    "Child" "We are... so scared."
    "The ghostly figures fall over and disappear in a puff of dust."
    "You are left standing dumbfounded after what happened."
    "Hopefully, that will be the last you’ll see of those ghosts."
    "The ghosts left behind something on the floor, you pick it up."
    "< You get the Prince Badge. >"
    "< You get 800 EXP. >"
    $ Zalt.exp = min(Zalt.exp+800, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    $ jane_inv_K.take(prince_badge)
    $ Map.castle_17 = 2
    $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
    $ PPEXP = 50*Zalt.A_exp_lv
    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
    jump castle_map

    return
label battle_kid_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    hide kids with dissolve
    "The giant pillow smacks you in the face and topples you to the ground. "
    "You push yourself up from the floor when suddenly pairs of rock hands emerge from the floors and grab at you from every side."
    e 0 "Help! Help!"
    scene black with slow_dissolve
    "The ghost children stand over your body and giggle."
    "Your struggles are futile, the hands are just too strong."
    "You panic when you realize that your body is sinking into the earth like its not even there."
    e 0 "No! No!"
    play sound "music/blood.ogg"
    show red2 at center with vslow_dissolve
    "The children shush you and you scream as your vision is plunged into darkness."
    pause 3
    "{b}{color=#c22719}<GAME OVER>{/color}"
    menu:
        "New game" if True:
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
