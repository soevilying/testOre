label Thane_meet:
    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ Time.mins = Time.mins +5
    if Time.hours >= 6 and Time.hours <= 17:
        scene forest 3 with slow_dissolve
    elif True:
        scene forest 3n with slow_dissolve
    "You rush over to the bull leaning against the tree."
    "He tries to pull himself up but he slouches back in pain the moment his right foot makes contact with the ground."
    e 1 "Don’t move."
    "You use bind up to heal the wound."
    $ renpy.music.set_pause(False, channel='Thane')
    $ renpy.music.set_volume(1, 4, channel = "Thane")
    "After a few seconds he manages to stand back up with ease."
    "He stands upright with a confident, and regal composure."
    show thane stand at center with dissolve

    "Bull" "Thank you outsider, for saving my life."
    t "I am Thane of the Bull tribe."
    e 1 " I’m [name] of the... tavern?"
    t "The tavern, I’ve heard of that place."
    t "My tribe has traded with outsiders from the tavern before."
    t "That was until the fog blocked the way there."
    if Foe.bullab >= 3:
        e 9 "I’m surprised your tribe is willing to talk to outsiders."
        e 13 "My experience at your camp says you’d rather crush them."
        t "That is not true of all of us bulls."
        t "Things have been happening at the camp that has everyone on their toes, more so than usual."
    elif True:
        e 5 "You have traded before?"
        e 5 "I didn’t even know there were others living out in this forest."
        t "We’ve always lived here, even during the time of the first chief."
        t "But since the fog came my tribe has become fearful of even what lies within our borders."
        t "Also, I would advise you outsider to stay away from the tribe, for your sake."
        t "My brothers, if they spot any who are not aligned with the tribe will attack without hesitation."
    t "Ok, I better get to work."
    t "Thanks for your help."
    t "If you need anything find me under this tree."
    "I think I want to bring back some fruits for my brothers, so I will be here for a while."
    e 1 "Is your leg ok?"
    t "Yeah don't worry. There shouldn't be any monsters around for now."
    t "Even if there were I can handle them."
    "The bull waves goodbye to you, and leaves."
    $ Thane.meet = 1


    jump forest_map_3
label Thane_talk:

    $ Time.mins = Time.mins +5
    show thane stand at center with dissolve
    menu:
        "Asks how he injured his leg" if Thane.quest <= 4:
            e 1 "How’d you break your leg?"
            t "Funny story, I woke up and noticed the fog had cleared a bit,{p}and the old path towards your tavern revealed itself."
            t "My brothers dared not approach the path fearing it was a trap."
            t "So, I volunteered to investigate."
            t "As I journeyed through the path I noticed that my..."
            t "That my... stomach was rumbling."
            t "So I went to this tree that I knew from young, bore delicious fruits."
            t "I would always climb this tree with my brother when I was younger."
            t "Then... errr... I forgot I’m heavier than when I was a calf..."
            t "So the branch broke and that’s how I broke my leg."
            e 13 "Pff... you broke it with your big butt."
            t "I did not! The tree is old, and this is muscle!"
            e 3 "Ok, I believe you."
            "You do not believe him."
            "Thane rolls his eyes at you."
            jump Thane_talk
        "Ask how to get into the tribe camp" if Thane.quest == 0:
            e 1 "So, how do I get into the bull tribe camp safely?"
            t "There are several steps."
            t "First, you need someone from the tribe to vouch for you, to indicate that you are trustworthy."
            t "Second, you will need to pass through the trials set by the Chief."
            t "Pass them, and you will be declared as one of us."
            e 13 "Sounds easy enough."
            e 1 "Would you be able to vouch for me?"
            t "That depends, how do I know I can trust you?"
            e 9 "I saved your life?"
            t "Well yes, but I need to know if you will be able to follow our laws, and obey our leader."
            t "I will test you."
            t "Your test is to bring me 5 pieces of jerky, and 2 beers."
            e 1 "Why? You know what, never mind."
            e 1 "I'll be back before you know it."
            $ Thane.quest = 1
            jump Thane_talk
        "Give jerky and beers to Thane" if Thane.quest == 1:
            if Parif.witer_first != 0:
                if jane_inv.qty(beer) >= 2 and jane_inv.qty(jerky_p) >= 5:
                    $ jane_inv.drop(beer,2)
                    $ jane_inv.drop(jerky_p,5)
                    $ Thane.quest = 2
                    t "Excellent, you completed your task."
                    e 1 "What exactly is the purpose of these things?"
                    t "Well,it's been a while since I got to try the meals you outsiders make."
                    e 5 "What?"
                    t "Nothing, I just figured what better way to know if I can trust you than by sharing a meal with you."
                    hide thane stand with dissolve
                    "The two of you sit down to share the meal you brought."
                    "You share with Thane about your experience in the tavern and what you know so far about the fog."
                    "With your meal done, Thane announces that he will follow you to the tribe and vouch for you."
                    "Thane trusts you now."
                    "<[name] gains 300 EXP>"
                    $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                    jump Thane_talk
                elif True:
                    t "Remember, I just need 5 pieces of jerky and 2 beers."
                    jump Thane_talk
            elif True:
                if jane_inv.qty(beer) >= 2 and jane_inv.qty(jerky) >= 5:
                    $ jane_inv.drop(beer,2)
                    $ jane_inv.drop(jerky,5)
                    $ Thane.quest = 2
                    t "Excellent, you completed your task."
                    e 1 "What exactly is the purpose of these things?"
                    t "Well,it's been a while since I got to try the meals you outsiders make."
                    e 5 "What?"
                    t "Nothing, I just figured what better way to know if I can trust you than by sharing a meal with you."
                    hide thane stand with dissolve
                    "The two of you sit down to share the meal you brought."
                    "You share with Thane about your experience in the tavern and what you know so far about the fog."
                    "With your meal done, Thane announces that he will follow you to the tribe and vouch for you."
                    "Thane trusts you now."
                    "<[name] gains 300 EXP>"
                    $ Zalt.exp = min(Zalt.exp+300, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                    jump Thane_talk
                elif True:
                    t "Remember, I just need 5 pieces of jerky and 2 beers."
                    jump Thane_talk
        "Going to the bull tribe." if Thane.quest == 2:
            if Time.hours >= 6 and Time.hours <= 17:
                e 1 "Thane? You ready to head out?"
                t "..."
                e 1 "What’s wrong? You look worried."
                t " Nothing, I’m just thinking about what the chief will test you with."
                e 1 "Is it that hard?"
                t "We won’t know until we see him."
                $ renpy.music.set_pause(True, channel='Thane')
                $ renpy.music.set_volume(0, 4, channel = "Thane")
                jump Bull_tribe_map0
            elif True:
                e 1 "Thane? You ready to head out?"
                t "Not now,[name]."
                t "I'll take you now in the daytime."
                jump Thane_talk
        "Уйти" if True:
            e 1 "I need to go now."
            t "Sure."
            t "If you need anything, I'll be here."

            jump forest_map_3
label Thane_tribe_talk:
    $ renpy.music.set_volume(0, 0.5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0.5, channel = "Chan2")
    pause 0.5
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Thane')
    $ renpy.music.set_volume(1, 4, channel = "Thane")


    $ Time.mins = Time.mins +5
    if Time.hours >= 6 and Time.hours <= 17:
        scene tent 1 with slow_dissolve
    elif True:
        scene tent 1n with slow_dissolve
    if Time.athane == Time.days:
        "He doesn’t sound like he wants to talk at the moment, best to leave him be."
        jump Bull_tribe_map
    if Thane.movein == 1:
        show thane stand at center with dissolve
        t "I would love to stay over at the tavern."
        t "Mind asking Snow if he’s ok with it?"
        t "If he is, just call me."
        hide thane stand at center with dissolve
        jump Bull_tribe_map
    if Quest.campw == 5:
        if Roushk.bulltribe == 1:
            show thane stand at center with dissolve
            t "[name], what brings you here today?"
            e 1 "I need a favour Thane."
            e 1 "There’s a new lizard warrior who’s entered the forest."
            t "And?"
            e 1 "And he has a way to go back home, but it needs him to remove a curse from this magical artifact."
            e 1 "I was thinking maybe the mystic pool in the bull temple could remove that curse."
            t "Well the pool’s purpose is to remove corruption, but I’ve never heard of anyone trying to remove curses from an item using that before."
            t "Hmm..."
            e 1 "Please Thane, we just need to try."
            t "Can this lizard be trusted?"
            e 1 "I’ll keep an eye on him at all times, plus he hasn’t been doing anything suspicious, minus that one time I had to fight him in the swamp."
            "Thane’s left eyebrow flicks upwards at you."
            t "Hmm..."
            t "Fine, you can come by when it’s darker, there won’t be many bulls out that time."
            t "Does your friend have a disguise?"
            e 1 "I don’t think so."
            t "At least get him a cloak or something to disguise himself."
            t "Then come by when it’s night time."
            e 1 "Alright, thanks Thane."
            "You rush back to the tavern."
            $ Roushk.bulltribe = 2
            $ Time.hours = Time.hours +1
            jump forest_map0

        elif Roushk.bulltribe == 2 or Roushk.bulltribe == 3:
            show thane stand at center with dissolve
            t "Bring your lizard friend over in the evening."
            t "Make sure he’s wearing a disguise so he won’t get caught so easily."
            t "I’m trusting you to treat the temple with respect, don’t leave it in a mess, ok?"
            e 6 "I promise we’ll behave while we’re up there."
            hide thane stand
            jump Bull_tribe_map
        elif Roushk.thane == 1:
            show thane stand at center with dissolve
            $ Roushk.thane = 2
            t "Hey, good news."
            t "After Tomahawk regained consciousness, he forgot everything that happened in the last hour."
            t "Guess he was knocked on the head too hard."
            e 13 "I guess that’s good?"
            t "It’s the best we can ask for. "
            hide thane stand
            jump Bull_tribe_map
        elif True:
            if Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bombt == 5:
                $ Time.festival_day = Time.days
                $ Quest.fes_end == 0
                $ Quest.bombt = 6
                $ Thane.talktree = 1
                if Quest.bomb_result == Axel:
                    $ Quest.bomb_bull = 4
                    show thane stand at center with dissolve
                    $ Time.athane = Time.days
                    e 13 "Thane..."
                    t "So, you made your choice. I hope you know what it cost."
                    e 1 "I did what I thought was right."
                    "..."
                    "Thane’s shoulders droop, but he still maintains a soft smile at you."
                    t "I’m not going to give up on you, you know."
                    e 5 "What?"
                    t "I still believe that you will make the right decision when the time comes."
                    t "That you’ll still try to put an end to this war."
                    e 13 "You’re insane, that’s just gambling on nothing!"
                    t "I don’t see it that way. I’m betting on the person who saved my life before when there was nothing in it for him."
                    t "If you’re telling me moments like that mean nothing, and everything that has been done is just a random mess."
                    t "Then there’s no point in anyone doing anything."
                    e 1 "You’re an idiot."
                    t "Then so be it. Think about it [name], why you’re doing any of this."
                    "You coldly turn away."
                    jump Bull_tribe_map
                elif Quest.bomb_result == Nauxus:
                    $ Time.athane = Time.days
                    show thane stand at center with dissolve
                    e 13 "Thane..."
                    t "Not now, [name]. Can’t you see I’m busy packing my things so my father can take them away?"
                    t "Please just come back later if you want to talk."
                    hide thane stand at center with dissolve
                    jump Bull_tribe_map
                elif Quest.bomb_result == Thane:
                    scene black with dissolve
                    play sound "music/foot1.ogg"
                    "You know where Thane will be."
                    play sound "music/foot1.ogg"
                    $ Time.mins = Time.mins +20
                    if Time.hours >= 6 and Time.hours <= 17:
                        scene bulltree 1 with vslow_dissolve
                    elif True:
                        scene bulltree 1n with vslow_dissolve
                    "Thane is there, looking into the distance."
                    e 1 "Thane, you alright?"
                    t "No, not really."
                    "You lean against the rock and just wait in silence."
                    "You wish you could say something to help ease his pain, but you know that the experience is still raw, and he would need time."
                    e 13 "Listen, I-"
                    t "I was stupid wasn’t I? If I kept my mouth shut we didn’t even have to have that conversation with my father?"
                    e 13 "..."
                    t "Now he’s going to get in our way for ending this stupid war."
                    "Thane sighs."
                    "He leans forward a bit. His eyes half closed."
                    t "You know, this was bound to happen at some point."
                    t "My father and I... we don’t talk much, we prefer to just act like everything’s fine... "
                    t "But maybe we don’t talk because we never liked each other."
                    e 1 "I think... you two just need to talk to each other more."
                    e 1 "It seems like you two care more about each other than you’re letting on."
                    t "Maybe... "
                    if Thane.help < 2:
                        t "Mind giving me some time to myself?"
                        e 1 "Sure bud."
                        "You take your leave."
                        jump Bull_tribe_map
                    elif True:
                        show thane stand at center with dissolve
                        "Thane slides down his rock and faces you."
                        t "For now, stopping this war comes first."
                        t "I don’t think it’s safe for us to keep planning our missions here."
                        t "My father is already suspicious of me. Maybe, I need to move somewhere else."
                        e 1 "Where would you go?"
                        t "Maybe... the tavern?"
                        t "You’ll still be able to look into what’s going in the bull and lizard tribe, while I plan out how to find the real kidnapper."
                        t "Plus, it will make it easier for us to share information."
                        e 1 "I mean, there are rooms if you have the coin."
                        e 1 "It’s pretty spacious there, and I might be able to talk to Snow about letting you live there rent free."
                        e 1 "But, won’t your father be more upset that you just left the village?"
                        e 1 "I don’t know if that is going to help your relationship with him."
                        t "It’s possible, but maybe we also need some time apart... What do you think?"
                        t "I trust your judgement, should I stay or should I go?"
                        menu:
                            "Convince Thane to live in the tavern" if True:
                                $ Thane.movein = 1
                                e 13 "I think you should come to the tavern."
                                e 1 "As you said, it will make planning easier."
                                t "Excellent. I’ll pack my things and meet you there when I’m ready."
                                e 1 "Are you going to tell your father about this?"
                                t "No... I just want to be away from him as much as I can."
                                t "He doesn’t need to know about this. I’ll leave a note if need be."
                                e 1 "Alright, then I’ll see you then."
                                hide thane stand at center with dissolve
                                "Thane nods and he leaves to pack his things."
                                e 1 "(I better go talk to Snow first to make sure he’s ok with Thane staying over.)"
                                "<[name] gained one Level-up-point.>"
                                $ Zalt.points = Zalt.points +1
                                jump Bull_tribe_map
                            "Convince Thane to stay in the bull village" if True:
                                e 13 "I think your place is here."
                                e 1 "No matter what happens, your tribe still needs you."
                                e 1 "If you leave, it might cause more trouble for your father."
                                t "My father... I guess you're right. "
                                "Thane sighs."
                                t "Thanks for the advice. I’ve got a lot to think about. Mind giving me some time?"
                                e 1 "Alright, then I’ll see you then."
                                "Thane nods and you walk away from him."
                                "<[name] gained one Level-up-point.>"
                                $ Zalt.points = Zalt.points +1
                                hide thane stand at center with dissolve
                                jump Bull_tribe_map











            if Quest.bomb_end != 0:
                if Quest.bombt == 1:
                    jump Thane_letter
                elif Quest.bombt == 2:
                    show thane stand at center with dissolve
                    t "You said you can get the materials for the glue from Snow."
                    t "I’m making the “thing”, I’ll meet you at the tavern after you get some pepper, wheat flour and water."
                    t "I wish you luck trying to convince him to part with them."
                elif Quest.bombt == -1:
                    "Thane does not want to talk to you at the moment."
                elif True:
                    "Thane doesn’t look like he is in the mood to talk, best to come back later."
            elif True:

                if Quest.bombt == 6:
                    if Thane.talktree == 1:
                        label Thane_talktree_tribe:
                            show thane stand at center with dissolve
                            menu:
                                "Ask his opinion about his father" if True:
                                    if Quest.bomb_result == Thane and Thane.help >= 1:
                                        e 1 "Hey, things with your father were pretty intense there. Are you going to be ok with him?"
                                        t "..."
                                        t "I don’t know anymore, [name]."
                                        t "He’s made it pretty clear that I’m just getting in his way. "
                                        e 13 "Thane..."
                                        t "Things weren’t always like this you know."
                                        t "We didn’t see eye to eye on a lot of things, but it never escalated to this point."
                                        t "He liked axe fighting, I liked my spear."
                                        t "He wanted to push me to take on more battles, I just wanted to try making more arts and crafts. "
                                        "Thane sighs."
                                        e 13 "Every child and parent have disagreements. Even I do with my father."
                                        e 13 "Still there has to be some good times between the two of you."
                                        t "There were... but... Look just give me time to think this over."
                                        t "The whole ordeal is still very fresh for me. If you know what I mean."
                                        e 1 "Right, let's talk about something else."
                                        jump Thane_talktree_tribe
                                    elif True:
                                        t "Can we please not talk about my father."
                                        t "He’s just another thing on my long list of disappointments. "
                                        "Thane crosses his arms."
                                        e 1 "Right, my bad. Let’s talk about something else."
                                        jump Thane_talktree_tribe
                                "Ask about Thane’s living conditions" if True:
                                    e 1 "How are your living conditions?"
                                    t "It’s as wonderful as someone living with a mostly empty room. "
                                    t "Doesn’t help that father has his men watch over me in secret."
                                    e 1 "How did you know that?"
                                    "Thane points to his back without turning."
                                    "You lean to the right and catch a pair of bulls trying to blend in with the wall by covering themselves with leaves."
                                    e 13 "Ah."
                                    t "I’d be more upset if I wasn’t so embarrassed right now."
                                    jump Thane_talktree_tribe
                                "Ask about Thane’s future plans" if True:
                                    if Thane.help >= 2:
                                        e 1 "What are you going to do now?"
                                        t "I’m still carrying out my investigation."
                                        t "I’ve got a lead that will meet with me to share what they have on the kidnappings."
                                        e 5 "That doesn’t sound safe, maybe I should go with you."
                                        t "No, I have to do this alone, the lead made it clear that there can’t be anyone else."
                                        t "I’ll be fine, I know how to fight."
                                        e 13 "Yeah, but it still sounds dangerous."
                                        t "Have faith in me, [name]."
                                        t "But, if I disappear for more than a day, then you’d probably want to check the swamp for my body."
                                        "Thane laughs heartily."
                                        e 9 "Don’t joke about that. You’re really making me worry."
                                        t "[name], it will be fine. Trust me."
                                        t "You should be concerned with what you will do next with father and Nauxus. "
                                        jump Thane_talktree_tribe
                                    elif True:

                                        e 1 "What are you going to do now?"
                                        t "Oh, you’re still interested in knowing?"
                                        e 13 "I’m just concerned that you’ll get yourself in trouble."
                                        e 1 "We may not be a hundred percent on the same track, but that doesn’t mean I want to see you getting hurt unnecessarily."
                                        t "Don’t be too worried about my situation [name]."
                                        t "I am still interested in us working together, but I am not gullible enough to give up my plans so easily."
                                        t "Try asking me again some other time."
                                        e 1 "..."
                                        jump Thane_talktree_tribe
                                "Уйти" if True:

                                    jump Bull_tribe_map
                    elif True:




                        t "Don’t mind me, I’m making preparations for something big."
                        t "Maybe we can talk some other time."
                elif True:
                    "Thane doesn’t look like he is in the mood to talk, best to come back later."
        jump Bull_tribe_map
    show thane stand at center with dissolve
    if Quest.campw != 0 and Quest.campw < 5:
        jump Thane_tribe_camp_end
    if Thane.quest == 5:
        "Upon reaching the Chief’s tent you see Thane waiting for you."
        t "Ah, brother you made it. Hope you’re ready for a long walk."
        e 1 "Brother?"
        "Was he talking to someone else?"
        "You turn around expecting to see someone but it’s just you on the stairs."
        e 1 "You mean me?"
        t "Obviously, you’re part of the tribe now, so you’re our brother."
        e 1 "I’ve never had a brother before."
        t "We’re all brothers and sisters here. One big family that looks out for one another."
        t "We play together, work together, and occasionally we fight, but that’s what being a family is all about."
        t "But if it’s weird, I’ll stick to calling you by your name."
        e 6 "I feel like I’ve got to earn it first, till then, you can call me [name]."
        t "Alright, then if you are well equipped, we can climb."
        t "If you're not, you may want to visit the general store and get whatever you need."
        t "Just tell me when you’re ready to go."
        menu:
            "Ready" if True:
                e 1 "Ready, let’s go."
                "You both begin your climb up the mountain."
                $ Thane.quest = 6
                $ Thane.mountain = 1
                play music [ "<silence 1.0>", "music/bulls_mountain_path.ogg" ] fadein 1
                jump Mountain_map
            "Not yet." if True:
                e 1 "Not yet."
                t "Okay,I will wait you here."
                jump Bull_tribe_map
    elif Thane.quest == 7:
        if Quest.campl == 1 and Quest.campb == 1:
            t "Hey [name]. I’ll talk to you later."
            t "I’m trying to think of the ingredients I need to cook something tonight."
            jump Bull_tribe_map
        elif Quest.campl == 3 and Quest.campt == 2:
            t "You’re back, how’d it go?"
            e 1 "I’ve got a vial of the Fear Potion, should be enough to cover a large area once it’s used."
            t "Good, and not a minute too soon."
            t "I managed to spy on father’s meeting with a group of our warriors."
            t "They know about the lizards plan to step up a camp, but not when the attack will happen."
            e 1 "Is the timing of the attack that important?"
            t "Yes, for the plan to work we need both tribes to be at the same location near the same time. "
            t "That way we scare them both at the same time, and they will not suspect each other if both sides are affected at the same time."
            t "Do you know when the lizards plan to make their move?"
            e 1 "The attack will commence at{color=#19c22a} 10 a.m{/color}.They’re just waiting for me to give the signal to head out."
            t "Good, with the potion ready we can take both sides out tomorrow."
            t "My father picked Tomahawk and his crew for this mission."
            t "They haven't left the village yet, they're probably waiting for my father's orders."
            t "We can use this chance to persuade the bulls to head out about now and they should be able to reach the lizards around the same time."
            t "Follow me, and uhh, you might want to think of something convincing to say before we meet them."
            "Thane leads you down a flight of stairs faster than you’ve ever seen him move."
            hide thane stand with dissolve
            scene bulltribe 1 with dissolve
            "You both make your way through the village to the front of the tribe’s shop."
            scene tribe 1 with dissolve
            "There you see a group of four bulls some merrily drinking while others were eating plates of sandwiches."
            "One of the bulls sees the two of you coming over and heads over."
            "Leader bull" "If it isn't unlucky Thane. What brings you here brother?"
            show thane stand1 at center with dissolve
            t "Come on brother Tomahawk, do you really have to call me that?"
            "Tomahawk laughs."
            "Tomahawk" "You know I'm just messing with you. So, what can the village's best warrior do for you?"
            t "I hear you and your team will be going against the lizards trying to build a camp near us."
            "Tomahawk" "Damn right we are. Those slimy reptiles won't stand a chance against us."
            "Tomahawk" "We'll beat them in two shakes of a bull's tail."
            t "Well it so happens, [name] here has some valuable information you can use for your mission."
            hide thane stand with dissolve
            "Thane pushes you forward from the back."
            "You turn to him with a confused expression, to which his eyes just darts quickly between you and Tomahawk."
            e 6 "Uhh, hello. Nice to meet you, Tomahawk."
            e 1 "I come with news about your mission to stop the lizards from building their camp."
            "Tomahawk" "Oh?"
            menu:
                "Try to convince him(stat check)" if True:
                    e 1 "I came back from my reconnaissance of the lizard tribe and I uncovered their plan of attack."
                    e 1 "They are making their move at 10 a.m. tomorrow, you and your men should push out about that time tomorrow to take them on."
                    if Zalt.cha > 6:
                        "{b}{color=#19c22a}<Charm Check success>{/color}"
                        "Tomahawk" "Interesting, why would I be hearing this from you but not from the chief?"
                        "Tomahawk" "He never mentioned someone was going to spy on the enemy."
                        e 1 "I did it on my own, it was my way to show my loyalty to the tribe."
                        "Tomahawk" "Nobody likes a kiss ass wolf. Especially the chief."
                        e 1 "I don't have your amazing physique, I mean look at you, you're built like a house. "
                        e 1 "It's no wonder Chief Axel would pick you to lead this mission."
                        "Tomahawk laughs heartily and puffs out his chest."
                        "Your praise seems to work on him."
                        "Tomahawk" "You're damn right about that."
                        "Tomahawk" "If it weren't for Thane here, I bet I’ll be the best candidate for chief."
                        "Tomahawk" "Well makes sense why you got to work harder around here wolf."
                        "Tomahawk" "Hey, if you ever need training to be a real warrior, you can always look me up. "
                        "The bull laughs louder now. All you can do is chuckle nervously."
                        "He crosses his arms and turns to his group who are watching in silence."
                        "Tomahawk" "Pack up the party everyone, once we get our supplies we’ll head out."
                        "Tomahawk" "We’ll meet those lizards on time and show this outsider that Tomahawk and his men are the strongest!"
                        "The crowd cheers again. Tomahawk walks off to rejoin his men. Leaving you room to breathe. "

                        jump Thane_tribe_camp_bull
                    elif True:
                        "{b}{color=#c22719}<Charm Check failed>{/color}"
                        "Tomahawk" "I don't buy it. The chief wouldn't trust an outsider so easily with such an important mission."
                        e 9 "Err, I... I'm just trying to get on his good side."
                        "Tomahawk" "Nobody likes a kiss ass wolf."
                        "Tomahawk" "Especially the chief, and the longer I look at you the less I want to see you."
                        e 6 "Well I... come on give me a chance."
                        e 6 "Maybe I'd look better if I had some fake horns, then I'd look as good as you."
                        "Tomahawk" "You making fun of me, wolf?"
                        "Tomahawk's nostrils are flaring. He doesn't find you charming at all."
                        "Tomahawk" "That's it, no one makes fun of my horns!"
                        "Tomahawk balls his hand into a fist and throws a punch."
                        "You guard your face for the incoming impact, but it doesn't come."
                        "Instead Thane caught the hit with his right hand."
                        show thane stand1 at center with dissolve
                        "The son of the bull tribe's chief keeps a calm face against the enraged bull."
                        t "There, there brother. My friend here is not that good with words."
                        "Tomahawk" "Hmph!"
                        "The angry bull pulls his fist back."
                        t "But hear him out, what he says is true."
                        t "The lizards are attacking at 10 in the morning. "
                        t "[name] here was just concerned the lizards would have an advantage over you if you get there too late."
                        t "You and your troop should head there soon and meet them at the same time. "
                        "Tomahawk" "Your concern is appreciated but unnecessary. My men and I will have no problem achieving victory again. "
                        "Tomahawk" "But, it would be impolite to refuse a request from the chief's son."
                        "Tomahawk" "Perhaps if you can 'motivate' my men and I somehow, we'd be more driven to head out."
                        t "Would 10 mugs of beer and 5 pieces of jerky be motivating enough?"
                        "Tomahawk" "Sounds promising. You'll have to bring us the goods before we can say."
                        t "We'll see what we can do."
                        hide thane stand1
                        show thane stand at center with dissolve
                "Try to challege him(stat check)" if True:

                    "The bulls answer to who's the strongest. You'll need to show him you're stronger than him."
                    e 1 "Wow, if I knew the strongest warrior of the village is such a weakling, I can't wait to take that title away from you."
                    "Tomahawk" "What? "
                    "The fur on Tomahawk's back stiffens and stands erect like quills of an enraged porcupine."
                    e 1 "You heard me. Your plan lacks strategy."
                    e 1 "And only a weakling will be so full of himself that he'd let the enemy empower themselves before striking."
                    e 1 "You’re a brainless weakling, if you’re really strong you’ll face them head on at the time of their meeting and wipe them out before they even saw it coming!"
                    "Tomahawk" "Why you-"
                    "The bull’s face twitches uncontrollably, and he throws a powerful punch right at your face."
                    if Zalt.str > 6:
                        "{b}{color=#19c22a}<Strength Check success>{/color}"
                        "With your unwavering strength you raise your forearms and block the hit head on."
                        "Your feet dig deep into the ground but the force of impact pushes you back a few inches, leaving a trail from where you originally stood."
                        "Your quickly clutch his wrist with your left hand and you pull him forward with a strong tug."
                        "He loses his balance and lurches forward."
                        "He’s wide open for a hit, your right hand balls into a fist and you punch him square in the jaw."
                        "You release your grip and let the bull topple to the ground."
                        "Tomahawk coughs and wipes the saliva dripping down his mouth."
                        "Tomahawk" "You bastard, you actually held back on that one."
                        "He pulls himself back up and you ready yourself for a fight."
                        "Tomahawk" "You’re going to pay for that when I get back."
                        "Tomahawk" "I’m no weakling boy, but I will always listen to someone who’s strong."
                        "He crosses his arms and turns to his group who are watching in silence."
                        "Tomahawk" "Pack up the party everyone, once we get our supplies we’ll head out."
                        "Tomahawk" "We’ll meet those lizards on time and show this outsider that Tomahawk and his men are the strongest!"
                        "The crowd cheers again. Tomahawk walks off to rejoin his men. Leaving you room to breathe. "
                        jump Thane_tribe_camp_bull
                    elif True:
                        "{b}{color=#c22719}<Strength Check failed>{/color}"
                        "You pull up your arms to defend yourself, but the force of impact is too strong for you to block."
                        "Tomahawk's punch sends you flying backwards but Thane catches you by the shoulders before you land."
                        "You look up and catch a glimpse of how Thane’s beady eyes are locked on Tomahawk."
                        "He leaves you standing at the side before charging forward at the other bull."
                        show thane stand1 at center
                        hide thane stand1 at center with dissolve
                        "Thane runs and kicks Tomahawk square on the chest. The force topples the bull to the ground."
                        "He doesn’t give him a chance to stand up, and plants his feet right on the bull’s stomach."
                        show thane stand1 at center with dissolve
                        t "Listen here, you mess with my friend, you mess with me."
                        t "And I’ll break you down as many times as it takes for you to get through your thick head that you need to get to the lizards at the same time. "
                        t "I’ll drag you by the horns there if I have to, and you know I can do it! You hear me?"
                        "Tomahawk" "Alright, alright! Just get off of me."
                        hide thane stand1 at center with dissolve
                        "Thane lifts his foot off the bull and helps him up to his feet."
                        "On Tomahawk’s chest and stomach are two separate hoof prints where Thane’s foot came in contact earlier."
                        "Tomahawk" "You're lucky you caught me off guard brother. "
                        t "Doesn't matter, a win's a win."
                        "Tomahawk" "Yeah well I let you win this time, consider it a break from all your bad luck."
                        "Thane rolls his eyes at the defiant bull."
                        t "Are you done? Just go do your job."
                        "Tomahawk" "Not so fast. You might have convinced me with your strong kick, but unless you're willing to take on all my men. They aren't budging."
                        "You peek from behind Thane, and true enough, Tomahawk's crew were not happy that their leader was drop kicked."
                        t "Alright, let's just make a deal. What will it take for you all to get going and meet the lizards on time?"
                        "Tomahawk" "Perhaps if you can 'motivate' my men and I somehow, we'd be more driven to head out."
                        t "Would 10 mugs of beer and 5 pieces of jerky be motivating enough?"
                        "Tomahawk" "Sounds promising. You'll have to bring us the goods before we can say."
                        t "We'll see what we can do."
                        hide thane stand1
                        show thane stand at center with dissolve
            "Thane takes you away by the arm until you are outside of ear shot from the other bulls."
            t "That was close."
            e 13 "Man I suck at this negotiating thing."
            t "That's ok, we just need to make sure this next part works out."
            t "Do you have 10 beer and 5 jerky on you?"
            if Parif.witer_first != 0:
                if jane_inv.qty(beer) < 10 or jane_inv.qty(jerky_p) < 5:
                    e 1 "No, not yet, but I can get them from the tavern."
                    t "Alright, get them quick. I’ll keep Tomahawk and his men entertained here."
                    t "Once you get all the items meet me back here in front of the shop."
                    "You need to get 10 beer and 5 jerky before meeting Thane back."
                    $ Quest.campt = 3
                    jump Bull_tribe_map
                elif True:
                    $ jane_inv.drop(beer,10)
                    $ jane_inv.drop(jerky_p,5)
                    e 1 "Yeah, I'm good to go."
                    t "Great, I'll help you carry it over."
                    "Thane takes the items from you and walks over to the bulls. You follow from behind."
                    "Tomahawk and his gang make quick work and rush in to grab their share of the meal."
                    "Tomahawk with a beer in hand pats Thane on the back."
                    "Tomahawk" "These are some pretty good beer."
                    "Tomahawk" "Alright, guess we should head off early and get this lizard crap over with, then we can get back and get more beer!"
                    "Tomahawk" "Ain’t that right short stuff?"
                    e 1 "Eh, me?"
                    "Tomahawk" "Damn right, at least you’re good for something. Fetching us more beer!"
                    "Tomahawk" "Let’s move men! "
                    "Tomahawk and his men now satisfied with their meal, leave the village."
                    jump Thane_tribe_camp_bull
            elif True:

                if jane_inv.qty(beer) < 10 or jane_inv.qty(jerky) < 5:
                    e 1 "No, not yet, but I can get them from the tavern."
                    t "Alright, get them quick. I’ll keep Tomahawk and his men entertained here."
                    t "Once you get all the items meet me back here in front of the shop."
                    "You need to get 10 beer and 5 jerky before meeting Thane back."
                    $ Quest.campt = 3
                    jump Bull_tribe_map
                elif True:

                    $ jane_inv.drop(beer,10)
                    $ jane_inv.drop(jerky,5)
                    e 1 "Yeah, I'm good to go."
                    t "Great, I'll help you carry it over."
                    "Thane takes the items from you and walks over to the bulls. You follow from behind."
                    "Tomahawk and his gang make quick work and rush in to grab their share of the meal."
                    "Tomahawk with a beer in hand pats Thane on the back."
                    "Tomahawk" "These are some pretty good beer."
                    "Tomahawk" "Alright, guess we should head off early and get this lizard crap over with, then we can get back and get more beer!"
                    "Tomahawk" "Ain’t that right short stuff?"
                    e 1 "Eh, me?"
                    "Tomahawk" "Damn right, at least you’re good for something. Fetching us more beer!"
                    "Tomahawk" "Let’s move men! "
                    "Tomahawk and his men now satisfied with their meal, leave the village."
                    jump Thane_tribe_camp_bull
        elif True:

            t "[name], what brings you here?"
            e 1 "Well."
            menu:
                "Discuss lizard tribe camp mission" if Quest.campl == 3 and Quest.campt == 0:
                    e 1 "Thane."
                    t "What?"
                    e 13 "(No wait, is this really what I want to do?)"
                    e 13 "(Thane is still Axel’s son and he is devoted to his tribe.)"
                    e 13 "(Would he use what I tell him to get an advantage against the lizards?)"
                    e 1 "(But, he’s never shown any animosity against the lizards. Can I trust him?)"
                    menu:
                        "He is my friend." if True:
                            e 1 "(He's my friend and he said he wants the best for the tribe. I can trust him.)"
                            e 1 "(Sorry,Nauxus.)"
                            e 1 "Nauxus has started his plans to take over the bull tribe."
                            t "What? That's... I never expected he would make the first move, father yes, but him?"
                            t "Wait, come over here."
                            hide thane stand with dissolve
                            play sound "music/foot1.ogg"
                            $ Time.mins = Time.mins +20
                            if Time.hours >= 6 and Time.hours <= 17:
                                scene bulltree 1 with vslow_dissolve
                            elif True:
                                scene bulltree 1n with vslow_dissolve
                            "He leads you until you into the forest just outside of the village."
                            "You both stop in front of a plain tree."
                            "He walks off to the side of a rock and leans against it, he pats the right side signaling you to join him."
                            "Thane looks around as you take your place next to him."
                            "Once he's done looking he turns to you and speaks in a hushed tone."
                            show thane stand at center with dissolve
                            t "Ok, tell me what's their plan."
                            e 1 "..."
                            e 1 "How do I know you won't use this to advance the bull's own goals?"
                            t "[name] I thought it was pretty clear, I don't want a war to break out between our tribe."
                            t "This is misdirected hate, I know for a fact, none of the bulls would do something as vile as to attack children, no matter their species."
                            t "I just haven't thought of a way for the lizard tribe to see that."
                            e 1 "But the bull children are missing too, it won't look good if your tribe finds out you are soft on them."
                            t "They won't find out, and if I worry about what my tribe thinks of me I wouldn't be here today."
                            t "Look you came to me for a reason, that maybe some part of you knows that if you go along with any side this will not end well for anyone."
                            t "[name], you have my word I will do what I can to ensure peace among both tribes until this whole kidnapping issue is dealt with."
                            e 13 "Fine, I'm in."
                            e 1 "I was instructed to lead a team to a spot closer to the bull tribe to set up a camp for the lizard tribe."
                            e 1 "They plan to use the camp to spy on the bull tribe and to advance the invasion."
                            t "That's not good. The woods are dangerous enough as it is, but if the lizards plan to establish a camp."
                            t "That location can be equally dangerous if the bulls get their hands on it."
                            t "We have to make sure no one gets that point."
                            e 1 "How do we keep both sides from coming back there?"
                            t "We scare them off! All we need is something to make them not want to build the camp there at all."
                            e 1 "Scaring them huh, it makes sense, like I could make a costume out of some leaves and branches."
                            t "That's too simple, the bulls won't be afraid of something like that. "
                            e 1 "What are they afraid off then."
                            t "Probably a giant monster, if you know someone who can cast illusions or make a Fear Potion. "
                            e 13 "A Fear Potion... maybe Chet knows how to make it."
                            t "Who’s Chet?"
                            e 1 "Our residential tavern shopkeeper."
                            e 1 "He can make potions already, maybe he can help us craft a Fear Potion."
                            t "Try to find out, I’ll get information if father is making any plans against the lizards as well. I’ll call for you if I find something."
                            e 1 "Right, and Thane, please stay safe. No one can know about this but us."
                            t "I know, now go. We’ve got to work quickly."
                            t "Once you get the Fear Potion meet me back here, and we’ll plan what to do."
                            $ Time.mins = Time.mins +20
                            hide thane stand with dissolve
                            scene black with dissolve
                            "Both of you walk back to the tribe."
                            "Thane leaves you and heads into Chief Axel’s tent."
                            "You need to talk to Chet to see if he can brew for you a Fear Potion."
                            $ Quest.campt = 1
                            $ Quest.campc = 1
                            jump Bull_tribe_map
                        "It’s too risky" if True:


                            e 13 " (No, it’s too risky. He’s still the chief’s son, if the pressure is put on him he might just spill everything.)"
                            e 6 "Nothing, I just wanted to see how you’re doing."
                            t "Well I’m fine, thanks for asking."
                            $ Quest.campt = -1
                            jump Bull_tribe_map
                "Here is the beer and jerky" if Quest.campl == 3 and Quest.campt == 3:
                    if Parif.witer_first != 0:
                        if jane_inv.qty(beer) < 10 or jane_inv.qty(jerky_p) < 5:
                            t "Do you have the 10 beer and 5 jerky?"
                            e 1 "No, not yet."
                            t "Hurry, they probably won’t listen to us if we don’t get them what they want."
                            jump Bull_tribe_map
                        elif True:
                            $ jane_inv.drop(beer,10)
                            $ jane_inv.drop(jerky_p,5)
                            t "Do you have the 10 beer and 5 jerky?"
                            e 1 "I got them right here."
                            t "Great, I'll help you carry it over."
                            hide thane stand with dissolve
                            scene bulltribe 1 with dissolve
                            "Thane takes the items from you and walks over to the bulls. You follow from behind."
                            scene tribe 1 with dissolve
                            show thane stand1 at center with dissolve
                            "Tomahawk and his gang make quick work and rush in to grab their share of the meal."
                            "Tomahawk with a beer in hand pats Thane on the back."
                            "Tomahawk" "These are some pretty good beer."
                            "Tomahawk" "Alright, guess we should head off early and get this lizard crap over with, then we can get back and get more beer!"
                            "Tomahawk" "Ain’t that right short stuff?"
                            e 1 "Eh, me?"
                            "Tomahawk" "Damn right, at least you’re good for something. Fetching us more beer!"
                            "Tomahawk" "Let’s move men! "
                            "Tomahawk and his men now satisfied with their meal, leave the village."
                            jump Thane_tribe_camp_bull
                    elif True:


                        if jane_inv.qty(beer) < 10 or jane_inv.qty(jerky) < 5:
                            t "Do you have the 10 beer and 5 jerky?"
                            e 1 "No, not yet."
                            t "Hurry, they probably won’t listen to us if we don’t get them what they want."
                            jump Bull_tribe_map
                        elif True:
                            $ jane_inv.drop(beer,10)
                            $ jane_inv.drop(jerky,5)
                            t "Do you have the 10 beer and 5 jerky?"
                            e 1 "I got them right here."
                            t "Great, I'll help you carry it over."
                            hide thane stand with dissolve
                            scene bulltribe 1 with dissolve
                            "Thane takes the items from you and walks over to the bulls. You follow from behind."
                            scene tribe 1 with dissolve
                            show thane stand1 at center with dissolve
                            "Tomahawk and his gang make quick work and rush in to grab their share of the meal."
                            "Tomahawk with a beer in hand pats Thane on the back."
                            "Tomahawk" "These are some pretty good beer."
                            "Tomahawk" "Alright, guess we should head off early and get this lizard crap over with, then we can get back and get more beer!"
                            "Tomahawk" "Ain’t that right short stuff?"
                            e 1 "Eh, me?"
                            "Tomahawk" "Damn right, at least you’re good for something. Fetching us more beer!"
                            "Tomahawk" "Let’s move men! "
                            "Tomahawk and his men now satisfied with their meal, leave the village."
                            jump Thane_tribe_camp_bull
                "Discuss bull tribe camp mission" if Quest.campb == 3 and Quest.campt == 0:
                    e 1 "Your father summoned me to his tent."
                    t "So, he’s started his move. Wait, come here, we can't risk someone overhearing us."
                    hide thane stand with dissolve
                    play sound "music/foot1.ogg"
                    $ Time.mins = Time.mins +20
                    if Time.hours >= 6 and Time.hours <= 17:
                        scene bulltree 1 with vslow_dissolve
                    elif True:
                        scene bulltree 1n with vslow_dissolve
                    "He leads you until you into the forest just outside of the village."
                    "You both stop in front of a plain tree."
                    "He walks off to the side of a rock and leans against it, he pats the right side signaling you to join him."
                    "Thane looks around as you take your place next to him."
                    show thane stand at center with dissolve
                    e 1 "Actually, the lizards made the first move."
                    e 1 "Chief Axel got word that they plan to establish a camp near the bull tribe to advance their attack on the bulls."
                    t "This is most disturbing. I never knew Nauxus to act so rashly."
                    t "Perhaps the mounting pressure of his tribe made him make the move?"
                    "You shrug."
                    e 1 "More importantly what are we going to do about it?"
                    e 1 "I'm to lead the bulls to the same location to fight off the lizards."
                    t "No, that's going to work in our favour."
                    t "You can get the bulls to meet the lizards and then scare them both off from ever trying to build a camp there."
                    e 1 "Easier said than done, what can scare both the bulls and lizard?"
                    "Thane puts a hand to his chin and looks deep in thought."
                    t "A Fear Potion."
                    t "I've heard of those, they make those exposed to its fumes see hallucinations of the things they fear."
                    t "It would be very effective against both sides. You just need to get them to meet at the same time."
                    t "That way they won't suspect each other since both the bulls and the lizards will get hit."
                    e 13 "A Fear Potion... maybe Chet knows how to make it."
                    t "Who’s Chet?"
                    e 1 "Our residential tavern shopkeeper."
                    e 1 "He can make potions already, maybe he can help us craft a Fear Potion."
                    e 13 "But..damn it, I don't know when the lizards are making their move."
                    t "Then you'll need to find out before we can proceed."
                    e 13 "Hmm..."
                    e 1 "Nauxus relies on Selye to organize these plans. "
                    e 1 "Maybe if I can show him something to worry about their plan."
                    e 1 "Then maybe he might call his men in to discuss the plan again."
                    t "I got just the thing."
                    hide thane stand with dissolve
                    "Thane asks you to wait by the rock while he back to the tribe."
                    $ Time.mins = Time.mins +15
                    show thane stand at center with dissolve
                    "He comes back up and gives you a rolled up piece of paper."
                    e 1 "What’s this?"
                    "You unrolled the parchment and you see a map very similar to yours."
                    t "Your way into information. "
                    t "Now, show me where the attacks going to take place."
                    e 1 "Here."
                    hide thane stand with dissolve
                    "Thane then pulls out a stamp and marks the area with a stamp in the shape of a lizard's head."
                    "He rolls the map and hands it over to you. "
                    show thane stand at center with dissolve
                    t "Just hand this over to that Selye guy and it’ll make him double-think his plans."
                    e 1 "Huh, ok. I’ll give it a try."
                    t "Remember, get the time the lizards plan to make their move first, then get the Fear Potion."
                    t "The potion will be useless to us if we don’t know if we can even time this plan properly."
                    t "Once you have those, come find me here."
                    "You nod understandingly and head out with the map."
                    $ Quest.campt = 1
                    hide thane stand with dissolve
                    jump Bull_tribe_map
                "About the time and the potion" if Quest.campb == 3 and Quest.campt >= 1 and Quest.campt <4:
                    if Quest.campc != 4:
                        t "Remember, you’ll need the time the lizards plan to make their move first, then get a Fear Potion."
                        t "Once you are done with both, come find me here."
                        jump Bull_tribe_map
                    elif True:
                        if Time.days <= Time.lizardgo+1:
                            e 3 "Thane, I got it!"
                            "Thane nods and leads you until you into the forest just outside of the village."
                            "You follow him and stand beside him."
                            hide thane stand with dissolve
                            play sound "music/foot1.ogg"
                            $ Time.mins = Time.mins +20
                            if Time.hours >= 6 and Time.hours <= 17:
                                scene bulltree 1 with vslow_dissolve
                            elif True:
                                scene bulltree 1n with vslow_dissolve
                            show thane stand at center with dissolve
                            t "So, you have the potion?"
                            e 1 "Right here."
                            "You pull out the large vial of Fear Potion."
                            t "Ok, that’s good. So, what do we know about the attack?"
                            e 1 "It’s going to happen tomorrow at 10 a.m."
                            t "Excellent, then we’re ready to go. Lead the bulls to the same location at the same time."
                            t "When you are near, sneak away and get into a prime location to drop the potion."
                            t "The best time is when both sides catch sight of each other, but before they try to kill one another."
                            e 1 "Right, I’ll make sure to time it right. I’ll meet you after I’m done reporting back to Chief Axel."
                            t "What are you going to tell him?"
                            e 1 "That maybe the place is cursed by the fog, doesn’t sound too far fetched. Wish me luck."
                            hide thane stand with dissolve
                            "Thane approaches you and wraps his arms around your back."
                            "He pulls you close for a hug, smothering your snout between his pecs."
                            "His deep earthy scent fills your nostrils."
                            show thane stand at center with dissolve
                            "Thane looks down at you. His eyes look heavily upon yours."
                            t "You know my luck isn’t worth anything, just make sure you come back to me, ok."
                            "He presses you closer against him, you can hear his heartbeat clearly against your ear."
                            e 7 "I’ll be back. "
                            "You pull yourself away from Thane. He smiles at you, but you can tell he’s forcing himself to put on a brave front."
                            "You punch his chest softly, and give him a reassuring nod before you prepare yourself for what is to come."
                            hide thane stand with dissolve
                            $ Quest.campb = 4
                            $ Quest.campt = 4
                            jump camp_map
                        elif True:

                            "You return to Thane pacing back and forth muttering to himself. He looks utterly distressed."
                            e 1 "Thane?"
                            "He turns to you, he looks shocked to see you standing there."
                            t "Thank the Divine Beings you're back. I thought something terrible had happened to you."
                            e 1 "I’m fine Thane. It just took longer than expected to get all the materials."
                            e 1 "I have the potion and the info on the lizard’s attack."
                            "Thane’s shoulders drop, and he frowns like he lost something dear to him."
                            t "What’s the point, we’ve waited too long. They probably have their camp set up."
                            e 9 "Is this true? Did Chief Axel announce it?"
                            t "No, he didn’t say anything. Actually, he hasn’t made a move at all."
                            e 9 "We better see him first, if we’re really too late his silence isn’t a good sign."
                            hide thane stand with dissolve
                            scene bulltent with dissolve
                            "You both are granted permission into the chief’s tent. Axel sits with his arms crossed. "
                            show thane stand1 at left with dissolve
                            show axel stand at right with dissolve
                            a "Thane, good you brought your little friend over."
                            a "I was beginning to worry he’d run away, or worse defect to the lizard’s side."
                            e 9 "I was just preparing for the mission."
                            a "Well you took your sweet time!"
                            t "Is it too late? Were the lizards successful in their plans?"
                            a "It’s none of your concerns, son."
                            a "But, if you must know, one of the bulls spotted the lizard group roaming the forest area."
                            a "They appeared lost as though they’re walking without a map."
                            e 1 "What happened to them?"
                            a "They escaped, the bull wasn’t enough to take them down."
                            a "Worse still, the lizard team gathered their bearings and were last seen heading towards the campsite they were targeting."
                            a "It’s estimated they will reach the area by 10 a.m. tomorrow."
                            a "So, I’m pretty sure you’re ready now, aren’t you wolf boy?"
                            "Axel’s face blackens and his fists tightens."
                            "He doesn’t look happy that you’ve kept him waiting to start the mission."
                            e 9 "Right, I’m ready to go."
                            "Axel summons four other bull warriors and gives you command over them."
                            "You and your team head out to the camp area, you most likely will encounter the lizards right on time."
                            $ Quest.campb = 4
                            $ Quest.campt = 4
                            jump camp_map
                "Уйти" if True:





                    e 6 "Nothing, I just wanted to see how you’re doing."
                    t "Well I’m fine, thanks for asking."
                    jump Bull_tribe_map
    elif True:

        "You see this mean it's a bug."
label Thane_tribe_camp_bull:
    $ Quest.campt = 4
    hide thane stand with dissolve
    play sound "music/foot1.ogg"
    $ Time.mins = Time.mins +20
    if Time.hours >= 6 and Time.hours <= 17:
        scene bulltree 1 with vslow_dissolve
    elif True:
        scene bulltree 1n with vslow_dissolve
    "Thane pulls you aside by the arm and escorts you to a quiet area nearby with no one around."
    show thane stand at center with dissolve
    "Once you’re both sure you’re in the clear, your shoulders drop and you feel all the energy in you just abandon you. "
    "You sense the same tiredness from Thane judging from the beads of sweat dripping from his forehead."
    "Even the colour on his face looks paler. "
    t "I’m glad that worked out."
    e 6 "Same here, I didn't expect negotiating to be this tiring."
    t "We’ll have time to rest once this is done, there is no turning back from this point on."
    t "You need to get back to the lizard tribe and lead their team to the camp’s location."
    t "Make sure they get there in time by tomorrow."
    t "Slip away from them, and find a suitable position to drop the potion. "
    e "Right, I’ll make sure to time it right. I’ll meet you after I’m done reporting back to Nauxus and Selye."
    t "What are you going to tell them?"
    e 1 "That maybe the place is cursed by the fog, doesn’t sound too far fetched. Wish me luck."
    hide thane stand with dissolve
    "Thane approaches you and wraps his arms around your back."
    "He pulls you close for a hug, smothering your snout between his pecs."
    "His deep earthy scent fills your nostrils."
    show thane stand at center with dissolve
    "Thane looks down at you. His eyes look heavily upon yours."
    t "You know my luck isn’t worth anything, just make sure you come back to me, ok."
    "He presses you closer against him, you can hear his heartbeat clearly against your ear."
    e 7 "I’ll be back. "
    "You pull yourself away from Thane. He smiles at you, but you can tell he’s forcing himself to put on a brave front."
    "You punch his chest softly, and give him a reassuring nod before you head out of the tribe."
    jump forest_map0
label Thane_tribe_camp_end:
    if Quest.campw1 == 1 or Quest.campw1 == 2:
        t "[name]."
        "He waves at you from behind his rock. You join him."
        t "What's wrong with your eye?"
        t "Let me find some drugs for you."
        "Thane tried to leave, but you stop him."
        e 6 "It's okay, no need to worry."
        e 6 "I will heal it later, okay?"
        "Thane takes a deep breath."
        t "Fine,[name]. And thanks."
        t "I can’t believe we pulled it off."
        "Thane isn’t containing his excitement."
        "His feet are stomping the ground like he is doing a little dance."
        e 1 "Me too, it was such a hassle setting everything up, but thank goodness it’s over."
        t "You were amazing through and through."
        e 1 "Me? You were the one coming up with the plan. "
        t "Well when you are used to living with bad luck, thinking your way out things just comes second nature."
        t "I’d like to say this is the end of the worst part, but I am sure there is more to come."
        e 1 "Have you finally figured out how to stop both sides from going to war permanently?"
        t "No, not unless if I find some evidence that neither side did it."
        t "Which is impossible since I can’t get near the lizard tribe."
        e 1 "I’ll look around, see what I can find. People are bound to talk."
        t "Do what you can, for now we can breathe easily for a bit. "
        t "We’ll talk later, I need a long nap after what just happened."
        $ Quest.campw = 5
        jump Bull_tribe_map
    elif Quest.campw1 == 3:

        "Thane sits on his rock looking at the village right before him."
        e 1 "Thane? "
        t "Hi [name], you probably heard the news going around the village, we managed to secure a campsite for our tribe. Good job on that."
        e 13 "Then why do you look so upset?"
        t "I’m not going to comment on your choice on which side you wish to help, that’s your right to choose."
        t "But think about how this war is going to affect both sides."
        t "This war will be even harder to end peacefully now."
        t "I hope you will consider your next move carefully."
        t "Now, I need some time alone. Talk to you later."
        $ Quest.campw = 5
        jump Bull_tribe_map
    elif True:

        "You find Thane sitting on his rock looking at the village."
        "He plays with his thumbs and something about the sombre look on his face tells you he is not in a good mood."
        e 1 "Thane, you ok up there?"
        "Thane looks down at you."
        t "They didn’t come back [name]."
        t "My father sent out a team to stop the lizards from building their camp near us, and they never came back."
        "Thane takes a deep breath and continues looking at the village."
        t "I’m not really in the mood to talk. Can you come back later?"
        e 13 "Ok."
        $ Quest.campw = 5
        jump Bull_tribe_map


label Thane_letter:
    if Quest.bombt == 1:
        if Quest.campt > 0:
            "As you approach Thane’s rock you hear him humming a tune to himself."
            t "Mmm...mmhmmm...mmm."
            e 6 "Nice tune there."
            show thane stand at center with dissolve
            t "Oh, [name]. Didn’t see you there."
            "He jumps off his rock to meet you."
            e 1 "Thane... there’s we need to talk about your father and Nauxus."
            "His eyebrows furrow and he nods his head."
            "The two of you head to your usual spot to discuss the two chief’s plans."
            $ Thane.join = 1
        elif True:
            "As you approach Thane’s rock you hear him humming a tune to himself."
            t "Mmm...mmhmmm...mmm."
            e 6 "Nice tune there."
            show thane stand at center with dissolve
            t "Oh, [name]. Didn’t see you there."
            "He jumps off his rock to meet you."
            e 1 "Thane, I could use some advice."
            t "What is this about?"
            e 1 "..."
            "You lean in and whisper into Thane’s ears."
            e 0 "I know what Nauxus and Axel are planning to do in the next phase of the war."
            "Thane is surprised, his mouth drops slightly."
            t "You serious?"
            "You nod."
            t "Then we need to talk about this privately. Come with me."
            $ Thane.join = 1

        hide thane stand with dissolve
        play sound "music/foot1.ogg"
        $ Time.mins = Time.mins +20
        if Time.hours >= 6 and Time.hours <= 17:
            scene bulltree 1 with vslow_dissolve
        elif True:
            scene bulltree 1n with vslow_dissolve
        "By the time you've explained what you've found out Thane is rubbing his forehead with both his hands."
        t "A bomb?! When the heck did he even- A bomb!"
        "Thane paces back and forth in front of you. "
        show thane stand at center with dissolve
        t "I can't believe he would dare to harm innocent lives like that."
        t "So much for the honour of a bull warrior."
        e 1 "Thane..."
        "He stares at the ground for a few seconds before turning to you."
        "His eyes burn with determination."
        t "We can't have any of them have their way, especially my father."
        e 1 "What do you propose?"
        t "I propose we deal with the bomb first."
        t "With some materials I can replace it with a decoy."
        t "Once that bomb fails there won't be a second chance."
        t "Then you need to stop Nauxus from recruiting those rogue lizards."
        t "I don't know what the negotiation is going to be like, but sabotage it somehow. "
        t "Be rude to them, break their things 'accidentally' or just tell them how much Nauxus can't be trusted."
        e 1 "..."
        t "What? You look unsure about something."
        e 1 "I can see that Chief Axel’s plan is hard to defend."
        e 13 "It's just that... Nauxus's plan might buff his army, but it also means an end to a war between their own kind."
        "Thane crosses his arms."
        t "Look, I can't and I won’t stop you if you don’t wish to go through with my plans."
        t "I’m not going to be like my father and force you into this."
        t "Just... I need your help to buy me time so I can gather clues on who the real kidnapper is."
        t "Until then we cannot let this war happen."
        e 1 "Can’t we just stop Axel’s plan?"
        "Thane shakes his head."
        t "Any advantage to one side means putting the other at serious risk of getting hurt."
        t "I don’t think it’s a wise move."
        e 1 "..."
        "You scratch the back of your neck and avoid Thane’s gaze."
        t "[name], I need you to decide now what you want to do."
        "{b}{color=#ffd65c}<Warning:{p} You can't change your option anymore after this option.>{/color}"
        menu:
            "Go with Thane’s plan " if True:
                e 1 "Alright, I trust you. Let’s do your plan."
                t "Excellent."
                t "Now the bomb, I know our tribe only makes one kind of bomb."
                t "It is spherical in shape, and has a paper like exterior."
                t "I can make a copy with some paper, pepper,fuse rope and some adhesive."
                e 1 "Where are we going to get glue?"
                t "We can make some from wheat flour and water, basic kitchen materials."
                t "Probably want to grab the pepper too."
                t "I have the paper and I can buy the fuse rope from the store."
                e 1 "Alright, I think I can get the remaining stuff from Snow."
                t "That’s great!"
                t "We haven’t much time. Accept the job from my father, then go to the tavern to obtain the other materials."
                t "I’ll get to work straight away on the body. I’ll meet you at the tavern to put the bomb together."
                t "The next half of the mission requires you to accept Nauxus’s mission first."
                t "Go with him, and find the opportunity to sabotage the negotiations."
                t "You’re on your own from then on."
                e 1 "Alright, let’s move."
                hide thane stand with dissolve
                "With your plan in sight, you both return to the village. "
                $ Quest.bombt = 2
            "Go with one of the chief’s plans" if True:

                e 13 "Thane, I don’t think I can go through with your plan..."
                t "Oh... I see."
                t "Well, I’m glad you told me. "
                "He looks away disappointed. You feel a sense of regret even telling Thane any of this, but you choose to stick with your decision."
                t "Then... I won’t interfere. You do what you think is right, and I’ll keep to my plans."
                hide thane stand with dissolve
                "He starts walking back to the village."
                e 5 "Thane wait!"
                "He stops and turns his head to the side to look at you."
                e 13 "Is that it? You’re just going to walk away?"
                e 1 "You said you want to stop this war, but you’re not even trying to convince me to go through with your plan?"
                "Thane looks at you without flinching."
                show thane stand at center with dissolve
                t "If you’re asking me to beg for you to choose my side I have too much pride for that, [name]."
                t "More importantly, if you have to ask me to convince you to help me, then you’re not taking what’s going on seriously."
                t "This is a war. There is no room for hesitation or uncertainty to sway from side to side. "
                hide thane stand with dissolve
                t "I know where I stand. Do you?"
                "He leaves."
                $ Quest.bombt = -1
        play sound "music/foot1.ogg"
        $ Time.mins = Time.mins +20
        jump Bull_tribe_map0

label Thane_tavern_talk:
    scene tavern 1
    $ renpy.music.set_volume(0, 0.5, channel = "music")
    pause 0.5
    $ renpy.music.set_pause(True, channel='music')

    $ renpy.music.set_pause(False, channel='Thane')
    $ renpy.music.set_volume(1, 4, channel = "Thane")

    $ Time.mins = Time.mins +5
    show thane stand2 at center with dissolve

    t "Warm meals and friendly smiles."
    t "I couldn’t have asked for a better place to stay over."
    t "Did you want something?"
    label Thane_talktree_tavern:
        menu:
            "Ask about how Thane’s doing here." if True:
                e 1 "Are you settling in ok?"
                t "Yeah, I’m doing pretty good actually."
                t "The bed is very comfy here, I think my muscles are less sore after sleeping here."
                t "Plus not having that many bulls snoring does help with sleep too."
                e 6 "That’s good to hear. Are you getting along with the others?"
                t "I haven’t spoken to them yet, but I will soon."
                t "Wish me luck that I don’t come off as weird in front of them."
                e 5 "What, you’re not the least bit weird."
                t "You say that, but I am pretty unlucky."
                t "What if I break like the stool while I’m talking to Hakan, or I break one of Chet’s stuff by accident, or if I break-"
                e 5 "Ok hold up. It sounds like you’re focusing too much on breaking stuff."
                e 1 "Second, just be yourself. You’ll see everyone here is pretty accommodating. "
                t "Alright, I’ll try not to think too much about it. "
                jump Thane_talktree_tavern
            "Ask about Thane’s future plans" if True:
                e 1 "What are you going to do now?"
                t "I’m still carrying out my investigation."
                t "I’ve got a lead that will meet with me to share what they have on the kidnappings."
                e 5 "That doesn’t sound safe, maybe I should go with you."
                t "No, I have to do this alone, the lead made it clear that there can’t be anyone else."
                t "I’ll be fine, I know how to fight."
                e 13 "Yeah, but it still sounds dangerous."
                t "Have faith in me, [name]."
                t "But, if I disappear for more than a day, then you’d probably want to check the swamp for my body."
                "Thane laughs heartily."
                e 9 "Don’t joke about that. You’re really making me worry."
                t "[name], it will be fine. Trust me."
                t "You should be concerned with what you will do next with father and Nauxus. "
                jump Thane_talktree_tavern
            "Ask about training together" if True:
                e 1 "You know, now that we’re living closer."
                e 1 "Would you want to train with me by any chance?"
                t "Just the two of us?"
                "Thane’s tail stands up."
                e 1 "I mean I could invite Hakan over or maybe Witer if it’s just working out."
                t "Ah... sure, the others could join... I guess."
                e 1 "Yeah, we all can train together and get stronger."
                "Now his tail droops down and he gives you a twitching smile."
                "Almost like he is forcing himself."
                "You shrug and give him a thumbs up."
                jump Thane_talktree_tavern
            "Уйти" if True:
                jump map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
