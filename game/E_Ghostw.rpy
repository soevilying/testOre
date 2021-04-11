label battle_ghost_w:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 80
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ Battle.holyfcd = 0
    $ Map.good_battle = True
    stop music
    if Witer.sleep == 4:
        "You go towards the side of the tavern where Hakan and Witer's room is located."
        "It takes a while for your eyes to adjust to the dark. You can faintly make out what's around you."
        "Thud!"
        "Thud."
        e 5 "Who's there?"
        "Thud."
        "Something flies by missing your face by an inch."
        "The thing lands behind you with a heavy thud. "
        "You quickly draw your blade before the object lunges at you."
        "It hits your blade and you fling it back as hard as you can."
        "It's a rock! No doubt about it."
        "A mysterious energy begins to envelope the rock and takes shape."
        "Whatever this is, you got to fight!"
    elif True:
        "You hear the familiar tapping from before."
        show ghost 02 at center with dissolve
        "A lone rock knocks against the basement window."
        e 12 "Get away from there!"
        "You attack!"






    jump battle_ghost_w_loop


label battle_ghost_w_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show ghost 02 at center
    play music "<loop 4.6903>music/forest_fight_small.ogg"




    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False

        if res == "Holy Fist":
            $ red_damage = renpy.random.randint(Zalt.MATK*2, int((Zalt.MATK*2.5)+10))
            $ wolf_hp -= red_damage
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            $ Battle.holyfcd = 3
            $ Random = renpy.random.randint(1, 3)
            if wolf_hp <= 0:
                pass
            elif True:
                if Random == 1:
                    "You dart forward and land a punch on the enemy."
                elif Random == 2:
                    "You hit the enemy with your Holy Fist."
                elif True:
                    "With blazing speed you hit the foe with Holy Fist."
                " (Damage dealt - [red_damage]hp)"

        if res == "Items":
            $ Zalt.hp = min(Zalt.hp +5, Zalt.maxhp)
            $ cookies_left -= 1
            "*Drink* 5hp restored"

        if res == "Attack":
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-20), Zalt.ATK)
            $ Random = renpy.random.randint(0, 100)
            $ wolf_hp -= 0
            "Your sword cuts through the phantom enemy, it appears unaffected by your attack!"
            e 0 "My attacks aren’t working. Is this some kind of an indestructible enemy?"

        if res == "Submit":
            e "I can't fight anymore.."
            "The enemy is too strong."
            "You’re knocked onto the ground."
            jump battle_ghost_w_lose
        if res == "Flirt":
            "You try to seduce the ghost, but it has no body to feel anything."
            pass
        if res == "Bind up":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Bind up* [Zalt.heal]hp restored"
        if res == "Hp potion":
            $ Zalt.heal = 60
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ jane_inv.drop(hp_potion)
            "*Hp potion* [Zalt.heal]hp restored"
        if res == "Mp potion":
            $ Zalt.heal = 60
            $ Zalt.mp = min(Zalt.mp+Zalt.heal, Zalt.maxmp)
            $ jane_inv.drop(mp_potion)
            "*Mp potion* [Zalt.heal]mp restored"
        if res == "Escape":
            "This thing’s too fast. You run from battle and head for the tavern, locking the front door tightly."
            "It doesn’t sound like the ghost is chasing you, you need to find a way to beat that thing. "
            if Witer.sleep == 4:
                $ Witer.sleep = 5
            hide screen simple_stats_screen
            hide screen battle_menu
            hide screen battle_skill
            hide screen battle_item
            stop music fadeout 1
            hide ghost 02
            jump map1
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_ghost_w_win
        $ Random = renpy.random.randint(1, 4)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "A phantom arm forms and claws at you."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(10, 20)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "A phantom arm forms and claws at you."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "A powerful force knocks you back."
                "But you dodged its attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(30, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "A powerful force knocks you back."


        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1





    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_ghost_w_win
        elif True:

            jump battle_ghost_w_win

    elif Zalt.hp <= 0:
        jump battle_ghost_w_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_ghost_w_lose
    elif True:
        jump battle_ghost_w_loop


label battle_ghost_w_win:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_small_end.ogg" noloop
    pause 1
    hide ghost 02 with slow_dissolve

    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    "The ghostly form fades into the darkness, the rock it possessed lays still on the ground."
    "You get an ectoplasm and a rock."
    "You get 80 EXP."
    $ jane_inv_M.take(rock)
    $ jane_inv_M.take(ectoplasm,1)
    $ Zalt.exp = min(Zalt.exp+80, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    $ Witer.sleep = 6
    $ Foe.ghostappear = True
    jump T_outdoor

    return
label battle_ghost_w_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    "The phantom fires a purple bolt of lightning and strikes you square in the chest."
    hide ghost 02 with dissolve
    e 0 "Ahhhh!"
    "Your can’t move your body! Like a ragdoll your body collapses onto the ground."
    "The searing pain from your chest burns like hot molten metal seeping into you."
    "A faint whisper grows louder in your ears but there's nobody around you."
    "Then it speaks."
    "Ghost" "Oh fuck yes. I've forgotten what it's like to have a body."
    e 0 "Who are you? Get out of my head!"
    "Ghost" "Shut up you little piss stain. This body's mine."
    "You try to move your fingers but there's something wrong."
    "Your body starts to sit up, and your fur blackens like the night itself."
    "Purple lines form around your forearms and your entire body gives off an intimidating aura."
    "Your eyes glow in a haunting blue colour, and your pupils turn red like blood."
    "Ghost" "That's more like it."
    "The words that leave your mouth they sound like your voice, but they are not yours."
    e 0 "My body! I can’t control it."
    "Your arms start to swing about like the ghost is trying to get accustomed to how to control you."
    "With every swing you can still feel every motion of your joints. "
    "Ghost" "You have a pretty hot body piss stains. Mmm, yeah look at these pecs."
    "Ghost" "I can't wait to test it out and fuck all your friends."
    e 0 "No! Get out of my body you bastard."
    "Ghost" "More importantly lets see what you're packing."
    "Controlling your hands he reaches for your loincloth."
    e 0 "Stop!"
    scene black
    show ghost lose1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos -0.3 ypos 0
        zoom 1.5
        linear 20.0 xpos 0 ypos -1000
    "You try to wrestle control back from the ghost, but it doesn't work."
    "He pulls off your loincloth letting your hard member plop onto your thigh."
    show ghost lose1 with slow_dissolve:
        xpos 0.19 ypos -0.05
        zoom 0.86
    "Ghost" "Yes, this will do just fine."
    "He wraps your hand around your dick and squeezes."
    e 0 "Ahh!"
    "You feel it."
    "The tightness of your grip around the shaft and the heat of your throbbing dick."
    "The ghost manipulates your hand to start caressing the hard member."
    "Rubbing your dick vigorously, your body shudders and moans."
    "A deep and revolting moan."
    "You bring your other hand close to your mouth and suck on the first three fingers hungrily."
    e 0 "Stop, stop, stop! Don’t."
    "The ghost continues to ignore your cries and laps your fingers hungrily."
    "Your tongue extends out like a lizard and lathers your fingers in saliva."
    "Ghost" "Yeah all lubed up for the main event."
    "Ghost" "I got to practice to be the biggest slut of the kingdom."
    "You push your hips forward and raise your legs to expose your puckered hole."
    e 0 "No! Ahhh!"
    "Together you both moan in unison as you ram all three fingers into your hole."
    "Your whole body shudders and your cock throbs wildly in your hands."
    show ghost lose2 with slow_dissolve:
        xpos 0.19 ypos -0.05
        zoom 0.86
    "Ghost" "Oh fuck yes! I want to shove just as many dicks in my ass."
    "Ghost" "You can take it can’t you?"
    "Your only response is a pitiful moan."
    "It’s just too much, how your fingers fill your insides, practically ripping you a new hole as your fingers fuck your ass relentlessly."
    "With your other thumb, you caress the head of your dick."
    "Panting heavily a stream of pre cum leaks from the tip and down all over your thigh."
    "You jerk your dick furiously building the pressure in your balls."
    "Stopping just when you are at the edge of climax."
    "The teasing and edging makes your groan from pleasure."
    "Ghost" "Fuck I want to go deeper!"
    "You hold your breath as your fingers plunge even further and briefly tickling your prostate."
    "Ghost" "Fuck yea!"
    "More pre gushes out of your cock."
    "Your whole body is burning hot and your asshole aches as the ghost forces you to finger fuck yourself faster and faster."
    "The walls of your asshole grips your wet fingers sucking them deeper inside you."
    "With the rich flow of pre coming out of your dick your hand becomes wet and slick."
    "You jerk yourself like you’ve never jerked before."
    "Wetness fills your hole from the finger fucking, every thrust brings you closer to shooting your load."
    "Heavy pants fill the night, and you whine like a puppy."
    "Your resistance against the ghost taking over you weakens as you succumb to the need for release."
    with flashbulb
    show ghost lose3 with slow_dissolve:
        xpos 0.19 ypos -0.05
        zoom 0.86
    "With an ear shattering howl your balls retract and your cock blasts a hot stream of cum all over the grass."
    "Ghost" "Fuck!"
    "The orgasm feels intense, you can’t keep your eyes open as you continue to shoot ropes of cum all over the place."
    show ghost lose4 with slow_dissolve:
        xpos 0.19 ypos -0.05
        zoom 0.86
    "Ghost" "Buhehehehe."
    "You sit on your spot exhausted and covered in cum."
    "Some of it trails down onto your fingers and enters your stretched hole."
    "In your heart, you feel the ghost’s cocky satisfaction that the ghost feels."
    "He’s lecherous smile shows on your face, and it disgusts you to the core. "
    e 0 "YOU..."
    hide ghost lose4 with slow_dissolve
    "You’re boiling with rage!"
    e 0 "YOU... GET OUT OF MY BODY!"
    with flashbulb
    "Ghost" "What the hell?"
    "The purplish glow around your body waxes and wanes. "
    "Ghost" "No! No! This is my body!"
    "Through sheer force of will, the ghost’s hold on you breaks and your body collapses to the ground."
    "You see the ghostly apparition shrivel and shrink in the air."
    "Ghost" "Fuck you kid! I’ll be back!"
    "Ghost" "If not me, one of us will!"
    "Ghost" "You’ll rue the day you try to go against us!"
    "The ghost turns into a wisp of purple smoke and flies into your pouch, several coins come to life and roll away from you and disappear into the darkness."
    "Ugh."
    "You faint."
    scene outdoor 1n with slow_dissolve
    $ persistent.CG_ghost_lose = True
    $ Foe.ghostwin = True
    if jane_inv.qty(coin) != None:
        $ qty = int(jane_inv.qty(coin)*0.2)
        $ jane_inv.drop(coin,qty)
        "When you awaken you find that you’ve lost <[qty]> coins. Good thing you still have your loincloth."
    $ Zalt.lust = 0
    $ Zalt.hp = 1
    $ Zalt.cor = min(Zalt.cor+1,100)

    if Witer.sleep == 4:
        $ Witer.sleep = 5
        "You force yourself up from the ground dragging yourself to the tavern entrance."
        "It's a struggle even to move."
        "That battle was a complete failure. "
        "You reason that your usual tactic of hitting enemies hard wasn't going to work with this enemy."
        "It will most likely come back again. There's got to be a way to defeat it, would Meko know how? He is a ghost himself."
    $ Time.hours = Time.hours+1
    jump T_outdoor
    menu:
        "New game" if True:
            return
        "No!" if True:
            jump forest_map
    stop music
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
