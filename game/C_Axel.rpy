label Axel_meet:
    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Axel')
    $ renpy.music.set_volume(1, 4, channel = "Axel")

    $ Time.mins = Time.mins +5
    if Quest.campb == 1 and Quest.campl < 3:
        "The guard bows and takes his leave, leaving you and Axel alone in the tent."
        show axel stand at center with dissolve
        a "Let’s skip the greetings."
        a "I’ve gotten news that the lizard tribe are making their move."
        a "They plan to claim an area close to our tribe, and to station some of their troops there."
        a "Cheeky bastards those lizards, but I’ll give them credit it’s a good spot."
        e 1 "So, what does this have to do with me?"
        a "Simple, you will lead a group of my men to the area the lizards want to take over."
        a "Knock their heads off, and make sure they don’t get to claim it ever again."
        e 1 "Where did you even get this info from?"
        e 1 "The bulls aren’t exactly the stealthiest of the bunch."
        a "Who needs stealth when all you have to do is break a few bones, and they’ll sing for you."
        a "Now, I’ll be merciful and fair, and let you choose to accept this job or not."
        a "The last thing I need is a useless warrior working against his will."
        menu:
            "Yes" if True:
                e 1 "Very well, Chief Axel."
                a "Good, if only Thane could learn a thing or two from you about not talking back so much."
                a "I’ll give you some time to prepare, come back to me when you are ready, and I’ll introduce you to your team."
                $ Quest.campb = 3
            "No" if True:
                e 5 "I still need some time to think about it."
                a "Then get out of my sight, I don’t have time to waste on someone who won’t work!"
                $ Quest.campb = 2
        if Time.hours >= 6 and Time.hours <= 17:
            scene bulltribe 1 with vslow_dissolve
        elif True:
            scene bulltribe 1n with vslow_dissolve
        e 1 "(What do I do now? Do I go through with Axel’s orders?)"
        e 13 "(If I don't, then what will the lizard tribe do? I’m not exactly his favourite person at the moment. )"
        if Quest.campb == 3 or Quest.campl == 3:
            "You turn and your gaze falls on Thane sitting on his rock."
            e 5 "(Thane! Maybe he has some other way to deal with this, but do I really want his help?)"
            e 1 "(Things might get trickier with him involved.)"
        elif True:
            "You turn and your gaze falls on the rock Thane usually sits on, but he isn’t there."
            e 6 "Where is he when I need him?"
            e 13 "(I can’t wait for Thane to show up to decide on what to do. )"
            e 13 "(I’ll have to make my choice and tell Thane about it later.)"
        hide axel stand
        jump Bull_tribe_map

    if Quest.campb == 2 and Quest.campl < 3:
        show axel stand at center with dissolve
        a "Have you finally decided to take on the job of getting rid of those trespassing lizards?"
        menu:
            "Yes" if True:
                e 1 "Very well, Chief Axel."
                a "Good, if only Thane could learn a thing or two from you about not talking back so much."
                a "I’ll give you some time to prepare, come back to me when you are ready, and I’ll introduce you to your team."
                $ Quest.campb = 3
            "No" if True:
                e 5 "I still need some time to think about it."
                a "Then get out of my sight, I don’t have time to waste on someone who won’t work!"
        hide axel stand
        jump Bull_tribe_tent
    if Quest.campb == 3 and Quest.campl < 3:
        show axel stand at center with dissolve
        a "I take it you're ready to head out?"
        menu:
            "Yes" if True:
                e 1 "I'm ready to go."
                "Axel summons four other bulls to his tent."
                "They've been instructed to follow your orders."
                "And by your commands the team will head out and reach the campsite by 11 a.m."
                $ Quest.campb = 4
                jump camp_map
            "No" if True:
                e 5 "I need more time to prepare."
                a "Axel sighs and waves you away with a disappointed shake of his head. "
        hide axel stand
        jump Bull_tribe_tent
label Axel_camp_end:

    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Axel')
    $ renpy.music.set_volume(1, 4, channel = "Axel")

    window hide None
    stop music fadeout 1
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    scene bulltent with slow_dissolve
    if Time.bullkid == 9999:
        $ Time.bullkid = Time.days
    if Quest.campb > Quest.campl and Quest.campt >=5:
        $ Time.hours = Time.hours +3
        "You hobble your way up the stairs towards Axel’s tent. The pain in your eye and stomach still stings from every step."
        "When you enter the tent, you see the fours bulls that made up your team on their knees in a row."
        show axel stand at center with dissolve
        "Axel paces back and forth while speaking to team."
        a "So, you’re telling me four trained bull warriors, ran away because a “giant wolf” appeared out of nowhere and started terrorizing everyone."
        "First Bull Warrior" "Honest, it happened."
        a "And you! Where were you? Why are you coming back here without your team."
        "He points at you standing at the tent’s entrance."
        "The bulls on their knees turn towards you and look surprised to see you there."
        "You take a step back, but you tell yourself not to run."
        e 13 "I was knocked out by something heavy when I went to scout ahead."
        e 1 "When I woke up I was in a bunch of bushes and no one was around."
        "Second Bull Warrior" "Yeah, looks like you got stomped against a rock."
        "Fourth Bull Warrior" "See, the wolf giant is real, and it’s too strong for us to beat."
        "Axel huffs loudly, you can see the puffs of air jettisoning out of his nostrils."
        hide axel stand with dissolve
        "He turns and sits on his throne, resting his chin on one hand. "
        a "And what about the lizards?"
        "Second Bull Warrior" "I saw them run off scared. I think they were no match for the giant wolf either."
        a "If there is such a dangerous creature out there, you four, head to the village and spread the word for everyone to stay away from that place. "
        "All Four Bulls" "Yes, Chief Axel!"
        a "After, you visit the local healer and get yourselves checked out."
        "The warriors salute their leader and leave the tent."
        show axel stand at center with dissolve
        "Axel taps the arm of his throne and gives you a curious look."
        a "So neither side wins the campsite. What do you think about that?"
        menu:
            "Stay silent" if True:
                e 13 "..."
                a "..."
                a "Fine, I’ll call you when there’s work."
                "You bow and turn to leave the tent."
                a "Hey, Fleabag."
                "You turn to the chief."
                a "You look like shit, take this and get some medicine."
                a "That wolf did a number on your eye."
                "He tosses you a pouch of coins."
                "<[name] gained 200 coins>"
                "<[name] gained one Level-up-point.>"
                $ jane_inv.take(coin,200)
                $ Zalt.points = Zalt.points +1
                e 13 "Thank you."
                "You leave the tent."
            "No bull had to die" if True:
                e 1 "No one died, I think that’s good enough."
                a "Is it now? Well no lizards died either."
                a "If we had taken them down it could have dealt a blow to their morale, but nothing’s changed, and my people are still in danger."
                a "Do you still think this is a good ending?"
                e 1 "..."
                e 1 "Is there anything else?"
                a "Just this."
                "He tosses you a pouch of coins."
                a "Fix up your wounds. Your eye looks like shit."
                "<[name] gained 200 coins>"
                "<[name] gained one Level-up-point.>"
                $ jane_inv.take(coin,200)
                $ Zalt.points = Zalt.points +1
                e 13 "Thank you."
                "You leave the tent."
        $ Quest.campb =6
        $ Quest.campt =6
        $ Quest.camp_a = 2
        jump Bull_tribe_map
    elif Quest.campb < Quest.campl and Quest.campt >=5:
        $ Quest.camp_a = 2
        "You cautiously approach the bull tribe’s chief who sits upon his throne and looks at the ground with a weary expression. "
        show axel stand at center with dissolve
        a "What do you want Fleabag?"
        "He looks up at you, his eyes burn with the glare of a dangerous warrior."
        "His body gives off a powerful aura."
        "Your senses tell you to tread carefully, he isn’t in a good mood."
        e 1 "I just wanted to talk, I can come back later."
        a "Why not right? You see an old bull looking troubled, you best just let him be, don’t even bother to ask what’s wrong."
        e 9 "(This feels awkward.)"
        e 1 "Ok, what’s wrong?"
        a "If you had bothered to care, our tribe was dealing with the lizards' first attempt to take over the place."
        a "Where were you? So called “ally of the bull tribe.”"
        e 9 "I-"
        a "I don’t want to hear it! It’s clear that you have a long way to go before you can truly be one of us."
        a "If I had my way you’ll be kicked hard enough you’ll fly back to the tavern for how much you've “helped” so far, but my son still thinks you worthy."
        a "I honestly do not see it, you have no love for my people."
        a "For that you will never ever be worthy of being our ally."
        "Despite his resistance to you being in the tribe, it sounds like he genuinely wants you to help them."
        "Still, is this the route you want to take?"
        "Do the lizards deserve to be taken down?"
        "How long can you keep up playing the middleman, stalling for time?"
        a "So, I decided, I will make you eat, sleep and breathe bull culture and make you into a warrior worthy of our tribe."
        "You want to reject whatever it is that Chief Axel is offering, but you decide against it for fear of what he’d do in his angered state."
        "He turns back and sits on his throne."
        a "My horns are practically steaming now, I just want to put all this lizard nonsense behind me."
        a "Talk, Fleabag."
        jump Axel_tribe_talk1
    elif Quest.campl > Quest.campb and Quest.campt <5:
        $ Quest.camp_a = 2
        "You hear a loud crashing sound and an angry moo coming from the inside of the tent."
        "You gulp at the entrance to Axel’s tent. "
        "The chief must have heard about what happened to his men."
        "You are hesitant to enter."
        "Still, there’s also the chance that he doesn’t know about all of it."
        "In which case, being distant isn’t going to help."
        "You grit your teeth and enter the tent."
        a "FUCK!"
        show axel stand at center with dissolve
        "The bull kicks his throne onto the ground."
        a "What the fuck you want?"
        e 9 "I-"
        a "Shut it, I lost my men. Do you even know what it means to lose your people?"
        a "They were good men, they had families, they had ambition. All fucking gone."
        a "Unless if the next words from your mouth, is you’re going to help deal with these lowlife lizards."
        a "I don’t want to hear it! Get out!"
        scene bulltribe 1 with dissolve
        "You run out of the tent."
        $ Time.aaxel = Time.days
        jump Bull_tribe_map
    elif Quest.campb > Quest.campl and Quest.campt <5:
        $ Quest.camp_a = 2
        show axel stand at center with dissolve
        "Chief Axel stands in front of his throne with his arms crossed and a large smile on his face."
        a "Welcome back Fleabag, I’m impressed, you helped me stop the lizards and got us an impenetrable campsite."
        e 1 "News travels fast."
        a "I could hear your crew cheering their victory from here."
        a "I might get some use from you yet,Fleabag."
        e 13 "Thanks, I guess."
        "Axel tosses you a pouch of coins."
        a "Spend it wisely."
        "<[name] gained 500 coins>"
        "<[name] gained one Level-up-point.>"
        $ jane_inv.take(coin,500)
        $ Zalt.points = Zalt.points +1
        a "One last thing, I think it’s time you start to know the bulls around here."
        a "You can’t be an ally of our tribe if you don’t know the tribe itself."
        e 6 "Ok?"
        a "I’ll call for you Fleabag when it’s time. Now move, I’ve got a village to run."
        $ Quest.campb =6
        jump Bull_tribe_map

label Axel_tribe_talk:
    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Axel')
    $ renpy.music.set_volume(1, 4, channel = "Axel")

    show axel stand at center with dissolve
    if Quest.bomb_end != 0 or (Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bomb_bull ==2):
        jump Axel_letter
    if Quest.fes_end == 0 and Quest.fesa >= 1:
        jump Axel_festival
    a "Hmm, well if it isn’t my personal hound. What is it Fleabag?"
    jump Axel_tribe_talk1
label Axel_tribe_talk1:
    if Axel.talktree == 1:
        menu:
            "Ask about making new weapons" if True:
                e 1 "Chief Axel, I wanted to talk to you about weapons."
                a "What about it Fleabag?"
                e 1 "Well I’ve seen almost every bull villager carry a weapon of their own."
                a "All the more easier to protect themselves of course."
                e 1 "True, but what I’m really interested in is, is it possible for me to get a bull made weapon for myself? "
                a "Interested in our weaponsmithing, ay kiddo."
                a "Can’t say I blame you. \nOur weapons when in the right hands will be enough to topple armies. "
                a "You’ll need to talk to the shopkeeper if you want some of his gear."
                a "Even I have to play by his rules if it comes to weapons."
                jump Axel_tribe_talk1
            "A new tour" if True:
                a "Hey Fleabag. How familiar are you with the village now?"
                e 6 "I’d say I’ve seen most of it by now."
                a "Hmm, what about the bull temple?"
                e 1 "Well there’s a room with a weird partition in it."
                a "Yeah, yeah. We all know about that room, \nbut have you seen anything out of the ordinary around the area?"
                a "Perhaps of a gravestone variety."
                e 1 "No, I haven’t before."
                a "Alright, then it’s decided. Make yourself available when I call."
                a "We’ll continue the tour to somewhere special."
                e 1 "I’m always at your service Chief Axel."
                a "And lighten your load, I’ve got some heavy equipment for you to carry. "
                e 9 "Very well. "
                jump Axel_tribe_talk1
            "Ask about remarrying" if Axel.s <=3:
                e 1 "Chief Axel, there’s something that’s been on my mind, about you."
                a "What is it Fleabag?"
                e 6 "You ever thought about remarrying?"
                a "Hah! There’s a question people will never stop asking. "
                a "I’ll admit, it’s been lonely a bit having no one else to share the bed with."
                e 6 "I mean I could…"
                a "No. No offense, but you’d have to be a goddamn hero to this village for me to consider being in bed with you."
                a "Even then I’d won’t call us lovers."
                a "It’s just I’m not sure if getting a new wife would be the right thing for Thane and I."
                a "You’ve seen what has become of us."
                a "If another women enters our lives it won’t be fair to her to go through our family drama."
                e 13 "Maybe that’s more of a reason to settle things with Thane. "
                a "Maybe. If any woman would want an ol’ tubby like me."
                e 6 "Trust me, you’re plenty attractive."
                a "..."
                a "You’ll bang just about anything that walks wouldn’t you?"
                e 5 "… Oh, look at the time. I should be heading back out there."
                jump Axel_tribe_talk1
            "Leave" if True:


                jump Bull_tribe_tent
    elif True:
        menu:
            "Ask about the fog" if True:
                e 1 "Chief Axel, I need to ask about the fog."
                e 1 "Despite the war, the greater threat is us being stuck here with this fog conjuring monsters."
                a "Well let me save you some time by saying, we don’t know anything about this fog."
                a "When the fog first came we didn’t think much of it, we had experienced fog before."
                a "After a while, we realized that the fog wasn’t going anywhere."
                a "So, I sent a few scouts to find the forest exit, around then we made contact with the tavern, it was only that hyena and…"
                a "What’s his name? Claude? No, Snow."
                a "The fog does lift at odd moments, we once gathered all the bulls and lizards by the exit and had them leave the moment the fog lifted."
                e 1 "Then why are so many of you still here."
                a "Those who stayed behind did so to protect the village and the temple."
                a "Our tribe’s ancestors travelled far to build this home for us, we aren’t letting a fog take it away from us without a fight."
                e 1 "So the bulls and the lizards were able to work together before."
                a "That was a long time ago."
                a "Then the kidnappings happened, and before we knew it we got separated from the rest of the forest by the fog."
                a "The kidnappings stopped around then, adding suspicion that because the lizards couldn’t find us."
                a "We were safe, but we have been connected again to the rest of the forest."
                e 13 "It could all just be a coincidence. "
                a "A coincidence doesn’t explain the lizard scales and the lizard weapons we found when we confronted the kidnapper."
                a "That, and the horrid tattoo on his back. I’ll never forget that."
                e 1 "You were there?"
                a "Ahh, my mood is spoiled. Talk about something else."
                jump Axel_tribe_talk1
            "Ask about the proof of the kidnappings" if True:
                e 1 "How are you so sure someone from the lizard tribe is the kidnapper."
                a "We have the lizard scales from the scene of the crimes to prove it, and because I damn well saw it with my own eyes."
                a "The slimy piece of trash was caught red handed trying to break into a home by the night patrol."
                a "The whole village ran out to go after the lizard, he had a tatoo plastered on his back."
                a "I can still see its revolting shape whenever I think back to that night."
                a "We nearly cornered the damn thing but it was stronger than it looked, and beat up most of us before escaping during the confusion."
                e 1 "If you know what the culprit looks like just grab him from the lizard village."
                a "You think I didn’t try? Nauxus threw a fit when I demanded he hand over the culprit."
                a "He kept lying that there was no one like that, and had the balls to throw the accusation to my tribe, and that my people had kidnapped their children."
                a "Oh, he is good, lying to my face without a shred of guilt."
                "Axel taps the end of his chair’s arm."
                a "I can’t let him get away with this, he’s putting lives in danger by protecting a mad lizard."
                a "I’ve seen families torn apart by the loss of their children."
                a "Then I thought, what if that happened to Thane, and I just… I. Argh! "
                "His left hand balls into a fist and slams down on the chair. It’s a wonder that the chair is still standing."
                a "No parent should go through something like losing a child like that."
                a "I’ll tear that blasted village apart until we find that lizard and make him pay for his crimes."
                a "No one messes with the bull tribe!"
                "His determination is set, you don’t think you can convince Axel other wise for now."
                jump Axel_tribe_talk1
            "Ask about Axel’s relationship with Thane" if Axel.s <=3:
                e 6 "You know, you could give Thane a chance to be a part of your plans."
                e 1 "I don’t even see the two of you in the same room half the time."
                "Axel scoffs."
                a "And have him lecture me on ohh, peace, love, and how I need to watch how much I eat. Pff. "
                e 1 "I really can’t see how you two are related."
                a "Well he takes after his mother."
                a "…"
                a "He nags like her, he cooks badly like her, he likes watching the village like her… he even has her eyes."
                hide axel stand with dissolve
                "Axel rests his cheek on his hand and lets out a long sigh."
                e 13 "Sounds like you miss her."
                show axel stand at center with dissolve
                a "Hmph, when do I not?"
                a "Every day he reminds me of her, and the promise she made me keep to protect him and guide him to becoming a great bull."
                a "But he and I will never understand each other. We’re too different. "
                e 1 "Maybe it’s time you give it a chance, this war’s already keeping you two apart."
                e 1 "Do you really want to lose him forever?"
                a "..."
                "The bull rests his chin on his fist, and appears to think on your words."
                jump Axel_tribe_talk1
            "Ask about what to do for fun" if Axel.s <=2:
                e 1 "There’s really not a lot to do around here. What do you bulls even do for fun?"
                a "What do you mean there’s nothing to do?"
                a "You can wrestle with the warriors, you can beat up the training dummies, you can even arm wrestle the kids if you want."
                e 9 "Why is everything on the list just som way of fighting with someone."
                a "Well, sorry princess. If you want more dainty work, you could offer to work with the shopkeeper to make some axes for sale."
                e 8 "I rather stick to wrestling then."
                a "Perfect, I was just in the mood for a good rumble. Come on."
                e 5 "What? Here? Now?"
                hide axel stand with dissolve
                "Axel gets off his throne and leaves behind cloak."
                "He stands across you, his heavy legs spread out."
                show axel stand at center with dissolve
                a "Come on Fleabag, if you can take me down, you can take on any lizards."
                "You gulp and strip off your sword."
                hide axel stand with dissolve
                "You hold your hands held in front of you, you both circle around the empty space, waiting for each other to make a move. "
                a "Hah!" with vpunch
                "Axel charges forward faster than you expect."
                "You manage to catch his hands but the weight of his body combined with his speed is too strong for you to stop."
                "You topple onto the floor, and the chief pins your face between his pecs."
                a "Yeah, come on push it harder unless you want bull stink in your face."
                "Your snout is buried under the layers of sweaty fat and muscle pinning against you."
                "You tap hard against Axel’s back, imploring him to get off."
                a "Hahahahah. What’s that? You want more of the bull? "
                "His pecs flexes and locks your snout in place."
                "You can’t move from the jaws of Axel’s cleavage."
                "You tap harder again, your cries for help are muffled by Axel’s body."
                "Worse still, you felt something hard pushing against your crotch and getting larger the more you struggle.."
                e 9 "Buhhhuh!"
                "He releases you from a minute. You gasp for air, the stench of Axel’s fur is still stuck on your nose."
                "Your respite doesn’t last long, he grabs you by the back of the head and pushes you downwards."
                "His legs swing over your shoulder his thighs flex and trap your head between them."
                e 5 "No, no, wait!"
                "Axel laughs and presses your head hard against his bulge."
                "His boner pokes you in the eye, but he pushes you down further until you’re nose deep between his balls."
                a "Yeah smell that, that’s the smell of a bull man!"
                "The pungent aroma overwhelms your senses."
                "All you can smell is Axel’s musky balls."
                "Your kicks and squirms do nothing to lessen the grip of his powerful thighs."
                "Eventually, you succumb to the tiredness and just rest your face between Axel’s balls."
                "At which point he lets go of you and leaves you lying on the ground laughing heartily as he walks away."
                "You pull yourself back up later, and collect back your sword and your composure."
                show axel stand at center with dissolve
                a "Ready for round two?"
                e 9 "No!"
                jump Axel_tribe_talk1
            "Leave" if True:
                jump Bull_tribe_tent

label Axel_bullkid:

    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Axel')
    $ renpy.music.set_volume(1, 4, channel = "Axel")

    window hide None
    stop music fadeout 1
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    scene bulltent with slow_dissolve
    "Inside, Chief Axel is scratching his chin while looking at the tent’s ceiling."
    show axel stand at center with dissolve
    e 1 "You called for me Chief Axel?"
    a "Hmm…"
    "His eyes fall on you, his hand drops onto his chest and he scratches the tuft of fur between his pecs."
    "You avert his powerful gaze."
    "It feels embarrassing the way he looks at you from top to bottom."
    a "Alright,I decided where I want to start with you."
    e 1 "...Pardon?"
    a "I’ve picked where we’re visiting today."
    a "You’re going to get a first hand experience of bull culture."
    e 6 "Bull culture? Aren’t I already experiencing it?"
    a "What by hanging around my son’s big behind every time?"
    a "I’m talking about real culture here, Fleabag. "
    a "Come on! I want to show you a special spot."
    hide axel stand at center with dissolve
    "The chief walks past you and out of the tent."
    $ renpy.music.set_volume(0, 5, channel = "Axel")
    "Mumbling under your breath you reluctantly follow Axel."
    $ renpy.music.set_pause(True, channel='Thane')
    $ renpy.music.set_volume(1, 5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
    $ renpy.music.set_pause(False, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    scene bulltribe 1 with slow_dissolve
    "He leads the way with wide strides."
    "It amazes you how a heavy set bull like him can move so fast. "
    "The two of you reach the open area right across from the general store, where two wooden bull dummies stand beside a wide empty field."
    scene tribe 1 with slow_dissolve
    show axel stand at center with dissolve
    a "Welcome to the training area."
    e 1 "Hmm, ok."
    "In the distance you can see two calves fighting each other with wooden swords."
    a "Take a look at that, makes my heart proud to know the youngins are still training."
    e 6 "Yeah, it’s good to see the kids still can have fun despite the fog."
    a "That’s what we’re all about Fleabag. Resilience."
    hide axel stand at center with dissolve
    "Axel crosses his arms and you both watch side by side as the two youths battle each other. "
    "One of them has the clearer advantage of being bigger and having longer limbs than the other. "
    "He easily dodges the smaller calves attacks."
    "The shorter one whose head barely reaches the taller one’s chest swings his weapon clumsily. "
    "His slow swings and clumsy posture are unlike a young child who just learnt to hold a weapon."
    show axel stand at center with dissolve
    a " This place used to see a whole lot more bulls training here."
    a "Everyone would try their hand to prove themselves here."
    a "If you could beat everyone you had the bragging rights to call yourself the strongest, and to challenge the chief even."
    e 1 "That sounds like you’re putting your job on the line here."
    a "It’s only fair Fleabag, to claim the title of chief you have to show everyone why they should listen to you, and the battlefield accepts all fighting styles. "
    e 1 "So, you actually beat all the bulls in the village before?"
    a "All those that would challenge my claim to the rank of chief. Thane will have to do the same someday…"
    e 1 "You think he can do it? Prove to everyone he can be chief?"
    a "…"
    hide axel stand at center with dissolve
    "The old bull looks on ahead, his eyebrows furrow while he watches the battle in front of him."
    a "I hope so. "
    "Axel shakes his head, and snorts."
    show axel stand at center with dissolve
    a "Here’s something interesting about this place, this is also where we settle most of our disagreements."
    a "You don’t like something about someone, you fight them off here."
    e 1 "Must everything be solved here with fighting?"
    "Just then you hear a loud yell."
    $ renpy.music.set_volume(0.8, 5, channel = "Chan1")
    hide axel stand at center with dissolve
    "Small calf" "I WILL KILL YOU!!"
    show black2
    show bullkid01 at center with dissolve
    "The two calves from earlier are now rolling on the floor."
    "Dust is floating everywhere as the shorter calf relentlessly tries to pound the bigger calf in the face."
    e 9 "Woah, what the heck, we got to stop them. "
    "You rush over to the two calves but Axel stops you by pulling you by the arm."
    a "Just let them fight, that’s how boys settle their problems around here."
    e 12 "Not like this, they’re going to kill each other. Now let's go!"
    "Axel releases his hold and rolls his eyes as he follows you towards the duo."
    hide bullkid01 with dissolve
    hide black2 with dissolve
    "You manage to grab the smaller calf by the armpits and pull him off the other one."
    "Small calf" "I’m going to kill you!"
    "It takes a lot of energy out of you to drag the calf away as he thrashes about."
    "Axel helps the other calf up on his feet."
    "The teenage bull pulls himself up and calmly brushes the dirt off of his face."
    "Small calf" "Die! Just die you stupid jerk!"
    show axel stand at center with dissolve
    a "What’s all this about?"
    "Teenage calf" "Chief Axel, I-I’m sorry for the trouble."
    "Teenage calf" "My little brother is just being a brat."
    "Small calf" "You shut up!" with vpunch
    "Small calf" "Tell him the truth! You horrible, terrible, ass fart!"
    e 5 "Woah, calm down kid."
    "Small calf" "Let me go! He needs to pay for what he did!"
    "Teenage calf" "Oh, quit being so dramatic. I apologized for it already."
    "Teenage calf" "Why can’t you let it go."
    "Small calf" "You know why!"
    "Small calf" "You killed what’s left of mommy! Murderer!"
    a "Enough! Get your tails in line!" with vpunch
    hide axel stand at center with dissolve
    "Chief Axel’s booming voice silences the arguing siblings."
    "Finally, you can let go of the smaller calf."
    "The two young boys lined up in front of Axel."
    "The smaller calf sniffles loudly, fighting back his tears."
    "His shoulders won’t stop trembling. "
    show axel stand at center with dissolve
    a "You, the big brother, explain what’s going on."
    "Taller calf" "My little brother is upset that I broke his toy yesterday by accident."
    "Small calf" "You lie!" with vpunch
    "Small calf" "You did it on purpose, you hated mommy, and wanted to break what she left to me!"
    "Taller calf" "I did not! It was an accident, I didn’t see where you stu- where your toy was!"
    hide axel stand at center with dissolve
    e 9 "Was that toy really important? Can’t your parents replace it?"
    "Small calf" "Mommy’s gone. She left daddy, and left the tribe."
    "The small calf sobs loudly, he doesn’t try to hide his sadness anymore."
    "Small calf" "You always hated her. It’s not fair!"
    "Small calf" "You broke mommy’s gift to me. I hate you! "
    "Taller calf" "What’s it going to take for you to forgive me? If I could have fixed it I would have."
    "Taller calf" "Look we’re causing a lot of trouble to the chief as is."
    "Taller calf" "Quit being such a whiny calf!"
    "Small calf" "Shut up! I don’t want to see you anymore, I hate you, I hate you!"
    show axel stand at center with dissolve
    a "Quiet! I’ve heard enough."
    "The two calves freeze in their spot and look to the chief with frightened eyes."
    a "You, the older brother, I hear you are responsible for breaking your little brother’s prized possession."
    a "Am I right?"
    "Taller calf" "I.. did."
    $ renpy.music.set_volume(0.3, 5, channel = "Chan1")
    a "Then it’s decided, the only way to solve this is for your little brother to exact his vengeance."
    a "As you’ve said little one, he is your brother no more."
    a "I hereby decree a final battle."
    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    e 5 "What final battle? You want them to kill each other?"
    $ renpy.music.set_volume(0.3, 10, channel = "Axel")
    a "No, the small one, you will strike your older brother down, and in doing so ends your ties with him, you two will be brothers no more!"
    e 9 "Just hold it, that’s way too drastic."
    a "Quiet, Fleabag. You wanted an intervention, you got one."
    a "My word is law. Now ready yourselves!"
    "The two smaller bulls look at each other with trepidation."
    "Reluctantly, the taller bull turns to face his sibling. "
    "His little brother looks to the ground with clenched fists and his tears falling to the ground."
    hide axel stand at center with dissolve
    "Axel twists his head to his side, signaling to you to come over."
    "You obey, but you give Axel a long and dark stare, questioning his judgement."
    "The stage falls silent as all eyes are on the two children."
    "Uneasiness fills the pit of your stomach."
    "Small calf" "Yaargh!"
    "The small calf rushes forward his arms in the air, then he throws his punch."
    "Like the wind the punch flies so quickly you can’t catch sight of it."
    $ renpy.music.set_volume(0, 3, channel = "Axel")
    "His big brother flinches and closes his eyes."
    pause 3
    "Everything ends in a blink of an eye. "
    "The little brother’s fist hangs in mid-air just inches away from his big brother’s snout. "
    "His cries cut through the silence, he tries to muster something to say, but all you hear are tears, and the sniffling of a sad child."
    $ renpy.music.set_volume(1, 10, channel = "Axel")
    "Small calf" "I’m sorry… "
    "He sobs."
    "Small calf" "Don’t take my big brother away…"
    "Small calf" "I don’t want to lose anyone anymore."
    "The taller calf opens his eyes and slowly pulls his brother close, letting him cry into fur."
    "Taller calf" "Forgive us chief, for the trouble we caused."
    "Small calf" "I’m sorry…"
    show axel stand at center with dissolve
    a "Tell me, what was the broken toy?"
    "Taller calf" "A small bow our mother made, she gave it to him before she left."
    "Taller calf" "I could fix it with some materials but I don’t have the coins to buy them."
    a "Then take this."
    hide axel stand at center with dissolve
    "Axel hands the older brother a bag of coins."
    show axel stand at center with dissolve
    a "There should be enough there to patch up the bow and to get you two a small snack to share. "
    "Taller calf" "Thank you Chief Axel. Hey, go on, say thanks."
    "Small calf" "Thank you, Chief Axel."
    "The small calf’s eyes are red from all the crying, and his voice is hoarse. "
    "Axel kneels down and wipes the small calf’s face with his cape."
    hide axel stand at center with dissolve
    a "You’re welcome little one. You did a good thing today giving your brother a chance."
    a "That kind of strength at such a young age, I think you’ll go far."
    a "Promise me you’ll try to be kinder to each other."
    "Small calf" "I promise."
    show axel stand at center with dissolve
    a "Good, now go on you two. I’ve got a tour to finish with our friend Brother Fleabag here."
    "Taller calf" "Good bye Chief Axel, Brother Fleabag."
    "Small calf" "Good bye Chief Axel and Brother Fleabag."
    e 8 "Ah."
    hide axel stand at center with dissolve
    "As the children leave, Axel laughs heartily while smacking you in the back three times, you almost fall over from his strong slap."
    "He then leads the way back to his tent, and you follow from behind."
    scene bulltribe 1 with slow_dissolve
    e 1 "Did you know the little brother wouldn’t hit his big brother?"
    a "Like I said the training grounds is where disputes are handled."
    a "All I did was give them a little push in the right direction."
    "Axel throws you a cocky grin."
    e 1 "Your methods are… risky."
    a "Yeah well it gets the job done."
    a "Sometimes you need tough love to get people to be honest about their feelings. "
    a "Action speaks louder than words, that’s something you got to remember Fleabag. "
    e 13 "I’ll keep that in mind. It was nice of you to pay for the calves to fix the toy."
    a "Don’t go spreading it around Fleabag, last thing I need is for my men to think I have gold to give around like leaves. "
    "While Axel walks up ahead, you become aware of his broad back, and you start to see the shadow of a father that the chief is."
    "You wonder if he sees the village as his child as well, and the way he rules is like a father showing his tough love."
    scene tent 1 with slow_dissolve
    show axel stand at center with dissolve
    "The moment you both reach the top of the steps. Axel turns to you with arms crossed."
    a "Alright, that’s the end of the tour for today. Check up with me to see if I’m free for another tour."
    e 1 "I look forward to it."
    a "You better, damn stairs make my thighs burn."
    hide axel stand at center with dissolve
    scene black with slow_dissolve
    "You bow and the bovian chief takes his leave into his tent."
    "<[name] gained one Level-up-point.>"
    $ Zalt.points = Zalt.points +1
    $ Time.hours = Time.hours + 2
    jump Bull_tribe_map

label Axel_letter:
    if Quest.bomba == 1:
        e 1 "Chief Axel."
        show axel stand at center with dissolve
        a "You have some balls to keep me waiting Fleabag."
        e 13 "Right..."
        a "Let's get down to brass tacks."
        a "I have a message that needs to be sent to the lizards. One that can only be sent via a catapult."
        e 1 "A catapult?"
        a "Yes, making weapons is our tribe’s specialty. We scraped what limited materials we could to make it."
        e 1 "I don’t get what kind of message you can send with a catapult?"
        hide axel stand at center with dissolve
        a "They will understand everything, with this."
        show bullbomb at center with slow_dissolve
        "He pulls out from behind his seat what looks like a crudely made spherical bomb wrapped in some kind of paper material, its fuse sticks right up."
        hide bullbomb at center with dissolve
        show axel stand at center with dissolve
        a "Your job is simple, take the bomb to the catapult that’s already set up at the swamp."
        a "One of my men who’s been scouting the area knows the proper trajectory for the bomb to hit their ceremonial stage."
        e 5 "If you needed someone to just deliver something for you I’m sure you have many other options besides me."
        a "You’re a better choice. Faster, smaller, there would be less risk of you getting caught by the lizards."
        e 13 "Still, this is a dangerous move, innocent people could get hurt."
        a "It won't, I know of their ceremonial stage, it is mostly unguarded."
        a "And even if a few lizards are lost that works in our favour."
        hide axel stand at center with dissolve
        "Axel crosses his arms and locks eyes with you. "
        show axel stand at center with dissolve
        a "The lizards brought this upon themselves."
        a "They should consider themselves lucky that they even get a warning shot."
        a "The longer I delay, my men will think I am unfit to lead them in this war."
        a "The lizards already had an upper hand when they sent their spy."
        e 5 "Wait, did the spy take something important?"
        a "It’s not what the spy took, it’s what they left."
        a "It was also Nauxus’s way of saying he could have me killed anytime, and I refuse to have him have the satisfaction thinking I am just a bug dancing on the palm of his hands."
        e 1 "…"
        e 13 "I will need some time to think it over."
        if Quest.campw1 == 4:
            a "Really? After all I just said you’re leaving me with a maybe?"
            a "If Tomahawk was still around I could rely on him to do this."
            a "If you won’t do this job out of respect for me, at least have the decency to respect the dead who you abandoned. "
            a "Now out!"
        elif True:
            a "Really? I just gave a long winded explanation and you’re leaving me with a maybe?"
            a "Tsk, if only Tomahawk isn’t recovering from his freak blow to the head, I could have him do this job, at least he doesn’t need so much convincing."
            a "Now out!"

        hide axel stand at center with dissolve
        "You gulp and leave the tent."
        $ renpy.music.set_pause(True, channel='Thane')
        $ renpy.music.set_pause(True, channel='Axel')
        scene black with dissolve
        "..."
        if Time.hours >= 6 and Time.hours <= 17:
            scene bulltribe 1 with vslow_dissolve
        elif True:
            scene bulltribe 1n with vslow_dissolve

        $ Quest.bomba = 2
        if Quest.bombn == 1:
            e 13 "(So Chief Axel plans to launch an attack on the lizard tribe using a catapult and a bomb."
            e 1 "(Do I want to go through with it?)"
            e 1 "No wait, I need to find out what Nauxus wants first."
        elif True:
            e 13 "Great, so I have one chief that wants to bomb a village, and the other wants to recruit more lizards for his army."
            e 1 "(Do I pick a side or see Thane for his advice?)"
            $ Quest.bombt = 1
            $ Quest.bomb = 2
        jump Bull_tribe_map


    elif Quest.bomba == 2 and Quest.bombn == 2 and Quest.bomb == 2:
        show axel stand at center with dissolve
        a "You ready to send this bomb to those bloody lizards?"
        if Quest.bombt != 3:
            "{b}{color=#ffd65c}<Warning:{p} You can't change your option anymore after this option.>{/color}"
        menu:
            "Yes" if True:
                e 1 "I’m ready."
                $ jane_inv_K.take(real_bomb)
                show bullbomb at center with slow_dissolve
                "Axel hands you the bomb."
                hide bullbomb at center with slow_dissolve
                a "Meet my man at the entrance to the lizard tribe, it’s the swampy area before you enter their village. He knows to expect a delivery."
                a "He’ll hand you your reward as well. Don’t damage the bomb, it’s the only one we are able to make."
                e 1 "Alright. I just need to give the bull the bomb, and I’m done."
                $ Quest.bomba = 3
                $ Quest.bomb = 3
                if Quest.bombt == 3:
                    hide axel stand at center with dissolve
                    scene bulltribe 1 with slow_dissolve
                    "You leave the tent and casually make your way out of the village."
                    stop Axel
                    scene forest 3 with slow_dissolve
                    show bullbomb at left with slow_dissolve
                    show bullbomb2 at right with slow_dissolve
                    "You make sure that you recognize which is the original bomb in your satchel."
                    hide bullbomb2 with slow_dissolve
                    show bullbomb at center with slow_dissolve
                    "Once you are at a decent distance from the bull village and that no one is around you pull out the original bomb."
                    "With your claws you rip through its shell and let loose the explosive powder inside."
                    hide bullbomb at center with slow_dissolve
                    "As long as the powder is not contained in a small space, it should do no harm."
                    "You then rip apart the bomb’s outer body and scatter its ripped remains among the trees."
                    "Now all that’s left is to head to the swamp."
                    $ jane_inv_K.drop(real_bomb)
                    jump forest_map
                elif True:
                    hide axel stand at center with dissolve
                    jump Bull_tribe_tent
            "No" if True:
                e 13 "Not yet, I’m still preparing."
                a "Then don’t waste my time standing here."
                jump Bull_tribe_tent
    elif Quest.bomba == 3 and Quest.bombn == 2 and Quest.bomb == 3:
        a "Get your tail into gear and deliver that bomb to the swamp! Don’t make me tell you again!"
        jump Bull_tribe_tent
    elif Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bomb_bull ==2:
        $ Axel.talktree = 1
        if Quest.bomb_lizard == 3:
            $ Time.bomb = Time.days
        $ Quest.bomb_bull =3
        if Quest.bomb_result == Axel:
            a "I have good news Fleabag."
            a "The bomb hit its target."
            a "Those lizards will probably think twice before they try to make a move on us."
            e 13 "I was just doing my duty, Chief Axel."
            a "Now I’m in the mood to celebrate!"
            e 1 "What do you have in mind?"
            a "The Feast of Fire will come soon. It’ll be the perfect time to rouse the spirits of the bulls."
            e 1 "I’m not familiar with that festival. "
            a "It’s what our people have been doing since the ancient days."
            a "We eat, drink and dance the night away to give thanks to our ancestors."
            e 6 "It sounds like fun, what do you guys usually do?"
            a "Typical celebration stuff, we sing songs from our forefathers and usually the women and children would put on a nice stage show."
            a "You’ll like it. All I have to do is make sure we have enough resources for it."
            a "I’ll call you if we need any help."
            "He leans back against his seat."
            a "Now, I still have some time to kill. Do you need anything Fleabag?"
            jump Axel_tribe_talk1
        elif Quest.bomb_result == Nauxus:
            $ Time.aaxel = Time.days
            if Time.hours >= 6 and Time.hours <= 17:
                scene tribe 1 with vslow_dissolve
            elif True:
                scene tribe 1n with vslow_dissolve
            "You head for the chief’s tent wondering what happened to his plans to attack the lizard village. "
            if Time.hours >= 6 and Time.hours <= 17:
                scene tent 1 with vslow_dissolve
            elif True:
                scene tent 1n with vslow_dissolve
            "Strangely the guards who are usually outside of the tent are nowhere to be found."
            "The moment your hand touches the tent’s door you hear Axel shouting!"
            a "What kind of an imbecile are you?" with vpunch
            a "Don’t you realize how much trouble you got yourself into?"
            a "You’re a fucking traitor now!"
            a "Do you think it’s easy to cover this up?"
            t "I don’t need you to cover anything up!"
            t "I did what I had to do, to stop you from crossing over into becoming a tyrant!"
            a "Why are you being so difficult? This is a war!"
            a "I’m doing what it takes to keep you and the village safe!"
            a "That bomb was a calculated attack, it was just to scare them off our backs!"
            t "You don’t know it would have worked!"
            t "And if I didn’t stop you now, you’re just going to escalate, and escalate!"
            a "Enough! You can plant your ungrateful ass on your rock and sit there until all of this is over! "
            t "I’m a grown bull, you can’t ground me!"
            a "Just watch me, I am chief, my word is law! Thane, as of now your tools will be confiscated and locked away. "
            a "And I’ll make sure if you so much as move from your rock I will come down hard on you like a thunderstorm!"
            t "This isn’t over!"
            show thane stand at center with dissolve
            "Thane suddenly bursts out from the tent forcing you to the side."
            hide thane stand at center with dissolve
            "He doesn’t even notice your presence."
            a "Thane!" with vpunch
            "He ignores his father’s call from the tent and continues walking down the lengthy steps. "
            "You poke your head through the tent’s entrance only to have Axel throw a heavy axe that narrowly misses your head."
            a "Get out!" with vpunch
            "You regret doing that."
            "Best to come back at a later time to talk to Axel and Thane."
            jump Bull_tribe_map0
        elif Quest.bomb_result == Thane:
            $ Time.aaxel = Time.days
            if Time.hours >= 6 and Time.hours <= 17:
                scene tribe 1 with vslow_dissolve
            elif True:
                scene tribe 1n with vslow_dissolve
            "Before you can head over to your meeting spot, a bull warrior stops you."
            "Bull warrior" "Hold it. The chief wants a word with you."
            e 6 "Can’t he wait? I have a meeting with Thane."
            "Bull warrior" "More reason for you to come along. Thane’s with him too."
            "You feel queasy in the stomach. This does not sound good for you or Thane."
            "You follow the warrior to the chief’s tent."
            scene bulltent with vslow_dissolve
            show thane stand1 at left with dissolve
            show axel stand at right with dissolve
            "Thane stands with his hands behind his back while he faces his father."
            "The chief eyes you with the same angry look Nauxus gave you earlier."
            e 1 "Chief Axel."
            a "…"
            hide axel stand at right with dissolve
            "He stands up and passes through you and Thane."
            "Poking his head out through the tent, you can hear him telling the guards outside to have an early break."
            show axel stand at right with dissolve
            a "So, I am not sure if you heard, but the bomb you delivered failed to go off."
            a "Instead, the scout heard sneezing in the distance."
            a "Know anything about that, Fleabag?"
            e 1 "I can’t say. I just dropped the bomb off, the bull checked it and I left."
            a "Really? You didn’t stop anywhere and maybe switched the bombs?"
            e 1 "No."
            "You try to deny it as convincingly as you can."
            "Axel strokes his chin and looks at you suspiciously."
            t "Where’s your proof? If you’re going to accuse people of things, you better have evidence."
            a "Proof?" with vpunch
            "Axel slams his fist on his armchair."
            a "You want proof? I was there when the bomb was made!"
            a "And I am bloody sure I didn’t put sneezing powder in it!"
            "Axel points accusingly at Thane."
            a "There’s only one bull in the whole village that I know who has the skills to make a decoy fast enough. "
            t "…"
            "Axel stands up, and approaches Thane who evades his gaze."
            a "Son, tell me you didn’t have something to do with this."
            t "…"
            a "Thane!"
            e 5 "He didn’t do anything. The bomb was just a dud!"
            t "No, I did it. I switched the bomb when [name] wasn’t looking."
            e 5 "Thane!"
            "The chief’s son looks at you and shakes his head."
            a "You're lying, he put you up to this didn't he?"
            "Axel points at you."
            t "No, ask me a million times and the answer will still stay the same."
            "You stand in shocked silence."
            hide thane stand1 at left with dissolve
            hide axel stand at right with dissolve
            "Thane's father grabs him by the shoulders and shakes him."
            "His nostrils flare up and his eyes bulge out intensly. "
            a "You take it back! Don't you know what you're saying?"
            "Thane pushes his father back with a huff and angrily points at him."
            show thane stand1 at left with dissolve
            show axel stand at right with dissolve
            t "No, never! I couldn't let you go through with your plans. You were going to kill innocent civilians with that thing!"
            a "You foolish calf! I planned everything from the start."
            a "That bomb was supposed to just hit their ceremonial stage, and the only casualties would have been the guards there!"
            t "You don’t know that!"
            t "It still could have hurt innocent bystanders!"
            t "How can you leave something so important to chance?"
            t "What kind of a chief are you?"
            a "Enough Thane! This is beyond selfish even for you!"
            a "Have you no consideration for the lengths I have to go through to keep this under wraps?"
            a "You’re putting yourself in grave danger. If anyone else finds out it’s punishable by banishment!"
            t "I don’t need your protection, father! I don’t need your protection!"
            t "I need you to listen to reason! Stop this pointless war!"
            "Axel clenches his fists and his face flushes red."
            t "I am doing what's right to protect the peace!"
            t "Something you never even tried to do! What kind of a chief does that?"
            "Axel snorts and stomps his hoof against the ground."
            "Thane doesn’t flinch and stands his ground against his father."
            a "Enough of this! We are done talking about this! The bomb was a dud, end of story!"
            "The chief turns to you, his eyes burn with anger and his fists look ready to strike."
            "You hold your breath fearing he will try to silence you after what you’ve heard."
            a "What did I say happened to the bomb mission Fleabag?"
            e 9 "The- the bomb was a dud. Nothing more."
            "Good, and if you so much as breathe a word about what happened here. "
            "Axel cracks his knuckles."
            a "Your head won’t leave this tent."
            "You gulp and nervously nod."
            t "Stop threatening my friend!"
            a " Don’t think you’re out of the woods either boy."
            a "As of now, all of your tools are confiscated, and I will keep a close eye on you."
            a "You so much as sneeze out of line, I’ll send you to the temple until you’re my age!"
            "Thane’s entire body trembles."
            "You can see him gritting his teeth, trying to hold back his tears."
            "You could only imagine what he might be feeling right now."
            t "Then do it! You’ll be happy right?"
            t "Keeping me aside like I’m never there!"
            t "That way you won’t have to look at your pathetic excuse of a son!"
            a "I didn’t say that!"
            t "You didn’t have to!"
            hide thane stand1 at left with dissolve
            "Thane turns away and leaves the tent."
            a "Thane. THANE!"
            hide axel stand at right with dissolve
            "Axel angrily grabs his own horns and lets out a loud grunt."
            "You decide to follow Thane and see if he’s alright."
            jump Thane_tribe_talk
    elif True:
        "U see this mean it's a bug"
        jump Bull_tribe_tent

label Axel_bomb_done:
    if Quest.bombt == 3:
        "As you trudge through the swamp, you’re unsure where exactly you’re supposed to find this bull."
        "Suddenly, a figure emerges from among the mangrove trees. It’s a bull warrior!"
        "Catapult Bull" "Hey, Brother Fleabag. I was told to expect you."
        e 1 "Umm… yeah. Where’s the catapult?"
        "Catapult Bull" "It’s in position. Had to hide it under some leaves and vines."
        "Catapult Bull" "Now give me the bomb, I’ve been here for so long the mosquitoes are having a buffet with my blood."
        show bullbomb2 at center with slow_dissolve
        "You hand the bull the fake bomb."
        hide bullbomb2 with slow_dissolve
        "He holds it close to his snout and eyes it suspiciously."
        "The fur on your back stands up on end. Will he figure out the bomb is a fake?"
        "The bull brings it close to his snout and sniffs it around."
        "Your heart rate starts beating uncomfortably fast."
        "The palms of your hands begin to sweat."
        "His eyes now fall on you."
        "He approaches, closer and closer."
        "And he pulls out a bag of coins."
        "Catapult Bull" "Here, your payment as Chief Axel instructed."
        e 5 "Oh… ok."
        "<[name] gained 250 coins>"
        $ jane_inv.take(coin,250)
        "Catapult Bull" "Yup, now get out of here. I have work to do."
        e 1 "Alright then."
        "You pretend to head off, wiping away your foot prints as you go."
        "Once you’re sure he cannot see you, you leap into the trees. "
        "Staying hidden up above, you follow the bull from behind until he leads you to the catapult."
        "You lay in wait...watching. "
        "The bull arrives at a pile of leaves and vines."
        "He removes them all to reveal a catapult built with random pieces of items from the bull tribe."
        "He places the bomb on the catapult and pulls out a pair of flint and steel."
        "With his tools, he ignites the bomb. The fuse starts burning."
        "He pulls the lever and the catapult launches the bomb into the air. "
        "As the bomb flies, the catapult crumbles away."
        "The bull watches for a few minutes."
        $ jane_inv_K.drop(fake_bomb)
        play sound "music/bomb-small.mp3"
        "A soft pop sound can be heard in the distance, followed by people sneezing."
        "Catapult Bull" "Damn, was that bomb a dud? Chief Axel will not like this."
        "Satisfied that the plan worked, you sneak away and head over to meet Nauxus."
        $ Quest.bombt = 4
        $ Quest.bomba = 4
        jump forest_map
    elif True:
        "As you trudge through the swamp, you’re unsure where exactly you’re supposed to find this bull."
        "Suddenly, a figure emerges from among the mangrove trees. It’s a bull warrior!"
        "Catapult Bull" "Hey, Brother Fleabag. I was told to expect you."
        e 1 "Umm… yeah. Where’s the catapult?"
        "Catapult Bull" "It’s in position. Had to hide it under some leaves and vines."
        "Catapult Bull" "Now give me the bomb, I’ve been here for so long the mosquitoes are having a buffet with my blood."
        show bullbomb at center with slow_dissolve
        "You hand the bull the bomb."
        hide bullbomb with slow_dissolve
        "He sniffs and knocks the bomb as though to inspect it."
        "Catapult Bull" "Alright, looks good."
        "Catapult Bull" "You might not want to be here when this thing is lit, this rudimentary catapult might just break and then we both might lose a limb or two."
        e 13 "Alright, then… Axel mentioned something about collecting my reward from you?"
        "Catapult Bull" "Oh yeah, here."
        "<[name] gained 400 coins>"
        "<[name] gained one Level-up-point.>"
        stop music fadeout 2
        $ jane_inv.take(coin,400)
        $ Zalt.points = Zalt.points +1
        scene black with slow_dissolve
        stop Chan1
        stop Chan2
        "You take your reward, and walk away."
        "You’re careful to distort your footprints left behind on the muddy ground."
        play sound "music/bomb-big.ogg"
        "As you make your way to the entrance of the swamp you hear a loud explosion from behind you, followed by harrowing screams."
        "You hesitate to turn back… but you don’t."
        "Clutching your fists you continue walking."
        "The job is done."
        $ Quest.bombt =5
        $ jane_inv_K.drop(real_bomb)
        $ Quest.bomb_end = 0
        $ Quest.bomba = 4
        $ Quest.bomb_lizard= 2
        $ Quest.bomb_bull= 2
        $ Quest.bomb = 5
        $ Quest.bomb_result = Axel
        $ Nauxus.s = Nauxus.s + 3

        jump forest_map0

label Axel_festival:
    if Quest.fesa ==1:
        "As you approach the tent, you see a female bull talking to Axel."
        "She appears distraught with her unkempt hair and a frantic look in her eyes."
        "Female Bull" "It took everything from the storage unit. We have no food for the festival!"
        a "Was it a lizard?"
        "Female Bull" "No, I don’t think so. Look at this bite mark."
        "She hands Axel something that fits in the palm of the chief’s hand. "
        "The chief holds up a half eaten apple and observes it from every angle."
        a "Did it leave a trail? "
        "Female Bull" "There’s a line of dropped fruits every few steps."
        a "Make sure nobody touches the crime scene."
        a "I'll get someone on it."
        "Axel then turns to you."
        show axel stand at center with dissolve
        a "Fleabag, I hope you’re not making a habit of eavesdropping on people’s conversations."
        e 9 "Never Chief Axel. It was just a coincidence. "
        a "Hpmh, that aside, as you might have overheard, something has stolen the fruits we gathered for the Feast of Fire."
        a "Now I can't imagine something more in the spirit of the festival than you bringing back those stolen delights."
        e 5 "I won’t hold my breath for all of the food to be returned though."
        e 5 "If it’s something that can take all of the fruits that was to feed an entire village."
        e 5 "Then it’s either really big or there’s going to be an army of them."
        a "Use your wits Fleabag, I’d spare you my men but there’s too much to do before the Festival can begin."
        a "Not to mention the amount of damage control that needs to be done."
        a "The kids have been looking forward to the celebration for so long."
        a "I’ll try to hold off on the ceremony until you show up with the fruits. "
        a "Are you ready to take the job? Time is of the essence."
        label Axel_festival_start:
            menu:
                "Yes" if True:
                    e 1 "I’m on it."
                    a "Good, then meet the shopkeeper and tell him I sent you."
                    a "He’ll give you a sack to help carry back the fruits. "
                    a "You’re looking for around 500 pieces of fruit."
                    a "Also,dispose of this while you’re at it."
                    "He hands you the half eaten apple."
                    e 1 "Oh…"
                    e 1 "I’ll hang on to it, in case I have trouble tracking the criminal."
                    a "One last thing before you go… it’s about Thane."
                    if Thane.movein == 0:
                        "Axel hans you a note."
                        "{u}{i}Gone out to hunt. Don’t wait for me.\n——Thane{/i}{/u}"
                        a "We found the note on his rock."
                        a "Did you see him on your way here?"
                        e 1 "Err… no. "
                        a "Hmm, so my ever defiant son wants to skip out on the festival."
                        a "He has no idea how disgraceful this will look with his seat empty."
                        e 1 "Maybe he needs some space after all that’s happened."
                        "Axel crosses his arms."
                        a "Well he can be in a ditch for all I care."
                        a "If he’s going to act like a brat, then it’s better he stays away."
                        a "Now go deal with the fruit thief."
                        "You bow with deference and take your leave."
                    elif True:
                        a "Did he say anything about coming back for the festival?"
                        e 6 "Coming back? I’m not sure I know what you mean Chief Axel."
                        a "Don’t play dumb, I know he’s staying in the tavern."
                        a "I have my sources."
                        e 1 "… Fine, he’s in the tavern and no, he didn’t mention anything about coming back."
                        a "Utterly irresponsible. He has no idea how disgraceful this will be with his seat empty during the ceremony."
                        e 13 "Maybe give him some space, a lot has happened recently."
                        a "He can have all the space he wants."
                        a "He’ll come crawling back once he learns he cannot survive out there without the tribe’s help."
                        a "Now go, this conversation has left a sour taste in my mouth."
                        e 1 "Yes Chief Axel."
                    hide axel stand at center with dissolve
                    $ Quest.fesa = 3
                    if Quest.fesn == 3:
                        scene tribe 1 with slow_dissolve
                        $ renpy.music.set_pause(True, channel='Axel')
                        e 13 "Both villages have been hit by the fruit thief."
                        e 13 "The timing is way too perfect to be coincidental."
                        e 1 "Not to mention…"
                        "You pull out the half eaten fruits you got from both villages."
                        e 1 "The bite marks on these two fruits are identical."
                        e 13 "So, I’m just dealing with one monster. "
                        e 1 "Any path I take to track down the creature won’t matter then."
                        jump Bull_tribe_map0
                    jump Bull_tribe_tent
                "No" if True:
                    e 6 "I still have something to deal with first. "
                    a "Move your ass Fleabag. This festival needs those fruits."
                    $ Quest.fesa = 2
                    hide axel stand at center with dissolve
                    jump Bull_tribe_tent
    elif Quest.fesa ==2:
        show axel stand at center with dissolve
        a "Don’t waste my time, are you going to help find those fruits or not?"
        jump Axel_festival_start
    elif Quest.fesa >=3 and Quest.fesa <=5:
        hide axel stand with dissolve
        "Axel is busy managing the tasks for the festival, he has no time to talk to you."
        jump Bull_tribe_tent
    elif True:
        jump Bull_tribe_tent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
