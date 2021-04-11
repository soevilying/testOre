label Mountain_map:
    stop Thane
    $ renpy.music.set_volume(1, 5.5, channel = "music")
    $ Time.mins = Time.mins +10
    window hide None
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1

    if Time.hours >= 6 and Time.hours <= 17:
        scene mountain 1 with dissolve
    elif True:
        scene mountain 1n with dissolve

    call screen mountain_map with dissolve
    if _return == 'tribe':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        jump Bull_tribe_map0
        return

    if _return == 'point 1':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        if Map.m1 == 0:
            "Winding paths and stone steps lead you up the mountain."
            "The road is mostly empty with vegetation growing only the side."
            "As you walk higher and higher you hear the faint sound of water rushing down like a waterfall."
            "You both then come upon a large white rock sitting on top of a flight of stairs."
            "You jog ahead of Thane to observe the rock."
            show black2
            show bullstone at center with slow_dissolve
            "The rock is marble white with red paint smeared across it in the shape of symbols you do not recognize. "
            "Around the rock you see pots of fresh colourful flowers, and a few dolls propped against the rock."
            e 1 "What is all this?"
            t "This is the shrine we erected to our fallen warriors... and to the children that were taken."
            t "There used to be groups of bulls coming up here to pay their respect to the fallen."
            t "Even the parents of their lost children came hoping that their wish for their children’s return would be answered."
            t "But as time went on less came up here, until everyone avoided coming here. It’s just too painful I guess."
            show black3 with dissolve
            show bulldoll at center with slow_dissolve
            "You hold one of the straw dolls in your hand. It’s dress is faded but you can tell it used to be a colourful doll of a bull."
            "You wonder, who was the child who had this doll before? Do the parents still wait for the child’s return? "
            "A sharp ache stabs your heart. You place the doll against the rock."
            hide bulldoll at center with dissolve
            hide black3 with dissolve
            e 13 "I’m sorry for their loss."
            t "Thank you. Your sympathy is appreciated."
            e 1 "One more thing, what are these markings by the way?"
            t "It’s our tribe’s language. It roughly translates to, “May the peace with us.”"
            e 1 "I wonder what it means."
            t "There are several ways to read into it, but we’ll save that for another time."
            t "Come, let’s continue forward."
            hide black2
            hide bullstone
            $ Map.m1 = 1
            $ Map.m2 = 1
            jump Mountain_map
        return
    if _return == 'point 2':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        if Map.m2 == 1:
            "As you continue forward your heart sinks as you approach a wall of fallen rocks blocking your way."
            t "Damn it, I should have known something like this would have happened."
            "The blockade is twice your height. It's uncertain how long this has been here."
            e 1 "It looks too big to clear for now."
            t "Maybe I can-"
            "Thane lowers himself into a squatting position."
            "He eyes the top of the wall of debris and with an audible grunt he leaps into the air and successfully lands on the top."
            t "It's stable up here. Come on!"
            "You take a few steps back. Taking a deep breath you make a running start and leap!"
            if Zalt.agi >= 5:
                "{b}{color=#19c22a}<Agile Check success>{/color}"
                "With precise timing you leap off one rock onto another until you reach Thane at the top."
                t "Impressive."
                e 6 "You expected anything else?"
                $ Map.m2 = 3
                $ Map.m3 = 1
                jump Mountain_map
            elif True:
                "{b}{color=#c22719}<Agile Check failed>{/color}"
                "Only to miss your landing on the wall for your second leap."
                "Instead you slam smack onto the wall and fall back."
                e 9 "Ughhh!" with vpunch
                t "That looked painful. Really thought you'd be more agile than that [name]."
                "Picking yourself off the ground you flip Thane off."
                t "Hahaha, you want to try again?"
                e 8 "I’m good, I still want to keep my teeth."
                e 1 "Is there some place I can get a rope or something?"
                t "Alright, just make your way back down to the general store."
                t "It's the one across from the training dummies. I'll be here till you get back."
                $ Map.m2 = 2
                jump Mountain_map
        elif True:
            if jane_inv_M.qty(rope) == None:
                t "Quit wasting time, go back to the village and buy a rope from the general store. I’ll wait here."
                jump Mountain_map
            elif True:
                $ jane_inv_M.drop(rope,1)
                "You pull out the rope you bought from your bag and tie one end into a lasso."
                e 1 "Thane! Heads up."
                "Thane catches the noose you throw at him and he ties it around one of the heavy rocks on the top of the debris wall. "
                t "It’s secured, come on up."
                "You nod in response and climb over the wall with the help of your rope."
                $ Map.m2 = 3
                $ Map.m3 = 1
                jump Mountain_map
        return
    if _return == 'point 3':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        t "If you look to your left you’ll see our tribe’s impound reservoir."
        e 1 "So, this is where the tribe gets its water?"
        t "It’s where we pool the water from the lake up top."
        t "The lake overflows with water so the first bulls that came here built channels to guide the water here, then it flows down to us."
        e 1 "The water is so clear you can see right straight to the bottom."
        t "Yeah, when I was just a calf I was never strong enough to make it all the way to the top."
        t "All the other calves could though. So, father left me here with a guard to watch over me."
        t "I always pretended that this was my personal mountain peak, and that if I had such a good time here the others would come join me."
        e 13 "Thane..."
        "He breaks into a nervous laughter."
        t "Come on [name], don’t give me those sad puppy dog eyes."
        t "It wasn’t all that bad. At least I got to play games with the different guards assigned to watch me."
        t "Then again, they could have just been doing it so father wouldn’t punish them."
        t "That and check out how much that wimpy calf grew."
        "He raises his spear over his head to show off the power in his muscular arms."
        "You chuckle and pat Thane on the back, his silly antics put you at ease, if he was upset about his time in the reservoir you can’t tell anymore."
        "The two of you continue your journey up the mountain."
        $ Map.m3 = 2
        $ Map.m4 = 1
        jump Mountain_map
        return
    if _return == 'point 4':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        "The sounds of crashing water grow louder as you near the midpoint of your climb."
        "From where you stand you can see the rushing waters descend from the lake above."
        "The air around you feels refreshingly cool against your sweaty body."
        t "Let’s take a quick break over here."
        "You nod in agreement."
        $ Map.m4 = 2
        $ Map.m5 = 1
        jump Mountain_map
        return
    if _return == 'point 5':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        "Thane leads you to an open area across from the falls. You both take a seat on two mounds of dirt high enough."
        e 1 "How much further before we reach the top?"
        t "Should be another hour, you tired already?"
        e 1 "No, I’m sweating like never before but I can still keep going."
        t "Come on, there’s no shame in admitting you need a shoulder to- OUCH!" with vpunch
        "Thane jolted up from his seat, stomping his feet against the ground and smacking his ass wildly."
        e 5 "Woah, woah! What the heck is wrong with you?"
        t "That’s a fire ant hill! They crawled up my AAAA." with vpunch
        "The bull smacks his ass so violently it can still be heard loudly amidst the roar of the falls."
        "It takes him a few minutes for the raging bull to calm down, breathing heavily as he softly massage his behind."
        "You laugh at Thane."
        "His cheeks turn a shade of pink. "
        t "It’s not funny!"
        e 3 "No, I’m not laughing because of the ants in your ass."
        e 3 "I’m laughing cause I finally figured you out."
        t "What?"
        e 1 "I mean think about it, the slime creatures, the chief’s punishment, the landslide, and the ants."
        e 1 "You’re the unluckiest bull I’ve ever met."
        t "..."
        t "So even you, huh. "
        e 1 "Huh?"
        "Thane sighs and walks over to pick up his spear."
        "He looks to the ground with a tired expression."
        t "“The Marked Bull,” that’s what the village folk called me since birth at least not to my face, but yeah."
        t "It’s basically their way of saying I bring misfortune anywhere I go."
        e 9 "I’m sorry, I didn't mean that."
        t "No, I don’t blame you, must mean that it’s really true if you see it."
        t "I mean how else would you explain killing your own mother through childbirth."
        t "How? Every time something would go wrong when I’m there."
        e 5 "That’s ridiculous, that’s like saying the sun goes down because a chicken died."
        t "It is silly, but our kind is a superstitious bunch."
        t "Eventually, after being called bad luck all my life I can’t help but believe in it."
        t "And I could take all the whispering behind my back, the teasing, the shunning, but I hated how I know my own father believes it’s true. "
        e 1 "I-"
        "Thane puts a fingers on your lips."
        t "No, not another word of pity from you."
        t "The last thing I ever want is someone to pity me."
        if Foe.spydie == 0:
            "He brushes his finger away."
            t "I know I can be a great chief and show everyone that I’m not a victim of luck."
            t "I believe this more than ever since the day I met you."
            t "That day was one of the luckiest moments of my life."
            "You both exchanges warm smiles."
            e 7 "Well I’m glad you have faith in me."
            "Thane nods and extends his hand for you to grab on to, he pulls you onto your feet so quickly your face bounces off his chest, slightly bruising your nose."
            e 5 "Ow." with vpunch
            t "Woops!"
            "His luck is truly remarkable. You both continue your journey."
        elif True:
            "He brushes his finger away."
            t "If I blame my luck, then that lizard would have died for nothing."
            t "And I... I can’t let that happen again."
            t "So please, let’s just keep all this talk of luck for some other time."
            e 13 "Ok, I understand."
            "You both continue your journey."

        $ Map.m5 = 2
        $ Map.m6 = 1
        $ Map.m7 = 1
        jump Mountain_map
        return
    if _return == 'point 6':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        if Map.m6 == 1 and Thane.mountain == 1:
            "On your way from the falls you notice a fork in the road that leads to a collection of brightly coloured rocks and ore veins on the right side."
            "Only if you had a pickaxe."
            t "I know what you’re thinking."
            t "If you want to mine those, you’ll need to get a permit from the general store."
            t "The bull that runs the shop will also take anything you mine and help turn it into something useful."
            e 1 "That’s pretty handy."
            t "But I’m not sure if he’s giving out the permits right now."
            t "He’s temperamental about these things."
            t "Even father has difficulties getting him to bend to his ways."
            e 1 "There’s actually someone who can stand up to your father? That’s impressive."
            t "He is the best weaponsmith in the village, and we rely on him for our equipment should we ever go to war."
            t "Everyone knows this, so we let him be, you can’t force good work."
            e 1 "Either way, I’ll make sure to remember to see him for a pickaxe, and a permit."
            t "You know, I’ve noticed that you never write anything down when you get a job."
            e 1 "What can I say I have a pretty good memory."
            t "Right."
            $ Map.m6 = 2
            jump Mountain_map
        elif Map.m6 == 1 and Thane.mountain != 1:
            "On your way from the falls you notice a fork in the road that leads to a collection of brightly coloured rocks and ore veins on the right side."
            "Only if you had a pickaxe."
            $ Map.m6 = 2
            jump Mountain_map
        elif Map.m6 == 2:
            if jane_inv_K.qty(pickaxe) == None:
                "On your way from the falls you notice a fork in the road that leads to a collection of brightly coloured rocks and ore veins on the right side."
                "Only if you have a pickaxe."
                jump Mountain_map
            elif True:
                if Map.ore != Time.days:
                    "You mine a fresh ore vein."
                    $ Random = renpy.random.randint(2, 3)
                    $ jane_inv_M.take(iron_ore,Random)
                    "You get [Random] iron ore."
                    $ Map.ore = Time.days
                    jump Mountain_map
                elif True:
                    "According to the permit, only the ore is allowed to be mined only once time per day."
                    jump Mountain_map
        elif True:
            "If you see this, that mean this is a bug or you're cheater."
            jump Mountain_map
        return
    if _return == 'point 7':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        "You walk side by side Thane."
        "Your movements have slowed since the start of the climb, but you both still persist on."
        "Something catches your attention from above you."
        e 1 "Hey, I see the tip!"
        t "What?" with vpunch
        "Your companion frantically drops his spear and starts adjusting his loincloth."
        t "Hey! You tricked me, my dick isn't out."
        "He huffs at you and picks up his weapon."
        e 9 "Seriously, how do you jump to that conclusion so quick?"
        e 9 "I meant I see the tip of the temple's top."
        t "Muhh."
        e 3 "I'll be more specific next time."
        t "Come on, the bridge is right up ahead."
        $ Map.m7 = 2
        $ Map.m8 = 1
        jump Mountain_map
        return
    if _return == 'point 8':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        "The stone bridge that you cross, the way each slab was cut feels refined and delicate to the touch. "
        "It's nothing like the architecture you saw in the bull village."
        "They don't even use stones to build their huts. "
        e 1 "Hey, how did the bulls build this bridge? "
        t "We didn't. It was already here before our tribe first settled below the mountain."
        e 1 "Then who or what built this bridge?"
        t "It's not just the bridge, whoever lived in these lands made the structure that became our temple as well."
        t "There are theories going around the tribe, but honestly, nobody knows who made them."
        e 1 "A mysterious temple built by a mysterious tribe. This I got to see."
        $ Map.m8 = 2
        $ Map.m9 = 1
        $ Map.m10 = 1
        jump Mountain_map
        return
    if _return == 'point 9':
        play sound "music/foot1.ogg"
        play music [ "<silence 1.0>", "music/bulls_temple.ogg" ] fadein 3
        if Map.m9 == 1:
            if Time.hours < 18:
                $ Time.hours = 18
                $ Time.mins = 30
            elif True:
                $ Time.mins = Time.mins +30

            if Time.hours >= 24:
                $ Time.hours = Time.hours - 24
                $ Time.days = Time.days + 1
            if Time.mins >= 60:
                $ Time.mins = Time.mins -60
                $ Time.hours = Time.hours +1

            if Time.hours >= 6 and Time.hours <= 17:
                scene temple 1 with dissolve
            elif True:
                scene temple 1n with dissolve
            e 5 "Wow."
            e 5 "This place is amazing! It’s like a hidden paradise."
            "Bright green grass stretches as far as you can see."
            "Only to end around a large crystal clear lake."
            "The water shines like a bed of diamonds reflecting the sun's rays."
            "In the middle of the lake sits a magnificent marble structure."
            "It’s faded white colour blends well with the rest of the scenery."
            "You feel like you can look at it all day long."
            "Your face beams with excitement as the adventurer in you just wants to drop everything and run about exploring the new land."
            t "I can tell you like the place from the way your tail’s wagging."
            e 10 "Ack!"
            "You push down the base of your tail with both hands and try to tuck it between your legs to keep it out of view, but even if you are no match for your own tail."
            "Thane laughs at your frantic attempt to compose yourself."
            t "Don’t worry about that, I find it adorable. Come, I'll show you around."
            e 1 "O-ok!"
            $ Map.m9 = 2
            $ Thane.mountain = 2
            $ Thane.temple = 1
            $ Map.temple = 1
            jump Temple_map

        $ Time.hours = Time.hours +1
        jump Temple_map

        return
    if _return == 'point 10':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        if Map.m10 == 1 and Thane.mountain == 1:
            e 1 "Hey, where does that lead to."
            "You point to another fork in the road."
            "This time there’s a path leading downwards from the peak."
            "You see what looks like a broken suspension bridge, with one half dangling on the other side of the chasm."
            t "I have no idea actually."
            t "That bridge’s been broken ever since I first came up here."
            e 1 "So, you don’t know what’s on the other side?"
            t "Nope, but stay away from it."
            t "We couldn't have sent any of our men to clear the area, there may still be monsters in that area."
            e 1 "But, there could be some unknown discovery over there."
            t "Yeah, like your tombstone, “[name] died, not listening to his friend.”"
            e 5 "Ok, ok. No need to get so dramatic about it."
            "Thane leads you by the arm away from the bridge."
            $ Map.m10 = 2
            jump Mountain_map
        elif Map.m10 == 1 and Thane.mountain != 1:
            "It’s a broken bridge. You can’t reach the other side. Best turn back."
            $ Map.m10 = 2
            jump Mountain_map
        elif True:
            "It’s a broken bridge. You can’t reach the other side. Best turn back."
            jump Mountain_map
        return
screen mountain_map:
    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'mountainmap'
            hover 'mountainmap'
        else:
            idle 'mountainmapn'
            hover 'mountainmapn'

        vbox:
            xalign 0.47 ypos 0.66
            imagebutton:
                idle "UI/down button1.png"
                hover "UI/down button2.png"

                action Return("tribe")
        vbox:
            xalign 0.48 ypos 0.62
            if Map.m1 == 0:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 1")
            elif Map.m1 == 1:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.4 ypos 0.52
            if Map.m2 >= 1 and Map.m2 <= 2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 2")
            elif Map.m2 == 3:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.363 ypos 0.435
            if Map.m3 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 3")
            elif Map.m3 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.32 ypos 0.35
            if Map.m4 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 4")
            elif Map.m4 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.22 ypos 0.37
            if Map.m5 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 5")
            elif Map.m5 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.245 ypos 0.275
            if Map.m6 >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 6")
            else:
                pass
        vbox:
            xalign 0.245 ypos 0.15
            if Map.m7 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 7")
            elif Map.m7 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.33 ypos 0.15
            if Map.m8 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 8")
            elif Map.m8 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.48 ypos 0.19
            if Map.m9 >= 1:
                imagebutton:
                    idle "UI/up button1.png"
                    hover "UI/up button2.png"
                    action Return("point 9")
            else:
                pass
        vbox:
            xalign 0.48 ypos 0.275
            if Map.m10 >= 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 10")
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
