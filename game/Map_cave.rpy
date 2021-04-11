label Cave_map0:
    stop music
    stop Thane
    stop Chan1
    stop Chan2
    $ renpy.music.set_volume(1, 1, channel = "Chan1")

    play Chan1[ "<silence 0.5>", "music/cave.ogg" ]fadein 3

    jump Cave_map


label Cave_map:
    stop music
    $ Time.mins = Time.mins +10
    $ Zalt.dungeon = True
    $ config.rollback_enabled = False
    $ renpy.music.set_volume(1, 5, channel = "Chan1")
    $ renpy.music.set_pause(False, channel='Chan1')
    window hide None
    if Zalt.Dungeon_leave:
        jump Cave_leave
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Zalt.A_exp >= 100:
        $ Zalt.A_exp = Zalt.A_exp -100
        $ Zalt.A_lv = min(Zalt.A_lv + 1, 5)
        $ Zalt.AP = Zalt.AP +1
        "You get one AP, you have [Zalt.AP] now."
        "Your A-LV now is [Zalt.A_lv]"


    if Zalt.A_lv == 5:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 4:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 3:
        $ Zalt.A_exp_lv = 2
    elif Zalt.A_lv == 2:
        $ Zalt.A_exp_lv = 1.5
    elif Zalt.A_lv == 1:
        $ Zalt.A_exp_lv = 1.2
    elif True:
        $ Zalt.A_exp_lv = 1


    scene cave 1 with dissolve
    play music "music/drip.ogg"
    call screen cave_map with dissolve
    if _return == 'exit':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        jump Cave_leave
        return
    if _return == 'point 1':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "You find an open space."
        "This place looks safe to set up a campfire and rest."
        "You can also level up here."
        $ qty = jane_inv_M.qty(stick)
        $ qty1 = jane_inv_M.qty(rock)
        "You have [qty] sticks and [qty1] rocks now."
        if Map.ca1 == 0:
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.ca1 = 1
        menu:
            "Rest (use 3 sticks and 2 rocks)" if jane_inv_M.qty(stick) >= 3 and jane_inv_M.qty(rock) >= 2:
                $ jane_inv_M.drop(stick,3)
                $ jane_inv_M.drop(rock,2)
                scene black
                "You rest a while, feel refreshed and full of energy."
                "HP and MP have been restored to maximum."
                $ Zalt.hp = Zalt.maxhp
                $ Zalt.mp = Zalt.maxmp
                $ Time.mins = Time.mins +30
                jump Cave_map
            "Level up" if Zalt.exp >= Zalt.maxexp and Zalt.lv < Zalt.maxlv:
                $ Zalt.exp = Zalt.exp - Zalt.maxexp
                $ Zalt.maxexp = Zalt.lv*250+100*(Zalt.lv-1)
                $ Zalt.lv = Zalt.lv+1
                $ Zalt.points = Zalt.points+1
                $ Zalt.points1 = Zalt.points1+1
                "After taking a short break to reflect on your battles, you feel stronger."
                "{b}{color=#19c22a}[name]'s level increases to [Zalt.lv].{/color}"
                $ Random = renpy.random.randint(1, 2)
                if Random == 2:
                    "{b}{color=#19c22a}[name]'s Hp increase 5 points.{/color}"
                    $ Zalt.maxhp = Zalt.maxhp +5
                elif True:
                    "{b}{color=#19c22a}[name]'s Mp increase 5 points.{/color}"
                    $ Zalt.maxmp = Zalt.maxmp +5
                "{b}{color=#19c22a}[name]'s ATK increase 2 points.{/color}"
                "{b}{color=#19c22a}[name]'s MATK increase 1 points.{/color}"

                $ Zalt.ATK = Zalt.ATK +2
                $ Zalt.MATK = Zalt.MATK +1

                jump Cave_map
            "Masturbate" if Zalt.lust >= 40:
                "You spend some time to deal with your desires."
                $ Zalt.lust = 0
                $ Time.mins = Time.mins+15
                jump Cave_map
            "Leave" if True:

                jump Cave_map
    if _return == 'point 2':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "The further you walk your ears pick up on the sound of something wet sloshing around."
        "You’re unable to make out where the sound is coming from the sound bouncing off the walls."
        "Slosh."
        "Waving the torch around you see nothing around you but rocks."
        e 1 "Huh, maybe I’m imagining things."
        "Drip!"
        "Sizzles!"
        show black2 with dissolve
        hide black2 with dissolve
        "The flame of your torch flickers. "
        "Sizzles!"
        "Some kind of liquid is dripping onto your torch."
        "You look up and you instantly draw your sword."
        "It’s a pair of slimes on the roof of the cave. One of the lunges at you!"
        jump battle_cave_slime

    if _return == 'point 3':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.ca3 == 1:
            "You enter a room with stelae lining the walls."
            "Closer inspection reveals these stelae are broken, intentionally."
            "You can barely make out the names and stories that were carved on these broken pieces."
            "A lone path leads to one stela deeper inside illuminated by light from the cave ceiling."
            "Curious, you head inwards to investigate the sole stone pillar."
            "A deep gash cuts through the text but it’s still readable."
            "To all who renounce the evil that are the mages and their cruelty towards the common folk."
            "Venture forth through these caves-"
            "You suddenly feel uncomfortable, as if someone is watching you around."
            "But there's more below,do you keep reading?"
            menu:
                "Yes" if True:
                    "A stone hand grabs you from behind and a massive gargoyle roars into your face."
                    $ Map.ca3 = 3
                    $ Map.ca3garg = True
                    $ Map.ca18garg0 = False
                    jump battle_gargoyle
                "No" if True:
                    $ Map.ca3 = 2
                    jump Cave_map
        elif Map.ca3 == 2:
            "The sole stone pillar is still here."
            "And that things is still here too."
            "Do you keep reading?"
            menu:
                "Yes" if True:
                    "A stone hand grabs you from behind and a massive gargoyle roars into your face."
                    $ Map.ca3 = 3
                    $ Map.ca3garg = True
                    $ Map.ca18garg0 = False
                    jump battle_gargoyle
                "No" if True:
                    jump Cave_map
        elif Map.ca3 == 3:
            "The gargoyle is still here."
            "Do you want to fight it again?"
            menu:
                "Yes" if True:
                    $ Map.ca3garg = True
                    $ Map.ca18garg0 = False
                    jump battle_gargoyle
                "No" if True:
                    jump Cave_map
        elif True:
            "The sole stone pillar is still here."
            "To all who renounce the evil that are the mages and their cruelty towards the common folk."
            "Venture forth through these caves-"
            "Guided by the courage of our fallen who fought to find their freedom in the Kingdom of Aplistia."
            "The rest of the text is unreadable."
            jump Cave_map


    if _return == 'point 4':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "You hear rushing waters up ahead."
        "A dark gloomy river runs through in front of you and the path now branches into two directions. "
        e 1 "How deep is this thing?"
        "Crouching down you take out your sword and dip it into the water."
        "The whole sword is submerged in the river and you still can’t feel the riverbed."
        e 1 "Well walking across is out of the question."
        "You pull out the gloves and sniff its scent again."
        "His scent is coming from the left road. "
        "Then you hear a knocking coming from the right side."
        "Knock."
        e 5 "Hello? Is someone there?"
        "Knock."
        "It sounds like someone knocking against a wooden surface."
        "Knock."
        "Should you investigate the noise or continue searching for Flo?"
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.ca4 = 2
        $ Map.ca5 = 1
        $ Map.ca7 = 1
        jump Cave_map
    if _return == 'point 5':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        jump Cave_ferryman

    if _return == 'point 6':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

    if _return == 'point 7':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "As you continue onwards the heat inside the cave is slowly suffocating you."
        "Wiping the sweat from your brow you think about what kind of creatures could be living down here. "
        "The eerie quietness of the cave is disturbing."
        "Every rock that passes your way fills you with suspicion for fear that at any second it could."
        "You trudge your feet along when you feel a cold chill pass the back of your neck."
        "Instantly you turn, but there’s nothing there."
        e 9 "Get it together [name], just get it together get the shark and get out."
        "Then your ears pick up faint whispers coming nearby."
        "You try to focus on what is being said, but you can’t make it out. "
        "The voices seem to be coming from a path to your left. "
        $ Map.ca7 = 2
        $ Map.ca8 = 1
        $ Map.ca9 = 1
        $ Map.ca10 = 1
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump Cave_map

    if _return == 'point 8':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.ca8 == 1:
            "You decide to follow the voices, their whispers grow louder in volume and leads you to an open area."
            "It’s four bulls sitting by a campfire."
            menu:
                "Approach" if True:
                    e 5 "What? What are you all doing here?"
                    "The bulls seem to ignore your presence, and you can still hear the whispering growing louder and louder in your head."
                    e 5 "Hey! I said-"
                    "All four of their heads turn towards you at the same time. "
                    "The whispers halt and the first bull stands with his axe in hand."
                    e 12 "Shit, I know where this is going."
                    "Angry Bull Warrior" "Give us back what’s ours, demon!"
                    $ Map.ca8 = 3

                    jump battle_cave_bull
                "Leave" if True:
                    e 5 "...I don't know why, but I think they are very dangerous."
                    "You decide to leave them alone."
                    $ Map.ca8 = 2
                    jump Cave_map
        elif Map.ca8 == 2:
            "The bulls are still here."
            menu:
                "Approach" if True:
                    e 5 "What? What are you all doing here?"
                    "The bulls seem to ignore your presence, and you can still hear the whispering growing louder and louder in your head."
                    e 5 "Hey! I said-"
                    "All four of their heads turn towards you at the same time. "
                    "The whispers halt and the first bull stands with his axe in hand."
                    e 12 "Shit, I know where this is going."
                    "Angry Bull Warrior" "Give us back what’s ours, demon!"
                    $ Map.ca8 = 3
                    jump battle_cave_bull
                "Leave" if True:
                    e 5 "...I don't know why, but I think they are very dangerous."
                    "You decide to leave them alone."
                    jump Cave_map
        elif Map.ca8 == 3 and Map.ca8bull == 0:
            "The bulls are still here."
            "Do you want to fight it again?"
            menu:
                "Yes" if True:
                    jump battle_cave_bull
                "No" if True:
                    jump Cave_map
        elif Map.ca8 == 3 and Map.ca8bull == 1:
            "...The things are still here."
            "Do you want to fight it again?"
            menu:
                "Yes" if True:
                    jump battle_cave_bull
                "No" if True:
                    jump Cave_map
        elif True:
            jump Cave_map


    if _return == 'point 9':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        jump Cave_pillars

    if _return == 'point 10':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.ca10 == 1:
            "This wall looks unusual."
            "There’s an unusual slot where something rectangular could fit inside."
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.ca10 = 2
            $ Map.ca11 = 1
            jump Cave_map
        elif True:
            if jane_inv_K.qty(jester_badge) == None and jane_inv_K.qty(knight_badge) == None and  jane_inv_K.qty(prince_badge) == None:
                "This wall looks unusual."
                "There’s an unusual slot where something rectangular could fit inside."
            elif True:
                "It seems a badge would fit in this slot. "
                menu:
                    "Jester Badge" if jane_inv_K.qty(jester_badge) ==1:
                        "The shape of the badge doesn’t fit the slot."
                        jump Cave_map
                    "Knight’s Badge" if jane_inv_K.qty(knight_badge) ==1:
                        $ Map.ca10 = 3
                        $ Map.ca12 = 1
                        jump Bread_meet
                    "Prince Badge" if jane_inv_K.qty(prince_badge) ==1:
                        $ Map.ca10 = 3
                        $ Map.ca12 = 1
                        jump Bread_meet
                    "Not yet" if True:
                        jump Cave_map
            jump Cave_map
    if _return == 'point 11':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.ca11 == 1:
            "You find an abandoned packet here."
            "You find a rope, a torch and 2 bottles of MP potion in it."
            $ jane_inv.take(mp_potion,2)

            $ jane_inv_M.take(rope,1)
            $ jane_inv_M.take(torch,1)
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.ca11 = 2
            jump Cave_map
        elif True:
            jump Cave_map

    if _return == 'point 12':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Bread.map == 0:
            if Bread_meet == -1:
                "Nothing here, it's just a empty room."
                $ Map.ca12 = 2
                jump Cave_map
            if Bread_meet == 1 and Parif.meet < 1:
                scene caveruin 2
                "You find Bread digging some holes inside the chamber."
                "He would find a spot, squat down and dig with his hands."
                e 1 "What are you doing?"
                show bread stand at center with slow_dissolve
                b "Oh hey there buddy."
                b "I’m looking for a treasure map I buried around here a long time ago."
                show bread happy at center with dissolve
                b "Just that I can’t remember where I buried it."
                "He starts laughing."
                e 13 "Right… I just came to check on you."
                e 1 "Do you need anything? Food? Water?"
                show bread stand at center with dissolve
                b "Oh, do you have Bread?"
                e 9 "I… do not have bread."
                b "Aww shame, that’s ok. I’m not that hungry anyways."
                e 1 "Ok, but if I see any I’ll bring you some."
                b "Thanks Buddy."
                hide bread stand at center with slow_dissolve
                "He continues digging again."
                e 1 "(What a weird guy.)"
                jump Cave_map
            elif Bread_meet == 1 and Parif.meet >= 1:
                $ Bread.map = 1
                jump Bread_map_start
            elif True:

                jump Cave_map
        elif True:
            jump Bread_talk
    if _return == 'point 13':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "You spot a massive boulder in the distance."
        "The way it is next to another entrance gives you the feeling that this boulder was supposed to lock something away."
        "Inside there are many and many treasure chests!"
        e 5 "Treasure!"
        "Running over to the chest you quickly open the unlocked chest"
        "Empty."
        e 5 "What?!"
        "You try to open other chests."
        "In the last chest,you find a piece of paper inside."
        "'Thanks for the loot.'"
        e 8 "Bloody bandits or whoever they stole the treasure before me! Ugh!"
        e 1 "Dang it, I came here too late."

        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.ca13 = 2
        $ Map.ca14 = 1
        jump Cave_map

    if _return == 'point 14':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.ca14 == 1:
            "You walk to the back of the empty room, there’s a pile of boulders closing what looks like a path to another room."
            e 1 "I wonder what could be on the other side…"
            "You place a hand on a boulder imagining what could be over there."
            "Unknown Voice" "How long have I been in here? A week? Two?"
            e 5 "Huh? Hello? Who’s there?"
            "You repeatedly confirm that there is no smell of Flo across."
            "Unknown Voice" "Hopefully Captain Asmund doesn’t find out I locked myself in here by accident."
            e 5 "Hey, if you mean this room, it’s empty!"
            "Unknown Voice" "Guess I can take a little cat nap for now."
            "Whoever is on the other side doesn’t sound like he can hear you."
            e 1 "This is pointless."
            e 1 "Hey, I’ll come back for you later ok."
            $ Map.ca14 = 2

            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        elif True:
            "silence."
            if Map.ca10 != 3:
                e 1 "This is pointless."
                e 1 "Hey, I’ll come back for you later ok."
        jump Cave_map

    if _return == 'point 15':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "You can see it now, in the distance a large triangular structure."
        "It looks like a pyramid from where you’re standing. "
        "There are stone steps leading towards the pyramid."
        "Squinting your eyes hard enough you see a large statue at the start of the stairs."
        "Maybe some climbing is needed."
        e 13 "Hang on Flo, I’m on my way!"
        $ Map.ca15 = 2
        $ Map.ca17 = 1

        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"

        jump Cave_map
    if _return == 'point 16':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

    if _return == 'point 17':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        jump Cave_statue


    if _return == 'point 18':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.ca18 == 1:
            "Like a mad bull you run across the open area to get to the pyramid."
            "Just as you pass a pair of statues facing each other a hand grabs you by the back of your neck and throws you backwards."
            e 9 "Waah!"
            "You roll across the ground and accidentally drop your torch."
            "The fire of your torch continues to burn and reveals a pair of gargoyles eyeing you with a lecherous smile."
            "The first gargoyle attacks!"
            $ Map.ca18 = 2
            $ Map.ca18garg0 = True
            $ Map.ca3garg = False
            jump battle_gargoyle
        elif Map.ca18 == 2:
            "The gargoyles are still here."
            "Do you want to fight it again?"
            menu:
                "Yes" if True:
                    $ Map.ca18garg0 = True
                    $ Map.ca3garg = False
                    jump battle_gargoyle
                "No" if True:
                    jump Cave_map
        elif Map.ca18 == 3:
            "The gargoyle is still here."
            "Do you want to fight it again?"
            menu:
                "Yes" if True:
                    $ Map.ca18garg0 = True
                    $ Map.ca3garg = False
                    jump battle_gargoyle
                "No" if True:
                    jump Cave_map
        elif True:
            jump Cave_map


    if _return == 'point 19':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.ca19 == 1:
            e 5 "This is…"
            "The pyramid turns out not to be a pyramid at all."
            "This whole thing is made out of wood. "
            "Circling around the structure you find a hole that lets you peer inside."
            e 5 "There’s a giant bell in here, it’s a bell tower!"
            e 1 "Should I head down here?"
            "Just to be sure, you sniff the air and pick up Flo’s scent."
            "Whatever took him definitely went in this direction."
            "There could be more dangerous monsters lurking down below, you have to be sure that you’re ready to go."
            $ Map.ca19 = 2
            $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
            $ PPEXP = 50*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            jump Cave_map
        elif Map.ca19 == 2:
            menu:
                "Use a rope" if True:
                    if jane_inv_M.qty(rope) >= 1:
                        $ jane_inv_M.drop(rope,1)
                        $ Map.ca19 = 3
                        "Using a rope You climb downwards."
                        jump belltower_map0
                    elif True:
                        e 1 "I need a rope then I can climb down the statue."
                        jump Cave_map
                "Leave" if True:
                    jump Cave_map
        elif True:


            "You climb downwards."
            jump belltower_map0

    if _return == 'point 20':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

label Cave_ferryman:

    if Map.ca5 == 1:
        "You follow the knocking sound to its source."
        "When you reach the end of the road you see a cloaked figure standing on top of a shadowy boat."
        "He holds a long stick in one hand and knocks it against the side of his boat."
        e 1 "H-hello? Who are you?"
        show ferryman stand with dissolve
        "The figure stops and turns its head towards you but you can’t see its face."
        "He raises a hand and points at you."
        "You instantly draw your sword expecting an attack."
        "Cloaked Figure" "Show me proof of your identity to board this vessel."
        e 5 "What? Why would I want a ride on some creepy ship with you?"
        e 5 "Explain yourself."
        "Cloaked Figure" "Show me proof of your identity to board this vessel."
        e 12 "Didn’t you hear me? Explain who the heck you are."
        "Cloaked Figure" "Show me proof of your identity to board this vessel."
        "It seems that talking to this figure isn’t going anywhere. It wants some proof of identity."
        $ Zalt.A_exp = Zalt.A_exp + 20*Zalt.A_exp_lv
        $ PPEXP = 20*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.ca5 = 2
    if Map.ca5 <= 3:
        show ferryman stand with dissolve
        "Cloaked Figure" "Show me proof of your identity to board this vessel."
        menu:
            "Show Proof" if True:
                if jane_inv_K.qty(jester_badge) == None and jane_inv_K.qty(knight_badge) == None and  jane_inv_K.qty(prince_badge) == None:
                    menu:
                        "Show your sword" if True:
                            "You draw the sword strapped on your back and show it to the cloaked figure."
                            "Cloaked Figure" "Wrong."
                            e 13 "This isn’t right."
                        "Show your hand" if True:
                            "You show the cloak figure your right hand."
                            "Cloaked Figure" "Wrong."
                            e 13 "This isn’t right."
                        "Show your dick" if True:
                            e 12 "This probably isn’t right, but hey worth giving it a try."
                            "You strip off your loincloth and flash your dick at the cloaked figure."
                            "Cloaked Figure" "Wrong."
                            e 5 "Really? Not even a whistle at least?"
                    jump Cave_ferryman
                elif True:
                    menu:
                        "Show 'Jester Badge'" if jane_inv_K.qty(jester_badge) ==1:
                            "You show him the Jester’s Badge. "
                            "Cloaked Figure" "If it isn’t the royal jester."
                            "Cloaked Figure" "I take it that you want to visit your secret room?"
                            e 1 "What secret room?"
                            "silence."
                            e 13 "Take me there."
                            "The figure bows slightly."
                            $ renpy.music.set_volume(0, 3, channel = "Chan1")
                            "The cloaked figure gestures to the empty seat on his boat."
                            hide ferryman stand with dissolve
                            "You get on it."
                            scene black with vslow_dissolve
                            play music "music/wave.ogg"
                            "The ride over to the secret place is not as far as you expected."
                            "It’s only a corner away from where you started from."
                            "Upon landing you notice two paths to take."
                            "To your left is a hole in the wall large enough for a full grown adult to go through."
                            "In front of you is a wooden treasure chest. It can’t be that easy, can it?"
                            $ Map.caj0 = 1
                            jump Cave_map_ferryman
                        "Show 'Knight’s Badge'" if jane_inv_K.qty(knight_badge) ==1:
                            "You show the Knight’s Badge."
                            "Cloaked Figure" "Knight Asmund, salutations."
                            "The figure bows slightly."
                            $ renpy.music.set_volume(0, 3, channel = "Chan1")
                            "The cloaked figure gestures to the empty seat on his boat."
                            hide ferryman stand with dissolve
                            "You get on it."
                            scene black with vslow_dissolve
                            play music "music/wave.ogg"
                            "The cloaked figure steers the boat off the shore."
                            "He heads straight ahead."
                            "The cloaked figure remains ever silent until he brings the boat to a halt on another shore."
                            "Cloaked Figure" "We are here."
                            $ Map.cak0 = 1
                            jump Cave_map_ferryman
                        "Show 'Prince Badge'" if jane_inv_K.qty(prince_badge) ==1:
                            "You present the Prince’s Badge."
                            "Cloaked Figure" "Your Highness."
                            "The figure bows slightly."
                            $ renpy.music.set_volume(0, 3, channel = "Chan1")
                            "The cloaked figure gestures to the empty seat on his boat."
                            hide ferryman stand with dissolve
                            "You get on it."
                            scene black with vslow_dissolve
                            play music "music/wave.ogg"
                            "With his long tiller he pushes the boat from the shore and heads deeper inwards to the caverns."
                            "As he steers the boat you notice his hands are not made of flesh but of white pearly bones."
                            "You avoid staring at the figure."
                            "The boat moves straight ahead until it comes to a fork in the river."
                            scene cave 2ferry with vslow_dissolve
                            "The figure steers the boat to the left and stops the boat in the middle of nowhere."
                            e 1 "Where is this? "
                            "Cloaked Figure" "A child should not be out and about with his parents."
                            "Cloaked Figure" "Go ahead, the queen is waiting for you."
                            scene black with slow_dissolve
                            "And then... the boat disappear."
                            play sound "music/watersplash.ogg"
                            stop music fadeout 3
                            e 9 "AHHHHHHH!" with vpunch
                            "You plunge into the cold and dark waters."
                            pause 1
                            scene cave 1 with vslow_dissolve
                            "You swim back up and gasp for air."
                            "The boat is heading back to the shore."
                            e 9 "Fuck! You could have at least waited for me!"
                            e 9 "But why he says that thing..?"
                            e 9 "The queen? I thought there’s nobody left in the castle."
                            $ Zalt.hp = max(1,Zalt.hp-80)
                            "{b}{color=#c22719}You lose 80 HP {/color}but at least you reach the ground."
                            jump Cave_map
                        "Not yet" if True:
                            jump Cave_map
            "Attack the Figure" if True:


                menu:
                    "Use your sword" if True:
                        e 12 "That’s it, I’ve had it with you."
                        "You pull out your sword and swing it across the cloaked figure’s chest."
                        "The blade cuts through but the phantom is still standing."
                        "Where your blade met his chest is now a gaping hole."
                        jump Cave_ferryman
                    "Use Holy Fist" if Battle.holyf == True:
                        e 12 "That’s it, if you’re not going to talk, I’ll let my fist do the talking!"
                        "Your Holy Fist lands right on the ferryman’s face but he is unphased by it."
                        e 5 "What?"
                        menu:
                            "HOLY FIST!!!" if True:
                                e 12 "That’s it, if you’re not going to talk, I’ll let my fist do the talking!"
                                show ferryman stand1 with dissolve
                                "Your Holy Fist lands right on the ferryman’s face and...."
                                e 5 "What?"
                                menu:
                                    "ROYAL SUPER GREAT HANDSOME HOLY FIST" if True:
                                        "You punch the ferryman one more time, and you hear something crack."
                                        "The ferryman staggers backwards and collapses onto its boat."
                                        e 5 "Hey!"
                                        hide ferryman stand1 with dissolve
                                        "The ferryman’s body deflates and the ship’s shadowy form disappears."
                                        "You carefully approach the now rundown dinghy, the body is nowhere to be found, only a pile of bones remains. "
                                        "Did you make the right move?"
                                        $ Map.ca5 = 4
                                        jump Cave_map
                                    "Leave" if True:
                                        jump Cave_ferryman
                            "Leave" if True:
                                jump Cave_ferryman
                    "Leave" if True:
                        jump Cave_ferryman
            "Leave" if True:

                e 12 "Yeah, well good luck with that. "
                "You leave the figure and head back to the crossroad."
                jump Cave_map
    elif True:
        if Map.ca5 == 4:
            "All that remains is the broken looking boat and the cloak that the ferryman used to wear."
            label ferryman_cloak:
                menu:
                    "Get the cloak" if Map.ca5 == 4:
                        "You try to grab the cloak but the fabric disintegrates upon your touch and turns to dust."
                        $ Map.ca5 = 5
                        jump ferryman_cloak
                    "Leave" if True:

                        jump Cave_map
        elif True:

            "All that remains is the broken looking boat."
            jump Cave_map


label Cave_statue:
    "It’s another ledge, the pyramid like structure is on another level below you."
    "From up close the statue from earlier is gigantic."
    if Map.ca3 ==4:
        "The face of the statue is unclear, perhaps it’s dedicated to some Devine Being or to whoever ruled this kingdom before."
    "There’s a long black cloth draped across the statue’s torso."
    "By the looks of the stains on it, it’s very old."
    e 1 "I gotta get down there."
    label Cave_statue_choose:
        menu:
            "Use a rope" if True:
                if jane_inv_M.qty(rope) >= 1:
                    $ jane_inv_M.drop(rope,1)
                    "Using a rope you manage to lasso onto the monument’s ear."
                    "After ensuring the rope is secure, you climb downwards by hopping down the statue."
                    $ Map.ca17 = 3
                    $ Map.ca18 = 1

                    $ Zalt.A_exp = Zalt.A_exp + 30*Zalt.A_exp_lv
                    $ PPEXP = 30*Zalt.A_exp_lv
                    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                    jump Cave_map
                elif True:
                    e 1 "I need a rope then I can climb down the statue."
                    jump Cave_statue_choose
            "Leap off parts of the statues (Agility Check)" if True:
                e 1 "I can just jump from its shoulders to its arms then grab onto its legs and shimmy down."
                if Zalt.agi >= 7:
                    "You leap onto the statue’s shoulders."
                    "{b}{color=#19c22a}<Agile Check success>{/color}"
                    "The structure wobbles a bit but you’re fine."
                    "As planned you fall onto the arms of the statue then with precise timing you manage to grab onto its legs before slowly releasing your grip and sliding all the way to the ground."

                    $ Map.ca17 = 3
                    $ Map.ca18 = 1

                    $ Zalt.A_exp = Zalt.A_exp + 30*Zalt.A_exp_lv
                    $ PPEXP = 30*Zalt.A_exp_lv
                    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                    jump Cave_map
                elif True:
                    "You leap onto the statue’s shoulders but slip and end up falling onto its arms."
                    "{b}{color=#c22719}<Agile Check failed>{/color}"
                    e 9 "Gack!"
                    "A burst of pain spread from your back. It feels like something broke."
                    "But the fall isn’t over your legs slip over the statue’s hands and you plunge downwards onto the ground."
                    $ Zalt.hp = max(1,Zalt.hp-80)
                    "{b}{color=#c22719}You lose 80 HP {/color}but at least you reach the ground."
                    "The earth beneath you shakes violently."
                    "You turn and see the statue tumbling down and crashes against the wall behind."
                    "The statue’s head falls a few feet from where you stood earlier."
                    "Now you have a way back up. "
                    $ Map.ca17 = 3
                    $ Map.ca18 = 1

                    $ Zalt.A_exp = Zalt.A_exp + 30*Zalt.A_exp_lv
                    $ PPEXP = 30*Zalt.A_exp_lv
                    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                    jump Cave_map
            "Leave" if True:
                jump Cave_map




label Cave_leave:
    scene black
    $ Zalt.A_exp = 0
    $ Zalt.A_lv = 0
    $ Zalt.dungeon = False
    $ Zalt.Dungeon_leave = False
    $ Map.undercity_here = False
    "You leave the dungeon."
    $ config.rollback_enabled = True
    jump forest_map0


label Cave_pillars:
    "You reach the end of a chasm."
    "On your side there are two stone pillars, while across there is only one. "
    "Standing right in the middle of the gap is another stone pillar, it looks like it’s standing strong. "
    "You need to get across somehow. The question is, how?"
    menu:
        "Check the chasm." if True:
            "You look down from the chasm, you really don't know what will happen if you falls down."
            menu:
                "Leap onto the middle pillar(Agility Check)" if Map.ca9 !=2:
                    e 1 "Looks easy enough to jump."
                    "You take a good look at the space between the ledge and the middle pillar."
                    "Backing away a few steps you make a running start and leap towards the middle pillar."
                    if Zalt.agi >= 7:
                        "{b}{color=#19c22a}<Agile Check success>{/color}"
                        "You manage to stick the landing and leap off to the other side."
                        e 3 "Easy! "
                        $ Map.ca9 = 3
                        $ Map.ca13 = 1
                        $ Map.ca15 = 1

                        $ Zalt.A_exp = Zalt.A_exp + 30*Zalt.A_exp_lv
                        $ PPEXP = 30*Zalt.A_exp_lv
                        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                        jump Cave_map
                    elif True:
                        "{b}{color=#c22719}<Agile Check failed>{/color}"
                        e 9 "Wah!!"
                        scene black with dissolve
                        play sound "music/splash.wav"
                        if Map.ca5 != 4:
                            "Your feet slip right on the top of the pillar and you fall into the river below."
                            "Fortunately, the waters below cushions your fall, but you still sustain damage."
                            "The current forces you along the river until you see a cloaked figure by the river bank riding a shadowy boat."
                            play sound "music/swim.wav"
                            "You swim ashore and manage to pull yourself out of the waters."
                            "Coughing and breathing violently, you’re dead exhausted from the fall."
                            $ Zalt.hp = max(1,Zalt.hp-50)
                            $ Zalt.mp = max(1,Zalt.mp-50)
                            "{b}{color=#c22719}You lose 50 HP and 50 MP.{/color}"
                            "Cloaked Figure" "Show me proof of your identity to board this vessel."
                            e 12 "Shut up!"
                            "You wait until you are able to breathe like normal to continue your journey."
                            $ Map.ca9 = 2
                        elif True:
                            "Your feet slip right on the top of the pillar and you fall into the river below."
                            "Fortunately, the waters below cushions your fall, but you still sustain damage."
                            "The current forces you along the river until you see a shadowy boat."
                            play sound "music/swim.wav"
                            "You swim ashore and manage to pull yourself out of the waters."
                            "Coughing and breathing violently, you’re dead exhausted from the fall."
                            $ Zalt.hp = max(1,Zalt.hp-50)
                            $ Zalt.mp = max(1,Zalt.mp-50)
                            "{b}{color=#c22719}You lose 50 HP and 50 MP.{/color}"
                            "You wait until you are able to breathe like normal to continue your journey."
                            $ Map.ca9 = 2
                        jump Cave_map
                "Try other ways" if True:

                    jump Cave_pillars
        "Check the pillar near you." if True:
            e 13 "Safest thing right now is to build a bridge to the other side."
            e 1 "This pillar here looks long enough."
            menu:
                "Make a bridge from the fallen pillar(Strength Check)" if True:
                    "Squatting in front of one of the pillars you wrap your arms around the structure and hug it tightly."
                    if Zalt.str >= 8:
                        e 12 "Hrgh!"
                        "{b}{color=#19c22a}<Strength Check success>{/color}"
                        "You focus all your strength into pulling the structure from the ground."
                        "Your eyes feel like they are bulging out as you pull with all your might."
                        "Slowly but surely the pillar starts to budge and with a mighty roar you pull the entire pillar out and slam it across to the other side."
                        "Dusting the dirt off your hands you give your right bicep a pat."
                        $ Map.ca9 = 3
                        $ Map.ca13 = 1
                        $ Map.ca15 = 1

                        $ Zalt.A_exp = Zalt.A_exp + 30*Zalt.A_exp_lv
                        $ PPEXP = 30*Zalt.A_exp_lv
                        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                        jump Cave_map
                    elif True:
                        e 12 "Hrgh!"
                        "{b}{color=#c22719}<Strength Check failed>{/color}"
                        "You focus all your strength into pulling the structure from the ground, but it does n’t move an inch."
                        "Defeated, you let go of the pillar."
                        e 12 "Damn it, I ’m not strong enough. I need a different way across."
                        jump Cave_pillars
                "Try other ways" if True:

                    jump Cave_pillars
        "Check the pillar on another side." if True:

            e 13 "The pillar on another side seems easier to be pulled down than the pillar next to you."
            e 1 "But I need a rope to reach it."
            menu:
                "Make a bridge from the fallen pillar(Strength Check)" if True:
                    if jane_inv_M.qty(rope) >= 1:
                        $ jane_inv_M.drop(rope,1)
                        "With the first rope you toss it across and it catches the other pillar. "
                        "And you pull it."
                        if Zalt.str >= 6:
                            e 12 "Hrgh!"
                            "{b}{color=#19c22a}<Strength Check success>{/color}"
                            "You focus all your strength into pulling the structure from the ground."
                            "Your eyes feel like they are bulging out as you pull with all your might."
                            "Slowly but surely the pillar starts to budge and with a mighty roar you pull the entire pillar out and slam it across to the other side."
                            "Dusting the dirt off your hands you give your right bicep a pat."
                            $ Map.ca9 = 3
                            $ Map.ca13 = 1
                            $ Map.ca15 = 1

                            $ Zalt.A_exp = Zalt.A_exp + 30*Zalt.A_exp_lv
                            $ PPEXP = 30*Zalt.A_exp_lv
                            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                            jump Cave_map
                        elif True:
                            e 12 "Hrgh!"
                            "{b}{color=#c22719}<Strength Check failed>{/color}"
                            "You focus all your strength into pulling the structure from the ground, but it does n’t move an inch."
                            "Defeated, you let go of the pillar."
                            e 12 "Damn it, I ’m not strong enough. I need a different way across."
                            jump Cave_pillars
                    elif True:


                        e 1 "I get a idea."
                        e 13 "I’m going to need 1 rope to make this plan work. "
                        jump Cave_pillars
                "Use ropes to make a rope bridge" if True:
                    if jane_inv_M.qty(rope) >= 2:
                        $ jane_inv_M.drop(rope,2)
                        e 13 " I have an idea, it might just be crazy enough to work."
                        "You pull out two bundles of rope from your bag, and tie them both into lassos."
                        "With the first rope you toss it across and it catches the other pillar. "
                        "The rope falls onto the ground and you pull to tighten it."
                        "With the other end you tie the rope around the pillar near you."
                        "Now comes the hard part."
                        "The second rope has to land perfectly on the top of the pillar across for this to work."
                        "You swing the lasso with one hand, and take deep breaths to steady yourself."
                        "You toss the rope and just as it lands and slides a few feet you pull as hard as you can locking it in place. "
                        e 0 "Yes!"
                        "You tie the other end just as high and successfully make a rope bridge."
                        "Tugging both ropes to ensure they’re secure you slowly hold onto the top of the rope and side step to the other side."
                        "It takes you awhile but you manage to reach the other side."
                        $ Map.ca9 = 3
                        $ Map.ca13 = 1
                        $ Map.ca15 = 1

                        $ Zalt.A_exp = Zalt.A_exp + 30*Zalt.A_exp_lv
                        $ PPEXP = 30*Zalt.A_exp_lv
                        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                        jump Cave_map
                    elif True:
                        e 1 "I get a idea."
                        e 13 "I’m going to need 2 ropes to make this plan work. "
                        jump Cave_pillars
                "Leave" if True:
                    jump Cave_map
        "Leave" if True:


            jump Cave_map




screen cave_map:
    imagemap:
        idle 'cave_map'
        hover 'cave_map'

        vbox:
            xalign 0.64 ypos 0.71
            imagebutton:
                idle "UI/down button1.png"
                hover "UI/down button2.png"

                action Return("exit")
        vbox:
            xalign 0.62 ypos 0.67
            imagebutton:
                idle "UI/button1.png"
                hover "UI/button2.png"
                action Return("point 1")
        vbox:
            xalign 0.65 ypos 0.54
            if Map.ca2 ==0:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 2")
            elif Map.ca2 == 1:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.69 ypos 0.44
            if Map.ca3 >= 1 and Map.ca3 <= 4:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 3")
            else:
                pass
        vbox:
            xalign 0.5 ypos 0.5
            if Map.ca4 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 4")
            elif Map.ca4 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.53 ypos 0.37
            if Map.ca5 >= 1 and Map.ca5 <= 5:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 5")
            else:
                pass
        vbox:
            xalign 0.245 ypos 0.275
            if Map.ca6 >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 6")
            else:
                pass
        vbox:
            xalign 0.4 ypos 0.54
            if Map.ca7 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 7")
            elif Map.ca7 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.42 ypos 0.65
            if Map.ca8 >= 1 and Map.ca8 <4:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 8")
            elif Map.ca8 == 4:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.37 ypos 0.5
            if Map.ca9 >= 1 and Map.ca9 <= 2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 9")
            elif Map.ca9 == 3:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.22 ypos 0.56
            if Map.ca10 == 1 or Map.ca10 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 10")
            elif Map.ca10 ==3:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.23 ypos 0.69
            if Map.ca11 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 11")
            elif Map.ca11 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.18 ypos 0.5
            if Map.ca12 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 12")
            elif Map.ca12 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.28 ypos 0.42
            if Map.ca13 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 13")
            elif Map.ca13 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.24 ypos 0.46
            if Map.ca14 >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 14")
            else:
                pass
        vbox:
            xalign 0.3 ypos 0.31
            if Map.ca15 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 15")
            elif Map.ca15 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.48 ypos 0.275
            if Map.ca16 >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 16")
            else:
                pass
        vbox:
            xalign 0.365 ypos 0.2
            if Map.ca17 >= 1 and Map.ca17 <= 2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 17")
            elif Map.ca17 == 3:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.37 ypos 0.25
            if Map.ca18 >= 1 and Map.ca18 <=3:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 18")
            elif Map.ca18 == 4:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.435 ypos 0.36
            if Map.ca19 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 19")
            elif Map.ca19 == 2 or Map.ca19 ==3:
                imagebutton:
                    idle "UI/down button1.png"
                    hover "UI/down button2.png"
                    action Return("point 19")
            else:
                pass
    frame:
        xalign 0.97 ypos 0.84
        imagebutton:
            idle "UI/bag01.png"
            hover "UI/bag02.png"

            action Show("bag"),Hide("inventory_screen"),Show("inventory_screen", first_inventory=jane_inv),Show("EWinventory_view_new", inventory=jane_equipment)
    frame:
        xalign 0.89 ypos 0.84
        imagebutton:
            idle "UI/stats01.png"
            hover "UI/stats02.png"

            action Show("stats")



label Cave_map_ferryman:
    stop music
    $ Time.mins = Time.mins +10
    $ Zalt.dungeon = True
    $ config.rollback_enabled = False
    $ renpy.music.set_volume(1, 5, channel = "Chan1")
    $ renpy.music.set_pause(False, channel='Chan1')
    window hide None
    if Zalt.Dungeon_leave:
        jump Cave_leave
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Zalt.A_exp >= 100:
        $ Zalt.A_exp = Zalt.A_exp -100
        $ Zalt.A_lv = min(Zalt.A_lv + 1, 5)
        $ Zalt.AP = Zalt.AP +1
        "You get one AP, you have [Zalt.AP] now."
        "Your A-LV now is [Zalt.A_lv]"


    if Zalt.A_lv == 5:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 4:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 3:
        $ Zalt.A_exp_lv = 2
    elif Zalt.A_lv == 2:
        $ Zalt.A_exp_lv = 1.5
    elif Zalt.A_lv == 1:
        $ Zalt.A_exp_lv = 1.2
    elif True:
        $ Zalt.A_exp_lv = 1


    scene cave 1 with dissolve
    play music "music/drip.ogg"
    call screen Cave_map_ferryman with dissolve
    if _return == 'Knight_point1':
        $ Time.mins = Time.mins +10
        "The ferryman is waiting for you."
        menu:
            "Leave" if True:
                e 1 "Time to leave."
                "The figure bows slightly."
                $ renpy.music.set_volume(0, 3, channel = "Chan1")
                "The cloaked figure gestures to the empty seat on his boat."
                hide ferryman stand with dissolve
                "You get on it."
                scene black with vslow_dissolve
                play music "music/wave.ogg"
                pause 3
                $ Map.cak0 = 0
                jump Cave_map
            "Not yet" if True:
                jump Cave_map_ferryman
        return
    if _return == 'Knight_point2':
        $ Time.mins = Time.mins +10

        if jane_inv_K.qty(pickaxe) == None:
            e 5 "This is....Blood crystals!"
            e 5 "I can't believe I will come across this kind of crystal here."
            e 13 "Only if I have a pickaxe."
            jump Cave_map_ferryman
        elif True:
            if Map.cak2 != Time.days:
                "You mine some blood crystals"
                $ Random = renpy.random.randint(1, 2)
                $ jane_inv_M.take(blood_crystals,Random)
                "You get [Random] blood crystals."
                $ Map.cak2 = Time.days
                jump Cave_map_ferryman
            elif True:
                e 13 "The vein is exhausted temporarily, maybe I will come back later."
                jump Cave_map_ferryman
        jump Cave_leave
        return
    if _return == 'Jester_point1':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "The ferryman is waiting for you."
        menu:
            "Leave" if True:
                e 1 "Time to leave."
                "The figure bows slightly."
                $ renpy.music.set_volume(0, 3, channel = "Chan1")
                "The cloaked figure gestures to the empty seat on his boat."
                hide ferryman stand with dissolve
                "You get on it."
                scene black with vslow_dissolve
                play music "music/wave.ogg"
                pause 3
                $ Map.caj0 = 0
                jump Cave_map
            "Not yet" if True:
                jump Cave_map_ferryman
        jump Cave_leave
        return
    if _return == 'Jester_point2':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.caj2 == 0:
            "You approach the treasure chest. "
            "With your sword you knock the top of the chest. Nothing happens."
            "Figuring it's safe you open the chest."
            e 5 "Wow!"
            "Inside you find a large pile of coins."
            "You get 1000 coins."
            $ jane_inv.take(coin,1000)
            $ Map.caj2 = 1
        elif True:
            "It is an empty chest."
        jump Cave_map_ferryman


        return
    if _return == 'Jester_point3':
        $ Time.mins = Time.mins +10
        if Map.caj3 == 0:
            "You head towards the hole in the wall."
            "Just as you approach the hole the earth beneath your feet shakes."
            "Something is approaching!"
            "You run back and draw your sword."
            "A gargoyle attacks!"
            $ Map.caj3 = 1
            $ Map.caj3g = 1
            jump battle_gargoyle
        elif True:
            "Here is the gargoyle lair."
            "Do you want to challenge?"
            menu:
                "Yes" if True:
                    "A gargoyle attacks!"
                    $ Map.caj3g = 1
                    jump battle_gargoyle
                "No" if True:
                    jump Cave_map_ferryman


        return

screen Cave_map_ferryman:
    imagemap:
        idle 'cave_map'
        hover 'cave_map'
        vbox:
            xalign 0.63 ypos 0.22
            if Map.cak0 != 0:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("Knight_point1")
            else:
                pass
        vbox:
            xalign 0.65 ypos 0.2
            if Map.cak0 != 0:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("Knight_point2")
            else:
                pass
        vbox:
            xalign 0.56 ypos 0.33
            if Map.caj0 != 0:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("Jester_point1")
            else:
                pass
        vbox:
            xalign 0.615 ypos 0.375
            if Map.caj0 != 0:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("Jester_point2")
            else:
                pass
        vbox:
            xalign 0.63 ypos 0.43
            if Map.caj0 != 0:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("Jester_point3")
            else:
                pass
    frame:
        xalign 0.97 ypos 0.84
        imagebutton:
            idle "UI/bag01.png"
            hover "UI/bag02.png"

            action Show("bag"),Hide("inventory_screen"),Show("inventory_screen", first_inventory=jane_inv),Show("EWinventory_view_new", inventory=jane_equipment)
    frame:
        xalign 0.89 ypos 0.84
        imagebutton:
            idle "UI/stats01.png"
            hover "UI/stats02.png"

            action Show("stats")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
