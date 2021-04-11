


screen gallery:
    tag menu




    add "images/back.jpg"




    vbox:
        align (0.1, 0.9)
        spacing 10





    frame background None:



        has grid 3 3:

            pos (0.55,0.1)

            xfill True
            yfill True


            xsize 1200
            ysize 600

            spacing 100

        button:
            if persistent.CG_goo_lose:
                add "UI/00.png"
                action Show("slimelose_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_witer_bj:
                add "UI/01.png"
                action Show("witerbj_g")
            else:
                add "UI/coming_soon.png"

        button:
            if persistent.CG_bull_lose:
                add "UI/02.png"
                action Show("bulllose_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_bull_winA:
                add "UI/03.png"
                action Show("bullwinA_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_bull_winB:
                add "UI/04.png"
                action Show("bullwinB_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_tree_lose:
                add "UI/05.png"
                action Show("treelose_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_ghost_lose:
                add "UI/06.png"
                action Show("ghostlose_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_hakan_ride:
                add "UI/07.png"
                action Show("hakanride_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_bull_lick:
                add "UI/08.png"
                action Show("bulllick_g")
            else:
                add "UI/coming_soon.png"

    if mp.beat_part_1:
        textbutton "Bonus" action ShowMenu("B_gallery") xalign 0.7 yalign 0.9
    else:
        pass
    textbutton "->" action ShowMenu("gallery02") xalign 0.9 yalign 0.8
    textbutton "Back" action Return() xalign 0.9 yalign 0.9



screen slimelose_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("slimelose_g")

    vbox:
        text "{color=#ffffff}{size=-1}Player defeated by the goo foe.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("slimelose_g"), Jump("slimelose_gcg") ]
    add "slime lose1.png":
        size (450 ,507)
        xalign 0.04 yalign 0.04

screen witerbj_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("witerbj_g")

    vbox:
        text "{color=#ffffff}{size=-1}Witer gives player a reward after gets some tips.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("witerbj_g"), Jump("Witer_bj_gcg") ]
    add "witer blowjob1.png":
        size (512 ,280)
        xalign 0.02 yalign 0.15


screen bulllose_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("bulllose_g")

    vbox:
        text "{color=#ffffff}{size=-3}Player defeated by the bull foe.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("bulllose_g"), Jump("battle_bull_lose_gcg") ]
    add "bull lose1.png":
        size (512 ,390)
        xalign 0.02 yalign 0.12


screen bullwinA_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("bullwinA_g")

    vbox:
        text "{color=#ffffff}{size=-3}Player helps the bull foe solve his small problems. (Low endurance version) {/size}{/color}"
        area (62, 871, 1778, 172)

    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("bullwinA_g"), Jump("battle_bull_sex_agcg") ]
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    add "bull win1.png":
        size (450 ,507)
        xalign 0.04 yalign 0.04

screen bullwinB_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("bullwinB_g")

    vbox:
        text "{color=#ffffff}{size=-3}Player helps the bull foe solve his small problems. (High endurance version) {/size}{/color}"
        area (62, 871, 1778, 172)

    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("bullwinB_g"), Jump("battle_bull_sex_bgcg") ]
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    add "bull win1.png":
        size (450 ,507)
        xalign 0.04 yalign 0.04

screen treelose_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("treelose_g")

    vbox:
        text "{color=#ffffff}{size=-3}Player defeated by the tree monster. {/size}{/color}"
        area (62, 871, 1778, 172)

    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("treelose_g"), Jump("battle_tree_lose_gcg") ]
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    add "tree lose1.png":
        size (512 ,400)
        xalign 0.02 yalign 0.12

screen ghostlose_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("ghostlose_g")

    vbox:
        text "{color=#ffffff}{size=-3}Player defeated by the ghost. {/size}{/color}"
        area (62, 871, 1778, 172)

    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("ghostlose_g"), Jump("battle_ghost_lose_gcg") ]
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    add "ghost lose1.png":
        size (512 ,516)
        xalign 0.02 yalign 0.03

screen hakanride_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("hakanride_g")

    vbox:
        text "{color=#ffffff}{size=-1}Player gets a riding invitation from Hakan.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("hakanride_g"), Jump("Hakan_ride_gcg") ]
    add "hakan ridec.png":
        size (512 ,346)
        xalign 0.02 yalign 0.15

screen bulllick_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("bulllick_g")

    vbox:
        text "{color=#ffffff}{size=-1}Player is always up to help someone in need.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("bulllick_g"), Jump("bull_lick_gcg") ]
    add "lick bull1.png":
        size (512 ,280)
        xalign 0.02 yalign 0.15



screen gallery02:
    tag menu




    add "images/back.jpg"




    vbox:
        align (0.1, 0.9)
        spacing 10





    frame background None:



        has grid 3 3:

            pos (0.55,0.1)

            xfill True
            yfill True


            xsize 1200
            ysize 600

            spacing 100

        button:
            if persistent.CG_lizard_win:
                add "UI/09.png"
                action Show("lizradwin_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_lizard_lose:
                add "UI/14.png"
                action Show("lizardlose_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_gargoyle_lose:
                add "UI/10.png"
                action Show("gargoylelose_g")
            else:
                add "UI/coming_soon.png"

        button:
            if persistent.CG_gargoyle_win:
                add "UI/11.png"
                action Show("gargoylewin_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_roushk_top:
                add "UI/12.png"
                action Show("roushktop_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_roushk_bottom:
                add "UI/13.png"
                action Show("roushkbottom_g")
            else:
                add "UI/coming_soon.png"

        button:
            if persistent.CG_eyvind_sell:
                add "UI/15.png"
                action Show("eyvindsell_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_hakan_sixnine:
                add "UI/16.png"
                action Show("hakansixnine_g")
            else:
                add "UI/coming_soon.png"
        button:
            if persistent.CG_witer_cowboy:
                add "UI/17.png"
                action Show("witercowboy_g")
            else:
                add "UI/coming_soon.png"

    if mp.beat_part_1:
        textbutton "Bonus" action ShowMenu("B_gallery") xalign 0.7 yalign 0.9
    else:
        pass
    textbutton "<-" action ShowMenu("gallery") xalign 0.88 yalign 0.8
    textbutton "->" action ShowMenu("gallery03") xalign 0.9 yalign 0.8
    textbutton "Back" action Return() xalign 0.9 yalign 0.9

screen lizradwin_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("lizradwin_g")

    vbox:
        text "{color=#ffffff}{size=-1}The lizard need to learn how to shut up.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("lizradwin_g"), Jump("lizrad_sex_gcg") ]
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    add "lizard win1.png":
        size (450 ,507)
        xalign 0.04 yalign 0.04

screen lizardlose_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("lizardlose_g")

    vbox:
        text "{color=#ffffff}{size=-1}The lizard tops the Player.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("lizardlose_g"), Jump("lizrad_lose_gcg") ]
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    add "lizardtop 1g.png":
        size (512 ,321)
        xalign 0.02 yalign 0.15


screen gargoylelose_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("gargoylelose_g")

    vbox:
        text "{color=#ffffff}{size=-1}Player lose to the gargoyle.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("gargoylelose_g"), Jump("gargoyle_lose_gcg") ]
    add "garg lose1.png":
        size (512 ,346)
        xalign 0.02 yalign 0.13

screen gargoylewin_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("gargoylewin_g")

    vbox:
        text "{color=#ffffff}{size=-1}Player doggystyle the gargoyle.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("gargoylewin_g"), Jump("gargoyle_win_gcg") ]
    add "garg win1.png":
        size (512 ,346)
        xalign 0.02 yalign 0.13

screen roushktop_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("roushktop_g")

    vbox:
        text "{color=#ffffff}{size=-1}Player top Roushk.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("roushktop_g"), Jump("roushktop_gcg") ]
    add "etop 0.png":
        size (512 ,346)
        xalign 0.02 yalign 0.13

screen roushkbottom_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("roushkbottom_g")

    vbox:
        text "{color=#ffffff}{size=-1}Roushk top Player.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("roushkbottom_g"), Jump("roushkbottom_gcg") ]
    add "rtop 1.png":
        size (512 ,435)
        xalign 0.02 yalign 0.1

screen eyvindsell_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("eyvindsell_g")

    vbox:
        text "{color=#ffffff}{size=-1}Player works for currency.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("eyvindsell_g"), Jump("eyvindsell_gcg") ]
    add "eyvind sell01":
        size (512 ,290)
        xalign 0.021 yalign 0.15


screen hakansixnine_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("hakansixnine_g")

    vbox:
        text "{color=#ffffff}{size=-1}Player invite Hakan to sauna.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("hakansixnine_g"), Jump("Hakan_sixnine_gcg") ]
    add "hakan_sauna03.png":
        size (512 ,288)
        xalign 0.02 yalign 0.15


screen witercowboy_g:

    modal True
    zorder 1 tag sceneselect
    button:
        add "UI/gallery_bg2.png"
        action Hide("witercowboy_g")

    vbox:
        text "{color=#ffffff}{size=-1}Witer rides the player.{/size}{/color}"
        area (62, 871, 1778, 172)
    add "black.png":
        size (512 ,508)
        xalign 0.02 yalign 0.045
    imagebutton auto "UI/gallery_start_%s.png" xalign 0.025 yalign 0.65 action [ Hide("witercowboy_g"), Jump("Witer_cowboy_gcg") ]
    add "witer cowboy1.png":
        size (512 ,288)
        xalign 0.02 yalign 0.15




screen gallery03:
    tag menu




    add "images/back.jpg"




    vbox:
        align (0.1, 0.9)
        spacing 10





    frame background None:



        has grid 3 3:

            pos (0.55,0.1)

            xfill True
            yfill True


            xsize 1200
            ysize 600

            spacing 100

        button:
            add "UI/coming_soon01.png"
        button:
            add "UI/coming_soon01.png"
        button:
            add "UI/coming_soon01.png"
        button:
            add "UI/coming_soon01.png"
        button:
            add "UI/coming_soon01.png"
        button:
            add "UI/coming_soon01.png"
        button:
            add "UI/coming_soon01.png"
        button:
            add "UI/coming_soon01.png"
        button:
            add "UI/coming_soon01.png"

    if mp.beat_part_1:
        textbutton "Bonus" action ShowMenu("B_gallery") xalign 0.7 yalign 0.9
    else:
        pass
    textbutton "<-" action ShowMenu("gallery02") xalign 0.88 yalign 0.8
    textbutton "Back" action Return() xalign 0.9 yalign 0.9
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
