label forest_map_1:
    pause 0.5
    window hide None
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1

    if Time.hours >= 6 and Time.hours <= 17:
        scene forest 1 with slow_dissolve
    elif True:
        scene forest 1n with slow_dissolve
    if Map.forest1 == 1:
        "You explore the forest. There’s no path to lead you anywhere so you push through with your hunter’s instincts."
        "As you traverse through the woods you hear something bouncing and the sound of something wet landing on the ground."
        $ Map.forest1 = 2
    elif True:
        pass
    label forest_map_1_menu:
        $ Map.good_battle = False
        $ Random = renpy.random.randint(1, 3)
        $ Time.mins = Time.mins +20
        if Time.mins >= 60:
            $ Time.mins = Time.mins -60
            $ Time.hours = Time.hours +1
        if Time.hours >= 24:
            $ Time.hours = Time.hours - 24
            $ Time.days = Time.days + 1
        if Time.hours >= 6 and Time.hours <= 17:
            scene forest 1
        elif True:
            scene forest 1n
        show screen f1_goods
        menu:
            "Explore" if True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    if Time.hours >= 6 and Time.hours <= 17:
                        jump battle_slime
                    elif True:
                        if Witer.sleep >= 6:
                            $ Foe.ghostforest = 1
                            jump battle_ghost
                        elif True:
                            $ Random = renpy.random.randint(1, 4)
                            if Random == 1:
                                "You search around and find a sturdy stick."
                                "You get a stick."
                                $ jane_inv_M.take(stick)
                            elif Random == 2:
                                "You search around and find a hard rock."
                                "You get a rock."
                                $ jane_inv_M.take(rock)
                            elif True:
                                "You didn't find anything."
                            jump forest_map_1_menu
                elif True:


                    $ Random = renpy.random.randint(1, 5)
                    if Random == 1:
                        "You search around and find a sturdy stick."
                        "You get a stick."
                        $ jane_inv_M.take(stick)
                    elif Random == 2:
                        "You search around and find a hard rock."
                        "You get a rock."
                        $ jane_inv_M.take(rock)
                    elif True:
                        "You didn't find anything."
                    jump forest_map_1_menu
            "Leave" if True:


                hide screen f1_goods
                jump forest_map
    label f1_mushroom:
        $ Random_in = renpy.random.randint(1, 4)
        "You collected some mushrooms."
        $ Random_in = renpy.random.randint(1, 4)

        $ mushroom_check = renpy.random.randint(1, 5)
        $ mushroom_check = renpy.random.randint(1, 5)
        if mushroom_check == 1:
            "You get 1 toadstool."
            $ jane_inv_M.take(toadstool,1)
        elif True:
            $ mushroom_get = renpy.random.randint(1, 2)
            $ mushroom_get = renpy.random.randint(1, 2)
            "You get [mushroom_get] shiitake."
            $ jane_inv_M.take(shiitake,mushroom_get)

        if Random_in == 1:
            $ Map.f1_mushroom = Time.days + 2
        elif Random_in == 4:
            $ Map.f1_mushroom = Time.days + 3
        elif Random_in == 2 or Random_in == 3:
            $ Map.f1_mushroom = Time.days + 1
        elif True:
            "Bug here, pls report to Caro!"

        jump forest_map_1_menu
    label f1_carrot:
        if jane_inv_K.qty(small_shovel) == None:
            "It looks like some kind of ingredient, but the soil is too hard."
            "You can't dig it out of the soil without tools."
            jump forest_map_1_menu
        elif True:
            $ Random_in = renpy.random.randint(1, 4)
            "You dig the ground with your shovel."
            $ Random_in = renpy.random.randint(1, 4)
            "You get 1 carrot."
            $ jane_inv_M.take(carrot,1)
            $ worm_check = renpy.random.randint(1, 5)
            $ worm_check = renpy.random.randint(1, 5)
            if worm_check == 1 or worm_check == 2:
                $ worm_get = renpy.random.randint(1, 2)
                "You also get [worm_get] worm bait."
                $ jane_inv_M.take(worm_bait,worm_get)
            if Random_in == 1:
                $ Map.f1_carrot = Time.days + 2
            elif Random_in == 4:
                $ Map.f1_carrot = Time.days + 3
            elif Random_in == 2 or Random_in == 3:
                $ Map.f1_carrot = Time.days + 1
            elif True:
                "Bug here, pls report to Caro!"

        jump forest_map_1_menu
screen f1_goods:
    vbox:
        xalign 0.13 ypos 0.69
        if Map.f1_mushroom <= Time.days:
            if Map.good_battle == False:
                imagebutton:
                    idle "map/forest_things/mushroom_01.png"
                    hover "map/forest_things/mushroom_02.png"

                    action Jump("f1_mushroom")
            else:
                imagebutton:
                    idle "map/forest_things/mushroom_01.png"
                    hover "map/forest_things/mushroom_02.png"

                    action None
        else:
            pass
    vbox:
        xalign 0.8 ypos 0.8
        if Map.f1_carrot <= Time.days:
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/carrot_01.png"
                        hover "map/forest_things/carrot_02.png"

                        action Jump("f1_carrot")
                else:
                    imagebutton:
                        idle "map/forest_things/carrot_01.png"
                        hover "map/forest_things/carrot_02.png"

                        action None
            else:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/carrot_01n.png"
                        hover "map/forest_things/carrot_02n.png"

                        action Jump("f1_carrot")
                else:
                    imagebutton:
                        idle "map/forest_things/carrot_01n.png"
                        hover "map/forest_things/carrot_02n.png"

                        action None

        else:
            pass

label forest_map_2:
    window hide None
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1

    if Time.hours >= 6 and Time.hours <= 17:
        scene forest 2 with slow_dissolve
    elif True:
        scene forest 2n with slow_dissolve

    if Map.boss1 == 1:
        jump battle_skull_boss

    if jane_inv_K.qty(sack) != None and Quest.fes == 1:
        $ Quest.fes = 2
        e 8 "This is ridiculous, how far is this thing?"
        "The trail of fruits have started to dwindle, but you can still find some of them leading you deeper into the forest."
        "All you hear are the sounds of your footsteps breaking the dried up leaves beneath your feet."
        "Your tranquil walk is quickly interrupted when three slimes scurry out of a bush and dash past you."
        "They’re carrying fruits on top of their heads as they hop off. "
        "You believe you’re getting close to your target."
        "The smell leads you to where you met the spy before."
        jump forest_map
    elif True:
        label forest_map_2_menu:
            $ Map.good_battle = False
            show screen f2_goods
            $ Random = renpy.random.randint(1, 3)
            $ Time.mins = Time.mins +20
            if Time.mins >= 60:
                $ Time.mins = Time.mins -60
                $ Time.hours = Time.hours +1
            if Time.hours >= 24:
                $ Time.hours = Time.hours - 24
                $ Time.days = Time.days + 1
            if Time.hours >= 6 and Time.hours <= 17:
                scene forest 2
            elif True:
                scene forest 2n
            menu:
                "Explore" if True:
                    $ Random = renpy.random.randint(1, 3)
                    if Random == 1:
                        if Time.hours >= 6 and Time.hours <= 17:
                            jump battle_slime
                        elif True:
                            if Witer.sleep >= 6:
                                $ Foe.ghostforest = 2
                                jump battle_ghost
                            elif True:
                                "You didn't find anything."
                                jump forest_map_2_menu
                    elif Random == 2:
                        if Time.hours >= 6 and Time.hours <= 17:
                            jump battle_slime
                        elif True:
                            if Witer.sleep >= 6:
                                $ Foe.ghostforest = 2
                                jump battle_ghost
                            elif True:
                                "You didn't find anything."
                                jump forest_map_2_menu
                    elif True:
                        "You didn't find anything."
                        jump forest_map_2_menu
                "Smell the dried flower" if Hakan.quest == 3:
                    hide screen f2_goods
                    $ Hakan.quest = 4
                    "The scent of vanilla is strong in the air."
                    "Your keen sense of smell allows you to track it’s source."
                    "It’s almost like seeing a stream of colours in the air, and you see the one that will lead you to your target."
                    "You forge straight ahead, deeper into the forest."
                    hide screen f2_goods
                    jump forest_map
                "Leave" if True:
                    hide screen f2_goods
                    jump forest_map
    label f2_mushroom:
        $ Random_in = renpy.random.randint(1, 4)
        "You collected some mushrooms."
        $ Random_in = renpy.random.randint(1, 4)

        $ mushroom_check = renpy.random.randint(1, 5)
        $ mushroom_check = renpy.random.randint(1, 5)
        if mushroom_check == 1:
            "You get 1 toadstool."
            $ jane_inv_M.take(toadstool,1)
        elif True:
            $ mushroom_get = renpy.random.randint(1, 2)
            $ mushroom_get = renpy.random.randint(1, 2)
            "You get [mushroom_get] shiitake."
            $ jane_inv_M.take(shiitake,mushroom_get)


        if Random_in == 1:
            $ Map.f2_mushroom = Time.days + 2
        elif Random_in == 4:
            $ Map.f2_mushroom = Time.days + 3
        elif Random_in == 2 or Random_in == 3:
            $ Map.f2_mushroom = Time.days + 1
        elif True:
            "Bug here, pls report to Caro!"

        jump forest_map_2_menu
    label f2_potato:
        if jane_inv_K.qty(small_shovel) == None:
            "It looks like some kind of ingredient, but the soil is too hard."
            "You can't dig it out of the soil without tools."
            jump forest_map_2_menu
        elif True:
            $ Random_in = renpy.random.randint(1, 4)
            "You dig the ground with your shovel."
            $ Random_in = renpy.random.randint(1, 4)
            $ potato_check = renpy.random.randint(1, 2)
            $ potato_check = renpy.random.randint(1, 2)
            "You get [potato_check] potato."
            $ jane_inv_M.take(potato,potato_check)
            $ worm_check = renpy.random.randint(1, 5)
            $ worm_check = renpy.random.randint(1, 5)
            if worm_check == 1 or worm_check == 2:
                $ worm_get = renpy.random.randint(1, 2)
                "You also get [worm_get] worm bait."
                $ jane_inv_M.take(worm_bait,worm_get)
            if Random_in == 1:
                $ Map.f2_potato = Time.days + 2
            elif Random_in == 4:
                $ Map.f2_potato = Time.days + 3
            elif Random_in == 2 or Random_in == 3:
                $ Map.f2_potato = Time.days + 1
            elif True:
                "Bug here, pls report to Caro!"

        jump forest_map_2_menu
screen f2_goods:
    vbox:
        xalign 0.54 ypos 0.69
        if Map.f2_mushroom <= Time.days:
            if Map.good_battle == False:
                imagebutton:
                    idle "map/forest_things/mushroom_01.png"
                    hover "map/forest_things/mushroom_02.png"

                    action Jump("f2_mushroom")
            else:
                imagebutton:
                    idle "map/forest_things/mushroom_01.png"
                    hover "map/forest_things/mushroom_02.png"

                    action None
        else:
            pass
    vbox:
        xalign 0.85 ypos 0.79
        if Map.f2_potato <= Time.days:
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/potato_01.png"
                        hover "map/forest_things/potato_02.png"

                        action Jump("f2_potato")
                else:
                    imagebutton:
                        idle "map/forest_things/potato_01.png"
                        hover "map/forest_things/potato_02.png"

                        action None
            else:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/potato_01n.png"
                        hover "map/forest_things/potato_02n.png"

                        action Jump("f2_potato")
                else:
                    imagebutton:
                        idle "map/forest_things/potato_01n.png"
                        hover "map/forest_things/potato_02n.png"

                        action None

        else:
            pass
label forest_map_3:
    window hide None
    $ renpy.music.set_pause(True, channel='Thane')
    $ renpy.music.set_volume(0, 4, channel = "Thane")

    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1

    if Time.hours >= 6 and Time.hours <= 17:
        scene forest 3 with slow_dissolve
    elif True:
        scene forest 3n with slow_dissolve

    if Map.forest3 == 1:
        "The fog here is thick, and the forest is dense with foliage you’ve never seen before."
        "It’s eerie how the shadows of the trees can be mistaken for someone standing there watching you."
        "You proceed with caution.There’s no telling what you may find here."
        $ Map.forest3 = 2
    elif True:
        pass
    label forest_map_3_menu:
        $ Map.good_battle = False
        show screen f3_goods
        $ Random = renpy.random.randint(1, 4)
        $ renpy.music.set_pause(True, channel='Thane')
        $ renpy.music.set_volume(0, 4, channel = "Thane")

        $ Time.mins = Time.mins +20
        if Time.mins >= 60:
            $ Time.mins = Time.mins -60
            $ Time.hours = Time.hours +1
        if Time.hours >= 24:
            $ Time.hours = Time.hours - 24
            $ Time.days = Time.days + 1
        if Time.hours >= 6 and Time.hours <= 17:
            scene forest 3
        elif True:
            scene forest 3n
        menu:
            "Explore" if True:
                "You explore the foggy forest. The sound of rustling leaves and branches breaking tell you-you are not alone."
                $ Random = renpy.random.randint(1, 4)
                if Random == 1:
                    if Time.hours >= 6 and Time.hours <= 17:
                        jump battle_slime2
                    elif True:
                        if Witer.sleep >= 6:
                            $ Foe.ghostforest = 3
                            jump battle_ghost
                        elif True:
                            "You didn't find anything 1"
                            jump forest_map_3_menu
                elif Random == 2:
                    if Time.hours >= 6 and Time.hours <= 17:
                        jump battle_bull
                    elif True:
                        "Nothing happens, guess you were hearing things."
                        jump forest_map_3_menu
                elif Random == 3:
                    if Map.bulltribe == 0:
                        hide screen f3_goods
                        "You find a path leading into nothing but fog, you don't know what's inside."
                        "Do you want to go forward?"
                        menu:
                            "Yes" if True:
                                $ Map.bulltribe = 1
                                jump forest_map
                            "No" if True:
                                jump forest_map_3_menu
                    elif True:
                        if Thane.meet == 0:
                            jump battle_slimeT
                        elif True:
                            if Time.hours >= 6 and Time.hours <= 17:
                                jump battle_bull
                            elif True:
                                $ Random = renpy.random.randint(1, 5)
                                if Random == 1:
                                    "You get a stick."
                                    $ jane_inv_M.take(stick)
                                elif Random == 2:
                                    "You get a rock."
                                    $ jane_inv_M.take(rock)
                                elif True:
                                    "Nothing happens, guess you were hearing things."
                                jump forest_map_3_menu
                elif True:
                    if Thane.meet == 0:
                        hide screen f3_goods
                        jump battle_slimeT
                    elif True:
                        $ Random = renpy.random.randint(1, 5)
                        if Random == 1:
                            "You get a stick."
                            $ jane_inv_M.take(stick)
                        elif Random == 2:
                            "You get a rock."
                            $ jane_inv_M.take(rock)
                        elif True:
                            "Nothing happens, guess you were hearing things."
                        jump forest_map_3_menu

            "Find the way to the lake island" if (Snow.fish == 3 or (Snow.fish == -1 and Chet.ectoplasm == 2)) and Map.lakecabin == 0:
                hide screen f3_goods
                if Snow.fish == 3:
                    "Against Snow’s warning, you decide to travel to the island by the lake."
                    "You remembered what you saw last time, someone was watching you and Snow from over here."
                elif True:
                    "According to what Chet said, you decide to travel to the island by the lake."
                    "During one of his earlier travelers,he found a very interesting hut nearby the lake."
                $ Map.lakecabin = 1
                jump forest_map
            "Find Thane" if Thane.meet >= 1 and Thane.meet <= 2:
                hide screen f3_goods
                "You find Thane under the fruit tree."
                pause 0.5
                $ renpy.music.set_pause(True, channel='Chan1')
                $ renpy.music.set_pause(True, channel='Chan2')

                $ renpy.music.set_pause(False, channel='Thane')
                $ renpy.music.set_volume(1, 4, channel = "Thane")

                show thane stand at center with dissolve
                t "Oh,[name]."
                jump Thane_talk
            "Leave" if True:

                jump forest_map
    label f3_mushroom:
        $ Random_in = renpy.random.randint(1, 4)
        "You collected some mushrooms."
        $ Random_in = renpy.random.randint(1, 4)

        $ mushroom_check = renpy.random.randint(1, 5)
        $ mushroom_check = renpy.random.randint(1, 5)
        if mushroom_check == 1:
            "You get 1 toadstool."
            $ jane_inv_M.take(toadstool,1)
        elif True:
            $ mushroom_get = renpy.random.randint(1, 2)
            $ mushroom_get = renpy.random.randint(1, 2)
            "You get [mushroom_get] shiitake."
            $ jane_inv_M.take(shiitake,mushroom_get)

        if Random_in == 1:
            $ Map.f3_mushroom = Time.days + 2
        elif Random_in == 4:
            $ Map.f3_mushroom = Time.days + 3
        elif Random_in == 2 or Random_in == 3:
            $ Map.f3_mushroom = Time.days + 1
        elif True:
            "Bug here, pls report to Caro!"

        jump forest_map_3_menu
    label f3_berry:
        $ Random_in = renpy.random.randint(1, 4)
        "You collected some berry."
        $ Random_in = renpy.random.randint(1, 4)
        $ raspberry_check = renpy.random.randint(2, 5)
        "You get [raspberry_check] raspberry."
        $ jane_inv.take(raspberry,raspberry_check)
        if Random_in == 1:
            $ Map.f3_berry = Time.days + 2
        elif Random_in == 4:
            $ Map.f3_berry = Time.days + 3
        elif Random_in == 2 or Random_in == 3:
            $ Map.f3_berry = Time.days + 1
        elif True:
            "Bug here, pls report to Caro!"

        jump forest_map_3_menu
screen f3_goods:
    vbox:
        xalign 0.26 ypos 0.83
        if Map.f3_mushroom <= Time.days:
            if Map.good_battle == False:
                imagebutton:
                    idle "map/forest_things/mushroom_01.png"
                    hover "map/forest_things/mushroom_02.png"

                    action Jump("f3_mushroom")
            else:
                imagebutton:
                    idle "map/forest_things/mushroom_01.png"
                    hover "map/forest_things/mushroom_02.png"

                    action None
        else:
            pass
    vbox:
        xalign 0.935 ypos 0.572
        if Map.f3_berry <= Time.days:
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/redberry_01.png"
                        hover "map/forest_things/redberry_02.png"

                        action Jump("f3_berry")
                else:
                    imagebutton:
                        idle "map/forest_things/redberry_01.png"
                        hover "map/forest_things/redberry_02.png"

                        action None
            else:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/redberry_01n.png"
                        hover "map/forest_things/redberry_02n.png"

                        action Jump("f3_berry")
                else:
                    imagebutton:
                        idle "map/forest_things/redberry_01n.png"
                        hover "map/forest_things/redberry_02n.png"

                        action None

        else:
            pass
label river_1:
    window hide None
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1

    if Map.river == 1:
        stop music
        scene black
        play music "music/waterfall.wav" fadeout 1
        "You hear the sound of rushing water and head over to the source to investigate."
        "You find yourself standing in front of a dirt road connecting two sides of a ravine."
        "Cautiously you approach the path and place a foot on it to be sure its safe."
        if Time.hours >= 6 and Time.hours <= 17:
            scene river 1 with slow_dissolve
        elif True:
            scene river 1n with slow_dissolve
        "The ground feels very solid against your feet. "
        "Your attention is then drawn to what’s below the ravine."
        "A massive torrent cascades down a river into a large lake in the distance."
        "Across you see a dense wall of trees still shrouded in fog."
        "However, there is a fork in the road, one leading into the forest {p}and the other down towards a shallow close to the lake."
        "The longer you look at the trees,the more you feel your heart getting pulled towards the forest."
        "Even the way the fog rolls seems to tempt you to enter the forest."
        "You gulp, but steel your nerves by beating your chest once."
        "Instinct tells you there’s something important to be found in there, if it doesn’t kill you."
        "So, you walk down the path but you remain vigilant through the fog for any sign of a threat."
        $ Map.forest3 = 1
        $ Map.river = 2
        jump forest_map
    elif True:
        play music "music/waterfall.wav" fadeout 1
        if Time.hours >= 6 and Time.hours <= 17:
            scene river 1 with slow_dissolve
        elif True:
            scene river 1n with slow_dissolve
        label river_1_menu:
            $ Random = renpy.random.randint(1, 3)
            $ Time.mins = Time.mins +20
            if Time.mins >= 60:
                $ Time.mins = Time.mins -60
                $ Time.hours = Time.hours +1
            if Time.hours >= 24:
                $ Time.hours = Time.hours - 24
                $ Time.days = Time.days + 1
            if Time.hours >= 6 and Time.hours <= 17:
                scene river 1
            elif True:
                scene river 1n
            menu:
                "Explore" if True:
                    if Ebb.kidnap == 1:
                        "You’re on the right track, the shark’s smell is stronger now than before."
                        "The trail seems to be leading you to the cave near the lake."
                        scene black with dissolve
                        "Rushing forward following his scent, you hope you are not too late."
                        play sound "music/foot1.ogg"
                        $ Map.cave = 1
                        $ Ebb.kidnap = 2
                        jump forest_map
                    elif True:
                        if jane_inv_K.qty(Mysterious_note_1) == 1:
                            if jane_inv_K.qty(Mysterious_note_2) == None:
                                "Wait, what's this?"
                                "You find a Mysterious Note."
                                "It’s another piece of a journal."
                                "You read its contents."
                                "{u}{i}News has been spreading around the town about shadows kidnapping people off the street in the dead of night.{/i}{/u}"
                                "{u}{i}It’s gotten to the point that no one dares to be out when the sun goes down. {/i}{/u}"

                                "{u}{i}The king has made me his private inquisitor to investigate this strange case.{/i}{/u}"
                                "{u}{i}A task I will carry out diligently.{/i}{/u}"
                                "{u}{i}I swear upon the Divine Being of War’s blessing to bring this perpetrator to justice.{/i}{/u}"
                                "{u}{i}- Razik Gallows{/i}{/u}"
                                "The journal entry ends here."
                                $ jane_inv_K.take(Mysterious_note_2)
                            elif True:
                                "You stand upon the road that connects the ravine, watching the water run down into the lake."
                                "There is nothing to do here for now."
                            jump river_1_menu
                        elif True:
                            $ Random = renpy.random.randint(1, 3)
                            if Random == 1 and jane_inv_K.qty(Mysterious_note_2) == None:
                                "Wait, what's this?"
                                "You find a piece of Mysterious Note."
                                "You read its contents."
                                "{u}{i}News has been spreading around the town about shadows kidnapping people off the street in the dead of night.{/i}{/u}"
                                "{u}{i}It’s gotten to the point that no one dares to be out when the sun goes down. {/i}{/u}"

                                "{u}{i}The king has made me his private inquisitor to investigate this strange case.{/i}{/u}"
                                "{u}{i}A task I will carry out diligently.{/i}{/u}"
                                "{u}{i}I swear upon the Divine Being of War’s blessing to bring this perpetrator to justice.{/i}{/u}"
                                "{u}{i}- Razik Gallows{/i}{/u}"
                                "The journal entry ends here."
                                $ jane_inv_K.take(Mysterious_note_2)
                            elif True:
                                "You stand upon the road that connects the ravine, watching the water run down into the lake."
                                "There is nothing to do here for now."
                            jump river_1_menu
                "Leave" if True:
                    jump forest_map


label bulltribe_1:
    window hide None
    $ Time.mins = Time.mins +30
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Thane.quest == 3:
        if Time.hours >= 6 and Time.hours <= 17:
            scene tribe 1 with vslow_dissolve
        elif True:
            scene tribe 1n with vslow_dissolve
        e 1 "No, I need to find the spy first."
        jump forest_map
    stop Chan1
    stop Chan2
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    if Thane.quest >= 4:
        jump Bull_tribe_map0

    if Foe.bullab == 0:
        stop music fadeout 1
        scene black
        "Sunlight breaks through just up ahead, covering your eyes you walk straight ahead."
        if Time.hours >= 6 and Time.hours <= 17:
            scene tribe 1 with vslow_dissolve
        elif True:
            scene tribe 1n with vslow_dissolve
        "You squint and slowly open your eyes to readjust to the sunlight."
        e 5 "Woah…"
        "Groups of large scantily clad bull men roam the field."
        "Some stand by huts, talking and selling items to one another."
        "Others are working on weapons, repairing swords, axes and shields."
        "They don’t seem to notice your presence yet, so you head closer to them. "
        "As you walk, you take note of the rows of huts facing one another. "
        "It looks like this is what the members of the tribe use as shelter."
        "The rows of huts stretch out all the way up to the middle of a mountain in the distance,{p}where one massive tent sits overseeing the whole valley of huts."
        e 13 "This really reminds me of home. Someone pretty important must own that large tent."
        "Bull A" "Hey you!"
        "Just as you are about to approach the first tent two massive male bulls run up to you."
        "They stand taller over you by a feet."
        "Up close, their bulging muscles makes you feel even smaller near them."
        "Both of them eye you suspiciously."
        "Bull B" "It’s one of them from the other side."
        "Bull A" "We don’t like your kind. Your kind made this fog didn’t you?"
        e 5 " I’m not here looking for trouble."
        e 5 "I just followed a path here, and I have nothing to do with the fog."
        "Bull B" "Lies! All your kind lie, like that hyena!"
        "Bull A" "Rarghhh! No outsiders!"
        "The bulls attack!"
        jump battle_bullAB
    elif True:
        stop music fadeout 1
        if Time.hours >= 6 and Time.hours <= 17:
            scene tribe 1 with vslow_dissolve
        elif True:
            scene tribe 1n with vslow_dissolve
        "Bull A" "It’s him again!"
        "Bull B" "Ragh! Stupid outsider, we’ll beat you til you understand we don’t want you!"
        e 9 "It seems they won't listen to me."
        e 9 "I need to find a way to reconcile first."
        "You run away."
        jump forest_map

label forest_map_4:
    window hide None
    $ Time.mins = Time.mins +20
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    stop music fadeout 1
    scene forest 4 with slow_dissolve
    if Hakan.quest == 4:
        "The trail ends in front of a single branch sticking out of the mossy ground."
        "There’s five white flowers growing on the branch, but no sign of the tree creature."
        e 1 "Where are you hiding?"
        "You pick up a small stone and toss it towards the branch."
        "It knocks one of the flowers, but nothing happens."
        "The risks are high, but you walk closer towards it."
        play music "music/tree.ogg" fadein 1
        "Just as you are an arm’s length from the flower you sense powerful vibrations beneath your feet."
        play sound "music/treestep.ogg" fadein 1
        "Sharp wooden spikes burst through the earth." with vpunch
        "You don’t even have a second to think." with vpunch
        "Your legs instinctively propel you into the air with a powerful jump. " with vpunch
        "The spikes can’t reach you up in the air." with vpunch
        show tree at center with slow_dissolve
        "And you get a good look at the creature breaking free from its camouflage."
        "You land right in front of the monster with your sword drawn."
        "It’s massive! The bipedal creature is twice your size and is dangerously covered in spikes."
        "You ready your stance, and prepare to fight!"
        jump battle_tree
    elif True:
        pass
    label forest_map_4_menu:
        $ Map.good_battle = False
        show screen f4_goods
        menu:
            "Explore" if True:
                "The tree's corpse is still here,all the flowers on its back have withered away."
                "It seems there is nothing to do here for now."
                jump forest_map_4
            "Leave" if True:

                jump forest_map
    label f4_carrot:
        if jane_inv_K.qty(small_shovel) == None:
            "It looks like some kind of ingredient, but the soil is too hard."
            "You can't dig it out of the soil without tools."
            jump forest_map_4_menu
        elif True:
            $ Random_in = renpy.random.randint(1, 4)
            "You dig the ground with your shovel."
            $ Random_in = renpy.random.randint(1, 4)
            "You get 1 carrot."
            $ jane_inv_M.take(carrot,1)
            $ worm_check = renpy.random.randint(1, 5)
            $ worm_check = renpy.random.randint(1, 5)
            if worm_check == 1 or worm_check == 2:
                $ worm_get = renpy.random.randint(1, 2)
                "You also get [worm_get] worm bait."
                $ jane_inv_M.take(worm_bait,worm_get)
            if Random_in == 1:
                $ Map.f4_carrot = Time.days + 2
            elif Random_in == 4:
                $ Map.f4_carrot = Time.days + 3
            elif Random_in == 2 or Random_in == 3:
                $ Map.f4_carrot = Time.days + 1
            elif True:
                "Bug here, pls report to Caro!"

        jump forest_map_4_menu

    label f4_potato:
        if jane_inv_K.qty(small_shovel) == None:
            "It looks like some kind of ingredient, but the soil is too hard."
            "You can't dig it out of the soil without tools."
            jump forest_map_4_menu
        elif True:
            $ Random_in = renpy.random.randint(1, 4)
            "You dig the ground with your shovel."
            $ Random_in = renpy.random.randint(1, 4)
            $ potato_check = renpy.random.randint(1, 2)
            $ potato_check = renpy.random.randint(1, 2)
            "You get [potato_check] potato."
            $ jane_inv_M.take(potato,potato_check)
            $ worm_check = renpy.random.randint(1, 5)
            $ worm_check = renpy.random.randint(1, 5)
            if worm_check == 1 or worm_check == 2:
                $ worm_get = renpy.random.randint(1, 2)
                "You also get [worm_get] worm bait."
                $ jane_inv_M.take(worm_bait,worm_get)
            if Random_in == 1:
                $ Map.f4_potato = Time.days + 2
            elif Random_in == 4:
                $ Map.f4_potato = Time.days + 3
            elif Random_in == 2 or Random_in == 3:
                $ Map.f4_potato = Time.days + 1
            elif True:
                "Bug here, pls report to Caro!"

        jump forest_map_4_menu
screen f4_goods:
    vbox:
        xalign 0.8 ypos 0.8
        if Map.f4_carrot <= Time.days:
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/carrot_01n.png"
                        hover "map/forest_things/carrot_02n.png"

                        action Jump("f4_carrot")
                else:
                    imagebutton:
                        idle "map/forest_things/carrot_01n.png"
                        hover "map/forest_things/carrot_02n.png"

                        action None
            else:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/carrot_01n.png"
                        hover "map/forest_things/carrot_02n.png"

                        action Jump("f4_carrot")
                else:
                    imagebutton:
                        idle "map/forest_things/carrot_01n.png"
                        hover "map/forest_things/carrot_02n.png"

                        action None

        else:
            pass
    vbox:
        xalign 0.27 ypos 0.79
        if Map.f4_potato <= Time.days:
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/potato_01n.png"
                        hover "map/forest_things/potato_02n.png"

                        action Jump("f4_potato")
                else:
                    imagebutton:
                        idle "map/forest_things/potato_01n.png"
                        hover "map/forest_things/potato_02n.png"

                        action None
            else:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/potato_01n.png"
                        hover "map/forest_things/potato_02n.png"

                        action Jump("f4_potato")
                else:
                    imagebutton:
                        idle "map/forest_things/potato_01n.png"
                        hover "map/forest_things/potato_02n.png"

                        action None

        else:
            pass
label crossroad:
    window hide None
    $ Time.mins = Time.mins +20
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.hours >= 6 and Time.hours <= 17:
        scene crossroad 1 with slow_dissolve
    elif True:
        scene crossroad 1n with slow_dissolve
    if Map.crossroad == 1:
        stop music
        "You come upon a crossroad."
        "The fog around here is light enough that you can make out several branching paths."
        "But where the roads lead to is beyond your sight."
        $ Map.crossroad = 2
    menu:
        "Explore" if True:
            $ Random = renpy.random.randint(1, 3)
            if Random == 1:
                "You try to find a way in the fog."
                "But to your surprise,you end up back to the crossroad again."
                jump crossroad
            elif Random == 2:
                "You try to find a way in the fog."
                "But to your surprise,you end up back to the crossroad again."
                jump crossroad
            elif True:
                if Nauxus.meet == 1:
                    "You find a path leading into nothing but fog, you don't know what's inside."
                    "Do you want to go forward?"
                    menu:
                        "Yes" if True:
                            $ Nauxus.meet = 2
                            $ Map.swamp = 1
                            jump forest_map
                        "No" if True:
                            jump crossroad
                elif True:
                    "You try to find a way in the fog."
                    "But to your surprise,you end up back to the crossroad again."
                    jump crossroad
        "Leave" if True:

            jump forest_map
label swamp:
    window hide None
    $ renpy.music.set_pause(True, channel='Nauxus')
    $ renpy.music.set_volume(0, 4, channel = "Nauxus")
    $ Time.mins = Time.mins +20
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.hours >= 6 and Time.hours <= 17:
        scene swamp 1 with slow_dissolve
        play music "music/bird2.ogg"
    elif True:
        scene swamp 1n with slow_dissolve
        play music "music/bird1n.ogg"

    if Map.swamp == 1:
        stop music
        "In the direction Nauxus told you to find the lizard tribe."
        "There’s a thick musky scent in the air like wet grass drying under the warm sun."
        "The sounds of crickets singing and frogs croaking fills the air keeping you company."
        $ Map.swamp = 2

    menu:
        "Explore" if True:
            $ Random = renpy.random.randint(1, 3)
            if Random == 1:
                "You didn't find anything."
                jump swamp
            elif Random == 2:
                "You didn't find anything."
                jump swamp
            elif True:
                if Nauxus.meet == 2:
                    "You hear someone talking not too far away."
                    "Do you want to go forward?"
                    menu:
                        "Yes" if True:
                            $ renpy.music.set_pause(True, channel='Chan1')
                            $ renpy.music.set_pause(True, channel='Chan2')

                            $ renpy.music.set_pause(False, channel='Nauxus')
                            $ renpy.music.set_volume(1, 4, channel = "Nauxus")
                            jump Nauxus_meet
                        "No" if True:
                            jump swamp
                elif True:
                    "You didn't find anything."
                    jump swamp
        "Find Nauxus" if Nauxus.meet == 3 or Nauxus.meet == 4:
            $ renpy.music.set_pause(True, channel='Chan1')
            $ renpy.music.set_pause(True, channel='Chan2')

            $ renpy.music.set_pause(False, channel='Nauxus')
            $ renpy.music.set_volume(1, 4, channel = "Nauxus")
            jump Nauxus_meet
        "Find the catapult bull" if Quest.bomba == 3:
            jump Axel_bomb_done
        "Leave" if True:
            jump forest_map


label lake_bank:
    window hide None
    $ Time.mins = Time.mins +40
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.hours >= 6 and Time.hours <= 17:
        scene bank 1 with slow_dissolve
        play music "music/waterfall.wav"
    elif True:
        scene bank 1n with slow_dissolve
        play music "music/waterfall.wav"

    if Snow.fish == 2:
        "Snow leads the way to a nearby lake bank."
        "The lake itself is wide with a small island connected to the far right of the lake by a path."
        "Through the fog you can make out the sounds of rushing water coming from the left of the lake."
        "After setting the fishing equipment down you kneel by the waters and immerse your hands into it, only to quickly pull out from the freezing temperature."
        e 9 "Ah, so cold!"
        show snow happy1 at center with dissolve
        s "Quit screwing around there, help me set the bait for these fishing rods."
        e 6 "Coming!"
        hide snow happy1 with dissolve
        "Together you help Snow put the bait on while he holds the fishing rod in place."
        show snow stand at center with dissolve
        e 1 "So what are we fishing for exactly?"
        show snow happy1 at center with dissolve
        s "Morata fishes."
        e 1 "Morata fishes? Never heard of them before."
        show snow stand at center with dissolve
        s "Yeah, I named them myself since I discovered them when I was first here."
        s "Their meat is delicious, you can cook them in any way and it will work."
        s "That’s why I use them for my jerky."
        e 1 "Huh, ok. How hard is it to catch these things?"
        show snow happy1 at center with dissolve
        s "It depends, they’re pretty slow to take the bait."
        s "We’ll mostly be doing a lot of waiting, but one Morata fish should be large enough to prepare jerky for a week."
        s "So, if we both get one, we’ll be good."
        hide snow happy1 with dissolve
        "With your fishing rods ready you both cast your line into the lake."
        "And set the rods against some stones while you sat on the ground."
        "Waiting."
        show snow stand at center with dissolve
        show snow stand2 at center with dissolve
        "Snow walks over to the box and suddenly takes off his shirt."
        "He bends down and picks up the two bottles of beer."
        "You can’t help but stare as he walks over."
        hide snow stand2 at center with dissolve
        "His chiseled body makes your heart rush a bit. "
        "You shake your head and try to focus on the fishing."
        "Snow sits beside you and hands you a bottle, and takes one himself."
        s "To a good catch."
        e 7 "To a good catch."
        "You both toast your beers and chug down most of its contents."
        "Watching the lake feels oddly calming with only the sounds of insects buzzing and the rushing water in the distance."
        show snow stand2 at center with dissolve
        "You turn to Snow who’s drinking his beer with a content smile."
        "He notices you looking at him."
        show snow happy3 at center with dissolve
        s "Something on your mind, kid?"
        e 6 "No, I was just taking in the view."
        show snow stand2 at center with dissolve
        s "Huh, that so? "
        hide snow stand2 with dissolve
        "You both turn back towards the lake."
        show snow stand2 at center with dissolve
        s "You know what goes great with beer?"
        e 1 "Some nuts?"
        s "That, and a good story. I’ve got pages of anecdotes right here."
        "He points to his head and takes another swing of his beer."
        s "So ask away, and let this old wolf regale you with his tales."
        "Looks like the beer has Snow in a chatty mood."
        "What would you like to know?"
        jump Snow_lake_bank_chat
    label lake_bank_menu:
        if Time.mins >= 60:
            $ Time.mins = Time.mins -60
            $ Time.hours = Time.hours +1
        if Time.hours >= 24:
            $ Time.hours = Time.hours - 24
            $ Time.days = Time.days + 1
        if Time.hours >= 6 and Time.hours <= 17:
            scene bank 1
        elif True:
            scene bank 1n
        menu:
            "Explore" if True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You search around and find a hard rock."
                    "You get a rock."
                    $ jane_inv_M.take(rock)
                    $ Time.mins = Time.mins +30
                    jump lake_bank_menu
                elif Random == 2:
                    "You didn't find anything."
                    $ Time.mins = Time.mins +30
                    jump lake_bank_menu
                elif True:
                    "You didn't find anything."
                    $ Time.mins = Time.mins +30
                    jump lake_bank_menu
            "Fish" if jane_inv_K.qty(fishing_rod) != None:
                if jane_inv_M.qty(worm_bait) != None:
                    $ jane_inv_M.drop(worm_bait,1)
                    $ Fish_get = renpy.random.randint(1, 100)
                    $ Fish_get = renpy.random.randint(1, 100)
                    "You wave the fishing rod and start fishing."
                    scene black with vslow_dissolve
                    play sound "music/wave.ogg"
                    pause 3
                    "..."
                    stop sound
                    if Fish_get <= 5:
                        "You get a Morata fish!"
                        $ jane_inv_M.take(morata_fish,1)
                    elif Fish_get > 5 and Fish_get <= 35:
                        "You get a Grass carp!"
                        $ jane_inv_M.take(grass_carp,1)
                    elif Fish_get > 35 and Fish_get <= 70:
                        "Oh..It's not fish..."
                        "You get a Seaweed."
                        $ jane_inv_M.take(seaweed,1)
                    elif Fish_get > 70 and Fish_get <= 85:
                        "Oh..It's not fish..."
                        "You get a Rock."
                        $ jane_inv_M.take(rock,1)
                    elif True:
                        "Oh..It's not fish..."
                        "You get a Stick."
                        $ jane_inv_M.take(stick,1)
                    $ Time.mins = Time.mins +50
                    jump lake_bank
                elif True:
                    "You don't have bait."
                    jump lake_bank_menu
            "Leave" if True:
                jump forest_map

label bullforest:
    window hide None
    $ Time.mins = Time.mins +20
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    stop music
    if Thane.quest == 3:
        if Time.hours >= 6 and Time.hours <= 17:
            scene forest 5a with slow_dissolve
        elif True:
            scene forest 5an with slow_dissolve
        "You sniff the cloth, many different smells are mixed into the fabric,{p}but one stands out the most."
        "Its potency is unlike the other smells."
        "You sniff the air and attempt to filter out the maze of scents all around you."
        e 1 "There!"
        "The smell is faint but it’s unmistakable."
        "You follow your nose to where the smell is the strongest."
        "You run as fast as your feet can take you."
        if Time.hours >= 6 and Time.hours <= 17:
            scene forest 5 with slow_dissolve
        elif True:
            scene forest 5n with slow_dissolve
        "Darting past the trees and shrubs until you come upon a particular tree."
        "It looks no different from the others around you, but this is where the trail ends."
        "The top is masked by the heavy fog, but you sense someone is watching you."
        "Taking a deep breath you kick the tree as hard as you can."
        "The leaves rustle and you hear something heavy falling."
        "THUMP!"
        "A slender figure appears in front of you."
        show lizardw at center with dissolve
        "It’s a lizard man!"
        menu:
            "Talk." if Nauxus.meet == 3:
                "He holds his short blade ready to strike."
                e 1 "Wait. The nimble hen drinks ale under the moonlight."
                "Lizard spy" "What?"
                e 1 "The nimble hen drinks ale under the moonlight."
                "Lizard spy" "Who told you that phrase."
                e 1 "Chief Nauxus."
                e 1 "Now put the weapon down, we don’t need to fight."
                e 1 "I’m here to help bring you back."
                "Lizard spy" "Back? You mean the path has reopened?"
                e 13 "Yes! Your family is waiting for you."
                "The lizard sheaths his weapon back and lets out a heavy sigh of relief."
                "Lizard spy" "Ughh, you have no idea how much I’ve wanted to go back to them."
                "Lizard spy" "It’s been a hell hole here, thank you-"
                e 1 "[name]."
                "Lizard spy" "[name], right. I’ll never forget this."
                e 1 "Wait!"
                "Lizard spy" "What?"
                e 13 "Sorry, I got too excited and forgot to mention two things."
                e 1 "One, I found you thanks to this cloth one of the bull men gave me."
                e 1 "They know you’re here, and I’m tasked with bringing your heart back."
                "Lizard spy" "My heart… well I definitely can’t give you that."
                e 13 "I know, that’s why I need something else to prove I did the deed."
                e 1 "I can say we fought on a cliff and your body fell into who knows where."
                "Lizard spy" "Possible, then you’ll need this."
                hide lizardw with dissolve
                "The spy pulls out his dagger and stabs the weapon through his right palm."
                play sound "music/blood.ogg"
                "Lizard spy" "FUCK!"
                "He pulls the bloodied blade and tosses it in front of you."
                show lizardw at center with dissolve
                "Lizard spy" "Take it, I can recover from this wound easily."
                "You take the blade and store it in your bag."
                "Lizard spy" "What’s the other thing?"
                e 1 "The bull said the lizard men have been kidnapping their children."
                "Lizard spy" "Hah, that’s almost funny."
                "Lizard spy" "Don’t trust anything those bulls say."
                "Lizard spy" "They reek of lies and murder."
                "Lizard spy" "It’s no surprise they try to deceive you."
                "Lizard spy" "They’re the actual kidnappers and murderers."
                "Lizard spy" "Nauxus sent me out to find clues of our tribe’s missing children."
                "Lizard spy" "But those beasts guard their secrets well."
                "Lizard spy" "I’m not looking forward to reporting this back."
                "Lizard spy" "But in short [name], no, our tribe is innocent."
                e 1 "Ok, thank you for telling me."
                "Lizard spy" "I’ll see you back in the lizard village."
                hide lizardw with dissolve
                "The spy darts off into the woods, his footsteps silent as he runs."
                e 1 "I better head back to the bull village."
                $ jane_inv_K.take(Lizard_dagger)
                $ Nauxus.meet = 4
                $ Thane.quest = 4
                jump forest_map
            "Attack." if True:
                jump battle_lizad_spy

    if jane_inv_K.qty(sack) != None and Quest.fes == 2:
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
        if Time.hours >= 6 and Time.hours <= 17:
            scene forest 5a with slow_dissolve
        elif True:
            scene forest 5an with slow_dissolve

        "Following the trail of fruits, you find your prize guarded by a large four legged beast."
        "It has its back turned to you as it busily munches on the fruits it has gathered under a large tree."
        e 5 "Is it a... Katos?"
        "You rush forward with your blade ready to take it down with the element of surprise."
        "But just as your blade is about to meet its back, it swings around at a tremendous speed."
        "Its tail hits you in the chest and sends you flying back."
        "Katos growls angrily at you."
        show katos at center with dissolve
        "Drool and pieces of fruit dangle down from its razor sharp rows of teeth."
        "You lunge forward ready to finish the beast off."
        jump battle_katos

    if Time.hours >= 6 and Time.hours <= 17:
        scene forest 5 with slow_dissolve
    elif True:
        scene forest 5n with slow_dissolve

    label forest_map_5_menu:
        $ Map.good_battle = False
        show screen f5_goods
        menu:
            "Explore" if True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You didn't find anything."
                    jump bullforest
                elif True:
                    $ Random = renpy.random.randint(1, 5)
                    if Random == 1:
                        "You search around and find a sturdy stick."
                        "You get a stick."
                        $ jane_inv_M.take(stick)
                    elif Random == 2:
                        "You search around and find a hard rock."
                        "You get a rock."
                        $ jane_inv_M.take(rock)
                    elif True:
                        "You didn't find anything."
                    jump bullforest
            "Leave" if True:

                hide screen f5_goods
                jump forest_map
    label f5_mushroom:
        $ Random_in = renpy.random.randint(1, 4)
        "You collected some mushrooms."
        $ Random_in = renpy.random.randint(1, 4)

        $ mushroom_check = renpy.random.randint(1, 5)
        $ mushroom_check = renpy.random.randint(1, 5)
        if mushroom_check == 1:
            "You get 1 toadstool."
            $ jane_inv_M.take(toadstool,1)
        elif True:
            $ mushroom_get = renpy.random.randint(1, 2)
            $ mushroom_get = renpy.random.randint(1, 2)
            "You get [mushroom_get] shiitake."
            $ jane_inv_M.take(shiitake,mushroom_get)

        if Random_in == 1:
            $ Map.f5_mushroom = Time.days + 2
        elif Random_in == 4:
            $ Map.f5_mushroom = Time.days + 3
        elif Random_in == 2 or Random_in == 3:
            $ Map.f5_mushroom = Time.days + 1
        elif True:
            "Bug here, pls report to Caro!"

        jump forest_map_5_menu


    label f5_tomato:
        $ Random_in = renpy.random.randint(1, 4)
        "You collected some tomato."
        $ Random_in = renpy.random.randint(1, 4)

        $ tomato_check = renpy.random.randint(1, 2)

        "You get [tomato_check] tomato."
        $ jane_inv_M.take(tomato,tomato_check)

        if Random_in == 1:
            $ Map.f5_tomato = Time.days + 2
        elif Random_in == 4:
            $ Map.f5_tomato = Time.days + 3
        elif Random_in == 2 or Random_in == 3:
            $ Map.f5_tomato = Time.days + 1
        elif True:
            "Bug here, pls report to Caro!"

        jump forest_map_5_menu
screen f5_goods:
    vbox:
        xalign 0.96 ypos 0.8
        if Map.f5_mushroom <= Time.days:
            if Map.good_battle == False:
                imagebutton:
                    idle "map/forest_things/mushroom_01.png"
                    hover "map/forest_things/mushroom_02.png"

                    action Jump("f5_mushroom")
            else:
                imagebutton:
                    idle "map/forest_things/mushroom_01.png"
                    hover "map/forest_things/mushroom_02.png"

                    action None
        else:
            pass
    vbox:
        xalign 0.105 ypos 0.784
        if Map.f5_tomato <= Time.days:
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/tomato_01.png"
                        hover "map/forest_things/tomato_02.png"

                        action Jump("f5_tomato")
                else:
                    imagebutton:
                        idle "map/forest_things/tomato_01.png"
                        hover "map/forest_things/tomato_02.png"

                        action None
            else:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/tomato_01n.png"
                        hover "map/forest_things/tomato_02n.png"

                        action Jump("f5_tomato")
                else:
                    imagebutton:
                        idle "map/forest_things/tomato_01n.png"
                        hover "map/forest_things/tomato_02n.png"

                        action None

        else:
            pass

label deepswamp:
    window hide None
    $ Time.mins = Time.mins +40
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.hours >= 6 and Time.hours <= 17:
        scene swamp 2 with slow_dissolve
        if Roushk.fight == 1:
            jump Roushk_fight
    elif True:
        scene swamp 2n with slow_dissolve
    menu:
        "Explore" if True:
            if Time.hours >= 6 and Time.hours <= 17:
                "Lizard warrior" "Nauxus’s flunky, die!"
                jump battle_lizard
            elif True:
                "Nothing in the night for now"
                jump deepswamp
        "Leave" if True:


            jump forest_map

label cave_entrance:
    window hide None
    $ Time.mins = Time.mins +10
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.hours >= 6 and Time.hours <= 17:
        scene cavee 1 with slow_dissolve
        play music "music/waterfall.wav"
    elif True:
        scene cavee 1n with slow_dissolve
        play music "music/waterfall.wav"
    if Map.cave == 1:
        "You remember seeing this cave when you first headed to the bull tribe."
        "The shark’s smell is interrupted here."
        "From the outside, the cave looks like an ordinary cave."
        "But you sense something dark coming from the inside, like a cold bony hand reaching out from the shadows."
        "Gripping you by the heart and pulling you into the cave."
        "You gulp, against your better judgment you know you need to do this."
        "The moment you take a step forward and your foot is instantly submerged by the darkness."
        "It’s going to be dangerous to go in without some light."
        $ Map.cave = 2
        $ Map.Cavetorch = 1
    if Zalt.Dungeon_unlock == False:
        "You’ve found a dungeon."
        "Dungeons are long maps that contain monsters and treasure for you to find."
        "{b}You can't use 'Roll-back'system in the dungeon."
        "While travelling through a dungeon, a new EXP system is used on top of your regular EXP system."
        "{color=#19c22a}Adventure EXP(A-EXP), Adventure LV(A-LV) and Adventure Point(AP).{/color}"
        "As you explore the dungeon you gain {color=#19c22a}Adventure EXP{/color}, once you get 100 {color=#19c22a}Adventure EXP{/color} your {color=#19c22a}Adventure LV{/color} will increase by 1."
        "Each {color=#19c22a}Adventure LV{/color} increase will give you 1 {color=#19c22a}Adventure Point{/color} for short."
        "For every 3 AP you get, you can exchange them for 1 level up point."
        "As your {color=#19c22a}Adventure LV{/color} increases the more {color=#19c22a}Adventure EXP{/color} you can gather."
        "You’re free to leave the dungeon anytime, but watch out, the moment you leave the dungeon your {color=#19c22a}Adventure LV{/color} resets back to 0."
        "Losing to enemies in a dungeon will kick you out of the dungeon, and your {color=#19c22a}Adventure LV{/color} resets back to 0."
        "Along the way you will find campsites, these come in handy if you’ve travelled far into a dungeon and want to regain your HP and MP, but it will cost you sticks."
        "2 sticks restores all your MP and HP back to full."
        "You can get the sticks from the ghost foe for now."
        "So go out there and explore more dungeons!"
        "You get 3 sticks."
        $ jane_inv_M.take(stick,3)
        $ Zalt.Dungeon_unlock = True

    menu:
        "Enter(use torch)" if Map.Cavetorch != Time.days:
            if jane_inv_M.qty(torch) == None:
                e 1 "I need a torch before I go forward. "
                "You can’t make out what’s inside."
                "Looks like you need to come back with a torch."
                jump cave_entrance
            elif True:
                "Pulling out the torch you light it up and you’re ready to enter the cave."
                "You think this torch can burn for a day."
                $ jane_inv_M.drop(torch,1)
                $ Map.Cavetorch = Time.days
                jump Cave_map0
        "Enter" if Map.Cavetorch == Time.days:
            jump Cave_map0
        "Leave" if True:

            jump forest_map

        "Dungeon Explanation" if Zalt.Dungeon_unlock:
            "Dungeons are long maps that contain monsters and treasure for you to find."
            "{b}You can't use 'Roll-back'system in the dungeon."
            "While travelling through a dungeon, a new EXP system is used on top of your regular EXP system."
            "{color=#19c22a}Adventure EXP(A-EXP), Adventure LV(A-LV) and Adventure Point(AP).{/color}"
            "As you explore the dungeon you gain {color=#19c22a}Adventure EXP{/color}, once you get 100 {color=#19c22a}Adventure EXP{/color} your {color=#19c22a}Adventure LV{/color} will increase by 1."
            "Each {color=#19c22a}Adventure LV{/color} increase will give you 1 {color=#19c22a}Adventure Point{/color} for short."
            "For every 3 AP you get, you can exchange them for 1 level up point in your room."
            "As your {color=#19c22a}Adventure LV{/color} increases the more {color=#19c22a}Adventure EXP{/color} you can gather."
            "You’re free to leave the dungeon anytime, but watch out, the moment you leave the dungeon your {color=#19c22a}Adventure LV{/color} resets back to 0."
            "Losing to enemies in a dungeon will kick you out of the dungeon, and your {color=#19c22a}Adventure LV{/color} resets back to 0."
            "Along the way you will find campsites, these come in handy if you’ve travelled far into a dungeon and want to regain your HP and MP, but it will cost you sticks."
            "2 sticks restores all your MP and HP back to full."
            "You can get the sticks from the ghost foe for now."
            jump cave_entrance





label lakecabin:
    window hide None
    $ Map.good_battle = False
    $ Time.mins = Time.mins +20
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Map.lakecabin == 1:
        scene black with dissolve
        $ renpy.music.set_volume(0, 2, channel = "Chan2")
        $ renpy.music.set_volume(0, 2, channel = "Chan1")
        "There shouldn’t be anything wrong with just taking a look around."
        "The road leading you to the island is clean of bushes and trees."
        "However, as you approach the island dense trees encompass the road."
        "Nothing seems out of the ordinary as you walk along the path."
        "Not long after you see a small wooden hut up ahead."
        $ Map.lakecabin = 2
    if Ebb.kidnap == 3:
        hide screen f6_goods
        if Flo.meet == 1:
            $ Ebb.kidnap = 4
            jump Ebb_kidnap_end
        elif Flo.meet == -1:
            $ Ebb.kidnap = 4
            jump Ebb_kidnap_end
        elif True:
            pass
    if Time.hours >= 6 and Time.hours <= 17:
        scene lakecabin 1 with slow_dissolve
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
    elif True:
        scene lakecabin 1n with slow_dissolve
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
    label forest_map_6_menu:
        show screen f6_goods
        menu:
            "Enter the cabin" if True:
                if Ebb.meet == 0:
                    hide screen f6_goods
                    "You walk faster towards the hut when suddenly your foot knocks something hard on the ground."
                    e 1 "Hmm? What’s this?"
                    "As you try to pick up the object your hands freeze, it’s a broken half of a bear trap."
                    "You look around and see hints of traps that have been used lying about."
                    "Thin tripwire strings that have been severed lie along the path."
                    "There’s even a huge log embedded inside the trunk of another tree."
                    "Just to be safe you tread carefully towards the hut, but your confidence grows as there are no signs of active traps."
                    "Once you reach the front of the hut, you sniff the air, there’s a potent smell of fish and something fragrant, tea leaves?"
                    "You walk up to the door with trepidation."
                    "You knock."
                    pause 3
                    "And there’s no answer."
                    e 5 "Huh."
                    "Placing your hand on the door you push it gently and it swings open."
                if Ebb.tavern == 1:
                    hide screen f6_goods
                    jump Ebb_hang
                jump lakecabin_inside
            "Leave" if True:

                jump forest_map


    label f6_lemon:
        $ Random_in = renpy.random.randint(1, 4)
        "You collected some lemon."
        $ Random_in = renpy.random.randint(1, 4)

        $ lemon_check = renpy.random.randint(1, 2)

        "You get [lemon_check] lemon."
        $ jane_inv_M.take(lemon,lemon_check)

        if Random_in == 1:
            $ Map.f6_lemon = Time.days + 2
        elif Random_in == 4:
            $ Map.f6_lemon = Time.days + 3
        elif Random_in == 2 or Random_in == 3:
            $ Map.f6_lemon = Time.days + 1
        elif True:
            "Bug here, pls report to Caro!"

        jump forest_map_6_menu
    label f6_cabbage:
        $ Random_in = renpy.random.randint(1, 4)
        "You collected some cabbage."
        $ Random_in = renpy.random.randint(1, 4)
        "You get 1 cabbage."
        $ jane_inv_M.take(cabbage,1)
        if Random_in == 1:
            $ Map.f6_cabbage = Time.days + 2
        elif Random_in == 4:
            $ Map.f6_cabbage = Time.days + 3
        elif Random_in == 2 or Random_in == 3:
            $ Map.f6_cabbage = Time.days + 1
        elif True:
            "Bug here, pls report to Caro!"

        jump forest_map_6_menu
screen f6_goods:
    vbox:
        xalign 0.33 ypos 0.646
        if Map.f6_lemon <= Time.days:
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/lemon_01.png"
                        hover "map/forest_things/lemon_02.png"

                        action Jump("f6_lemon")
                else:
                    imagebutton:
                        idle "map/forest_things/lemon_01.png"
                        hover "map/forest_things/lemon_02.png"

                        action None
            else:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/lemon_01n.png"
                        hover "map/forest_things/lemon_02n.png"

                        action Jump("f6_lemon")
                else:
                    imagebutton:
                        idle "map/forest_things/lemon_01n.png"
                        hover "map/forest_things/lemon_02n.png"

                        action None

        else:
            pass
    vbox:
        xalign 0.24 ypos 0.673
        if Map.f6_cabbage <= Time.days:
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/cabbage_01.png"
                        hover "map/forest_things/cabbage_02.png"

                        action Jump("f6_cabbage")
                else:
                    imagebutton:
                        idle "map/forest_things/cabbage_01.png"
                        hover "map/forest_things/cabbage_02.png"

                        action None
            else:
                if Map.good_battle == False:
                    imagebutton:
                        idle "map/forest_things/cabbage_01n.png"
                        hover "map/forest_things/cabbage_02n.png"

                        action Jump("f6_cabbage")
                else:
                    imagebutton:
                        idle "map/forest_things/cabbage_01n.png"
                        hover "map/forest_things/cabbage_02n.png"

                        action None

        else:
            pass

label lakecabin_inside:
    hide screen f6_goods
    window hide None
    $ Time.mins = Time.mins +5
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.hours >= 6 and Time.hours <= 17:
        scene cabin 1 with slow_dissolve
    elif True:
        scene cabin 1n with slow_dissolve
    if Ebb.meet == 0:
        jump Ebb_meet
    menu:
        "Enter Ebb's room" if Ebb.room != 0:
            jump lakecabin_ebbroom
        "Enter Flo's room" if Flo.room != 0:
            "It's closed."
            jump lakecabin_inside
        "Leave" if True:
            jump lakecabin

label lakecabin_ebbroom:
    window hide None
    $ Time.mins = Time.mins +5
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.hours >= 6 and Time.hours <= 17:
        scene ebbroom 1 with slow_dissolve
    elif True:
        scene ebbroom 1n with slow_dissolve
    menu:
        "Talk to Ebb" if True:
            jump Ebb_talk0
        "Leave" if True:
            jump lakecabin_inside
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
