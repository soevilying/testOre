label battle_bull:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new

    $ wolf_max_hp = 120
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 20

    $ Map.good_battle = True
    $ Battle.holyfcd = 0
    scene forest 3
    stop music
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')






    "A massive shadow blocks your path ahead."
    "A huge bull emerges from the fog brandishing his axe."
    "Bull warrior" "Outsider! I will break you!"
    "The bull swings his weapon at you."
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    jump battle_bull_loop


label battle_bull_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show bullw at center
    play music "<loop 4.6903>music/forest_fight_small.ogg"






    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False

        if res == "Holy Fist":
            $ red_damage = renpy.random.randint(Zalt.MATK*2, int((Zalt.MATK*2.5)+10))
            $ wolf_hp -= red_damage
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            $ Random = renpy.random.randint(1, 3)
            $ Battle.holyfcd = 3
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
            jump battle_bull_lose
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
                "His will to fight is broken, he only wants to pleasure you."
                menu:
                    "Fuck him" if Zalt.lust >=40:
                        jump battle_bull_sex
                    "Leave" if True:
                        "You choose to leave the bull alone."
                        "As you walk away you can hear the bull’s lustful moans and the squishy sound when someone jerks off."
                        "You get 1 bundle of fur and 100 EXP."
                        $ jane_inv_M.take(bull_fur)
                        $ Zalt.exp = min(Zalt.exp+100, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                        jump forest_map_3
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
            $ Random = renpy.random.randint(1, 2)
            if Random == 1:
                "You run away."
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item
                hide slime
                jump forest_map
            elif True:
                "Escape failed!"
                pass
        elif True:
            pass

        if wolf_hp <= 0:
            jump battle_bull_win
        $ Random = renpy.random.randint(1, 6)
        if Random <= 3:
            $ wolf_damage = renpy.random.randint(15, 30)
            $ Zalt.lust += wolf_damage
            "The bull warrior's musk is earthy and potent."
            "Your crotch warms up."
            "Bull warrior" "You like that, hmmm? Submit now and I'll give you something fun!"
        elif True:
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
            jump battle_bull_win
        elif True:

            jump battle_bull_win

    elif Zalt.hp <= 0:
        "The enemy bull’s fist slams hard onto your gut."
        "Your body spasms for a second and you are left wobbling on your feet."
        jump battle_bull_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_bull_lose
    elif True:
        jump battle_bull_loop


label battle_bull_win:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_small_end.ogg" noloop
    pause 1
    "Bull warrior" "Egh..!"
    hide bullw with slow_dissolve

    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    "You knock the bull out with the butt of your weapon."
    "You cut off some of his hair with your sword."
    "You get 1 bundle of fur and 100 EXP."
    $ jane_inv_M.take(bull_fur)
    $ Zalt.exp = min(Zalt.exp+100, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    jump forest_map_3

    return
label battle_bull_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    hide bullw with dissolve
    if Foe.bullw == True:
        "Do you want to skip the scene?"
        menu:
            "Yes" if True:
                scene black with dissolve
                "......"
                scene forest 3 with dissolve
                "When you wake up again, you find that some coins is missing."
                "You smile grimly, glad that you're still alive."
                "After cleaning yourself up, you start over again."
                if jane_inv.qty(coin) != None:
                    $ qty = int(jane_inv.qty(coin)*0.2)
                    $ jane_inv.drop(coin,qty)
                $ Zalt.lust = 0
                $ Zalt.hp = 1
                jump forest_map_3
            "No" if True:
                pass
    elif True:
        pass
    "You feel the bull gripping you tightly by the head and swings you around so you would not face him."
    "He plunges his arms under your right armpit and pulls you onto the ground."
    "His massive body falls with a heavy thud."
    "He spreads one of your legs over his thigh, giving him full view of you."
    "Bull warrior" "You smell so good wolf."
    "[name]" "Ngh, let me go!"
    "His meaty fingers wrap around your neck."
    "You can still talk but you know he’s letting you."
    "If he wants he can break you right here and now."
    "Bull warrior" "Shh, it’s been so long since I had a nice fuck session."
    "Bull warrior" "Be a good pup and let me have my fun."
    "He releases his hold on your neck and nuzzles his nose close to your neck."
    "Your face is so close to his you can feel his hot breath tickling your neck and climbing up towards your ear."
    "The bull nibbles on your ear and you groan."
    "[name]" "No.... I mustn't...."
    "The musk he radiates is so pungent your nose stings from its smell."
    "You try to resist but your body betrays you."
    "Your crotch is getting warmer and harder by the minute."
    "Bull warrior" "Let's get a little more comfortable."
    scene black
    show bull lose1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos 0.1 ypos 0
        zoom 1.2
        linear 100.0 xpos -50 ypos -800
    "The bull rips off your loincloth, making your hardon spring free."
    "Your cock is hot and pulses feverishly,stimulated by the bull’s powerful scent."
    "He grabs your manhood and squeezes it tightly."
    "He places his thumb over your dickhead and presses into your dickslit."
    e "What are you- Argh!"
    show bull lose1 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "Your legs try to squirm but they are held down by the bull’s arms."
    "Bull warrior" "Hah! I love it when you scream."
    show bull lose2 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "Your eyes widen in shock as the bull’s cock slides free from his loin cloth and rises to its full girth."
    "Beads of precum cascade from the tip of the bull’s cock."
    "He grabs hold of his dick and yours like a bundle of sticks."
    "Bull warrior" "Look at all that meat."
    e "What the fuck is that?"
    "Bull warrior" "Take a good look little wolf, cause it's going to be in you soon."
    e "No, no. I can’t fit all that!"
    "Bull warrior" "I’ll make it fit."
    "The bull releases his hold on your member and shakes his leaking member around your hole."
    "His movements are clumsy, and his pre doesn’t help."
    "Every few seconds you feel your taint getting slammed by the bull’s wet dickhead before it slips away."
    "Bull warrior" "Fuck this!"
    with flashbulb
    show bull lose3 with dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "He holds his dick right over your hole and pushes through."
    "Your ass twitches and burns."
    e "Fu-AHHH! It’s too big!"
    "Bull warrior" "Fuck, your hole is tight."
    "You feel an immense explosion of pain like your whole body is getting torn in two."
    "His cock is so deep inside you that you can feel the bull’s apple sized balls slapping against your butthole."
    "The bull is panting heavily over your shoulder."
    "His cock continues to gush pre cum inside you."
    "Bull warrior" "Argh yea, hug my cock with your hole."
    "He plunges a kiss into your mouth, overpowering you with his thick tongue."
    show bull lose4 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "The pain you felt gives way to waves of pleasure."
    "Your whole body loosens up letting the bull’s dick slide into you with ease."
    "He pulls his dick half way out and rams the whole shaft back inside you."
    "The bull’s strong arms holds you in place as he begins to gyrate his hips."
    e "Ahhhh."
    "With every hump he shoots more pre inside you."
    "His grip on you is so strong you can’t even squirm."
    with flashbulb
    "He rides your ass faster and faster."
    "Bull warrior" "Yeah, squeeze my dick with your tight ass!"
    "You spew pre from your still throbbing cock all over your stomach."
    "You feel like your body is not your own anymore, it’s his."
    "Before you know it you are riding the bull’s massive club,{p}wanting more, wanting him to cum in you and conquer you."
    e "Fuck! My insides are burning!"
    "Your pleas go unnoticed."
    "The bull keeps fucking you harder and harder."
    "He eyes you with one eye open, he grins watching your face contort in different expressions of lust."
    "Your cock aches painfully, desiring desperately to release its load."
    e "CCC- CUMMING!"
    with flashbulb
    show bull lose5 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "A hot stream of cum sprays from your cock."
    "Coating the grassy field with your seed."
    "Some of it dribbled all over the bull’s balls."
    "Bull warrior" "Fuck! I can’t hold it in anymore!"
    "The bull’s pumping starts to slow."
    "His balls press up close against your ass and you feel the already thick shaft expand inside your ass."
    with flashbulb
    with flashbulb
    show bull lose6 with slow_dissolve:
        xpos 0.07 ypos 0
        zoom 1
    "The bull unloads his cum inside you."
    "As you scream in pleasure your cock erupts again and fires a cumshot on the bull’s face."
    "Ropes of cum fill you to the breaking point."
    "Your try to hold it all in but its too much cum."
    "Streams of cum leaks out of your hole like an overfilled cup."
    "Panting, the bull kisses you on the cheeks and pulls you off of his dick."
    "Trails of cum leak from your ass and splatter over the bull’s cock."
    "He drops you onto the ground and gets on his feet."
    hide bull lose6 with slow_dissolve
    scene forest 3 with slow_dissolve
    "Everything aches especially your twitching butthole."
    "Your heart aches from all sorts of emotions,anger,humiliation,lust{p}but mostly you feel empty without the bull’s dick."
    "The large bull steps on your back, his cock still dripping cum on your naked body."
    "He crouches over you and stuffs his middle finger into your ass."
    "You yelp loudly."
    "He pulled his finger out with a glob of cum on it and licked it clean."
    "Bull warrior" "That was a good fuck."
    "Bull warrior" "Come back again wolf, I’ll gladly pound that ass."
    "You hear him walk away, but you are too tired to catch up to him."
    "Your eyelids are getting heavy..."
    scene black with vslow_dissolve
    "...{w}..."
    scene forest 3 with vslow_dissolve
    "When you wake up again, you find that some coins is missing."
    "You smile grimly, glad that you're still alive."
    "After cleaning yourself up, you start over again."
    $ Foe.bullw = True
    if jane_inv.qty(coin) != None:
        $ qty = int(jane_inv.qty(coin)*0.2)
        $ jane_inv.drop(coin,qty)
    $ Zalt.lust = 0
    $ Zalt.hp = 1
    $ persistent.CG_bull_lose = True
    jump forest_map_3
    return
label battle_bull_sex:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    hide bullw with dissolve
    "You unsheath your loincloth letting your plump semi-hard member sway against your thighs."
    "The bull crawls towards you and nuzzles your scrotum."
    "His hot breath feels good against your cock."
    "Bull warrior" "Claim me... champion."
    "All he wants is your manhood inside him, his hunger for you burns within his eyes."
    "You let him worship your manhood."
    "From brushing against your balls, the bull laps your balls eagerly."
    "The gentle strokes of his tongue feels so good your dick rises to its full length."
    "[name]" "Give me that ass!"
    scene black
    show bull win1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos 0 ypos 0
        zoom 1.5
        linear 20.0 xpos 0 ypos -1000

    "You shove the bull by the shoulder."
    "His massive frame falls back onto the ground with ease, like pushing a pillow."
    "The way his hefty pecs rise and fall tell you he’s breathing heavily."
    "His hard cock lies firmly against his abs."
    "Its club like size could knock someone out if they are slapped with enough force."
    show bull win1 with slow_dissolve:
        xpos 0.2 ypos -0.13
        zoom 0.86
    "[name]" "Well,what are you waiting for?"
    "[name]" "I said give me your ass!"
    "The bull gulped but he obeys."
    "He raises his legs up high until his hole just grazes your scrotum."
    "[name]" "I like what I’m seeing."
    "You approach him and hold him by the thighs, resting your hard cock on top of his hole."
    "Your dickhead only inches away from touching the bull’s bronze balls."
    "[name]" "Yeah, you like that don’t you, bull?"
    "Bull warrior" "Yes... please... it feels so warm... I need you inside me."
    "[name]" "You’re a bottom virgin aren’t you?"
    "[name]" "I can feel how tight your hole is just by rubbing against it."
    "The bull gasps, he puts on a strong face, but his pulsating dick betrays him."
    "[name]" "Take it, big boy!"
    "You press your glans against his hole. Just as the tip breaks forces itself in, the bull screams."
    show bull win2 with slow_dissolve:
        xpos 0.2 ypos -0.13
        zoom 0.86
    "Bull warrior" "Ahhhh! Yes! Pound my ass with your cock!"
    "You are taken aback by the bull’s sudden change in intensity, but a part of you feels energized by it as well."
    "[name]" "Yeah! Take it you muscle bound ass."
    "The bull as though on command loosens the muscles around his anus letting you slide your glans further inwards."
    with flashbulb
    show bull win3 with dissolve:
        xpos 0.2 ypos -0.13
        zoom 0.86
    "The bull moans and gasps as you slam the rest of your dick inside him."
    "His face melts feeling your hot dick inside him."
    "You growl and toss your head into the air."
    "Your cock tingles as the muscles of the bull’s anus grips around the shaft."
    "Bull warrior" "Yes! More! More!"
    show bull win4 with slow_dissolve:
        xpos 0.2 ypos -0.13
        zoom 0.86

    "Pulling your dick part way you thrust it all the way in as hard as you can."
    "Bull warrior" "Harder! Yes, don’t slow down on me, outsider!"
    "You gyrate your hips until you reach a familiar rhythm."
    "Every thrust of your cock sends jolts of ecstasy throughout your body."
    "You feel like every fiber of your body is turning into butter."
    "As you fuck the bull, your tongue falls out as you pant heavier."
    "The view in front of you is not too bad either, every time you slam your dick inside the bull his pecs would jiggle."
    "Bull warrior" "Fuck me,yes,ohhh."
    "Both of your bodies are burning up with passion."
    "The lustful bull sprays pre all over his face and chest."
    "You can feel your limits reaching its peak as well."
    if Zalt.end <= 6:
        "[name]" "RARRGGGHHH!"
        "You can’t hold it in anymore."
        with flashbulb
        show bull win5a with slow_dissolve:
            xpos 0.2 ypos -0.13
            zoom 0.86
        "Your cock spews its load deep inside the bull, every part of your body tenses and goes numb for what feels like minutes."
        "Ropes of hot cum fills the bull’s hole."
        "Bull warrior" "Moo!"
        hide bull win5a with dissolve
        scene forest 3 with dissolve
        "Panting heavily you pull out your soft dick from the bull’s hole."
        "A string of cum trails along connecting your glans to his hole."
        "The bull is unable to climax."
        "He turns his attention to his own cock and starts to jerk himself off."
        "You take the chance to walk away, he will be too preoccupied to be any trouble. "
        "You get 1 bundle of fur and 100 EXP."
        $ Zalt.lust = 0
        $ Foe.bullwin = True
        $ jane_inv_M.take(bull_fur)
        $ persistent.CG_bull_winA = True
        $ Zalt.exp = min(Zalt.exp+100, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        jump forest_map_3
    elif True:
        "Bull warrior" "Mooooooo!"
        with flashbulb
        show bull win5b with slow_dissolve:
            xpos 0.2 ypos -0.13
            zoom 0.86
        "The bull lets out an earth shattering roar as he cums all over himself."
        "He blasts thick creamy cum all over his face."
        "Its musky scent fills your nostrils."
        "His body shudders as he leaks cum all over himself."
        "[name]" "Fuck!"
        "The spastic movements of his anus tightens its grip around your cock."
        "You can’t hold it in anymore!"
        "[name]" "I’m cumming!"
        with flashbulb
        show bull win6b with vslow_dissolve:
            xpos 0.2 ypos -0.13
            zoom 0.86
        "Your thrusts begin to slow to a halt."
        "Clutching the bull’s thighs even tighter your cock spews its load deep inside the bull."
        "Every part of your body tenses and goes numb for what feels like minutes."
        "Bull warrior" "FUCK!"
        "The sudden blast of cum inside his rectum triggers the bull’s cock."
        "He cums once again all over himself. Some of it gets into his eye causing him to roar in pain."
        "Panting heavily you pull out your soft dick from the bull’s hole, a string of cum trails along connecting your glans to his hole."
        hide bull win5a with dissolve
        scene forest 3 with dissolve
        "The bull is too exhausted and collapses."
        "You take the chance to walk away."
        "He won’t be causing you trouble anytime soon."
        "You get 1 bundle of fur and 100 EXP."
        $ Zalt.lust = 0
        $ Foe.bullwin = True
        $ jane_inv_M.take(bull_fur)
        $ persistent.CG_bull_winB = True
        $ Zalt.exp = min(Zalt.exp+100, Zalt.maxlv*250+100*(Zalt.maxlv-1))
        jump forest_map_3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
