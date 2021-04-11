label battle_bullcamp:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 170
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    $ Map.good_battle = True
    $ Battle.holyfcd = 0
    stop music
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    jump battle_bullcamp_loop


label battle_bullcamp_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show bullw at center

    play music "<loop 12.6082>music/forest_fight_friend.ogg"





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
            jump battle_bullcamp_lose
        if res == "Flirt":
            $ Random = renpy.random.randint(1, 4)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You strike a series of poses with a confident smile."
                "The enemy is intrigued by your movements."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You tease your opponent by attacking them head on."
                "Rubbing them sensually on their nipples, crotch, and lightly fingering their backsides."
                "Your opponent is panting heavily, clutching his obvious erection."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You rub your crotch sensually, letting your cock chub up a bit before flashing your dickhead at the enemy."
                "Lust fills your opponent, he is immobilized by powerful desire for your cock."
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You strike a series of poses with a confident smile."
                    "The enemy catches you by surprise and throws you back. You barely land on your feet."
                elif Random == 2:
                    "You tease your opponent by attacking them head on."
                    "Rubbing them sensually on their nipples, crotch, and lightly fingering their backsides."
                    "The enemy ignores your attempts to seduce him."
                elif True:
                    "You rub your crotch sensually, letting your cock chub up a bit before flashing your dickhead at the enemy."
                    "The enemy is enraged by your actions."
            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                "The bull falls to his knees, his hard cock throbs and leaks pre all over the battlefield."
                jump battle_bullcamp_win
            elif True:
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
            "You can't run!"
            pass
        elif True:
            pass

        if wolf_hp <= 0:
            jump battle_bullcamp_win
        $ Random = renpy.random.randint(1, 80)
        if Random <= Battle.dodge:
            "Bull warrior" "RrrrrRRrrrr! {i}*The monster hits you*{/i}"
            "But you dodged his attack!"
        elif True:
            $ wolf_damage = renpy.random.randint(20, 35)
            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
            "Bull warrior" "RrrrrRRrrrr! {i}*The monster hits you*{/i}"

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1




    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_bullcamp_win
        elif True:

            jump battle_bullcamp_win

    elif Zalt.hp <= 0:
        "The enemy bull’s fist slams hard onto your gut."
        "Your body spasms for a second and you are left wobbling on your feet."
        jump battle_bullcamp_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_bullcamp_lose
    elif True:
        jump battle_bullcamp_loop


label battle_bullcamp_win:
    if Foe.bullcamp ==2:
        play music "music/forest_fight_friend_end.ogg" noloop
        pause 1
        hide bullw with slow_dissolve
        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item
    elif True:
        "Bull warrior" "Egh..!"
        hide bullw with dissolve
    $ Foe.bullcamp = Foe.bullcamp+1
    if Foe.bullcamp ==1:
        "You plunge your blade into the bull’s chest."
        play sound "music/blood.ogg"
        "Screaming at the top of your lungs you pull hard on the blade, slashing the bull in half."
        "He falls to the ground-dead."
        "On the other side, the lizards manage to take out their foe."
        "The bull’s face turns a dark shade of purple and collapses onto the ground."
        "He writhes in pain, foam spewing out of his mouth before his entire body stops moving."
        "You shout at the lizard."
        e 1 "I will go to set the final stone.Stay here,be careful!"
        "You run to the final place."
        scene black with dissolve
        "Third Lizard Guard" "More are coming!"
        play sound "music/foot1.ogg"
        scene forest 6 with dissolve
        "You set the final stone on its place"
        with flashbulb
        e 9 "Ahhhhhhh"
        "<Your HP turns to 1>"
        "<Your MP turns to 1>"
        $ Zalt.hp = 1
        $ Zalt.mp = 1
        "From the fog two more bulls come running in."
        "Third Bull Warrior" "Traitor!!"
        "Fourth Bull Warrior" "Let's take the wolf!"
        "Dazed and in pain."
        "No time for respite, you need to beat the bulls."
        jump battle_bullcamp
    elif Foe.bullcamp ==2:
        "Another bulls attack!!"
        jump battle_bullcamp
    elif True:
        "Your sword cuts him across his right arm."
        "All over his body, blood drips from the wounds you’ve inflicted upon him, still the bull will not relent."
        "His movement is sluggish but he still clutches his weapon for dear life. "
        "This has gone long enough, you let the bull raise his axe over his head before swiftly stabbing him through the jaw.."
        "Your blade pierces his skull and a jet of blood fires from it, you barely dodge the torrent of blood."
        "The larger bull falls to the ground with a heavy thud. "
        "Third Lizard Warrior" "Look out [name]."
        e 9 "Huh?"
        "You leap out of the way just in time as the other bull’s dead body flies across and lands with the bull you just killed."
        "First Lizard Warrior" "You alright there, [name]?"
        "You land flat on your back, dazed and in pain."
        "The lizards try to help you get up."
        "Second Lizard Warrior" "You handled them like a champ, but boy they looked more pissed than ever."
        "Third Lizard Warrior" "Yeah, what did you do to them?"
        e 13 "I don’t know... Look, give me some times to rest."
        e 1 "Can you guys do something about the bodies?"
        "First Lizard Warrior" "No problem, two of us can clean up the mess."
        "You return to the campsite take a rest."
        "One by one the lizards move the dead body. "
        "It’s difficult to concentrate on the task at hand, there’s a part of you that worries if the lizards know that you’ve made contact with the bull tribe."
        "You smack yourself in the head to focus, and find they already plant the third stone when you left."
        "You turn to the final point and accidentally looked at the first bull you killed."
        "His dead eyes stare at you with such hatred and malice you have to look away. "
        "After the last body is removed, the lizards come back."
        "First Lizard Guard" "How do we even know if this thing works?"
        "Second Lizard Guard" "Hey, what were you thinking when you used those stones?"
        e 1 "I was just thinking keep whatever that would harm the lizard tribe and its allies out."
        "Second Lizard Guard" "Hmm, let me try something. "
        "The lizard walks away from the group, away from where you planted the first two rune stone and picks up a pebble."
        "He tosses it at your feet but the pebble hits an invisible wall and falls."
        "The other two lizards are wowed by what they saw. "
        e 13 "Guess that means it works."
        "Second Lizard Guard" "Hey, this is kinda fun."
        "He keeps finding pebbles to throw at the invisible barrier just to see which one would finally get through."
        "You roll your eyes and instruct them that it’s time to return to the village. "
        scene black with slow_dissolve
        hide red1
        hide red2
        "Along the way the lizards share with you some of their concoctions to remove the bull’s blood from the sword and yourself."
        "There wasn’t enough of it for everyone, but hopefully you are clean."
        jump Nauxus_camp_end

    return
label battle_bullcamp_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    if Foe.bullcamp ==0:

        "As your reactions slow from the injuries inflicted on you, the bull warrior wastes no time in finding an opening."
        "With a roar, the bull uses the blunt knob of his battle axe and smashes it against your knee."
        show red1 at center with dissolve
        play sound "music/blood.ogg"
        "You hear a sharp crack followed by a splitting pain as you lose your balance and fall screaming."
        show red2 at center with dissolve
        play sound "music/blood.ogg"
        "As you feebly attempt to get back up with your bloodied hands, you look back up to see your foe gleefully smiling as he swings his weapon at your face."
        scene black with vslow_dissolve
        "Everything fades to black."
        "{b}{color=#c22719}<GAME OVER>{/color}"
        menu:
            "New game" if True:
                return
            "New game" if True:
                return
    elif Foe.bullcamp ==1 or Foe.bullcamp ==2:
        "Too weak to fight back, your enemy kicks you square in the chest as you feel the wind get knocked out of you."
        "You land flat on your back, dazed and in pain."
        show red1 at center with dissolve
        play sound "music/blood.ogg"
        "As you try to get back up, the bull doesn't spare you that moment as he brings down his axe onto your chest."
        "You scream wildly as blood comes out of your mouth."
        "Coughing up copious amounts of blood as you struggle to breathe."
        show red2 at center with dissolve
        play sound "music/blood.ogg"
        "The bull pulls the axe from your sternum only to bring it down again, and again, and again."
        "Cries for mercy slowly become garbled as your blood chokes you."
        scene black with vslow_dissolve
        "Everything fades to black."
        "{b}{color=#c22719}<GAME OVER>{/color}"
        menu:
            "New game" if True:
                return
            "New game" if True:
                return
    hide bullw with dissolve

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
