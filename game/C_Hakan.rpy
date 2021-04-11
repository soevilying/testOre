


label Hakan_meet:
    scene tavern 1
    $ renpy.music.set_volume(0, 0.5, channel = "music")
    pause 0.5
    $ renpy.music.set_pause(True, channel='music')

    $ renpy.music.set_pause(False, channel='Hakan')
    $ renpy.music.set_volume(0.8, 6, channel = "Hakan")

    $ Time.mins = Time.mins +5
    if EF.hakan == 1:
        $ EF.hakan = 2
        show hakan stand at center with dissolve
        h "A butler and a barely young adult shark travelling together. "
        e 1 "Something the matter?"
        h "It just makes me think about the past. Unhappy memories that sort of thing."
        e 1 "Is this about that partner of yours?"
        h "Hey, my mug is empty. I’m going to call another round. You want one?"
        e 13 "Hakan, you’re not answering my question."
        h "{size=+8}And I am not answering it, damn it. Get a clue.{/size}" with vpunch
        "You flinch back at how angrily Hakan spoke to you."
        "He quickly realizes what he’s doing and pulls himself back."
        h "Sorry, please… just drop it."
        e 1 "Ok, we can talk about other things."
        jump Hakan_talk
    if Roushk.hakan_e == 1:
        $ Roushk.hakan_e = 2
        show hakan stand at center with dissolve
        h "I’m going to miss that Roushk guy."
        h "We never really settled who was the strongest. "
        e 6 "Must you challenge every new person that comes to the tavern?"
        h "Only the ones I find attractive."
        e 5 "(Oh, ohhhhh.)"
        h "Now what do you want Fuzz Butt?"
        jump Hakan_talk
    if Roushk.hakan == 1 and Roushk.barn ==1:
        show hakan stand at left with dissolve
        show roushk stand at right with dissolve
        h "Hey, you’re some kind of a big shot from where you came, right?"
        ro "I’m the leader of the lizardmen."
        h "Well you can be a Divine Being for all I care, what I want to know is are you strong enough to beat me in an arm wrestling competition?"
        ro "A fiery fighter I see, you remind me of Rhot back home."
        ro "He’s always itching to pick a fight with me."
        ro "Well, I’ve yet to be defeated in a battle of power."
        h "Big talk, guess most royal types do that."
        h "Are you going to take me on or what?"
        ro "Bring it."
        h "That’s what I like to hear, I’ll set up the table once I’m done with this one."
        h "Yeah, you want something [name]?"
        $ Roushk.hakan = 2
        hide roushk stand with dissolve
        jump Hakan_talk
    if Hakan.quest == 8:
        show hakan stand at center with dissolve
        e 3 "Wow,You finally wake up Hakan."
        e 3 "You have been sleeping for three days and three nights."
        h "Muhh, what hit me?"
        e 1 "Probably yourself, I might have dropped you down the stairs."
        h "Ngh, buzz off [name]. You’re too loud."
        h "Come back some other time. I don’t want to talk right now."
        "Hakan looks pretty hangover, better leave him alone for now."
        $ Time.event1 = Time.days
        $ Hakan.quest = 9
        jump map1
    if Hakan.quest == 9 and Time.event1 == Time.days:
        show hakan stand at center with dissolve
        "Hakan looks pretty hangover, better leave him alone for now."
        jump map1
    if Hakan.meet == 0:
        show hakan stand at center with dissolve
        "You approach the grumpy looking dragon sitting across his unconscious friend."
        "His table reeks of alcohol you feel like someone punched you in the nose with a bottle of beer."
        e 1 "Hi, I’m [name]."
        h "Muhh… buzz off."
        e 5 "..."
        "The fur behind your back stands erect."
        "That was the opposite effect you expected."
        h "Sorry, I’m being rude."
        h "Unless you’re a mug of beer, you can buzz off."
        e 1 "..."
        e 6 "(It looks like if I want to talk to him, I need to get a beer first.)"
        $ Hakan.meet = 1

        jump map1
    elif Hakan.meet == 1 and jane_inv.qty(beer) > 0:
        show hakan stand at center with dissolve
        "The red dragon doesn't respond to your presence."
        menu:
            "< Give him a beer >" if True:
                $ jane_inv.drop(beer)
                $ Hakan.meet = 2
                e 1 "Here’s your beer."
                h "Thanks."
                "He downs the whole mug in one gulp, and slams the mug hard against the table."
                h "Ah, tasty but I am totally not buzzed at all."
                h "Why do I even bother?"
                "You take the empty seat to Hakan’s right."
                e 1 "I’m looking for companions to join me in exploring the forest area until the fog clears up."
                e 1 "Would you be interested?"
                h "No way Fuzz Butt."
                h "My experience with partners is part of the reason why I need to get drunk."
                e 1 "What happened?"
                "Hakan has one furrowed eye on you."
                h "You’re pretty nosy for a new guy here."
                e 5 "I’m just curious."
                e 6 "It’s pretty natural for an adventurer to want to know more about his world."
                e 1 "How else will you find treasure and adventure?"
                "Hakan scowls at you, something you said seems to have pissed him off."
                "He pokes you in the chest so strongly it’s like he is trying to stab your heart."
                h "Your type are pretty thick headed."
                h "So I doubt you’d even remember my advice but I’m going to say it anyways."
                h "You may think that poking your nose into everything is exciting"
                h "You think it's an adventure, but what it really is..."
                "His eyes, the anger in his eyes they’ve soften."
                h "It’s a death sentence. Not every cave needs to be explored."
                h "Some things are best left as is or you’ll regret it. "
                e 8 "You expect me to turn away from adventure with my tail between my legs?"
                e 8 "That’s coward’s talk."
                h "No, that’s how you survive. Ah, enough of this."
                h "You young blood will never understand. He never understood..."
                e 1 " … Is this about your partner?"
                h "....."
                e 13 "I understand..."
                "Hakan turns back to his drink, it seems he is uninterested to continue the topic."
                hide hakan stand with dissolve
                "You look back{w} and see Witer carrying a case of wine from the basement to the bar."
                jump map1
            "Leave" if True:
                jump map1
    elif Hakan.meet ==2 and jane_inv.qty(rum) > 0:
        show hakan stand at center with dissolve
        "The red dragon doesn't respond to your presence."
        menu:
            "< Show him the Fire Rum >" if True:
                $ Hakan.meet =3
                e 1 "Hakan, up for a drink?"
                h "Did you really have to ask Fuzz Butt? Pull up a chair."
                "You take your seat next to Hakan and pass him the mug of Fire Rum."
                "He takes a hearty swig at the drink and burps loudly."
                $ jane_inv.drop(rum)
                h "Fire Rum huh? Been a long time since I tasted it."
                h "Tasty, but nope still as sober as a newborn hatchling."
                e 1 "What is it with you and trying to get drunk?"
                h "Take a good look around you Fuzz Butt."
                h "There’s nothing to do here except eat, sleep, kill monsters and fuck around."
                h "Eventually, you’ll get bored of it. "
                h "So what the heck do you want this time?"
                jump Hakan_talk
            "Leave" if True:
                jump map1

    elif Hakan.meet ==3:

        show hakan stand at center with dissolve
        if Chet.tree == 1:
            h "Hahahhahaha..."
        elif True:
            if Roushk.fight == 1:
                h "You know, that tussle with the lizard earlier has made me thirsty."
                h "Heck, we should get a drink after you’re done dealing with them too. "
            elif True:
                h "Grr…"
        jump Hakan_talk
    elif True:

        e 1 "(I need to get a drink first.)"
        jump map1
label Hakan_talk:
    scene tavern 1
    show hakan stand at center

    if Snow.basement >= 2 and Hakan.quest == 0:
        h "Fuzz Butt, I got a job for you."
        e 1 "Sure, what do you need?"
        h "You’ve been a good pal."
        h "Drinking with me and listening to me prattle on about the past."
        e 6 "Well it’s always fun to have a drinking buddy."
        h "Exactly, and you know good drinks."
        h "That’s why I know I can trust you with this job."
        h "You are going to help me get drunk."
        e 8 "I think I've been trying to do that this whole time."
        h "Well this time it’s different."
        h "You’re going to help me craft a drink strong enough to get a dragon drunk."
        e 1 "There’s actually a drink that can do that?"
        e 1 "How does it work?"
        h "Come on Fuzz Butt, do you really want to hear how dragons get drunk?"
        menu:
            "Tell me" if True:
                h "Think about how you, Snow and all non-dragon related people drink."
                h "In the brain, there’s actually a barrier that is supposed to protect your brain from most toxins."
                h "But, with alcohol it can normally slip through, and mess up how those cells in your brain work."
                h "For us dragons, our barrier is thicker or stronger than other species."
                h "So, alcohol doesn’t affect us in any way."
                h "However, if there is a way to mildly weaken the barrier."
                h "Just enough for alcohol to take effect, then you can get a dragon drunk."
                e 1 "Huh, I never took you for the book smart type."
                h "You really think being a mercenary means you just have to be a mindless brute with a lust for blood?"
                h "My clients sometimes require different services."
                h "So I take it upon myself to understand every type of body, inside and out."
                e 1 "Wow, so what’s the job?"
            "Just give me the job" if True:
                e 1 "Yeah, just skip to what you need me to do."

        h "Talk to Snow to fill you on the details."
        h "Now move your butt, I’m getting thirsty."
        $ Hakan.quest = 1
        jump map1
    elif True:
        pass
    if Hakan.quest == 9:
        h "Hey, Fuzzbutt. Pull up a chair."
        "You take a seat next to Hakan."
        "Just as you sit down you notice two empty bottles to Hakan's right."
        h "Witer, bring me my beer and a plain ale for [name] here."
        "Witer nods and gets to work on the order."
        e 1 "Been enjoying the new beer?"
        h "Can't get enough of it. I'm practicing to build up my tolerance."
        show hakan stand at left with moveoutleft
        show witer stand1 at right with moveinright
        "Witer comes over with bottles of beer in hand."
        hide witer stand1 with moveoutright
        show hakan stand at center with moveinright
        "You both grab a bottle and toast one another."
        h "Just bring me up to speed, what else did I do during that drinking party?"
        e 6 "Nothing much really."
        e 6 "You sang a couple of songs, made some lewd jokes and I took you back to your room."
        h "That’s it?"
        e 13 "Well… you mentioned something about Pierro and a mimic box."
        h "Oh."
        hide hakan stand with dissolve
        "The red dragon scratches his head and lets out a disgruntled sigh."
        show hakan stand at center with dissolve
        h "I guess you’d want to know who Pierro is?"
        e 1 "Only if you want to tell me."
        h "Well I don’t, not to you, not to anyone."
        h "I want to forget Pierro, and that my friend also, is what this beer is for."
        "Hakan chugs down half the contents of the bottle."
        "His satisfied breath is audible, he follows it up by wiping the rest of the golden liquid that spills a little on the side of his mouth."
        "His face turns sober."
        h "Still, did I mention anything about getting into a fight in the tavern?"
        e 1 "No, when did that happen?"
        h "I’m not sure. Maybe it was just a dream."
        h "A very vivid one, I was in the tavern fighting something off…"
        h "I couldn’t quite tell what it was, then we both stabbed each other with our swords. "
        h "There was blood everywhere, and then everything just faded away."
        e 1 "So you had a nightmare of you dying?"
        h "Yeah. Real disturbing, but nothing a good drink can’t fix."
        "The dragon takes another drink of his beer."
        h "Hey, I do remember something from that night."
        e 1 "What?"
        h "I wanted to fuck you hard!"
        "You cheeks instantly flush red. "
        e 10 "Well,Yes. You were drunk. So, people say crazy things when they are drunk."
        "He suddenly leans in close, the smell of beer and vanilla is strong on his body."
        h "I still want to fuck you [name], and I want it now."
        e 7 "… Wha- You’re joking aren’t you?"
        e 7 "No, you must have hit your limit again."
        e 7 "You’re drunk, aren’t you?"
        h "I may be buzzed, Fuzz Butt, but I am sober enough to know I want that ass."
        "You press your hands against his strong chest and hesitantly push him back."
        h "Playing hard to get huh, Fuzz Butt? "
        "Hakan unleashes a deep growl with a cocky grin."
        "He pulls out a small dagger from his side and slams his left hand on the table."
        h "Watch!"
        hide hakan stand with dissolve
        "He starts with a light stab on the area around his thumb then he jumps from one finger to another, stabbing the space between."
        "The knife swiftly dances off of one space onto another with increasing speed, narrowly missing the dragon’s fingers."
        "Hakan does this game for a few more turns, ending it by stabbing the middle of the table with tremendous force."
        "The blade vibrates while standing upright."
        show hakan stand at center with dissolve
        h "How’s that for drunk?"
        h "Now, I’m not going to repeat myself again. You want to do it?"
        $ Hakan.quest = 10
        menu:
            "Yes" if True:
                "You gulp and nod."
                "Hakan crosses his arms and smiles."
                "I’ll go and get freshen up then. Get comfortable."
                "He leans in again and blows hot air into your ear, sending shivers down your spine."
                hide hakan stand with dissolve
                "Driven by your lustful urges you move up to your room with haste, hoping that your protruding bulge goes unnoticed."
                jump Hakan_ride
            "No" if True:
                e 13 "I don’t think so. Not really looking for a quick fuck right now."
                h "Huh, well at least I tried. Guess I ain’t your type."
                "You shrug."
                jump map1
    if Hakan.quest == 11:
        h "Well well, looks like I didn’t wreck that ass too hard."
        e 7 "It’ll take more than that to keep me off my feet."
        e 7 "Plus, it was nice, I’m really glad we got to blow off some steam."
        h "Don’t mention it, I’m up for it again whenever you want."
        e 1 "Thanks, I’ll keep that in mind. And, uhh, about the kiss thing."
        h "It’s nothing personal, I just… I don’t give out kisses to any bloke."
        h "I want it to be someone special who I can call my mate."
        e 13 "I see, does that mean I still have a chance to earn that kiss?"
        "Hakan smiles at you."
        h "You’ll just have to hang around me more to find out."
        h "Now, what do you want?"
        $ Hakan.quest = 12


    if Quest.fes_end == 2 and Quest.fes_hakan == 0:
        $ Quest.fes_hakan = 1
        show hakan stand at center with dissolve
        if Thane.movein != 2 and Quest.fes_result == Axel:
            h "Hey [name], got time to share some beer?"
            e 13 "Not now Hakan."
            e 13 "My head’s all wound up after what happened to Thane in the village."
            h "He didn’t die did he?"
            e 1 "No, but he could have. He… there was blood everywhere."
            h "Hmm."
            "He takes a sip of his beer."
            e 1 "What do I do? I feel so restless."
            h "Then rest, if you’re going to worry yourself to death it won’t help."
            h "You’ll need a clear head if you want to help Thane and the tribes."
            e 1 "It doesn’t feel easy."
            h "That’s why you drink, and talk to me for a bit."
            "He hands you a bottle of beer."
            e 13 "Ok."
            "You accept Hakan’s offer and take a few minutes to drink and talk."
            "It doesn’t help you solve your worries about Thane or the two tribes, but having someone to listen to your concerns helps."
        elif Thane.movein == 2 and Quest.fes_result == Axel:
            "Hakan is downing beer after beer."
            e 1 "Hey, you want to talk?"
            h "Sure, I’m going in my head the many, many traps we can set up to protect the tavern."
            e 1 "Traps?"
            h "Yes, traps."
            h "Just because we didn’t find the monster today doesn’t mean it won’t show up tomorrow."
            e 1 "But what if it isn't a monster, what if it was someone from one of the tribes?"
            h "Do you believe that?"
            "He puts his beer on the table."
            e 13 "I don’t know what to believe. I don’t have all the facts."
            h "Then it sounds like you got to go out there and find them."


        elif Thane.movein ==2 and Quest.fes_result == Nauxus:
            e 13 "Hakan."
            h "Waddya want Fuzzbutt?"
            e 1 "Thanks for helping Thane while I was away, and for dealing with Axel."
            h "It was no big deal. "
            h "Buy me a beer and tell me all about this lizard festival you went to if you want to reward me."
            e 5 "What? After all that’s happened the night, you’re in the mood for a story?"
            h "After the night, it’s exactly what I need. "
            h "No warrior can function if they are all dark and brooding all the time."
            h "So share… Please?"
            e 13 "Ok!"
            "You join Hakan for a drink and tell him about the lizard festival."
        elif True:

            e 13 "I’ve got some bad news."
            e 1 "I think the bulls and the lizards are about to go to war."
            h "Haven’t they already done that?"
            e 1 "Yeah, but this is actual war, war. "
            h "So all the things before this was what?"
            e 1 "Just sizing up the enemies I guess."
            h "I’ll never understand tribe politics."
            h "Gives me a headache just thinking about it."
            h "Which is why mercenary work is more my style."
            h "Just point me to the person you want to take care of."
            "Hakan performs a neck cutting motion with his left thumb."
            e 1 "Well keep those mercenary skills sharp."
            e 13 "We don’t know what will happen next."
    if Parif.hakan_first == 1:
        $ Parif.hakan_first = 2
        e 1 "So Parif’s back."
        h "Damn right, I’ll finally get good meat to go along with my beer."
        e 1 "What can you tell me about him?"
        h "A good deer, and an even better chef."
        h "I like drinking with him."
        e 6 "Oh, so he can match you in drinks?"
        h "No one can match me in how much I can drink."
        h "Parif is just good company. We get each other."
        e 6 "That’s sweet."
        h "So, what else do you want to talk about?"



    menu:
        "Find some topics to chat" if True:
            label Hakan_chattree:
                show hakan stand at center
                menu:
                    "Offer self for company" if Witer.squat < 4 and Hakan.quest < 10:
                        e 1 "Well a brawny dragon like yourself deserve a strong company in kind."
                        "You puff out your chest and give him a confident smile."
                        "He chuckles in response."
                        h "Boy you sure don’t wait to beat around the bush."
                        h "Is that how you were taught on how to pick someone up?"
                        "You break your smile and rub the back of your head."
                        e 3 "Mating with others in my tribe is a common activity."
                        e 4 "During our festivals it's tradition to mate with the elders to carry on their blessings."
                        e 4 "So, yes, I know what it means to pleasure a partner!"
                        h "Pleasure doesn’t mean you know how to get one."
                        "You turn to where Snow would usually stand and look at his spot in silence for a few seconds."
                        h "Hah! Well then Fuzz Butt, good luck with your tribal techniques."
                        e 9 "What?"
                        "You cross your arms in a huff."
                        e 12 "If you’re so good at it, how’d you do it?"
                        hide hakan stand with dissolve
                        "Hakan looks straight at you."
                        "He inches closer never taking his eyes off of your face."
                        "Your heart beats faster and your cheeks flush a little as you try to avert your gaze."
                        "With his mouth just inches away from your face."
                        "You feel his breath hotter than anyone you ever met blow softly into your ear."
                        show hakan stand at center with dissolve
                        h "If you have to ask, you’re not ready for it yet."
                        "You feel a rush of heat climbing up from the pit of your stomach."
                        "Hakan returns to his the rest of his drink and sips on it."
                        jump Hakan_chattree
                    "Ask about previous partner" if Witer.squat < 4 and Hakan.quest < 10:
                        e 1 "Last time we spoke, you hinted at a partner?"
                        "Hakan sighs and takes another swig of his drink."
                        h "He’s dead."
                        e 13 "I,I’m sorry to hear that."
                        h "Don’t be, he made a stupid move and got himself killed."
                        e 1 "What do you mean?"
                        "He rubs the body of his mug and looks at it as though deep in thought."
                        h "Stupid kid I travelled with a few years back."
                        h "I think, I’m not sure how much time has passed in this foggy prison."
                        h "I’m a mercenary by trade. So I travel to wherever the work takes me."
                        h "One night, I stopped by a tavern by a small town."
                        h "The place was nothing special, it looked more like someone’s house that sold liquor to strangers than a tavern."
                        h "It was a dreavy establishment, the customers were all the farm hands in the town."
                        h "Still, the bartender was pretty sociable and he got me to share about my travels."
                        h "He had a son, a scrawny gecko puberty wasn’t kind to him."
                        h "Didn’t made much of an impression at first, he was just sweeping around."
                        h "But I could tell he was listening, he stayed near the corner of the bar sweeping in one place."
                        h "So, I shared more than usual, added a little extra details to my tales."
                        h "Figured I bring some excitement to the dull tavern."
                        h "Next thing I know before I was ready to move out the next day the gecko came to me."
                        h "Said he’d wanted to be my apprentice."
                        h "Wouldn’t take no for an answer even though I threatened to bludgeon his head in."
                        e 1 "You didn’t say yes did you?"
                        h "I didn’t, but the kid kept following me."
                        h "He kept a distance and I was hoping he’d lose his determination after a day or two but he just kept going."
                        h "I can’t even remember when I eventually took him in as my partner."
                        "Hakan smiles and chuckles."
                        h "He didn’t even know how to hold a sword right."
                        "I had to teach him that and every time he tried to pick one up, he’d topple from its weight."
                        h "Then he heard that rumor…"
                        h "..."
                        "You wait for Hakan to continue but something about the way his forehead furrows tells you that he’s upset."
                        h "Sorry, I’m going to need something stronger to finish this story. "
                        "You choose not to say anything. It isn't the time for it."
                        jump Hakan_chattree
                    "Ask about what he does in the tavern." if Map.bulltribe >= 1 and Hakan.quest < 1:
                        e 1 "What exactly do you do around here?"
                        e 1 "Snow mentioned you were the muscle for the tavern?"
                        h "Same thing you’re doing, mostly odd work for the tavern, and don’t think I’m happy about it."
                        e 1 "Hey, I’m not the one who broke your knee."
                        h "That’s not the point! I just don’t like it when someone muscles in on my job."
                        e 1 "Do you even hear yourself? I’m not stealing your job."
                        e 13 "I’m just here to help till you get back on your feet."
                        h "That’s what they all say."
                        h "What’s more frustrating is that you’re the replacement Snow picked."
                        e 6 "You saying I’m not right for the job?"
                        e 6 " I’ve been training my whole life to be a warrior."
                        e 6 "I know I can protect the tavern."
                        h "Well put up or shut up."
                        "Hakan places his elbow on the table, he’s challenging you to an arm wrestling match."
                        e 1 "You’re on!"
                        if Zalt.str < 8:
                            e 12 "Ngh!"
                            h "Heh."
                            e 12 "Grr."
                            "{b}{color=#c22719}<Strength check failed.>{/color}"
                            "The match ends in minutes. Hakan’s arm barely budged the whole time."
                            e 5 "Best two out of three."
                            h "Hah, I won’t waste my time on you Fuzz Butt."
                            e 12 "Grr…"
                            h "I’m the one who should be mad."
                            h "If you can’t even beat me, how can you say you will protect everyone here."
                            hide hakan stand with dissolve
                            "He stands up and casts a wide shadow over you."
                            "Your ears droop and your heart is chilled by Hakan’s cold glare."
                            show hakan stand at center with dissolve
                            h "Until the fog goes away everyone only has each other here, we’re missing friends and family."
                            h "So, get strong and do your job right, or I’ll throttle you to the floor until you do."
                            "Somewhere inside that threat you cannot help but think that Hakan cares more about the rest than his appearance shows."
                            e 2 "I’ll be back for a rematch."
                            h "I look forward to it then Fuzz Butt."
                            $ Hakan.quest = 0
                            jump map1
                        elif True:
                            h "Grr..."
                            e 12 "Ngh."
                            h "Rarghh…"
                            "{b}{color=#19c22a}<Strength Check success>{/color}"
                            "Both of your arms tremble, neither side wanting to concede."
                            "Hakan’s eyes bulge out at you you almost think they would pop out of his skull."
                            "You let loose a mighty roar and slam Hakan’s hand onto the table, causing his drinking mug to jump a little."
                            h "Fuck, you actually beat me."
                            e 13 "Huff..huff… I meant it when I said I’m not here for you job."
                            e 1 "I just want to help everyone out. Trust me."
                            "Hakan and you exchange strong glares at one another."
                            hide hakan stand with dissolve
                            "He snickers and grabs your hand."
                            "You instinctively think he is about to start a fist fight, but instead he shakes your hand."
                            show hakan stand at center with dissolve
                            h "How could I not trust someone with an arm like that. Do me proud Fuzz Butt."
                            hide hakan stand with dissolve
                            "Hakan grabs you by the forearm and pulls you close and whispers into your ear."
                            h "And if you keep getting stronger, I have a special task for that strong arm of yours."
                            e 10 "... Wait what do you mean by that?"
                            "He ignores your question and hums a melody while turning back to his drink."
                            "At least he is satisfied for now."
                            $ Hakan.quest = 0
                            jump Hakan_chattree

                    "Ask about Hakan’s plans" if Hakan.quest >= 10:
                        e 1 "So, you’ve got the beer. What else you have planned for the rest of your stay here?"
                        h "Well, Snow and I had a heart to heart, I can’t keep mooching off of his charity."
                        h "So, I’ve been picking up some of the small jobs Chet has."
                        h "The pay’s decent, at least it covers the drinks."
                        e 1 "Then that means you can join me on my missions then."
                        h "Not going to happen Fuzz Butt."
                        h "I’ll be damned before I take another partner."
                        h "Plus, you’re doing pretty good on your own, so you won’t need me."
                        e 6 "Thanks for the word of confidence."
                        h "Go find us an earlier way home Fuzz Butt."
                        jump Hakan_chattree


                    "Opinion on bull tribe" if Witer.squat >= 4 and Thane.quest >= 5:
                        e 1 "Have you heard of the bull tribe that lives nearby?"
                        h "Hmm, I remember meeting one or two of them before."
                        h "They used to come by to trade with us."
                        e 1 "Any advice on dealing with them?"
                        h "They’re a tough bunch, I can tell from their physique."
                        h "Best advice is not to make the head bull mad."
                        h "I’ve heard stories about that one."
                        h "He has the thickest head in all the tribe, makes it easier for him to bash in the skulls of those who won’t listen to him."
                        e 9 "Yikes!"
                        jump Hakan_chattree
                    "Opinion on lizard tribe" if Witer.squat >= 4 and Nauxus.meet >= 6:
                        e 1 "I’ve met the lizard tribe, even got a nice place to stay there."
                        h "Did ya now? Does this mean you’ll be leaving us for the rest of your foggy stay?"
                        e 6 "No, I’m just saying they’re pretty nice, especially their leader Nauxus."
                        h "Hmph, one heck of a charmer, that snake."
                        e 1 "I think he’s a lizard."
                        h "No, I mean he’s just too darn perfect."
                        h "Sure, he might have Witer looking at him with adoring eyes, but no one can be that charming."
                        e 3 "You sure you’re just not jealous that Witer likes him?"
                        "Hakan slams the table with his fist."
                        h "No! I’m not. I just look out for him, we don’t know what weirdos creep around the fog, that’s all."
                        e 3 "Alright, Mr. Hot Head."
                        jump Hakan_chattree
                    "About the people living at the lake" if Ebb.meet != 0 and Ebb.tavern != 2:
                        e 1 "Hey Hakan, you wouldn’t believe what I found."
                        e 1 "There’s a cabin by the lake-"
                        h "With a butler orca called Ebb, and his Young Master Flo."
                        hide hakan stand with dissolve
                        "Hakan makes air quotes in the air when he mentions the Young Master part."
                        e 5 "Oh, you already know about them."
                        show hakan stand at center with dissolve
                        h "Everyone here knows about them."
                        h "The kid got kidnapped a few days ago, right about the time I hurt my ankle."
                        h "That orca staggered in here like the undead, dripping blood all over the floor."
                        h "Apparently, he fought off some monster to protect the shark, but couldn’t save him."
                        e 1 "Yeah, I’m helping Ebb get Flo back."
                        h "Good, and while you’re at it, try to work in a good price for bringing the kid back."
                        h "Basic mercenary rule, don’t work for free."
                        e 13 "Honestly I’m not even sure if I can save him in time…"
                        h "Hey! "
                        hide hakan stand with dissolve
                        "Hakan slams the table with his mug of beer."
                        show hakan stand at center with dissolve
                        h "If you have time to worry about bullshit like that, you have time to find the kid."
                        "You’re taken aback by Hakan’s sudden wordy reaction. "
                        h "More so, you’re just doing your job."
                        h "Just, just don’t let it get to you, ok. "
                        hide hakan stand with dissolve
                        "Hakan puts his hands on your shoulder and pulls you close. "
                        "His eyes softened as he looks at you."
                        h "What I’m trying to say is, that kid’s life no matter what happens next, it isn’t on your shoulders to bare."
                        e 13 "Oh, thanks. I wasn’t really thinking about it that far, but I get what you’re trying to say."
                        show hakan stand at center with dissolve
                        h "Good, then get to it. The beer sours when people talk about work around it."
                        hide hakan stand with dissolve
                        jump Hakan_chattree
                    "Back" if True:
                        jump Hakan_talk
        "Ask about sex" if Hakan.quest >= 10:
            if Hakan.quest == 10:
                e 7 "So...does the invitation still open?"
                "Hakan looks at you with a raised eyebrow."
                h "Yes,do you wanna fuck?"
                "You gulp and nod."
                "Hakan crosses his arms and smiles."
                "I’ll go and get freshen up then. Get comfortable."
                "He leans in again and blows hot air into your ear, sending shivers down your spine."
                hide hakan stand with dissolve
                "Driven by your lustful urges, you move up to your room with haste, hoping that your protruding bulge goes unnoticed."
                jump Hakan_ride
            elif True:
                e 6 "Hey, Hakan."
                e 7 "Meet me upstairs later?"
                h "Let me finish this beer, and I’ll bring the lube."
                hide hakan stand with dissolve

                jump Hakan_ride
        "Hakan’s request." if Map.bulltribe >= 1 and Map.boss1 >= 3 and Hakan.quest <= 2 and Hakan.quest >= 1:
            h "What are you doing standing around for?"
            h "Talk to Snow to fill you on the details."
            h "Now move your butt, I’m getting thirsty."
            jump map1
        "Let’s celebrate." if Hakan.quest == 6:
            h "Hah, you did it! I knew I could count on you."
            e 3 "Damn right I did."
            e 3 "Tonight we drink like there’s no tomorrow!"
            show hakan stand at left with moveoutleft
            show witer stand1 at right with moveinright
            w "Hey boys, here’s your drinks."
            w "Just call if you need a refill."
            hide witer stand1 with moveoutright
            show hakan stand at center with moveinright
            h "Ah! Mmm, the flower really enhances the smell of the beer."
            e 3 "I’ll have to take your word for it."
            play Hakan[ "<silence 0.5>", "music/hakan_drunk.ogg" ]fadein 3
            h "A toast- to [name], the slayer of wood, and a friend of the tavern."
            hide hakan stand with dissolve
            "The rest of the tavern chant, “Here, here.”"
            "Hakan raises his mug and you knock yours against his."
            "Your face beams with pride and happiness."
            "Drinking with Hakan feels extra special this time."
            "And for a while you forget about the fog, and all its problems."
            "For now it's just about having a good time with a friend."
            "The first drink goes down with not much funfare."
            "By the second drink Hakan starts to act a little strange."
            show hakan stand at center with dissolve
            h "Witer, get your ass over here."
            h "We got to see who has the bigger balls."
            h "No wait, you don’t have any, but I do! Hahahaha!"
            hide hakan stand with dissolve
            "You and him start singing songs by the fifth mug."
            "You don’t know the lyrics so you just blurt out random sounds."
            "Then everything comes to an end by the eighth drink."
            show hakan stand at center with dissolve
            h "Waaaiiii, bring muh drinxx."
            e 5 "You’ve had enough Hakan."
            e 5 "Snow’s not going to serve you any."
            h "Buh… buh… Eyz. We got to celeplate."
            stop music fadeout 1
            hide hakan stand with dissolve
            scene black with dissolve
            $ renpy.music.set_volume(0, 6, channel = "Hakan")
            "By Snow’s orders you shoulder Hakan back to his room."
            e 7 "Sure, sure, after you sober up buddy."
            scene basement 1 with dissolve
            e 7 "Watch your head, we’re going down the stairs."
            "The Dragon’s Bane beer was stronger than anyone had anticipated."
            "That or Hakan is actually a lightweight."
            "He’s been immune to the effects of alcohol for so long."
            "You wonder if that makes him more susceptible to its effects."
            e 1 "Careful, we’re almost to the foot of the stairs."
            play sound "music/door.mp3"
            scene room 2 with vslow_dissolve
            "You use the key Witer lends you to open their room door and bring Hakan inside."
            show hakan stand_nude1 at center with dissolve
            h "Hehehhehe."
            e 6 "Glad you’re enjoying yourself."
            hide hakan stand_nude1 with dissolve
            "You manage to plop Hakan on the bed."
            "But he suddenly pulls you by the arm,{p}and you’re pulled right into his embrace."
            show hakan stand_nude1 at center with dissolve
            if name == u"Eyvind":
                h "EYVIND! EYVIND! It sounds like Windy!"
                h "I should call you Windy!"
            elif True:
                h "[name]![name]! That sounds so weird."
                h "You look more like a Windy."
                h "I'm going to call you Windy!"
            h "You can call me Haky. Hahaha."
            e "Not so loud, I’m right next to you."
            hide hakan stand_nude1 with dissolve
            "Even in his intoxicated state, his hold on you is strong."
            "Your cheek brushes against his, the stubble of his beard tickles you slightly."
            "It's not the most comfortable position to be in as your hands are stuck to your sides."
            "But a part of you doesn’t mind being so close to the dragon."
            "Hakan turns his face towards you."
            h "I luv boo, Windy."
            e 7 "Yea, love you too buddy."
            "You try to push yourself off of him, but he just hugs you tighter."
            h "I luuvvvvvv you so much. You feel that?"
            "Something hot presses against your butt."
            "Hakan has his tongue sticking out while he giggles at you."
            e 7 "I, heh. I’m flattered, but you’re drunk."
            h "Aww come on, lets just fuck."
            e 10 "…"
            h "You’re so cute, just like Pierro."
            e 1 "Pierro?"
            "Hakan breaks his hug and pulls a hand back to stroke your face."
            "His touch feels tender,{p}but the way he looks at you makes you think he isn’t seeing you."
            h "Pierro, I’m so sorry."
            h "It should’ve been me, not you."
            h "I let you open that chest without knowing better."
            h "I’m sorry, I couldn’t stop it."
            e 13 "Hakan…"
            h "I wish I could’ve changed things."
            h "I wish I knew how to save you from that ghoul."
            h "I’m sorry."
            "He covers his face with his hand to hide that he is crying, but you don’t know what to do."
            "You close your arms around his neck, and just listen to him sobbing."
            "In a few seconds his sobs quiet down a bit into soft sniffles."
            "Just when you think Hakan’s calmed down, he lets out a loud snore."
            e 6 "Heh, good night Hakan."
            scene basement 1 with dissolve
            play sound "music/door.mp3"
            "You pull yourself off of the sleeping dragon."
            "And leave the room key on the dresser before leaving the room."
            play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
            $ Time.hours = Time.hours +3
            $ Hakan.quest = 7
            $ Time.event1 = Time.days

            jump T_basement
        "Leave" if True:
            jump map1

label Hakan_ride:
    $ renpy.music.set_pause(True, channel='Hakan')
    "...{w}..."
    play sound "music/door.mp3"
    scene room 1 with vslow_dissolve

    if Hakan.quest == 10:
        "The moment you return to your room your senses are amplified."
        "Your heart pounds against your chest like the beat of a hundred drums."
        "The mere thought of Hakan making his way up to your room weakens your stance."
        "You hastily remove your clothes, freeing your throbbing manhood."
        "Just then, there’s a loud knock on the door. "
        play sound "music/door.mp3"
        show hakan stand at center with dissolve
        "You open the door and there’s Hakan with his arms outstretched holding the top of the door frame."
        "His large form fills the entire door way."
        "Your cock twitches at the sight of him."
        "He smiles at your reaction and makes his way in. You don't know why but your feet start backing up as he comes closer."
        "Hakan tosses what looks like a small vial of blue liquid onto your bed."
        "Then he turns his attention to you with a grin, and makes his way towards you."
        "Every step he takes, he undoes pieces of his armor."
        "Never taking his eyes off of you, you stare transfixed at his eyes."
        show hakan stand_nude1 at center with dissolve
        "Your naked rump bumps against the wall next to your bed, you cannot back away from Hakan any more. "
        "He stands almost naked except for the small underwear covering his very obvious bulge."
        "He’s at an arm’s reach in front of you. "
        "Hakan strips the underwear, slowly tugging left and right."
        "You bite your bottom lip and your cock twitches again."
        "Hakan chuckles."
        h "I'm not even fully nude and you look like you'll cream yourself any second."
        e 10 "Shut up!"
        "His underwear drops to the floor and his massive tool springs upwards."
        show hakan stand_nude2 at center with dissolve
        "You gasp at the sight of his girthy dick. Its sheer width leaves you speechless."
        h "Go ahead, touch it."
        "He grabs your right hand and guides it to his heavy erection. Your hand just barely covers it. "
        "Hakan growls as you curiously stroke his member. "
        "You can practically feel the hard cock throbbing in your hands."
        "The weight of his cock in your hands makes you pant, you want so much to taste the dragon’s meat club."
        "You’re so lost in enjoying Hakan’s dick in your hand you didn’t notice him grabbing you by the ass."
        e 5 "Woah, what?"
        h "Hang on."
        hide hakan stand_nude2 with dissolve
        "He lifts you off the ground with one hand while the other supports your back."
        "Hakan presses you against his body and falls onto your bed."
        scene black with dissolve
        "The wooden frame creaks under your combined weight."
        scene hakan ride1 with vslow_dissolve
        "You find yourself sitting right on top of Hakan’s stomach."
        "There’s that familiar sensation around your behind that you never forgot since that night."
        "Your bare ass is resting right on top of the dragon’s cock."
        "It feels warmer against your buttcheeks."
        "Holding onto his shoulders your face is just inches away from the smiling dragon. "
        "The heat of his beer-soaked breath engulfs your nose."
        "It tempts you to come closer to the dragon’s mouth."
        "Hakan spanks your right buttcheek."
        e 0 "Hey!"

        "You pull yourself back, there’s no doubt that he has left a red handprint where he spanked you."
        "Your voluptuous rump jiggles from the impact, but before you can rub your butt cheek."
        "He rests his hands on the side of your rump, ruffling your fur. "
        "Almost massaging your bruised ass."
        "The way he kneads your soft ass makes you grip harder on his shoulders."
        "He spreads and pushes your butt cheeks together all the while with a cocky grin on his face."
        "You merely whimper with a look of embarrassment as your dick throbs with excitement."
        "Your cock slides back and forth from the gentle pushes from your behind, until your cock slides right between his bulging pectorals."
        "The smoothness of his scales gripping your cock sends an electric jolt of pleasure up your spine."
        "Your cock blasts a hot wad of pre all over Hakan’s cleavage."

        h "Tell me, how much you want it, pup?"
        e 0 "Please, fuck me. "
        "You feel Hakan’s dick hardening and pressing against your butthole even more."
        scene hakan ride2 with vslow_dissolve
        "The way the cock pulsates against your ass crack as it slowly rises to its full size makes you howl softly."
        e 0 "Fuck, how is that thing so big? It’s not natural."
        h "Does it really matter? You know you just want me to fill you up with it."
        "Hakan’s pecs then clench themselves around your cock with a single flex."
        e 0 "Aahh!"
        "You throw your head up towards the ceiling, and you let out a heavy moan."
        "Hakan’s pecs ripples from the lower pec towards the top."
        "The movement of his chest muscles massages your cock forcing more pre to spew from your tip."
        e 0 "Fuck, what’re you doing to me?"
        "Hakan licks his lips."
        h "Just preparing my dessert."

        h "Now open that hole nice and wide."
        "You rock your hips left and right trying to position your hole right on top of the dragon’s dickhead."
        "The moment you feel the touch of his tip right on your hole your fingers dig deeper into his back."
        e 0 "I don’t...I don’t think it’ll-"
        h "Shh, just trust me. Relax."
        "Hakan pulls the vial of slime and pours a dollop of the liquid."
        "He reaches behind you and rubs the lube all over his dick."
        h "There we go, now do your thing."
        "You position yourself again over the dragon’s dick, you slowly lower yourself and let the large dickhead brush against your waiting hole."
        "Its sheer girth stretches your butthole forcing you to take deep breaths."
        "But the fullness of his rock-hard dick inside you is too much for you to not focus on it."
        "Your face eases from a tight teeth grinding wince into a satisfied grin as your hole begins to loosen up to Hakan’s member."
        "You close your eyes and focus on the sound of Hakan’s breathing."
        "Slowly, inch by inch Hakan’s dick slides into your hole."
        scene hakan ride3 with vslow_dissolve
        "Panting heavily, you push your ass to its limits, your buttcheeks barely reaches the base of his dick."
        h "That’s it, pup. Take it all in."
        scene hakan ride4 with vslow_dissolve
        e 0 "Aah! Too big!"
        scene hakan ride5 with dissolve
        h "Hehe, your tight ass feels so good on my cock. Now get ready pup!"
        scene hakan ride4 with dissolve
        "Hakan lifts you by the ass, his shaft slides partway out of you before he rams the entire length inside you."
        "You wince in pain trying to accomodate Hakan’s powerful thrusts. "
        scene hakan ride5 with dissolve
        "However, slowly the pain melts away and your body gives in to the waves of pleasure every time Hakan’s dick hits your spot."
        "You don’t even realize your own body is riding the dragon’s dick with intense vigor."
        scene hakan ride4 with dissolve
        scene hakan ride5 with dissolve
        e 0 "Yes, yes, yes! Fuck me harder!"
        h "Yeah! Ride that cock!"
        scene hakan ride4 with dissolve
        scene hakan ride5 with dissolve
        "Both your bodies rub and slide off each other from the torrential sweat dripping down your naked forms."
        "The feeling of your nipples pressing against the dragon’s muscular chest sends tingles down your spine."
        e 0 "Fuck! Aah! Aah! More, more!"
        scene hakan ride4 with dissolve
        scene hakan ride5 with dissolve
        "Your glute muscles clench harder on Hakan's dick."
        "Hakan roars and the bed grunts and squeaks as you both succumb to your desires."
        "You don't want this moment to end but your body screams for Hakan's load."
        scene hakan ride4 with dissolve
        scene hakan ride5 with dissolve
        "The pressure builds up inside your balls, the cum churning and the urge to shoot your hot load is rising with every thrust of Hakan’s cock."
        "Your fingers dig deep into his shoulder blades and he flexes his back muscles in response."
        "Pre gushes from your cock all over Hakan’s abs."
        "Hakan’s movements grow ever more ruthless and faster."
        "The way his eyes fog up and slightly roll upwards to the ceiling tells you he’s close."
        "Pre erupts from his cock like a broken dam, wetting the insides of your ass with its warmth."
        "Your cock screams for release as more pre spews from your tip."
        "The dragon just groans none stop while his grip on your ass gets tighter as climax approaches."
        h "Fuck, how you want it, pup?"
        menu:
            "Inside me" if True:
                e 0 "Yes! Cum inside me. Ah, I’m cumming!"
                with flashbulb
                "With a mighty roar you both unleash your seed."
                scene hakan ride4 with dissolve
                "Hakan’s cum explodes inside you, his warm cum fills your insides like a geyser."
                scene hakan ride5 with dissolve
                "You cum all over Hakan’s hairy chest."
                "Some of the cum flies into his mouth, and the dragon laps it up hungrily."
                with flashbulb
                "Your entire body shudders as he fires another hot load inside you, just as thick and strong before."
                scene hakan ride6b with vslow_dissolve
                "There’s so much cum that streams of it begins to leak out of your ass, coating the dragon’s balls and pubes."
                "Both of you breathe heavily and look longingly into each other's eyes."
            "Spray it all over me" if True:
                e 0 "Don’t you dare cum inside me. Ahh! I can’t hold it anymore!"
                with flashbulb
                "Hakan pulls his dick all the way out of your body with an audible plop."
                h "Argh! Here it comes!"
                scene hakan ride6a with vslow_dissolve
                "His cock fires volleys of cum into the air, the force of his cumshot is so strong some of it hits the wall across from the bed."
                "The sound of cum hitting the floor is drowned out by both of your screams of ecstasy."
                "Your cock fires its cum all over Hakan’s chest, some of it landing on his lips which he licks up happily."
                "Streams of Hakan’s cum dribbles along his shaft and leaks into your hungry butt crack."
                "Panting heavily, you both look at each other with longing eyes."
        "You bend down for a kiss, but Hakan moves his head away."
        h "Sorry kid I don’t lock lips with fuck buddies."
        e 0 "Oh…"
        "He reaches out and strokes your face before pulling you in for a hug."
        "Hakan’s soft dick slides out of you, leaving you feeling slightly empty inside."
        $ Hakan.quest = 11
    elif True:
        "You hastily remove your clothes, freeing your throbbing manhood."
        "Just then, there’s a loud knock on the door. "
        play sound "music/door.mp3"
        show hakan stand at center with dissolve
        "You open the door and there’s Hakan with his arms outstretched holding the top of the door frame."
        "His large form fills the entire door way."
        "Your cock twitches at the sight of him."
        "He smiles at your reaction and makes his way in. You don't know why but your feet start backing up as he comes closer."
        "Hakan tosses what looks like a small vial of blue liquid onto your bed."
        "Then he turns his attention to you with a grin, and makes his way towards you."
        "Every step he takes he undoes pieces of his armor."
        "Never taking his eyes off of you, you stare transfixed at his eyes."
        show hakan stand_nude1 at center with dissolve
        "Your naked rump bumps against the wall next to your bed, you cannot back away from Hakan any more. "
        "He stands almost naked except for the small underwear covering his very obvious bulge. "
        "Hakan strips the underwear slowly tugging left and right."
        "You bite your bottom lip and your cock twitches again."
        "Hakan chuckles."
        "His underwear drops to the floor and his massive tool springs upwards. "
        show hakan stand_nude2 at center with dissolve
        "You gasp at the sight of his girthy dick. Its sheer width leaves you speechless."
        h "Go ahead, touch it."
        "He grabs your right hand and guides it to his heavy erection. Your hand just barely covers it. "
        "Hakan growls as you curiously stroke his member. "
        "You can practically feel the hard cock throbbing in your hands."
        "The weight of his cock in your hands makes you pant, you want so much to taste the dragon’s meat club."
        "You’re so lost in enjoying Hakan’s dick in your hand you didn’t notice him grabbing you by the ass."
        e 5 "Woah!"
        h "Hang on."
        hide hakan stand_nude2 with dissolve
        "He lifts you off the ground with one hand while the other supports your back."
        "Hakan presses you against his body and falls onto your bed."
        scene black with dissolve
        "The wooden frame creaks under your combined weight."
        scene hakan ride1 with vslow_dissolve
        "You find yourself sitting right on top of Hakan’s stomach."
        "There’s that familiar sensation around your behind that you never forgot since that night."
        "Your bare ass is resting right on top of the dragon’s cock."
        "It feels warmer against your buttcheeks."
        "Holding onto his shoulders your face is just inches away from the smiling dragon. "
        "The heat of his beer-soaked breath engulfs your nose."
        "It tempts you to come closer to the dragon’s mouth."
        "Hakan spanks your right buttcheek."
        e 0 "Hey!"

        "You pull yourself back, there’s no doubt that he has left a red handprint where he spanked you."
        "Your voluptuous rump jiggles from the impact, but before you can rub your butt cheek."
        "He rests his hands on the side of your rump, ruffling your fur. "
        "Almost massaging your bruised ass."
        "The way he kneads your soft ass makes you grip harder on his shoulders."
        "He spreads and pushes your butt cheeks together all the while with a cocky grin on his face."
        "You merely whimper with a look of embarrassment as your dick throbs with excitement."
        "Your cock slides back and forth from the gentle pushes from your behind, until your cock slides right between his bulging pectorals."
        "The smoothness of his scales gripping your cock sends an electric jolt of pleasure up your spine."
        "Your cock blasts a hot wad of pre all over Hakan’s cleavage."


        h "Tell me, how much you want it, pup?"
        e 0 "Please, fuck me. "
        "You feel Hakan’s dick hardening and pressing against your butthole even more."
        scene hakan ride2 with vslow_dissolve
        "The way the cock pulsates against your ass crack as it slowly rises to its full size makes you howl softly."
        e 0 "Fuck, this thing never gets easier."
        h "You know you love it Fuzz Butt."
        "Hakan’s pecs then clench themselves around your cock with a single flex."
        e 0 "Aahh!"
        "You throw your head up towards the ceiling, and you let out a heavy moan."
        "Hakan’s pecs ripples from the lower pec towards the top."
        "The movement of his chest muscles massages your cock forcing more pre to spew from your tip."
        e 0 "Fuck, that trick always gets to me."
        "Hakan licks his lips."
        h " No one can resist these pecs."
        "He bounces his pecs."
        h "Now open that hole nice and wide."
        "You rock your hips left and right trying to position your hole right on top of the dragon’s dickhead."
        "The moment you feel the touch of his tip right on your hole your fingers dig deeper into his back."
        e 0 "Got the lube?"
        h "Always, hang on"
        "Hakan pulls the vial of slime and pours a dollop of the liquid."
        "He reaches behind you and rubs the lube all over his dick."
        h "There we go, now do your thing."
        "You position yourself again over the dragon’s dick, you slowly lower yourself and let the large dickhead brush against your waiting hole."
        "Its sheer girth stretches your butthole forcing you to take deep breaths."
        "But the fullness of his rock-hard dick inside you is too much for you to not focus on it."
        "Your face eases from a tight teeth grinding wince into a satisfied grin as your hole begins to loosen up to Hakan’s member."
        scene hakan ride3 with vslow_dissolve
        "You close your eyes and focus on the sound of Hakan’s breathing."
        "Slowly, inch by inch Hakan’s dick enters your hole."
        "Your ass barely reaches the base of his dick."
        h "That’s it, pup. Take it all in."
        scene hakan ride4 with vslow_dissolve
        e 0 "Aah! Too big!"
        scene hakan ride5 with dissolve
        h "Hehe, your tight ass feels so good on my cock. Now get ready pup!"
        scene hakan ride4 with dissolve
        "Hakan lifts you by the ass, his shaft slides partway out of you before he rams the entire length inside you."
        "You wince in pain trying to accomodate Hakan’s powerful thrusts. "
        scene hakan ride5 with dissolve
        "However, slowly the pain melts away and your body gives in to the waves of pleasure every time Hakan’s dick hits your spot."
        "You don’t even realize your own body is riding the dragon’s dick with intense vigor."
        scene hakan ride4 with dissolve
        scene hakan ride5 with dissolve
        e 0 "Yes, yes, yes! Fuck me harder!"
        h "Yeah! Ride that cock!"
        scene hakan ride4 with dissolve
        scene hakan ride5 with dissolve
        "Both your bodies rub and slide off each other from the torrential sweat dripping down your naked forms."
        "The feeling of your nipples pressing against the dragon’s muscular chest sends tingles down your spine."
        e 0 "Fuck! Aah! Aah! More, more!"
        scene hakan ride4 with dissolve
        scene hakan ride5 with dissolve
        "Your glute muscles clench harder on Hakan's dick."
        "Hakan roars and the bed grunts and squeaks as you both succumb to your desires."
        "You don't want this moment to end but your body screams for Hakan's load."
        scene hakan ride4 with dissolve
        scene hakan ride5 with dissolve
        "The pressure builds up inside your balls, the cum churning and the urge to shoot your hot load is rising with every thrust of Hakan’s cock."
        "Your fingers dig deep into his shoulder blades and he flexes his back muscles in response."
        "Pre gushes from your cock all over Hakan’s abs."
        "Hakan’s movements grow ever more ruthless and faster."
        "The way his eyes fog up and slightly roll upwards to the ceiling tells you he’s close."
        "Pre erupts from his cock like a broken dam, wetting the insides of your ass with its warmth."
        "Your cock screams for release as more pre spews from your tip."
        "The dragon just groans none stop while his grip on your ass gets tighter as climax approaches."
        h "Fuck, how you want it, pup?"
        menu:
            "Inside me" if True:
                e 0 "Yes! Cum inside me. Ah, I’m cumming!"
                with flashbulb
                "With a mighty roar you both unleash your seed."
                scene hakan ride4 with dissolve
                "Hakan’s cum explodes inside you, his warm cum fills your insides like a geyser."
                scene hakan ride5 with dissolve
                "You cum all over Hakan’s hairy chest."
                "Some of the cum flies into his mouth, and the dragon laps it up hungrily."
                with flashbulb
                "Your entire body shudders as he fires another hot load inside you, just as thick and strong before."
                scene hakan ride6b with vslow_dissolve
                "There’s so much cum that streams of it begins to leak out of your ass, coating the dragon’s balls and pubes."
                "The both of you breathe heavily and look longingly into each other's eyes."
            "Spray it all over me" if True:
                e 0 "Don’t you dare cum inside me. Ahh! I can’t hold it anymore!"
                with flashbulb
                "With a mighty roar you both unleash your seed."
                h "Argh! Here it comes!"
                scene hakan ride6a with vslow_dissolve
                "His cock fires volleys of cum into the air, the force of his cumshot is so strong some of it hits the wall across from the bed."
                "The sound of cum hitting the floor is drowned out by both of your screams of ecstasy."
                "Your cock fires its cum all over Hakan’s chest, some of it landing on his lips which he licks up happily."
                "Streams of Hakan’s cum dribbles along his shaft and leaks into your hungry butt crack."
                "Panting heavily, you both look at each other with longing eyes."
        "He pulls you in for a warm hug."
        "Hakan’s soft dick slides out of you, leaving you feeling slightly empty inside."
    scene black with vslow_dissolve
    "The two of you fall asleep in each others embrace."
    "..."
    "......"
    scene room 1 with vslow_dissolve
    "When you wake up, you find yourself lying in bed alone."
    "After simply cleaning yourself, you get up and set off."
    $ Zalt.lust = 0
    $ sex = True
    $ Time.hours = Time.hours +4
    $ persistent.CG_hakan_ride = True
    $ Zalt.sex = Zalt.sex +1
    jump Room1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
