label battle_katos:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 300
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 20
    if jane_inv_E.qty(murphy_hand) == None and Items.Murphy_Hand == 1:
        $ Zalt.cor = min(Zalt.cor +2, 100)
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    $ Map.good_battle = True
    $ Battle.holyfcd = 0
    stop music








    jump battle_katos_loop


label battle_katos_loop:



    show screen simple_stats_screen
    show screen battle_menu
    window hide None
    show katos at center
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
                $ Random = renpy.random.randint(1, 3)
                if wolf_hp <= 0:
                    pass
                elif True:
                    if Random ==1:
                        "You let the creature chase you then at the last minute you dodge to the left."
                        "Unable to turn the monster slams face first into a tree.\n(Damage dealt- [red_damage]hp)"
                    elif Random ==2:
                        "You grab a wad of dirt and manage to throw it in the monster’s eyes, blinding it and causing it to crash into a tree.\n(Damage dealt- [red_damage]hp)"
                    elif True:
                        "You slash one of the monster’s feet.\n(Damage dealt- [red_damage]hp)"
            elif True:
                $ qty = red_damage*2
                $ wolf_hp -= red_damage*2
                if wolf_hp <= 0:
                    pass
                elif True:
                    "You slash one of the monster’s feet.\n{b}{color=#ffd65c}(Critical damage! -[qty]hp){/color}"

        if res == "Submit":
            e "I can't fight anymore.."
            "The enemy is too strong."
            "You’re knocked onto the ground."
            jump battle_katos_lose
        if res == "Flirt":
            $ Random = renpy.random.randint(1, 6)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You growl to assert your dominance, showing your foe who is boss."
                "The enemy is taken aback and feels a rising sensation of arousal."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You pin the foe down and force it to smell your pits."
                "The enemy is shocked and hungers for your smell again."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+10)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You perform a seductive dance."
                "The enemy is feeling heaty and eyes you hungrily. "
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You growl to assert your dominance, showing your foe who is boss."
                    "The enemy feels nothing for your attempts to seduce it. "
                elif Random == 2:
                    "You pin the foe down and force it to smell your pits."
                    "The enemy growls angrily at you, you could not seduce it."
                elif True:
                    "You perform a seductive dance."
                    "The enemy ignores your seduction and leers at you."

            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                jump battle_katos_win
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
            "You can't run!"
        elif True:
            pass
        if wolf_hp <= 0:
            jump battle_katos_win

        $ Random = renpy.random.randint(1, 4)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The creature darts left and right dodging your swings and claws your right arm."
                "But you dodged its attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(15, 45)
                $ Zalt.hp -= wolf_damage
                "The creature darts left and right dodging your swings and claws your right arm."
        elif Random == 2:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The creature rushes forward and headbutts you in the stomach."
                "But you dodged its attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(35, 50)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The creature rushes forward and headbutts you in the stomach."
        elif Random == 3:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The creature fakes you out by pretending to claw at your face but actually chomps down on your leg."
                "But you dodged its attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The creature fakes you out by pretending to claw at your face but actually chomps down on your leg."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "The side of the creature’s face charges blue."
                "It lets loose a bolt of lightning from its mouth."
                "But you dodged its attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(10, 80)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "The side of the creature’s face charges blue."
                "It lets loose a bolt of lightning from its mouth."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1





    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_katos_win
        elif True:

            jump battle_katos_win

    elif Zalt.hp <= 0:
        jump battle_katos_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_katos_lose
    elif True:
        jump battle_katos_loop


label battle_katos_win:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    play music "music/forest_fight_boss_end.ogg" noloop
    hide katos with slow_dissolve
    "You kick the creature into a tree."
    "Before it can get up, you rush forward and swing your blade across its neck."
    "Your blade cuts through and sends its dismembered head rolling across the ground."
    "Its dark blood spurts out of its exposed neck painting the bark of the tree in horrid black."
    e 1 "Finally, it’s done. "
    "You sheath your weapon and walk over to the pile of fruits."
    e 1 "This is just enough for one village."
    "Most of the fruits have been bitten into"
    "You begin to pack the fruits into the bags you brought. "
    "Both bags are filled to the brim with fruits."

    "You get 1 Katos's horn and 300 EXP."
    $ jane_inv_M.take(katos_horn)
    $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))

    if jane_inv_K.qty(sack) == 2:
        $ jane_inv_K.drop(sack,2)
    if jane_inv_K.qty(sack) == 4:
        $ jane_inv_K.drop(sack,4)
    if Quest.fesn >=2 and Quest.fesa >=2:
        e 5 "Both villages need these fruits, but there is only enough to feed one village."
        e 1 "Then again, I could split it between them, but then no one is happy in that situation."
        e 13 "No I must choose."
        menu:
            "Give all to the Lizards" if True:
                e 13 "The lizards need this more."
                "You decide to go to the lizard village."
                jump Festival_ending_lizard
            "Give all to the Bulls" if True:
                e 13 "The bulls need this more."
                "You decide to go to the bull village."
                jump Festival_ending_bull
    elif Quest.fesa >=2 and Quest.fesn <2:
        e 1 "Time to go, the bulls are waiting."
        "You head to the bull village."
        jump Festival_ending_bull
    elif Quest.fesa <2 and Quest.fesn >=2:
        e 1 "I hope the lizards will enjoy this."
        "You head to the lizard village."
        jump Festival_ending_lizard
    elif True:
        "If you see this ,that mean the game is bugged, pls report to Caro, thx!"

    jump forest_map

    return



label Festival_ending_bull:
    $ Quest.fes_result = Axel
    $ Axel.s = Axel.s - 2
    $ Quest.fesa = 6
    $ Quest.fes = 3
    $ Quest.fes_end = 1

    stop Chan1
    stop Chan2
    scene black with vslow_dissolve
    "You heave the sacks of fruit all the way to the bull village."
    if Time.hours >= 6 and Time.hours <= 17:
        scene tribe 1 with slow_dissolve
    elif True:
        scene tribe 1n with slow_dissolve
    "Upon entering the village, you notice how the place has been completely decorated, giving it a very festive feel."
    "You’d enjoy the sights more if you didn’t have two heavy sacks of fruits to lug around."
    "Stopping by the shop, you drop off the fruits to the shopkeeper."
    "Bull Shopkeeper" "Good job kiddo, this ought to get the festival running again."
    "Bull Shopkeeper" "Why don’t you do me a favour, and go inform Chief Axel that we can start the festival when he’s ready? "
    "Bull Shopkeeper" "I bet he’ll appreciate the good news."
    "You accept the task and head off to Axel’s tent."
    if Thane.movein == 2:
        scene bulltent with slow_dissolve
        "Chief Axel is reading a piece of paper when you enter his tent."
        show axel stand at center with slow_dissolve
        a "Hmm? Oh, you’re back. How’d it go?"
        e 1 "I’ve dropped the fruits off at the shopkeeper’s. You’re all good for the festival."
        a "Excellent. Then I have one last job for you."
        a "Here."
        "<[name] gained 400 coins>"
        "<[name] gained one Level-up-point.>"
        $ jane_inv.take(coin,400)
        $ Zalt.points = Zalt.points +1
        hide axel stand at center with slow_dissolve
        "Axel pulls from the side of his throne a basket filled with an assortment of jars of foods and pieces of fabric."
        show axel stand at center with slow_dissolve
        a "Give this to Thane, the food you can share with the tavern folk."
        a "I’m sure my son doesn’t need to worry about food there."
        e 6 "Is this like a care package? That’s sweet."
        "Axel’s nostrils flare up."
        a "My foolish son may be persistent in defying me, but... he is still my son, and is a part of this tribe."
        a "At least he should have something to remind him of today’s festival."
        a "Now go. I have a festival to prepare."
        e 3 "Very well chief."
        hide axel stand at center with slow_dissolve
        "You take the basket of goods and make your back to the tavern."
        scene black with vslow_dissolve
        pause 3
        play sound "music/door.mp3"
        play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
        scene tavern 1 with slow_dissolve
        "You return to the tavern, but Thane is nowhere to be seen."
        e 1 "Hmm, Thane still isn’t back yet?"
        show snow stand with slow_dissolve
        s "Haven’t seen him the whole day. Maybe he’ll turn up later."
        e 6 "Yeah, you’re right."
        hide snow stand with slow_dissolve
        scene black with slow_dissolve
        "You sit down and play some card games with Hakan until nightfall."
        pause 3
        scene tavern 1 with slow_dissolve
        e 1 "It’s getting pretty late."
        stop music fadeout 5
        "Then you hear the creak of the tavern door opening."
        play sound "music/door.mp3"
        "You turn towards the door and you’re shocked by what you see."
        pause 2
        show thane dying1 at center with vslow_dissolve
        "Thane is clutching his spear for dear life while dripping blood from head to toe."
        play sound "music/body_fall.mp3"
        hide thane dying1 at center with slow_dissolve
        "His body is a bloodied mess with blood gushing out of the many open wounds across his muscled frame."
        e 9 "Thane!" with vpunch
        "You rush over just in time to grab him."
        h "Holy crap the kid is badly hurt. "
        s "Witer, get the kit! Chet, set up the floor."
        s "Hakan help to bring Thane over here, now!" with vpunch
        "The hyena rushes out with a brown mat he pulled out from his bag of items."
        "Hakan picks Thane up from you and cradles the bull all the way to the front of the bar."
        "The dragon then sets Thane on the mat."
        "You walk up and feel sick to the stomach seeing your friend in such a beaten state."
        e 9 "I’ll go get a bucket of water."
        "Thane’s hand lunges upward and grabs yours." with vpunch
        e 5 "Thane?"
        t "{cps=10}Listen...{/cps}"
        "You crouch down to listen to the weary bull."
        "He winces in pain as though every breath is piercing his chest."
        e 9 "No, you can tell me after we patch you up."
        t "{cps=10}Listen...{/cps}"
        t "{cps=7}Lizard...{/cps}"
        "You press your head closer to hear his faint words."
        t "{cps=5}Lizard. Was{/cps}{cps=1}...Lie.{/cps}"
        pause 2
        e 5 "What? Thane what do you mea-"
        "His eyes close and Thane loses consciousness."
        e 12 "THANE!" with vpunch
        show snow angrys1 with slow_dissolve
        s "Shhh, he just fell unconscious."
        s "If you want to help go get the bucket of water."
        s "We need to treat his wounds quickly."
        hide snow angrys1 with slow_dissolve
        scene black with slow_dissolve
        "You make haste into the kitchen to grab the water. "
        pause 3
        scene tavern 1 with slow_dissolve
        "When you return with the water, Witer quickly grabs it and starts cleaning Thane’s wounds."
        show snow angrys1 with slow_dissolve
        s "You better wait outside [name]."
        e 5 "What? Why?"
        s "We don’t know what could have done this to him."
        s "I need you and Hakan to keep watch just in case we’re in trouble."
        s "You can come back after you’re done making sure we’re safe."
        e 12 "But I-"
        h "Come on Fuzzbutt. You heard the boss."
        hide snow angrys1 with slow_dissolve
        scene black with slow_dissolve
        play sound "music/door.mp3"
        "Hakan grabs you by the fur on the back of your neck and pulls you away."
        scene outdoor 1n with slow_dissolve
        show hakan stand with slow_dissolve
        e 12 "W-wait. Thane needs me."
        h "No he doesn’t, the guys can take care of him."
        h "Now you’re patrolling with me."
        h "We got to make sure there’s nothing dangerous around."
        e 12 "..."
        "You sigh."
        e 13 "Alright, fine."
        hide hakan stand with slow_dissolve
        scene black with slow_dissolve
        "Hakan walks ahead and you follow him."
        "You both start by checking the nearby barn and bath house before heading to the area closest to the forest."
        "There was no exchange of words, all you want to do is find the person or creature responsible for this and have his head."
        "However, your patrol yielded nothing."
        "You both return to the tavern."
        "Inside the drinking hall, Witer and Thane are nowhere to be seen."
        scene tavern 1 with slow_dissolve
        show snow stand with slow_dissolve
        e 5 "Where-"
        show snow happy1 with slow_dissolve
        s "We moved Thane to his room. He’s stable for now and Witer will watch over him for the night. "
        "Hakan smacks you in the back."
        h "See Fuzzbutt, everything’s alright."
        "You breathe a sigh of relief."
        e 13 "Yeah, I’m glad."
        "You take a seat at the bar."
        e 13 "Ugh, this is a crazy night."
        s "And it’s not over yet."
        e 1 "Why?"
        s "Because you need to tell Axel that his son is beaten up badly here. "
        e 5 "Crap, you’re right."
        show snow stand1 with slow_dissolve
        s "But you need to make sure that Axel doesn’t get any ideas about sending his men to overtake the tavern."
        e 1 "How do I do that?"
        s "Very firmly and don’t back down."
        s "Remind him that we are caring for his deeply injured son, and if he wishes to keep it that way he’ll not overstep his boundaries."
        s "I’ll permit healers from their tribe but nothing more."
        e 13 "Why don’t you just let them take Thane back? He’s safer at his tribe."
        s "If you see the condition he’s in you’ll know he is in no condition to be moved. Now go."
        "You nod."
        hide snow stand1 with slow_dissolve
        scene black with vslow_dissolve
        play sound "music/foot1.ogg"
        "When you arrive in the bull village, the celebration is over."
        "Signs of a bonfire are all that remains near the bull entrance."
        "You run up to the chief’s tent to tell Axel what has happened. "
        "Chief Axel sits upon his throne."
        scene bulltent n with vslow_dissolve
        show axel stand with slow_dissolve
        e 5 "Chief Axel." with vpunch
        a "Fleabag, I didn’t expect to see you today. Waddya want?"
        e 1 "It’s about Thane."
        a "Yeah, you seen him? I need to have a long talk with him about his curfew. "
        "You take a deep breath."
        e 13 "He’s recovering from some injuries back at the tavern."
        a "Injuries? What!? " with vpunch
        "The chief stands up, his mouth falls open and his eyebrows furrow in shock and horror."
        e 13 "No he’s stable. We managed to patch him up as best we could."
        a "No, I need to get to him, I need to be with him. Guard!"
        "A bull guard enters the tent."
        a "Ready the healers, and the troops we’re moving out to-"
        e 5 "No, you can’t send your men to the tavern."
        e 5 "Snow only allows the healers."
        e 13 "Please, you have to respect that it is a neutral ground."
        a "What? My son is dying in your tavern and you dare stand in my way to treat him?"
        e 5 "I’m doing no such thing."
        e 1 "You’re just going to attract more attention if your men are there, and Thane is in no position to be moved."
        e 12 "Send the healers only!"
        a "..."
        "Axel looks to the guard."
        a "Have the healers ready to move out, they will be escorted by Fleabag."
        "The guard nods and leaves."
        "Axel begins pacing about, his angry eyes never once looking away from you."
        a "Tell me, {cps=7}who hurt my{/cps}{cps=3}son?{/cps}"
        e 5 "We don’t know. "
        a "..."
        "His cold eyes watching, waiting for you to try to lie to him."
        a "Did my son say anything when you found him?"
        e 13 "He... he said Lizard. Was. Lie."
        hide axel stand with slow_dissolve
        pause 3
        a "{cps=10}Lizards!{/cps} {cps=25}AAAAAAHHHHHHHH!{/cps}" with vpunch
        "The chief’s monstrous roar forces you to step back."
        a "I’ll have their heads! No more mercy, they’re all dead by sunrise."
        e 5 "What? What are you talking about? You can’t kill them all in one night that’s impossible."
        a "No, but those pieces of trash taking up space in my prison, they will pay for what their kind did to my son."
        e 9 "That’s insane, you cannot kill them, they're innocent."
        a "Don’t talk to me about innocence. They did this to my son."
        a "MY SON!" with vpunch
        e 1 "You do not know that. That message could have meant anything."
        a "AAAAHHHH!" with vpunch
        e 5 "Think this through chief."
        e 5 "If Thane wakes up and he finds out innocent lizards died because you did it under Thane’s name... he’d... he’d never forgive you."
        "The bull chief’s nostrils flare up, his eyes are practically red with rage."
        e 13 "You’ll lose him further than ever before."
        a "Get out! "
        e 5 "Chief!"
        a "I said out! I don’t want to see you for the rest of the day. "
        "Axel steps forward and presses his finger angrily at your chest."
        a "You better make sure my son stays alive or else!"
        "Your ears fall and you take your leave."
        scene bulltribe 1n with slow_dissolve
        "Once you reach the entrance two bull healers are waiting for you."
        "You escort them to the tavern."
        "..."
        pause 3
        scene room 1 with slow_dissolve
        "The healers get to work quickly freeing up Witer’s responsibilities."
        "You rub the back of your neck."
        "There’s just so much tension building it over the past two days."
        e 1 "I better check in on Chief Axel tomorrow."
        e 13 "He looked like he would do something crazy. "
        scene black with vslow_dissolve
        pause 3
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
        jump Room1
    elif True:
        scene bulltent with slow_dissolve
        "You see Chief Axel pacing back and forth in his tent."
        e 1 "Chief Axel."
        a "Huh?"
        "He turns to you."
        show axel stand with slow_dissolve
        a "You’re back. How did it go?"
        e 1 "I’ve got the fruits back, and a bunch more actually."
        e 1 "I think the creature must have hit another spot too."
        a "Hah! More fruits, that’s a win if I ever saw one."
        a "You actually did a good job Fleabag."
        e 6 "Thanks chief."
        a "That's why I want you to fill Thane's seat at the festival tonight."
        e 5 "Me? But what if Thane shows up?"
        a "Bah, if my son wanted to come, he would have stayed to help with the preparations."
        a "He of all people knows how important this is."
        a "You'll fill his seat next to me, and I don't want to hear anymore questions about it."
        e 13 "Got it. "
        a "Here’s your reward for a job well done."
        "<[name] gained 400 coins>"
        "<[name] gained one Level-up-point.>"
        $ jane_inv.take(coin,400)
        $ Zalt.points = Zalt.points +1
        e 1 "Is there like some kind of a dress code for this festival?"
        e 6 "Because all I brought with me to this forest is just this."
        "You point to your loincloth."
        a "Does it look like the bulls here are dressed up for the festival?"
        e 9 "Now that you mention it, no."
        a "Even if we weren’t in the middle of war preparations, our tribe isn’t well known for our choice of clothing."
        a "As long as it covers what it needs to cover, then it’s good enough."
        e 1 "Still, don’t you guys want to look good when you entertain guests or something?"
        a "Hah, our guests enjoy our men’s brawny muscles and the healthy glow of our tribe’s women whenever they come. "
        a "Why would you want to cover any of this up?"
        hide axel stand with slow_dissolve
        "Axel flexes his right arm and you instantly press your thighs close to one another."
        "You force yourself not to smile too widely at the older bull’s bulging arm."
        "Axel brings his arm down."
        a "Heck, if I could I’d make it a law that everyone goes about in the nude."
        e 6 "That would be beefy heaven."
        show axel stand with slow_dissolve
        a "What did you just say? I didn’t catch that."
        e 10 "I... said, that would be hard to pull off. "
        "Axel shrugs."
        "Your cheeks start to burn and you feel flustered looking at the chief."
        e 1 "Anyways, I better get ready for tonight. See you later Chief Axel."
        a "Sure."
        hide axel stand with slow_dissolve
        "You leave the tent."
        scene black with vslow_dissolve
        "With the festival happening later in the night, you decide to freshen up in your hut."
        $ Time.days = Time.days+1
        $ Time.hours = 18
        $ Time.mins = 30
        scene room 3n with slow_dissolve
        "As the start of the festival approaches, you hear the sound of drums beating, footsteps moving to and fro and jolly laughter coming from outside."
        e 1 "Sounds like the preparations are about done."
        "You finish wiping yourself with the wet cloth provided in your room and head out."
        play sound "music/door.mp3"
        scene bull fesnight with slow_dissolve
        play music "music/small-bonfire.ogg"
        "From your hut, you can see the bulls making their way to the entrance of the bull village."
        e 1 "So the celebration is out in the open."
        "You head over to join the tribe."
        "The fruits you brought back earlier have been washed and are now served on long tables that are placed on the left and right of the entrance. "
        "The bulls are gathering around the table and scarfing down the fruits with gusto."
        "Even among those who look down spirited are pulled along and encouraged to eat something."
        "In front of each table, there are many straw mats spread out around the gate in an almost U shaped formation."
        "Right in the middle of the formation there is a roaring bonfire."
        "Its warm flames flicker and dance in the night."
        "You walk over to the mats and notice that on the side of each one there is a long pole next to it that bears a piece of tapestry."
        "Before you can take a closer look, you hear someone calling your name."
        "A bull warrior is waving at you to join them to eat."
        "What do you want to do?"
        menu:
            "Continue looking at the tapestries" if True:
                "You wave back at the group but point down to the carpets indicating you want to spend time looking at them."
                "The bull warrior sends you a thumbs up and rejoins his group."
                "Turning your attention back at the tapestries, you realize that each one had a different pattern embroidered into it like a sort of coat of arms. "
                "Starting from the left side of the entrance, the first embroidery is a series of gold weapons arranged in a circle placed against a red backdrop."
                "Next to it, is a piece that shows a bull fighting a multi headed snake monster."
                "Then the next one appears lavishly long with a multitude of coloured squares from one end to the..."
                e 13 "Oh, it’s incomplete."
                a "It is complete."
                show axel stand with slow_dissolve
                "Chief Axel appears behind you, the sounds of the ongoing celebration must have masked his footsteps."
                "The chief looks at you and crosses his arms."
                a "These coats of arms are a testament to who lives here."
                e 1 "What do you mean chief?"
                a "It is our tribe’s tradition that every year when the festival comes."
                a "The villagers group up and make a new coat of arms to represent their group or family."
                a "The patterns you see tell a story about who the bulls are or where they came from. "
                "Chief Axel walks from one coat of arms to another as he continues his explanation."
                stop music
                scene tribe 1n with slow_dissolve
                "You follow from behind while listening attentively."
                a "That special patchwork you said is incomplete is actually from a family that has maintained its name through the ages."
                a "From the original bloodline to the foster children they took up."
                a "The first one are by the guard bulls, they showed off their favourite weapons."
                a "Over here, the tapestry with the picture of bulls crafting a weapon belongs to the shopkeeper."
                hide axel stand with slow_dissolve
                "Axel stops right in front of the coat of arms placed in the very center of the mats."
                "Embroidered in yellow, brown, and white thread is a picture of the bull village."
                "All around the tapestry little bull figures are sewn in."
                "The bulls are shown to be doing their tasks around town."
                "Where the chief’s camp is placed, two figures are seen sitting in front of the tent."
                "You recognize them as Axel and Thane."
                e 1 "This is..."
                show axel stand with slow_dissolve
                a "It’s what Thane and I made earlier this year... before the whole war thing broke out."
                "Axel looks longingly at the carpet and sighs."
                a "It took us months to make that and he can’t even be bothered to show up."
                a "Bah, come take a seat next to me, the dance is about to begin."
                e 5 "Oh, alright."
                hide axel stand with slow_dissolve
                scene black with slow_dissolve
                pause 2
            "Join the bull group" if True:
                if Quest.campw1 != 4:
                    "You approach the bull that invited you."
                    "He is sitting with Tomahawk and a group of other bulls around their personal plate of fruits."
                    "Bull Warrior" "Hey, hey welcome to the party Fleabag. "
                    "Bull Warrior" "Want some fruit?"
                    "The bull offers you an apple."
                    e 6 "Thanks, but I’ve had my fair share of fruits today."
                    "Tomahawk" "MORE FOR US THEN!"
                    "The rowdy and very large bull makes his presence known with his loud voice."
                    e 1 "Tomahawk, nice to see you again."
                    "Tomahawk takes a big bite from a piece of watermelon."
                    "Tomahawk" "News around the village is that you brought back these fruits? "
                    e 1 "Yeah, it was no easy feat."
                    e 1 "There was this crazy monster guarding all the fruits."
                    "Tomahawk" "Hah, a fruit stealing monster."
                    "Tomahawk" "How hard can that be? Chief Axel should have sent me and the boys."
                    e 8 "Please I’m sure you’d have eaten all the fruits before you made it back."
                    "Tomahawk" "Hmm... that is true."
                    "The whole table bursts into laughter."
                    "You can’t help but join in the fun. "
                    "You and the bull warriors exchange stories for a few minutes until Chief Axel reaches the festival area and calls for you."
                    show axel stand with slow_dissolve
                    e 1 "Chief Axel."
                    a "Having a good time chatting it up with the men?"
                    e 6 "Yeah, it’s nice to just sit down and chat without having Tomahawk trying to get in my way."
                    a "You’ll have more time to chit chat after the dance. "
                    e 1 "What kind of dance?"
                    a "It’s a show we put on every year. Come, sit next to me."
                    hide axel stand with slow_dissolve
                    scene black with slow_dissolve
                    pause 2
                elif True:
                    "You approach the group of four bulls."
                    "They've formed their own circle with a plate of fruits for them to share."
                    "Bull Warrior" "Saw you walking around alone, why don’tcha join us here."
                    e 1 "Thanks, so how’s everyone enjoying the festival?"
                    "Second Bull Warrior" "Could be better if Tomahawk and his team were here."
                    "Second Bull Warrior" "Things just got quiet around since he died."
                    e 13 "Yeah... it was terrible what happened..."
                    "Sombreness falls upon the circle of bulls."
                    "Bull Warrior" "Come on, let’s not spoil the festival for Fleabag here."
                    "Bull Warrior" "It’s his first time."
                    "Second Bull Warrior" "Sorry there, Brother."
                    e 1 "No, it’s fine. Let’s just enjoy the food."
                    "You force yourself to eat along with the bulls even though you’re not really in the mood for food."
                    "The group makes small talk about the weather and what they plan to do after the war."
                    "After a few minutes, Chief Axel comes to the group."
                    show axel stand with slow_dissolve
                    a "Fleabag, come sit with me."
                    a "You’ll have a nice view of the dance."
                    e 1 "There’s a dance?"
                    a "It’s the main part of the festival, come."
                    e 1 "Ok, guys I’ll talk to you all later."
                    "The bulls wave at you as you walk over to join Axel on the red carpet."
                    hide axel stand with slow_dissolve
                    scene black with slow_dissolve
                    pause 2
        play music "music/small-bonfire.ogg"
        scene bull fesnight with slow_dissolve
        "As you and Chief Axel take your seats on the red carpet, the other bulls do the same. "
        "They break into their groups and families and fill the remaining carpets."
        "Six bulls walk up to the bonfire, standing in pairs of males and females."
        "They bow to Axel."
        "He then stands up, your eyes follow his face upwards, his expression is stern but he maintains a soft smile."
        "The chief extends his hands out to his people and begins a speech in an unknown language."
        "You try as hard as you can to guess what he is saying but it is unlike anything you’ve heard before."
        "It must be their tribe or their kinds’ own language."
        "You sit in silence as Axel continues speaking."
        "Once he finishes, the tribe cheers in unison and you hear the beat of drums."
        "Axel takes his seat next to you."
        "You turn away from him to look at what the other bulls are doing."
        "The dancers in front of you ululate in unison and begin their dance around the bonfire."
        "Their every step follows the beat of the music."
        scene black with slow_dissolve
        "The dancers move with surprising grace as their footwork is accompanied by powerful hand gestures like how warriors wield their weapons."
        "You watch enthralled by the music and movement, your tail wags happily as the performance continues."
        stop music fadeout 5
        $ renpy.music.set_volume(0.5, 0, channel = "sound")
        "Until..."
        play sound "music/woman-scream.ogg"
        "Someone in the crowd lets out an ear piercing scream."
        "The music stops. All eyes turn to the gate of the bull village. "
        $ renpy.music.set_volume(1, 5, channel = "sound")
        scene tribe 1n with slow_dissolve
        pause 2
        show thane dying at center with vslow_dissolve
        "Standing there clutching his spear for support while covered in blood was Thane."
        play sound "music/body_fall.mp3"
        hide thane dying at center with slow_dissolve
        pause 1
        "You jump up to your feet just as he collapses to the ground."
        a "THANE!" with vpunch
        "Thane’s father rushes towards him and you follow from behind. "
        "The crowd swarms in and forms a circle around the chief’s son. "
        "Axel manages to roll Thane’s bloodied body over."
        "Despite his broken state Thane is still breathing."
        t "{cps=10}Father...{/cps}"
        a "Healers! Where are the god damn healers?" with vpunch
        a "Bring the stretcher and prepare the healing hut!" with vpunch
        "You hear the sound of footsteps running off from the crowd."
        t "{cps=10}[name] ...{/cps}"
        a "Thane, save your breath."
        t "{cps=10}[name] ...{/cps}"
        a "[name]? Fleabag get over here!"
        "You rush forward and kneel down next to Axel."
        e 5 "Thane? I’m here."
        t "{cps=10}Listen...{/cps}"
        e 1 "The lizards?"
        t "{cps=5}Lizard. Was{/cps}{cps=1}...Lie.{/cps}"
        pause 2
        "His eyes close."
        a "THANE!" with vpunch
        e 5 "He’s ok, he’s ok. He’s still breathing."
        "The crowd breaks into a frenzy of murmurs and chatter."
        "Word of lizards attacking Thane begins to spread through the crowd."
        "The healers then arrive and work together to move Thane onto the stretcher."
        "They then take him to the healing hut."
        "Chief Axel stands where his son’s bloodied body laid earlier looking at his blood soaked hands."
        "His hands tremble."
        e 1 "Chief-"
        a "Celebrations over!" with vpunch
        a "Everyone back to your huts!"
        a "I want all guards at their stations now. "
        a "I don’t want even the shadow of what’s not part of our tribe to step through. "
        "The chief walks straight ahead to follow the healers. "
        "Without saying a word, the crowd breaks apart letting him through."
        "The crowd slowly makes their way back to their homes guided by the bull warriors."
        "You on the other hand stand there dumbfounded by what you’ve witnessed."
        e 9 "What the fuck was that? Lizard. Was. Lies? "
        "You grip the fur on your head trying to figure out what it all means."
        e 13 "Dear gods... Thane."
        "After all that has happened, you decide to sleep in your hut in the bull village."
        scene black with vslow_dissolve
        pause 3
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
        jump Room3



label Bull_hanging:
    $ Quest.fesa = 7
    if Quest.fesn == 7 and Quest.fesa == 7:
        $ Quest.fes_end = 2
        if Time.hours >= 6 and Time.hours <= 17:
            scene tribe 1 with slow_dissolve
        elif True:
            scene tribe 1n with slow_dissolve
        "To your horror, three lizard bodies are hanging by a gallow built in front of the bull village."
        e 9 "What? Why-When did they do this?"
        "Their lifeless forms sway at the mercy of the winds."
        if Thane.movein != 2:
            "Bull Guard" "Hey! Who’s there?"
            "A bull guard approaches you with his sword drawn."
            e 5 "It’s me. "
            "The guard sheaths his sword."
            "Bull Guard" "You shouldn’t be standing out here for no reason."
            "Bull Guard" "Everyone's been on edge since last night."
            e 5 "Yeah? Is that what caused that?"
            "You point to the gallows."
            "Bull Guard" "The chief was mad."
            "Bull Guard" "Thane came back injured and bloodied."
            "Bull Guard" "Mentioned something about a lizard and lies."
            "The guard sighs."
            "Bull Guard" "That Black Bull really has no luck."
            "Bull Guard" "Getting ambushed by the lizards."
            e 5 "I want to see Thane, where is he?"
            "Bull Guard" "No can do Fleabag. Only the chief is allowed visiting rights."
            "Bull Guard" "And don’t even try talking to the chief. He has banned all visitors to his tent."
            "Bull Guard" "Now please go ahead and do your business."
        elif True:
            "Bull Guard" "Hey! Who’s there?"
            "A bull guard approaches you with his sword drawn."
            e 5 "It’s me. "
            "The guard sheaths his sword."
            "Bull Guard" "You shouldn’t be standing out here for no reason."
            "Bull Guard" "Everyone's been on edge since last night."
            e 5 "I want to see Thane, where is he?"
            "Bull Guard" "No can do Fleabag. Only the chief is allowed visiting rights."
            "Bull Guard" "And don’t even try talking to the chief. He has banned all visitors to his tent."
            "Bull Guard" "Now please go ahead and do your business."
        "You enter the village frustrated and left with many unanswered questions."
    elif True:
        scene tribe 1 with slow_dissolve
        "The moment you enter the bull tribe, a crowd has gathered around the bull entrance."
        "They surround what looks like a gallow, and to the side of it, three lizard shaped figures stand next to the gallow."
        e 5 "What?"
        "You run down the steps and hurry to the entrance."
        "Using all your strength, you push through the crowd until you break through to the front row of the right side."
        "The chief is right across from you watching, the lizards make their way up the platform."
        "His eyes they’re red like he has been crying all night long."
        e 5 "CHIEF! What are you doing?"
        "He turns his head to face you."
        show axel stand with slow_dissolve
        a "I’m paying these lizard bastards for what they did to my son!"
        a "The lizards look frail and small as thought they’ve been barely kept alive, they couldn’t be the ones who have hurt Thane."
        a "These must be the prisoners of the bull tribe. "
        e 5 "You need to think this through, killing random lizards isn’t the way to help Thane."
        a "They’re all the same." with vpunch
        a "I don’t need to be lectured by someone who doesn’t even know the pain of seeing a son hurt."
        hide axel stand with slow_dissolve
        "Axel raises his hand signaling to the executioner to put the bags over the lizards’ head."
        "You can hear the muffled cries of the lizards."
        "The executioner moves to tie the noose around each of their necks."
        "Your mind is reeling."
        "All you can hear is the sound of your heart pounding madly from your chest."
        menu:
            "Stop the execution" if True:
                e 5 "Stop! You can’t do this. Think about Thane."
                a "It is because of Thane that I am doing this!" with vpunch
                "The chief’s thunderous voice shakes your courage, but you stand strong."
                e 1 "No, if you really care about him, then you won’t do it."
                e 13 "You’re reacting out of anger and sadness."
                e 1 "What will happen when he wakes up and he finds out that you did this?"
                a "Then he will learn to be thankful I took revenge for him!"
                e 1 "You don’t know that, you could be driving him further away from you."
                e 1 "What if he blames himself for all of this?"
                e 12 "Can you live with that?!"
                if Axel.s <=3:
                    "Axel scowls at you and turns back to the executioner."
                    "He raises his hands once more."
                    "You sense the look of every pair of eyes watching, waiting for what the chief would do."
                    "You dare not move a muscle."
                    "The chief’s hand forms into a fist and you see him trembling, the ramifications of his mind are unknown to you."
                    pause 4
                    "Then he retracts his hand."
                    show axel stand with slow_dissolve
                    a "Send them back to their dirt jail!"
                    a "I don’t want to see or smell their putrid scent."
                    a "I want all warriors assembled at the training grounds. It’s time for war!"
                    hide axel stand with slow_dissolve
                    "The crowd cheers, the civilians rush back into their homes while the bull warriors make their way to the training grounds."
                    "You try to make your way to Chief Axel to ask where Thane is but he moves too quickly and is off to be with the rest of his men."
                    e 13 "This is it... it’s war."
                    $ Quest.fest = 1
                elif True:
                    "Axel scowls at you and turns back to the executioner. "
                    "He raises his hands once more."
                    "You sense the look of every pair of eyes watching, waiting for what the chief would do."
                    "You dare not move a muscle."
                    "The chief’s hand forms into a fist and you see him trembling, the ramifications of his mind are unknown to you."
                    pause 4
                    "Then his hand falls."
                    e 0 "No!"
                    "The executioner pulls the lever and the trap doors open, dropping their bodies down."
                    "They kick and struggle, desperate to find a footing, anything to save them from the tightening of the noose."
                    "They kick, and kick, and kick until finally their bodies go limp."
                    pause 5
                    "The kicking stops, and all three are dead."
                    "The crowd cheers, some even cursing the lizards souls to damnation in the after life."
                    "Axel then addresses the crowd. "
                    show axel stand with slow_dissolve
                    a "It’s time for war!" with vpunch
                    a "I want all warriors on the training grounds now!"
                    a "Everyone else, raise the defenses!"
                    "With Axel’s command the crowd disperses."
                    hide axel stand with slow_dissolve
                    "You are left to stand alone watching the bodies sway upon the gallows."
                    e 13 "This is it... this is war."
            "Keep silence" if True:
                "Then his hand falls."
                "The executioner pulls the lever and the trap doors open, dropping their bodies down."
                "They kick and struggle, desperate to find a footing, anything to save them from the tightening of the noose."
                "They kick, and kick, and kick until finally their bodies go limp."
                pause 5
                "The kicking stops, and all three are dead."
                "The crowd cheers, some even cursing the lizards souls to damnation in the after life."
                "Axel then addresses the crowd. "
                show axel stand with slow_dissolve
                a "It’s time for war!" with vpunch
                a "I want all warriors on the training grounds now!"
                a "Everyone else, raise the defenses!"
                "With Axel’s command the crowd disperses."
                hide axel stand with slow_dissolve
                "You are left to stand alone watching the bodies sway upon the gallows."
                e 13 "This is it... this is war."
    jump Bull_tribe_map0



label Festival_ending_lizard:
    $ Quest.fes_result = Nauxus
    stop Chan1
    stop Chan2
    $ Nauxus.s = Nauxus.s - 2
    $ Quest.fesn = 6
    $ Quest.fes = 3
    $ Quest.fes_end = 1
    scene black with vslow_dissolve
    if Time.hours >= 6 and Time.hours <= 17:
        scene lizardtribe 1 with vslow_dissolve
    elif True:
        scene lizardtribe 1n with vslow_dissolve
    "You haul the sacks full of fruits all the way back to the swamp."
    "When you arrive in the lizard village, colourful strings line every roof and every lizard is out and about. "
    "Some kids are running around with plates while adult lizards go after them."
    "You walk over to the shopkeeper to unload your baggage."
    e 1 "Here you go."
    "The bags of fruits rest with a heavy thud on the shopkeeper’s desk."
    "Lizard Shopkeeper" "Oh my, I didn’t expect there to be so many intact."
    e 6 "Yeah we’re lucky."
    e 1 "There is just enough for the whole village."
    "Lizard Shopkeeper" "Yes this is perfect for tonight.I’ll have them prepped and ready for every family."
    "Lizard Shopkeeper" "Would you be so kind to deliver the news to Chief Nauxus that the festival can begin tonight."
    e 6 "I’ll be happy to."
    "Lizard Shopkeeper" "Thank you dearie."
    "You head off to meet Nauxus."
    if Time.hours >= 6 and Time.hours <= 17:
        scene meetingroom with vslow_dissolve
    elif True:
        scene meetingroom n with vslow_dissolve

    "In the council chamber Nauxus appears to be asleep on the throne."
    e 1 "Hmm."
    "You walk closer towards the slumbering lizard. His heavy pectorals rising and falling with every breath."
    "You stand close enough for both your toes to touch."
    "Bending over, your snout draws close to the side of his face."
    "You feel yourself grinning over him."
    "You turn your head to the side to ponder what you could do to wake him up or perhaps if you shouldn’t at all."
    "The possibilities are endless, maybe a kiss on the cheek, or maybe a shake of his broad shoulders, or if you want, you could surprise him with a loud yell."
    "You turn back only to face Nauxus looking at you with a playful smile."
    e 9 "Err... hi."
    n "A little tip, if you want to sneak up on someone you might want to wash the sweat out of your fur first."
    show nauxus stand at center with slow_dissolve
    "You step back and avoid looking Nauxus in the eyes."
    "Every fibre of your body tightens and locks making you feel like one large boulder."
    e 9 "I just wanted to... report that the fruits have been delivered."
    n "Good. Very good. Then here is your reward."
    "<[name] gained 400 coins>"
    "<[name] gained one Level-up-point.>"
    $ jane_inv.take(coin,400)
    $ Zalt.points = Zalt.points +1
    e 6 "Thank you, I... better go."
    n "Wait a minute, who says your reward ends there?"
    n "I also extend an invitation to you to attend the festival, and you get to be my guest beside me."
    e 1 "Wow..."
    n "Then you can be as close to me as you like."
    "You raise a finger to try to say something but you just blush and pull it back."
    e 7 "Ok."
    n "Here you’ll need this."
    "Nauxus pulls a piece of paper from his satchel."
    "It’s a list of lyrics."
    e 1 "What’s this for?"
    n "It’s part of the village’s tradition that a new song be written in honour of the festival and is sung by everyone of the tribe."
    e 6 "That’s great, but I don’t even know the melody."
    n "You can just sing along when the song starts. It's no big issue. "
    hide nauxus stand at center with slow_dissolve
    "Nauxus then summons a guard into the chambers and orders him to instruct the villagers to begin with the feast, he would come down later."
    "The guard leaves to carry out his orders."
    show nauxus stand at center with slow_dissolve
    n "I think that’s everything."
    n "Now I gotta get back to practising my speech for the big event."
    e 1 "Alright, guess I’ll see you then."
    "Nauxus yawns and nods. "
    hide nauxus stand at center with slow_dissolve
    if Time.hours >= 6 and Time.hours <= 17:
        scene lizardtribe 1 with vslow_dissolve
    elif True:
        scene lizardtribe 1n with vslow_dissolve
    "On your way down to your hu,t you see the lizards setting up two long tables on the walkway that joins the left and right side of the village. "
    "The lizard shopkeeper with the help of a few guards bring large bowls stacked with the fruits earlier and place them on the tables."
    "The children all watch with hungry eyes at the food."
    "You could practically feel the excitement in their faces."
    "You smile watching the children gather around the fruits. "
    "However the same can’t be said of the adults who watch on with a tired smile. "
    "For the children, they can still look at this year’s festival as a moment of celebration as they are shielded from the conflict of war."
    "Or perhaps they put on a brave face just so not to worry their parents."
    "You wonder which is true. "
    "Then your nose twitches as you catch a whiff of a strong sweaty smell. "
    "You raise your right hand and sniff it... it is you."
    e 9 "Huh, Nauxus was right. I do need a bath."
    "You head to the hut in the lizard village to clean yourself."
    scene black with slow_dissolve
    $ Time.days = Time.days+1
    $ Time.hours = 18
    $ Time.mins = 30
    pause 5
    play music "<loop 12.4405>music/lizard_party.ogg"
    scene lizardtribe 1n with slow_dissolve
    "Some time passes as you clean yourself in the hut."
    "When you leave you see all the lizard folk have come out of their homes."
    "Most of them sit by the edge of the walkway with their friends and families as they eat the fruits from earlier."
    "The table of fruits from before is now gone, in its place are a group of child lizards practising their song."
    "Amongst the crowd you spot an unamused Selye standing by the side alone."
    menu:
        "Take a closer listen to the children singing" if True:
            if Quest.campw1 != 3:
                "You decide to go listen to the children prepare."
                "The closest spot is taken by the lizard trio."
                "You stand beside them without drawing any attention to yourself."
                "Uno" "I am liking this new song but it doesn’t hold a candle against the one we sang when we were younger."
                "Duo" "Yeah our song had the catchiest of tunes."
                "Duo" "Remember how the crowd was screaming while we sang?"
                "Blep" "Blep was best singer."
                "Uno" "Oh Blep, we all were. I still remember the lyrics."
                "Uno starts singing a line from their old song."
                "The sheer shrillness of his voice makes your fur stand on end."
                "Goosebumps run up your spine making you want to grab hold of your ears to shut the noise out."
                "Then Duo joins in and sings along, then Blep."
                "The combined frequencies of their voices is too much to bear."
                "You feel your head reeling."
                "Looking around, the other lizards are leering at the trio as well. "
                "Yet the three are unaware of everyone else’s response, instead they are engrossed in their song."
                n "Ehem."
                "The trio stop their singing the moment their chief appears."
                show nauxus stand at center with slow_dissolve
                n "Boys, singing your old tune huh, I remember that year. "
                "The chief drapes his arms on the trio’s shoulders."
                "Duo" "Yeah chief, it was the best! Did you enjoy our song?"
                n "Ohh... it sounds... just like how you guys sang it that year."
                "Uno" "Yes!"
                hide nauxus stand at center with slow_dissolve
                "The trio high five each other and start complementing one another for a job well done."
                "Nauxus puts a hand to your shoulder and points to the empty spot next to the lizard children."
                n "Shall we?"
                e 5 "Oh yeah, lets."
                "As you walk away you whisper to Nauxus."
                e 8 "Thanks back there."
                n "Don’t mention it."
            elif True:
                "You stand by the side and listen to the children practice their song."
                "Seeing them work so hard with their song you pull out the lyrics sheet that Nauxus gave you."
                "You begin to mouth the lyrics to yourself."
                n "My, my aren’t we diligent."
                show nauxus stand at center with slow_dissolve
                "You turn around and see Nauxus approaching."
                e 5 "It’s just, I don’t want to mess up when the song starts."
                n "You’ll be fine. I usually don’t end up singing either."
                e 1 "What? Why?"
                n "I’m not confident with my singing voice."
                n "I may be a master artist, but singing is not my strong suit."
                e 6 "You can still humm it along at least."
                n "Maybe, seeing how enthusiastic you are about it does put me to shame that I’d be embarrassed by how I sing."
                e 1 "Are you saying I sing poorly as you?"
                hide nauxus stand at center with slow_dissolve
                n "Oh look we should start."
                e 5 "Nauxus, wait you haven’t answered me."
                e 5 "Nauxus!"
                "You don’t get your answer, instead you follow the chief to start the ceremony."
        "Talk to Selye" if True:


            "You head over to the lonely naga."
            e 1 "Hey Selye."
            show selye stand at center with slow_dissolve
            se "Ssssimpleton."
            e 5 "Come on man, how are you not in the spirit of the festival? Try a fruit at least."
            se "How I choose to enjoy this festival is none of your business."
            se "Honestly, I don’t see the point of this when we are in the middle of a coming war."
            e 1 "Geez, you make it sound like you’ve never liked festivals to begin with."
            se "That’s where you’re wrong ssssimpleton."
            se "I will relish the day the bull tribe falls, and we celebrate our victory."
            se "It will give me no greater honour than to receive a token of appreciation from Chief Nauxus."
            e 5 "Is that... is that why you’re trying to kiss his ass so hard?"
            "Selye slithers closer to you and pats you on the right cheek."
            se "Take it as you wish ssssimpleton. Now I believe you have some ass kissing of your own to do."
            e 5 "What?"
            n "My, my, aren’t you two close now."
            hide selye stand at center with slow_dissolve
            "You hear Nauxus’s voice coming from behind you."
            show nauxus stand at left with slow_dissolve
            show selye stand at right with slow_dissolve
            se "Chief Nauxus, happy festival to you my chief. "
            n "Aren’t you staying for the song Selye?"
            se "Not tonight I’m afraid, there’s an important sssspell in my hut that I must attend to."
            se "Good day chief."
            hide selye stand with slow_dissolve
            show nauxus stand at center with slow_dissolve
            "Selye leaves the both of you."
            e 1 "Nauxus."
            n "Yes?"
            e 13 "I don’t want to ruin the festival but..."
            n "But?"
            e 1 "I think selye is too mysterious to trust."
            n "Oh, and how do you know this?"
            "Nauxus shrugs."
            n "It’s no big surprise to me."
            n "If there’s anything my years as a chief has taught me is that everyone has a price for their services."
            n "As long as he plays his part I will have no qualms with what he wants."
            n "Now come, the main event is about to start."
            e 1 "Oh... ok."
            "You follow Nauxus to stand next to the lizard children."

    scene black with slow_dissolve
    stop music fadeout 5
    "The moment Nauxus stands in front of the entire village,a he commands their attention."
    scene lizardtribe 1n with slow_dissolve
    "With everyone silent Nauxus begins speaking."
    "You are surprised to hear him speak in a series of hisses."
    "It is a language you do not recognize but everyone else is listening intently."
    "When he finishes his speech the lizards all cheer in unison."
    play music "<loop 12.4405>music/lizard_party.ogg" fadein 10
    "The lizard children start singing their song."
    "You pull out the lyrics sheet and follow along."
    "The voices of the children singing vibrates throughout the village. "
    "Their melodic voices put your heart at ease."
    "After the first verse the rest of the village joins along."
    "The entire village erupts in song."
    "..."
    "..."
    scene black with slow_dissolve
    "As you sing a long you turn to Nauxus. "
    "He is humming along to the song."
    "He notices you staring and bashfully turns his face."
    "You smile with your eyes and continue singing closer to him."
    "Nauxus is drawn in by your singing and is drawn to your face."
    "..."
    "He starts humming alongside you as you sing."
    "Seconds pass into minutes and you both continue transfixed looking at each other."
    "You could look at the lizard’s bright eyes none stop."
    "At some point you forget you are singing and just hear Nauxus humming at you."
    "Were the others looking? You didn’t care. All that matters is this moment."
    stop music fadeout 5
    "..."
    scene lizardtribe 1n with slow_dissolve
    "Then the song ends."
    "The cheer of the village folk snaps you out of your trance."
    show nauxus stand at center with slow_dissolve
    n "That was some nice singing."
    e 6 "Thanks, you hummed well too."
    "Nauxus smiles. "
    "With the end of the song the crowd begins to disperse back into their homes."
    e 1 "I guess I should go."
    "Just as you turn to leave Nauxus grabs hold of your hand."
    n "Wait."
    e 1 "Yeah?"
    n "Umm."
    "The lizard chief turns his head away from you."
    n "The night is still young... and I was wondering... maybe... maybe you’d want to share a drink with me?"
    e 6 "Maybe next time. "
    pause 3
    "Nauxus turns back towards you with a frown."
    n "Oh ok."
    "You step forward and rub Nauxus on the cheek."
    e 3 "Thanks for letting me be part of the festival."
    "He smiles, and you walk back to your hut."
    scene black with vslow_dissolve
    pause 3
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
    jump Room4



label Lizard_defend:

    $ Quest.fesn = 7
    if Quest.fesn == 7 and Quest.fesa == 7:
        $ Quest.fes_end = 2
        "The tribe is a buzz with activity."
        "The moment you enter the tribe Nauxus’ advisors rush out of the room with a frantic look on their faces."
        e 1 "Nauxus."
        show nauxus stand at center with slow_dissolve
        n "[name], I’m afraid now isn’t the best time for a visit."
        e 1 "What’s wrong?"
        "Nauxus sighs."
        n "I got word of an attack at one of our camps stationed to observe the bull tribe."
        n "Their forces obliterated everything, and the lizards were lucky to escape with injuries."
        n "The bulls are out for blood far earlier than I anticipated."
        n "This is war I am afraid."
        n "You wouldn’t happen to know what could have caused this do you?"
        e 1 "Thane, was injured badly last night."
        e 13 "Axel suspects it was the lizard tribe that hurt him."
        e 1 "Did you or your men do it?"
        if Nauxus.s <=3:
            n "[name], look at me. I have nothing to do with what happened to Thane."
            n "And if there is a lizard here who values ​​their lives they would know better than to go behind my back and to put the entire village in jeopardy to wound one bull."
            e 13 "Ok, I believe you."
            n "Look I hate to do this, but I need some time to prepare for this war."
            n "We can discuss this whole Thane thing when there is more time."
            e 13 "I understand."
            n "I’ll summon you when I have something."
            hide nauxus stand at center with slow_dissolve
            "You nod and Nauxus leaves."
        elif True:
            "Nauxus’s face winces."
            n "To answer your question, no we were not involved."
            n "And how do I know you didn’t play a part in all of this?"
            e 5 "What?"
            n "Yes, what proof do you have that you didn't set all of this up just to push the two tribes into war faster to ensure the side you support wins?"
            n "Because it seems awfully convenient that the bulls are attacking when we aren't ready."
            e 12 "I have nothing to do with this."
            "You both stare each other down."
            n "That will be all then [name]. I’ll call for you when I need you."
            "Nauxus waves you away, cutting the conversation short."
            "Nauxus leaves."
            "You feel so frustrated."
        jump Lizard_tribe_map0
    elif True:
        "You hear the sound of footsteps and people shouting orders to each other to head out outside of your door."
        "The commotion forces you awake."
        show nauxus stand at left with slow_dissolve
        show selye stand at right with slow_dissolve
        hide nuaxus stand with slow_dissolve
        hide selye stand with slow_dissolve
        "You step through the door and see Nauxus, Selye and a lizard guard standing by the entrance."
        se "I don’t think the reinforcements will make it in time to ssssave the next camp."
        n "They have to, or else we’re all doomed."
        n "Guard, are you sure there is no new information on what led the bulls to start attacking our camps?"
        "Lizard Guard" "I’ve asked around. Nobody really knows, chief."
        n "This is dangerous. They are advancing ahead of what I predicted. We-"
        se "Chief."
        "Selye nudges his head towards you."
        "Nauxus turns and sees you at the door."
        show nauxus stand at left with slow_dissolve
        show selye stand at right with slow_dissolve
        n "Oh, [name]. "
        e 1 "What’s going on?"
        n "Last night the bulls launched an attack on one of our surveillance camps."
        n "The lizards posted there barely escaped with their lives."
        n "We fear that the bulls will continue marching from camp to camp until they get to the village."
        n "You best stay away from that village, Chief Axel has become a desperate bull to desecrate his village’s festival with a war."
        n "Now if you’ll excuse me I need to start preparing."
        n "I will call for you, you don’t need to find me."
        e 5 "Ok..."
        hide nuaxus stand with slow_dissolve
        hide selye stand with slow_dissolve
        "Nauxus signals to the other two and they leave in the direction of the council chamber."
        e 5 "Axel started attacking? "
        e 5 "Does Thane know about this? "
        if Thane.movein == 2:
            scene black with vslow_dissolve
            pause 3
            play sound "music/door.mp3"
            play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
            scene tavern 1 with slow_dissolve
            "When you enter the tavern you see Snow talking to two bulls dressed in white robes."
            "Snow points to the stairs and the two bulls head up the stairs."
            e 1 "What’s going on?"
            "You walk over to Snow."
            show snow stand with slow_dissolve
            s "Those are bull healers. They’re here to watch over Thane for the time being."
            e 5 "Thane? What happened?"
            s "It happened last night, where were you anyways?"
            e 1 "I was in the lizard village, they had a big festival."
            s "Huh, well while you were off having fun."
            s "Thane came back dripping in blood. "
            s "He kept muttering your name and a strange message before he lost consciousness."
            e 1 "What did he say?"
            s "He said Lizard.Was.Lie."
            e 5 "..."
            e 5 "What does that even mean?"
            show snow happy1 with slow_dissolve
            s "I wouldn’t know. After he said that he fainted and hasn’t woken up. "
            c "Then where did those bulls come from?"
            s "I’ll let Hakan share that."
            s "He was the one who came back with them. Hakan!"
            show snow stand at left with slow_dissolve
            show hakan stand at right with slow_dissolve
            "The red dragon walks over to the bar."
            s "Tell our friend here what happened when you went to the bull tribe."
            h "Well let’s see."
            h "I came into the village, they were all dancing and I demanded to see the chief."
            h "He did not take the news well."
            h "He wanted to have the entire village storm the tavern."
            h "But I reminded him Thane needed help and that he would be drawing more attention than needed."
            h "But... the look in his eyes."
            h "I’ve seen people with that look, the look of a man at the mercy of his emotions."
            h "They do drastic things, people like that."
            e 13 "I should check upon him."
            h "You can try but I don't think he is in the mood for company."
            jump map1
        elif True:
            jump Lizard_tribe_map0



label battle_katos_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    hide katos with slow_dissolve
    "Your body fails to keep up with the movements of the beast."
    "Exhaustion takes you first before it’s replaced with pain as you feel a set of claws digging into your flesh."
    "An overbearing weight causes your already bruised body to collapse."
    "The beast then wraps it’s maw around your neck before clamping down."
    "Try as you might to scream, your feeble efforts amount to nothing as the pressure of the beast’s bite ruptures your vocal cords,quickly filling your mouth with a mixture of blood and saliva."
    play sound "music/blood.ogg"
    "Without wasting time, the beast continues to feast on your flesh in earnest, happy to finally indulge in a meal that’s worth more than any stolen fruit."
    "The last thing you register is the brief pain that comes from the beast as it moves its mouth from your neck to your head."
    play sound "music/blood.ogg"
    show red2 at center with slow_dissolve
    "Then darkness takes you."
    scene black with vslow_dissolve
    "{b}{color=#c22719}<GAME OVER>{/color}"
    menu:
        "New game" if True:
            return
    stop music
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
