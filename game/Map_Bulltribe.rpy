label Bull_tribe_map0:
    stop music
    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(1, 5, channel = "Chan1")
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(1, 5, channel = "Chan2")
    play Chan1[ "<silence 0.5>", "music/bulls_village.ogg" ]fadein 3
    play Chan2[ "<silence 0.5>", "music/bird1n.ogg" ]fadein 3
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    play Thane "music/thane.ogg"
    play Axel "music/axel.ogg"
    jump Bull_tribe_map


label Bull_tribe_map:
    $ Time.mins = Time.mins +10
    window hide None
    pause 0.5
    $ renpy.music.set_pause(True, channel='Thane')
    $ renpy.music.set_pause(True, channel='Axel')

    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(1, 5, channel = "Chan1")
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_pause(False, channel='Chan1')
        $ renpy.music.set_pause(True, channel='Chan2')
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(1, 5, channel = "Chan2")
        $ renpy.music.set_pause(True, channel='Chan1')
        $ renpy.music.set_pause(False, channel='Chan2')


    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Thane.quest == 7 and Quest.campb == 0 and Quest.campl == 0:
        $ Quest.campb = 1
        $ Quest.campl = 1
    if Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bomb_bull ==2 and Quest.bomb_result != Axel:
        jump Axel_letter
    if Thane.quest == 2:
        $ Thane.meet = 3
        scene black
        stop music fadeout 1
        $ Map.bulltribe = 1
        "Thane leads the way into the bull tribe."
        if Time.hours >= 6 and Time.hours <= 17:
            scene tribe 1 with vslow_dissolve
        elif True:
            scene tribe 1n with vslow_dissolve
        "The two guards at the front stand aside and and lower their heads in his presence."
        show thane stand1 at center with dissolve
        t "This one is under my protection."
        t "Until the Chief says otherwise he will be granted passage into the tribe."
        "He points to one of the bull guards."
        t "Tell the rest of the tribe, and Chief Axel."
        "Bull A" "Right away brother Thane."
        hide thane stand1 with dissolve
        "The guard runs off into the village and you see him pass the message to anyone nearby."
        show thane stand at center with dissolve
        "Thane turns to you."
        t "The Chief is up there."
        "He points at the large tent in the middle of the mountain."
        "Thane walks off not giving you a chance to say anything so you follow him from behind."
        hide thane stand with dissolve
        if Time.hours >= 6 and Time.hours <= 17:
            scene bulltribe 1 with vslow_dissolve
        elif True:
            scene bulltribe 1n with vslow_dissolve
        "A crowd forms along your way to the stone steps."
        "They all give you a look like they are contemplating whether to throw their axes at you."
        "You notice that there are very few children around."
        "You catch a glimpse of two boy calves playing with bows and branches."
        "You try to wave at them but a larger adult bull steps in front blocking them from view."
        "He has his arms crossed as he gives you a scornful glare."
        "Thane isn’t much help either."
        "His face looks tense since you two start walking through the village."
        "You both climb the stairs until you reach the entrance to the Chief’s tent."
        e 1 "Are you ok?"
        t "Huh? Yeah, yeah."
        t "Just, don’t say anything for now."
        "Thane breathes and approach the tent."
        "You follow suit."
        if Time.hours >= 6 and Time.hours <= 17:
            scene tent 1 with vslow_dissolve
        elif True:
            scene tent 1n with vslow_dissolve
        "???" "THANE!"
        "The booming voice makes you shudder."
        "An intimidating figure stands in front of you both."
        show thane stand1 at left with dissolve
        show axel stand at right with dissolve
        "You have the immediate urge to get on one leg and avert your gaze from him."
        "But you stay rooted in your place. "
        "He looks like a giant even next to Thane."
        "Judging from his protruding gut he’s a heavy eater."
        "But he radiates strength and authority through his powerful arms."
        "That look like they can encompass your entire head."
        t "Father."
        a "What is this I hear about an outsider granted entry into our village?"
        t "This is [name]."
        e 9 "Chief."
        "Your tail hides between your legs as you look up to Thane's father."
        a "Hmph!"
        a "You really think this measly bag of bones has the right to be here?"
        t "[name] is a strong warrior."
        t "He saved my life, that's why he is more than worthy of being welcomed here."
        a "He’s only of use to us if he has the balls to kill a lizard on sight."
        a "Until then he be better off as a punching dummy."
        t "Then let him prove his place here."
        t "I vouch for him, and he has the right to be tested by you to earn his place."
        t "He can help us."
        a "Our tribe is doing perfectly fine without the interference of an outsider for many years."
        a " We don’t need his help."
        a "And he should be grateful that I'm even letting him{p}stand near my tent with his head still on his shoulders."
        t "Are you blind old man?"
        t "We’re losing good people fighting the lizards, we need a different way!"
        a "Watch your tone Thane."
        a "You’re speaking to the chief first and your father second."
        t "...Forgive me, I spoke out of place."
        "The chief glares at his son who refuses to look at him directly before his eyes fall on you."
        "You feel his heavy gaze studying you from top to bottom while he gives you a look of discontent."
        a "So Thane thinks you are worthy of our tribe’s trust."
        a "Very well, as traditions must be uphold I will give you your test wolf."
        a "There’s a lizard spy darting about our village and hiding in the woods nearby."
        a "My men managed to scrape this off of the spy while he tried to escape last night. "
        "The chief pulls out a piece of brown cloth that looks like it was torn ferociously from something larger."
        a "Take this, find the spy, and bring me his heart."
        t "No! You can’t."
        a "Silence!"
        a "One more outburst from you and I will have this stranger and your horns banished!"
        t "..."
        a "I’m sure you wouldn’t have any troubles with your canine sense of smell."
        "You gulp."
        t "No, there’s never been a test that involved killing someone before."
        t "Leave him out of this."
        a "Quiet!"
        a "You’re always going on and on about change, well here it is son."
        a "Now let the wolf decide."
        e 9 "I..."
        a "Remember this, the lizards have been a thorn in our side since the fog came."
        a "Their kind have lost themselves and are guilty of kidnapping and murdering our children!"
        a "So imagine what would happen if word got out that the tavern folk are soft for these child killers."
        "The chief cracks his knuckles and stares down at you."
        e 13 "I... I will do it."
        "Thane hangs his head low in shame upon hearing your answer."
        a "Good, I look forward to hear your news."
        hide thane stand1 with dissolve
        hide axel stand with dissolve
        t "[name] lets go."

        if Time.hours >= 6 and Time.hours <= 17:
            scene tribe 1 with vslow_dissolve
        elif True:
            scene tribe 1n with vslow_dissolve
        "You both step out of the tent and walk down the stairs in silence. Halfway down Thane turns to you."
        show thane stand at center with dissolve
        t "I’m sorry, about my father."
        t "He ... he doesn’t usually like meeting outsiders."
        t "I... I shouldn’t have gotten you involved."
        e 1 "No, I was the one who agreed to it."
        e 1 "I’ll figure a way to deal with it."
        t "I’m sorry."
        hide thane stand with dissolve
        "You see pain in Thane’s eyes as you make your way down the rest of the stairs."
        "He watches you walk out the village from where he stands."
        $ Thane.quest = 3
        $ Map.bullforest = 1
        jump forest_map0
    elif Thane.quest == 4:
        if Time.hours >= 6 and Time.hours <= 17:
            scene bulltribe 1
        elif True:
            scene bulltribe 1n

        if Time.hours >= 6 and Time.hours <= 17:
            scene tent 1 with vslow_dissolve
        elif True:
            scene tent 1n with vslow_dissolve

        "You return to the chief’s tent to find Thane standing next to the chief."
        show thane stand1 at left with dissolve
        show axel stand at right with dissolve
        a "Hahahaha, you actually made it back wolf."
        a "I was honestly expecting that I would need to send a search party to bring back your corpse."
        "Thane glares at his father."
        a "Now tell me what has happened to our lizard problem?"
        if Foe.spydie == 1:
            $ jane_inv_K.drop(Lizard_heart)
            "You pull out from your satchel the lizard’s heart."
            "Thane grimaces at the sight of the organ."
            a "Huh, you maybe more useful than you look."
            a "I hope he was alive long enough to see you rip the heart out of his chest."
            t "Enough of this, the spy is dead."
            t "The least we can do is not make a spectacle of his death."
            t "The deed is done, are we done here?"
            a "For now, [name], I Chief Axel declare you an ally of the bull tribe."
            "You may come and go as you please, but you will pledge your services to me as well."
            a "I’ll call for you in due time. For now, you can have this."
            "<[name] gained 150 coins and 500 EXP>"
            $ Zalt.exp = min(Zalt.exp+500, Zalt.maxlv*250+100*(Zalt.maxlv-1))
            $ jane_inv.take(coin,150)
            a "As for you Thane."
            a "Don’t think you’re off the hook just because you brought in a competent warrior."
            a "His mere presence goes in defiance of my instructions that no outsiders be permitted into the village."
            a "Your punishment is to meditate on the temple grounds for a full day."
            t "Gladly! [name], lets go."
            hide thane stand1 with dissolve
            hide axel stand with dissolve
            if Time.hours >= 6 and Time.hours <= 17:
                scene bulltribe 1 with dissolve
            elif True:
                scene bulltribe 1n with dissolve
            "You place the heart back inside your satchel and follow Thane leave the tent."
            "He walks briskly without saying a word."
            e 1 "Thane where are we going?"
            t "..."
            play sound "music/foot1.ogg"
            stop music fadeout 1
            if Time.hours >= 6 and Time.hours <= 17:
                scene bulltree 1 with vslow_dissolve
            elif True:
                scene bulltree 1n with vslow_dissolve
            "He leads you until you into the forest just outside of the village."
            "You both stop in front of a plain tree."
            t "Take the heart out."
            "Thane gets on one knee and digs a hole with his bare hands."
            "He pulls away mounds of dirt in one go until he makes a small hole deep enough to bury a small box."
            "You understand what he intends to do and give the young bull the heart. "
            "He cradles the organ in both his palms and whispers something softly to it."
            "You watch in silence from behind him as he conducts the ceremony."
            "Thane falls silent for a second and places the heart into the soil before burying it."
            t "..."
            "He turns towards you."
            show thane stand at center with dissolve
            t "Congrats on making it into the tribe."
            e 13 "Thanks..."
            "Thane glances at the spot he buried the heart."
            t "Look it’s been a long day."
            t "Why don’t I show you to your place and I’ll let you get some rest."
            e 1 "Ok."
            hide thane stand with dissolve
            scene black with dissolve
            "The two of you walk back into the village."
            "He brings you to a hut tucked away from the others but is high enough that you can see most of the bull village."
            if Time.hours >= 6 and Time.hours <= 17:
                scene bulltribe 1 with vslow_dissolve
            elif True:
                scene bulltribe 1n with vslow_dissolve
            t "You can stay here whenever you’re in the village."
            "He opens the hut with a key."
            play sound "music/door.mp3"
            if Time.hours >= 6 and Time.hours <= 17:
                scene room 3 with vslow_dissolve
            elif True:
                scene room 3n with vslow_dissolve
            "Inside, a powerful stench hits your nostrils."
            "The room reeks of bull and dirt."
            "There’s very little space inside too."
            "You wonder if this used to be some kind of a storage hut they hastily cleaned for you."
            "The bed looks so beaten in you worry if it will hold your weight."
            show thane stand at center with dissolve
            t "I’m sorry I can’t give you better accommodations."
            t "Your arrival and success with gaining entrance to the tribe was a surprise to the tribe."
            t "So no one had enough time to build a new hut for you."
            e 6 "It’s ok, I’ll make do."
            "Thane smiles and leaves your new hut."
            t "Now if you’ll excuse me I must make preparations to head to the temple."
            e 1 "No wait."
            t "Yes?"
            e 1 "Can I come with you?"
            t "What?"
            e 1 "Can I come with you to the temple?"
            e 13 "I’m technically the reason you even need to be punished."
            e 1 "It’s only fair I face it with you."
            t "You don’t have to. It’s a really annoying trip up to the mountain top."
            "He points towards the mountain."
            e 1 "I insist, plus if I’m going to be an ally of the tribe best I get to know the place."
            t "..."
            "He scratches the back of his head and looks towards the training dummies lost in thought."
            t "Fine, you can come, get yourself freshen up and I’ll wait for you near the chief’s tent."
            "You nod in agreement. Thane then walks off towards another hut."
            "Looks like you need to climb a mountain."
            "You wonder if you have enough supplies for the trip."
            "Or maybe you should rest for a while before you meet Thane."
            $ Thane.quest = 5
            $ renpy.music.set_pause(True, channel='Chan1')
            $ renpy.music.set_pause(True, channel='Chan2')
            jump Room3
        elif True:
            $ jane_inv_K.drop(Lizard_dagger)
            $ Thane.help = Thane.help +1
            "You pull out the spy’s short blade from your satchel."
            a "This is no heart."
            e 1 "It’s the lizard’s weapon."
            e 13 "That’s all I could save from our fight."
            e 1 "I cornered him near a cliff and managed to stab him in the heart with his own weapon."
            e 1 "but he tumbled back and fell."
            a "A very convenient string of events."
            a "But now how would anyone know that the spy is dead."
            t "What does it matter?"
            t "I trust [name], and even if the lizard is out there he is defenseless."
            t "It would be suicide of him to try to come back here."
            t "He’s gone, we’re done here."
            hide thane stand1 with dissolve
            hide axel stand with dissolve
            "The chief calls you closer with a flick of his finger."
            "He grabs the blade and examines it intently."
            "Even smelling the dried blood on it."
            show thane stand1 at left with dissolve
            show axel stand at right with dissolve
            a "I am not satisfied wolf."
            a "But since I’m in a good mood today, I will let you pass ..."
            a "But you will have to work your ass off before I trust you."
            a "For now, you may enter and leave the village freely, but I’m watching you."
            a "Thane! Don’t think you’re off the hook just yet."
            a "You dare disobey your chief’s orders by bringing in an outsider into the village despite my clear instructions."
            a "Meditate on your actions in the temple grounds for one day."
            t "Gladly! [name], lets go."
            hide thane stand1 with dissolve
            hide axel stand with dissolve
            if Time.hours >= 6 and Time.hours <= 17:
                scene bulltribe 1 with vslow_dissolve
            elif True:
                scene bulltribe 1n with vslow_dissolve
            "You follow Thane leave the tent."
            t "Ugh! What an infuriating day, did you really kill the lizard?"
            e 9 "I-"
            t "No! Don’t tell me. I don’t want to know."
            t "My head’s a mess."
            t "Just let me take you to your hut for now."
            t "We’ll talk about this later."
            e 1 "Ok."
            "He brings you to a hut tucked away from the others but is high enough that you can see most of the bull village."
            if Time.hours >= 6 and Time.hours <= 17:
                scene bulltribe 1 with vslow_dissolve
            elif True:
                scene bulltribe 1n with vslow_dissolve
            t "You can stay here whenever you’re in the village."
            "He opens the hut with a key."
            play sound "music/door.mp3"
            if Time.hours >= 6 and Time.hours <= 17:
                scene room 3 with vslow_dissolve
            elif True:
                scene room 3n with vslow_dissolve
            "Inside, a powerful stench hits your nostrils."
            "The room reeks of bull and dirt."
            "There’s very little space inside too."
            "You wonder if this used to be some kind of a storage hut they hastily cleaned for you."
            "The bed looks so beaten in you worry if it will hold your weight."
            show thane stand at center with dissolve
            t "I’m sorry I can’t give you better accommodations."
            t "Your arrival and success with gaining entrance to the tribe was a surprise to the tribe."
            t "So no one had enough time to build a new hut for you."
            e 6 "It’s ok, I’ll make do."
            "Thane smiles and leaves your new hut."
            t "Now if you’ll excuse me I must make preparations to head to the temple."
            e 1 "Wait."
            t "Yes?"
            e 1 "Can I come with you?"
            t "What?"
            e 1 "Can I come with you to the temple?"
            e 13 "I’m technically the reason you even need to be punished."
            e 1 "It’s only fair I face it with you."
            t "You don’t have to. It’s a really annoying trip up to the mountain top."
            "He points towards the mountain."
            e 1 "I insist, plus if I’m going to be a friend to the tribe best I get to know the place."
            t "..."
            "He scratches the back of his head and looks towards the training dummies lost in thought."
            t "Fine, you can come, get yourself freshen up and I’ll wait for you near the chief’s tent."
            "You nod in agreement. Thane then walks off towards another hut."
            "Looks like you need to climb a mountain."
            "You wonder if you have enough supplies for the trip."
            "Or maybe you should rest for a while before you meet Thane."
            $ renpy.music.set_pause(True, channel='Chan1')
            $ renpy.music.set_pause(True, channel='Chan2')
            $ Thane.quest = 5
            $ Axel.s = Axel.s + 2
            jump Room3
    elif True:
        pass
    if Time.hours >= 6 and Time.hours <= 17:
        scene bulltribe 1 with dissolve
    elif True:
        scene bulltribe 1n with dissolve
    $ Thane.meet = 3

    if Time.bull == 9999 and Thane.quest == 7:
        $ Time.bull = Time.days
    if Time.lizard == 9999 and Thane.quest == 7:
        $ Time.lizard = Time.days

    if Thane.quest == 7 and Quest.campl < 3 and Quest.campb == 1 and Time.days >= Time.bull+1 and Selye.meet != 0 and Time.hours >= 6 and Time.hours <= 17:
        if Time.hours >= 6 and Time.hours <= 17:
            "When you walk into the village,A bull warrior calls out to you."
            "Bull warrior" "Hey, outsider."
            e 1 "Yup, that’s me."
            "Bull warrior" "Follow me, the chief called for you."
            "With no right to refuse, you follow the bull warrior to the tent."
            jump Bull_tribe_tent
    if Quest.camp_a == 2 and Time.bullkid == 9999:
        $ Time.bullkid = Time.days
    if Quest.camp_a == 2 and Time.days >= Time.bullkid+1 and Axel.bullkid == 0 and Time.hours >= 6 and Time.hours <= 17:
        "When you walk into the village,A bull warrior calls out to you."
        "Bull warrior" "Hey Brother Fleabag."
        e 5 "What did you call me?"
        "Bull warrior" "Brother Fleabag, that’s what the chief said to call you from now on."
        e 8 "Erk, never mind. What is it?"
        "Bull warrior" "The chief wants you in his tent now."
        e 1 "I’m coming."
        "You jog towards Chief Axel’s tent."
        $ Axel.bullkid = 1
        jump Axel_bullkid

    if Time.days >= Time.festival_day +2 and Quest.fes_end == 0 and Quest.fesa ==0 and Thane.movein != 1:
        if Quest.fes == 0:
            $ Quest.fes = 1
        $ Quest.fesa =1

        "The atmosphere in the bull village is different today."
        "You see bulls young and old heading to and from the shoopkeeper’s store."
        "Some of them carry decorations like flags and jars filled with juices."
        "You walk over and tap the shoulder of a bull warrior putting sun stones into jars."
        e 1 "Excuse me, what’s going on?"
        "The bull turns his head to the side to address you."
        "Bull Warrior" "Festival preparation."
        e 1 "I think I remember this, the Feast of Fire right?"
        "The bull grunts affirmatively."
        "Bull Warrior" "If you want to help, go talk to the chief."
        "Bull Warrior" "He might have some work to dull out."
        e 1 "Ok, I’ll think about it."

    if Quest.fes == 3 and Quest.fesa < 7:
        jump Bull_hanging
    call screen bull_outdoor with dissolve
    window show None
    show screen days
    if _return == 'exit':
        jump forest_map0
        return
    if _return == 'bull_room':
        play sound "music/door.mp3"
        jump Room3
    if _return == 'Axel_tent':
        if Time.aaxel == Time.days:
            "You should stay away from Axel for now."
            "He's still tossing things in his tent."
            jump Bull_tribe_map
        elif True:
            if Time.hours >= 6 and Time.hours <= 17:
                if Quest.fesa == 7:
                    "You shouldn't bother Axel."
                    jump Bull_tribe_map
                if Quest.campl >= 3 and Quest.campl < 6:
                    "Bull guard" "Chief Axel does not wish to be disturbed, please come back later."
                elif Quest.bomb_end == 1 and Quest.bombt == 2:
                    e 1 "I should go to get the materials for the glue from Snow fist. "
                    jump Bull_tribe_map
                elif Quest.bombt == 4 and Quest.bomba == 4:
                    e 1 "Nauxus told me to meet Selye, I should go to see him first."
                    jump Bull_tribe_map
                elif Quest.bombn == 3 and Quest.bomb_end == 1:
                    e 13 "I already choose my route, I think I should go to see Nauxus."
                    jump Bull_tribe_map
                elif Quest.bombn == 1 and Quest.bomba == 2:
                    e 13 "I think I should go to see what Nauxus want."
                    jump Bull_tribe_map
                elif True:
                    if Quest.campb >= 2 or Quest.campl >= 6:
                        jump Bull_tribe_tent
                    elif True:
                        "Bull guard" "The chief has no time to see you now, outsider."
                        "Bull guard" "Now move."
            elif True:

                if Thane.movein != 2 or Quest.fes_end != -1:
                    "Angry noises are coming out of the tent."
                    "It sounds like Thane and Axel are arguing."
                    "It's better not to enter the tent now."
                elif True:
                    "You shouldn't bother Axel."

            jump Bull_tribe_map
        return
    if _return == 'bull_shop':
        if NPC.bullshop == 0:
            "Shopkeeper" "Hey, I’ve never seen you around here before. You that new guy they call [name]?"
            e 1 "That I am, word travels fast."
            "Shopkeeper" "Well ain’t every day they lift the ban on outsiders coming in the tribe."
            "Shopkeeper" "A stupid law if you ask me. Basically putting me out of business."
            "Shopkeeper" "Well whatever, you ain’t here for the chatter."
            $ NPC.bullshop = 1
        if Quest.fesa == 3:
            $ Quest.fesa = 4
            e 1 "Shopkeep."
            "Shopkeeper" "Ya? Waddaya want Fleabag?"
            e 6 "Chief Axel sent me to deal with the missing fruits situation."
            "Shopkeeper" "Did he now?"
            e 1 "He says you can provide me with a sack or two to carry the fruits?"
            "Shopkeeper" "Well that I can do."
            "The shopkeeper rummages through his supplies and tosses you two large empty sacks."
            "Shopkeeper" "Once you get the fruits, bring’em to me. Anything else?"
            e 1 "Yeah, you wouldn’t happen to have a weapon that can instantly kill whatever took the fruits, perhaps?"
            "Shopkeeper" "You must be referring to one of the weapons I forge."
            "Shopkeeper" "Too bad kid, the chief didn’t clear you to have access to them yet. "
            e 13 "Typical. So where is this storage place anyways?"
            "The bull shopkeeper gives you a series of directions to where the fruits were kept."
            "With the directions in mind, you take the sacks and leave."
            scene black with dissolve
            "The moment you reach the storage hut you are taken aback by the destroyed state of the hut. "
            "The door itself remains untouched but in the back there is a gaping hole big enough for you and a bull to step through."
            "From the back, a trail of half eaten and stepped on fruits leads straight through the wall that splits the tribe from the forest."
            "You decide to follow the trail."
            $ jane_inv_K.take(sack,2)
            jump forest_map0
        "Shopkeeper" "Waddya want?"
        menu:
            "Oat flour-30 coins" if True:
                "Shopkeeper" "How many would you like?"
                menu:
                    "1" if True:
                        $ buy = 1
                    "3" if True:
                        $ buy = 3
                    "5" if True:
                        $ buy = 5
                    "Leave" if True:
                        jump Bull_tribe_map
                if jane_inv.qty(coin) >=30*buy:
                    $ jane_inv.drop(coin,30*buy)
                    $ jane_inv_M.take(oat_flour,buy)
                    "You get [buy] oat flour."
                    jump Bull_tribe_map
                elif True:
                    e 6 "(Nah,I don't have the money.)"
                    jump Bull_tribe_map
            "Rope-60 coins" if True:


                "Shopkeeper" "How many would you like?"
                menu:
                    "1" if True:
                        $ buy = 1
                    "3" if True:
                        $ buy = 3
                    "5" if True:
                        $ buy = 5
                    "Leave" if True:
                        jump Bull_tribe_map
                if jane_inv.qty(coin) >=60*buy:
                    $ jane_inv.drop(coin,60*buy)
                    $ jane_inv_M.take(rope,buy)
                    "You get [buy] rope."
                    jump Bull_tribe_map
                elif True:
                    e 6 "(Nah,I don't have the money.)"
                    jump Bull_tribe_map
            "Torch-80 coins" if True:

                "Shopkeeper" "How many would you like?"
                menu:
                    "1" if True:
                        $ buy = 1
                    "3" if True:
                        $ buy = 3
                    "5" if True:
                        $ buy = 5
                    "Leave" if True:
                        jump Bull_tribe_map
                if jane_inv.qty(coin) >=80*buy:
                    $ jane_inv.drop(coin,80*buy)
                    $ jane_inv_M.take(torch,buy)
                    "You get [buy] torch."
                    jump Bull_tribe_map
                elif True:
                    e 6 "(Nah,I don't have the money.)"
                    jump Bull_tribe_map
            "Ask about the permit" if Map.m6 == 2 and jane_inv_K.qty(mining_permit) == None:
                e 1 " I want to get a permit to go mining in the mountains."
                "Shopkeeper" "Well do ya now?"
                "Shopkeeper" "I don’t usually give out those things so easily on account that them bulls around here are careless with the way they swing their pickaxes."
                "Shopkeeper" "You have no idea how many of them came back with useless broken ores. Can’t even use them."
                "Shopkeeper" "But for you- I’ll make an exception because you’re just so darn cute."
                "Shopkeeper" "You can have your permit and I’ll throw in a pickaxe too just for the low price of 500 coins."
                e 5 "That’s extortion."
                "Shopkeeper" "Well I ain’t forcing ya to buy it. Take it or leave it."
                menu:
                    "Buy" if True:
                        if jane_inv.qty(coin) >=500:
                            $ jane_inv.drop(coin,500)
                            $ jane_inv_K.take(mining_permit)
                            $ jane_inv_K.take(pickaxe)
                            "You get a pickaxe."
                            jump Bull_tribe_map
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump Bull_tribe_map
                    "Not now" if True:
                        jump Bull_tribe_map
            "Ball of thread" if Witer.squat == 3 and jane_inv_K.qty(bullthread) == None:
                e 1 "You have any thread?"
                "Shopkeeper" "Thread? Don’t get that many requests for that."
                "Shopkeeper" "But yeah I can whip a ball of it for you."
                "Shopkeeper" "Only, 350 coins."
                e 9 "That price is daylight robbery! What the heck?"
                "Shopkeeper" "Well it ain’t cheap to make thread out of bull fur."
                "Shopkeeper" "Someone’s going to be walking around with a bald patch for a few weeks."
                "Shopkeeper" "So you want it or what?"
                menu:
                    "Buy" if True:
                        if jane_inv.qty(coin) >=350:
                            e 13 "Fine, I’ll take it."
                            $ jane_inv.drop(coin,350)
                            $ jane_inv_K.take(bullthread)
                            "You get a ball of thread."
                            jump Bull_tribe_map
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump Bull_tribe_map
                    "Not now" if True:
                        jump Bull_tribe_map
            "Leave" if True:
                jump Bull_tribe_map
        jump Bull_tribe_map
        return
    if _return == 'Chibi_bullf1':
        if Quest.campb == 6 or Quest.campt == 6 or Quest.campl ==6:
            "Female bull" "I better stock up on supplies until this war is over."
        elif True:
            "Female bull" "There’s a new outsider in the village, haven’t seen one in a long time."
        jump Bull_tribe_map
        return
    if _return == 'Chibi_bullf2':
        if Quest.campb == 6 or Quest.campt == 6 or Quest.campl ==6:
            "Female bull" "I curse!"
            "Female bull" "I curse the kidnapper and all its ancestors for what it’s done to our children."
        elif True:
            "Female bull" "My baby... when will you come home?"
        jump Bull_tribe_map
        return
    if _return == 'Chibi_bullm1':
        if Quest.campb == 6 or Quest.campt == 6 or Quest.campl ==6:
            $ Random = renpy.random.randint(1, 2)
            if Random <= 1:
                "Bull warrior" "A war! Finally I can show off my skills."
            elif True:
                "Bull warrior" "Don’t you go making trouble for Chief Axel, outsider."
        elif True:
            "Bull warrior" "The chief’s been fuming mad since Thane got back, wonder what that’s about? "
        jump Bull_tribe_map
        return
    if _return == 'Thane_talk':
        jump Thane_tribe_talk
        return
    if _return == 'Climb_mountain':
        stop Chan1
        stop Chan2
        play music [ "<silence 1.0>", "music/bulls_mountain_path.ogg" ] fadein 1
        jump Mountain_map
        return
    if _return == 'Bull_lick':
        jump bull_lick
        return
    return
screen bull_outdoor:
    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'bulltribe ground'
            hover 'bulltribe hover'
        else:
            idle 'bulltribe groundn'
            hover 'bulltribe hovern'

        if Time.hours >= 6 and Time.hours <= 17:
            hotspot (1682, 514, 127, 202) action Return("bull_shop")
        hotspot (170, 70, 304, 219) action Return("bull_room")

        hotspot (1150, 0, 485, 258) action Return("Axel_tent")


        hotspot (123, 932, 153, 141) action Return("exit")
        vbox:
            xalign 0.5 ypos 0.74
            if Time.hours >= 6 and Time.hours <= 17:
                imagebutton:
                    idle "NPC/bullfemale_1 ground.png"
                    hover "NPC/bullfemale_1 hover.png"

                    action Return("Chibi_bullf1")
            else:
                pass

        vbox:
            xalign 0.03 ypos 0.615
            if Time.hours >= 6 and Time.hours <= 17:
                imagebutton:
                    idle "NPC/bullfemale_2 ground.png"
                    hover "NPC/bullfemale_2 hover.png"

                    action Return("Chibi_bullf2")
            else:
                pass

        vbox:
            xalign 0.55 ypos 0.105
            if Time.hours >= 6 and Time.hours <= 17:
                imagebutton:
                    idle "NPC/bullmale_1 ground.png"
                    hover "NPC/bullmale_1 hover.png"

                    action Return("Chibi_bullm1")
            else:
                pass
        vbox:
            xalign 0.155 ypos 0.32
            if Time.hours >= 6 and Time.hours <= 17:
                imagebutton:
                    idle "NPC/bullmale_2 ground.png"
                    hover "NPC/bullmale_2 ground.png"
            else:
                pass
        vbox:
            xalign 0.67 ypos 0.11
            if Time.hours >= 6 and Time.hours <= 17:
                imagebutton:
                    idle "NPC/bullmale_3 ground.png"
                    hover "NPC/bullmale_3 ground.png"

            else:
                pass
        vbox:
            xalign 0.48 ypos 0.07
            if Thane.movein != 2:
                if Time.hours >= 6 and Time.hours <= 17 and Thane.quest >= 5 and Thane.quest != 6:
                    if Quest.campl >= 1 and Quest.campl <= 2 and Quest.campb >= 1 and Quest.campb <= 2:
                        if Quest.campl == 1 and Quest.campb == 1:
                            if Quest.fes <1 and Quest.fesa == 0 and Quest.fesn == 0:
                                imagebutton:
                                    idle "NPC/thane01.png"
                                    hover "NPC/thane02.png"

                                    action Return("Thane_talk")
                            else:
                                pass
                    elif Quest.campl == 3 and Quest.campt == 1:
                        pass
                    elif Quest.bombt == 4 and Quest.bomba == 4:
                        pass
                    elif Quest.bomb_end == 1 and (Quest.bombn >= 3 or Quest.bomb >= 3 or Quest.bomba >= 3) and Quest.bombt < 2:
                        pass
                    elif Quest.bomb_bull ==2:
                        pass
                    elif Quest.fesa != 0 or Quest.fesn != 0:
                        pass
                    else:
                        imagebutton:
                            idle "NPC/thane01.png"
                            hover "NPC/thane02.png"

                            action Return("Thane_talk")
                else:
                    pass
            else:
                pass
        vbox:
            xalign 0.32 ypos 0.02
            if Thane.mountain >= 1 and Map.mountain == 0:
                imagebutton:
                    idle "UI/mountain01.png"
                    hover "UI/mountain02.png"

                    action (Return("Climb_mountain"),SetVariable("Map.mountain",1))
            if Thane.mountain >= 1 and Map.mountain != 0:
                imagebutton:
                    idle "UI/basement03.png"
                    hover "UI/mountain02.png"

                    action Return("Climb_mountain")
            else:
                pass


        vbox:
            xalign 0.4 ypos 0.67
            if Time.hours >= 6 and Time.hours <= 17:
                pass
            else:
                if Foe.bulllick == False:
                    $ Random = renpy.random.randint(1, 3)
                    if Random == 1:
                        imagebutton:
                            idle "NPC/bullmale_4 ground.png"
                            hover "NPC/bullmale_4 hover.png"
                            action Return("Bull_lick")
                    else:
                        pass
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

label Bull_tribe_tent:
    $ renpy.music.set_volume(0, 0.5, channel = "Axel")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Axel')

    $ renpy.music.set_pause(False, channel='music')
    $ renpy.music.set_volume(1, 4, channel = "music")

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

    scene bulltent with dissolve
    if Quest.camp_a == 1:
        jump Axel_camp_end
    if Time.hours >= 6 and Time.hours <= 17:
        pass
    elif True:
        a "I need to rest, now move."
        jump Bull_tribe_map

    if Thane.quest == 7 and Quest.campl < 3 and Quest.campb == 1:
        jump Axel_meet

    if Quest.fesa ==1 and Quest.fes_end != 1:
        jump Axel_festival

    call screen Bull_tribe_tent with dissolve
    window show None
    show screen days
    stop music fadeout 1
    if _return == 'exit':
        jump Bull_tribe_map
        return
    if _return == 'Axel':
        if Quest.camp_a == 2:
            jump Axel_tribe_talk
        elif True:
            jump Axel_meet
        return
screen Bull_tribe_tent:

    imagemap:
        idle 'bulltent ground'
        hover 'bulltent hover'



        vbox:
            xalign 0.45 ypos 0.3505
            imagebutton:
                idle "NPC/axel01.png"
                hover "NPC/axel02.png"

                action Return("Axel")


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

label Room3:
    if Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bombt == 6 and Quest.fes_end == -1:
        $ Quest.fes_end = 0
        $ Time.festival_day = Time.days
    if Time.hours >= 6 and Time.hours <= 17:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(1, 5, channel = "Chan1")
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan1")
        $ renpy.music.set_volume(1, 5, channel = "Chan2")

    $ renpy.music.set_volume(0.3, 1, channel = "music")
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    $ Zalt.public = False
    if Time.hours >= 6 and Time.hours <= 17:
        scene room 3 with dissolve
    elif True:
        scene room 3n with dissolve
    if Map.yourroom == 0:
        "This is your room."
        "Whenever you rest in your bed you can spend the experience points you gain to level up."
        "As you level up you gain lvl-points which you can spend to raise HP/MP or ability levels."
        "Spend them wisely, and good night."
        $ Map.yourroom = 1
    call screen Room3
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
                jump Room3
            "Get stat point" if Zalt.points >= 5:
                menu:
                    "Strength" if Zalt.str <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.str = Zalt.str +1
                        $ Zalt.ATK = Zalt.ATK +3
                        "Your {color=#19c22a}STR{/color} now increase to {b}{color=#19c22a}[Zalt.str]{/color}."
                        jump Room3
                    "Agile" if Zalt.agi <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.agi = Zalt.agi +1
                        $ Zalt.ATK = Zalt.ATK +1
                        $ Zalt.CRIT = Zalt.CRIT +2
                        $ Battle.dodge = Battle.dodge +2
                        "Your {color=#19c22a}Agi{/color} now increase to {b}{color=#19c22a}[Zalt.agi]{/color}."
                        jump Room3
                    "Intelligence" if Zalt.int <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.int = Zalt.int +1
                        $ Zalt.maxmp = Zalt.maxmp +10
                        $ Zalt.MATK = Zalt.MATK + 3
                        "Your {color=#19c22a}INT{/color} now increase to {b}{color=#19c22a}[Zalt.int]{/color}."
                        "Your {color=#19c22a}MaxMp{/color} now increase to {b}{color=#19c22a}[Zalt.maxmp]{/color}."
                        jump Room3
                    "Endurance" if Zalt.end <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.end = Zalt.end +1
                        $ Zalt.maxhp = Zalt.maxhp +20
                        "Your {color=#19c22a}END{/color} now increase to {b}{color=#19c22a}[Zalt.end]{/color}."
                        "Your {color=#19c22a}MaxHp{/color} now increase to {b}{color=#19c22a}[Zalt.maxhp]{/color}."
                        jump Room3
                    "Charm" if Zalt.cha <= 10:
                        $ Zalt.points = Zalt.points -5
                        $ Zalt.cha = Zalt.cha +1
                        "Your {color=#19c22a}CHA{/color} now increase to {b}{color=#19c22a}[Zalt.cha]{/color}."
                        jump Room3
                    "Leave" if True:
                        jump Room3
            "Exchange 3 AP to 1 lv-point" if Zalt.AP >= 3:
                "{b}{color=#19c22a}You get 1 lv-point.{/color}."
                $ Zalt.AP = Zalt.AP -3
                $ Zalt.points = Zalt.points +1
                jump Room3
            "Leave" if True:
                jump Room3

    if _return == 'outroom':
        if Items.nude == False:
            jump Bull_tribe_map
        elif True:
            scene black
            e 7 "....No,I don't think it's a good idea to being nude in public."
            jump Room3
    if _return == 'Rest':
        menu:
            "Rest" if Time.hours >= 6 and Time.hours <= 21:
                scene black
                "You sleep for 3 hours, feel refreshed and full of energy."
                "HP and MP have been restored half of the maximum."
                $ Zalt.hp = min(Zalt.hp+Zalt.maxhp/2, Zalt.maxhp)
                $ Zalt.mp = min(Zalt.mp+Zalt.maxmp/2, Zalt.maxmp)
                $ Time.hours = Time.hours+3
                jump Room3

            "Rest until evening" if Time.hours >= 6 and Time.hours <15:
                scene black
                "You sleep until evening, feel refreshed and full of energy."
                "HP and MP have been restored to maximum."
                $ Zalt.hp = Zalt.maxhp
                $ Zalt.mp = Zalt.maxmp

                $ Time.hours = 18
                $ Time.mins = 0

                jump Room3
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

                jump Room3
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

                jump Room3
            "Leave" if True:
                jump Room3

    if _return == 'eyvind_solo':
        if Time.hours >= 6 and Time.hours <= 17:
            scene room 3 with dissolve
        elif True:
            scene room 3n with dissolve
        if persistent.CG_eyvind_solo:
            "Do you want to skip the scene?"
            menu:
                "Yes" if True:
                    "Slowly, you drift off to sleep."
                    $ Zalt.lust = 0
                    $ Time.mins = Time.mins+15
                    jump Room3
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
        jump Room3
screen Room3:

    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'room 3'
            hover 'room 3'
        else:
            idle 'room 3n'
            hover 'room 3n'



    frame:
        xalign 0.81 ypos 0.84
        imagebutton:
            idle "UI/outdoor01.png"
            hover "UI/outdoor02.png"

            action Return("outroom")
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
label bull_lick:
    "You hear strange noises coming from a nearby bush."
    "Groggy Voice" "Ugh,,, no more... Cecilia... no more."
    e 5 "What the heck is that?"
    "You part a few bushes and find a drunk bull warrior lying on his back."
    "His eyes are closed and the pungent smell of alcohol wafts from his open mouth."
    "On the ground you notice a bottle of spilled beer."
    "No doubt about it, this bull is beyond drunk."
    "Drunk Bull" "Cecilia! Come on baby, let’s do it!"
    e 10 "What are you talking about?"
    "He doesn’t respond. Then you notice what’s twitching between his legs. "
    "The drunk bull is hard! His twitching boner pushes the fabric of his loincloth upwards."
    "Drunk Bull" "Come on babe, just a quick blowjob."
    if Zalt.cor < 5:
        "You slap yourself in the face for even thinking about sucking him off."
        e 6 "No,I'm not a bad guy."
        "Clearing your head, you walk off and leave the drunk bull alone."
        jump Bull_tribe_map

    "What do you do?"
    menu:
        "Suck him off" if True:
            stop music
            scene black with slow_dissolve
            "Well, you’re always up to help someone in need."
            "You cross the bushes and stand over the bull’s head, taking your time to admire his thick body."
            "The moonlight illuminates his fuzzy brown fur revealing the fine sculpted muscles most of the bull warriors have."
            "Standing proudly under the moonlight is the bull’s thick cock."
            "Twitching ever so slightly, as though tempting you to come closer to it."
            "Looking at the bull’s face he looks so peaceful in his half conscious state."
            "Drunk Bull" "Come on! Quit making me wait all night!"
            "He grabs your calves and pulls you forward."
            e 0 "Argh!"
            "He is surprisingly strong even when he’s drunk. You lose your balance and fall on him."
            e 0 "Oof!"
            scene lick bull1 with dissolve
            e 0 "Huh? Wha!"
            "The bull’s cock rubs against your snout."
            "His cock’s musky scent is overpowering until you don’t notice the scent of alcohol anymore."
            e 0 "(Damn, he’s thick down here.)"
            "You touch his bulge slowly to avoid stirring the bull."
            "The moment your paw makes contact with his boner the bull lets out a loud mooing sound from behind."
            "Every fibre of your body freezes, as though you’ll turn invisible and avoid getting caught."
            "Turning around slightly, you see the bull over your shoulder sound asleep."
            "You breathe a sigh of relief and turn back to the bull’s dick."
            "Your heart pounds against your chest, the thrill of almost getting caught is exhilarating."
            "Mustering some courage, you cup a feel of the bull’s balls."
            "The sheer size of his orbs in your hands impresses you."
            "You fondle the pair in your one hand and knead them gently."
            "The sleeping bull groans in response to your playful touch."
            "Drunk Bull" "Take it off...Cecilia."
            e 0 "Ok?"
            e 0 "Who the heck is this Cecilia he keeps moaning about?"
            "Regardless, you strip the bull of his loincloth and bury your nose deep into his pulsating cock."
            scene lick bull2 with dissolve
            "Drunk Bull" "Yeah... suck it..."
            e 0 "Not yet."
            "You whisper to his member and continue playing his cock."
            "Using your tongue you lick his cock from its base right up to the tip."
            "The bull mutters something followed by soft gasps."
            "You lap his hot member like a tasty piece of candy, edging him until you get to the creamy center."
            "The bull grunts and a thick drop of pre pushes out from the tip of his dick."
            "Breathing heavily on top of his member, you jiggle your butt to free your own throbbing erection from beneath you."
            "Your hard boner pokes out from your loincloth and rests between his boulder like chest."
            "Drunk Bull" "Yeah, that’s it girl, put...your whole... on it... I promise it won’t hurt this time."
            scene lick bull3 with dissolve
            "You open your mouth and suckle on the head of his dick. His pre tastes deliciously salty. "
            "The more you suck on his dickhead the more pre fills your mouth."
            "You can’t help but drool and lose yourself in the taste of the bull’s cock. "
            "Your tongue circles around the head and rolls around it, every time, a dash of saltiness runs down your throat."
            "You pull your mouth off from the warm member and jerk it vigorously."
            "The bull moans and his right leg pulls upwarss towards him before kicking the ground hard several times, leaving a trench where his foot now sinks in."
            e 0 "Damn, if he's that rough when he's drunk, I can't imagine what he did."
            e 0 "I better just make him cum and go."
            "Drunk bull" "Ahhhh..."
            "You hang onto his cock for balance, and start licking his shaft with gusto."
            "The bull calms down slowly and lets out a satisfied breath."
            "Starting from the tip you take in the whole length."
            "Its girth fills your entire mouth and you can feel the tip hitting the back of your throat the moment your nose brushes against the base."
            "Taking deep breaths through your nose you pull back slowly along his cock."
            scene lick bull4 with dissolve
            e 0 "Mmm...mmm....mmmfff."
            "And you go down his shaft again."
            "Your tongue wraps and releases the meaty pole as you get accustomed to sucking the bull off."
            "It takes you a few tries but you find your momentum and you're able to suck the thick, throbbing dick with ease."
            "The bull is practically gasping for air."
            "You don't know when but his hips start buckling and he thrusts his dick in you forcing you to stay still."
            "Drunk bull" "Ahhhh...!!"
            with flashbulb
            scene lick bull5 with dissolve
            "A hot blast of cum jettisons from his cock."
            "You gag as mouthfuls of cum force their way down your throat."
            "Ultimately you are unable to drink it all and you're forced off of his cock gasping for air. "
            "Your face is stained with the bull's semen."
            e 0 "How the heck is he still cumming?"
            scene bulltribe 1n with slow_dissolve
            "The bull's still hard cock stands proudly under the moonlight and fires squirts of cum all over himself, some even landing on his face."
            "You sit next to him and smile."
            "The drunk bull still fast asleep has a silly looking grin on his face."
            "After licking yourself clean you leave the bushes. "
            $ Zalt.cor = min(Zalt.cor+1,100)
            $ Foe.bulllick = True
            $ persistent.CG_bull_lick = True
            jump Bull_tribe_map
        "Leave him be" if True:


            "You slap yourself in the face for even thinking about sucking him off."
            "Clearing your head, you walk off and leave the drunk bull alone."
            jump Bull_tribe_map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
