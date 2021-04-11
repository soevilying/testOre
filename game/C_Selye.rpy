label Selye_meet:
    $ Time.mins = Time.mins +5
    if Quest.campl == 1 and Quest.campb < 3:
        with flashbulb
        "The moment you step into Selye’s hut, a bright light flashes in front of you.Blinding you temporarily. "
        e 5 "Wha-"
        "Taken off guard, something flies over and wraps around your hands and legs, binding them to one another."
        "You tumble onto the wooden floor." with vpunch
        e 12 "What the fuck is this?"
        show selye stand at center with dissolve
        se "Quiet, brute. I am running a sssecurity inspection."
        se "You’d think I’d let you into my humble abode without making ssssure you’re not carrying sssomething dangerous or try to sssspy on me?"
        e 12 "What the heck? I’m not a threat!"
        se "Then you won’t have anything to worry about while I go through this."
        se "He grabs your satchel and rummage through your belongings."
        hide selye stand with dissolve
        e 12 "Hey, give that back! That’s an invasion of privacy."
        if Items.em >= 1:
            se "What’s this?"
            show selye stand at center with dissolve
            "The naga pulls out the emblem."
            e 5 "That’s nothing, that’s just something my friend wants me to collect."
            "He examines the emblem closely before chucking it back into the satchel and tossing it towards you."
            "The force that kept your limbs bound fades away, and you grab your satchel as you stand back up."
        elif True:
            se "A whole load of nothing."
            show selye stand at center with dissolve
            "He tosses your satchel right in front of your face."
            "The force that kept your limbs bound fades away, and you grab your satchel as you stand back up."
        "Your nostrils flare and your tail poofs up in anger."
        e 12 "Listen here, you prick!"
        "You point at Selye."
        e 12 "I don't know who you think you are-"
        "Selye beats hand away with a wave of his sceptre."
        se "I am the chief’s right hand man."
        se "I ssstand above the red and blue advisors, because I am the one who will ensure nothing gets in the way of fulfilling Chief Nauxus’ grand destiny."
        e 12 "You’re a pompous eggsucker is more like it! Now give me my mission so I can get out of here!"
        se "Hmph, very well then."
        se "Chief Nauxus has instructed me to pass this mission information to you, but you will be free to choose to take it or not."
        se "SSSSomething about him trusting you’ll do the right thing."
        se "Your mission is to help in the construction of a lizard camp near the bull tribe."
        se "I’ll mark the location on your map. It will be a ssssuitable location to sssstation our men to observe the enemy."
        se "Your mission is to take these rune sssstones I have crafted."
        se "Place them around the tree area, and it will create a barrier that will push out all other creatures except those recognized as allies by the lizard tribe."
        se "You need to be very careful when using these runes."
        se "They respond to the thoughts of the one who activates it, lose concentration and you will be blocking the wrong things out."
        "Selye holds out the four runes for you to see."
        "You observe the stones with curiosity, but then a thought came to mind."
        e 1 "Still this... is this really what’s right? We’re talking about actually going to war!"
        "Selye rolls his eyes at you and pulls back the runes."
        se "Ugh, must a foot ssssoldier like you really question your instructions?"
        se "Just take the job, and play your part."
        se "Is that ssssimpleton of a wolf brain unable to even make ssssense of that?"
        e 5 "What? A foot soldier? I’m a seasoned adventurer!"
        e 1 "Plus, all I’m saying is that this is a big deal. I’m just not sure if-"
        "Selye brings his scepter close to your lips and shushes you."
        se " Don’t worry your pretty little head about that."
        se "I can tell that you’re a born fighter, that’s what you’re meant to do."
        se "Leave the planning to those with natural talents for it."
        e 12 "What? Are you saying I can’t be anymore than some meathead who needs to follow orders?"
        hide selye stand with dissolve
        "He slithers close to you and coils around your legs, you’re stuck in the coil of his powerful tail."
        "He pulls himself close, forcing you to look at his face up close."
        show selye stand at center with dissolve
        se "Oh, no, no, no, don’t take it the wrong way."
        se "I’m just ssssaying that ssssome people are destined to do certain things better than others."
        se "And those that can’t keep up, sssshouldn’t trouble themselves with trying to be more than what they really are."
        se "Just like me, I’m willing to sssservice Chief Nauxus."
        se "I choose to obey him unconditionally, he is the most talented person I’ve ever met."
        e 12 "You don’t know that, nothing is set in stone."
        se "Oh, but I do. I believe you, me, and everyone else have been dealt their hands the moment they’re born."
        se "You either have all the right cards to win the game, or you don’t. That’s just how it is. "
        se "For those of you my friend who won’t win the game of life, you’re better off just sssserving the winners."
        se "At least, ssssome good will come of your existence."
        e 12 "I’m not your friend, and what are you even talking about?"
        e 12 "If you think I’m just going to accept my place in this world just as it is, you don’t know me!"
        se "No I don’t, but hopefully you will soon. "
        hide selye stand with dissolve
        "He frees you from his clutches and slithers across the room, before turning back to speak to you."
        show selye stand at center with dissolve
        se "Back to the matter at hand. Will you take these runes and help us sssset up our camp?"
        menu:
            "Yes" if True:
                e 1 "Fine, I’ll do it."
                se "Good, head to the area I marked on your map, and sssset the runes."
                se "Once you’re done, you’ll find me at Chief Nauxus’s hut, he will want to hear the outcome of these missions as well."
                se "The mission will take place {b}at 10 a.m{b} ."
                se "We leave when you’re ready. Sssso, sssspeak to me again when you are ready to depart, and I will take you to your team. "
                "You get four rune stones."
                "Now off with you."
                $ Quest.campl = 3
            "No" if True:
                e 1 "Not yet, I need to make preparations."
                se "Ugh, typical.Don’t keep me waiting, if you’re going to be incompetent to Chief Nauxus I will make sure you’re out of this village in a blink of an eye."
                se "Now begone, and don’t come back until you’ve decided."
                $ Quest.campl = 2
        hide selye stand with dissolve
        play sound "music/door.mp3"
        if Time.hours >= 6 and Time.hours <= 17:
            scene tree 1 with dissolve
        elif True:
            scene tree 1n with dissolve
        e 1 "(So, I have to help set up this lizard camp, huh.)"
        if Quest.campl == 2:
            e 13 "(I wonder if I should talk to Thane about this when I aceepet the quest, but will it be ok for him to know?)"
        elif True:
            e 13 "(I wonder if I should talk to Thane about this, but will it be ok for him to know?)"
        jump Lizard_tribe_tree
    if Quest.campl == 2 and Quest.campb < 3:
        show selye stand at center with dissolve
        se "So you’re back, are you ready to take the mission to set up the lizard camp?"
        menu:
            "Yes" if True:
                e 1 "Fine, I’ll do it."
                se "Good, head to the area I marked on your map, and sssset the runes."
                se "Once you’re done, you’ll find me at Chief Nauxus’s hut, he will want to hear the outcome of these missions as well."
                se "The mission will take place at{color=#19c22a} 10 a.m{/color} ."
                se "We leave when you’re ready. Sssso, sssspeak to me again when you are ready to depart, and I will take you to your team. "
                "You get four rune stones."
                "Now off with you."
                $ Quest.campl = 3
            "No" if True:
                e 1 "Not yet, I need to make preparations."
                se "Then stop wasting my time with pointless chatter. Off with you."
        hide selye stand with dissolve
        jump Lizard_tribe_tree
    if Quest.campl == 3 and Quest.campb < 3:
        show selye stand at center with dissolve
        se "Are you ready to begin the mission?"
        menu:
            "Yes" if True:
                e 1 "I’m ready."
                "Selye takes you to your team of three lizards, and discusses the plan of attack yet again."
                "They've been instructed to follow your directions."
                "By your command, your group departs the next day, if all goes to plan you will reach the campsite by 10 a.m."
                $ Quest.campl = 4
                jump camp_map
            "No" if True:
                e 1 "No, I need to prepare still."
                se "Then don’t waste my time. Come back when you’re ready."
                se "The longer you wait, the harder it is to execute this mission."
        hide selye stand with dissolve
        jump Lizard_tribe_tree
label Selye_camp_bull:
    if Time.hours >= 6 and Time.hours <= 17:
        scene lizardtribe 1 with dissolve
        play music "music/bird1.ogg"
    elif True:
        scene lizardtribe 1n with dissolve
        play music "music/bird1n.ogg"
    "You clutch the map given to you by Thane, your heart races and you wonder if your plan will work out or not."
    "As chance would have it, you spot Selye by the tribe shop, and you walk briskly towards him."
    e 6 "(Keep it cool [name], keep it cool.)"
    e 1 "Hey, Selye. You have a minute?"
    show selye stand at center with dissolve
    "Selye turns to you and rolls his eyes."
    se "What is it ssssimpleton?"
    e 1 "I found this near the swamp during a walk. Know what is it about?"
    "He opens the map that you hand over to him."
    se "Do you really need to bother me with ssssomething as ssssimple as-"
    "He appears to be at a loss for words, his hands trembling while looking at the parchment in his hand."
    se "Where did you get this?"
    e 1 "It was just by the entrance earlier."
    se "Well forget you ssssaw anything. This doesn’t concern you."
    hide selye stand with dissolve
    "He looks beyond mad by the map you gave him. He slithers away while calling one of the lizard guards. "
    "The guard runs off and calls two other lizards with him."
    "They follow Selye from behind up the stairway to Selye’s hut."
    "This is your chance to find out more about the lizard camp mission."
    scene lizardtree 1 with dissolve
    "You maintain some distance from the lizards as you sneak behind them."
    "The moment they enter Selye’s hut, you tiptoe to a nearby open window. "
    e 5 "(Damn it, the window’s too tall. I can’t hear what they’re saying.)"
    "You need to be careful while spying on them, if you’re not agile enough they’ll catch you, and that will be even harder to talk your way out of it."
    "Carefully, you press up against the corner of the window frame and peek your head out a little bit."
    scene treehut 1 with dissolve
    show selye stand at center with dissolve
    "The lizards have their back turned to you, and Selye’s fuming mad."
    se "Which one of you did this? Who left the mission map lying around the sssswamp?" with vpunch
    "First Lizard Guard" "Wasn’t me."
    "Second Lizard Guard" "Mine’s still with me."
    "Third Lizard Guard" "Doesn’t look like mine."
    se "I want to ssssee proof! Pull out your maps."
    hide selye stand with dissolve
    "The lizards pull out from their satchels pieces of paper. "
    show selye stand at center with dissolve
    se "Hmm, if you all have it then what is this?"
    "Second Lizard Guard" "Maybe it’s just a toy one of the children made."
    "Third Lizard Guard" "Yeah, I seen the kids play around with maps pretending to be like the chief."
    "Third Lizard Guard" "Plus look, the stamp on that map is kinda sloppy looking. "
    "First Lizard Guard" "Probably one of the kids made a toy stamp and just stamped a map."
    se "Possible, but I’m not taking any chances."
    se "Either this was merely by chance, or an enemy party has gotten news about our plans."
    "First Lizard Guard" "Must be a stupid enemy to drop the map around here."
    "Second Lizard Guard" "Do we call off the mission?"
    se "No! We will proceed as planned. We must succeed sssso that Chief Nauxus doesn’t lose faith in his plan."
    "Third Lizard Guard" "Don’t you mean doesn’t lose faith in you?"
    "The group burst into laughter but Selye gives them the evil eye, effectively silencing them."
    se "Memorize the attack location, then destroy the maps."
    hide selye stand with dissolve
    "The lizards take a few minutes to look at their map and exchanging whispers among each other."
    "They then rip apart the map and Selye burns the pieces of torn paper with fire he conjures from thin air."
    show selye stand at center with dissolve
    se "Now, recite the plan to me. When is the attack happening?"
    "Selye looks at each guard and his eyes suddenly falls upon your direction."
    if Zalt.agi >5:
        "{b}{color=#19c22a}<Agile Check success>{/color}"
        "You quickly duck back down. Your heart is racing, but your legs won’t budge. Did he see you?"
        se "Well?"
        "Third Lizard Guard" "Uhh, let me think about it."
        "Second Lizard Guard" "Can’t quite remember."
        "First Lizard Guard" "Give me a minute to think."
        se "Ugh, incompetents goons!"
        "Good, Selye didn’t see you."
        "First Lizard Guard" "Now I remember, we were supposed to head out when we’re ready."
        "Second Lizard Guard" "Yeah, yeah. Just as long as we get there at 10 a.m."
        "Third Lizard Guard" "Then we plant rune stones."
        "Selye rubs his forehead like he has a headache from talking to his men."
        se "Forget the time for preparations, you’ll make your move tomorrow."
        se "Now get your tails in gear and leave me be."
        se "This whole debacle has left me sour for the whole day."
        "The three lizards bow and make their way towards the door."
        scene black with dissolve
        "You dart off fast enough to reach the stairs unseen."
        "Now you know when the attack is going to happen. Best to leave the tribe for now."
        "Time to ask Chet about the potion."
        $ Quest.campc = 1
        $ Time.lizardgo = Time.days
        jump Lizard_tribe_map
    elif True:
        "{b}{color=#c22719}<Agile Check failed>{/color}"
        se "Who’s there?" with vpunch
        hide selye stand with dissolve
        "You duck back down, but it’s too late."
        scene lizardtree 1 with dissolve
        play sound "music/door.mp3"
        "The sound of running feet approach you, and the door swings open."
        e 5 "(Damn it!)"
        scene treehut 1 with dissolve
        play sound "music/door.mp3"
        "The lizard guards grab you and pull you against your will inside the hut."
        "They force you onto your knees in front of Selye."
        show selye stand at center with dissolve
        "He hisses angrily as he stares down at you."
        se "Why are you here?"
        "One of the guards presses their claws deep into your shoulder."
        "You wince from the sharp pain."
        if Zalt.int >6:
            "{b}{color=#19c22a}<Intelligence Check success>{/color}"
            e 1 "I was just waiting for my turn to go talk to you."
            se "What for? I didn’t ssssummon you. "
            e 1 "Yes, well you didn’t let me explain about the map earlier and you just slithered away!"
            e 1 "I found some kids playing with another map with the similar stamp."
            e 1 "So I told them off, and was coming here to tell you maybe it’s a toy, before you did anything stupid with your plans for the war!"
            "First Lizard Guard" "Should have come in sooner."
            "Second Lizard Guard" "Yeah, he made us tear up our maps for nothing."
            "Selye hisses and backs away with a twitch in his right eye."
            "It’s as though having his mistakes pointed out to him is inflicting him physical pain. "
            se "Enough! Let’s not talk about it anymore." with vpunch
            se "Just get your tails at the meeting point tomorrow at 10 a.m."
            se "Now, everyone out!"
            play sound "music/door.mp3"
            hide selye stand with dissolve
            scene lizardtree 1 with dissolve
            "Third Lizard Guard" "What happened to us heading out when we’re prepared? Swamp crud, now we have to go tomorrow."
            "Second Lizard Guard" "I just hope we don't get lost without our maps."
            "First Lizard Guard" "Wait, which one of us is supposed to have the rune stones?"
            "The three lizards chat nonchalantly while walking off to the platform and out of sight. "
            "You thank the Divine Beings that it all worked out. "
            "Now, you have the information on when the attack is going to happen. Time to ask Chet about the potion."
            $ Quest.campc = 1
            $ Time.lizardgo = Time.days
            jump Lizard_tribe_map
        elif True:

            "{b}{color=#c22719}<Intelligence Check failed>{/color}"
            e 6 "I was just, following this really colourful butterfly, and it landed on your window. That’s all."
            "The lizards behind you laugh in unison."
            se "Likely sssstory, you may be the chief’s guest, but no one sssspys on me and gets away with him."
            se "Discipline him!" with vpunch
            e 9 "Wait! Wait!"
            hide selye stand with dissolve
            scene lizardtree 1 with dissolve
            "The lizards drag you out of the hut like a roast ready for serving on a pole."
            "You flail for freedom, twisting your arms and trying to kick your captures away, but their hold on your limbs are too strong."
            "They drop you in the middle of the platform and circle around you."
            "There’s no room to run, and they’re all looking at you and chuckling menacingly."
            "You get ready to guard your face."
            "First Lizard Guard" "Hey! Wolf guy."
            "The lizard speaks in a soft voice."
            "First Lizard Guard" "Relax, we’re not going to hurt you, much."
            "You relax your guard a little."
            e 1 "What?"
            "Second Lizard Guard" "Yeah,nobody likes getting bossed around by Selye, who’s he to come in here and act all high and mighty just cause he got the job to consul the chief about the war."
            "Third Lizard Guard" "He’s so full of himself. I was actually happy someone can get under his skin."
            e 9 "Yeah, I get it. Listen, I really just wanted to pull a prank on him."
            e 9 "Like on the day of his grand plan he gets an egg or twenty to the face. That’s all."
            "Selye’s voice can suddenly be heard from across the platform."
            se "What are you drones doing? Can’t you even beat ssssomeone up properly?"
            "First Lizard Guard" "Ah, there he goes again."
            "First Lizard Guard" "Yeah, sorry mate but have to make it look convincing, we’ll talk more after he’s gone."
            e 9 "Oh crap."
            "The lizards pummel you with their fists and kicks, you feel your health dwindling away." with vpunch
            show red2 at center with dissolve
            "<You lose half of your HP>"
            "Your purse is accidentally kicked out of your satchel and soars through the sky and falls off the platform."
            "Not too long you hear the sound of something falling into water."
            "<Player loses all coins>"
            "First Lizard Guard" "Oh shit."
            $ qty = jane_inv.qty(coin)
            $ jane_inv.drop(coin,qty)
            $ Zalt.hp = Zalt.hp/2
            show selye stand at center with dissolve
            se "Alright, that’s enough!"
            "Selye’s command ends the beatings."
            "You see him standing over you with his arms crossed."
            se "There’s your lesson about knowing your place , ssssimpleton. Alright, we’re done here. "
            se "The plan goes as we discussed originally. I’ll personally ssssend the instructions again later. Dismiss!"
            hide selye stand with dissolve
            "After Selye walks away one of the lizards help you up to your feet, and the three of them take you back to your hut. "
            $ Time.hours = Time.hours +2
            hide red2 with dissolve
            if Time.hours >= 24:
                $ Time.hours = Time.hours - 24
                $ Time.days = Time.days + 1
            if Time.mins >= 60:
                $ Time.mins = Time.mins -60
                $ Time.hours = Time.hours +1
            if Time.hours >= 6 and Time.hours <= 17:
                scene room 4 with dissolve
            elif True:
                scene room 4n with dissolve
            "First Lizard Guard" "That wasn’t so bad, now was it?"
            "First Lizard Guard" "Well,except for your purse."
            e 13 "Ugh."
            "First Lizard Guard" "So back to the thing we talked about. You want to embarrass Selye on the day of the mission."
            e 1 "Yes."
            "Third Lizard Guard" "Well it's our bad you lost all your coins, so I guess we owe you something."
            "Third Lizard Guard" "Basically, Selye gave us time to prepare ourselves before going, so it’s up to us. "
            "First lizard guard" "We plan to head out tomorrow morning at 10 a.m."
            e 6 "Thanks for the info, I really appreciate it."
            "First Lizard Guard" "All the best egging him."
            "Second Lizard Guard" "You think we'll get lost without our maps tomorrow?"
            "Third Lizard Guard" "Who knows, if anything we'll just blame it on Selye for destroying our maps."
            "The lizards leave your hut, and you now know when the attack is going to happen. Time to ask Chet about the potion."
            $ Time.lizardgo = Time.days
            $ Quest.campc = 1
            jump Room4
label Selye_letter:
    if Quest.bombn == 2:
        scene treehut 1 with dissolve
        "The naga advisor slumps over his desk muttering to himself while he toys with his scepter."
        "You hear the sound of stones clicking from where he’s working."
        "He notices you and his face instantly sours. He picks up his things and turns to you."
        show selye stand at center with dissolve
        se "What brings you here, ssssimpleton?"
        "You cross your arms and take a long breath."
        e 1 "Look, if we’re going to keep working together… you got to get off your high horse, and start talking to me with some respect."
        se "Respect? For Chief Nauxus’s boytoy?"
        "You stare the naga down."
        e 1 "Watch what you say next, Selye."
        if Quest.campw1 == 4:
            "Selye rolls his eyes at you. He leans in and matches your gaze with his sharp eyes."
            se "Don’t think you’ve proven yourself just by doing one grunt job properly. You are still just a grunt."
            "You clench your fists and grit your teeth in anger."
            se "What’s more, I detest you to the very core, [name]."
            se "You’re everything that I hate in a person."
            e 1 "What kind of bullshit is that? We don’t even know each other."
            se "Yes, but I know your type. A nobody that comes into the lives of others and disrupts the order of things."
            se "Ssssoon, friends turn on another, lovers become sssstrangers, and …"
        elif True:
            "Selye rolls his eyes at you. He leans in and matches your gaze with his wide eyes."
            se "You couldn’t even execute your mission properly."
            se "Yet, Chief Nauxus still favours you, he still trusts you with his plans."
            se "Ssssimply, mind boggling."
            se "But why am I ssssurprised? I’ve seen it happen before, it’s only bound to happen again."
            se "People like you are everywhere, and that just makes me detest you even more."
            e 1 "What?"
            se "You’re the kind that waltz into people’s lives and disrupts the order of things."
            se "Just like a parasite. Eventually, friends turn into enemies, lovers into sssstrangers, and…"

        e 1 "And?"
        se "It doesn’t concern you for now, ssssimpleton."
        e 12 "Jackass!"

        se "Now before I went off on a tangent, I think I was asking why you're here?"
        "Although still annoyed, you decide to put your feelings aside so you can get on with the mission."
        e 1 "Chief Nauxus asked me to come here if I decided to help him with convincing the rogue lizards to rejoin the tribe."
        se "And of course, he chose you, his pet."
        "You growl angrily."
        se "I was wondering why he would commission me to make a transformation amulet just for a diplomatic mission. "
        show amulet at center with dissolve
        "Selye hands you an amulet. It’s simple in its design, just a green stone with tiny inscriptions on it tied by a coarse string."
        e 1 "A transformation amulet? Why do I need it?"
        show selye stand at center with dissolve
        hide amulet at center with dissolve
        se "It’s simple common sense. Chief Nauxus is going into enemy territory."
        se "If they ssssee him with an outsider, their suspicions will go through the roof."
        se "And ssssince Chief Nauxus insists on having you along, you will need to disguise yourself as a lizard warrior."
        e 1 "Ok, how do I use it?"
        se "I’ve made it user friendly so even a ssssimpleton like you can use it with ease."
        se "Sssssimply wear it, and it will project a barrier around you, giving you the looks, feel and sssscent of a lizard."
        e 5 "That’s incredible."
        hide selye stand at center with dissolve
        "Selye appears pleased with your reaction."
        "He lifts his nose into the air with a smug smile."
        e 1 "I hate to admit it, but you make strong magic items. How’d you learn to do it?"
        show selye stand at center with dissolve
        se "Now you’re curious about my talents?"
        se "I guess to a ssssimple creature like yourself, these trinkets I make must seem like amazing acts of magic."
        e 1 "Well I’m just curious about your backstory, how did you become so powerful?"
        "His smile suddenly frozen."
        se "Hmm… I guess it can’t be helped, my greatness draws all to me."
        se "But if you want to hear my story, wait until you ssssuccessfully carry out this mission, and you best tell Chief Nauxus it’s my magic that helped you do it."
        e 1 "Ok…?"
        se "Now off with you, return to Chief Nauxus. I have things to do."
        hide selye stand with dissolve
        scene black with slow_dissolve
        "You leave Selye’s hut."
        play sound "music/door.mp3"
        scene lizardtree 1 with dissolve
        show amulet at center with dissolve
        "Right at the foot of the steps you put on the amulet."
        e 1 "I don’t feel any different."
        hide amulet at center with dissolve
        "Looking down, your hands and feet still look the same."
        e 13 "He better be right about this."
        $ jane_inv_K.take(selye_amulet)
        $ Quest.bombn = 3
        $ Quest.bomb = 3
        jump Lizard_tribe_tree
    elif Quest.bombn == 3:
        scene treehut 1 with dissolve
        show selye stand at center with dissolve
        se "You have the transformation amulet, now go ssssee Chief Nauxus to escort him to the dark sssswamp."
        se "Don’t bother me until you finish your mission."
        hide selye stand at center with dissolve
        jump Lizard_tribe_tree
    elif True:
        "See this mean it's a bug , pls report."
        jump Lizard_tribe_tree


label Selye_past:
    "You enter Selye’s hut and find him pouring a glass of wine for two."
    show selye stand at center with dissolve
    se "My, my if it isn’t the wolf that reunited the lizard tribe. "
    se "I was just about to ssssend ssssomeone to get you."
    hide selye stand at center with dissolve
    "He walks over with both glasses of wine in hand."
    "You reach out for the closest glass thinking it is for you, instead he pulls it away and downs the entire drink before putting the glass on his table."
    show selye stand at center with dissolve
    se "Now, before I go sssspeak to Chief Nauxus I believe I owed you a sssstory didn’t I?"
    e 1 "I wasn’t expecting you to keep your promise."
    se "My dear ssssimpleton, you underestimate me."
    se "After all, you might learn a thing or two about how not to be such a pain in the ass."
    "You click your tongue."
    se "Well what can I ssssay about myself?"
    se "I was born as the sssson of the sssstrongest hunter in my village. "
    se "With a beautiful woman in my arms I trained day by day in preparation to take over my father’s title. "
    e 1 "Then why are you here?"
    "He clutches the other glass of wine and his face twists into a dark frown."
    se "Because… one day, out of nowhere another naga appears."
    se "His origins unknown, his body battered and bruised from who knew what."
    se "We took him in, and…"
    se "And he took everything from me. "
    e 1 "What do you mean?"
    "Selye leans in close, his pupils widen like a mad man."
    se "He tricked everyone in the village into loving him."
    se "Winning everyone over with his hunting sssskills and courageous deeds."
    se "It sssstung me in the heart how every day I would ssssslip further and further into the ssssshadows while he became the village hero, an outsider!"
    se "No matter how hard I trained my body, I was never close to besting him. "
    se "But I could have forgiven all of that, if only… "
    "He pulls back and his hand forms a fist that rests on the left side of his chest."
    se "If only sssshe hadn’t fallen in love with him."
    e 13 "I’m sorry to hear that."
    se "..."
    se "Don’t be ridiculous. It was a learning experience."
    "He hides his hands behind him and his face stretches as he smiles widely."
    "You are taken aback by how alien he looks now."
    se "That valuable betrayal taught me how futile it was for me to try to play catch up to him as a hunter."
    se "He had been naturally blessed by the gods of our world in every way."
    se "That’s why I abandoned the way of the hunter and picked up magic."
    se "I will raise through the ranks and be great again."
    "He staggers a bit as he slithers forward."
    se "Now, I think that’s all you need to know."
    hide selye stand at center with dissolve
    "He points to the door signaling to you that it’s time to leave."
    "You take a step towards the exit before turning back to Selye."
    e 1 "Are you… are you trying to win your old love back?"
    "Selye takes a deep breath and the frills on his neck expand outwards and shake vigorously."
    show selye stand at center with dissolve
    "He stands staring at you."
    se "What a sssstupid thing to say."
    hide selye stand at center with dissolve
    "You leave."
    $ Selye.past = 1
    play sound "music/door.mp3"
    jump Lizard_tribe_tree0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
