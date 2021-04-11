label Roushk_meet:
    if Roushk.meet == 1:
        if Time.hours >= 6 and Time.hours <= 17:
            $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
            $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
            scene forestmap 1
        elif True:
            $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
            $ renpy.music.set_volume(0.5, 5, channel = "Chan2")
            scene forestmap 1n

        play music "music/thunder.wav"
        "As you are out and about, a loud rumble in the skies catches your attention."
        "Up above, dark clouds form and you hear the unmistakable sound of thunder rolling."
        e 1 "(This doesn’t look right. A storm inside a fog?)"
        "A sudden thunder crash sends goosebumps down your spine, causing the fur on your back to stand on end."
        e 5 "Is the tavern going to be alright? I better get back there and check."

        scene black with slow_dissolve
        "All the while as you head back to the tavern there’s not a drop of rain anywhere, just more rumbling and dark clouds."

        "A sense of unease follows you through your travel back to the tavern."
        stop Chan1
        stop Chan2
        stop music
        play sound "music/foot1.ogg"
        "..."
        play sound "music/door.mp3"
        scene tavern 1 with slow_dissolve

        play Chan1[ "<silence 0.5>", "music/tavern.ogg" ]fadein 3
        play Chan2[ "<silence 0.5>", "music/thunder.wav" ]fadein 3
        $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
        $ renpy.music.set_volume(0.3, 5, channel = "Chan2")
        "Upon returning to the tavern the warmth of its inhabitants welcomes you back."
        "You can feel your shoulders lighten up the moment you step inside."
        "Witer in the distance waves at you while Chet peeks from his spandrel for a quick glance before sinking back into his seat."
        show hakan stand at left with dissolve
        show witer stand at right with dissolve
        h "Hey, it’s Fuzzbutt! Pull up a chair, and have a beer with me."
        e 6 "Hey Hakan, in a second, I just want to check something with Snow."
        h "Alright. Witer, get a beer ready on me."
        w "One beer coming right up."
        hide hakan stand with dissolve
        hide witer stand with dissolve
        "You walk over to the bar where Snow readies the drink Hakan ordered for you. "
        show snow stand1 at center with dissolve
        s "Finally had enough adventuring for one day?"
        hide snow stand1 with dissolve
        "The wolf puts the mug of beer in front of you."
        e 6 "Actually, I’m just here to check in on how you guys are doing."
        e 1 "There’s a freak storm happening outside."
        show snow stand1 at center with dissolve
        s "We heard. First time it has ever happened."
        e 1 "Is the tavern strong enough to withhold a storm?"
        show snow laugh at center with dissolve
        s "We’ll see, I’ve buffed up this beauty ever since I started up shop."
        s "Even if anything happens, we can still patch it up."
        s "Now, go enjoy your beer, and leave the tavern to me."
        hide snow laugh with dissolve
        "Snow sends you away with your beer. "
        scene black with slow_dissolve
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
        "With the thunder outside thumping against the roof of the tavern, you decide to spend the remainder of your day indoors and catch up with your friends."
        "Come nightfall, the thunder carries on."
        "With an uneasy heart, you head to bed."
        "Hopefully, the clouds will clear in the morning."
        $ Time.days =Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
        $ Zalt.hp = Zalt.maxhp
        $ Zalt.mp = Zalt.maxmp
        $ Zalt.lust = 0
    elif Roushk.meet == 2:

        stop music
        scene tavern 1
        play Chan1[ "<silence 0.5>", "music/tavern.ogg" ]fadein 3
        play Chan2[ "<silence 0.5>", "music/thunder.wav" ]fadein 3
        $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
        $ renpy.music.set_volume(0.3, 5, channel = "Chan2")
        e 1 "A storm? Here and now? That’s so strange."
        show hakan stand at left with dissolve
        show witer stand at right with dissolve
        h "Hey, it’s Fuzzbutt! Pull up a chair, and have a beer with me."
        e 6 "Hey Hakan, in a second, I just want to check something with Snow."
        h "Alright. Witer, get a beer ready on me."
        w "One beer coming right up."
        hide hakan stand with dissolve
        hide witer stand with dissolve
        "You walk over to the bar where Snow readies the drink Hakan ordered for you. "
        show snow stand1 at center with dissolve
        s "So, where will you be exploring today?"
        e 6 "Nowhere really, there’s a fierce storm going on."
        s "I heard, well the fog and the storm isn’t going anywhere, might as well take a break."
        hide snow stand1 with dissolve
        "The wolf puts the mug of beer in front of you."
        show snow stand1 at center with dissolve
        e 1 "Has there been a storm in the fog before?"
        s "First time it has ever happened."
        e 1 "Weird, and more importantly, will the tavern be able to handle such a storm?"
        show snow laugh at center with dissolve
        s "We’ll see, I’ve buffed up this beauty ever since I started up shop."
        s "Even if anything happens, we can still patch it up."
        s "Now, go enjoy your beer, and leave the tavern to me."
        hide snow laugh with dissolve
        "Snow sends you away with your beer. "
        scene black with slow_dissolve
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
        "With the thunder outside thumping against the roof of the tavern, you decide to spend the remainder of your day indoors and catch up with your friends."
        "Come nightfall, the thunder carries on."
        "With an uneasy heart, you head to bed."
        "Hopefully, the clouds will clear come morning."
        $ Time.days =Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
        $ Zalt.hp = Zalt.maxhp
        $ Zalt.mp = Zalt.maxmp
        $ Zalt.lust = 0
    $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
    scene tavern 1 with slow_dissolve
    "The next morning, you start your day off with a hearty plate of scrambled eggs at the bar."
    "Suddenly, Hakan and Witer burst in from the main door."
    show hakan stand at left with moveinleft
    show witer stand at right with moveinleft
    "Strangely, the both of them look out of breath as they enter."
    "Witer who is panting heavily, runs up to the bar and pantomimes that he wants a glass of water from Snow."
    show snow angrys1 at center with dissolve
    s "Witer I don’t know what you’re trying to say."
    show witer stand at right with dissolve
    w "Water… please!" with vpunch
    show snow angrys1 at center with dissolve
    s "What happened to you two?"
    "Snow reaches below his counter and pulls out a mug and starts pouring from a bottle of water."
    show hakan stand at left with dissolve
    h "You won’t… you won’t…" with vpunch
    "Hakan coughs, and signals to the rest to wait with his forefinger."
    "He takes a few deep breaths."
    "Just as Snow hands the drink to Witer, the lizard downs the whole mug in one go."
    h "Ok, we were both attacked by lizard warriors."
    e 9 "Attacked? Are you both injured?"
    w "No, we’re fine. Hakan ran into me after I dealt with my attacker."
    w "Then we came in here. That lizard scared the crap out of me. "
    w "He came out of nowhere while I was looking for mushrooms."
    w "We were so close, I could see the madness in its eyes."
    e 5 "How’d you even get away?"
    w "Well I punched him in the snout so hard that it sent him flying against a tree."
    w "Then I just ran as fast as I could."
    h "Same thing happened to me, I was out in the deeper parts of the woods looking for slime jewels, then this little prick jumped me from behind."
    h " I bashed him against a rock but the damn bug got away. I tried to run after him but he was too quick."
    h "Then, through the fog and trees I accidentally bumped into this green one."
    "Hakan points to Witer with his thumb."
    s "This is serious. Why would the lizard tribe start attacking us?"
    s "Did any of you do anything to anger them?"
    hide hakan stand
    hide witer stand
    hide snow angrys1 with dissolve
    "All three of them turn their heads at you."
    "You stare back dazed."
    e 9 "What? I didn’t do anything."
    show snow angrys1 at center with dissolve
    s "Let’s take a step back, we can’t jump to any conclusions."
    s "Are you two sure those who attacked you were from the lizard tribe?"
    show hakan stand at left with dissolve
    h "Not really."
    show witer stand at right with dissolve
    w "I was so scared I didn’t get that good a look at them."
    hide hakan stand
    hide witer stand
    hide snow angrys1 with dissolve
    "Snow taps the bar with his hook hand, and from where you’re sitting, you can see his left foot tapping furiously. "
    show snow stand1 with dissolve
    s "Alright, this is what we’ll do."
    s "[name], go with Hakan and Witer, investigate the site of the attacks."
    s "And see if those lizards left any clues to their identity."
    e 6 "Sure, let me just-"
    "With your spoon you reach out for the rest of your meal but you are tugged backwards by the fur on the back of your neck."
    h "Come on Fuzz Butt."
    w "Ah, I just want to be done with this and get back to work, I got jerkies to prepare."
    hide snow stand1 with dissolve
    e 5 "My eggs!"
    play sound "music/door.mp3"
    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    scene black with dissolve
    $ Time.mins = Time.mins + 20
    "Witer leads you both to the back of the barn through some trees."
    "You aren’t too far from the tavern."
    play sound "music/foot1.ogg"
    scene forest 7 with dissolve
    show hakan stand at left with dissolve
    show witer stand at right with dissolve
    w "This was where I was attacked. "
    h "Look around, see what clues the lizard left behind."
    "The three of you scrounge around the area in search of some hint of the lizard. "
    "Digging through the bushes and trees you find nothing but sticks and stones."
    "Your stomach rumbles a bit and you can’t help thinking about the eggs you left behind."
    w "I found something!"
    hide hakan stand
    hide witer stand with dissolve
    "You all group together to see what Witer found."
    w "It’s a part of the lizard’s tooth."
    h "Must have been one heck of a punch."
    "Hakan spanks Witer, causing the green alligator to stand on his tiptoes."
    w "Woo, Hakan! Watch where you’re touching or you’ll see what these hands can really do." with vpunch
    h "Oh, I bet I will."
    "Hakan winks at Witer who elbows the red dragon in the gut."
    e 8 "Focus you guys, the scent on this tooth is faint."
    e 8 "Let’s see if there is anything else in Hakan's area."
    scene black with dissolve
    "The three of you head to the other end of the tavern, inside the forest where you first encountered the slimes."
    $ Time.hours = 7
    $ Time.mins = 40
    play sound "music/foot1.ogg"
    scene forest 1 with dissolve
    "Again the three of you look around to search for clues."
    "Hakan quickly spots a torn piece of cloth amongst the bushes."
    "He hands the piece of fabric to you."
    show hakan stand at right with dissolve
    show witer stand at left with dissolve
    h "The darn lizard probably ripped his loincloth while running away."
    w "You sure you didn’t rip it off him? "
    "Hakan laughs heartily. "
    h "I have a special technique to rip off clothes."
    h "If I wanted to, I’d have the whole thing with me."
    h "Want to try?"
    "Witer blushes and punches the red dragon on his shoulder."
    e 1 "The smell on this one is stronger. It’s definitely a lizard’s scent."
    h " I’ll leave the rest to you then. Find out who the attackers were."
    h "I’ll be at the tavern to make sure this doesn’t happen to anyone else again."
    e 1 "Right, I’ll just track this lizard down and get some answers. Thanks for the help you guys."
    w "Let’s get out of here, who knows when a slime will come out of nowhere."
    hide hakan stand
    hide witer stand with dissolve
    "Hakan and Witer leave you to return to the tavern."
    "You sniff the torn cloth that was found, and the path becomes clear to you."
    "It's from the dark swamp."
    "You follow your nose to the source of the smell."
    "Fortunately, it looks like the storm is almost over."
    "Tracking the smell, you find yourself heading towards the dark swamp."
    e 1 "Best to head to the dark swamp while its sunny. Without light it will be like walking into a death trap."
    $ Roushk.fight = 1
    jump forest_map0

label Roushk_fight:
    stop Chan1
    stop Chan2
    stop music
    play sound "music/foot1.ogg"
    "..."
    "You trudge through the muddy grounds of the dark swamp. "
    "Your nose wrinkles as the wretched stench of the swamp is stronger here than in the lizard tribe."
    "The thickness of the muddy grounds makes it hard for you to move quickly."
    "Each step feels like you have boulders tied to your feet."
    "You swing your blade, cutting through branches and vines that block your way. "
    "The lizard’s smell grows increasingly potent as you head deeper inwards."
    "Once you are deep inside the swamp, you stop."
    "The fur on your back shoots upwards."
    "Through the shadows of the mangrove trees you sense multiple pairs of eyes looking at you."
    "The eerie dread of danger closes in upon you as the sounds of scurrying feet and splashing water circles around you but the enemies dart by so fast you only catch a glimpse of their shadow."
    show lizardw at center with dissolve
    "Suddenly, a rogue lizard warrior leaps out from between the trees brandishing his spear."
    "Rogue Lizard Warrior" "Lookie here, fresh meat for the boss! Here to bask in our boss’s glory and power?"
    "You hold your sword close ready to attack."
    e 12 "No, I’m here to beat you and your friends to teach you to stay away from the tavern."
    "The Rogue Lizard Warrior laughs maniacally."
    "Rogue Lizard Warrior" "Foolish meat, all will join the boss and spread his influence."
    jump battle_roushk

label battle_roushk:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ Map.good_battle = True
    if Roushk.fight == 1:
        $ Battle.holyfcd = 0
        $ wolf_max_hp = 120
        $ wolf_hp = wolf_max_hp
        $ players_turn = False
        $ wolf_max_lust = 100
        $ wolf_lust = 0
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
    elif True:
        $ Battle.holyfcd = 0
        $ wolf_max_hp = 250
        $ wolf_hp = wolf_max_hp
        $ players_turn = False
        $ wolf_max_lust = 100
        $ wolf_lust = 13
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    jump battle_roushk_loop


label battle_roushk_loop:



    show screen simple_stats_screen
    show screen battle_menu





    if Roushk.fight == 1:
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
                e 0 "I can't fight anymore.."
                "The enemy is too strong."
                "You’re knocked onto the ground."
                jump battle_roushk_lose
            if res == "Flirt":
                $ Random = renpy.random.randint(1, 5)
                if Random == 1:
                    $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                    $ wolf_lust = wolf_lust+Zalt.flirt
                    "You successfully jump behind the lizard and plunge your hands down his loincloth."
                    "You find his thin slit and gently massage its entrance before jumping away."
                    "The lizard is confused and breathing heavily."
                elif Random == 2:
                    $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                    $ wolf_lust = wolf_lust+Zalt.flirt
                    "You tease the lizard by playing with your nipples and motioning him to join you."
                    "The lizard darts his tongue out with a lewd smile, you can tell he wants more."
                elif Random == 3:
                    $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                    $ wolf_lust = wolf_lust+Zalt.flirt
                    "You strike a series of poses with a confident smile."
                    "He gasps loudly and grabs his groin as though trying to hide it from view."
                elif True:
                    $ Random = renpy.random.randint(1, 3)
                    if Random == 1:
                        "You successfully jump behind the lizard and plunge your hands down his loincloth."
                        "You find his thin slit and gently massage its entrance before jumping away."
                        "The lizard growls angrily at you and swats his spear at you."
                    elif Random == 2:
                        "You tease the lizard by playing with your nipples and motioning him to join you."
                        "He spits on the ground and angrily cuts the air with his dagger."
                    elif True:
                        "You strike a series of poses with a confident smile."
                        "He ignores your seduction."
                if wolf_lust >= 100:
                    hide screen simple_stats_screen
                    hide screen battle_menu
                    hide screen battle_skill
                    hide screen battle_item

                    stop music
                    jump Roushk_fight_2
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
                jump Roushk_fight_2
            elif True:
                pass
            $ Random = renpy.random.randint(1, 4)
            if Random == 1:
                $ Random = renpy.random.randint(1, 100)
                if Random <= Battle.dodge:
                    "The lizard cuts you with his dagger."
                    "But you dodged his attack!"
                elif True:
                    $ wolf_damage = renpy.random.randint(20, 30)
                    $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                    "The lizard cuts you with his dagger. It burns deep into your flesh."
            elif Random == 2:
                "The lizard stares you down."
                "His forked tongue darts in and out, and he stabs his spear into the ground."
                "You watch him curiously, he leans against the spear, his hands wrap near the tip of the weapon."
                "He thrusts his hips forward, and your heart skips a beat."
                "He continues his seductive dance along his pole rendering you immobile."
                $ wolf_damage = renpy.random.randint(10, 30)
                $ Zalt.lust += wolf_damage
            elif True:
                $ Random = renpy.random.randint(1, 100)
                if Random <= Battle.dodge:
                    "The lizard plunges his spear into your arm."
                    "But you dodged his attack!"
                elif True:
                    $ wolf_damage = renpy.random.randint(10, 20)
                    $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                    "The lizard plunges his spear into your arm."

            if Battle.holyfcd !=0:
                $ Battle.holyfcd = Battle.holyfcd-1
        if wolf_hp <= 0:
            if Zalt.hp <= 0:
                jump battle_roushk_lose
            elif True:

                jump Roushk_fight_2

        elif Zalt.hp <= 0:
            jump battle_roushk_lose
        elif Zalt.lust >= Zalt.maxlust:
            "You're too horny to fight anymore."
            "You fall to the ground."
            jump battle_roushk_lose
        elif True:
            jump battle_roushk_loop
    elif True:
        show roushk_b at center
        play music "<loop 12.4405>music/forest_fight_strong2.ogg"
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
                e 0 "I can't fight anymore.."
                "The enemy is too strong."
                "You’re knocked onto the ground."
                jump battle_roushk_lose
            if res == "Flirt":
                "You perform a seductive dance."
                "The red lizard is too focused on the battle to care about your seductive moves."
                "He throws a log at you."
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
                "You can't escape!"
            elif True:
                pass
            if wolf_hp <= 0:
                jump Roushk_fight_win
            $ Random = renpy.random.randint(1, 4)
            if Random == 1:
                $ Random = renpy.random.randint(1, 100)
                if Random <= Battle.dodge:
                    "The red lizard rushes towards you with his arms wide open."
                    "But you dodged his attack!"
                elif True:
                    $ wolf_damage = renpy.random.randint(25, 45)
                    $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                    "The red lizard rushes towards you with his arms wide open."
                    "Before you can bring your sword down he grabs you by the hips and swings you against a tree."
            elif Random == 2:
                $ Random = renpy.random.randint(1, 100)
                if Random <= Battle.dodge:
                    "Despite his large muscular form, the red lizard is surprisingly fast on his feet."
                    "You try to block his right punch but he quickly switches to the left."
                    "But you dodged his attack!"
                elif True:
                    $ wolf_damage = renpy.random.randint(25, 40)
                    $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                    "Despite his large muscular form the red lizard is surprisingly fast on his feet."
                    "You try to block his right punch but he quickly switches to the left and hits you in the face."
            elif True:

                $ Random = renpy.random.randint(1, 100)
                if Random <= Battle.dodge:
                    "The lizard leader punches you in the gut and grabs you by the back of your neck."
                    "He slams your snout into the muddy earth trying to drown you in the dirt."
                    "You manage to swing the back of your sword knocking him in the head."
                    "He staggers back and releases his hold on you letting you free yourself."
                    "But you dodged his attack!"
                elif True:
                    $ wolf_damage = renpy.random.randint(25, 40)
                    $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                    "The lizard leader punches you in the gut and grabs you by the back of your neck."
                    "He slams your snout into the muddy earth trying to drown you in the dirt."
                    "You manage to swing the back of your sword knocking him in the head."
                    "He staggers back and releases his hold on you letting you free yourself."
            if Battle.holyfcd !=0:
                $ Battle.holyfcd = Battle.holyfcd-1
        if wolf_hp <= 0:
            if Zalt.hp <= 0:
                jump Roushk_fight_win
            elif True:

                jump Roushk_fight_win

        elif Zalt.hp <= 0:
            jump battle_roushk_lose
        elif Zalt.lust >= Zalt.maxlust:
            "You're too horny to fight anymore."
            "You fall to the ground."
            jump battle_roushk_lose
        elif True:
            jump battle_roushk_loop


label battle_roushk_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item

    stop music
    if Roushk.fight == 1:
        hide lizardw with dissolve
        "The Rogue Lizard Warrior kicks you hard on the chest sending you falling onto the muddy floor."
        "Rogue Lizard Warrior" "Take him!"
        "More and more lizard warriors pounce upon you, their grabby hands pulling at your fur and restraining your limbs." with vpunch
        e 0 "What are you?"
        "Thump!" with vpunch
        "Something heavy falls close to you and you feel the presence of someone large walking over."
        "A large red foot stomps on you, knocking the air out of you. "
        "You wanted to scream but your eyes widen at the sight of the creature’s glowing yellow eyes. "
        with flashbulb
        "Its light envelopes your face, and all traces of who you are is gone."
        "Only one idea fills your consciousness… you live to serve the boss."
        scene black with vslow_dissolve
        "{b}{color=#c22719}<GAME OVER>{/color}"
        menu:
            "New game" if True:
                return
            "No!" if True:
                jump forest_map
    elif True:
        hide roushk_b with dissolve
        show roushk stand1 at center with dissolve
        "Red lizard" "If you won’t listen to me by choice. I’ll just have to hammer that obedience into you."
        hide roushk stand1 with dissolve
        "He grabs you by the neck and slowly lifts you up. Your feet barely touch the ground."
        "Red lizard" "Prepare to kiss my feet, cause that’s all you’re going to want for the rest of your life."
        show purple at center with dissolve
        "Alas, any attempt to avert your gaze fails as you feel your mind burning away into oblivion."
        "Before long, any trace of your individuality is snuffed out as you stare deeper and deeper into your foes' ever hypnotic eyes."
        "{b}{color=#c22719}<GAME OVER>{/color}"
        menu:
            "Give in" if True:
                return
            "Give in" if True:
                return
            "Give in" if True:
                return
            "Give in" if True:
                return
            "Give in" if True:
                return
    return

label Roushk_fight_2:
    $ Roushk.fight = 2
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    "The Rogue Lizard Warrior staggers backwards and leaps back into the woods."
    hide lizardw with dissolve
    "You get 1 lizard scale and 150 EXP."
    $ jane_inv_M.take(lizard_scale)
    $ Zalt.exp = min(Zalt.exp+150, Zalt.maxlv*250+100*(Zalt.maxlv-1))
    "A deep booming laughter then echoes through the swamp. "
    e 1 "Who’s there? Show yourself?"
    "The trees in front of you shake as a pair of large red hands grab them by the trunk and with a deafening roar, the creature pushes the trees with such forces they topple to the side."
    "A large lumbering figure steps out. "
    show roushk stand1 at center with dissolve
    "Licking his lips the massive red lizard stands proudly before you."
    "He crosses his arms and you can feel his blood red eyes staring you down."
    e 12 "You the leader of this whole operation?"
    "Red lizard" "I'm the boss of this whole swamp and soon this entire kingdom."
    "Red lizard" "You do well to surrender and pledge your allegiance to me!"
    e 12 "You’re insane if you think I’ll just work for you."
    "Red lizard" "Oh, trust me when I’m done with you, you won’t have a choice."
    "Red lizard" "Don’t let him escape!"
    "The lizards that were watching now start to quickly circle you. They’ve got you surrounded from every possible side."
    "Running away will not be an option this time."
    e 12 "Bring it!"
    hide roushk stand1
    jump battle_roushk

label Roushk_fight_win:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    play music "music/forest_fight_boss_end.ogg" noloop fadein 1.4
    "You duck dodging the red lizard’s swing. "
    e 0 "Hyah!"
    "Propelling yourself with a jump you land a powerful uppercut on the lizard’s jaw."
    "Red lizard" "Guah!"
    hide roushk_b with dissolve
    "Like a toppling tower, the massive lizards falls on his back, unconscious."
    "Rogue Lizard Warrior" "He beat the boss! Ahh!"
    "In unison all the lizards around you yell and their bodies fall from the trees landing flat onto the ground. "
    "The entire scene sends chills down your spine. "
    e 9 "What the heck is going on?"
    e 9 "Crap, doesn’t look like they’re going to come help you now."
    "You kick the red lizard lightly on the shoulder, but he doesn’t move."
    "He’s out cold."
    e 1 "I can’t really leave you here now can I?"
    e 1 "Your goons have abandoned you for death, but that’s not going to do us any good."
    e 1 "If you die, they’ll just replace you and may have greater initiative to attack us again."
    e 1 "(Best, to convince him of otherwise.)"
    "You crouch down and lift the lizard onto your shoulders."
    "Your feet sink deeper into the mud with him on your shoulders."
    e 1 "Guh, you need to lose some muscle.."
    "With some effort you stand up and leave the dark swamp with your unconscious companion."
    "You decide to head to the tavern and get some help to make sure the red lizard doesn't cause anymore trouble."
    $ Roushk.fight = 3
    jump Roushk_evening_1
label Roushk_evening_1:
    if Time.hours <= 18:
        $ Time.hours = 18
    elif True:
        $ Time.hours = Time.hours +2
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1

    play sound "music/foot1.ogg"
    "..."
    scene outdoor 1n with slow_dissolve
    "The red lizard’s heavy build slows your journey back to the tavern, by the time you reach there it’s already evening."
    play sound "music/door.mp3"
    scene tavern 1 with slow_dissolve
    $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
    $ renpy.music.set_volume(0, 5, channel = "Chan2")
    $ renpy.music.set_pause(False, channel='Chan1')
    $ renpy.music.set_pause(False, channel='Chan2')
    play Chan1[ "<silence 0.5>", "music/tavern.ogg" ]fadein 3
    "You kick the tavern door open."
    e 1 "Witer, quick I need you to bring some medical supplies, this guy is hurt."
    show witer stand at center with dissolve
    w "Huh? Who is he?"
    e 1 "He’s the jackass that led the lizards who attacked you."
    e 13 "Please, he’s really heavy, let’s save the questions for later."
    w "Alright, just put him in the barn."
    show hakan stand at left with dissolve
    w "Hakan, bring your rope from the room."
    h "Gah, but my beer-"
    w "Don’t start with me, or I’m dumping all your beer into the bushes."
    h "Guh!"
    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    play sound "music/door.mp3"
    hide hakan stand
    hide witer stand with dissolve
    scene black with dissolve
    "..."
    scene barn 1 with slow_dissolve
    "As Witer instructed, you head over to the barn and drop the lizard onto a bed of hay."
    "Hakan comes running with a bundle of rope in hand."
    "He helps you to bind the lizard’s arms wrists together."
    "Meanwhile, Witer brings his medication to help treat the lizard’s wounds."
    show witer stand at left with dissolve
    show hakan stand at right with dissolve
    w "You sure did a number on him."
    e 1 "I made sure not to hit any of his vital areas."
    w "So this guy led a group of lizards. He is pretty well dressed for the role."
    h "Yeah, I’ve never seen attire like this before."
    w "Maybe he’s from some far off continent."
    e 1 "Doesn’t explain why he’d come here to lead a bunch of rogue lizards."
    e 1 "He mentioned wanting to take over the forest, then the entire kingdom."
    h "Yeah he’s crazy."
    hide hakan stand with dissolve
    "Hakan twirls his forefinger around the side of his head to emphasize his point."
    show hakan stand at right with dissolve
    e 1 "Well if he is, then he’s better off locked up than out there sending his gang to attack us."
    w "I’m done with his wounds, give it some time and they should heal completely."
    e 1 "Thanks, I’ll keep watch of him."
    h "Alright, you’ll know where to find us. Come get us if he starts making trouble."
    e 1 "I will, thanks guys."
    hide hakan stand
    hide witer stand with dissolve
    "Witer and Hakan leave the barn. "
    "You find a stool nearby and start keeping watch of the sleeping lizard."
    "Hopefully, he will wake up soon."
    "Until then, you sit and wait."
    scene black with slow_dissolve
    "Waiting."
    "It feels uneasy just sitting and watching."
    "You start noticing things you usually don’t, like how itchy your feet feel."
    "You even try to make a game with your tail to pass the time."
    "Whenever your tail flicks to one side, you’d try to grab the tip."
    e 1 "Miss."
    e 5 "Come on tail."
    e 8 "Nearly got it."
    "Some time passes by while you entertain yourself."
    $ Time.hours = Time.hours +1
    $ Time.mins = Time.mins +30
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    scene barn 1 with slow_dissolve
    "Red lizard" "Ngh."
    e 1 "Hmm? Is he awake?"
    "You stand up and walk over to the lizard."
    "He appears to be sleeping still."
    "Slowly, you bend over to get a closer look."
    show roushk stand at center with dissolve
    hide roushk stand with dissolve
    "Snap!" with vpunch
    "The lizard rips his binds apart and grabs you by the shoulder. "
    with flashbulb
    "It all happens so fast your brain is unable to even process what’s going on until your back is slammed against the wall."
    menu:
        "Fight back!" if True:
            $ Roushk.ke = 1
            "The lizard rushes forward with both his arms held up high."
            "You grab him by the hands and push back."
            "Both you growl at each other like wild beasts."
            "You push as hard as you can but the two of you are equally matched."
            "Neither side relents. You dig your feet into the ground and push back even harder."
            "The red lizard doesn’t move an inch."
            "With your right foot, you place it behind his left calf and then you pull your foot back. The sudden movement forces the lizard to break his stance and lose balance."
            "The sudden shift trips the red lizard."
            "The lizard's eyes widen in surprise as he tumbles back."
            "You quickly grab him by his forearms and twist him around, sending him flying onto the wall behind you with a loud bang."
            e 12 "Enough!"
            scene roushk eke with slow_dissolve
            "You slam both your arms against the spaces beside the lizard, trapping him between your arms."
            "He looks at you with ferocious intensity, unphased by your actions while never breaking eye contact for even a second."
            e 12 "Enough with the fighting. I don’t want to fight you anymore."
            "Red lizard" "Then why the heck did you kidnap me if you weren’t looking for a fight? "
            e 12 "I didn’t kidnap you. You were the one picking a fight with me."
            "Red lizard" "That’s utter nonsense. Where in Aigran are we, wolf? "
            "Red lizard" "Explain how you kidnapped me from the temple?"
            e 5 "Temple? Aigran? What are you talking about, I never heard of that place, and we didn’t come from a temple."
            "It troubles you that Hakan may be right, this lizard is a few marbles short."
            "You could knee him in the groin and make a run for help, but you decide to see how far you can reason with him."
            "Red lizard" "No, how can this not be Aigran? That’s the name of this whole world. "
            e 1 "Hey, I might be taught by my father but I know damn well this world isn’t Aigran."
            e 12 "Now calm yourself down, and let’s talk like civilized people."
            "Red lizard" "Or what you’re going to knee me in the groin?"
            "Your eyes widen."
            "Red lizard" "I can see the gears in your head turning, it’s the easiest strategy you can pull off. "
            "Red lizard" "I’m not going to do anything weird, let’s just talk."
            e 1 "Fine."
            scene barn 1 with slow_dissolve
            "You back away from the lizard, giving him space to breathe."
            show roushk stand at center with dissolve
            "Red lizard" "Start by explaining who you are, and where this is."
            e 1 "I am [name], and this is the Tavern of Spear."
            e 1 "Currently, we’re all trapped in this foggy forest."
            "Red lizard" "A foggy forest that traps people? This day just keeps getting better."
            e 1 "I’ve answered your questions, now tell me who you really are and what are you doing here?"
            hide roushk stand with dissolve
            "The red lizard claps his hands together in front of him."
            show roushk stand at center with dissolve
            ro "My name is Roushk, one half that leads the lizardmen tribe."
            ro "I can’t explain how I really got here."
            ro "I found an odd looking artifact during an expedition, and after a bright flash of light I ended up awakening here."
            e 5 "That’s not possible, don’t you remember fighting me just now in the swamp?"
            e 5 "You were declaring yourself ruler of this forest and soon the entire kingdom."
            ro "That… doesn’t sound like me at all. A boastful warrior is no warrior at all. "
            e 1 "Then who was I fighting earlier?"
            ro "I don’t know…"
            "Roushk’s forehead furrows and he shakes his head trying to recall what happened to him."
            ro "This is all so confusing, what did this thing do to me?"
            hide roushk stand with dissolve
            "Roushk shows his left wrist, and you notice the bracelet he is wearing."
            e 1 "What is that?"
            show roushk stand at center with dissolve
            ro "This is the thing that started this whole mess."
            ro "If it brought me here, it can take me back, but based on what you told me, I wasn’t acting like myself until you defeated me."
            ro "Then it’s possible there is something in this artifact then."
            ro "When I use it, it will possess me into that violent character."
            e 1 "I mean it’s possible. "
            ro "Then [name], I need your help."
            ro "This land is completely foreign to me, would you find it in your heart to help me find a way to remove the curse from this item so I may return home?"
            "Roushk pulls his foot back."
            ro "Please the other warriors and my mate, Othra will be worried sick that I suddenly disappeared."
            e 1 "First things first, I’m an adventurer."
            e 1 "Second, I’ll be willing to help."
            e 13 "A lot of crazy things have been happening in this fog."
            e 13 "Suddenly getting transported here by a cursed artifact is the least of the weirdness around here."
            ro "Thank you."
            hide roushk stand with dissolve
            "He extends a hand to you and you both shake hands to your new found bond."
            show roushk stand at center with dissolve
            ro "So, where do we start?"
            e 1 "Probably by introducing you to the tavern."
            e 1 "If they see me walking around with you without any explanation they’ll probably jump on you."
            ro "Ah, friends from a new land, I’d love to meet them."
            hide roushk stand with dissolve
            "You escort Roushk into the tavern."
        "Run and get help!" if True:

            $ Roushk.ke = 2
            "You dart from the left to the right, and manage to give the lizard the slip. "
            "Running as fast as you can you nearly reach the barn exit when you are tugged back by your cape."
            "One strong tug and you fling backwards into the lizard’s arms."
            "He spins you around and shoves you near to a wall."
            "The lizard rushes forward with both of his arms raised."
            "He lunges forward and slams against the spaces beside you, trapping you between his beefy arms."
            scene roushk rke with slow_dissolve
            "He looks at you with ferocious intensity, never breaking eye contact for even a second."
            "Strangely, your heart is beating fast, this scenario strangely makes you feel excited."
            "Red lizard" "Where in Aigran are we, wolf? Explain how you kidnapped me from the temple?"
            e 9 "Temple? Aigran? What are you talking about, I never heard of that place, and we didn’t come from a temple."
            "It troubles you that Hakan may be right, this lizard is a few marbles short."
            "You could knee him in the groin and make a run for help, but you decide to see how far you can reason with him."
            "Red lizard" "No, how can this not be Aigran? That’s the name of this whole world. "
            e 9 "Hey, I might be taught by my father but I know damn well this world isn’t Aigran."
            e 9 "Now calm yourself down, and let’s talk like civilized people."
            "Red lizard" "Or what you’re going to knee me in the groin?"
            "Your eyes widen in surprise."
            "Red lizard" "I can see the gears in your head turning, it’s the easiest strategy you can pull off."
            "Red lizard" "I will let you go, but any weird moves, and I’m pinning you down faster than you can call to your friends."
            "You reluctantly nod."
            scene barn 1 with slow_dissolve
            "The red lizard backs away giving you some room to breathe."
            show roushk stand at center with dissolve
            "Red lizard" "Start by explaining who you are, and where this is."
            e 1 "I am [name], and this is the Tavern of Spear."
            e 1 "Currently, we’re all trapped in this foggy forest."
            "Red lizard" "A foggy forest that traps people? This day just keeps getting better."
            e 1 "I’ve answered your questions, now tell me who you really are and what are you doing here?"
            hide roushk stand with dissolve
            "The red lizard claps his hands together in front of him."
            show roushk stand at center with dissolve
            ro "My name is Roushk, one half that leads the lizardmen tribe."
            ro "I can’t explain how I really got here."
            ro "I found an odd looking artifact during an expedition, and after a bright flash of light I ended up awakening here."
            e 5 "That’s not possible, don’t you remember fighting me just now in the swamp?"
            e 5 "You were declaring yourself ruler of this forest and soon the entire kingdom."
            ro "That… doesn’t sound like me at all. A boastful warrior is no warrior at all. "
            e 1 "Then who was I fighting earlier?"
            ro "I don’t know…"
            "Roushk’s forehead furrows and he shakes his head trying to recall what happened to him."
            ro "This is all so confusing, what did this thing do to me?"
            hide roushk stand with dissolve
            "Roushk shows his left wrist, and points to a bracelet."
            e 1 "What is that?"
            show roushk stand at center with dissolve
            ro "This is the thing that started this whole mess."
            ro "If it brought me here, it can take me back, but based on what you told me, I wasn’t acting like myself until you defeated me."
            ro "Then it’s possible there is something in this artifact then."
            ro "When I use it, it will possess me into that violent character."
            e 1 "I mean it’s possible. "
            ro "Then [name], I need your help."
            ro "This land is completely foreign to me, would you find it in your heart to help me find a way to remove the curse from this item so I may return home?"
            "Roushk holds his hands together and begs you with pleading eyes."
            ro "Please the other warriors and my mate, Othra will be worried sick that I suddenly disappeared."
            e 1 "First thing’s first, I’m an adventurer."
            e 1 "Second, I’ll be willing to help."
            e 13 "A lot of crazy things have been happening in this fog."
            e 13 "Suddenly getting transported here by a cursed artifact is the least of the weirdness around here."
            ro "Thank you."
            hide roushk stand with dissolve
            "He extends a hand to you and you both shake hands to your new found bond."
            show roushk stand at center with dissolve
            ro "So, where do we start?"
            e 1 "Probably by introducing you to the tavern."
            e 1 "If they see me walking around with you without any explanation they’ll probably jump on you."
            ro "Ah, friends from a new land, I’d love to meet them."
            hide roushk stand with dissolve
            "You escort Roushk into the tavern."

    $ Time.mins = Time.mins +30
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    play sound "music/door.mp3"
    scene tavern 1 with slow_dissolve
    $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
    play Chan1[ "<silence 0.5>", "music/tavern.ogg" ]fadein 3
    "The moment you enter the tavern, all hell breaks loose."
    "Starting with Hakan trying to jump at Roushk but trips on one of the beer bottles at his seat."
    "Witer rushes over with his frying pan and Chet right behind him with a bar stool. "
    "Luckily, you manage to calm things down."
    "You introduce everyone to the red lizard and explain to the best of your abilities how he has come from another world. "
    show snow stand1 at left with dissolve
    show roushk stand at right with dissolve
    s "So, you’re a leader of a lizard tribe from another world?"
    ro "It would seem that way, since no one here knows about Aigran."
    w "Wow, a traveller from another world, that’s so romantic. "
    ro "Glad you think so."
    h "My head is going to explode, if the whole world is going to come into this forest we might as well build a new kingdom here."
    c "That doesn’t sound like a bad idea, that just means more business for me."
    e 6 "Guys, focus."
    e 1 "I’ll be helping Roushk find a way to remove the curse on his artifact before he can use it to go home."
    show snow stand at left
    s "Sounds good, until it’s done, he can rent a room here."
    ro "Thank you for the offer Snow, but I am perfectly satisfied with staying in the barn."
    s "Are you sure?"
    ro "Very sure, it’s actually quite comfortable."
    w "So where are you planning to go to get his artifact fixed?"
    e 1 "I’ll need to talk it over with Roushk."
    e 6 "You guys mind if we have some privacy?"
    s "Not at all, alright give these two some privacy. "
    hide roushk stand
    hide snow stand with dissolve
    "He claps his left wrist signalling to everyone to go back to their work. "
    "Hakan even orders another beer from Witer."
    "The both of you find an empty table to discuss your plans."
    show roushk stand at center with dissolve
    ro "So what is this plan that you won’t let your other friends in on it?"
    e 6 "It’s complicated to explain, but I know someone who might be able to help us."
    e 1 "But you need to play along and don’t say anything to anyone about who I’m going to introduce you to."
    ro "Ok… you’re not sending me to speak some dangerous character are you?"
    e 5 "What? No? He’s....harmless?"
    e 1 "But he’s good with magic. Helped me out a few times already."
    e 1 "Now come with me and remember, just play along."
    hide roushk stand with dissolve
    "You stand up first and walk over to Snow, Roushk follows you from behind."
    show snow stand1 at center with dissolve
    e 1 "Hey Snow."
    s "Hmm? Are you two done figuring out your plans yet?"
    e 6 "Not yet, but Roushk would like a tour of the tavern so I thought I'd show him around."
    hide snow stand with dissolve
    "Snow looks over at Roushk. The red lizard just smiles."
    show snow stand1 at left with dissolve
    show roushk stand at right with dissolve
    s "Sounds fine to me."
    e 1 "Thanks, come on, I’ll show you where the beer is kept."
    show snow angry1 at left
    s "No free samples!"
    e 9 "I know!"
    hide roushk stand
    hide snow angry1 with dissolve
    "You open the basement door and lead Roushk down stairs."
    $ renpy.music.set_volume(1, 5, channel = "Chan1")
    play Chan1[ "<silence 0.5>", "music/drip.ogg" ]fadein 3
    scene basement 1 with dissolve
    "You walk over to the barrel where Meko’s horn sits. "
    show meko stand at center with dissolve
    e 1 "Meko, I brought someone over."
    m "For real?"
    m "Wow, I should have cleaned the place up if I knew I was getting company."
    "Roushk stands to your side looking at you with a perplexed look."
    e 1 "Ehh...This is Roushk."
    hide meko stand with dissolve
    "You point to the red lizard."
    show roushk stand at center with dissolve
    e 6 "Roushk, this is Meko."
    ro "..."
    ro "I’m starting to get worried now, there’s nobody there."
    e 5 "Oh shit, Meko turn off your invisibility spell."
    m "Right, I forgot."
    show meko stand70 at left with dissolve
    show roushk stand at right with dissolve
    ro "Woah, where did that horn come from?"
    m "Hello, I’m Meko. I’m [name]’s soulmate."
    e 9 "Friend, he’s my friend."
    ro "A talking horn? That’s amazing! "
    hide meko stand70
    hide roushk stand with dissolve
    "Roushk crouches down and moves his hands around Meko’s horn without touching him."
    show meko stand70 at left with dissolve
    show roushk stand at right with dissolve
    ro "How can this be? Are you like a horn that came to life?"
    m "More like a dead magic user that came back from the dead in the form of a horn."
    e 1 "Anyways, Roushk here is not from our world."
    e 1 "He used an artifact to get here, but it is cursed."
    e 1 "Last time, he became this dangerous fighter that wanted to take over the kingdom."
    e 1 "We need some way to remove the curse so he can use it. "
    m "A cursed item, show me."
    "Roushk shows Meko the metal bracelet."
    m "Hmm, are you able to take it off?"
    ro "I don’t know, let me-"
    hide meko stand70
    hide roushk stand with dissolve
    "The lizard grabs his bracelet and tries to pull it off but it would not come off."
    show meko stand70 at left with dissolve
    show roushk stand at right with dissolve
    ro "This thing won’t come off!"
    m "I figured as much. Whatever curse is on that thing must be strong. "
    e 1 "Can you remove the curse though?"
    m "Hmm… it will take me some time. I first need to relearn how to curse items, then to remove the curses."
    m "Maybe it’ll take a few days."
    e 9 "A few days? But is there a chance the bracelet’s curse will activate again?"
    m "It might, you beating Roushk once probably just weakened it."
    m "If he starts acting weird again it’s a sign the curse is powering back up. "
    m "We won’t know when that is though."
    ro "Then you need to lock me up, it is too risky, I won’t be able to control my actions."
    m "Instead of that, I suggest you two try to find other magic users around the area to see if they can get the curse removed quickly before I am ready."
    e 13 "The only other magic user I know is… "
    "You place your hand to your forehead and shake your head."
    e 8 "Why did it have to be him, but it’s not like I have a choice."
    e 1 "Tomorrow morning we will head out to the lizard tribe, that’s the best chance to find Selye."
    ro "I’ll follow your lead."
    ro "Come look for me when you’re ready. I will wait in the barn."
    ro "Also, good luck Meko. I hope you’ll be able to retrieve the spell to end all this."
    m "Leave it to me!"
    e 1 "Alright, let me just give you the rest of the tour and I’ll walk you to the barn."
    ro "Sounds good."
    hide meko stand70
    hide roushk stand with dissolve
    scene black with dissolve
    "After that, you take Roushk on the actual tour, showing him around the tavern area."
    "He listens intently, but doesn’t say much. "
    "You feel a little unsure if Roushk is taking all this in well, but you remain optimistic that tomorrow will be better."
    "Once the tour is over you return to your room to rest."
    $ Time.hours = Time.hours +2
    $ Roushk.barn = 1
    $ Roushk.lizardtribe = 1
    play sound "music/door.mp3"
    stop Chan1
    stop Chan2
    jump Room1
label Roushk_talk:
    scene barn 1
    show roushk stand at center with dissolve
    if Roushk.party == 2:
        e 1 "Hey Roushk."
        ro "[name], good to see you."
        e 1 "Have any plans for today?"
        ro "Just resting and probably cleaning up the barn before the celebrations tonight."
        ro "Would you like to join me?"
        ro "We can just spend the day cleaning and head to the party straight away."
        "(This action will push the time into the evening.)"
        menu:
            "Go to the party directly" if True:
                hide roushk stand with dissolve
                scene black with dissolve
                "You spend the day cleaning the barn."
                "Come evening you and Roushk head into the tavern."
                $ Time.hours = 18
                jump Roushk_meko_battle_end
            "Do other things for now" if True:
                e 1 "Maybe later, I’ve got some things to do for now."
                ro "Alright."
                $ Roushk.party = 3
                jump T_barn
    if Roushk.party == 3:
        ro "Want to help me clean the barn then head to the party?"
        "(This action will push the time into the evening.)"
        menu:
            "Go to the party directly" if True:
                hide roushk stand with dissolve
                scene black with dissolve
                "You spend the day cleaning the barn."
                "Come evening you and Roushk head into the tavern."
                $ Time.hours = 18
                jump Roushk_meko_battle_end
            "Do other things for now" if True:
                e 1 "Maybe later, I’ve got some things to do for now."
                ro "Alright."
                jump T_barn

    if Roushk.meko == 2:
        e 1 "Roushk! Meko has the spell ready."
        ro "Good, it’s time to put an end to this."
        ro "I don’t know if it’s because I’m suspicious."
        ro "I don’t think it’s so easy to solve."
        ro "Tell me when you are ready,Ok?"
        $ Roushk.meko = 3
        jump Roushk_talk1
    "You meet Roushk who’s sitting on a barrel."
    ro "Hey, [name]."
    label Roushk_talk1:

        if (Time.hours >= 0 and Time.hours <= 5)or(Time.hours >= 12 and Time.hours <= 24):
            if Roushk.bulltribe == 2:
                ro "How did it go?"
                e 1 "I spoke to Thane, he suggests we sneak in in the evening, but you’ll need a disguise. "
                ro "What a coincidence I bought one already from Chet earlier."
                e 5 "That’s some foresight."
                ro "You mentioned going into a dangerous no-lizard area. It makes sense to remain inconspicuous especially for someone like me. So, I took it upon myself to prepare accordingly."
                e 1 "Right, I should prepare my equipment too. I’ll come get you when I’m ready."
                $ Roushk.bulltribe = 3
            menu:
                "What do we need to do?" if True:
                    if Roushk.lizardtribe == 1:
                        ro "It’s far too late to head out, it will be dangerous."
                        ro "If you plan to go to find Selye I suggest we do it in the morning."
                        e 1 "Alright."
                    if Roushk.bulltribe == 1:
                        ro "Oh, didn’t you say you were going to the bull tribe to talk to a friend so we can find a way into their temple?"
                        e 1 "Right, I’m on it."
                    if Roushk.bulltribe == 3:
                        if (Time.hours >= 0 and Time.hours <= 5)or (Time.hours >= 18 and Time.hours <= 24):
                            ro "We’re supposed to go to bull tribe right?"
                            menu:
                                "Let's go" if True:
                                    e 1 "Ready?"
                                    ro "Got my cloak, let’s go."
                                    "Roushk puts on the cloak and follows you from behind."
                                    hide roushk stand with dissolve
                                    jump Roushk_bulltribe
                                "Not now" if True:
                                    e 1 "Not yet."
                                    ro "OK, find me when you're ready."
                        elif True:

                            ro "It’s still too early to head out."
                            ro "We’ll need to wait until evening before we can go to the bull tribe."
                            ro "Best prepare your equipment until the time is right."
                    if Roushk.meko == 1:
                        ro "We’ve exhausted most of our options already."
                        ro "Please see if Meko has made any progress."
                        ro "Then we’ll talk further."
                        jump Roushk_talk1
                    if Roushk.meko == 3:
                        ro "We need to meet Meko right?"
                        ro "I don’t know if it’s because I’m suspicious."
                        ro "I don’t think it’s so easy to solve."
                        ro "Find me when you're ready, ok?"
                        menu:
                            "Let's go" if True:
                                e 1 "Ready?"
                                ro "Always, let’s go."
                                hide roushk stand with dissolve
                                jump Roushk_meko
                            "Not now" if True:
                                e 1 "Not yet."
                                ro "OK, find me when you're ready."
                        jump Roushk_talk1
                    jump Roushk_talk1
                "Leave" if True:
                    hide roushk stand with dissolve
                    jump T_barn
        elif True:
            if Roushk.bulltribe == 2:
                ro "How did it go?"
                e 1 "I spoke to Thane, he suggests we sneak in in the evening, but you’ll need a disguise. "
                ro "What a coincidence I bought one already from Chet earlier."
                e 5 "That’s some foresight."
                ro "You mentioned going into a dangerous no-lizard area. It makes sense to remain inconspicuous especially for someone like me. So, I took it upon myself to prepare accordingly."
                e 1 "Right, I should prepare my equipment too. I’ll come get you when I’m ready."
                $ Roushk.bulltribe = 3
            menu:
                "What do we need to do?" if True:
                    if Roushk.lizardtribe == 1:
                        ro "We’re supposed to go to find this person called Selye right?"
                        menu:
                            "Let's go" if True:
                                e 1 "Ready to go?"
                                ro "Always."
                                hide roushk stand with dissolve
                                jump Roushk_lizardtribe
                            "Not now" if True:
                                e 1 "Not yet."
                                ro "OK,find me when you're ready."
                    if Roushk.bulltribe == 1:
                        ro "Oh, didn’t you say you were going to the bull tribe to talk to a friend so we can find a way into their temple?"
                        e 1 "Right, I’m on it."
                    if Roushk.bulltribe == 3:
                        ro "It’s still too early to head out."
                        ro "We’ll need to wait until evening before we can go to the bull tribe."
                        ro "Best prepare your equipment until the time is right."
                    if Roushk.meko == 1:
                        ro "We’ve exhausted most of our options already."
                        ro "Please see if Meko has made any progress."
                        ro "Then we’ll talk further."
                        jump Roushk_talk1
                    if Roushk.meko == 3:
                        ro "We need to meet Meko right?"
                        ro "I don’t know if it’s because I’m suspicious."
                        ro "I don’t think it’s so easy to solve."
                        ro "Find me when you're ready, ok?"
                        menu:
                            "Let's go" if True:
                                e 1 "Ready?"
                                ro "Always, let’s go."
                                hide roushk stand with dissolve
                                jump Roushk_meko
                            "Not now" if True:
                                e 1 "Not yet."
                                ro "OK,Find me when you're ready."
                        jump Roushk_talk1

                    jump Roushk_talk1
                "Leave" if True:
                    hide roushk stand with dissolve
                    jump T_barn

label Roushk_lizardtribe:
    if Roushk.lizardtrio == 0:
        play sound "music/foot1.ogg"
        $ Time.hours = Time.hours +1
        scene black with dissolve
        "..."
        scene crossroad 1 with slow_dissolve
        "As you reach the crossroads you turn to Roushk who gives you a gentle smile."
        "The two of you haven’t spoken a word since you left the tavern."
        "That is until Roushk breaks the silence."
        show roushk stand at center with dissolve
        ro "So what can you tell me about this lizard tribe of yours?"
        e 1 "Well it’s run by their leader Nauxus, a very charismatic leader."
        e 1 "The tribe is hidden in the swamp. They are currently having some problems with a bull tribe that also lives in this forest."
        ro "How serious are their problems with each other?"
        e 13 "Serious enough that they are trying to murder one another."
        ro "Hmm, is it safe for us to head over there then?"
        e 1 "It’s ok, the war hasn’t really blown up yet."
        e 1 "Plus we need a magic user to look into this, and there are not that many of them around."
        e 1 "They live pretty secluded lives."
        ro "So magic is rare around here? That’s about the same from where I’m from."
        ro "We typically rely on herbs and magical items for magic."
        e 1 "Oh hey, what is your tribe like?"
        ro "My tribe is filled with the strongest of lizard warriors, and healers."
        ro "I run the tribe in an ancient temple with my mate Othra, the priestess of the tribe."
        ro "She’s the expert on magic in my tribe."
        e 1 "A mate, wow. You look pretty young to have a mate."
        ro "She is a beautiful lizard, I can’t imagine my life without her."
        ro "Unlike me she has powerful patience and wisdom. "
        e 1 "She sounds like a nice person."
        ro "Yes she is. Do you have someone you are mated to?"
        e 1 "Well…"
        ro "Perhaps one of your tavern mates?"
        hide roushk stand at center with dissolve
        "You blush and let out a fake cough. "
        "Rhousk laughs."
        show roushk stand at center with dissolve
        e 10 "Oh would you look at that, we've nearly reached the swamp. Let’s head forward."
        hide roushk stand at center with dissolve
        play sound "music/foot1.ogg"
        $ Time.hours = Time.hours +1
        scene black with dissolve
        "..."
        scene lizardtribe 1 with dissolve
        ro "This place looks so homey, I’m impressed."
        e 1 "Tell that to the chief, but we’ll save that for later."
        e 1 "Let’s go find Selye, he’s the tribe’s magic user."
        scene black with dissolve
        "You both head up the stairs to Selye’s hut."
        scene tree 1 with dissolve
        if Quest.campw1 != 3:
            "At the top the steps three figures block your way."
            "They stand with arms crossed."
            "The middle lizard takes a step forward and puffs out his chest."
            "First Lizard Guard" "Halt, you face the might of the Lizard Trio!"
            "The other two lizards on cue turn to the side and perform a pose with their individual weapons."
            e 9 "Huh?"
            show roushk stand at center with dissolve
            ro "Is this a ritual of this tribe?"
            e 1 "No, look whoever you three are, can you please just move."
            e 1 "We need to see Selye."
            "Second Lizard Guard" "Can you believe this guy? He’s forgotten who we are already."
            "First Lizard Guard" "We’re the lizard guards who worked under Selye! We met before."
            e 5 "The heck happened to the three of you?"
            "First Lizard Guard" "We rebranded ourselves."
            "First Lizard Guard" "Now, Selye says not to let you near his hut, he has no time for you right now."
            ro "Please, from one lizard to another, I am a lost traveler and I seek the help of your mage to get back home."
            "Second Lizard Guard" "Orders are orders. We can’t let you see him."
            ro "Oh dear, it doesn’t seem like talking to them is going to get us through."
            hide roushk stand at center with dissolve
            "Roushk leans in near you and whispers."
            ro "Try to butter them up, maybe they’ll let us through then."
            e 1 "Look… I just realized I have no idea what your names are."
            "The first lizard guard sneers. He beats his chest with one fist."
            "First Lizard Guard" "Then get ready for a proper introduction, Wolf."
            "First Lizard Guard" "I’m the leader of the group, Nuo!" with vpunch
            "Second Lizard Guard" "I’m Duo!" with vpunch
            "Third Lizard Guard" "Blep." with vpunch
            show lizard trio at center with dissolve
            play sound "music/silly.mp3"
            "Lizard Trio" "And we’re the Lizard Trio!" with vpunch
            e 1 "..."
            "They break into their poses again."
            "You blink in disbelief at how confident they are in their poses."
            e 1 "Wow, you guys sound so cool, I didn’t know you were a group before."
            "Duo" "We just formed the team today, and the Lizard Trio has never been defeated once."
            ro "Well, you just made your team official today."
            "Nuo" "Hey, you calling us weak?"
            "Duo" "No one mocks the Lizard Trio!"
            ro "No, I’m just pointing out that-"
            "Blep" "Blep will destroy all enemies of Lizard Trio."
            "The way Blep delivers his threat with a straight face unnerves you."
            "Duo" "Blep, since when did you start referring to yourself in the third person?"
            "Blep" "Blep trying something new."
            "Nuo" "Nuo like it, Nuo will do it too! "
            "Blep" "No, only Blep can do this."
            ro "Maybe you three can step aside and try to settle this while we speak to Selye."
            "Nuo" "There he goes cutting us off. You dare disrespect the Lizard Trio?"
            "Nuo" "That’s it, we’re going to teach you guys that no one messes with us."
            ro "I wasn’t even messing with anything."
            "Roushk turns to you, pleading for you to jump in."
            "Duo" "Oh, now you’re calling us silly!"
            "Nuo" "Attack!"
            e 5 "Roushk, get back!"
            "You push Rosuhk back and draw your sword ready to fight."
            label Roushk_lizardtribe_battle:
                $ Map.good_battle = True
                $ Battle.holyfcd = 0
                $ wolf_max_hp = 250
                $ wolf_hp = wolf_max_hp
                $ players_turn = False
                $ wolf_max_lust = 100
                $ wolf_lust = 0

                $ renpy.music.set_pause(True, channel='Chan1')
                $ renpy.music.set_pause(True, channel='Chan2')
                if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
                    $ Zalt.cor = min(Zalt.cor +2, 100)
                jump Roushk_lizardtribe_battle_loop
            label Roushk_lizardtribe_battle_loop:

                show screen simple_stats_screen
                show screen battle_menu
                play music "<loop 4.6903>music/forest_fight_small.ogg"
                show lizard trio at center
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
                        e 0 "I can't fight anymore.."
                        "The enemy is too strong."
                        "You’re knocked onto the ground."
                        jump Roushk_lizardtribe_battle_lose
                    if res == "Flirt":
                        $ Random = renpy.random.randint(1, 5)
                        if Random == 1:
                            $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                            $ wolf_lust = wolf_lust+Zalt.flirt
                            "You perform a seductive dance."
                            "The trio are breathing heavily, you can see Duo’s loincloth protruding forward where his cock is."
                        elif Random == 2:
                            $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                            $ wolf_lust = wolf_lust+Zalt.flirt
                            "You bravely flash your legs, flexing your calves at the trio."
                            "The trio’s faces blush red, they shake their heads to snap themselves from falling for your tricks."
                        elif Random == 3:
                            $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                            $ wolf_lust = wolf_lust+Zalt.flirt
                            "You flex your arms and kiss your bicep with a wink."
                            "The trio’s faces blush red, they shake their heads to snap themselves from falling for your tricks."
                        elif True:

                            $ Random = renpy.random.randint(1, 3)
                            if Random == 1:
                                "You perform a seductive dance."
                            elif Random == 2:
                                "You bravely flash your legs, flexing your calves at the trio."
                            elif True:
                                "You flex your arms and kiss your bicep with a wink."
                            "The lizards slap each other, breaking themselves from the influence of your lustful moves."
                        if wolf_lust >= 100:
                            hide screen simple_stats_screen
                            hide screen battle_menu
                            hide screen battle_skill
                            hide screen battle_item
                            jump Roushk_lizardtribe_battle_win
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
                        "You need to protect Roushk!"
                    elif True:
                        pass
                    if wolf_hp <= 0:
                        jump Roushk_lizardtribe_battle_win

                    $ Random = renpy.random.randint(1, 7)
                    if Random == 1:
                        $ Random = renpy.random.randint(1, 100)
                        if Random <= Battle.dodge:
                            "Nuo" "Formation Papaya-Angelfish-Ingot-Nuts."
                            "Duo and Blep come in from both sides, you’re only able to block one of their attacks."
                            "Now that you’re distracted, the other lizard attempts to strike you from behind."
                            "You try to turn in time but he was just a decoy."
                            "A surprise attack comes from in front, Nuo fires an arrow with his crossbow."
                            "But you dodged his attack!"
                        elif True:
                            $ wolf_damage = renpy.random.randint(15, 45)
                            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                            "Nuo" "Formation Papaya-Angelfish-Ingot-Nuts."
                            "Duo and Blep come in from both sides, you’re only able to block one of their attacks."
                            "Now that you’re distracted, the other lizard attempts to strike you from behind."
                            "You try to turn in time but he was just a decoy."
                            "A surprise attack comes from in front, Nuo fires an arrow with his crossbow, hitting you in the shoulder."
                    elif Random == 2:
                        "Nuo and Duo run up and each grab one of your arms, locking them behind you."
                        "Blep runs forward and grabs your face forcing your snout against his crotch."
                        "The musky scent of his groin strangely arouses you."
                        $ wolf_damage = renpy.random.randint(0, 15)
                        $ Zalt.lust += wolf_damage
                    elif Random == 3:
                        "Blep fires a dart into your neck."
                        "You manage to pull out the dart but suddenly, you are feeling comfortably warm."
                        "Your crotch feels especially hot, and your hand is itching to grope yourself."
                        $ wolf_damage = renpy.random.randint(15, 30)
                        $ Zalt.lust += wolf_damage
                    elif Random == 4:
                        $ Random = renpy.random.randint(1, 100)
                        if Random <= Battle.dodge:
                            "Duo" "Eat this!"
                            "Duo throws a flurry of small knives."
                            "But you dodged his attack!"
                        elif True:
                            $ wolf_damage = renpy.random.randint(20, 30)
                            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                            "Duo" "Eat this!"
                            "Duo throws a flurry of small knives."
                            "You are unable to swipe them away fast enough with your sword, some cuts you."
                            "The other two lizards take advantage of your stunned state to sweep you off your feet with their tails before leaping back."
                    elif Random == 5:
                        $ Random = renpy.random.randint(1, 100)
                        if Random <= Battle.dodge:
                            "Blep" "Blep’s turn."
                            "Blep throws a smoke bomb onto the ground. A thick cloud of smoke surrounds the battlefield. "
                            "You’ve lost track of the lizards."
                            "Then from out of nowhere, several fists come flying out of the smoke hitting you from every side."
                            "But you dodged their attack!"
                        elif True:
                            $ wolf_damage = renpy.random.randint(10, 40)
                            $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                            "Blep" "Blep’s turn."
                            "Blep throws a smoke bomb onto the ground. A thick cloud of smoke surrounds the battlefield. "
                            "You’ve lost track of the lizards."
                            "Then from out of nowhere, several fists come flying out of the smoke hitting you from every side."
                    elif Random == 6:
                        "Nuo" "Let’s try our new move! Black Leaves Swarm!"
                        "Blep spins his spear around his body, he passes the weapon from hand to hand in a quick motion."
                        "With his final spin the spear spins horizontally and smacks his two friends in their guts."
                        "Duo and Nuo collapse to the ground in pain."
                        "Nuo" "Bad idea."
                    elif True:
                        "Nuo is distracted by doing odd poses with his crossbow."
                        "Nuo" "Pew, Pew, you’re going down!"
                        "Duo and Blep smack him in the head for messing around."

                    if Battle.holyfcd !=0:
                        $ Battle.holyfcd = Battle.holyfcd-1
                if wolf_hp <= 0:
                    if Zalt.hp <= 0:
                        jump Roushk_lizardtribe_battle_win
                    elif True:

                        jump Roushk_lizardtribe_battle_win

                elif Zalt.hp <= 0:
                    jump Roushk_lizardtribe_battle_lose
                elif Zalt.lust >= Zalt.maxlust:
                    "You're too horny to fight anymore."
                    "You fall to the ground."
                    jump Roushk_lizardtribe_battle_lose
                elif True:
                    jump Roushk_lizardtribe_battle_loop
            label Roushk_lizardtribe_battle_win:
                $ renpy.music.set_pause(True, channel='Chan1')
                $ renpy.music.set_pause(True, channel='Chan2')
                play music "music/forest_fight_small_end.ogg" noloop
                pause 1
                hide lizard trio with slow_dissolve

                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                if wolf_lust >= 100:
                    "The trio drop onto their bellies. Their long tongues extend outwards as they pant heavily."
                    "{b}{color=#19c22a} <[name] gained one Level-up-point.>{/color}"
                    $ Zalt.points = Zalt.points +1
                    e 3 "I can still keep going!"
                    "Lizard Trio" "No!"
                    "Nuo" "Guh, you win. We admit defeat. No more seductive moves please."
                    "Nuo" "My cock can’t take it anymore."
                    "Duo" "Nuo, I can’t move. I think even the slightest breeze will make me erupt."
                    "Blep" "Blep has never felt so horny."
                    "Roushk walks over to you."
                    show roushk stand at center with dissolve
                    ro "My friend here has defeated you three in fair combat, I am certain you won’t have trouble with us seeing Selye now."
                    "Nuo" "You can’t. Selye’s not home, he left early this morning to do some errands."
                    "Nuo" "We don’t know when he’ll be back."
                    e 5 "What? Why didn’t you just say that from the beginning?"
                    e 5 "We didn’t have to waste our time here."
                    e 13 " Fine, let’s just go see Nauxus maybe he can help us out."
                    "Duo" "Chief Nauxus hasn’t been seen since this morning either."
                    "You stare in disbelief at the trio. "
                    "For some reason your body feels heavier than a minute ago."
                    "With a heavy sigh you motion to Roushk to follow you down the stairs."
                    scene lizardtribe 1 with dissolve
                    show roushk stand at center with dissolve
                    ro "What do we do now?"
                    e 1 "We should head back for now."
                    hide roushk stand at center with dissolve
                    scene black with dissolve
                    $ Time.hours = Time.hours +2
                    "..."
                    scene barn 1 with dissolve
                    show roushk stand at center with dissolve
                    ro "Make sure to treat your wounds, then come find me in the barn if you wish to talk."
                    jump Roushk_lizardtribe_night
                elif True:
                    "Duo and Blep fall onto the ground leaving only Nuo standing."
                    "Their leader drops his weapon and raises his hands up in defeat."
                    "Nuo helps his fallen teammates up on their feet."
                    "{b}{color=#19c22a} <[name] gained one Level-up-point.>{/color}"
                    $ Zalt.points = Zalt.points +1
                    show roushk stand at center with dissolve
                    ro "Now move aside so we may speak with Selye."
                    "Duo" "You can’t, he’s not home today. Not sure when he’ll be back."
                    e 5 "What? Why didn’t you just say that from the beginning?"
                    e 5 "We didn’t have to waste our time here."
                    e 13 " Fine, let’s just go see Nauxus maybe he can help us out."
                    "Duo" "Chief Nauxus hasn’t been seen since this morning either."
                    "You stare in disbelief at the trio. "
                    "For some reason your body feels heavier than a minute ago."
                    "With a heavy sigh you motion to Roushk to follow you down the stairs."
                    scene lizardtribe 1 with dissolve
                    show roushk stand at center with dissolve
                    ro "What do we do now?"
                    e 1 "We should head back for now."
                    hide roushk stand at center with dissolve
                    scene black with dissolve
                    $ Time.hours = Time.hours +2
                    "..."
                    scene barn 1 with dissolve
                    show roushk stand at center with dissolve
                    ro "Make sure to treat your wounds, then come find me in the barn if you wish to talk."
                    jump Roushk_lizardtribe_night

            label Roushk_lizardtribe_battle_lose:
                $ qty = int(jane_inv.qty(coin)*0.2)
                $ jane_inv.drop(coin,qty)
                $ Zalt.lust = 0
                $ Zalt.hp = 1
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                if Zalt.hp <= 0:
                    "You collapse on the ground, unable to battle."
                    "Roushk runs over to pick you up."
                    "Blep" "Blep take."
                    "Blep snatches your coin pouch when you’re distracted and takes [qty] coins from it before tossing the pouch back."
                    "Blep" "This will buy us food."
                elif True:
                    "You fall to your knees, and cover your crotch in shame. "
                    "Duo" "I’ll take that."
                    "Duo snatches your coin pouch when you’re distracted and takes [qty] coins from it before tossing the pouch back."
                    "Duo" "This should be enough for a round of beer. "
                    "Nuo" "Hah, you didn’t stand a chance. Go back and deal with that-"
                    "Nuo points at your crotch."
                    "Nuo" "Before you try to take us on again. If you dare!"
                hide lizard trio with dissolve
                ro "Excuse me, I think you three are forgetting one thing."
                "Duo" "What?"
                show roushk stand at center with dissolve
                hide roushk stand at center with dissolve
                "Roushk rushes in and punches Duo in the gut."
                "You can see the lizard’s eyes pop out from the force of the impact."
                "Then, just as quickly, he throws Duo to the ground before giving a generous kick. Roushk’s kick connects squarely to Nuo’s face, sending him flying a few feet back."
                "Blep rushes forward with his spear but Roushk dodges his attack, grabbing the weapon by the middle of the shaft, Roushk pulls on it tripping Blep forward."
                "Roushk then knees him right in the groin."
                "Blep coughs out in pain and collapses to the ground."
                "All three lizards wriggle in pain from the surprise attack."
                "Roushk signals to you to get up. You walk over to him."
                show roushk stand at center with dissolve
                ro "You forgot that I was here."
                e 9 "That was… amazing!"
                "Roushk smiles at you."
                ro "Yes, well I was more surprised you left me out of a fight. I am here to help you out you know."
                ro "There, the three of you have been defeated. I take it you won’t have any issues with us going to see Selye now?"
                "Nuo" "You… can’t. Ouch. He’s gone out to find runestones."
                "Nuo" "He-ngh! We don’t know when he’ll be back."
                e 5 "What? Why didn’t you three just say that from the start?"
                e 5 "We’ll have to go find Nauxus, and see if he can help bring Selye back."
                "Duo" "Chief Nauxus has been missing since this morning. We don’t know where he is."
                "Duo rubs his hurt jaw."
                "Blep" "Blep balls have died."
                "You stare in disbelief at the trio. "
                "For some reason your body feels heavier than a minute ago."
                hide roushk stand at center with dissolve
                scene black with dissolve
                $ Time.hours = Time.hours +1
                "With a heavy sigh you motion to Roushk to follow you down the stairs."
                scene lizardtribe 1 with dissolve
                show roushk stand at center with dissolve
                ro "What do we do now?"
                e 1 "We should head back for now."
                hide roushk stand at center with dissolve
                scene black with dissolve
                $ Time.hours = Time.hours +2
                "..."
                scene barn 1 with dissolve
                show roushk stand at center with dissolve
                ro "Make sure to treat your wounds, then come find me in the barn if you wish to talk."
                jump Roushk_lizardtribe_night
        elif True:
            "At the foot of the steps to Selye’s hut a single lizard warrior guards the entrance."
            "Lizard warrior" "Halt, what business do you have here Wolf?"
            e 1 "We’re just looking for Selye to ask for his help."
            "Lizard warrior" "That would not be possible. Advisor Selye isn’t in his hut today."
            e 5 "What? Where did he go?"
            "Lizard Warrior" "He left a note."
            "The lizard pulls out a small parchment from his satchel."
            "Lizard Warrior" "Ehem...mi mi mi."
            e 1 "What are you doing?"
            "Lizard Warrior" "I’m trying to get into character. "
            "Lizard Warrior" "Ehem, ssssimpleton-"
            e 8 "Oh no, he’s doing the voice too."
            "Lizard Warrior" "If you try to sssseek me out, I am not going to be around for a while."
            "Lizard Warrior" "I must find new stones for runes before Chief Nauxus’s next plan."
            "Lizard Warrior" "Sssso, keep your dirty hands off of my hut."
            "Lizard Warrior" "And that’s all the note wrote."
            show roushk stand at center with dissolve
            ro "This is quite a predicament, maybe the village chief can give us some advice? "
            e 1 "Yeah, let’s go see Nauxus then."
            "Lizard Warrior" "That won't be possible either."
            "Lizard Warrior" "Chief Nauxus hasn’t been seen since this morning."
            "Lizard Warrior" "Nobody knows where he went."
            e 5 "Can this day get any worse?"
            ro "Well we have more time for that tour around the village."
            e 1 "Sure, why not right?"
            hide roushk stand at center with dissolve
            "You spend the day showing Roushk around the lizard village."
            "By the time you both return to the tavern it’s already evening."
            $ Time.hours = 18
            "..."
            scene barn 1 with dissolve
            show roushk stand at center with dissolve
            ro "Make sure to treat your wounds, then come find me in the barn if you wish to talk."
            jump Roushk_lizardtribe_night
label Roushk_lizardtribe_night:
    e 1 "Roushk?"
    ro "Anything else?"
    e 1 "I haven’t seen you take a step into the tavern since you first met everyone, don’t you want to get a drink inside ?"
    ro "I didn’t want to intrude, my concerns about going back home aren't doing much good for my mood."
    hide roushk stand at center with dissolve
    "You take a seat next to Roushk."
    e 1 "I get that feeling. It’s like you’re feeling really on edge all the time."
    show roushk stand at center with dissolve
    ro "Yes it is. I’m sorry, I didn't mean to trouble you with my problem again."
    e 1 "No, it’s fine. I found it really helpful when I first came here that I had my friends in the tavern to talk to."
    e 1 "Then the work came in and it kept my mind off from worrying."
    ro "Your tavern friends sound like good people. Maybe I do need to speak to them a bit more."
    ro "After all, how often do I get to make friends with people from other worlds."
    ro "Or if I have to stay here long enough, I shouldn’t be rude to my future neighbours."
    e 6 "That’s the spirit."
    ro "But first, any plans on how to deal with this corrupted item?"
    "You cross your arms and think hard."
    e 1 "Hmm… I’m not really sure waiting for Selye will do us much good."
    ro "If only we were back in my tribe."
    ro "There’s a legend that somewhere near the old temple there is a magical lake that has magical cleansing properties."
    ro "I wonder if that would have worked on this artifact."
    e 5 "Lake… a lake! That’s it."
    ro "Excuse me?"
    e 1 "There’s a pool in the bull village. It has the power to cure corruptions."
    e 1 "This might be a long shot, but I think we should try it."
    ro "Ok, then let's go."
    e 13 "One problem, the bulls dislike the lizard tribe here."
    e 1 "They may attack you on sight."
    ro "Can’t they be reasoned with? I’m not from their tribe."
    e 6 "Doubt they’ll listen."
    e 6 "Let’s play it safe, come morning I’ll talk to a friend of mine there to see what he can do to help."
    ro "Very well. Come find me once you figure a way up with this friend of yours."
    ro "Until then, I think I’ll take a look around the tavern when I’m ready."
    $ Roushk.snow = 1
    $ Roushk.hakan = 1
    $ Roushk.witer = 1
    $ Roushk.chet = 1
    $ Roushk.passoutguy = 1
    $ Roushk.lizardtribe = 2
    $ Roushk.bulltribe = 1
    $ Time.hours = Time.hours +1
    jump T_barn
label Roushk_bulltribe:
    scene black with dissolve
    "Just as Thane told you, the village is almost empty."
    "You and Roushk manage to hide behind the cover of shadows while a pair of guards go on their patrol."
    "Keeping yourselves hidden from view, you make it to the foot of the steps leading to the bull temple."
    "Making your way up the mountain, you wish you had the time to tell Roushk about the area around you. If only there was proper lighting and no threat of getting caught by the angry bulls."
    scene bulltribe 1n with slow_dissolve
    scene mountain 1n with slow_dissolve
    scene temple 1n with slow_dissolve
    play music [ "<silence 1.0>", "music/bulls_temple.ogg" ] fadein 3
    ro "We’ve made it."
    ro "Wow, what a view."
    "Moonlight illuminates the ancient temple, and the lake surrounding it."
    "The waters bounce back the moon’s rays, making it appear like the temple sits on a bed of diamonds."
    ro "Looking at that temple, it really reminds me of the one we live in back home."
    e 1 "Yeah? Does yours have a magical lock on it at night?"
    ro "No it does not."
    ro "So, this means we can’t go in yet?"
    e 13 "Not until morning comes."
    e 1 "We can rest in the tent till then."
    ro "Let’s then."
    "You both pull out the mats and blankets the bulls keep nearby, and ready the tent for sleep."
    e 9 "Sorry, excuse me."
    ro "Ah, sorry I elbowed you."
    e 1 "It’s ok, let me just scootch a bit."
    "The two of you lie down facing the top of the tent."
    e 13 "This is cozy."
    ro "I don’t mind, once in a while after a long training session I like to share the temple floor with the other warriors."
    ro "It feels a bit secure like this."
    "You lie in silence for a bit, it’s hard to fall asleep."
    e 1 "You know, I still can’t believe you’re from another world."
    ro "Well I can’t believe I’m in another world."
    e 1 "Can you tell me more about the place you live in?"
    ro "Well the temple we live in, it’s actually built by some ancient civilization we don’t know of."
    ro "To the west there is the town the humans built."
    ro "We don’t go near the town because the humans are afraid of us."
    ro "Even further, well it’s hard to say. I usually can’t go far from the temple."
    e 1 "Humans? So it’s not a world of just lizardmen?"
    ro "Nope, there are all kinds of species on Aigran."
    ro "What about your world? I hope it isn’t all trapped in fog like this."
    e 1 "No, no. There’s lots to see."
    e 13 "My village especially, has a nice river nearby where you can go fishing."
    e 13 "Plus the wolves there are all friendly, especially my father."
    e 1 "Hmm…"
    ro "Something on your mind?"
    e 1 "I just miss home I guess, haven’t seen anyone from there in forever."
    e 13 "There’s so much I want to tell them."
    ro "Tell me more about your tribe. Is there something special about it?"
    e 1 "Well, we have the blessing ritual."
    ro "And… what’s that?"
    "Roushk yawns, your eyelids also start to feel heavy."
    e 1 "It’s a ritual where the warriors of the village receive a blessing from the elders."
    e 1 "The ritual involves the elder mating with the younger wolf. "
    e 13 "It’s supposed to symbolize the wolf becoming a true warrior, and to remind them the burden of mating."
    ro "Mating?"
    e 1 "Yeah, it’s not uncommon."
    ro "And you haven’t done this ritual?"
    e 6 "No, not yet. I’m still traveling to find a grand treasure to bring back to the village."
    e 6 "Until that is done I will not be able to return and receive the ritual."
    ro "Is that how you ended up here? Searching for a grand treasure?"
    e 1 "Kind of. What about you? What got you stuck with a cursed bracelet anyways?"
    ro "Honestly, I just followed a treasure map one of the scouts found."
    ro "I picked up the bracelet thinking it would have been a beautiful gift for Othra."
    ro "Damn thing stuck onto me, and next thing I know, I’m in your barn."
    e 1 "Classic treasure hunting mishap. Can’t wait for me to experience that."
    "Roushk laughs."
    ro "You’re crazy."
    e 13 "Crazy for adventure. Yeah, maybe I’ll be able to go to another world someday."
    ro "That would be the day. It sounds like... "
    ro "Like a…"
    ro "Zzz."
    "Roushk is snoring now. You chuckle a bit and close your eyes too."
    scene black with dissolve
    "..."
    $ Zalt.hp = Zalt.maxhp
    $ Zalt.mp = Zalt.maxmp
    if Time.hours >=21:
        $ Time.days = Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
    elif True:
        $ Time.hours = 6
        $ Time.mins = 30
    scene temple 1 with dissolve
    "Come morning, you and Roushk are ready to head into the temple."
    "Inside the prayer hall you both approach the glowing pool."
    e 1 "Try sticking your foot into the water."
    "Roushk nods."
    "He sits on the edge and slowly places his left arm into the pool."
    e 1 "Feel anything?"
    ro "Nothing different. Maybe it takes a bit longer?"
    "You two sit in silence waiting for something to happen."
    "After a while has passed. "
    e 1 "How is it now?"
    ro "I don’t think it’s working. "
    "The lizard stands back up and lets out a heavy sigh."
    ro "Thanks for trying."
    e 13 "I’m sorry."
    ro "No, it’s fine, we still have Meko."
    ro "Let’s just get back and see how that goes."
    e 13 "RIght, we can’t give up hope yet."
    e 1 "Why don’t we catch some lunch and rest before evening comes."
    e 1 "It’s safer to travel in the dark."
    ro "Well I’m hungry, is the lake here filled with fish?"
    e 1 "Definitely, let’s go catch some fish."
    "Making your way to the lake you both strip down to your loincloths and jump into the cold lake waters."
    "In seconds, your eyes adjust to the waters and you spot your prey."
    "You kick your legs and with a quick swipe, you catch a fish and quickly swim upwards to toss it over to the ground."
    " Diving back again you go for another fish, but a red figure dashes in front of you and catches it before you get a chance."
    "Roushk moves like a speeding arrow that can travel in the water, jettisoning himself from one side to another."
    "He manages to catch two fishes before heading back up."
    "Not wanting to be outdone, you too manage to grab another fish and toss it onto land."
    "Once you return to dry land, you shake the water off your fur and join Roushk who’s already by the campfire that he had started making."
    e 5 "Wow, you work fast."
    ro "I’ve gotten a lot of practice."
    ro "Take a seat, the fishes are still cooking."
    "The heat from the fire is soothing after that cold swim."
    "Roushk watches the skewered fishes intently, turning them when needed."
    e 6 "This takes me back, Thane took me up here the first time I came to the temple, he fished for lunch too, but not as elegant as you did."
    e 6 "The fish ended up taking him back into the lake."
    "Roushk laughs lightly."
    ro "He sounds like a funny guy. I would love to meet him."
    e 5 "Oh yeah, you guys haven’t met."
    e 1 "Thane lives here in the bull tribe with his father, Chief Axel."
    ro "Son of a tribe chief, that doesn’t sound easy."
    e 1 "It isn’t, especially when he doesn’t agree with his father’s stance on lizards."
    ro "So this Chief Axel, what does he have against the lizard-kind?"
    e 1 "It’s complicated, Chief Axel didn’t used to hate all lizards, there was a time of peace once when he and Chief Nauxus worked together to help get their people out of the fog."
    e 1 "Then one day, everything changed when children from both sides started getting kidnapped."
    e 1 "Both the chiefs blame each other for hiding the culprit."
    e 13 "Thane gets stuck in between them, he doesn’t want either side to go to war."
    e 13 "He believes both sides to be innocent."
    ro "If he has proof, why doesn’t he show it."
    e 1 "He’s still looking, but regardless, going to war now won’t solve anything."
    e 13 "We’re all still stuck here."
    "The fire crackles, and Roushk turns a fish."
    ro "It sounds like a complicated situation,and you’re involved?"
    e 1 "Somewhat, it’s the only way to keep the tavern safe."
    e 1 "I don’t like to think about what’s going to happen next."
    e 13 "Either one of the chiefs dies, or Thane and I go down."
    "Roushk doesn’t say a word. He merely turns the fish, and offers you a cooked one."
    "He picks one stick of fish for himself and bites into it."
    ro "Listen, I will not deny that I am a lizard of peace so I have my views about war."
    ro "But, if you go to war, don’t take it lightly. Lives will be taken. if not yours, maybe someone else who matters to others too."
    ro "So, think it through. Ask yourself why you make your choices."
    "You munch on the fish, but you’re unable to taste it as you sit and ponder about the war a bit more."
    "After you two are done with your meal, you clean up the campsite, just in time for the sun to set."
    $ Time.hours = 22
    stop music fadeout 3
    scene black with dissolve
    "As the darkness of the night begins to take over, you both head down from the temple with caution."
    jump Roushk_bulltribe_back
label Roushk_bulltribe_back:
    scene bulltribe 1n with dissolve
    $ Roushk.bulltribe = 4
    if Quest.campw1 == 4:
        "Just as the two of you reach the stone where Thane would usually be sitting on, a lone bull warrior brandishing a heavy club."
        "Bull warrior" "Hey!"
        e 9 "What?"
        "Bull warrior" "Where did you two come from?"
        e 6 "Err, the temple?"
        "Bull warrior" "I’ve been guarding this spot the whole day, I never seen you two go up."
        e 5 "We went up early, now out of our way."
        "The bull drops his club right in front of your feet."
        "Bull warrior" "Why the hurry Fleabag?"
        "Bull warrior" "I never got the chance to meet the one outsider who made it into the village in so long?"
        e 6 "Well friend, why don’t you let us head back down?"
        "Bull warrior" "What, you think you’re too good to talk to me?"
        "Bull warrior" "You think you can just waltz into the tribe and act like you own the place?"
        "The bull shoves you back."
        "Roushk steps forward between you and the bull."
        ro "Hey, you’re out of line. We’re not here to cause any trouble."
        "Bull warrior" "Who the fuck are you?"
        "The bull smacks Roushk in the face. "
        "Roushk growls angrily, you sense a dangerous aura emanating from Roushk’s body just like the first time you fought him. "
        e 9 "Roushk, no!"
        t "Hey!"
        "Thane’s voice breaks the tension in the air as he appears from the top of the stairs."
        show thane stand at center with dissolve
        t "What’s with all this commotion?"
        "You manage to pull Roushk back by the arm."
        "He grabs his own left hand as though trying to stop himself from attacking."
        e 1 "Thane, my friend is sick now, we got to go and this jackass won’t stop harassing us."
        "Thane stares down the other bull."
        t "Is this true?"
        "Bull warrior" "I- I was just messing around Brother Thane."
        "Bull warrior" "Hahahaha, we’re just having a good laugh. Of course I’m letting them go."
        t "You, me, in the tent right now."
        t "We do not harass a guest when they are in the village."
        t "Not even the Chief would tolerate that. "
        hide thane stand with dissolve
        "Thane drags the other bull by the horn into Chief Axel’s tent."
        e 5 "Come on we gotta get back to the tavern before the curse makes you do something worse."
        "You both run back to the tavern."
        $ Roushk.thane = 1
        $ Roushk.meko = 1
        jump T_outdoor
    elif True:
        "Upon reaching the stone where Thane would usually be sitting on, an imposing figure blocks your way."
        "Tomahawk" "If it isn’t Brother Fleabag."
        "Tomahawk" "What the heck are you doing coming from the bull temple?"
        e 9 "Honestly that name… "
        "Tomahawk" "What the heck were you doing up in the temple grounds?"
        e 5 "What? What’s so weird about me going up to the temple?"
        "Tomahawk" "It’s weird because I’ve been guarding the spot since this morning, but I never saw you go up."
        "Tomahawk" "Makes you wonder why all the secrecy. "
        e 9 "I came last night, what’s it to you?"
        e 9 "You suddenly take an interest in everyone going to the temple?"
        "Tomahawk" "Oh yeah, and who’s your cloaked friend here?"
        ro "…"
        "Tomahawk" "Hey, I’m talking to you. Who the heck are you?"
        ro "…"
        e 1 "My friend is sick now, we got to go."
        "Roushk sniffs the air."
        "Tomahawk" "He smells like a lizard! Take off that cloak!"
        ro "Tsk."
        "Tomahawk forces his way forward and tries to grab at Roushk’s throat."
        "The red lizard quickly slaps the bull’s hand away and launches a punch. "
        "Tomahawk blocks the hit but gives Roushk time to make some space between them."
        "Tomahawk" "What is the meaning of this? "
        ro "Mine lending me a hand?"
        e 13 "I don’t have much of a choice."
        "You draw your blade and ready your fighting stance."


        label Roushk_bulltribe_battle:
            hide screen bag
            hide screen inventory_screen
            hide screen EWinventory_screen
            hide screen EWinventory_view_new
            $ Map.good_battle = True
            $ Battle.holyfcd = 0
            $ wolf_max_hp = 400
            $ wolf_hp = wolf_max_hp
            $ players_turn = False
            $ wolf_max_lust = 100
            $ wolf_lust = 10
            if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
                $ Zalt.cor = min(Zalt.cor +2, 100)
            $ renpy.music.set_pause(True, channel='Chan1')
            $ renpy.music.set_pause(True, channel='Chan2')
            jump Roushk_bulltribe_battle_loop
        label Roushk_bulltribe_battle_loop:

            show screen simple_stats_screen
            show screen battle_menu
            play music "<loop 4.6903>music/forest_fight_small.ogg"
            show bullwip at center
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
                    e 0 "I can't fight anymore.."
                    "The enemy is too strong."
                    "You’re knocked onto the ground."
                    jump Roushk_bulltribe_battle_lose
                if res == "Flirt":
                    $ Random = renpy.random.randint(1, 5)
                    if Random == 1:
                        $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+5)
                        $ wolf_lust = wolf_lust+Zalt.flirt
                        "You stab your sword onto the ground, and rub your sweat from your chest along the rest of your abdomen."
                        "Flexing your abs as you wet them with sweat."
                        "Tomahawk lets out a strong huff."
                        "You can see a noticeable shape growing behind his loincloth."
                    elif Random == 2:
                        $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+5)
                        $ wolf_lust = wolf_lust+Zalt.flirt
                        "You manage to get up close to the large bull and grab him by the groin, groping and squeezing his thick cock before jumping away."
                        "Tomahawk growls and grabs his bulge, massaging it slightly."
                        "Still he shakes his head trying to focus on fighting you."
                    elif Random == 3:
                        $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+5)
                        $ wolf_lust = wolf_lust+Zalt.flirt
                        "You perform a sexy dance. "
                        "Tomahawk lets out a strong huff."
                        "You can see a noticeable shape growing behind his loincloth."
                    elif True:
                        $ Random = renpy.random.randint(1, 3)
                        if Random == 1:
                            "You stab your sword onto the ground, and rub your sweat from your chest along the rest of your abdomen."
                            "Flexing your abs as you wet them with sweat."
                        elif Random == 2:
                            "You manage to get up close to the large bull and grab him by the groin, groping and squeezing his thick cock before jumping away."
                        elif True:
                            "You perform a sexy dance. "
                        "Tomahawk yawns, he is not impressed by your seductive skills."

                    if wolf_lust >= 100:
                        hide screen simple_stats_screen
                        hide screen battle_menu
                        hide screen battle_skill
                        hide screen battle_item

                        stop music
                        jump Roushk_bulltribe_battle_win
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
                    "You can't leave Roushk alone!"
                elif True:
                    pass
                if wolf_hp <= 0:
                    jump Roushk_bulltribe_battle_win
                $ Random = renpy.random.randint(1, 6)
                if Random == 1:
                    $ Random = renpy.random.randint(1, 100)
                    if Random <= Battle.dodge:
                        "Tomahawk slams his heavy weapon onto the ground, missing your feet by a few inches."
                        "But before you can dodge, the earth beneath your feet breaks and flies upwards hitting you in the snout."
                    elif True:
                        $ wolf_damage = renpy.random.randint(30, 50)
                        $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                        "Tomahawk slams his heavy weapon onto the ground, missing your feet by a few inches."
                        "But before you can dodge, the earth beneath your feet breaks and flies upwards hitting you in the snout."
                elif Random == 2:
                    "Tomahawk stops and performs a few poses."
                    "You are stunned and slightly aroused."
                    $ wolf_damage = renpy.random.randint(3, 15)
                    $ Zalt.lust += wolf_damage
                elif Random == 3:
                    "Tomahawk grabs and bear hugs you tightly with one hand."
                    "Using his other hand, he forces your snout between his pecs, forcing you to smell his pungent musk."
                    "You manage to kick the bull away with both legs but his smell is stuck in your nose, making you feel hotter and harder in the groin."
                    $ wolf_damage = renpy.random.randint(3, 25)
                    $ Zalt.lust += wolf_damage
                elif Random == 4:
                    "The bull traps you in a headlock, he flexes his other arm in front of you trying to impress you with his muscles."
                    "You kick him in the groin causing him to roar and to let go of you."
                    $ wolf_damage = renpy.random.randint(3, 20)
                    $ Zalt.lust += wolf_damage
                elif Random == 5:
                    $ Random = renpy.random.randint(1, 100)
                    if Random <= Battle.dodge:
                        "Tomahawk trys to grab you by the neck."
                        "But you dodged their attack!"
                    elif True:
                        $ wolf_damage = renpy.random.randint(30, 50)
                        $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                        "Tomahawk grabs you by the neck and lands a direct punch to the gut."
                        "You cough in pain as the bull sends you flying backwards."
                elif True:
                    $ Random = renpy.random.randint(1, 100)
                    if Random <= Battle.dodge:
                        "Tomahawk grabs a nearby rock and hurls it at you."
                        "But you dodged their attack!"
                    elif True:
                        $ wolf_damage = renpy.random.randint(15, 25)
                        $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                        "Tomahawk grabs a nearby rock and hurls it at you, it hits you square in the chest."
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "Roshk blocks the attack with his wrists and pushes the enemy back."
                    "The lizard slams into the bull’s stomach with his shoulders sending him back a few steps."
                    $ red_damage = renpy.random.randint(20, 40)
                    $ wolf_hp -= red_damage
                elif Random == 2:
                    "Roshk unleashes a barrage of punches, his fists are a blur, hitting the same spot rapidly."
                    "He finishes off his attack with one powerful punch."
                    $ red_damage = renpy.random.randint(15, 30)
                    $ wolf_hp -= red_damage
                elif True:
                    "Roshk signals for your sword. You pass him your sword."
                    "He dodges Tomahawk’s punch and slams the hilt of the sword on the bull’s foot."
                    "Tomahawk roars in pain, but Roushk follows up with an uppercut to the chin."
                    $ red_damage = renpy.random.randint(20, 40)
                    $ wolf_hp -= red_damage
                if Battle.holyfcd !=0:
                    $ Battle.holyfcd = Battle.holyfcd-1
            if wolf_hp <= 0:
                if Zalt.hp <= 0:
                    jump Roushk_bulltribe_battle_win
                elif True:

                    jump Roushk_bulltribe_battle_win

            elif Zalt.hp <= 0:
                jump Roushk_bulltribe_battle_lose
            elif Zalt.lust >= Zalt.maxlust:
                "You're too horny to fight anymore."
                "You fall to the ground."
                jump Roushk_bulltribe_battle_lose
            elif True:
                jump Roushk_bulltribe_battle_loop
        label Roushk_bulltribe_battle_win:
            $ renpy.music.set_pause(True, channel='Chan1')
            $ renpy.music.set_pause(True, channel='Chan2')
            play music "music/forest_fight_small_end.ogg" noloop
            pause 1
            hide bullwip with slow_dissolve

            hide screen simple_stats_screen
            hide screen battle_menu
            hide screen battle_skill
            hide screen battle_item

            "You land a powerful punch onto Tomahawk’s stomach. He falls to his knees."
            "{b}{color=#19c22a} <[name] gained one Level-up-point.>{/color}"
            $ Zalt.points = Zalt.points +1
            "Tomahawk" "Stop, I give!"
            e 1 "Learn to pick your fights."
            e 1 "Come on, let’s go Roushk."
            ro "Aaargh!" with vpunch
            e 5 "Roushk?"
            "The bracelet on his wrist glows brightly."
            show roushk stand1 at center with dissolve
            hide roushk stand1 with dissolve
            "Roushk snarls like a wild animal and rushes towards Tomahawk. "
            e 9 "No!"
            "Before you can stop him,he punches Tomahawk right in the jaw and slams his face into the ground." with vpunch
            "You’re forced to tackle Roushk down."
            jump Roushk_bulltribe_end
        label Roushk_bulltribe_battle_lose:
            $ Zalt.lust = 0
            $ Zalt.hp = 1
            hide screen simple_stats_screen
            hide screen battle_menu
            hide screen battle_skill
            hide screen battle_item
            stop music

            hide bullwip with dissolve
            "You fall to your knees, unable to fight."
            "Tomahawk stands above you with his club above, ready to strike you down."
            ro "No!" with vpunch
            show roushk stand1 at center with dissolve
            hide roushk stand1 with dissolve
            "The lizard leaps in between the two of you just in time to intercept the attack."
            "He struggles to push Tomahawk back when his bracelet begins to glow."
            "Roushk snarls and is suddenly able to push the large bull’s club away. "
            "He follows up his counter with a powerful punch sending the bull rolling across the grounds." with vpunch
            "Tomahawk's body stops right in front of Thane’s rock and remains motionless."
            show roushk stand1 at center with dissolve
            "Roushk screams in agony into the air and grabs his head as though he is in extreme pain."
            hide roushk stand1 with dissolve
            "You rush over and grab him by the arms."

            jump Roushk_bulltribe_end

label Roushk_bulltribe_end:
    e 12 "Roushk, Roushk! Snap out of it."
    "You punch Roushk in the face, and he somehow regains control of himself."
    show roushk stand at center with dissolve
    ro "Wha-what just happened?"
    e 9 "The bracelet activated itself. I think it took control of you for a minute."
    ro "Oh no, is he?"
    "You turn towards Tomahawk and rush over to check on him."
    hide roushk stand with dissolve
    e 1 "He’s still breathing, just knocked out."
    ro "I can’t believe I did this. "
    e 13 "It wasn’t you, it was the curse."
    "Thane then emerges from Axel’s tent and runs over to you three."
    show roushk stand at left with dissolve
    show thane stand at right with dissolve
    t "What the heck is going on? I heard a loud commotion nearby."
    e 13 "Roushk got possessed and knocked out Tomahawk."
    "Surprised Thane looks at the red lizard then back to you."
    hide roushk stand
    hide thane stand
    show thane stand at center with dissolve
    t "You two better head out of the village now before father returns."
    t "I’ll deal with Tomahawk when he wakes up."
    e 13 "Thank you Thane, I’ll come back once this is all settled. "
    "Tomahawk" "Mmm… meat..."
    t "He’s ok, go on before he comes to."
    "Wait, please use this to help him recover."
    hide thane stand at center with dissolve
    "Roushk pulls out a vial with red liquid in it. You recognize it as one of Chet’s HP potions."
    ro "It isn’t much but I hope it helps."
    show roushk stand at left with dissolve
    show thane stand at right with dissolve
    t "Thank you, I wish you the best on your return. "
    "Roushk nods and covers himself in his cloak and follows you out of the village."
    hide roushk stand
    hide thane stand
    scene black with dissolve
    "..."
    scene outdoor 1n with slow_dissolve
    show roushk stand at center with dissolve
    e 1 "Roushk get some rest, I’ll check with Meko, and come get you."
    ro "Sure..."
    hide roushk stand with dissolve
    "He walks away slowly, hanging his head low."
    "You wonder if he still blames himself for what happened to Tomahawk."

    $ Time.hours = Time.hours +2
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    $ Roushk.thane = 1
    $ Roushk.meko = 1
    jump T_outdoor
label Roushk_meko:
    $ Roushk.meko = 4
    scene basement 1 with dissolve
    show meko stand70 at left with dissolve
    show roushk stand at right with dissolve
    play sound "music/foot1.ogg"
    m "Now, show me the artifact."
    "Roushk shows his bracelet. "
    "He gulps."
    ro "Is this going to hurt?"
    m "Usually no, now don’t stare directly into the light."
    hide meko stand70 with dissolve
    hide roushk stand with dissolve
    if Time.hours >=22 or Time.hours <4:
        $ Time.hours= Time.hours+1
    elif True:
        $ Time.hours = 23
    if Time.hours >=24:
        $ Time.days = Time.days+1
        $ Time.hours = Time.hours-24
    "Meko begins chanting a spell."
    "A very long spell... it's so long it's already night, and he's not done chanting."
    "Meko floats into the air and a blast of blue light fires on Roushk’s bracelet."
    "The brightness of the beam forces you to look away."
    "Suddenly, a loud crack is heard followed by the sound of an ear shattering scream."
    m "Ahhhhhhhh!" with vpunch
    e 5 "Meko!"
    with flashbulb
    "A bright flash of light radiates from Meko’s body forcing you to look away. "
    "The space around you is turning like a weird distorted reflection in a mirror."
    "The walls and doors twist and turn. "
    scene basement 2 with vslow_dissolve
    "It doesn’t feel like you’re in the basement anymore!"
    show meko stand2 at center with dissolve
    "Meko’s horn takes on a strange purple hew, the same way he was possessed last time."
    "Meko?" "You fools, you’ve given me a more powerful vessel than I could’ve ever dreamed of!"
    ro "The curse is alive? Who the hell are you?"
    "Boss" "Oh, I’m more than just a curse, and you can call me The Boss, because that’s what I’m going to be, the boss of everything in this kingdom!"
    "Boss" "I’ve been trapped in that damn bracelet for thousands of years, and with this new form I’m going to enjoy taking over this kingdom starting with you two!"
    "Meko" "Gaah! You need to hit me. Just hit me… gahh… until this bastard... lets go of … of me."
    "Meko" "Don’t hold back!"
    ro "Don’t lose focus, we need to defeat that evil spirit or Meko is as good as dead, again."
    "Boss" "Shut up lizard breath, I don’t need a broken toy anymore."
    "The corrupted horn casts a spell that levitates Roushk up above into the air."
    ro "Wait, no! [name]!"
    e 9 "Roushk!"
    "The red lizard’s body flies across the air and slams against a distorted floor."
    "He falls on his face and doesn’t get up."
    e 12 "You’ll pay for that!"
    "{b}{color=#19c22a} <[name]'s stats temporarily improve!>{/color}"
    "You point your sword at the horn and charge in for an attack."
    label Roushk_meko_battle:
        hide screen bag
        hide screen inventory_screen
        hide screen EWinventory_screen
        hide screen EWinventory_view_new
        $ Map.good_battle = True
        $ Battle.holyfcd = 0
        $ wolf_max_hp = 400
        $ wolf_hp = wolf_max_hp
        $ players_turn = False
        $ wolf_max_lust = 666
        $ wolf_lust = 0
        if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
            $ Zalt.cor = min(Zalt.cor +2, 100)
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
        jump Roushk_meko_battle_loop
    label Roushk_meko_battle_loop:

        show screen simple_stats_screen
        show screen battle_menu
        play music "<loop 12.4405>music/forest_fight_strong2.ogg"
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
                $ red_damage = renpy.random.randint(Zalt.ATK+10, Zalt.ATK+20)
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
                e 0 "I can't fight anymore.."
                "The enemy is too strong."
                "You’re knocked onto the ground."
                jump Roushk_meko_battle_lose
            if res == "Flirt":
                "Now is not the time to do that!"

            if res == "Bind up":
                $ Zalt.heal = renpy.random.randint((Zalt.int*2)+30, (Zalt.int*2)+50)
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
                "You can't leave Roushk alone!"
            elif True:
                pass
            if wolf_hp <= 0:
                jump Roushk_meko_battle_win
            $ Random = renpy.random.randint(1, 3)
            if Random == 1:
                $ Random = renpy.random.randint(1, 100)
                if Random <= Battle.dodge:
                    "The horn spins and forms a blue ring around itself."
                    "But you dodged his attack!"
                elif True:
                    $ wolf_damage = renpy.random.randint(10, 25)
                    $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                    "The horn spins and forms a blue ring around itself."
                    "With lightning speed it blinks from place to place, you can’t follow it."
                    "Suddenly, it cuts through your abdomen like a razorblade. "
            elif Random == 2:
                $ Random = renpy.random.randint(1, 100)
                if Random <= Battle.dodge:
                    "The Boss unleashes a volley of fireballs."
                    "But you dodged his attack!"
                elif True:
                    $ wolf_damage = renpy.random.randint(10, 20)
                    $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                    "The Boss unleashes a volley of fireballs."
                    "You manage to dodge a few, but the fireballs are coming too fast."
                    "One lands right in front of your feet and explodes, sending you flying backwards."
            elif True:
                $ Random = renpy.random.randint(1, 100)
                if Random <= Battle.dodge:
                    "The boss summons two golem avatars; they both unleash Holy Fist onto you."
                    "But you dodged his attack!"
                elif True:
                    $ wolf_damage = renpy.random.randint(10, 25)
                    $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                    "The boss summons two golem avatars; they both unleash Holy Fist onto you."
            if Battle.holyfcd !=0:
                $ Battle.holyfcd = Battle.holyfcd-1
        if wolf_hp <= 0:
            if Zalt.hp <= 0:
                jump Roushk_meko_battle_win
            elif True:

                jump Roushk_meko_battle_win

        elif Zalt.hp <= 0:
            jump Roushk_meko_battle_lose
        elif Zalt.lust >= Zalt.maxlust:
            "You're too horny to fight anymore."
            "You fall to the ground."
            jump Roushk_meko_battle_lose
        elif True:
            jump Roushk_meko_battle_loop
    label Roushk_meko_battle_win:
        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item
        play music "music/forest_fight_boss_end.ogg" noloop fadein 1.4
        "You leap into the air with your sword drawn and plunge the cold blade where Meko’s horn sits."
        "Boss" "Nooooo!"
        hide meko stand2 with dissolve
        "Your sword pierces his horn, and a deep crack forms on his body. "
        m "Get out of me!"
        "A terrifying shadow spire bursts through the crack and flies upwards, smashing through the distorted ceiling."
        "Then silence falls upon you."
        "You grab Meko’s horn. The crack you made is no longer on his body."
        e 5 "Meko! Meko! Tell me you’re alive. Meko!"
        "You hold Meko close to your chest."
        m "Mmm...eh…"
        e 5 "Roushk!"
        "You run over to his unconscious body and shake him hard."
        ro "Mmm… [name]?"
        "Roushk’s eyes flutters open."
        show roushk stand at center with dissolve
        ro "What happened? Did you beat the evil spirit?"
        e 13 " I did, but more importantly, you guys are safe."
        "Roushk nods. "
        "Crack."
        hide roushk stand at right with dissolve
        "Up above, a massive crack appears where the ceiling would be and a large chunk falls down towards you."
        ro "Look out!"
        "Roushk pushes you down forcing you to duck while he uses his cloak to shield you. "
        "You both brace for the incoming impact, but it never comes."
        scene basement 1 with vslow_dissolve
        ro "What? "
        show roushk stand at center with dissolve
        "Roushk stands back up and you find yourself back in the tavern wine cellar."
        e 13 "We’re back. Oh, thank goodness."
        "Giving into the tiredness, you sit on the floor still clutching Meko’s horn."
        show meko stand70 at left with dissolve
        show roushk stand at right with dissolve
        m "Mmm… is it over yet?"
        e 13 "Yeah, we’re back buddy. It’s over."
        hide meko stand70
        hide roushk stand at right with dissolve
        "Meko floats away from your hands back onto the barrel he usually sits."
        m "… Ugh, I feel so drained."
        ro "That was no easy fight, but is it truly over?"
        m "Yes, I don’t sense the curse anywhere. As for the artifact-"
        "You spot the bracelet on the floor and pick it up."
        m "It’s now just an ordinary bracelet."
        show meko stand70 at left with dissolve
        show roushk stand at right with dissolve
        ro "But how will I return now?"
        m "Well, you would be happy to know that I managed to copy the spell and learn how it works during the entire battle."
        m "I can recreate the portal back to your home Roushk."
        "The red lizard puts on the biggest smile and hugs you tightly."
        ro "We did it! We did it!"
        e 3 "Wooohoo!"
        m "Heh, but you’ll need to give me a whole day to rest."
        m "Most of my magic has been drained by that bloody spirit."
        ro "Of course, thank you so much Meko. I owe you a debt of gratitude."
        e 1 "We should tell the rest. Can’t have you go home without a proper goodbye."
        hide meko stand70
        hide roushk stand at right with dissolve
        "Roushk nods."
        scene black with slow_dissolve
        "..."
        play Chan1[ "<silence 0.5>", "music/tavern.ogg" ]fadein 3
        $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
        scene tavern 1 with vslow_dissolve
        "The news of Roushk’s freedom fills you with immeasurable joy, you just have to wake up everyone and tell them to meet at the drinking hall."
        show snow happy1 at left with dissolve
        show roushk stand at right with dissolve
        s "What exactly is so important it can’t wait till morning?"
        e 1 "We did it! We found someone to uncurse the artifact, Roushk can go home tomorrow."
        "The rest gasp."
        hide snow happy1 at left with dissolve
        c "What did I say about waking me up when I’m sleeping?!" with vpunch
        "Chet continues to look at you with a disgruntled glare."
        e 9 "Chet, we found a way home for Roushk!"
        "Chet’s continues to look at you with a disgruntled glare."
        c "Cool. Now, keep it down or I’ll have both your asses on my feet."
        "He mutters under his breath and goes back into the spandrel."
        ro "I couldn’t have done it without [name]’s help, and all of your support."
        show witer stand at left with dissolve
        w "This is such great news, we have to organize a party!"
        hide witer stand
        show hakan stand at left with dissolve
        h "I’ll drink the booze."
        w "I think you mean you’ll bring the booze."
        h "I know what I said."
        hide hakan stand
        show snow happy1 at left with dissolve
        s "Now’s a good time to prepare my special grilled fish."
        show snow stand at left with dissolve
        s "Witer make sure to bring out the good beer."
        hide snow stand
        show witer stand at left with dissolve
        w "This is so exciting, do I have time to make decorations?"
        h "When Chet wakes up, lets get him to set up some games."
        w "And you can set up the tables with him."
        h "Only if you blow me."
        w "Hah, they better be the best damn table arrangement I ever see if you want that."
        hide witer stand
        show hakan stand at left with dissolve
        hide hakan stand
        hide roushk stand at right with dissolve
        "The whole group is excited to throw a party."
        "They decide to have it the next day."
        "For now, you can rest."
        $ renpy.music.set_volume(0, 2, channel = "Chan1")
        scene black with dissolve
        "..."
        "......"
        $ Zalt.hp = Zalt.maxhp
        $ Zalt.mp = Zalt.maxmp
        if Time.hours >=21:
            $ Time.days = Time.days+1
            $ Time.hours = 6
            $ Time.mins = 30
        elif True:
            $ Time.hours = 6
            $ Time.mins = 30
        $ Roushk.endday = Time.days
        $ Roushk.party = 1
        scene room 1 with dissolve
        e 1 "Today’s Roushk’s celebration party."
        e 1 "I should find out when it’s on."
        jump Room1
    label Roushk_meko_battle_lose:
        $ Zalt.lust = 0
        $ Zalt.hp = 1
        hide screen simple_stats_screen
        hide screen battle_menu
        hide screen battle_skill
        hide screen battle_item
        stop music

        hide meko stand2 with dissolve
        "Your sword is knocked out of your hand."
        "In a last ditch effort to save Meko you rush forwards to tackle the horn down."
        "Boss" "Freeze."
        "Every fibre of muscle in your body refuses to budge."
        "You’re both stuck in place like stone."
        e 5 "I can’t move!"
        "An invisible force lifts you and you are brought close to the horn. "
        "A haunting pair of purple eyes the size of two large shields forms in mid air staring back at both of you."
        "Boss" "Enough games, it was fun playing with you two for a bit, but now I have work for you, my puppet."
        "His massive eyes glow bright."
        "Unable to look away, your eyes turn a dark shade of black as the light consumes you. "
        "The very fabric of your mind is ripped apart, your thoughts become a jumbled mess."
        scene purple with slow_dissolve
        "Your feelings fade away into nothingness, and your memories of home shatter away."
        "The Boss laughs maniacally."
        "Boss" "Now get out there and bring me more minions to build my army."
        "Boss" "But first, kill the red lizard!"
        "{b}{color=#c22719}<GAME OVER>{/color}"
        menu:
            "KillKillKillKillKill" if True:
                pass
        scene black with slow_dissolve
        "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Ah, another unwanted intruder.{/color}{/b}"
        "{color=#7d0004}???{/color}" "{b}{color=#7d0004}I don’t like it when someone messes with my game.{/color}{/b}"
        "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Time to reset the board.{/color}{/b}"
        return
label Roushk_meko_battle_end:
    scene black with slow_dissolve
    "..."
    play Chan1[ "<silence 0.5>", "music/tavern_party.ogg" ]fadein 3
    $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
    scene tavern 1 with vslow_dissolve
    "Come evening, you join the rest at the drinking hall."
    "There must be two table’s worth of food and beer. "
    "Witer spots you and walks over to pass you a mug of beer."
    show snow happy1 at center with dissolve
    s "Finally, the second guest of honour is here."
    show snow laugh at center with dissolve
    s "Now, before we start tonight’s celebration, we should offer our short guest the opportunity to say a few words before he leaves."
    hide snow laugh with dissolve
    "Roushk is caught off guard, he tries to turn down the offer to speak, but everyone including yourself chants to him to give a speech."
    show roushk stand at center with dissolve
    ro "Ok, ok. I guess I don’t have much of a choice. What to say?"
    ro " I wanted to thank you all."
    ro "My mind was lost, I wasn't myself and yet there were people who decided to help me, despite not knowing me at all."
    ro "If it wasn't for you, I wouldn't be standing here and there would be no chance for me to return home. "
    ro "My tribe needs me, the same as I need them."
    ro "The same thing can be said about all of you here."
    ro "No matter how different you are, no matter where you came from, you created your own tribe. "
    ro "You can count on each other, in good times and in the bad times."
    ro "Thanks to you all, I'll be able to see my people once more."
    ro "If there are other ways out of the fog I am sure you all will find it."
    ro "For now... even if it's hard you couldn't have ended up with better company."
    ro "Stick together, that's what gives you strength."
    ro "Now before I leave tomorrow, I want to give something back as a sign of gratitude."
    ro "For Snow, here is a bag of gold coins."
    "Snow walks up to Roushk and receives the gift. He shaked the bag as though to The crowd erupts into an applause."
    "Roushk bows and makes way for Snow."
    hide roushk stand
    show snow stand at center with dissolve
    s "An endearing speech, does our young adventurer have anything else to add?"
    e 3 "Let’s drink!"
    hide snow stand at center with dissolve
    "Everyone raises their mugs and cheers."
    "The rest then break off into pairs."
    "Hakan joins Chet in his game of cards while Snow and Witer are engaged in conversation."
    "Roushk elbows your stomach softly."
    e 5 "Hmm?"
    ro "Look, over by the bowl of jerky."
    "Looking closely you see Meko’s horn next to the bowl."
    "You walk over to the table, your hand reaches out about to pick him up until you hear his voice."
    m "It’s ok, they can’t see or hear me."
    m "Go enjoy the party, I promise I won’t cause any problems."
    "You pull your hand back while rolling your eyes."
    "Seeing how Meko won’t cause any harm you decide to leave him be."
    s "Hey [name], quit staring at the food and come here for a second."
    "You walk over to Roushk who’s talking to Snow and Witer."
    show witer stand at left
    show roushk stand at right with dissolve
    w "So, you two still haven’t told any of us how you really got that artifact uncursed."
    e 9 "Well, it’s a long story. "
    "Nervous, you rub the back of your neck."
    "They can’t know about Meko, but what can you tell them without deceiving them?"
    "Roushk steps forward and with a charming smile, and starts talking."
    ro "It was a difficult battle, the curse was unleashed when the artifact was activated but it took over a nearby object instead."
    ro "Then it took on the form of this massive avatar."
    ro "It was a heated battle, [name] and I were getting pounded left and right."
    ro "Witer, you couldn’t have imagined it, bodies slamming hard against one another."
    ro "At one point the avatar was just pounding our ass with his fists. "
    ro "You ever experienced that Witer?"
    w "…Why are you saying that to me? "
    hide witer stand at left with dissolve
    "Witer frantically shakes his head while blushing."
    "He turns away and runs off with his drink to the food table."
    ro "What did I do? I’m just saying the fight was pretty hard."
    "Snow laughs out loud, and pats Roushk in the back. "
    s "I’ll go calm our waiter down, enjoy the party you two."
    "Once Snow is out of ear shot, you turn to Roushk."
    show roushk stand at center with dissolve
    e 1 "Thanks for covering for me."
    ro "It’s the least I can do, wouldn’t want to put a rift in your friendship, plus technically I didn’t lie."
    e 6 "Yeah, you just left out the important parts, and diverted the conversation. Clever."
    ro "It’s part of the job as a tribe leader."
    "Looking over at Hakan, you see the red dragon smacking himself on the forehead and pointing with a huff at a smiling Chet."
    ro "Let’s see what they’re up to."
    hide roushk stand at center with dissolve
    "The two of you walk over to the pair."
    c "You can beat the cards up all you want, you still lost 10 gold coins."
    show hakan stand at left
    show roushk stand at right with dissolve
    h "Gah! How am I losing all the time?"
    e 1 "What’s going on here boys?"
    c "Just a game of cards. You guys want in?"
    "Hakan shakes his head. "
    h "You gotta watch out for him, he’s a trickster. He beat me out of 50 gold coins already."
    e 1 "Damn, alright I like a challenge."
    ro "Well, I did keep some coins as a souvenir for myself, but sure, lets play."
    h "Well I need a drink. I’m getting some beer."
    hide hakan stand with dissolve
    "As Hakan leaves to refill his mug, you and Roushk take a seat at the table."
    e 1 "What are we playing?"
    c "A simple game of Lie."
    c "The goal is to empty out your hands. You can put one or more cards, but you have to declare what cards you placed down in their order."
    c "If someone thinks you’re lying they’ll call Lie. If they’re right, you get the whole stack, but if they’re wrong, they get the whole stack."
    c "Each round’s 30 coins to play."
    e 1 "I’m in."
    ro "I’ll try my best. To the best strategist then."
    hide roushk stand with dissolve
    "Every time a round ends, Chet’s sly smile fades slowly away."
    "You’re now in the final round. Chet’s hands are trembling."
    "He has only one card in his hand while Roushk has none."
    c "It’s a…"
    c "It’s a lie!"
    ro "Nope, it was true."
    "Chet slumps back against the chair, with an empty stare."
    c "Ha... ha… I lost again."
    show hakan stand at left
    show roushk stand at right with dissolve
    ro "Here Hakan, you can have my winnings, I just want a few coins to take back."
    h "You’re alright Roushk, I especially liked how you gave Chet a thrashing."
    c "My… my … money."
    e 6 "There, there."
    "You pat Chet on the head."
    "The party continues until the late hours of the night."
    "While everyone is busy drinking and having a merry time, you notice Roushk slipping out of the tavern."
    "You decide to leave the party and see if Roushk needs anything."
    $ Roushk.party = 4
    $ Roushk.end = 1
    jump Roushk_meko_battle_end1
label Roushk_meko_battle_end1:
    stop music
    play sound "music/door.mp3"
    "..."
    $ renpy.music.set_volume(0, 4, channel = "Chan1")
    play sound "music/foot1.ogg"
    scene outdoor 1n with slow_dissolve
    "..."
    scene barn 1 with slow_dissolve
    "The oil lamps hanging by the raptors cast a warm glow in the barn."
    "From across the barn door you see Roushk’s feet from the utility room."
    e "Tired?"
    "Roushk sits up to get a better look at you."
    ro "Not really, just wanted to get some fresh air."
    "Roushk pats the space next to him inviting you to sit down. "
    show roushk stand at center with dissolve
    e 1 "I noticed you didn’t really touch your beer."
    ro "I just want to keep a clear head before tomorrow comes."
    ro "There’s a lot that needs to be done when I get back."
    e 1 "Makes sense."
    e 13 "You know, I have a lot of mixed feelings knowing you’re going home so soon."
    ro "What kind of feelings?"
    e 1 "Well, I feel…"
    menu:
        "I feel happy" if True:
            e 13 "I’m happy you’re able to go back, that’s what I’ve been searching for so long to do."
            e 13 "Find a way out of this fog, and get rid of it so no one has to be trapped here anymore."
            ro "I think you can do it, no I know you can do it."
            ro "Your kind and courageous spirit is the reason I get to go back, and if you don’t lose it, you’ll find your way home."
            e 1 "Thanks Roushk."
            ro "Now, there’s something I want to give to you."
        "I feel sad" if True:

            e 13 "I’m sad that we can’t all leave together."
            e 1 "And well, it’s sad to say goodbye to a friend."
            ro "You will leave one day, I’m just a passerby."
            ro "One who’s glad a brave adventurer was waiting here, and with a kind enough heart to help me. "
            ro "But you’re right, it is sad to say goodbye so soon."
            ro "That’s why there’s something I want to give you."
        " I feel unsure" if True:
            e 13 " I’m not sure. Happy, sad, scared, maybe all of it at once?"
            e 1 "You get to go home, but I don’t know if we can too."
            e 13 "What if we’re stuck here forever?"
            ro "That’s not set in stone, and I don’t believe it."
            ro "Someway somehow you’ll get out, you just need to keep trying."
            e 1 "Will I be strong enough to do this though?"
            ro "You are, and to make sure you remember that there’s something I want to give you."
    e 1 "What ?"
    ro "My blessings."
    ro "You mentioned your tribe does a blessing ritual as a sign that you’ve become a warrior."
    ro "I want to give you my blessing."
    e 5 "Wait, really?"
    ro "Yes, I’m not sure what it’s worth, but I want you to always remember that you’re a capable person, and not to lose confidence in yourself."
    ro "In my eyes you’ve proven yourself to be a worthy warrior."
    hide roushk stand at center with dissolve
    "Roushk stands up, and undoes his broach. His cape falls. You watch with your mouth open."
    "It takes you a few seconds for your brain to connect the dots as to what he’s offering."
    "He looks larger than before as he towers above you."
    "The peaks of his arms bulge out without him even flexing."
    "You are drawn to the supple curves of his shelf like chest. "
    "With your right hand you reach out to touch his cobblestone abs."
    "Roushk meets you halfway, grabbing hold of your hand he pulls you closer until you feel his smooth scales that cover his stomach."
    "He guides your hand along his abs, groaning against your touch."
    e 13 "...Are you sure you want to do this? "
    ro "If you are worried about my relationship with Othra, don’t misunderstand."
    ro "This changes nothing about how I feel about her, I am merely fulfilling a ritual."
    ro "Othra knows that these traditions can involve some unorthodox methods."
    ro "As priestess of the tribe I’ve seen her go through some harder rituals."
    ro "I am sure she will be fine when I tell her what happened here."
    e 1 "..."
    ro "Why? Do you have feelings for me?"
    e 9 "Ah, no. I’m just nervous. "
    "He gets down on his knees and looks at you with a serious expression."
    ro "Do you want to do this ritual with me?"
    ro "I’m not forcing you if you don’t want to."
    menu:
        "Yes" if True:
            if Roushk.ke == 1:
                jump Roushk_sex_top
            elif Roushk.ke == 2:
                jump Roushk_sex_bottom
        "No" if True:
            e 13 "I think maybe not."
            e 1 "I appreciate the gesture, but I have to work hard to earn it."
            e 1 "When I find that grand treasure I’ll earn the right to have the ritual back in my village."
            ro "I can respect that."
            e 1 "Still, thank you. It means a lot that you care."
            ro "Well I still want to give you something to remind you to keep being strong."
            ro "Here, take this."
            "Roushk hands over the bracelet he wore."
            e 1 "The cursed bracelet?"
            ro "Formerly cursed, it’s just a regular bracelet now."
            e 1 "It’s an honour to accept this from you. "
            ro "Roushk smiles warmly and pats you on the head."
            "A pleasant warmth spreads across your head to your cheeks."
            "It’s been so long since someone patted you on the head. "
            ro "Anyways, I think I’ll turn in early. "
            e 1 "Alright, good night Roushk."
            "You push yourself back up and leave the barn."
            scene black with slow_dissolve
            play sound "music/foot1.ogg"
            "..."
            play sound "music/door.mp3"
            scene tavern 1 with slow_dissolve
            "When you return to the tavern the party has already died out. "
            show meko stand at center with dissolve
            "Before you can head up to your bedroom, Meko’s horn floats over to your line of sight. "
            m "[name], meet me in the barn tomorrow morning at 6 a.m. I’ll open up the portal for Roushk to go home."
            e 1 "(He can’t even say goodbye to the rest.)"
            m "It’s the best time and place so no one notices me."
            e 1 "Ok."
            play sound "music/door.mp3"
            scene room 1 with slow_dissolve
            "..."
            hide meko stand with dissolve
            jump Roushk_goodbye



label Roushk_sex_top:
    $ Zalt.lust = 0
    $ sex = True
    $ persistent.CG_roushk_top = True
    $ Zalt.sex = Zalt.sex +1
    e 13 "I do."
    "Roushk smiles at you and caresses your face."
    ro "Then let’s find somewhere more comfortable."
    "The lizard stands up and grabs a bundle of hay."
    "You follow him from behind, watching his plump butt sway with the swing of his tail."
    "The sheer volume and voluptuousness of his shiny red ass sends shivers down your spine."
    "He leads you to the side where two large mounds of hay sits."
    "Roushk quickly gets on all fours and spreads the hay he carried all around the floor."
    "With his tail raised, you can see his butt swaying to and fro. "
    "A wave of heat washes over your chest, and spreads down to your loins."
    "There’s no other way to say it, you want him badly."
    "You drop your sword. It falls with a loud clunk."
    "Roushk turns to you and smiles."
    ro "Eager are we? Then come over, there’s enough space for two."
    "Roushk pulls off his loincloth leaving him completely nude."
    "He lies back against the bed of hay, his wide hands supporting his head."
    "Your breathing shallows and a noticeable bulge forms between your legs."
    "Without hesitation you pull off your loincloth, freeing your semi hard dick."
    "A small drop of pre already forms at your tip."
    "Roushk licks his lips, and flexes his massive pecs to invite you to come closer."
    show etop 0 with slow_dissolve:
        xpos 0.05 ypos 0
        zoom 1
    "You get on your knees and marvel at the sight before you."
    "Roushk spreads his legs wide giving you a front row seat of his hole."
    "It’s like looking at the most seductive and tantalizing piece of meat you’ve ever seen, and your hunger is voracious tonight."
    show etop 1 with slow_dissolve:
        xpos 0.05 ypos 0
        zoom 1
    "Panting, you reach out, and grasps Roushk’s meaty pecs."
    "The powerful muscles beneath his scales tenses and relaxes between your fingertips."
    "Roushk huffs and purrs. His chest rises with each breath."
    ro "You know how to treat a man’s muscles."
    e 0 "I’ve been practising."
    "Roushk flexes his pecs, you watch as the fibers taunt and his entire chest hardens."
    "Your arms tremble, and your cock twitches, growing harder to its full mass. "
    "Digging your fingers deeper into Roushk's pecs it feels like you're kneading steel. "
    "You bend down closer with your butt lifted high up."
    "The fur on your neck brushes against the top of his abs while you slide your snout along the crevasse of Roushk’s pecs."
    "A deep rumble emanates from his chest."
    ro "Your fur tickles."
    "You smile and slide your face upwards to meet his."
    "All the while your hands remain glued to his chest, fondling his lower pecs."
    "He flexes his chest again squeezing your face between his muscular chest."
    e 0 "This feels so good. Don't stop."
    "Roushk is more than happy to oblige."
    "He squeezes and bounces his chest against your cheeks."
    "Droplets of sweat that form on his naked body bathes the fur on your snout."
    show etop 0 with slow_dissolve:
        xpos 0.05 ypos 0
        zoom 1
    "You then pull yourself off of Roushk. "
    "With your hands you rub his inner thighs sensually."
    ro "Mmm..."
    "The thick scent of musk overpowers the woody scent of hay around you both."
    "There’s still the faint sound of cheers coming from the tavern in the distance, but it’s drowned out by your heavy moans."
    "Nose flaring, you look down across his hard abs and notice the slit between his legs."
    e 0 "What do we have here."
    show etop 2 with slow_dissolve:
        xpos 0.05 ypos 0
        zoom 1
    "You run your hand down his abs until you touch the warm vent."
    "Roushk groans as you press a finger into his slit."
    "The inside feels warm to the touch, and slick with pre."
    ro "I’m sensitive there."
    e 0 "Do you want me to stop?"
    ro "No, you can keep going."
    "You smile and slide your middle finger into his slit."
    ro "Ahhh, so… big."
    "Roushk squirms as you slide your finger deeper inside him."
    "You lick your lips hungrily as you pull your finger out and plunge it back inside him."
    "Roushk practically howls in ecstasy."
    "Pressing deeper, you feel your finger brushing against the tip of Roushk’s dick."
    e 0 "Is that?"
    ro "Y...yes."
    ro "Please… [name], just fuck me."
    menu:
        "Fuck Roushk in the ass" if True:
            e 0 "Not yet, I want to see what you’re packing in there."
            "With your middle finger you brush against Roushk’s dickhead."
            "Like coaxing a smaller animal, you stroke Roushk’s member while slowly pulling your finger away."
            "The walls of his slit expand as Roushk’s hard cock pushes through and slaps against his hard abs."
            show etop a1 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "An immense wave of musk emanates from his freed cock."
            "You clasp your hand around his dick, your fingers just barely covering his entire girth."
            "Roushk groans again."
            "His chest rises following your hand’s motion up along his cock."
            "A thick coat of pre spews out of his dickhead, wetting the palm of your hand."
            "You look on with wide eyes, and rub the hot pre along his cock."
            show etop a2 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "There’s only one thing on your mind, to ram your cock in him, and make him beg for more."
            "You rub your raging hard on and slap it against Roushk’s left thigh."
            e 0 "You ready?"
            ro "Show me your strength, warrior."
            "Your heart beats fast with your throbbing boner in your hand."
            play Chan1[ "<silence 0.1>", "music/sex-noises.mp3" ]fadein 1
            $ renpy.music.set_volume(5, 2, channel = "Chan1")
            show etop a3 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "Its tip already drenched in pre from all the teasing."
            "Holding your cock close to Roushk’s hole, your push inwards slowly."
            "He grits his teeth to stifle his loud groans."
            "You growl softly from the tightness of Roushk’s hole clamping around the head of your dick."
            e 0 "Fuck, you’re tight."
            ro "Mph… more just put it all in!"
            "You force your entire weight onto Roushk , pushing the whole length of your cock inside him."
            "He twists his head and gasps like he has been without air."
            e 0 "Oh… fuck."
            "Thank goodness for the lube or this would be much harder for the both of you."
            "Your back muscles tighten and you hold onto Roushk’s ankles for dear life."
            "You pull your pre soaked dick out of his ass and ram it back in with intense force."
            show etop a4 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "Your knees buckle as a jolt of pleasure travels down your spine."
            "Cocking your head up into the air, you can’t help yourself as you trust the lizard’s hole with increasing vigor."
            "With every smack of the lizard’s firm ass, your balls churns up wave after wave of hot pre."
            "His warm hole loosens up to your thick member fucking him relentlessly."
            e 0 "Roushk , I can’t stop. I’m so close!"
            ro "Yes, yes. Keep going. Fuck me harder!"
            "Roushk’s requests cause you to shudder and moan heavily."
            "Your hips gyrate with intense force, the muscles in your body tenses up as you feel the pressure building inside your balls."
            e 0 "I’m cumming!"
            ro "Fuck!"
            $ renpy.music.set_volume(0, 5, channel = "Chan1")
            with flashbulb
            show etop a5 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "Howling loudly into the night, your entire body is awash with bliss as you shoot thick ropes of semen into Roushk."
            "The lizard screams in unison and his cock explodes with a volley of cum splattering across his stomach and all over the bed of hay."
            "Your body shakes as the last bit of your cum fills Roushk’s insides."
            show etop a6 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "Euphoria is soon replaced by exhaustion as you collapse on top of Roushk."
            "The both of you still panting at each other."
            "Roushk holds you by the shoulder and pulls you into a tight hug."
            hide etop 0
            hide etop 1
            hide etop 2
            hide etop a1
            hide etop a2
            hide etop a3
            hide etop a4
            hide etop a5
            hide etop a6 with slow_dissolve

            jump Roushk_sex_end
        "Fuck Roushk in the slit" if True:
            e 0 "Not yet, I want to enjoy this a bit more."
            "With your middle finger you brush against Roushk’s dickhead."
            "His dick leaks a stream of pre, wetting your finger."
            "Roushk moans, shuffling from side to side slightly as you play with his slit, fucking it with your finger."
            "You pull your finger out with a trail of pre still connecting your fingertip to the warm opening between his legs."
            "Watching him struggle while playing with his vent arouses you more."
            "You bend closer to his crotch and slowly lick his slit."
            ro "Ahh! "
            "Roushk’s thick thighs clamp around your neck holding your face close to his vent."
            "You continue to lap at the lizard’s crotch, sticking your tongue between his slit and wetting his pre soaked insides."
            "With every lick, Roushk ’s hold on you tightens."
            "After a long groan you push yourself upwards and shake your leaking manhood."
            show etop b1 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "There’s only one thing on your mind, to ram your cock in him, and make him beg for more."
            "You rub your raging hard on, mixing your coat of pre with his to lube up your cock."
            "With your dick slick and wet you slap your cock against Roushk’s left thigh."
            e 0 "You ready?"
            ro "Show me your strength, warrior."
            "Pressing your hard dick against his slit you push yourself deeper inside him."
            show etop b2 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            ro "Ugh! [name]..."
            "You manage to push halfway into Roushk ’s slit when you can go no further as you feel the tip of his cock poking against your dickhead."
            e 0 "Damn, that thing is big."
            "The stimulation of feeling both of your cocks touching one another sets your senses on fire."
            "Gripping onto Roushk’s ankles you steady yourself as you pull your hard dick out of his slit."
            "His slit has a tight hold on your cock, just by pulling out you have to fight the urge to not cum inside him right there and then."
            show etop b3 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "You pull your dick back and just before the tip springs out, you slam your cock back in as far as you can."
            "Gritting your teeth, your hips are a blurr fucking him with increasing speed."
            "More and more pre gushes from both your cocks, lubing your entire length."
            "Some of it even leaks through the lizard’s slit."
            "Groaning loudly, you continue to thrust your member inside of his slit. "
            "Roushk struggles to maintain his calm expression."
            "You ram your cock even deeper into his slit at one point, making him yell out in pleasure."
            "The pressure begins to build inside your balls."
            "Your movements start to slow, and your body burns with the heat of ecstasy."
            "Your lust is at its peak, you can’t hold it back anymore."
            e 0 "I’m gonna cum!"
            ro "Me too!"
            with flashbulb
            show etop b4 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "Both of you cum together."
            "Your cock tingles as you feel Roushk’s powerful cumshot coating your cock."
            "Together, the torrantal wave of cum is too much to contain and spills out of Roushk’s slit."
            e 0 "Fuck, I need to pull out. There’s so much inside me right now."
            show etop b5 with slow_dissolve:
                xpos 0.05 ypos 0
                zoom 1
            "A loud plop follows as you pull out your dick."
            "Your whole shaft is wet with your mixed cum."
            "Some of it drips from your cock and splatters against Roushk ’s hole."
            "He shivers a bit from the sudden wet sensation against his ass."
            "Roushk reaches out with one hand and digs into his slit, he stretches open his slit and lets his meaty cock out."
            "The club sized organ was still hard and soaked with cum all over it. "
            "Roushk drops his head back and just breathes heavily."
            "Overcoming exhaustion takes over and you collapse onto Roushk’s embrace."
            "He pulls you close into a warm hug."
            hide etop 0
            hide etop 1
            hide etop 2
            hide etop b1
            hide etop b2
            hide etop b3
            hide etop b4
            hide etop b5 with slow_dissolve
            jump Roushk_sex_end

label Roushk_sex_bottom:
    $ Zalt.lust = 0
    $ sex = True
    $ persistent.CG_roushk_bottom  = True
    $ Zalt.sex = Zalt.sex +1
    e 13 "I do."
    "Roushk smiles at you and caresses your face."
    ro "Then let’s find somewhere more comfortable."
    "He picks himself up and walks over to the door."
    "Giving you a full view of his muscular back lined with deep grooves. "
    "You gulp as the lines on his wide back moves along with every step he takes."
    "He stops at the doorway and turns to you."
    ro "Bring the hay."
    "You pick up the bed of hay Roushk laid on earlier and follow him closely to the other side of the barn where two large stacks of hay pile against the barn wall."
    "Roushk points to an empty spot for you to set up the bed."
    "After scattering the hay on the ground, you turn and bump into Roushk’s broad chest."
    "You’re at a loss for words. Only a weak squeak escapes your trembling mouth."
    "A deep rumble emanates from the lizard’s thick chest."
    "He places a hand on your cheek and gently rubs along your neck, then onto your shoulder."
    "His finger catches the strap of your scabbard and pulls off your almost naked form. "
    "Blowing into your ear, you shudder. "
    "With his other hand he reaches down and pulls your loincloth free. "
    e 5 "Roushk…"
    ro "Now, do me."
    scene black with dissolve
    "He holds your hands and guides them to the side of his rear."
    "Blushing harder, you grasp his firm buttocks, then his loincloth."
    "With one strong pull, the fabric comes off from him."
    "Roushk buries his snout against your neck, kissing and nibbling against it."
    "You can feel the heat rising up against your abdomen."
    "His hard cock presses against yours clumsily."
    "Painting your abdomen with streaks of pre."
    "He spins you around and lands onto the bed of hay."
    "Roushk lays himself out like a succulent meal of muscle and cock, his thick tool twitches at you, inviting you to come closer."
    "And so you do."
    show rtop 1 with slow_dissolve:
        xpos 0.114 ypos 0
        zoom 1
    "You slide down onto Roushk’s naked body until your balls rest upon his monolith of a cock. "
    ro "Steady there."
    "He grabs you by the chest, perhaps to keep you stable, or he just wanted to fondle you more."
    "It amazes you how big his dick actually is as it rests beneath yours."
    "You can feel the beat of his heart pulsing through the dick pressing against your eager hole."
    "You want him bad."
    "He fondles your right pec down to the nub."
    "Twisting and groping your chest, forcing you to moan."
    ro "Take your blessing, [name]."
    "Roushk grabs his hard cock and taps his large dickhead against your hole."
    ro "Ready?"
    e 0 "N...no. "
    ro "Shh… just relax and take deep breaths."
    show rtop 2 with slow_dissolve:
        xpos 0.114 ypos 0
        zoom 1
    "You clench your eyes as you feel the walls of your asshole expand."
    "More and more of Roushk’s dick fills your insides until your butt touches the base of his shaft."
    "You take deep breaths, the pain of putting something so big inside you in one go shakes you to your core."
    show rtop 3 with slow_dissolve:
        xpos 0.114 ypos 0
        zoom 1
    "But slowly all that stinging pain turns into sexual bliss, washing over you like a tidal wave of hot melting ecstasy."
    ro "There, that wasn’t so hard now was it."
    "You just groan in response. "
    play Chan1[ "<silence 0.1>", "music/sex-noises.mp3" ]fadein 1
    $ renpy.music.set_volume(5, 2, channel = "Chan1")
    show rtop 4 with slow_dissolve:
        xpos 0.114 ypos 0
        zoom 1
    "He kicks the hay beneath his feet a few feet back."
    "Your eyes widen when you feel his whole length pulling out of your ass before ramming itself back inside you with intense force."
    "Unable to hold back your cries, you moan heavily."
    "Roushk rides your ass non-stop."
    "Your cock bounces with every thrust of his dick. "
    "Your panting will not cease, as your insides are getting filled with hot pre."
    "Every time his dick brushes against your prostate, you lose control of yourself."
    "Hitting the point of orgasm repeatedly, but he keeps bringing you back by slowing down his trusts."
    "But you desire more, you take it upon yourself to ride his cock."
    show rtop 5 with slow_dissolve:
        xpos 0.114 ypos 0
        zoom 1
    "Loud slapping sounds echoes throughout the barn. Your combined musks permeate the air in the barn, driving you both mad with desire for each other."
    "Your movements start to slow, your cock is throbbing mad , ready to explode."
    "You are practically panting like a dog, yearning for release."
    e 0 "Fuck, I’m going to cum."
    ro "Me too! Argh!"
    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    with flashbulb
    show rtop 6 with slow_dissolve:
        xpos 0.114 ypos 0
        zoom 1
    "With an ear shattering roar the both of you cum at the same time."
    "It feels like someone poured hot cream inside your ass as Roushk’s cock erupts like a newly opened bottle of wine."
    "His cumshot forcefully gushes up your ass, making your toes curl."
    "Your whole body becomes numb as your cock cums shot after shot, splattering all over the barn floor."
    show rtop 7 with slow_dissolve:
        xpos 0.114 ypos 0
        zoom 1
    "Once both of your orgasms subsides Roushk’s cock flops out of your ass with a loud pop."
    "His entire cock is drenched in hot cum."
    "You both look at each other, panting with exhaustion."
    "Roushk rolls you over and pulls you in for a hug."
    hide rtop 1
    hide rtop 2
    hide rtop 3
    hide rtop 4
    hide rtop 5
    hide rtop 6
    scene barn 1 with dissolve
    hide rtop 7 with slow_dissolve
    jump Roushk_sex_end
label Roushk_sex_end:
    e 7 "That was great. "
    ro "I enjoyed it too."
    e 7 "If I ever go through the real ritual I hope it’s just as memorable as what we did."
    "Roushk smiles."
    "You both pull yourselves up and lean against a cool wall."
    e 13 "It’s a shame we won’t see each other anymore after tomorrow."
    ro "We’ll still be connected, by our hearts. Which reminds me."
    "Roushk stands up and runs back into the utility room."
    " It doesn’t take long for him to come running back, and join your side."
    ro "Here, for you."
    "He hands you the cursed bracelet."
    e 1 "Is that thing safe to pass around?"
    ro "It’s safe, I hope when you look at it, you’ll remember me when I’m gone."
    e 13 "Thanks, I wish I had something to give you."
    ro "Do not fret my friend, I’ll treasure our memories forever."
    ro "Plus, I still have some of your nation's coins."
    "You both smile and end up talking a bit longer before you head back to the tavern."
    scene black with slow_dissolve
    play sound "music/foot1.ogg"
    "..."
    play sound "music/door.mp3"
    scene tavern 1 with slow_dissolve
    "When you return to the tavern the party has already died out. "
    show meko stand at center with dissolve
    "Before you can head up to your bedroom, Meko’s horn floats over to your line of sight. "
    m "[name], meet me in the barn tomorrow morning at 6 a.m. I’ll open up the portal for Roushk to go home."
    e 1 "(He can’t even say goodbye to the rest.)"
    m "It’s the best time and place so no one notices me."
    e 1 "Ok."
    hide meko stand with dissolve
    play sound "music/door.mp3"
    scene room 1 with slow_dissolve
    "..."
    jump Roushk_goodbye

label Roushk_goodbye:
    $ Roushk.party = 5
    $ Time.days =Time.days+1
    $ Time.hours = 5
    $ Time.mins = 40
    scene black with slow_dissolve
    "..."
    scene room 1 with slow_dissolve
    e 1 "It’s time to say goodbye to Roushk."
    scene black with slow_dissolve
    "The walk over to the barn feels slower than usual, but no matter how slow you walk you know Roushk has to go home."
    "When you reach the barn Meko is already there with Roushk."
    scene barn 1 with slow_dissolve
    show meko stand70 at left with dissolve
    show roushk stand at right with dissolve
    m "Alright, you’re finally here. Now we can get this show on the road."
    "A loud horn toot blares."
    with flashbulb
    scene barn 2 with slow_dissolve
    show meko stand70 at left with dissolve
    show roushk stand at right with dissolve
    "The empty space in front of Roushk begins to bend and then cracks like a broken mirror revealing a blue round portal."
    m "I can only keep the portal up as long as I have magic. "
    "Roushk peeks through the portal."
    "He pulls back with a wide smile."
    ro "I see the temple on the other side."
    "Roushk looks to Meko."
    ro "Thank you for all your help Meko."
    m "You’rewelcomebutpleasehurryupthisspellissuckingmedry."
    "He turns to you."
    ro "I guess this is goodbye."
    e 3 "Good luck out there."
    ro "You too, and please tell the rest that I didn’t say goodbye to them to spare my heart."
    ro "That much is true, I’ll miss them as much as you."
    hide meko stand70
    hide roushk stand at right with dissolve
    "Roushk rushes over and pulls you into a hug."
    "With a heavy heart you return his hug."
    "You hold each other for a good minute before letting go."
    "You watch as Roushk steps through the portal."
    "He waves goodbye at you from the other side."
    with flashbulb
    scene barn 1 with slow_dissolve
    "There’s just enough time for you to wave back before the portal closes."
    show meko stand at center with dissolve
    "Meko lets out a heavy sigh."
    m "Fuck, that was tiring."
    e 1 "Thanks for helping us out."
    m "You’re welcome. Well, I am going to head back downstairs and rest."
    m "What about you?"
    "You look at where Roushk’s portal was created."
    "The memories of what Roushk told you last night fills you with determination."
    e 1 "The same thing I do every day, figure out how to beat this fog. Let’s go."
    scene black with slow_dissolve
    $ jane_inv_E.take(Roushk_bracelet)
    "And so."
    "Your adventure continues."
    $ Roushk.nauxus = 1
    $ Roushk.snow_e = 1
    $ Roushk.hakan_e = 1
    $ Roushk.witer_e = 1
    $ Roushk.chet_e = 1
    "{b}{color=#19c22a} <[name] gained three Level-up-point.>{/color}"
    $ Zalt.points = Zalt.points +3
    $ Roushk.barn = 2
    $ Time.hours = 6
    $ Time.mins = 30
    play sound "music/door.mp3"
    scene tavern 1 with slow_dissolve
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
    play Snow "music/char_snow.ogg"
    play Hakan "music/char_hakan.ogg"
    play Witer "music/char_witer.ogg"
    play Chet "music/char_chet.ogg"
    jump map1

label Roushk_meko_battle_end2:
    scene outdoor 1n with slow_dissolve
    e 5 "Crap, it’s late. The tavern is dead silent, I must have missed the party."
    e 13 "Way to go, [name]."
    e 13 "I should just go to bed."
    play sound "music/door.mp3"
    scene black with slow_dissolve
    "..."
    play sound "music/door.mp3"
    scene room 1 with slow_dissolve
    show meko stand at center with dissolve
    m "There you are, you missed one heck of a party."
    e 6 "Yeah, I had something to do."
    m "Something more important than your friend’s farewell party?"
    e 13 "It couldn’t be helped."
    m "Mmhmm, well tomorrow at 6 a.m."
    m "I will open the portal in the barn."
    m "Be there, if you want to say goodbye, either way Roushk is going home."
    m "Good night,[name]."
    e 1 "Night."
    hide meko stand with dissolve
    "You head to sleep."
    jump Roushk_goodbye2


label Roushk_goodbye2:
    $ Roushk.party = 5
    $ Time.days =Time.days+1
    $ Time.hours = 5
    $ Time.mins = 40
    scene black with slow_dissolve
    "..."
    scene room 1 with slow_dissolve
    e 1 "It’s time to say goodbye to Roushk."
    scene barn 2 with slow_dissolve
    e 9 "Roushk!"
    "You manage to make it in time, the portal in the barn has already opened."
    show meko stand70 at left with dissolve
    show roushk stand at right with dissolve
    ro "[name], I was afraid I wasn’t going to get a chance to say goodbye."
    e 13 "Me too, there’s so much I want to say. "
    ro "I understand, I wish we had more time to talk."
    ro "Listen, I have to go now, the portal won’t stay up for long."
    ro "Keep this, as my parting gift to you."
    "You receive a bracelet from Roushk."
    e 5 "This is…"
    ro "It should just work as a regular bracelet, don’t worry."
    ro "Thank you for all your help for the past few days my friend."
    ro "Goodbye."
    "Roushk runs through the portal and you watch it close as you hold the bracelet in hand."
    "To your left Meko gasps loudly."
    m "Good grief, keeping that thing up was hard."
    m "I’m going to need to rest. See you later, [name]."
    "Yeah, thanks Meko."
    "Meko’s horn swirls and disappears in a snap."
    "Your heart feels slightly heavy having to see Roushk go back like that."
    "If only there was more time to spend with him."
    scene black with slow_dissolve
    "And so."
    "Your adventure continues."
    $ jane_inv_E.take(Roushk_bracelet)
    "{b}{color=#19c22a} <[name] gained three Level-up-point.>{/color}"
    $ Roushk.snow_e = 1
    $ Roushk.hakan_e = 1
    $ Roushk.witer_e = 1
    $ Roushk.chet_e = 1
    $ Roushk.nauxus = 1
    $ Zalt.points = Zalt.points +3
    $ Roushk.barn = 2
    $ Time.hours = 6
    $ Time.mins = 30
    play sound "music/door.mp3"
    scene tavern 1 with slow_dissolve
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
    play Snow "music/char_snow.ogg"
    play Hakan "music/char_hakan.ogg"
    play Witer "music/char_witer.ogg"
    play Chet "music/char_chet.ogg"
    jump map1
label Roushk_goodbye3:
    $ Roushk.party = 5
    show snow stand1 at center with dissolve
    s "So, Roushk should have headed back by now."
    s "Last I checked, the barn was empty."
    e 13 "Yeah, I guess."
    s "You guess? Didn’t you see him off?"
    e 13 "I kind of missed it."
    s "Hmm, shame. I would have wanted a friend to say goodbye to me if this was my last time seeing them, but who am I to judge right?"
    s "By the way, when I checked the barn I found this."
    "Snow hands you a bracelet, you recognize it as the one Roushk wore."
    s "I figure he meant this for you. Take it."
    $ jane_inv_E.take(Roushk_bracelet)
    e 1 "Wow, thanks Snow. I’ll keep it safe."
    hide snow stand1 with dissolve
    "Snow grunts affirmatively."
    scene black with slow_dissolve
    "And so."
    "Your adventure continues."
    "{b}{color=#19c22a} <[name] gained three Level-up-point.>{/color}"
    $ Roushk.snow_e = 1
    $ Roushk.hakan_e = 1
    $ Roushk.witer_e = 1
    $ Roushk.chet_e = 1
    $ Roushk.nauxus = 1
    $ Zalt.points = Zalt.points +3
    $ Roushk.barn = 2
    $ Time.hours = 6
    $ Time.mins = 30
    play sound "music/door.mp3"
    scene tavern 1 with slow_dissolve
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
    play Snow "music/char_snow.ogg"
    play Hakan "music/char_hakan.ogg"
    play Witer "music/char_witer.ogg"
    play Chet "music/char_chet.ogg"
    jump map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
