label battle_knight:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 350
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    scene prison 2 with slow_dissolve
    $ Battle.holyfcd = 0
    $ Map.good_battle = True
    stop music
    $ renpy.music.set_volume(0.5, 0, channel = "sound")
    play sound "music/whistle.mp3"
    "The sound of the whistle’s pitch echoes through the empty prison."
    pause 4
    $ renpy.music.set_volume(1, 4, channel = "sound")
    play music"music/metal_drag.ogg"
    "Then, you hear the sound of footsteps and metal dragging against the ground approaching you."
    "You turn and see something moving towards you. "
    show nohead knight with vslow_dissolve:
        zoom 0.8
        xalign 0.5 yalign 0.45
    "From the shadows a headless knight carrying a bloodied jagged sword appears. "
    pause 3
    "Although vaguely aware, but now you can officially confirm."
    "The creature swings its sword against the prison bars. "
    "Your ears fall flat against your head. "
    hide nohead knight with slow_dissolve
    "A strong sense of danger emanates from the knight. "
    "The headless knight suddenly swings its weapon narrowly cutting you across but you manage to side step away from the attack."
    show nohead knight with slow_dissolve:
        zoom 0.8
        xalign 0.5 yalign 0.45
    "Its motion is sluggish but is still deadly as the sword swings back and cuts through the stone floor."
    e 13 "So this is why you couldn’t go back to the children."
    e 1 "Very well, then I’ll end your suffering!"
    "You attack!"
    jump battle_knight_loop

label battle_knight_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show nohead knight:
        zoom 0.8
        xalign 0.5 yalign 0.45
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
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-30), Zalt.ATK-5)
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
            jump battle_knight_lose
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
            jump battle_knight_win

        $ Random = renpy.random.randint(1, 5)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The knight swings its sword across your face."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(40, 60)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The knight swings its sword across your face."
                "By blocking it with your sword you soften the blow but the force of its swing sends you flying."
                "Your body hits the wall."
        elif Random == 2 or Random == 3:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The knight smashes his sword repeatedly on the ground."
                "The broken pieces of the floor start to levitate with a dark aura and fly towards you at tremendous speed."
                "Но ты увернулся от его атаки!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The knight smashes his sword repeatedly on the ground."
                "The broken pieces of the floor start to levitate with a dark aura and fly towards you at tremendous speed."
                "You’re unable to block some of them and take damage."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The knight is trying to catch you."
                "But you dodged it!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 55)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "You’re caught by the throat in the knight’s vice grip."
                "You struggle and manage to kick yourself free."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_knight_win
        elif True:

            jump battle_knight_win

    elif Zalt.hp <= 0:
        jump battle_knight_lose
    elif Zalt.lust >= Zalt.maxlust:
        "Ты слишком возбужден, чтобы драться."
        "Ты падаешь на землю."
        jump battle_knight_lose
    elif True:
        jump battle_knight_loop


label battle_knight_win:
    play Chan2 "music/spooky_fight_end.ogg" noloop
    pause 1
    hide nohead knight with slow_dissolve
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    play sound "music/body_fall.mp3"
    "The knight falls onto its knees, but still clings to his sword for support. You pant heavily, tired from the grueling battle."
    "It extends out before collapsing entirely on the ground. "
    "Its body dissipates into dust and as its form breaks away you can hear the faint whisper of."
    show black3 at center
    show lionkey at center with dissolve
    $ jane_inv_K.take(lion_key)
    $ jane_inv_K.take(knight_badge)
    "The knight leaves behind a badge and a key on the floor. "
    hide black3 at center
    hide lionkey at center with dissolve
    "< You get the lion key >"
    "The moment your hand touches the Knight’s Badge your vision is enveloped by light."
    scene white1 with vslow_dissolve
    play music "music/small-bonfire.ogg"
    pause 4
    scene prison 4 with vslow_dissolve

    play sound "music/sword_clash.ogg"
    "You find yourself heading towards the steps to the prison."
    "You are shocked to find the royal performers fighting against your knights, but the performers are not alone. "
    play sound "music/sword_clash.ogg"
    "The prisoners that have been held captive are now loose on the castle grounds."
    "The knights are overpowered by the sheer number of attackers."
    show red1 with dissolve
    "You are ambushed by an attacker from behind, the blood spilling from your split head blurs your vision, but you can hear the villain’s maniacal laugh."
    "You draw your blade and attack ferociously at the usurpers, hacking and slashing at all the enemies that stand between you and your men."
    play sound "music/sword_clash.ogg"
    "Alas, you too fall to the overwhelming numbers. "
    "You would not relent, you choose to fight to the very end."
    scene black with slow_dissolve
    play sound "music/sword_clash.ogg"
    play sound "music/blood.ogg"
    "Then everything fades away when you feel a powerful cut at your neck."
    show red2 with slow_dissolve
    pause 2
    asm "“Your highnesses...”"
    hide red1 with dissolve
    hide red2 with dissolve
    play sound "music/body_fall.mp3"
    stop music
    pause 4
    $ renpy.music.set_pause(False, channel='Chan1')
    scene prison 1 with vslow_dissolve
    "You awaken with a loud gasp."
    "While sitting on the floor you frantically touch your neck just to make sure it’s still intact."
    "Once you’re assured that you are fine you poke at the badge, but the memories do not come to you again."
    "It’s safe to pick up the items now."
    "< You get the Knight’s Badge. >"
    "< You get 800 EXP. >"
    $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
    $ PPEXP = 50*Zalt.A_exp_lv
    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
    $ Zalt.exp = min(Zalt.exp+800, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    $ Map.castle_prison_7 = 4
    jump castle_prison

    return
label battle_knight_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    hide nohead knight with dissolve
    "The knight’s blade cuts through your right knee, ripping off every nerve and muscle. "
    e 0 "AAARRGGH!"
    scene black with slow_dissolve
    "You cry in anguish as your body falls."
    "But before your body hits the ground the knight pulls you by the fur on your head."
    "Tears fill your eyes as he raises his sword and swings for your neck."
    play sound "music/blood.ogg"
    "Snap!"
    show red2 at center with vslow_dissolve
    pause 3
    "{b}{color=#c22719}<GAME OVER>{/color}"
    menu:
        "New game" if True:
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
