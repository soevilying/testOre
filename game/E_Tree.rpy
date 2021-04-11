label battle_tree:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 300
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
    jump battle_tree_loop


label battle_tree_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show tree at center
    play music "<loop 12.4405>music/forest_fight_strong2.ogg"





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
            if Random >= Zalt.CRIT:
                $ wolf_hp -= red_damage
                if wolf_hp <= 0:
                    pass
                elif True:
                    "You draw your sword and lunge in for an attack.\n(Damage dealt- [red_damage]hp)"
            elif True:
                $ qty = red_damage*2
                $ wolf_hp -= red_damage*2
                if wolf_hp <= 0:
                    pass
                elif True:
                    "You draw your sword and lunge in for an attack.\n{b}{color=#ffd65c}(Critical damage! -[qty]hp){/color}"

        if res == "Submit":
            e "I can't fight anymore.."
            "The enemy is too strong."
            "You’re knocked onto the ground."
            jump battle_tree_lose

        if res == "Bind up":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Bind up* [Zalt.heal]hp restored"
        if res == "Flirt":
            $ Random = renpy.random.randint(1, 3)
            if Random == 1:
                "You attempt to seduce the tree creature."
                "The tree creature is enraged!"
            elif Random == 2:
                "You attempt to seduce the tree creature."
                "The tree creature is enraged!"
            elif True:
                "You attempt to seduce the tree creature."
                "The tree creature is enraged!"
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
            $ Random = renpy.random.randint(1, 2)
            if Random == 1:
                "You run away."
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item
                hide tree
                jump forest_map
            elif True:
                "Escape failed!"
                pass
        elif True:
            pass

        if Chet.tree == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "The tree creature unleashes its vines and swipes you off your feet."
                elif Random == 2:
                    "The tree creatures shoots a barrage of wooden spikes towards you."
                elif True:
                    "The tree creature uses its vine to grab a rock and smashes it against you."
                "But you dodged its attack!"
            elif True:
                $ Random = renpy.random.randint(1, 3)
                $ wolf_damage = renpy.random.randint(20, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                if Random == 1:
                    "The tree creature unleashes its vines and swipes you off your feet."
                elif Random == 2:
                    "The tree creatures shoots a barrage of wooden spikes towards you."
                elif True:
                    "The tree creature uses its vine to grab a rock and smashes it against you."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "The tree creature unleashes its vines and swipes you off your feet."
                elif Random == 2:
                    "The tree creatures shoots a barrage of wooden spikes towards you."
                elif True:
                    "The tree creature uses its vine to grab a rock and smashes it against you."
                "But you dodged its attack!"
            elif True:
                $ Random = renpy.random.randint(1, 3)
                $ wolf_damage = renpy.random.randint(50, 80)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                if Random == 1:
                    "The tree creature unleashes its vines and swipes you off your feet."
                elif Random == 2:
                    "The tree creatures shoots a barrage of wooden spikes towards you."
                elif True:
                    "The tree creature uses its vine to grab a rock and smashes it against you."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_tree_win
        elif True:

            "Tree" "UUUBREAHHH"
            jump battle_tree_win

    elif Zalt.hp <= 0:
        "The enemy is too strong."
        "You’re knocked onto the ground."
        jump battle_tree_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_tree_lose
    elif True:
        jump battle_tree_loop


label battle_tree_win:
    play music "music/forest_fight_boss_end.ogg" noloop
    pause 1
    hide tree with slow_dissolve
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    "The creature collapses to the ground."
    "Its body turns a dark shade of brown and its movements slows to a halt."
    "With a weak groan the glows in its eyes dies out."
    "Its entire body turns coal black save for the single branch of flowers on its back. "
    "You stab the creature’s corpse once in the eye confirming its death{p}before proceeding to climb the dead creature and pluck the flowers."
    "<You get a handful of white flowers>"
    "After picking the flowers you make your way back to the tavern."
    "You walk a short distance before you turn to look behind you. "
    "Nothing but fog."
    "You try to head back to where the creature’s body laid but you find the path to the tree creature is gone."
    "Dense trees and shrubs have cover where the path once was. "
    e 1 "I know you’re watching me somewhere."
    if Chet.tree == 1:
        "Before you head back to the tavern, you find some water to wash the slimy armor off your body."
    elif True:
        "You feel empowered from defeat the tree monster without the help of goo armor."
        "{b}{color=#19c22a}<[name] gains two lv-points!>{/color}"
        $ Zalt.points = Zalt.points +2
        "You head back to the tavern."
    "<[name] gains 800 EXP>"
    $ Zalt.exp = min(Zalt.exp+800, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    $ Hakan.quest = 5
    $ Chet.tree = 0
    $ jane_inv_K.take(Raco_flower)
    jump forest_map

    return
label battle_tree_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music

    "The creature’s vines smacks you hard against the gut."
    "Knocking the air out of you and sending you flying against a tree."
    "It doesn’t give you a chance to pick yourself up."
    "You’re dragged by the ankles and swung up into the air. "
    if Chet.tree == 1:
        e 9 "What? It can grab me?"
        "The enemy’s vines are now coated with something that renders your slime armour useless."
        "The creature has adapted itself to finish you off!"
    "You frantically grasp at air but you fall backwards onto the creature’s back."
    "You scream as loud as you can expecting the sharp spikes to impale you."
    "But instead you feel thick wet vines wrap around your hips and arms,{p}pulling you faster downwards."
    play sound "music/treestep.ogg" fadeout 1
    scene black with slow_dissolve
    "The sky’s moving further and further away."
    "..."
    "...."
    ".....?"
    show tree lose1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos 0 ypos 0
        zoom 1.3
        linear 10.0 xpos 0 ypos -500
    "Then wetness consumes your entire body. Countless green vines wrap and slither all around your body."
    stop sound fadeout 1
    "You hear the creak of wood moving."
    show tree lose1 with slow_dissolve:
        xpos 0.06 ypos -0.05
        zoom 1.1
    e "What the hell?"
    "The last bit of sunlight disappears from view as the creature’s back closes."
    "You’re trapped."
    "You can’t see what’s happening but you can feel it."
    "Your wrists are bound by the vines."
    "You tug as hard as you can but the vines are too strong."
    "Warm sticky fluids are dripping from the roof of your tentacle prison."
    "These vines feel different from the ones you faced outside."
    "They're so much stronger and there's no telling what the goo they're excreting could do."
    "You want to scream."
    "You should scream, but the smell- it's incapacitating you."
    e "What is that? I… It smells… so good."
    "You start to struggle."
    "A lone tentacle slithers up your right thigh and wraps itself around your crotch."
    e "Ahhh!"
    "It grips your loincloth and lathers it with thick slime."
    "You faintly see from the soft light breaking through the tree creature’s shell."
    "Your loincloth sizzling and melting into nothingness in the tentacle’s hold."
    show tree lose2 with slow_dissolve:
        xpos 0.06 ypos -0.05
        zoom 1.1
    "In just seconds the fabric is gone and your dick is revealed."
    "The wall of vines around you starts to wave and slither erratically,{p}releasing a heavy dose of pollen at you."
    "There’s that smell again. That intoxicating, and heart pounding smell."
    e "What’s happening to me?"
    show tree lose3 with dissolve:
        xpos 0.06 ypos -0.05
        zoom 1.1
    "With every breath the pollen invades your lungs and your mind fills{p}feels heavy like you’ve had too much to drink. "
    "All you want is someone to play with your cock."
    "You groan loudly as your cock grows heavier and harder."
    e "Ahh, fuck make me cum. Let me cum!"
    "Your butthole muscles loosen and unclench."
    "More vines draw close towards you."
    "One of it grabs you by the left arm and grabs ahold of it."
    "Another rests just right on top of your left nipple."
    "The one tentacle feels cold on top of your protruding nub. "
    "It starts to twitch and flicks your nipple forward."
    e "Ahh!"
    "The vein falls back and flicks your nipple again."
    "You whimper loudly. The stimulation feels like bliss."
    "Your entire body is charged as every nerve is being caressed sensually. "
    "However, the more you try to move,{p}the stronger the vines hold you back until you are frozen in space, unable to move."
    "All you can do is moan."
    "You then feel something slithering along your buttcrack."
    "Then, the vine mercilessly penetrates your hole. "
    with flashbulb
    show tree lose4 with slow_dissolve:
        xpos 0.06 ypos -0.05
        zoom 1.1
    e "Gaah! Too quick! What are you doing to me?"
    "The vine entered you with ease thanks to the slime covering its exterior."
    "You’re breathing heavier and your cock throbs as the vine goes deeper into your rectum."
    "The vine finds your prostate and you feel it rubbing against it."
    "The stimulation is too much to bear."
    "Pulse after pulse of ecstasy fills your every being."
    "Your cock begins to drip pre all over your shaft."
    e "Fuck! I can’t hold it in."
    "Just when you think it can’t get any worse, another vine slithers towards your hard-on."
    "Unlike the other vines this one looked like a living snake with a gaping hole where its face would be."
    "The vine clamps on your dickhead and squeezes."
    "The inside of the vine feels warm and slick."
    e "FUCK!"
    with flashbulb
    show tree lose5 with slow_dissolve:
        xpos 0.06 ypos -0.05
        zoom 1.1
    e "Ugh! Feels so good!"
    "The vines move in unison assaulting your body and pushing you to brick of cumming."
    "Your brain is basically mush as the vine relentlessly fucks your ass,{p}probing it and massaging your prostate."
    "Loud squishing and sloshing sounds echo inside the wood prison."
    "Unconsciously your hips begin to gyrate, pumping your cock into the hungry vine. "
    "You’re practically gasping for air, but this feels so good, you don’t want it to stop."
    "Pre cum gushes out of your cock and into the vine, it sucks every drop hungrily."
    e "I can’t hold it in anymore, I’m cumming!"
    with flashbulb
    "Your entire body flexes as you fire ropes of hot cum from your cock."
    "There’s too much cum!"
    "The vine sucking on your dick is unable to hold it all{p}and small trickles of cum begin to pour out the tip."
    "Panting heavily, exhaustion overcomes you."
    "There’s no energy left inside you to even make a sound."
    "Then you feel a vine creeping along your face. "
    e "Hmm?!"
    show tree lose6 with slow_dissolve:
        xpos 0.06 ypos -0.05
        zoom 1.1
    "The vine invades your mouth and lodges itself inside your throat."
    e "Mmm!"
    "You panic, but there’s nothing you can do."
    "Liquid starts to drip from the vine inside your mouth."
    " As your belly is filled with the unknown liquid."
    "You feel your body rejuvinate with energy, and your cock hardens again."
    "For a brief moment you snap out of your trance."
    e "(It’s not going to kill me!)"
    e "(It wants to keep me alive to milk me for my life force!)"
    hide tree lose6 with slow_dissolve
    e "(I… I… want to cum again.)"
    "..."
    "...."
    "......"
    show tree lose7 with slow_dissolve:
        xpos 0.06 ypos -0.05
        zoom 1.1
    "Your fate is sealed."
    "The tavern never hears from you again."
    hide tree lose7 with slow_dissolve
    "While you remain trapped inside your prison of lust ever."
    "So often you hear the laughter of a mysterious voice."

    "{b}{color=#c22719}<GAME OVER>{/color}"
    $ persistent.CG_tree_lose = True
    menu:
        "New game" if True:
            return
        "No!" if True:
            jump forest_map0

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
