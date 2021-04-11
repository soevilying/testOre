label cook_wip:

    label cook_wip1:
        menu:
            "Cook screen" if True:
                jump cook_screen
            "Leave" if True:
                jump c_code
label cook_ft_animation:
    scene black with slow_dissolve
    play sound "music/cook_oil.ogg"
    show cook_black with dissolve
    show cook_parifcook01 with dissolve:
        xpos 0.388 ypos 0.29
        zoom 1
    pause 3
    hide cook_parifcook01 with dissolve
    play sound "music/cook_cut.ogg"
    show cook_parifcook02 with dissolve:
        xpos 0.495 ypos 0.29
        zoom 1
    pause 3
    hide cook_parifcook02 with dissolve
    play sound "music/cook_end.ogg"
    show cook_black02 behind cook_black with dissolve:
        xpos 0.388 ypos 0.29
        zoom 1

    show cook_table behind cook_black02:
        xpos 0.388 ypos 0.29
        zoom 1
    show cook_light behind cook_black02:
        xpos 0.388 ypos 0.29
        zoom 1
    show cook_lid behind cook_black02:
        xpos 0.388 ypos 0.29
        zoom 1
    show cook_ball behind cook_lid:
        xpos 0.388 ypos 0.29
        zoom 1
    show cook_star behind cook_ball:
        xpos 0.388 ypos 0.29
        zoom 1

    if Parif.cook_info =="Gsalad":
        show salad behind cook_star:
            xpos 0.388 ypos 0.29
            zoom 1
    elif Parif.cook_info =="Rpotato":
        show rpotato behind cook_star:
            xpos 0.388 ypos 0.29
            zoom 1

    elif Parif.cook_info =="Redjambread":
        show jam_bread behind cook_star:
            xpos 0.388 ypos 0.29
            zoom 1
    elif Parif.cook_info == "jam_cake":
        show jam_cake behind cook_star:
            xpos 0.388 ypos 0.29
            zoom 1
    elif Parif.cook_info =="GFskewer":
        show grilled_fish_skewer behind cook_star:
            xpos 0.388 ypos 0.29
            zoom 1
    elif Parif.cook_info =="Coffee":
        show h_coffee behind cook_star:
            xpos 0.388 ypos 0.3
            zoom 1
    elif True:
        pass


    hide cook_black02 with vslow_dissolve
    show cook_ball_ex:
        xpos 0.388 ypos 0.29
        zoom 1
    show cook_lid behind cook_ball_ex with MoveTransition(1.5):
        xpos 0.388 ypos -0.1
        zoom 1
    hide cook_lid
    pause 0.5
    hide cook_ball_ex with slow_dissolve
    hide cook_ball with vvslow_dissolve
    play sound "music/cook_end02.ogg"
    jump cook_check


label cook_screen:
    scene tavern kitchen
    show parif stand at center
    window hide None
    call screen cook_screen with dissolve


    if _return == 'back':
        jump Parif_talk_tree01
        return








    if _return == 'check':
        if Parif.cook_info =="Gsalad":
            if jane_inv_M.qty(cabbage) < 1 or jane_inv_M.qty(tomato) <2 or jane_inv_M.qty(carrot) <2:
                p "You don't have enough ingredient, eggshell."
                jump cook_screen
            elif True:
                if Parif.cook_Gsalad == 1:
                    p "Oh, carrots and cabbages, my kids loved them."
                    e 5 "Wow, you have a family and kids"
                    "He laughs loudly."
                    p "Do you think my charisma is such a failure like that silly single puppy at the tavern bar?"
                    "You heard a big sneeze from the bar."
                    p "Ok, this is easy to make, let me start."
                    jump cook_ft_animation
                elif True:
                    jump cook_check
        elif Parif.cook_info =="Rpotato":
            if jane_inv_M.qty(potato) < 2:
                p "You don't have enough ingredient, eggshell."
                jump cook_screen
            elif True:
                if Parif.cook_Rpotato == 1:
                    p "Potatoes, it looks like there is still a lot of dirt on them, you just dug them out?"
                    e 6 "Yeah, Chet sold me a shovel and it's pretty useful."
                    "You show Parif the shovel."
                    p "...This is my shovel."
                    e 5 "What, but Chet told me he found it in the barn and..."
                    p "Calm down kid, you paid for this and it's yours now."
                    p "About that hyena, I WILL talk to him about this later."
                    jump cook_ft_animation
                elif True:
                    jump cook_check
        elif Parif.cook_info =="Redjambread":
            if jane_inv_M.qty(red_jam) < 1 or jane_inv_M.qty(oat_flour) <3:
                p "You don't have enough ingredient, eggshell."
                jump cook_screen
            elif True:
                if Parif.cook_Redjambread == 1:
                    p "Oatmeal bread, so nostalgic."
                    e 1 "What's so nostalgic about it?"
                    p "Only the nobles can enjoy those delicious dishes."
                    p "So the oatmeal is the most frequent staple food of our family."
                    p "Cheap and easy to get. That and it makes you full easily. "
                    e 6 "Well, I don't really love them."
                    p "Yeah, yeah, I know you puppies still like meat the most."
                    p "Okay, now I am going to work."
                    jump cook_ft_animation
                elif True:
                    jump cook_check
        elif Parif.cook_info =="GFskewer":
            if jane_inv_M.qty(grass_carp) < 1 or jane_inv_M.qty(lemon) <1:
                p "You don't have enough ingredient, eggshell."
                jump cook_screen
            elif True:
                if Parif.cook_GFskewer == 1:
                    p "So you are still smart enough to catch some fish, good."
                    e 1 "Well, yeah, Snow's rod is useful."
                    p "Snow often finds me to go fishing."
                    p "But you know what, that guy really likes to take off his shirt every time he fishes."
                    e 9 "Well, that's not really a bad habit isn't it?"
                    e 6 "I too like to use my tail to attract fishes."
                    p "...I think I will never understand these special traits of you puppies."
                    jump cook_ft_animation
                elif True:
                    jump cook_check
        elif Parif.cook_info =="Redjam":
            if jane_inv.qty(raspberry) < 3:
                p "You don't have enough ingredient, eggshell."
                jump cook_screen
            elif True:
                jump cook_check

        elif Parif.cook_info =="Coffee":
            if jane_inv_M.qty(coffee_beans) < 1:
                p "You don't have enough ingredient, eggshell."
                jump cook_screen
            elif True:
                if Parif.cook_Hcoffee == 1:
                    p "Oh, these are coffee beans."
                    e 1 "You know them?"
                    e 6 "I've never seen them before, they're strangely tasty even though they're bitter."
                    p "Don't forget that I used to work for a lot of nobles, and they often find a lot of weird ingredients like this."
                    p "I might still remember how to make something special with this."
                    p "Hold on."
                    jump cook_ft_animation
                elif True:
                    jump cook_check
        jump cook_check
        return
    return


label cook_check:
    if Parif.cook_info =="Gsalad":
        "You get a mixed green salad!"
        $ jane_inv.take(mixed_green_salad,1)
        $ jane_inv_M.drop(cabbage,1)
        $ jane_inv_M.drop(tomato,2)
        $ jane_inv_M.drop(carrot,2)
        if Parif.cook_Gsalad == 1:
            $ Parif.cook_Gsalad = 2
            $ Zalt.maxmp = Zalt.maxmp + 5
            $ Zalt.mp = Zalt.maxmp
            $ Parif.cook_helptime = Parif.cook_helptime +1
            "{b}{color=#19c22a}<[name]'s Max MP +5>{/color}"
    elif Parif.cook_info =="Rpotato":
        "You get a plate of roasted potatoes!"
        $ jane_inv_M.drop(potato,2)
        $ jane_inv.take(roasted_potatoes,1)
        if Parif.cook_Rpotato == 1:
            $ Parif.cook_Rpotato = 2
            $ Zalt.maxhp = Zalt.maxhp + 5
            $ Zalt.hp = Zalt.maxhp
            $ Parif.cook_helptime = Parif.cook_helptime +1
            "{b}{color=#19c22a}<[name]'s Max HP +5>{/color}"
    elif Parif.cook_info =="Redjambread":
        "You get a jam oatmeal bread!"
        $ jane_inv_M.drop(red_jam,1)
        $ jane_inv_M.drop(oat_flour,3)
        $ jane_inv.take(jam_oatmeal_bread,1)
        if Parif.cook_Redjambread == 1:
            $ Parif.cook_Redjambread = 2
            $ Zalt.ATK = Zalt.ATK + 3
            $ Parif.cook_helptime = Parif.cook_helptime +1
            "{b}{color=#19c22a}<[name]'s ATK + 3>{/color}"
    elif Parif.cook_info =="GFskewer":
        "You get a grilled fish skewer!"
        $ jane_inv_M.drop(grass_carp,1)
        $ jane_inv_M.drop(lemon,1)
        $ jane_inv.take(grilled_fish_skewer,1)
        if Parif.cook_GFskewer == 1:
            $ Parif.cook_GFskewer = 2
            $ Zalt.DEF = Zalt.DEF + 2
            $ Parif.cook_helptime = Parif.cook_helptime +1
            "{b}{color=#19c22a}<[name]'s DEF + 2>{/color}"
    elif Parif.cook_info =="Redjam":
        "You get a red jam!"
        $ jane_inv.drop(raspberry,3)
        $ jane_inv_M.take(red_jam,1)

    elif Parif.cook_info =="Coffee":
        "You get a coffee!"
        $ jane_inv_M.drop(coffee_beans)
        $ jane_inv.take(h_coffee,1)
        if Parif.cook_Hcoffee == 1:
            $ Parif.cook_Hcoffee = 2
            $ Zalt.MATK = Zalt.MATK + 2
            $ Parif.cook_helptime = Parif.cook_helptime +1
            "{b}{color=#19c22a}<[name]'s MATK +2>{/color}"
    jump cook_screen
    return

screen cook_screen:





    add "images/UI/cook_screen01.png"
    add "images/UI/cook_screen02.png"


    add "UI/cook_screen05.png":
        size (128 ,118)
        xalign 0.42 yalign 0.83

    add "UI/cook_screen05.png":
        size (128 ,118)
        xalign 0.638 yalign 0.83

    add "UI/cook_screen05.png":
        size (128 ,118)
        xalign 0.42 yalign 0.966

    add "UI/cook_screen05.png":
        size (128 ,118)
        xalign 0.638 yalign 0.966

    vbox:
        xalign 0.37 ypos 0.041
        if Parif.cook_screen == "starter01":
            imagebutton:
                idle "UI/tag_starter02.png"
                hover "UI/tag_starter02.png"

                action None
        else:
            imagebutton:
                idle "UI/tag_starter01.png"
                hover "UI/tag_starter02.png"

                action (SetVariable("Parif.cook_screen","starter01"), SetVariable("Parif.cook_sjx",0), Hide("UI/cook_sjx.png"))

    vbox:
        xalign 0.41 ypos 0.06
        if Parif.cook_screen == "mains01":
            imagebutton:
                idle "UI/tag_main02.png"
                hover "UI/tag_main02.png"

                action None
        else:
            imagebutton:
                idle "UI/tag_main01.png"
                hover "UI/tag_main02.png"

                action (SetVariable("Parif.cook_screen","mains01"), SetVariable("Parif.cook_sjx",0), Hide("UI/cook_sjx.png"))

    vbox:
        xalign 0.44 ypos 0.06
        if Parif.cook_screen == "soup01":
            imagebutton:
                idle "UI/tag_soup02.png"
                hover "UI/tag_soup02.png"

                action None
        else:
            imagebutton:
                idle "UI/tag_soup01.png"
                hover "UI/tag_soup02.png"

                action (SetVariable("Parif.cook_screen","soup01"), SetVariable("Parif.cook_sjx",0), Hide("UI/cook_sjx.png"))

    vbox:
        xalign 0.47 ypos 0.06
        if Parif.cook_screen == "drinks01":
            imagebutton:
                idle "UI/tag_drinks02.png"
                hover "UI/tag_drinks02.png"

                action None
        else:
            imagebutton:
                idle "UI/tag_drinks01.png"
                hover "UI/tag_drinks02.png"

                action (SetVariable("Parif.cook_screen","drinks01"), SetVariable("Parif.cook_sjx",0), Hide("UI/cook_sjx.png"))

    vbox:
        xalign 0.51 ypos 0.06
        if Parif.cook_screen == "dessert01":
            imagebutton:
                idle "UI/tag_dessert02.png"
                hover "UI/tag_dessert02.png"

                action None
        else:
            imagebutton:
                idle "UI/tag_dessert01.png"
                hover "UI/tag_dessert02.png"

                action (SetVariable("Parif.cook_screen","dessert01"), SetVariable("Parif.cook_sjx",0), Hide("UI/cook_sjx.png"))

    vbox:
        xalign 0.56 ypos 0.06
        if Parif.cook_screen == "condiment01":
            imagebutton:
                idle "UI/tag_condiment02.png"
                hover "UI/tag_condiment02.png"

                action None
        else:
            imagebutton:
                idle "UI/tag_condiment01.png"
                hover "UI/tag_condiment02.png"

                action (SetVariable("Parif.cook_screen","condiment01"), SetVariable("Parif.cook_sjx",0), Hide("UI/cook_sjx.png"))


    vbox:
        xalign 0.974 yalign 0.65
        imagebutton:
            idle "UI/cook_screen04.png"
            hover "UI/cook_screen04a.png"

            action (Return("back"), SetVariable("Parif.cook_screen","starter01"), SetVariable("Parif.cook_sjx",0), Hide("UI/cook_sjx.png"))
    vbox:
        align (0.1, 0.9)
        spacing 20





    frame background None:



        has grid 4 4:

            pos (0.68,0.5)

            xfill True
            yfill True


            xsize 1080
            ysize 370

            spacing 70

        if Parif.cook_screen == "starter01":
            button:
                if Parif.cook_Gsalad != 0:
                    text "Mixed Green Salad"
                    action (SetVariable("Parif.cook_info","Gsalad"), SetVariable("Parif.cook_sjx",1))
                else:
                    add "UI/coming_soon.png"
            button:
                if Parif.cook_Rpotato != 0:
                    text "Roasted Potatoes"
                    action (SetVariable("Parif.cook_info","Rpotato"), SetVariable("Parif.cook_sjx",1))
                else:
                    add "UI/coming_soon.png"

            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"

        elif Parif.cook_screen == "mains01":
            button:
                if Parif.cook_Redjambread != 0:
                    text "Jam Oatmeal Bread"
                    action (SetVariable("Parif.cook_info","Redjambread"), SetVariable("Parif.cook_sjx",1))
                else:
                    text "???"
            button:
                if Parif.cook_GFskewer != 0:
                    text "Grilled Fish Skewer"
                    action (SetVariable("Parif.cook_info","GFskewer"), SetVariable("Parif.cook_sjx",1))
                else:
                    text "???"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"

        elif Parif.cook_screen == "soup01":
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"


        elif Parif.cook_screen == "drinks01":
            button:
                if Parif.cook_Hcoffee != 0:
                    text "Coffee"
                    action (SetVariable("Parif.cook_info","Coffee"), SetVariable("Parif.cook_sjx",1))
                else:
                    text "???"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"

        elif Parif.cook_screen == "dessert01":
            button:
                text "---"





            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"


        elif Parif.cook_screen == "condiment01":
            button:
                if Parif.cook_Redjam != 0:
                    text "Red Jam"
                    action (SetVariable("Parif.cook_info","Redjam"), SetVariable("Parif.cook_sjx",1))
                else:
                    text "???"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"

        else:
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"
            button:
                text "---"






    if Parif.cook_info == "Gsalad":
        if jane_inv_M.qty(cabbage) != None:
            $ NPC.cook_need1_0 = jane_inv_M.qty(cabbage)
        else:
            $ NPC.cook_need1_0 = 0

        if jane_inv_M.qty(tomato) != None:
            $ NPC.cook_need2_0 = jane_inv_M.qty(tomato)
        else:
            $ NPC.cook_need2_0 = 0
        if jane_inv_M.qty(carrot) != None:
            $ NPC.cook_need3_0 = jane_inv_M.qty(carrot)
        else:
            $ NPC.cook_need3_0 = 0
        modal True
        zorder 1
        vbox:
            xalign 0.95 ypos 0.81
            imagebutton:
                idle "UI/cook_screen03.png"
                hover "UI/cook_screen03a.png"
                action Return("check")
        if Parif.cook_sjx == 1:
            add "UI/cook_sjx.png":
                xalign 0.51 yalign 0.21
                zoom 0.9
        vbox:
            text "{b}{color=#ffffff}{size=+3}  MIXED GREEN SALAD{/size}{/color}"
            area (84, 66, 485, 64)

        if Parif.cook_Gsalad == 1:
            add "UI/cook_screen06.png":
                xalign 0.21 yalign 0.31

            add "items/food/salad0.png":
                size (384 ,362)
                xalign 0.084 yalign 0.34

            vbox:
                area (29, 670, 600, 61)
                text "{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} Max MP+5{/size}{/color}"
        else:
            vbox:
                area (29, 670, 600, 61)
                text "{s}{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} Max MP+5{/size}{/color}{/s}"

            add "items/food/salad.png":
                size (384 ,362)
                xalign 0.084 yalign 0.34


        vbox:
            area (30, 770, 614, 71)
            text "{color=#ffffff}{size=-3}Use:{/color}{/size}{size=+3}{color=#4d9e49}  MP+120{/size}{/color}"

        vbox:
            area (30, 859, 609, 198)
            text "{color=#ffffff}{size=-5}A healthy bowl of vegetables to get the appetite started.{/size}{/color}"

        add "items/cabbage.png":
            size (128 ,118)
            xalign 0.42 yalign 0.83

        vbox:
            text "{color=#ffffff}{size=-5}Cabbage{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need1_0]/1{/size}{/color}"
            area (895, 796, 258, 115)

        add "items/tomato.png":
            size (128 ,118)
            xalign 0.638 yalign 0.83

        vbox:
            text "{color=#ffffff}{size=-5}Tomato{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need2_0]/2{/size}{/color}"
            area (1295, 796, 300, 115)

        add "items/carrot.png":
            size (128 ,118)
            xalign 0.42 yalign 0.966

        vbox:
            text "{color=#ffffff}{size=-5}Carrot{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need3_0]/2{/size}{/color}"
            area (895, 926, 258, 110)


    elif Parif.cook_info == "Rpotato":
        if jane_inv_M.qty(potato) != None:
            $ NPC.cook_need1_0 = jane_inv_M.qty(potato)
        else:
            $ NPC.cook_need1_0 = 0

        modal True
        zorder 1
        vbox:
            xalign 0.95 ypos 0.81
            imagebutton:
                idle "UI/cook_screen03.png"
                hover "UI/cook_screen03a.png"
                action Return("check")

        if Parif.cook_sjx == 1:
            add "UI/cook_sjx.png":
                xalign 0.65 yalign 0.21
                zoom 0.9
        vbox:
            text "{b}{color=#ffffff}{size=+3}  ROASTED POTATOES{/size}{/color}"
            area (84, 66, 485, 64)

        if Parif.cook_Rpotato == 1:
            add "UI/cook_screen06.png":
                xalign 0.21 yalign 0.31

            add "items/food/rpotato0.png":
                size (384 ,362)
                xalign 0.084 yalign 0.34

            vbox:
                area (29, 670, 600, 61)
                text "{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} Max HP+5{/size}{/color}"
        else:
            vbox:
                area (29, 670, 600, 61)
                text "{s}{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} Max HP+5{/size}{/color}{/s}"

            add "items/food/rpotato.png":
                size (384 ,362)
                xalign 0.084 yalign 0.34

        vbox:
            area (30, 770, 614, 71)
            text "{color=#ffffff}{size=-3}Use:{/color}{/size}{size=+3}{color=#4d9e49}  HP+100{/size}{/color}"

        vbox:
            area (30, 859, 609, 198)
            text "{color=#ffffff}{size=-5}Cooked to perfection by blasting potatoes with high heat strong enough to melt a blade.\nHow it tastes so good is anyone’s wonder.{/size}{/color}"

        add "items/potato.png":
            size (128 ,118)
            xalign 0.42 yalign 0.83

        vbox:
            text "{color=#ffffff}{size=-5}Potato{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need1_0]/2{/size}{/color}"
            area (895, 796, 258, 115)
    elif Parif.cook_info == "Redjambread":
        if jane_inv_M.qty(red_jam) != None:
            $ NPC.cook_need1_0 = jane_inv_M.qty(red_jam)
        else:
            $ NPC.cook_need1_0 = 0

        if jane_inv_M.qty(oat_flour) != None:
            $ NPC.cook_need2_0 = jane_inv_M.qty(oat_flour)
        else:
            $ NPC.cook_need2_0 = 0
        modal True
        zorder 1
        vbox:
            xalign 0.95 ypos 0.81
            imagebutton:
                idle "UI/cook_screen03.png"
                hover "UI/cook_screen03a.png"
                action Return("check")
        if Parif.cook_sjx == 1:
            add "UI/cook_sjx.png":
                xalign 0.51 yalign 0.21
                zoom 0.9
        if Parif.cook_Redjambread == 1:
            add "UI/cook_screen06.png":
                xalign 0.21 yalign 0.31

            add "items/food/jam_bread0.png":
                xalign 0.071 yalign 0.3
                zoom 0.95

            vbox:
                area (29, 670, 600, 61)
                text "{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} ATK+3{/size}{/color}"
        else:
            vbox:
                area (29, 670, 600, 61)
                text "{s}{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} ATK+3{/size}{/color}{/s}"

            add "items/food/jam_bread.png":
                xalign 0.071 yalign 0.3
                zoom 0.95

        vbox:
            text "{b}{color=#ffffff}{size=+3}  JAM OATMEAL BREAD{/size}{/color}"
            area (84, 66, 485, 64)
        vbox:
            area (30, 770, 614, 71)
            text "{color=#ffffff}{size=-3}Use:{/color}{/size}{size=+3}{color=#4d9e49}  HP+150{/size}{/color}"

        vbox:
            area (30, 859, 609, 198)
            text "{color=#ffffff}{size=-5}A beautiful loaf of bread with a jar of sweet jam.\nIt is said that those that eat it for the first time see visions of a lush wheat field or the orchard where the fruits are plucked.{/size}{/color}"

        add "items/food/red_jam.png":
            zoom 0.4
            xalign 0.415 yalign 0.843

        vbox:
            text "{color=#ffffff}{size=-5}Red jam{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need1_0]/1{/size}{/color}"
            area (895, 796, 258, 115)


        add "items/oat_flour.png":

            xalign 0.638 yalign 0.83

        vbox:
            text "{color=#ffffff}{size=-5}Oat flour{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need2_0]/3{/size}{/color}"
            area (1295, 796, 300, 115)









    elif Parif.cook_info == "GFskewer":
        if jane_inv_M.qty(grass_carp) != None:
            $ NPC.cook_need1_0 = jane_inv_M.qty(grass_carp)
        else:
            $ NPC.cook_need1_0 = 0

        if jane_inv_M.qty(lemon) != None:
            $ NPC.cook_need2_0 = jane_inv_M.qty(lemon)
        else:
            $ NPC.cook_need2_0 = 0
        modal True
        zorder 1
        vbox:
            xalign 0.95 ypos 0.81
            imagebutton:
                idle "UI/cook_screen03.png"
                hover "UI/cook_screen03a.png"
                action Return("check")
        if Parif.cook_sjx == 1:
            add "UI/cook_sjx.png":
                xalign 0.65 yalign 0.21
                zoom 0.9
        if Parif.cook_GFskewer == 1:
            add "UI/cook_screen06.png":
                xalign 0.21 yalign 0.31

            add "items/food/grilled_fish_skewer0.png":
                xalign 0.071 yalign 0.3
                zoom 0.95

            vbox:
                area (29, 670, 600, 61)
                text "{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} DEF+2{/size}{/color}"
        else:
            vbox:
                area (29, 670, 600, 61)
                text "{s}{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} DEF+2{/size}{/color}{/s}"

            add "items/food/grilled_fish_skewer.png":
                xalign 0.071 yalign 0.3
                zoom 0.95


        vbox:
            text "{b}{color=#ffffff}{size=+3} GRILLED FISH SKEWER{/size}{/color}"
            area (84, 66, 485, 64)
        vbox:
            area (30, 770, 614, 71)
            text "{color=#ffffff}{size=-3}Use:{/color}{/size}{size=+3}{color=#4d9e49}  MP+90{/size}{/color}"

        vbox:
            area (30, 859, 609, 198)
            text "{color=#ffffff}{size=-5}A piece of fish grilled over a slow fire.\nSuitable to fill one up for a bit.{/size}{/color}"

        add "items/grass_carp.png":
            xalign 0.42 yalign 0.825

        vbox:
            text "{color=#ffffff}{size=-5}Grass carp{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need1_0]/1{/size}{/color}"
            area (895, 796, 258, 115)


        add "items/lemon.png":
            xalign 0.638 yalign 0.825

        vbox:
            text "{color=#ffffff}{size=-5}Lemon{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need2_0]/1{/size}{/color}"
            area (1295, 796, 300, 115)









    elif Parif.cook_info == "Redjam":
        if jane_inv.qty(raspberry) != None:
            $ NPC.cook_need1_0 = jane_inv.qty(raspberry)
        else:
            $ NPC.cook_need1_0 = 0
        modal True
        zorder 1
        vbox:
            xalign 0.95 ypos 0.81
            imagebutton:
                idle "UI/cook_screen03.png"
                hover "UI/cook_screen03a.png"
                action Return("check")
        if Parif.cook_sjx == 1:
            add "UI/cook_sjx.png":
                xalign 0.65 yalign 0.21
                zoom 0.9
        add "items/food/red_jam.png":
            xalign 0.083 yalign 0.35
            zoom 0.85
        vbox:
            text "{b}{color=#ffffff}{size=+3}              RED JAM{/size}{/color}"
            area (84, 66, 485, 64)
        vbox:
            area (30, 770, 614, 71)
            text "{color=#ffffff}{size=+3}---{/size}{/color}"

        vbox:
            area (30, 859, 609, 198)
            text "{color=#ffffff}{size=-5}Raspberry jam, a nice condiment that can go with different dishes.{/size}{/color}"

        add "items/raspberry.png":
            xalign 0.42 yalign 0.825

        vbox:
            text "{color=#ffffff}{size=-5}Raspberry{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need1_0]/3{/size}{/color}"
            area (895, 796, 258, 115)










    elif Parif.cook_info == "Coffee":
        if jane_inv_M.qty(coffee_beans) != None:
            $ NPC.cook_need1_0 = jane_inv_M.qty(coffee_beans)
        else:
            $ NPC.cook_need1_0 = 0

        modal True
        zorder 1
        vbox:
            xalign 0.95 ypos 0.81
            imagebutton:
                idle "UI/cook_screen03.png"
                hover "UI/cook_screen03a.png"
                action Return("check")

        if Parif.cook_sjx == 1:
            add "UI/cook_sjx.png":
                xalign 0.47 yalign 0.195
                zoom 0.9
        vbox:
            text "{b}{color=#ffffff}{size=+3}                Coffee{/size}{/color}"
            area (84, 66, 485, 64)

        if Parif.cook_Hcoffee == 1:
            add "UI/cook_screen06.png":
                xalign 0.21 yalign 0.31

            add "items/food/h_coffee0.png":
                size (384 ,362)
                xalign 0.087 yalign 0.34

            vbox:
                area (29, 670, 600, 61)
                text "{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} MATK +2{/size}{/color}"
        else:
            vbox:
                area (29, 670, 600, 61)
                text "{s}{color=#db5c48}{size=-3}Bonus:{/size}{size=+3} MATK +2{/size}{/color}{/s}"

            add "items/food/h_coffee.png":
                size (384 ,362)
                xalign 0.087 yalign 0.34

        vbox:
            area (30, 770, 614, 71)
            text "{color=#ffffff}{size=-3}Use:{/color}{/size}{size=+3}{color=#4d9e49}  MP+80{/size}{/color}"

        vbox:
            area (30, 859, 609, 198)
            text "{color=#ffffff}{size=-5}A cup of grinded coffee beans topped with Parif's artwork made from milk foam.\nA sip of this and you will have energy for hours.{/size}{/color}"

        add "items/coffee_beans.png":
            xalign 0.42 yalign 0.825

        vbox:
            text "{color=#ffffff}{size=-5}Coffee beans{/size}{/color}"
            text "{color=#ffffff}{size=-5}[NPC.cook_need1_0]/1{/size}{/color}"
            area (895, 796, 258, 115)



image cook_ball:
    "images/items/food/cook_ball01.png" with q_dissolve
    pause 1
    "images/items/food/cook_ball02.png" with q_dissolve
    pause 1
    repeat
image cook_ball_ex:
    "images/items/food/cook_ball06.png" with q_dissolve
    pause 0.05
    "images/items/food/cook_ball05.png" with q_dissolve
    pause 0.2
    "images/items/food/cook_ball03.png" with q_dissolve
    pause 0.5
    "images/items/food/cook_ball04.png" with slow_dissolve
image cook_star:
    "images/items/food/cook_star01.png" with q_dissolve
    pause 0.8
    "images/items/food/cook_star02.png" with q_dissolve
    pause 0.8
    repeat
image cook_parifcook01:
    "images/items/food/Parif_cook1__0001.png"
    pause 0.1
    "images/items/food/Parif_cook1__0002.png"
    pause 0.1
    "images/items/food/Parif_cook1__0003.png"
    pause 0.1
    "images/items/food/Parif_cook1__0004.png"
    pause 0.1
    "images/items/food/Parif_cook1__0005.png"
    pause 0.1
    "images/items/food/Parif_cook1__0006.png"
    pause 0.1
    "images/items/food/Parif_cook1__0007.png"
    pause 0.1
    "images/items/food/Parif_cook1__0008.png"
    pause 0.1
    "images/items/food/Parif_cook1__0009.png"
    pause 0.1
    "images/items/food/Parif_cook1__0010.png"
    pause 0.1
    "images/items/food/Parif_cook1__0011.png"
    pause 0.1
    "images/items/food/Parif_cook1__0012.png"
    pause 0.1
    "images/items/food/Parif_cook1__0013.png"
    pause 0.1
    "images/items/food/Parif_cook1__0014.png"
    pause 0.1
    "images/items/food/Parif_cook1__0015.png"
    pause 0.1
    "images/items/food/Parif_cook1__0016.png"
    pause 0.1
    "images/items/food/Parif_cook1__0017.png"
    pause 0.1
    "images/items/food/Parif_cook1__0018.png"
    pause 0.1
    repeat


image cook_parifcook02:
    "images/items/food/Parif_cook2_0001.png"
    pause 0.1
    "images/items/food/Parif_cook2_0002.png"
    pause 0.1
    "images/items/food/Parif_cook2_0003.png"
    pause 0.1
    "images/items/food/Parif_cook2_0004.png"
    pause 0.1
    "images/items/food/Parif_cook2_0005.png"
    pause 0.1
    "images/items/food/Parif_cook2_0006.png"
    pause 0.1
    "images/items/food/Parif_cook2_0007.png"
    pause 0.1
    "images/items/food/Parif_cook2_0008.png"
    pause 0.1
    "images/items/food/Parif_cook2_0009.png"
    pause 0.1
    "images/items/food/Parif_cook2_0010.png"
    pause 0.1
    "images/items/food/Parif_cook2_0011.png"
    pause 0.1
    "images/items/food/Parif_cook2_0012.png"
    pause 0.1
    "images/items/food/Parif_cook2_0013.png"
    pause 0.1
    "images/items/food/Parif_cook2_0014.png"
    pause 0.1
    "images/items/food/Parif_cook2_0015.png"
    pause 0.1
    "images/items/food/Parif_cook2_0016.png"
    pause 0.1
    "images/items/food/Parif_cook2_0017.png"
    pause 0.1
    "images/items/food/Parif_cook2_0018.png"
    pause 0.1
    "images/items/food/Parif_cook2_0019.png"
    pause 0.1
    "images/items/food/Parif_cook2_0020.png"
    pause 0.1
    "images/items/food/Parif_cook2_0021.png"
    pause 0.1
    "images/items/food/Parif_cook2_0022.png"
    pause 0.1
    "images/items/food/Parif_cook2_0023.png"
    pause 0.1
    "images/items/food/Parif_cook2_0024.png"
    pause 0.1
    "images/items/food/Parif_cook2_0025.png"
    pause 0.1
    "images/items/food/Parif_cook2_0026.png"
    pause 0.1
    "images/items/food/Parif_cook2_0027.png"
    pause 0.1
    "images/items/food/Parif_cook2_0028.png"
    pause 0.1
    "images/items/food/Parif_cook2_0029.png"
    pause 0.1
    "images/items/food/Parif_cook2_0030.png"
    pause 0.1
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
