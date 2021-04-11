label battle_gargoyle:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 250
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 99

    $ Map.good_battle = True
    $ Battle.holyfcd = 0
    stop Chan1
    stop Chan2
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    stop music
    scene caveruin 1n with slow_dissolve


label battle_gargoyle_loop:



    show screen simple_stats_screen
    show screen battle_menu
    show gargoyle at center
    play music "<loop 4.6903>music/forest_fight_small.ogg"





    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Holy Fist":
            $ red_damage = renpy.random.randint(int((Zalt.MATK*2)+5), int((Zalt.MATK*3)+10))
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
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-40), Zalt.ATK-10)
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
            jump battle_gargoyle_lose
        if res == "Flirt":
            $ Random = renpy.random.randint(1, 5)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You compliment the gargoyle for its hot, well cut muscles."
                "The gargoyle shakes his head, but you notice his breathing is shallower and faster."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You slip in close to the gargoyle and press your body close against him, your bulge grinds against the gargoyle’s crotch area."
                "The gargoyle roars and grips its loincloth, the outline of the gargoyle’s erection grows more visible."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You blow a kiss at the enemy gargoyle."
                "The gargoyle roars and grips its loincloth, the outline of the gargoyle’s erection grows more visible."
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You compliment the gargoyle for its hot, well cut muscles."
                    "The gargoyle ignores your moves, and counters with a powerful punch."
                elif Random == 2:
                    "You slip in close to the gargoyle and press your body close against him, your bulge grinds against the gargoyle’s crotch area."
                    "The gargoyle is enraged! It grabs you by the arm and throws you against the wall with a powerful spin."
                elif True:
                    "You blow a kiss at the enemy gargoyle. "
                    "The gargoyle feels nothing, and lets out an ear piercing screech. "
            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                if Map.caj3g == 1:
                    jump battle_gargoyle_sex0
                if Map.ca18garg == 0 and Map.ca3garg == False:
                    jump battle_gargoyle_win
                label battle_gargoyle_sex0:
                    "The gargoyle lumbers slowly towards you."
                    "His face is flush red and his hard cock slips out from his slit pulling along a long stream of pre-cum."
                    "You keep your guard up ready for its next attack."
                    "Then with a loud thud the gargoyle gets on all four."
                    e 0 "What is this?"
                    "Gargoyle" "You win… you...stronger… give… mercy… give… heat."
                    "The horny gargoyle turns around and presents its ass to you."
                    menu:
                        "Mate him" if True:
                            if persistent.CG_gargoyle_win == True:
                                $ persistent.CG_gargoyle_win = False
                            jump battle_gargoyle_sex
                        "Leave" if True:
                            if Map.caj3g == 1:
                                "You get a gleaming moss and 300 EXP."
                                $ jane_inv_M.take(moss)
                                $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                                $ Map.caj3g = 0
                                jump Cave_map_ferryman
                            if Map.ca3garg:
                                "The ground was strewn with gleaming moss that fell from the gargoyle."
                                "You think they will be useful."
                                "You get a gleaming moss and 300 EXP."
                                $ jane_inv_M.take(moss)
                                $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                                $ Map.ca3garg = False
                                scene cave 1 with dissolve
                                "Now you can read the rest of the text in peace."
                                "Guided by the courage of our fallen who fought to find their freedom in the Kingdom of Aplistia."
                                "The rest of the text is unreadable."
                                e 13 "A kingdom? This place doesn’t look like it's been inhabited in so long."
                                e 1 "Could Flo be over there?"
                                $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
                                $ PPEXP = 50*Zalt.A_exp_lv
                                "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                                $ Map.ca3 = 4
                                jump Cave_map
                            jump Cave_map
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
            "You run away."
            hide screen simple_stats_screen
            hide screen battle_menu
            hide screen battle_skill
            hide screen battle_item
            if Map.caj3g == 1:
                jump Cave_map_ferryman
            jump Cave_map
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_gargoyle_win
        $ Random = renpy.random.randint(1, 5)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The gargoyle smashes its fist into the ground, tall protruding rock spikes sprout out from the earth and slam into you."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(25, 45)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The gargoyle smashes its fist into the ground, tall protruding rock spikes sprout out from the earth and slam into you."
        elif Random == 2:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The gargoyle casts a spell in an unknown language."
                "A stone spike pierces through your shadow, you’re caught off guard and the attack cuts through your arm. "
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 45)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The gargoyle casts a spell in an unknown language."
                "A stone spike pierces through your shadow, you’re caught off guard and the attack cuts through your arm. "
        elif Random == 3 or Random == 4:
            "The gargoyle stomps its feet, and green moss spreads outwards from beneath it."
            "Blue flowers appear instantaneously on top of the moss."
            "You raise your sword in front of your face, ready to guard against what will happen next."
            "The flowers explode and the air is polluted by a powerful and intoxicatingly sweet smell."
            "The smell arouses you, and you feel your cheeks warm up. "
            $ wolf_damage = renpy.random.randint(6, 12)
            $ Zalt.lust += wolf_damage
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The enemy leaps into the air, and lands a powerful kick that breaks through your defenses."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 45)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The enemy leaps into the air, and lands a powerful kick that breaks through your defenses."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1





    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_gargoyle_win
        elif True:

            jump battle_gargoyle_win

    elif Zalt.hp <= 0:
        jump battle_gargoyle_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_gargoyle_lose
    elif True:
        jump battle_gargoyle_loop


label battle_gargoyle_win:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_small_end.ogg" noloop
    pause 1
    hide gargoyle with slow_dissolve

    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    if Map.caj3g == 1:
        "The gargoyle staggers backwards and falls to its knees."
        "Panting heavily the gargoyle slashes the ground spraying dirt and dust to obscure your view."
        "Once it clears the gargoyle is no more."
        "The gargoyle has escaped."
        "Only the ground was strewn with gleaming moss that fell from the gargoyle."
        "You think they will be useful."
        "You get a gleaming moss and 300 EXP."
        $ jane_inv_M.take(moss)
        $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        $ Map.caj3g = 0
        jump Cave_map_ferryman
    if Map.ca18garg0:
        if Map.ca18garg == 0:
            $ Map.ca18garg = Map.ca18garg + 1
            $ wolf_hp = wolf_max_hp
            $ wolf_lust = 0
            "The first gargoyle’s defeat enrages the second one. He swoops in and claws at your chest."
            "You successfully block the attack with your sword."
            e 0 "Bring it!"
            jump battle_gargoyle_loop
        if Map.ca18garg == 1:
            "You get two gleaming moss and 600 EXP."
            $ jane_inv_M.take(moss,2)
            $ Zalt.exp = min(Zalt.exp+600, Zalt.maxlv*250+100*(Zalt.maxlv-1))
            $ Map.ca18 = 4
            $ Map.ca19 =1

            $ Zalt.A_exp = Zalt.A_exp + 100*Zalt.A_exp_lv
            $ PPEXP = 100*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            jump Cave_map

    $ jane_inv_M.take(moss)
    $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    if Map.ca3garg:
        $ Map.ca3garg = False
        scene cave 1 with dissolve
        "Now you can read the rest of the text in peace."
        "Guided by the courage of our fallen who fought to find their freedom in the Kingdom of Aplistia."
        "The rest of the text is unreadable."
        e 13 "A kingdom? This place doesn’t look like it's been inhabited in so long."
        e 1 "Could Flo be over there?"
        $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
        $ PPEXP = 50*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.ca3 = 4
        jump Cave_map
    jump Cave_map
    return

label battle_gargoyle_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    hide gargoyle with dissolve

    stop music
    if persistent.CG_gargoyle_lose == True:
        "Do you want to skip the scene?"
        menu:
            "Yes" if True:
                "The gargoyle walks off and leaves you in your spot for the rest of the night."
                "Your only company are the miscellaneous bugs that crawl around you, sometimes even crawling across your face, the only comfort is that you can’t feel anything."
                "Once the pertification wears off and you slump onto the ground exhausted and naked."
                "You pick up your gear and drag yourself out of the cave."
                "Thankful that you survived."

                if Time.hours >=6:
                    $ Time.days = Time.days+1
                    $ Time.hours = 6
                    $ Time.mins = 30
                elif True:
                    $ Time.hours = 6
                    $ Time.mins = 30

                $ Zalt.hp = min(Zalt.hp+Zalt.maxhp/2, Zalt.maxhp)
                $ Zalt.mp = min(Zalt.mp+Zalt.maxmp/2, Zalt.maxmp)
                if jane_inv.qty(coin) != None:
                    $ qty = int(jane_inv.qty(coin)*0.2)
                    $ jane_inv.drop(coin,qty)
                $ Zalt.cor = min(Zalt.cor+2,100)
                $ Zalt.Dungeon_leave = True
                if Map.caj3g == 1:
                    $ Map.caj3g = 0
                    jump Cave_map_ferryman
                if Map.ca3garg:
                    $ Map.ca3garg = False
                if Map.ca18garg0:
                    $ Map.ca18garg0 = False


                jump Cave_map
            "No" if True:
                pass
    "The gargoyle misses a punch and ends up accidentally smashing the ground."
    "You bring down your sword upon the creature’s head, but an earth pillar bursts out from the ground and knocks the sword out of your hands."
    hide gargoyle with dissolve
    "Losing your footing you fall backwards; the gargoyle tackles you to the ground."
    "His hands cling onto your shoulders tightly as he spins you across the ground. "
    "Every time you hit the ground more and more of your energy is sapped away, leaving you stunned."
    "The final toss forces you onto the ground with the gargoyle pinning you down by the shoulders."
    "He slams his body on top of you, the sheer weight of his form forces the breath out of your lungs."
    "A deep rumble emanates from his chest right before he lifts you off the ground, and bear hugs you tightly."
    scene black
    show garg lose1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos -0.8 ypos 0
        zoom 1.2
        linear 20.0 xpos 0 ypos -250
    e 0 "Ahhh!"
    "A sharp, twisting pain spreads from your hands as you struggle to break free from the gargoyle’s hold."
    "The gargoyle lets out a high-pitched screech and squeezes its biceps even tighter locking your hands completely. "
    "He raises his razor-sharp claws to your throat and draws an imaginary line across your throat. "
    "Gargoyle" "Shh."
    "The gargoyle opens his mouth and lets his long-wet tongue brush against your cheeks."
    "You shudder and your legs tremble from the warm spot growing warmer and brushing up against your rump."
    e 0 "Stop, what are you?"
    show garg lose1 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "There’s no strength left inside you to struggle."
    "The gargoyle lets out a guttural laugh and starts to fondle your right pec in one hand while running his fingers along your sides with the other."
    "Your face twists and contorts as the creature man handles your body."
    "His fingers dig deep into your fur, combing them with his sharp claws."
    "His right hand slides along your firm abs. Your lower jaw trembles from the touch. "
    "Any mental resistance proves futile as your body is a slave to the meaty yet nimble fingers of the gargoyle."
    "Through your bound hands pressing against the gargoyle’s abdomen, you are surprised that his body is very much fleshy like yours."
    "The gargoyle coos into your ear again and with a swipe of his hand cuts off your loincloth."
    show garg lose2 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Your semi-hard cock flops out, and you let out a soft gasp."
    "Gargoyle" "Mmm."
    "The vibration of the gargoyle’s chest echoes through your back, your cheeks blush in response."
    "His voice hints that he likes what he sees. "
    "The hand that holds your right pec travels south while with the other hand cups your balls and fondles them."
    "His wide palm is cold to the touch."
    "You moan as he slides your testicles from one finger to another. "
    "Your member starts to stiffen and you feel yourself getting looser and hotter."
    "Gargoyle" "Warm...good. "
    "Gargoyle" "I want more!"
    e 0 "Wha-"
    show garg lose3 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    e 0 "What the hell are you doing?"
    "The gargoyle sweeps his arm beneath your butt and hoists you off your feet."
    "His other hand holds your upper limbs in place, all you can do is flail your legs in the air."
    "Your captor laughs and bounces you with his one arm like you weigh nothing."
    "Every time your butt falls slightly you feel the gargoyle’s rock hard erection smack against your buttcrack. "
    "The gargoyle presses you close against his bare chest. His dragon like head nudges against your throat."
    "He’s breathing heavily against your neck. His breath is hot and smells of the earth."
    with flashbulb
    show garg lose4 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Without warning, the gargoyle plunges his entire dick up your ass"
    "The surging pain erupting from your ass forces your eyes to close. "
    "Your toes curl and thrash about but that only causes you to plunge the gargoyle's cock deeper inside you."
    "Your chest heaves as you struggle to get used to the throbbing dick impaling your butthole."
    "His warm pre fills the walls of your butthole, lubricating his cock, and making it easier for you to take in his whole length."
    "Gradually, the pain melts away and you’re swimming in blissful euphoria."
    "Your cock hardens, and drops of pre dribble along your shaft. "
    "Your soft whimpers are accompanied by the slapping sounds of the gargoyle’s cock pulling out and slamming back inside you."
    show garg lose5 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Gargoyle" "Yes, wolf tight!"
    "The gargoyle thrusts his cock inside you relentlessly."
    "Leaving you in a daze as he rides your firm ass like a wild beast in heat."
    "Your jaw hangs open and you yelp with every hard thrust, not wanting the fullness inside your ass to stop. "
    "Gargoyle" "Good wolf. Make more sounds."
    "Your own cock bobs up and down spraying your pre all over the ground."
    "His hold on your hands and on your calves tightens. There’s no escape."
    "Every time his dickhead brushes against your spot, you throw your head back and whine and groan."
    "Your lustful sounds invigorates the gargoyle."
    "His mouth clamps onto your neck and bites down as he fucks your ass vigorously."
    e 0 "Fuck! Fuck!"
    "You feel the pressure building inside your balls. You’re close."
    "Gargoyle" "Gah!"
    "The gargoyle grits his teeth and lets out a muffled roar as his cock erupts and hot cum fills your insides."
    "The sheer force of his ongoing cumshot brings a tear to your eye. "
    "You can’t bear it any longer, your toes curl up and you cum just as hard. "
    with flashbulb
    e 0 "Cumming!"
    with flashbulb
    show garg lose6 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "A streak of white hot cum fires from your cock, and splatters a good feet away from the two of you."
    "Your entire body shudders as streams of cum flow out of your ass, unable to hold in the torrential amounts of cum plugging up your butt."
    "It feels like an eternity before the both of you finally stop cumming."
    "Your hot naked bodies press against each other, and you both pant heavily."
    "The buzz of your orgasm must still be lingering because you can’t feel your toes."
    "My toes?"
    show garg lose7 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "The gargoyle pulls his member out of your ass, you imagine his cock to be completely wet with cum judging from how much he unloaded inside you."
    e "What?"
    "A tingling sensation spreads from your toes to the rest of your foot."
    "You glance downwards and to your horror your feet are turning into stone."
    "Despite struggling to move your feet, they would not move an inch."
    "Gargoyle" "You,stone."
    "You struggle against the gargoyle’s solid grip, but your efforts are fruitless, leaving you with only burn marks on the joints of your wrists."
    "All you can do is watch in horror as the petrification continues."
    show garg lose8 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    e 0 "No, no, no. Don’t do this!"
    "Gargoyle" "Shh. No. Turn to stone. Good."
    "The petrification spreads faster until your entire leg turns into an ashen grey. "
    "Your ability to speak is sucked up by the impending fear spreading across your body."
    "Gargoyle" "Warm...Cold."
    show garg lose9 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "Your pupil pulsates and your heart races."
    "You’re literally screaming in terror inside your head, how you beg to the Divine Beings this would not be the end."
    "In just minutes the petrification consumes most of you, and you’ve lost all senses from below your neck."
    "The gargoyle continues to cradle your stoned body like a precious pet, patting your stone rump."
    "The entire process appears to speed up after making past your heart."
    show garg lose10 with slow_dissolve:
        xpos 0.08 ypos 0
        zoom 1
    "You can only whimper like a scared pup as the rest of you turns to stone."
    hide garg lose10 with slow_dissolve
    "..."
    "......"
    "Despite being turned to stone, your mind still works."
    "The gargoyle could easily smash you into bits and that would be the end of it, but instead he sets you on the ground."
    "Gargoyle" "Warm,fuck,good."
    "You hear the gargoyle runs one sharp claw across your stone face. Then he plants a kiss on your cheek."
    "And you hear that he grabs your satchel on the ground,Then you hear his chew."
    "Gargoyle" "Delicious."
    "The gargoyle walks off and leaves you in your spot for the rest of the night."
    "Your only company are the miscellaneous bugs that crawl around you, sometimes even crawling across your face, the only comfort is that you can’t feel anything."
    "Once the pertification wears off and you slump onto the ground exhausted and naked."
    "You pick up your gear and drag yourself out of the cave."
    "Thankful that you survived."

    if Time.hours >=6:
        $ Time.days = Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
    elif True:
        $ Time.hours = 6
        $ Time.mins = 30

    $ Zalt.hp = min(Zalt.hp+Zalt.maxhp/2, Zalt.maxhp)
    $ Zalt.mp = min(Zalt.mp+Zalt.maxmp/2, Zalt.maxmp)
    $ qty = int(jane_inv.qty(coin)*0.2)
    $ jane_inv.drop(coin,qty)
    $ Zalt.lust = 0
    $ persistent.CG_gargoyle_lose = True
    $ Zalt.cor = min(Zalt.cor+2,100)
    $ Zalt.Dungeon_leave = True
    if Map.caj3g == 1:
        $ Map.caj3g = 0
        jump Cave_map_ferryman
    if Map.ca3garg:
        $ Map.ca3garg = False
    if Map.ca18garg0:
        $ Map.ca18garg0 = False

    jump Cave_map

label battle_gargoyle_sex:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    hide gargoyle with dissolve
    if persistent.CG_gargoyle_win == True:
        "Do you want to skip the scene?"
        menu:
            "Yes" if True:
                if Map.caj3g == 1:
                    "Not wanting to take your chances once he wakes up you grab your things, and cut off a piece of the moss growing on the gargoyle’s wings."
                    "You get a gleaming moss and 300 EXP."
                    $ Zalt.lust = 0
                    $ jane_inv_M.take(moss)
                    $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                    $ Map.caj3g = 0
                    jump Cave_map_ferryman
                if Map.ca18garg0:
                    $ Map.ca18garg0 = False
                    "You get two gleaming moss and 600 EXP."
                    $ jane_inv_M.take(moss,2)
                    $ Zalt.exp = min(Zalt.exp+600, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                    $ Map.ca18 = 4
                    $ Map.ca19 =1

                    $ Zalt.A_exp = Zalt.A_exp + 100*Zalt.A_exp_lv
                    $ PPEXP = 100*Zalt.A_exp_lv
                    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                    jump Cave_map
                "Not wanting to take your chances once he wakes up you grab your things, and cut off a piece of the moss growing on the gargoyle’s wings."
                "You get a gleaming moss and 300 EXP."
                $ Zalt.lust = 0
                $ jane_inv_M.take(moss)
                $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))

                if Map.ca3garg:
                    $ Map.ca3garg = False
                    scene cave 1 with dissolve
                    "Now you can read the rest of the text in peace."
                    "Guided by the courage of our fallen who fought to find their freedom in the Kingdom of Aplistia."
                    "The rest of the text is unreadable."
                    e 13 "A kingdom? This place doesn’t look like it's been inhabited in so long."
                    e 1 "Could Flo be over there?"
                    $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
                    $ PPEXP = 50*Zalt.A_exp_lv
                    "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                    $ Map.ca3 = 4
                    jump Cave_map
                jump Cave_map
            "No" if True:
                pass
    scene black
    show garg win1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos -0.8 ypos 0
        zoom 1.2
        linear 20.0 xpos 0 ypos -250
    "This proposition has never happened before. "
    "The gargoyle lets out a weak groan and raises its tail to expose its tight looking butthole."
    "You cannot deny the sight before you looks tantalizing."
    "Sheathing your sword away, you put your torch down to claim your prize."
    "You strip off your loincloth and press your body against the gargoyle’s back."
    "Gargoyle" "Ah!"
    "The gargoyle’s wings bend aside to make way for your entire form and he lets out a guttural whine."
    show garg win1 with slow_dissolve:
        xpos 0.05 ypos -0.02
        zoom 1.05
    e 0 "Come here, you. You want this don’t you?"
    "You hold the gargoyle by the neck and turn him towards your face."
    "Gargoyle" "Yes… warm good."
    e 0 "Warm huh, you mean you want my warm cock inside you? Filling you?"
    "The gargoyle whines louder."
    "You reach down and grasp the warm phallic meat between the gargoyle’s legs."
    "His member fills your entire hand and throbs excitedly as you rub it slowly."
    "Gargoyle" "More warm… better… me like warm."
    e 0 "Oh I will make you feel warm. Feel that rubbing against you?"
    "You slide your cock along the gargoyle’s taint."
    "Slowly, letting him feel the hardness of your dick press against his skin."
    "Gargoyle" "Fuck… give me… warm cock!"
    e 0 "Shh, shh. I’m going to take my time with you."
    "With a beastly growl you grip the gargoyle’s cock tightly making him whimper like a beast in heat."
    "The beast tries to turn its head more towards you, you both lock eyes, your lips almost touching."
    "You try to position yourself just right but your dick slips along his ass crack smearing his hole with your pre."
    "Releasing his dick you grab your pulsating erection and guide it into the gargoyle’s waiting hole."
    "Gargoyle" "Gah… thick!"
    show garg win2 with slow_dissolve:
        xpos 0.05 ypos -0.02
        zoom 1.05
    "The gargoyle closes his eyes and groans heavily."
    "Small lines of saliva drip from his mouth as you push your cock deeper inside him."
    "His tight ass resists your meaty club."
    "You grunt and carassess the gargoyle by the neck and whisper into his ear."
    e 0 "Don’t fight it, just breathe and take it in big boy."
    "The gargoyle lets out a deep groan but you feel your hard member pushing in deeper inside him."
    e 0 "Mmm, yeah you have a hot tight ass. You feel that inside you?"
    "Gargoyle" "Yes...warm good."
    "You hear the sound of dribbling pre splashing onto the cave floor as you continue to jerk the gargoyle’s cock."
    "Your hand reaches down and cups his dickhead while smearing the pre all over your fingers and along his hard shaft."
    "The gargoyle closes his mouth and grits his teeth but you can still hear his muffled moans."
    "You pull the gargoyle back by the neck as you press your cock deeper inside him."
    "Immense pressure builds inside your balls. All you want is to fuck the gargoyle as hard as you can."
    show garg win3 with slow_dissolve:
        xpos 0.05 ypos -0.02
        zoom 1.05
    "You take hold of the gargoyle’s neck and pound his ass relentlessly."
    "The insides of his ass are lubed up by your leaking cock and spraying pre inside him."
    "Your chest burns with the heat of lust, pounding and pounding the gargoyle’s ass."
    "The way his asscheeks jiggle with every thrust and the gargoyle’s earth-shaking moans turns you on."
    "Heat radiates from your joined bodies warming the gargoyle’s cold body beneath you."
    "His dick in your hands is stiff as a rock pumping a pool of pre on the floor."
    "Gargoyle" "Me want to cum!"
    "Gritting your teeth the gargoyle’s ass clamps tighter on your dick."
    e 0 "Take it, Take it!"
    "Gargoyle" "Yes! Warm!"
    "Your thrusts start to slow and your knees buckle."
    e 0 "Fuck, I’m close!"
    "Gargoyle" "Gahhhh!"
    e 0 "I’m cumming!"
    with flashbulb
    "The gargoyle roars into your ears as both of you release your seed."
    with flashbulb
    show garg win4 with slow_dissolve:
        xpos 0.05 ypos -0.02
        zoom 1.05
    "Bright lights flashes before your eyes and the entire room spins while wave after wave of cum fills the gargoyle’shole."
    "Your hand feels sticky with the gargoyles cum dribbling onto it."
    "And soon you feel your hands are becoming numb."
    e 0 "Wahh, wow."
    "You quickly throw his semen away from your hand."
    "The gargoyle groans and closes his eyes. "
    "Gently, you set his head on the ground and pull your deflated cock from his butt."
    hide garg win4 with slow_dissolve
    "Gargoyle" "Warm…"
    "Through the light of your torch you can see the gargoyle smiling."
    "Not wanting to take your chances once he wakes up you grab your things, and cut off a piece of the moss growing on the gargoyle’s wings."
    $ persistent.CG_gargoyle_win = True
    if Map.caj3g == 1:
        "You get a gleaming moss and 300 EXP."
        $ Zalt.lust = 0
        $ jane_inv_M.take(moss)
        $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        $ Map.caj3g = 0
        jump Cave_map_ferryman
    if Map.ca18garg0:
        $ Map.ca18garg0 = False
        "You get two gleaming moss and 600 EXP."
        $ jane_inv_M.take(moss,2)
        $ Zalt.exp = min(Zalt.exp+600, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        $ Map.ca18 = 4
        $ Map.ca19 =1

        $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
        $ PPEXP = 50*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump Cave_map
    if Map.ca3garg:
        $ Map.ca3garg = False
        scene cave 1 with dissolve
        $ Zalt.lust = 0
        "You get a gleaming moss and 300 EXP."
        $ jane_inv_M.take(moss)
        $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        "Now you can read the rest of the text in peace."
        "Guided by the courage of our fallen who fought to find their freedom in the Kingdom of Aplistia."
        "The rest of the text is unreadable."
        e 13 "A kingdom? This place doesn’t look like it's been inhabited in so long."
        e 1 "Could Flo be over there?"
        $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
        $ PPEXP = 50*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.ca3 = 4
        jump Cave_map

    jump Cave_map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
