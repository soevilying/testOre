label T_barn:
    hide item_lack1
    hide item_lack2
    hide item_yes1
    hide item_yes2
    $ Time.mins = Time.mins +5
    window hide None

    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    scene barn 1 with dissolve
    call screen barn with dissolve
    window show None
    show screen days
    if _return == 'exit':
        play sound "music/foot1.ogg"
        jump T_outdoor
        return
    if _return == 'door':
        e 1 "This is the back door of the barn.It's locked."
        e 6 "Well,if I want to know what's inside."
        e 6 "I just can get out of the barn and go around to the back."
        e 1 "There's no need to open the door."
        jump T_barn
    if _return == 'utility room':
        e 1 "A utility room, it smells of grain inside."
        jump T_barn
        return
    if _return == 'Roushk_talk':
        jump Roushk_talk
        return
    if _return == 'Anvil_meet':
        jump Anvil_meet
        return

    return
screen barn:
    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'barn ground'
            hover 'barn hover'
        else:
            idle 'barn ground'
            hover 'barn hover'





















        vbox:
            xalign 0.772 ypos 0.30
            if Roushk.barn == 1:
                imagebutton:
                    idle "NPC/roushk01.png"
                    hover "NPC/roushk02.png"

                    action Return("Roushk_talk")
            else:
                pass




        hotspot (1159, 454, 121, 251) action Return("utility room")

        hotspot (927, 386, 105, 209) action Return("door")

        hotspot (633, 960, 580, 113) action Return("exit")
        vbox:
            xalign 0.16 ypos 0.71
            imagebutton:
                idle "NPC/anvil01.png"
                hover "NPC/anvil02.png"

                action Return("Anvil_meet")

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




label Anvil_meet:
    if NPC.anvil == 0:
        "There’s an anvil here in the barn. "
        e 1 "I should ask Snow for his permission to use this first."
        $ NPC.anvil = 1
    elif NPC.anvil == 1:
        e 1 "I should ask Snow for his permission to use this first."
    elif True:
        jump Anvil_update
    jump T_barn
label Anvil_update:
    show black4 with dissolve
    if Items.weapon >= 4:
        "The weapon has been upgraded to the maximum level of the current version."
        menu:
            "Leave" if True:
                jump T_barn

    if jane_inv_E.qty(sword) == None:
        e 1 "I need to unequip the weapon first."
        jump T_barn
    elif True:

        label Anvil_update_dadsword:

            show empty_bag:
                xpos 0.42 ypos 0.5
                zoom 1

            show empty_bag1:
                xpos 0.52 ypos 0.5
                zoom 1
            if Items.weapon == 0:
                if jane_inv_M.qty(rock) != None:
                    $ NPC.anvil_need1_0 = jane_inv_M.qty(rock)
                elif True:
                    $ NPC.anvil_need1_0 = 0

                if jane_inv_M.qty(slime_jewel) != None:
                    $ NPC.anvil_need2_0 = jane_inv_M.qty(slime_jewel)
                elif True:
                    $ NPC.anvil_need2_0 = 0

                $ NPC.anvil_need1_1 = 3
                $ NPC.anvil_need2_1 = 5
                $ NPC.anvil_name1 = "Rock"
                $ NPC.anvil_name2 = "Slime Jewel"
                show stone:
                    xpos 0.42 ypos 0.5
                    zoom 1
                show slimejewel:
                    xpos 0.52 ypos 0.5
                    zoom 1
            elif Items.weapon == 1:
                if jane_inv_M.qty(rock) != None:
                    $ NPC.anvil_need1_0 = jane_inv_M.qty(rock)
                elif True:
                    $ NPC.anvil_need1_0 = 0

                if jane_inv_M.qty(ectoplasm) != None:
                    $ NPC.anvil_need2_0 = jane_inv_M.qty(ectoplasm)
                elif True:
                    $ NPC.anvil_need2_0 = 0

                $ NPC.anvil_need1_1 = 5
                $ NPC.anvil_need2_1 = 4
                $ NPC.anvil_name1 = "Rock"
                $ NPC.anvil_name2 = "Ectoplasm"
                show stone:
                    xpos 0.42 ypos 0.5
                    zoom 1
                show ectoplasm:
                    xpos 0.52 ypos 0.5
                    zoom 1
            elif Items.weapon == 2:
                if jane_inv_M.qty(iron_ore) != None:
                    $ NPC.anvil_need1_0 = jane_inv_M.qty(iron_ore)
                elif True:
                    $ NPC.anvil_need1_0 = 0

                if jane_inv_M.qty(lizard_scale) != None:
                    $ NPC.anvil_need2_0 = jane_inv_M.qty(lizard_scale)
                elif True:
                    $ NPC.anvil_need2_0 = 0

                $ NPC.anvil_need1_1 = 4
                $ NPC.anvil_need2_1 = 5
                $ NPC.anvil_name1 = "Iron Ore"
                $ NPC.anvil_name2 = "Lizard Scale"
                show ironore:
                    xpos 0.42 ypos 0.5
                    zoom 1
                show lizardscale:
                    xpos 0.52 ypos 0.5
                    zoom 1
            elif Items.weapon == 3:
                if jane_inv_M.qty(iron_ore) != None:
                    $ NPC.anvil_need1_0 = jane_inv_M.qty(iron_ore)
                elif True:
                    $ NPC.anvil_need1_0 = 0

                if jane_inv_M.qty(blood_crystals) != None:
                    $ NPC.anvil_need2_0 = jane_inv_M.qty(blood_crystals)
                elif True:
                    $ NPC.anvil_need2_0 = 0

                $ NPC.anvil_need1_1 = 8
                $ NPC.anvil_need2_1 = 2
                $ NPC.anvil_name1 = "Iron Ore"
                $ NPC.anvil_name2 = "Blood Crystals"
                show ironore:
                    xpos 0.42 ypos 0.5
                    zoom 1
                show blood_crystals:
                    xpos 0.52 ypos 0.5
                    zoom 1

            show screen anvil_need
            show screen anvil_need_name


            if NPC.anvil_need1_0 < NPC.anvil_need1_1:
                show item_lack1:
                    xpos 0.42 ypos 0.5
                    zoom 1
                $ NPC.anvil_1 = 0
            elif True:
                show item_yes1:
                    xpos 0.42 ypos 0.5
                    zoom 1
                $ NPC.anvil_1 = 1
            if NPC.anvil_need2_0 < NPC.anvil_need2_1:
                show item_lack2:
                    xpos 0.52 ypos 0.5
                    zoom 1
                $ NPC.anvil_2 = 0
            elif True:
                show item_yes2:
                    xpos 0.52 ypos 0.5
                    zoom 1
                $ NPC.anvil_2 = 1




            screen anvil_need_name:
                vbox:
                    xalign 0.45
                    yalign 0.64
                    text "{size=-8}[NPC.anvil_name1]{/size}"
                vbox:
                    xalign 0.553
                    yalign 0.64
                    text "{size=-8}[NPC.anvil_name2]{/size}"
            screen anvil_need:

                vbox:
                    xalign 0.45
                    yalign 0.68
                    text "{size=-5}[NPC.anvil_need1_0]/[NPC.anvil_need1_1]{/size}"
                vbox:
                    xalign 0.553
                    yalign 0.68
                    text "{size=-5}[NPC.anvil_need2_0]/[NPC.anvil_need2_1]{/size}"
            menu:
                "Upgrade" if True:
                    if NPC.anvil_1 == 1 and NPC.anvil_2 == 1:
                        hide screen anvil_need
                        hide screen anvil_need_name

                        scene black with slow_dissolve
                        play sound "music/anvil.ogg"
                        pause 5
                        play sound "music/item-collect.ogg"
                        pause 1
                        scene barn 1 with dissolve
                        "{b}{color=#19c22a}Weapon Upgrade Success."
                        if Items.weapon == 0:
                            $ Items.weapon = 1
                            $ sword.change("Sword +1", "My sword, my father made it for me. \nATK +13", "images/items/sword.png", 0,False, 2,Show("inventory_popup", message="You wave the sword around wildly but nothing happens."),statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,13,0,0,0,0,0,0,0,0,0,0,0,0])
                            "{b}{color=#19c22a}ATK+10 -> ATK+13{/color}"
                            $ jane_inv_M.drop(rock,3)
                            $ jane_inv_M.drop(slime_jewel,5)
                        elif Items.weapon == 1:
                            $ Items.weapon = 2
                            $ sword.change("Sword +2", "My sword, my father made it for me. \nATK +16", "images/items/sword.png", 0,False, 2,Show("inventory_popup", message="You wave the sword around wildly but nothing happens."),statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,0,0,0])
                            "{b}{color=#19c22a}ATK+13 -> ATK+16{/color}"
                            $ jane_inv_M.drop(rock,5)
                            $ jane_inv_M.drop(ectoplasm,4)
                        elif Items.weapon == 2:
                            $ Items.weapon = 3
                            $ sword.change("Sword +3", "My sword, my father made it for me. \nATK +20", "images/items/sword.png", 0,False, 2,Show("inventory_popup", message="You wave the sword around wildly but nothing happens."),statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,20,0,0,0,0,0,0,0,0,0,0,0,0])
                            "{b}{color=#19c22a}ATK+16 -> ATK+20{/color}"
                            $ jane_inv_M.drop(iron_ore,4)
                            $ jane_inv_M.drop(lizard_scale,5)
                        elif Items.weapon == 3:
                            $ Items.weapon = 4
                            $ sword.change("Sword +4", "My sword, my father made it for me. \nATK +25", "images/items/sword.png", 0,False, 2,Show("inventory_popup", message="You wave the sword around wildly but nothing happens."),statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0])
                            "{b}{color=#19c22a}ATK+20 -> ATK+25{/color}"
                            $ jane_inv_M.drop(iron_ore,8)
                            $ jane_inv_M.drop(blood_crystals,2)

                        jump T_barn
                    elif True:
                        "You don't have enough materials."
                        jump Anvil_update_dadsword
                "Leave" if True:
                    hide screen anvil_need
                    hide screen anvil_need_name
                    jump T_barn

        jump T_barn
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
