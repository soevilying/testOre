label battle_lizard:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    if Quest.bombn ==4:
        $ wolf_max_hp = 220
    elif True:
        $ wolf_max_hp = 150
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ Battle.holyfcd = 0
    $ Map.good_battle = True
    stop music








    jump battle_lizard_loop


label battle_lizard_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show lizardw at center
    play music "<loop 4.6903>music/forest_fight_small.ogg"





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
            jump battle_lizard_lose
        if res == "Flirt":
            $ Random = renpy.random.randint(1, 7)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You grope your groin and make a sexual comment to play with your spear."
                "The lizard is confused and breathing heavily."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You wink at the lizard and gesture with your finger in a seductive manner inviting him to come closer."
                "The lizard darts his tongue out with a lewd smile, you can tell he wants more."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You wiggle your butt, feigning innocence. "
                "He gasps loudly and grabs his groin as though trying to hide it from view."
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You grope your groin and make a sexual comment to play with your spear."
                    "The lizard growls angrily at you and swats his spear at you."
                elif Random == 2:
                    "You wink at the lizard and gesture with your finger in a seductive manner inviting him to come closer."
                    "He spits on the ground and angrily cuts the air with his dagger."
                elif True:
                    "You wiggle your butt, feigning innocence. "
                    "He ignores your seduction curses you."
            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                "The lizard warrior breathes heavily."
                "His arms sway to and fro. Your nose picks up the musky scent of perspiration and desire in the air. "
                if Quest.bombn ==4:
                    jump Nauxus_rite1
                "The lizard tosses his weapon to the ground and rushes towards you with his tongue flapping against his cheek like a rabid animal."
                "You counter his attack with the back of your sword, swinging it across his face. "
                "The lizard drops to the ground."
                menu:
                    "Fuck him" if True:
                        jump battle_lizrad_sex
                    "Leave" if True:
                        "You choose to leave the lizard alone."
                        "You get 1 lizard scale and 150 EXP."
                        $ jane_inv_M.take(lizard_scale)
                        $ Zalt.exp = min(Zalt.exp+150, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                        jump deepswamp
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
                hide lizardw
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item
                jump forest_map0
            elif True:
                "Escape failed!"
                pass
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_lizard_win

        $ Random = renpy.random.randint(1, 4)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The lizard cuts you with his dagger."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(25, 45)
                $ Zalt.hp -= wolf_damage
                "The lizard cuts you with his dagger. It burns deep into your flesh."
        elif Random == 2:
            "The lizard stares you down."
            "His forked tongue darts in and out, and he stabs his spear into the ground."
            "You watch him curiously, he leans against the spear, his hands wrap near the tip of the weapon."
            "He thrusts his hips forward, and your heart skips a beat."
            "He continues his seductive dance along his pole rendering you immobile."
            $ wolf_damage = renpy.random.randint(14, 24)
            $ Zalt.lust += wolf_damage
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The lizard plunges his spear into your arm."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(25, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The lizard plunges his spear into your arm."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1





    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_lizard_win
        elif True:

            jump battle_lizard_win

    elif Zalt.hp <= 0:
        jump battle_lizard_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_lizard_lose
    elif True:
        jump battle_lizard_loop


label battle_lizard_win:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    play music "music/forest_fight_small_end.ogg" noloop
    pause 1
    hide lizardw with slow_dissolve

    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    "With a powerful punch you knock the lizard off his feet."

    if Quest.bombn ==4:
        jump Nauxus_rite1
    "The lizard tosses his weapon to the ground and rushes towards you with his tongue flapping against his cheek like a rabid animal."
    "You counter his attack with the back of your sword, swinging it across his face. "
    "The lizard drops to the ground."
    "You get 1 lizard scale and 150 EXP."
    $ jane_inv_M.take(lizard_scale)
    $ Zalt.exp = min(Zalt.exp+150, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    jump deepswamp

    return
label battle_lizrad_sex:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    hide lizardw with dissolve
    if persistent.CG_lizard_win == True:
        "Do you want to skip the scene?"
        menu:
            "Yes" if True:
                "You pull out your cock from the lizard and muster enough energy to grab your things and leave."
                $ Zalt.lust = 0
                $ Foe.lizardwin = True
                "You get 1 lizard scale and 150 EXP."
                $ jane_inv_M.take(lizard_scale)
                $ Zalt.exp = min(Zalt.exp+150, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                jump deepswamp
            "No" if True:
                pass
    "You seize your chance and rush at him, your hands meet his and you both push one another for dominance. "
    "Neither side relents. The enemy lizards digs his foot deep into the ground as you push harder."
    "Lizard Warrior" "When I’m done with you, that sweet piece of ass of yours is going to be riding my cock till you learn to love it."
    "Lizard Warrior" "I’ll grind you good, until you’ll beg for more."
    e 0 "Do you ever shut up?"
    "Lizard Warrior" "I’ll shut you up with my cock in your mouth!"
    "Lizard Warrior" "You’re going to be my bitch you furry cock sucker."
    e 0 "Rargh!"
    "Mustering all the strength in your arm, you knock the lizard off his feet with a well timed knee to the gut. "
    "He’s knocked back, clutching his stomach."
    "You jump him and he topples onto the ground."
    "Lizard Warrior" "Ahh! Fuck you, wolf! You won’t get away with this! I’ll have your ass."
    "He struggles while on his back, throwing random punches that you dodge easily."
    "Lizard Warrior" "You’re no match for me!"
    e 0 "Ah, shut up!"
    "With a strong punch, the lizard is silenced."
    "In his groggy state he lets out weak hisses."
    e 0 "There, if you don’t run your mouth, you actually look fuckable."
    "You tear away the lizards loincloth and two thick members reveal themselves."
    "The lizard comes to his senses, and tries to grab you by the throat but you bat his hands away."
    "His dick twitches and the lizard groans."
    e 0 "My, my, for all your talk, you love it when someone treats you rough huh.This turns you on?"
    "You grab his dicks and squeeze them hard."
    "The lizard warrior bites down on his lip, and groans louder. "
    e 0 "I’m going to enjoy this!"
    "Using the loincloth you took from the lizard you tear it into many different strips, and quickly muzzle the lizard with one of them."
    "He tries to resist again but he barely puts up a fight. "
    "Without much effort you tie his hands up. "

    scene black
    show lizard win1 with slow_dissolve:
        xanchor 0 yanchor 0
        xpos 0 ypos 0
        zoom 0.86
        linear 20.0 xpos 0 ypos -1000
    "The lizard squirms to speak against his restraints."
    "However, the more he struggles the more his cock twitches."
    "You pull him closer to you by the legs until his plump butt brushes against your ballsack."
    "With one swift pull your loincloth flies off, and your raging boner slaps against the lizard’s puckered hole. "
    "The lizard warrior lets out a soft yelp. "
    show lizard win1 with slow_dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    "A soft growl vibrates through your chest."
    "You lick your lips hungrily as seeing the lizard so vulnerable stirs the desire in your loins."
    "From his thick thighs you run your hand across his cobblestone stomach."
    "The small yet firm chest feels tender as you squeeze and grope them."
    "Despite the scales that cover his entire body, the lizard feels oddly smooth to touch."
    "His whole body shudders as you explore every inch of the trapped lizard. "
    "You squeeze him by the thigh and grind your cock along his hole."
    "His warm ass cradles your engorged member."
    "You groan loudly as you push your tip into him."
    with flashbulb
    show lizard win2 with slow_dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55

    "The lizard warrior tries to howl behind his gagged mouth."
    "He closes his eyes and looks away."
    "Inch by inch your hard cock enters his tight hole."
    e 0 "Fuck you're tight."
    "His toes twitch and curls around the back of your forearm."
    show lizard win3 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    "You pull him closer and your cock slides along the buttcrack. "
    e 0 "We’re going to need some lube!"
    "Without hesitation you grab his twin dicks with one hand and hold them close."
    "The moment you start jerking the hard members the lizard’s entire body flexes."
    "His taut chest draw your eyes from his throbbing cocks."
    "He looks at you with lustful eyes and flared nostrils, breathing heavily. "
    "You are entranced by his reactions as you continue to play with his dicks."
    "Your arms jerk him quick for one second, bringing him to the precipice of climax before you suddenly stop and squeeze his dicks together."
    "Hot pre gushes out from the tip of dicks, lathering your fingers in their hot goo."
    "You show him the mess he made."
    e 0 "Someone’s been pent up."
    "You bring the copious amount of pre to your cock, and later it up in the warm liquid."
    "Hot breath escapes your lips as the lizard’s pre feels so good on your raging boner."
    show lizard win2 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    "One completely covered in pre, you press the tip of your cock at the entrance of the lizard’s hole."
    "Your tip slides in easily and the lizard begins to squirm, but this time it feels like he’s inviting you to fuck him."
    "Half of your cock penetrates him and a jolt of electricity runs through your spine."
    "You push harder, until the whole length of your cock enters the lizard."
    "You howl loudly, and your grip on his legs tightens. "
    e 0 "Fuck, Fuck, Fuck!"
    "More pre spews out of the lizard’s cock, dribbling down his shaft while some spurt all over his abs."
    show lizard win3 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    show lizard win2 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    e 0 "Yeah, take it tough guy. Where’s all that cockyness now?"
    show lizard win3 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    show lizard win2 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    "You pull your cock half way and ram it back in hard."
    "The lizard squeals and you can see his eyes roll back as you continue thrusting harder and harder into him."
    "The walls of his insides clamps around your cock, the tightness is mind numbing."
    "Your hips gyrate back and forth, grunting like a beast."
    show lizard win3 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    show lizard win2 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    show lizard win3 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    show lizard win2 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    "The pressure builds inside your balls."
    "Your own pre fills his insides allowing you to pound his delicate hole with increasing vigor."
    show lizard win3 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    show lizard win2 with dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    "Sweat drips down your neck, and your movement slows."
    "The desire to cum is so strong there is nothing else in your mind."
    "You can tell he is close too as his toes curl behind you, his head turns back and forth, undoing the binds around his mouth."
    "Lizard Warrior" "CUMMING!"
    e 0 "Fuck!"
    with flashbulb
    show lizard win4 with slow_dissolve:
        xpos 0.18 ypos -0.08
        zoom 0.55
    "Your hands grasps the lizard’s legs tightly and you pump your hot load into the lizard’s ass."
    "The lizard warrior cums in unison and ropes of cum flies from his double dicks, spraying all over the grass and on his body."
    "Unable to hold in all your cum, some of it drips free from the lizard’s ass."
    "Lizard Warrior" "Ugh.... my ass."
    "The lizard warrior’s head drops to the ground and he is rendered unconscious."
    e 0 "Good grief."
    "You pull out your cock from the lizard and muster enough energy to grab your things and leave."
    $ Zalt.lust = 0
    $ Foe.lizardwin = True
    "You get 1 lizard scale and 150 EXP."
    $ jane_inv_M.take(lizard_scale)
    $ Zalt.exp = min(Zalt.exp+150, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    $ persistent.CG_lizard_win  = True
    jump deepswamp


label battle_lizard_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    hide lizardw with dissolve
    if Quest.bombn ==4:
        "You don’t see it coming, the rogue lizard appears behind you and stabs you with a poison knife."
        scene black with dissolve
        "You collapse on your face unable to move."
        "Nauxus yells your name but because he is distracted by you he too is struck down."
        "The poison has you frozen in place, you’re unable to even look away as the enemy bashes his head in."
        "Your internal screams are futile to stop the final blow from the lizard behind you."
        "{b}{color=#c22719}<GAME OVER>{/color}"
        menu:
            "New game" if True:
                return
            "New game" if True:
                return

    $ Random = renpy.random.randint(1, 2)
    if Random == 1:
        "The lizard warrior manages to fire a dart into your neck."
        "You feel its effects instantaneously, and collapse to the ground."
        "You’re unable to move. "
        "He walks up to your, spear in hand. It’s tip is inches away from your eyeballs."
        "Lizard Warrior" "My, my, what to do with such a sweet ass?"
        "Lizard Warrior" "Be a shame to just kill you like this."
        "Lizard Warrior" "There’s so few chances for me to really enjoy the sweet supple hole of another."
        "Your eyes widen in fear. What is he going to do to you?"
        "Suddenly another lizard warrior appears."
        "Another Lizard Warrior" "Hey, quit messing around. They need us back at camp."
        "Lizard Warrior" "Pff, fine. You got off easy wolf. I’ll let you go this time."
        "Lizard Warrior" "Promise to visit again, and I’ll claim you later."
        "The lizard warrior rummages through your satchel and steals a few coins from you before running off with the other warrior back into the depths of the swamp."
        if jane_inv.qty(coin) != None:
            $ qty = int(jane_inv.qty(coin)*0.2)
            $ jane_inv.drop(coin,qty)
        $ Zalt.hp = 1
        jump deepswamp
    elif True:
        "The lizard warrior gets behind you and knocks you to the ground with a kick to your knees."
        "You tumble forward to the ground."
        "Before you can get up, the lizard leaps onto your back and locks your hands in his strong grip."
        e 0 "Get off me!"
        "Lizard Warrior" "Struggle all you want, but you and I both know you’re too tired to fight back."
        "You yelp when you feel the sting of your behind getting slapped."
        "Lizard Warrior" "Oh yes, this will do nicely."
        "He rubs your right butt cheek and slaps it hard again."
        e 0 "Eeep! What the heck are you doing?"
        e 0 "I’ll rip your head off when I get out of this."
        "Lizard Warrior" "Hush, you’re in no position to talk. Now let daddy enjoy this."
        "He grips your asscheeks and rips off your loincloth."
        "Lizard Warrior" "Hiss. Yes, I love a sweet ripe ass."
        "Lizard Warrior" "It’s been so long since I had a chance to fuck another guy. "
        "Lizard Warrior" "You will do just fine."
        e 0 "Oh, I’m pretty sure no one would want to fuck you, you puny-"
        scene lizardtop 1 at center with slow_dissolve
        "He realigns his position and rests one foot on top of your back."
        "He tightens his grip on your hands so it sends a jolt of pain up your spine."
        "Lizard Warrior" "There’s nothing puny about me wolf."
        "Lizard Warrior" "I’m going to fill you up so good that you won’t be able to walk for days!"
        "He talks big, but you know you’ll have the upper hand once he is drained."
        "Then you feel the wet smack of a hot phallic object against your butthole, and another resting just on top of your butt."
        "You’re fake trashing about just to give him a show."
        "He growls at you and spanks you harder."
        "Lizard Warrior" "Now loosen that ass or this is really going to hurt!"
        "The lizard takes his time and thrusts one of his hard members against your ass crack."
        scene lizardtop 2 at center with slow_dissolve
        "Your body is immediately turned on by the feel of how his thick dick splits your buttcheeks."
        "Your attempts to resist your feelings fail as your own dick hardens."
        e 0 "....If it’s come to this. I might as well enjoy it."
        "You subtly press your butt closer against the lizard to tempt him to put it inside you."
        "Lizard Warrior" "Well, it looks like I awoke the slut in you Beg for it, bitch Beg for my cock..."
        e 0 "..."
        e 0 "Give me your dick..."
        "Lizard Warrior" "What was that? I can’t hear you, slut!"
        "He spanks you again causing you to let out a loud cry." with vpunch
        "Lizard Warrior:" "Louder!"
        e 0 "GIVE ME YOUR DICK! FUCK ME WITH IT!" with vpunch
        "Lizard Warrior" "That's it bitch Yeah Say how much you love dick!!!"
        e 0 "I love it!"
        with flashbulb
        scene lizardtop 3 at center with slow_dissolve
        "He presses the tip against your hole."
        "You yelp from his unsuspecting intrusion."
        e 0 "Ah...ah..."
        "His dick forces its way through your unprepared hole."
        "No matter how much you try to relax your butt, all you can do is struggle to let all of the lizard inside you."
        "You close your eyes and bury your face into the ground."
        "Your fingers dig deep into the palm of your hands and you growl loudly."
        scene lizardtop 4 at center with slow_dissolve
        "Lizard Warrior" "Fuck, I love a tight hole. Grip my cock like you can’t live without it."
        "The warrior pulls his cock out and then rams it back in all the way to the base of his dick."
        scene lizardtop 5 at center with dissolve
        "You let out a guttural cry and your dick starts to dribble pre cum along your shaft."
        "The lizard’s second dick wets your back with squirts of pre."
        scene lizardtop 6 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "You pant heavily and you feel the walls of your anus throbbing from the pain of taking in the lizard’s cock or perhaps that was his dick doing the throbbing, you can’t tell the difference."
        scene lizardtop 6 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "Lizard Warrior" "I knew you were a little bitch hungry for dick the moment I saw you."
        e 0 "Shut up, shut up!"
        scene lizardtop 6 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "Lizard Warrior" "I'm going to pound you until you learn your place bitch."
        "Lizard Warrior" "But don’t worry, I didn’t forget about you."
        "He reaches for your cock and tugs at it slowly."
        "Your eyes feel like they are rolling back by how arousing his touch feels."
        "His hand wraps around the shaft with just enough force that it doesn’t feel too rough."
        "The feeling of his cool hands against your warm cock is unlike any sensation you felt before."
        "You can’t help but shoot more pre into his hands as he rubs his forefingers around your cockhead."
        scene lizardtop 4 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "His hand moves downwards towards your balls and fondles them playfully, squeezing them to make you squeal."
        "Then he pulls his hand away and spanks you."
        scene lizardtop 4 at center with dissolve
        "He pulls his hard dick half way out causing your whole body to shudder. "
        scene lizardtop 5 at center with dissolve
        "He doesn’t give you a chance to catch a breath before he slams his cock inside you again."
        e 0 "FUCK!"
        "Your knees buckle from the sudden wave of pleasure shooting up inside you."
        "The tip of his dick presses right on your spot, sending bursts of ecstasy through your body."
        "You groan helplessly with your tongue rolling out."
        scene lizardtop 6 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "The lizard gets into a rhythm pulling his cock out just far enough before fucking you with relentless wanton again."
        scene lizardtop 6 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "And again."
        scene lizardtop 4 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "And again."
        "Lizard Warrior" "Yeah, fuck I love your hole."
        "With his tail, he smacks your right buttcheek in time with each thrust."
        scene lizardtop 6 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "Your nose twitches as it catches the smell of your musky sweat combined with his."
        "Your ass flexes and clamps onto the lizard’s dick."
        scene lizardtop 4 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "He grips your hands tighter and lets out a beastial growl. "
        e 0 "Uguhh!"
        "A gush of hot pre fills your ass again, and more squirts all over your back."
        "The heat of his pre cum in and on you makes you tremble."
        "You can feel the pressure building in your balls, pushing you to the brink of climax."
        scene lizardtop 4 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "Lizard Warrior" "You’d like that wouldn’t you?"
        "He spanks you with his tail again."
        scene lizardtop 6 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "Lizard Warrior" "But I’ll leave you wanting more wolf. "
        scene lizardtop 6 at center with dissolve
        scene lizardtop 5 at center with dissolve
        scene lizardtop 4 at center with dissolve
        scene lizardtop 5 at center with dissolve
        "The lizard grunts and his movements start to slow."
        "You can only pant in response. "
        scene lizardtop 6 at center with dissolve
        scene lizardtop 5 at center with dissolve
        with flashbulb
        pause 1
        scene lizardtop 7 at center with slow_dissolve
        "With one strong thrust the lizard cums inside your hole while his second cock bathes your body in hot cum."
        "Some of the cum even lands on your head."
        "The gush of his musky fluids sets you off, and your cock unloads all over the ground."
        "The lizard throws his head into the air and hisses while you grunt into the earth."
        "Your brain goes numb as so much cum floods your insides."
        scene lizardtop 8 at center with slow_dissolve
        "The lizard gasps for air as he pulls his dick out of your ass."
        "The excessive cum that was inside you leaks outwards like an overfilled cream custard."
        "Now’s your chance to take the lizard down, but his grip on your hands is still too tight."
        "How is he so powerful?"
        "Lizard Warrior" "Don’t think so wolf. I’ve fucked stronger things than you."
        scene black at center with slow_dissolve
        "He bends over to your ear. You can feel his tongue darting around it."
        "Lizard Warrior" "But I enjoyed it very much."
        "Lizard Warrior" "Come back soon bitch and we’ll do it again."
        "He frog leaps over your back pushing your head into the dirt."
        "The last thing you see is his plump butt as he runs back into the shadows of the swamp."
        "You groan and take some time before picking yourself back up again."
        $ persistent.CG_lizard_lose = True
        $ Zalt.lust = 0
        if jane_inv.qty(coin) != None:
            $ qty = int(jane_inv.qty(coin)*0.2)
            $ jane_inv.drop(coin,qty)
        $ Zalt.hp = 1
        jump deepswamp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
