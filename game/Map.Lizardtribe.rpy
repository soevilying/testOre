label Lizard_tribe_map0:
    stop music
    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(1, 5, channel = "Chan1")
        $ renpy.music.set_pause(False, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(1, 5, channel = "Chan2")
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(False, channel='Chan2')
    play Chan1[ "<silence 0.5>", "music/lizard_village.ogg" ]fadein 3
    play Chan2[ "<silence 0.5>", "music/bird1n.ogg" ]fadein 3
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    play Nauxus "music/char_nauxus.ogg"
    $ renpy.music.set_pause(True, channel='Nauxus')


    jump Lizard_tribe_map



label Lizard_tribe_map:
    $ Time.mins = Time.mins +10
    window hide None
    pause 0.5
    $ renpy.music.set_pause(True, channel='Nauxus')
    $ renpy.music.set_pause(True, channel='Selye')

    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(1, 5, channel = "Chan1")
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_pause(False, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
        scene lizardtribe 1
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(1, 5, channel = "Chan2")
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(False, channel='Chan2')
        scene lizardtribe 1n

    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1

    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1


    stop music fadeout 1
    $ Zalt.public = True

    if Nauxus.meet == 5:
        if Time.hours >= 6 and Time.hours <= 17:
            scene lizardtribe 1 with vslow_dissolve
        elif True:
            scene lizardtribe 1n with vslow_dissolve
        "You both travel down the path laid with wooden planks through the dense trees."
        "At the end of the path you stand in place to take in the view."
        e 5 "Wow."
        "The lizard village is built on top of the swamp water with wooden pathways connecting the wooden huts on the ground."
        "The place feels comfortably warm despite the green foliage surrounding the village."
        n "Welcome to the lizard village."
        n "Over here is where you’ll be staying."
        "He points to the first wooden hut to your left."
        "Feel free to use it as your place of residence while you’re visiting."
        e 5 "Thanks, I think I’ll need a few hours of sleep before I do anything else."
        "Nauxus nods and opens the hut door."
        play sound "music/door.mp3"
        if Time.hours >= 6 and Time.hours <= 17:
            scene room 4 with vslow_dissolve
        elif True:
            scene room 4n with vslow_dissolve
        "Inside you see a spacious single bedroom. The bed provided looks and feels comfortable to the touch."
        "The furniture looks like it's carved using the swamp trees nearby."
        "Bottles filled with sun stones hang above the bed."
        "You hate to admit it but the hut is almost if not better than your room in the tavern."
        show nauxus stand at center with dissolve
        n "Meet me later when you’ve freshen up."
        n "Just ask around if you can’t find me."
        hide nauxus stand with dissolve
        "The chief smiles and leaves you to your own affairs."
        $ Nauxus.meet = 6
        $ Map.lizard = 1
        $ Time.lizard = Time.days

        jump Room4
    if Time.days >= Time.lizard +1 and Nauxus.meet == 6:
        if Thane.meet == -1 or Thane.quest == 7:
            if Time.hours >= 6 and Time.hours <= 17:
                $ Nauxus.meet = 7
                jump Nauxus_event_1
    if Thane.quest == 7 and Quest.campl == 1 and Selye.lizardask == 0 and Nauxus.meet >= 7 and Selye.meet != 0 and Quest.campb < 3:
        "Lizard guard" "Hey,[name]. Advisor Selye asked us to find you, he is waiting you in his hut."
        e 1 "...OK?"
        "Lizard guard" "He’s reachable via the suspending bridge from here to the hut right behind the platform."
        "Lizard guard" "Be sure you will hurry, He is not the kind of person who have patience."
        $ Selye.lizardask = 1
    elif True:
        pass
    if Quest.campb == 3 and Quest.campt == 1 and Selye.meet != 0 and Quest.campc == 0:
        if Time.hours >= 6 and Time.hours <= 17:
            jump Selye_camp_bull

    if Quest.camp_n == 2 and Time.nauxusart == 9999:
        $ Time.nauxusart = Time.days

    if Time.days >= Time.festival_day +2 and Quest.fes_end == 0 and Quest.fesn ==0 and Thane.movein != 1:
        if Quest.fes == 0:
            $ Quest.fes = 1
        $ Quest.fesn = 1
        "The lizard village is bustling with energy."
        "Many of its villagers are running along the wooden pathway, putting green leaves with bright yellow flowers bundled together on top of their doors."
        "The kids gather at the foot of the stairs to the ceremonial stage."
        "They appear to be practising singing a song."
        "You struggle getting through the crowd but manage to push through until you reach the shopkeeper."
        e 6 "Let me guess, festival preparations?"
        "Shopkeeper" "That’s right, everyone is pitching in to decorate the place and the kids are practising the festival song."
        "Shopkeeper" "It brings my old heart joy seeing so many happy faces. "
        "Shopkeeper" "But you shouldn’t be here young man, Chief Nauxus is looking for you."
        e 1 "For me? Whatever for?"
        "Shopkeeper" "He can tell you more. The guards were asking around for you."
        "Shopkeeper" "Now go to him, you won’t want to keep him waiting."

    if Quest.fes == 3 and Quest.fesn < 7:
        jump Lizard_defend
    call screen Lizard_outdoor with dissolve
    window show None
    show screen days
    stop music fadeout 1
    if _return == 'exit':
        jump forest_map0
        return
    if _return == 'lizard_room':
        play sound "music/door.mp3"
        jump Room4
    if _return == 'Lizard_prison':
        "You hear the screams of bulls coming from the prison."
        e 1 "..."
        jump Lizard_tribe_map
    if _return == 'Nauxus_room':
        if Nauxus.meet < 7:
            if Time.hours >= 6 and Time.hours <= 17:
                "The lizard next to the doorway coughs and shakes his head."
                "You decide to leave."
            elif True:
                e 1 "This must be the way to Nauxus's room."
                e 6 "Guess even Nauxus needs some rest first."
                e 6 "I'll see him later."
            jump Lizard_tribe_map
        elif True:
            jump Lizard_tribe_tree
        return
    if _return == 'lizard_shop':
        if Quest.fesn == 3:
            $ Quest.fesn = 4
            "You stop by in front of the lizard shopkeeper’s shop."
            e 1 "Hello shopkeeper. Nauxus put me in charge of the missing fruits investigation."
            e 1 "Would you be so kind to show me where the fruits were stored?"
            "Shopkeeper" "Dearie I would be happy to help. "
            "Shopkeeper" "Before you go though, you might need these."
            "She pulls out two burlap sacks from her counter and hands them to you."
            e 1 "Thanks, I was wondering how’d I pick up all those fruits."
            "Shopkeeper" "All the best dearie. Once you get all the fruits you can drop them off here."
            "Shopkeeper" "I’ll have them cleaned and ready for the feast."
            e 1 "Got it and where’s the hut by the way?"
            "Shopkeeper" "It’s easy to find. Here are the directions."
            "With the shopkeeper's directions you manage to find the storage hut."
            scene black with dissolve
            "The storage hut looks fine from the front, but a quick walk to the side you spot the massive hole the creature made."
            "Inside the hut are only the eaten remains of the fruits that used to reside there."
            "The creature left a trail of half eaten and squashed fruits."
            "You follow the trail leading out of the lizard’s village."
            $ jane_inv_K.take(sack,2)
            jump forest_map0
        "Old female lizard" "Oh, kid. You want to buy something?"
        "Old female lizard" "Come back later."
        "Old female lizard" "Give this old woman some times to organize the goods first."
        jump Lizard_tribe_map
        return
    if _return == 'Chibi_lizardm1':
        if Quest.campb == 6 or Quest.campt == 6 or Quest.campl ==6:
            $ Random = renpy.random.randint(1, 2)
            if Random <= 1:
                "Lizard Guard" "We’re not safe until the kidnapper is brought to justice."
                "Lizard Guard" "Even then what’s stopping another one from coming out?"
            elif True:
                "Lizard Guard" "Gahh, everyone got to go to the welcoming party but me."
                "Lizard Guard" "Had to guard these damn prisoners."
        elif True:

            "Lizard guard" "No entrance for anyone without the chief's permission."
            e 1 "What's this place?"
            "Lizard guard" "This is our prison."
            "You hear the screams of bulls coming from the prison."
            e 1 "..."
        jump Lizard_tribe_map
        return
    if _return == 'Chibi_lizardm2':
        "Lizard guard" "Oh,hello,[name]."
        e 1 "You know my name?"
        "Lizard guard" "Yeah, the chief told us."
        "Lizard guard" "If you're here to meet the chief."
        "Lizard guard" "Then you’ll have to wait, he hasn’t returned here yet."
        e 1 "Fine."
        jump Lizard_tribe_map
        return
    if _return == 'Chibi_lizardm3':
        if Quest.campb == 6 or Quest.campt == 6 or Quest.campl ==6:
            "Male lizard" "The war’s started, it won’t end without bloodshed."
        elif True:
            "Male lizard" "I should go out hunting soon."
        jump Lizard_tribe_map
        return
    if _return == 'Chibi_lizardkid':
        if Foe.spydie == 0:
            "You look up and see a small head popping out of the window."
            "When she saw you, she seems very happy and waves to you."
            "You know her,she is that spy's daughter."
            "When her mother and Nauxus quarreled, she was next to her."
            "You smile and wave back."
        elif True:
            "You look up and see a small head popping out of the window."
            "She looks around and seems to be waiting for someone to come back."
        jump Lizard_tribe_map
        return
    return
screen Lizard_outdoor:
    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'lizardtribe ground'
            hover 'lizardtribe hover'
        else:
            idle 'lizardtribe groundn'
            hover 'lizardtribe hovern'

        hotspot (196, 482, 214, 365) action Return("lizard_room")

        hotspot (1682, 651, 50, 77) action Return("Lizard_prison")

        hotspot (849, 580, 59, 98) action Return("Nauxus_room")

        hotspot (442, 919, 302, 149) action Return("exit")
        vbox:
            xalign 0.702 ypos 0.6
            if Time.hours >= 6 and Time.hours <= 17:
                imagebutton:
                    idle "NPC/lizardf1 01.png"
                    hover "NPC/lizardf1 02.png"

                    action Return("lizard_shop")
            else:
                pass

        vbox:
            xalign 0.8 ypos 0.58
            if Time.hours >= 6 and Time.hours <= 17:
                imagebutton:
                    idle "NPC/lizardm1 01.png"
                    hover "NPC/lizardm1 02.png"

                    action Return("Chibi_lizardm1")
            else:
                pass

        vbox:
            xalign 0.45 ypos 0.56
            if Time.hours >= 6 and Time.hours <= 17 and Nauxus.meet < 7:
                imagebutton:
                    idle "NPC/lizardm2 01.png"
                    hover "NPC/lizardm2 02.png"

                    action Return("Chibi_lizardm2")
            else:
                pass
        vbox:
            xalign 0.38 ypos 0.63
            if Time.hours >= 6 and Time.hours <= 17:
                imagebutton:
                    idle "NPC/lizardm3 01.png"
                    hover "NPC/lizardm3 02.png"

                    action Return("Chibi_lizardm3")
            else:
                pass
        vbox:
            xalign 0.69 ypos 0.19
            if Time.hours >= 6 and Time.hours <= 17:
                if Quest.campb == 6 or Quest.campt == 6 or Quest.campl ==6:
                    pass
                else:
                    imagebutton:
                        idle "NPC/lizardkid 01.png"
                        hover "NPC/lizardkid 02.png"

                        action Return("Chibi_lizardkid")

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


label Lizard_tribe_tree0:
    stop music
    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0.7, 5, channel = "Chan1")
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(0.7, 5, channel = "Chan2")
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    play Nauxus "music/char_nauxus.ogg"
    $ renpy.music.set_pause(True, channel='Nauxus')

    jump Lizard_tribe_tree


label Lizard_tribe_tree:
    $ Time.mins = Time.mins +10
    window hide None
    pause 0.5
    $ renpy.music.set_pause(True, channel='Nauxus')
    $ renpy.music.set_pause(True, channel='Selye')

    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(1, 5, channel = "Chan1")
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_pause(False, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
        if Quest.bomb_result == Axel:
            scene lizardtree 2
        elif True:
            scene lizardtree 1
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(1, 5, channel = "Chan2")
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(False, channel='Chan2')
        if Quest.bomb_result == Axel:
            scene lizardtree 2n
        elif True:
            scene lizardtree 1n

    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1

    stop music fadeout 1
    $ Zalt.public = True
    if Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bomb_lizard ==2 and Quest.bomb_result == Axel:
        jump Nauxus_letter
    call screen Lizard_tree with dissolve
    window show None
    show screen days
    stop music fadeout 1
    if _return == 'exit':
        jump Lizard_tribe_map
        return
    if _return == 'naga_room':
        if Thane.meet == -1:
            play sound "music/door.mp3"
            jump Lizard_tribe_nagahut
        elif True:
            if Thane.quest == 7 and Quest.campb < 3 and Quest.campl <5 and Quest.campt <6:
                play sound "music/door.mp3"
                jump Lizard_tribe_nagahut
            elif Quest.bomb_end != 0:
                if Quest.bombt == 2 or Quest.bombt == 3:
                    e 1 "No, now isn’t the time to see Selye. I need to get the fake bomb to the bull at the swamp."
                    jump Lizard_tribe_tree
                elif Quest.bomba == 1 and Quest.bombn == 2:
                    e 13 "I think I should go to see what Axel want."
                    jump Lizard_tribe_tree
                elif True:
                    if Quest.bomb == 2 and (Quest.bombt == 1 or Quest.bombt != 1):
                        "{b}{color=#ffd65c}<Warning:{p} You can't change your option anymore after this option.>{/color}"
                        "{b}{color=#ffd65c}<Are you sure you want to enter?>{/color}"
                        menu:
                            "Yes" if True:
                                play sound "music/door.mp3"
                                jump Lizard_tribe_nagahut
                            "No" if True:
                                jump Lizard_tribe_tree
                    elif Quest.bombt == 4 or Quest.bombt == 5:
                        play sound "music/door.mp3"
                        jump Lizard_tribe_nagahut
                    elif True:
                        "The door is locked, it seems Selye is not here now."
                        "Or,it's just because he doesn't want to see you."
                        jump Lizard_tribe_tree
            elif Quest.bomb_result == Nauxus and Selye.past == 0:
                play sound "music/door.mp3"
                jump Lizard_tribe_nagahut
            elif True:
                "The door is locked, it seems Selye is not here now."
                "Or,it's just because he doesn't want to see you."
                jump Lizard_tribe_tree
    if _return == 'Lizard_prison':
        "You hear the screams of bulls coming from the prison."
        e 1 "..."
        jump Lizard_tribe_map
    if _return == 'meeting_room':
        if Quest.fesn == 7:
            "You shouldn't bother Nauxus."
            jump Lizard_tribe_tree

        if Quest.bomba == 3 and Quest.bomb == 3 and Quest.bomb_end != 0:
            e 13 "I should send the bomb to the swamp bull."
            jump Lizard_tribe_tree
        elif Quest.bombt == 4 and Quest.bomba == 4 and Quest.bomb_end != 0 and Quest.bombn < 3:
            e 1 "I should go to meet Selye first."
            jump Lizard_tribe_tree
        elif True:

            if Quest.campb == 6 or Quest.campl == 6 or Quest.campt == 6:
                if Roushk.barn == 1:
                    e 1 "It seems Nauxus really isn't here."
                    e 1 "That's strange. I wonder where could he have gone?"
                    jump Lizard_tribe_tree
                if Time.hours >= 6 and Time.hours <= 17:
                    jump Lizard_tribe_meetingroom
                elif True:
                    e 6 "Guess even Nauxus needs some rest first."
                    e 6 "I'll see him later."
                    "You decide to leave."
                    jump Lizard_tribe_tree
            elif True:
                e 1 "Nauxus is quite busy there."
                e 1 "I should finish my quest first before meet him."
                jump Lizard_tribe_tree
            return

    if _return == 'Torch Lizard':
        "Night Guard" "Move along civilian, nothing to see here."
        e 1 "Why are you here?"
        "Night Guard" "Gots to watch the hole there."
        "Night Guard" "Can’t let people fall in at night. "
        e 13 "Sounds like a tough job."
        "Night Guard" "Yup, but someone’s gotta do it. Now move boy."
        "Night Guard" "Don’t let me catch you messing around here."
        jump Lizard_tribe_tree
screen Lizard_tree:
    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            if Quest.bomb_result == Axel:
                idle 'lizardtree ground1'
                hover 'lizardtree hover1'
            else:
                idle 'lizardtree ground'
                hover 'lizardtree hover'

        else:
            if Quest.bomb_result == Axel:
                idle 'lizardtree ground1n'
                hover 'lizardtree hover1n'
                hotspot (1155, 637, 128, 152) action Return("Torch Lizard")
            else:
                idle 'lizardtree groundn'
                hover 'lizardtree hovern'


        hotspot (74, 146, 325, 575) action Return("meeting_room")
        hotspot (1632, 422, 95, 137) action Return("naga_room")

    frame:
        xalign 0.81 ypos 0.84
        imagebutton:
            idle "UI/outdoor03.png"
            hover "UI/outdoor04.png"

            action Return("exit")

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

label Lizard_tribe_meetingroom:

    $ renpy.music.set_pause(True, channel='Nauxus')
    $ renpy.music.set_pause(True, channel='Selye')
    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_pause(False, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0.8, 5, channel = "Chan1")
    elif True:
        $ renpy.music.set_pause(False, channel='Chan2')
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(0.8, 5, channel = "Chan2")
    $ Time.mins = Time.mins +10
    window hide None
    stop music fadeout 1
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    scene meetingroom with slow_dissolve
    if Roushk.nauxus == 1:
        $ Roushk.nauxus = 2
        jump Nauxus_roushk
    if Quest.camp_n == 1:
        jump Nauxus_camp_end
    if Time.hours >= 6 and Time.hours <= 17:
        pass
    elif True:
        e 1 "Here's not open at night. I'd better go."
        jump Lizard_tribe_tree
    if Quest.camp_n == 2 and Time.days >= Time.nauxusart+1 and Nauxus.artwork == 0 and Time.hours >= 6 and Time.hours <= 17:
        $ Nauxus.artwork = 1
        jump Nauxus_artwork
    if Quest.fesn ==1 and Quest.fes_end != 1:
        jump Nauxus_festival
    call screen Lizard_tribe_meetingroom with dissolve
    window show None
    show screen days
    stop music fadeout 1
    if _return == 'exit':
        jump Lizard_tribe_tree
        return
    if _return == 'Nauxus':
        jump Nauxus_tribe_talk
        return
screen Lizard_tribe_meetingroom:
    imagemap:
        idle 'meetingroom ground'
        hover 'meetingroom hover'



        vbox:
            xalign 0.46 ypos 0.474
            if Quest.camp_n == 2 and Time.anauxus != Time.days:
                imagebutton:
                    idle "NPC/nauxus01.png"
                    hover "NPC/nauxus02.png"

                    action Return("Nauxus")
            else:
                pass


    frame:
        xalign 0.81 ypos 0.84
        imagebutton:
            idle "UI/outdoor01.png"
            hover "UI/outdoor02.png"
            action Return("exit")
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

label Lizard_tribe_nagahut:
    $ Time.mins = Time.mins +10
    window hide None
    stop music fadeout 1
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    scene treehut 2 with slow_dissolve
    if Quest.bomb_result == Nauxus and Selye.past == 0:
        jump Selye_past
    if Quest.bombn == 2 or Quest.bombn == 3:
        jump Selye_letter
    if Selye.meet == 1:
        jump Selye_meet

label Room4:
    if Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bombt == 6 and Quest.fes_end == -1:
        $ Quest.fes_end = 0
        $ Time.festival_day = Time.days
    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0.3, 2, channel = "Chan1")
        $ renpy.music.set_pause(False, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(0.4, 2, channel = "Chan2")
        $ renpy.music.set_pause(False, channel='Chan2')
        $ renpy.music.set_pause(True, channel='Chan1')

    $ renpy.music.set_pause(True, channel='Nauxus')

    stop music

    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    $ Zalt.public = False
    if Time.hours >= 6 and Time.hours <= 17:
        scene room 4 with dissolve
    elif True:
        scene room 4n with dissolve

    if Map.yourroom == 0:
        "This is your room."
        "Whenever you rest in your bed you can spend the experience points you gain to level up."
        "As you level up you gain lvl-points which you can spend to raise HP/MP or ability levels."
        "Spend them wisely, and good night."
        $ Map.yourroom = 1
    call screen Room4
    window hide None
    window show None
    if _return == 'stat-points':
        "You can use {color=#19c22a}5 {/color} lv-points to increase one stat point you want."
        "Or you can also use {color=#19c22a}3 {/color} lv-points to increase 10 HP and 10 MP."
        "You have {color=#19c22a}[Zalt.points]{/color} lv-point now."
        menu:
            "Get 10 MaxHP+10 MaxMP" if Zalt.points >= 3:
                $ Zalt.points = Zalt.points -3
                $ Zalt.maxhp = Zalt.maxhp +10
                $ Zalt.maxmp = Zalt.maxmp +10
                jump Room4
            "Get stat point" if Zalt.points >= 5:
                menu:
                    "Strength" if Zalt.str <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.str = Zalt.str +1
                        $ Zalt.ATK = Zalt.ATK +3
                        "Your {color=#19c22a}STR{/color} now increase to {b}{color=#19c22a}[Zalt.str]{/color}."
                        jump Room4
                    "Agile" if Zalt.agi <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.agi = Zalt.agi +1
                        $ Zalt.ATK = Zalt.ATK +1
                        $ Zalt.CRIT = Zalt.CRIT +2
                        $ Battle.dodge = Battle.dodge +2
                        "Your {color=#19c22a}Agi{/color} now increase to {b}{color=#19c22a}[Zalt.agi]{/color}."
                        jump Room4
                    "Intelligence" if Zalt.int <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.int = Zalt.int +1
                        $ Zalt.maxmp = Zalt.maxmp +10
                        $ Zalt.MATK = Zalt.MATK + 3
                        "Your {color=#19c22a}INT{/color} now increase to {b}{color=#19c22a}[Zalt.int]{/color}."
                        "Your {color=#19c22a}MaxMp{/color} now increase to {b}{color=#19c22a}[Zalt.maxmp]{/color}."
                        jump Room4
                    "Endurance" if Zalt.end <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.end = Zalt.end +1
                        $ Zalt.maxhp = Zalt.maxhp +20
                        "Your {color=#19c22a}END{/color} now increase to {b}{color=#19c22a}[Zalt.end]{/color}."
                        "Your {color=#19c22a}MaxHp{/color} now increase to {b}{color=#19c22a}[Zalt.maxhp]{/color}."
                        jump Room4
                    "Charm" if Zalt.cha <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.cha = Zalt.cha +1
                        "Your {color=#19c22a}CHA{/color} now increase to {b}{color=#19c22a}[Zalt.cha]{/color}."
                        jump Room4
                    "Leave" if True:
                        jump Room4
            "Exchange 3 AP to 1 lv-point" if Zalt.AP >= 3:
                "{b}{color=#19c22a}You get 1 lv-point.{/color}."
                $ Zalt.AP = Zalt.AP -3
                $ Zalt.points = Zalt.points +1
                jump Room4
            "Leave" if True:
                jump Room4

    if _return == 'outroom':
        if Items.nude == False:
            jump Lizard_tribe_map
        elif True:
            scene black
            e 7 "....No,I don't think it's a good idea to being nude in public."
            jump Room4
    if _return == 'Rest':
        menu:
            "Rest" if Time.hours >= 6 and Time.hours <= 21:
                scene black
                "You sleep for 3 hours, feel refreshed and full of energy."
                "HP and MP have been restored half of the maximum."
                $ Zalt.hp = min(Zalt.hp+Zalt.maxhp/2, Zalt.maxhp)
                $ Zalt.mp = min(Zalt.mp+Zalt.maxmp/2, Zalt.maxmp)
                $ Time.hours = Time.hours+3
                jump Room4

            "Rest until evening" if Time.hours >= 6 and Time.hours <15:
                scene black
                "You sleep until evening, feel refreshed and full of energy."
                "HP and MP have been restored to maximum."
                $ Zalt.hp = Zalt.maxhp
                $ Zalt.mp = Zalt.maxmp

                $ Time.hours = 18
                $ Time.mins = 0

                jump Room4
            "Sleep" if Time.hours < 6 or Time.hours >=21:
                scene black
                "You sleep until morning, feel refreshed and full of energy."
                "HP and MP have been restored to maximum."
                $ Zalt.hp = Zalt.maxhp
                $ Zalt.mp = Zalt.maxmp
                if Time.hours >=21:
                    $ Time.days = Time.days+1
                    $ Time.hours = 6
                    $ Time.mins = 30
                elif True:
                    $ Time.hours = 6
                    $ Time.mins = 30

                jump Room4
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

                jump Room4
            "Leave" if True:
                jump Room4

    if _return == 'eyvind_solo':
        if Time.hours >= 6 and Time.hours <= 17:
            scene room 4 with dissolve
        elif True:
            scene room 4n with dissolve
        if persistent.CG_eyvind_solo:
            "Do you want to skip the scene?"
            menu:
                "Yes" if True:
                    "Slowly, you drift off to sleep."
                    $ Zalt.lust = 0
                    $ Time.mins = Time.mins+15
                    jump Room4
                "No" if True:
                    pass
        "A strong wave of heat washes over your body."
        "You place a hand over your chest and you feel your heart beating like a storm."
        e 11 "Ugh, I can’t... I can’t hold it in anymore."
        "From just placing your hand over your chest,{p}you start to massage your pecs."
        "You shudder and gasp from the touch.{p}Your loins feel heavy and tighten against your loincloth."
        "You tear away your loincloth exposing your throbbing dick.{p}With your cock in your hand you fall onto your bed."
        "You pant loudly while your hand rubs along your hot shaft."
        "This isn’t the first time you’ve jerked off, but you’ve never felt so horny in so long."
        "Your balls... your balls feels so full."
        "You grab the orbs dangling between your thighs and give them a good squeeze."
        e 11 "Hngh..."
        "Your thumb caresses the tip of your cock, smearing it with hot translucent pre. Perfect for lube."
        "You smear the pre along your cock while steadily jerking your cock."
        "A soft gasp escape your mouth."
        "Your whole body tenses as your dick pulsates from every rub."
        "Your right leg shakes and twitches a bit."
        "Gritting your teeth you pump your cock even faster."
        "You feel the pressure building inside your dick."
        e 4 "Fuck!"
        "Beads of sweat form around your forehead and your body is mind numbingly warm."
        "You pant louder and louder until..."
        "Your cock fires a hot wad of cum right onto your face."
        "Your cumshots splatter around your pecs and stomach."
        "When you finally stop cumming your body sinks into the bed."
        "The afterglow blankets you filling you with sweet warmth."
        "Slowly, you drift off to sleep."
        $ persistent.CG_eyvind_solo = True
        $ Zalt.lust = 0
        $ Time.mins = Time.mins+15
        jump Room4
screen Room4:

    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'room 4'
            hover 'room 4'
        else:
            idle 'room 4n'
            hover 'room 4n'



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
    frame:
        xalign 0.89 ypos 0.72
        imagebutton:
            idle "UI/sleep01.png"
            hover "UI/sleep02.png"

            action Return("Rest")
    frame:
        xalign 0.81 ypos 0.84
        imagebutton:
            idle "UI/outdoor01.png"
            hover "UI/outdoor02.png"

            action Return("outroom")
    if Zalt.lust >= 40:
        frame:
            xalign 0.97 ypos 0.60
            imagebutton:
                idle "UI/love01.png"
                hover "UI/love02.png"

                action Return("eyvind_solo")
    if Zalt.points >= 1 or Zalt.AP != 0:
        frame:
            xalign 0.97 ypos 0.72
            imagebutton:
                idle "UI/lv01.png"
                hover "UI/lv02.png"

                action Return("stat-points")

    else:
        pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
