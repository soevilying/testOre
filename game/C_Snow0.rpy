


label Snow_meet:
    scene tavern 1
    show snow stand at center with dissolve
    $ renpy.music.set_volume(0, 0.5, channel = "music")
    pause 0.5
    $ renpy.music.set_pause(True, channel='music')

    $ renpy.music.set_pause(False, channel='Snow')
    $ renpy.music.set_volume(1, 4, channel = "Snow")

    $ Time.mins = Time.mins +5
    if Roushk.snow_e == 1:
        $ Roushk.snow_e = 2
        show snow stand at center with dissolve
        s "So, Roushk went back?"
        e 1 "Yeah, he left."
        e 13 "He didn’t want to say goodbye to everyone, it would break his heart."
        s "What a sweet soul, but I’m glad he’s gone home."
        s "Who knows how long it will take for this fog to let up for us."
        e 13 "We’ll figure it out."
        s "So, need anything?"
        jump Snow_menu
    if Roushk.snow == 1 and Roushk.barn ==1:
        show snow stand at left with dissolve
        show roushk stand at right with dissolve
        ro "So you’re the owner of this tavern."
        show snow stand1 at left with dissolve
        s "That’s right. You can come to me for any kind of brew."
        s "I also double as the chef sometimes. "
        ro "Do you get your ingredients from the forest?"
        s "Most of them, but things like seasonings, I have them stored in bulk when I manage to leave the forest."
        ro "I am impressed by how much you do around here."
        ro "Alas, that must be the burden of he who wears the crown."
        show snow happy1 at left with dissolve
        s "What do you mean?"
        ro "I mean that you seem like the leader of this rowdy bunch."
        ro "And I can see that means you have a lot of responsibilities to keep this place running and keeping morale high."
        ro "I am impressed by your leadership."
        show snow stand at left with dissolve
        s "Well now, you’re going to make me blush. Here, have a beer on the house."
        ro "Thanks."
        s "What about you [name], need anything?"
        $ Roushk.snow = 2
        jump Snow_menu
    if Map.boss1 >= 3 and Map.basement == 0:
        s "Hey kid, come here for a second."
        e 1 "Hey Snow, got any work for me?"
        show snow happy at center with dissolve
        s "More of a chore than a job."
        s "Hakan just finished the bar’s entire supply of rum."
        show snow happy1 at center with dissolve
        s "I need to restock it, could you pick up a crate of rum downstairs?"
        e 1 "Sounds easy enough."
        show snow stand at center with dissolve
        s "Take this key, it’ll open the basement door right behind the bar."
        "Snow points to a trapdoor near his feet."
        "<You get the basement room key.>"
        $ jane_inv_K.take(basement_key)
        $ Map.basement = 1
        jump map1
    elif True:
        pass
    if Snow.meet==False:
        s "Hey kid, come here for a second."
        e 1 "Yea, what do you need Snow?"
        "The older wolf is massaging his forehead without looking at you."
        "With the other hand he is tapping loudly on the surface of the bar."
        "You've seen this action before."
        "Your father often does this when he is upset."
        hide snow stand
        show snow happy1 at center with dissolve
        s "Look, you remember the monsters from today?"
        e 1 "Yeah, why?"
        s "What did you think about it?"
        menu:
            "Nothing" if True:
                e 1 "He was just another meatbag."
                e 1 "Doubt he could be doing anything like mind control."
                s "I see."
            "Fighting it felt good" if True:
                e 7 "I’ll admit when our bodies pressed against each other while we were fighting, I was kind of turned on."
                s "I didn’t need to know that, and that’s not what I meant."
            "They looked tasty." if True:
                e 1 " It looked like it had a lot of meat on its bone."
                e 3 "I wonder how it would have tasted?"
                e 6 "You think skull demon meat would cook better grilled or boiled?"
                s "It doesn’t matter how you cook it, what matters is how you season it."
                s "And that’s not the point. We’re getting off track."

        hide snow happy1
        show snow stand at center with dissolve
        s "There was something weird going on when I went out to gather supplies."
        s "I was attacked by a trio of slimes."
        s "The thing is the slimes weren’t fighting in their usual pattern."
        s "Usually they came one by one, and could barely hit a barn door with their lunges."
        s "This time, they were more... organized."
        s "One snuck up on me while the others were keeping me busy."
        e 1 "That doesn’t mean much. It could be you weren’t paying attention."
        hide snow stand
        show snow stand1 at center with dissolve
        "Snow glares at you."
        e 5 "I mean, maybe."
        hide snow stand1
        show snow happy1 at center with dissolve
        s "Either way, I need you to go in to the forest and look around."
        s "The timing is just too perfect to be a coincidence."
        s "Weird monster shows up one night, the slimes get more dangerous."
        s "See if there’s anything that could be causing the monsters to act differently."
        s "Come back with your findings, and there’ll be a few pieces of coin for you."
        s "And I will give you a free room until you leave."
        $ Snow.meet = True
        hide snow happy1
        jump map1
    if Snow.fish == 0 and Time.days > 9 and Time.hours >=6 and Time.hours <=12:
        hide snow stand at center with dissolve
        "Snow is standing behind the counter as usual."
        "But he has a wooden box next to it with a metal bucket sticking out of it."
        e 1 "Hey, what's with the box?"
        "There's two bottles of beer next to the bucket."
        show snow stand1 at center with dissolve
        s "I'm just packing for my fishing trip. Time to get some more meat."
        e 1 "That sounds like fun."
        e 13 "I've fished with my father lots of time back in the village."
        s "I figured as much. You want to come along?"
        menu:
            "Yes" if True:
                e 3 "Yes, definitely, absolutely, ok. I want to go."
                "Your tail wags vigorously, bumping the stool next to you."
                "Snow smiles warmly as his tail wags happily too."
                show snow laugh1 at center
                s "I appreciate your company,kid."
                show snow stand at center with dissolve
                s "Hakan or Chet usually goes with me to fish."
                s "But Hakan doesn’t like waiting for the fish to bite, and Chet can talk my ear off about the wares he wants to push."
                s "Come on, you can help me carry the box, I’ll just grab the fishing rods and bait, and we’ll head out."
                s "Tell me when you are ready."
                $ Snow.fish = 1
                jump Snow_menu
            "No" if True:
                e 1 "No thanks, I've got something else to do."
                s "Suit yourself."
                s "If you need to buy anything, just wait for me to come back."
                s "See you later."
                hide snow stand1 at center with dissolve
                "Snow carryies his things and walks out of the tavern."
                $ Snow.fish = -1
                $ Snow.fishday = Time.days
                $ Map.lakebank = 1
                jump map1

    if Quest.fes_end == 2 and Quest.fes_snow == 0:
        $ Quest.fes_snow = 1
        show snow happy1 at center with dissolve
        if Thane.movein != 2 and Quest.fes_result == Axel:
            s "You look like shit, did something happen?"
            e 13 "Thane... he’s badly hurt. He came back to the bull tribe all bloodied."
            s "Seriously? What could have done that to him?"
            e 13 "I don’t know."
            e 13 "He was muttering something before he lost consciousness, but I can’t quite make sense of it."
            show snow stand at center with dissolve
            s "Give it some time, you’ve just been in a shocking experience maybe you need some rest."
            e 13 "I’ll be fine. Maybe some sleep will help to ease my tension."
        elif Thane.movein == 2 and Quest.fes_result == Axel:
            s "Good job getting Axel to agree to just send his healers."
            s "I don’t know what I would do if all his men were here."
            e 13 "..."
            show snow stand at center with dissolve
            s "What’s wrong?"
            e 1 "It’s just... he mentioned something about executing the lizard prisoners after what happened to Thane."
            e 13 "I can’t help but feel like that’s the wrong move. What do you think?"
            s "I think the burden of a chief is a heavy one, but the burden of a father is even heavier."
            s "If a chief were to be made to question the value of every enemy he has ever struck down he would not be much of a chief. "
            s "But... if I was a father like him, I think even I would have been guilty of inflicting such an act because it involves my child."
            e 1 "..."
            show snow happy1 at center with dissolve
            s "Let’s not speak more of this."
            s "You need rest or perhaps you need some supplies for your journey."
        elif Thane.movein ==2 and Quest.fes_result == Nauxus:
            s "Can I get you anything?"
            e 13 "Yeah, you have anything for shock from a friend being beaten to near death?"
            s "Well I am no healer, that’s those two bull’s job but I can always recommend some alcohol to numb the senses."
            e 1 "I’m not in the mood Snow."
            e 1 "Seriously, this has been a lot to take in."
            show snow stand at center with dissolve
            s "Steady your nerves kid. We need to prepare for what’s to come."
            s "With all that has happened, I’m not surprised the next step is a full on war between the tribes."
            s "We need to protect ourselves."
            e 13 "Right. Anything you need me to do?"
            s "I’ll call you if I have some jobs, if not just be wary of any activities between the tribes."
            e 1 "Got it."
        elif True:
            e 1 "The lizard village camp was just attacked. "
            s "Dear gods. How bad was the damage?"
            e 13 "The lizards got out safely, but I think they’re really doing it."
            e 1 "They’re going to war."
            show snow stand at center with dissolve
            s "Then we have no time to dally."
            s "I’ll prep the tavern’s defenses with the rest."
            s "If you need supplies you better get your hands on them now."


    if Map.bathroom_0 == 1:
        jump Snow_bathroom_questline
    if Parif.snow_first == 1:
        $ Parif.snow_first = 2
        show snow stand1 at center with dissolve
        e 1 "Hey Snow."
        s "What can I getcha?"
        e 6 "Just wanted to see how you are feeling now that Parif is here?"
        show snow stand at center with dissolve
        "Snow pulls out a mug and pours some beer into it. He lifts the cup and downs the entire mug."
        s "Love it."
        e 6 "You sure? You look tense."
        s "Parif can be a bit of a handful at first, but we always get used to how he runs the kitchen pretty quickly."
        show snow happy1 at center with dissolve
        s "Trust me, I am glad he’s back."
        s "I just hope he doesn’t find out about my experiments."
        e 3 "Good luck with that old man."
        s "You need anything else?"
        jump Snow_menu
    elif True:
        jump Snow_talk

label Snow_talk:
    scene tavern 1
    show snow stand at center
    if Chet.tree == 1:
        s "Err... what do you want?"
    elif True:
        s "What do you want?"
    label Snow_menu:
        menu:
            "Order something" if True:
                e 1 "I need to order something."
                s "Take a look."
                menu:
                    "Beer---$30" if True:
                        s "How many?"
                        menu:
                            "1" if True:
                                $ buy = 1
                            "5" if True:
                                $ buy = 5
                            "10" if True:
                                $ buy = 10
                            "Уйти" if True:
                                jump map1
                        if jane_inv.qty(coin) >=30*buy:
                            $ jane_inv.drop(coin,30*buy)
                            $ jane_inv.take(beer,buy)
                            s "Here is your beer."
                            "You get [buy] Plain ale."
                            jump Snow_menu
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump Snow_menu
                    "Rum---$50" if Hakan.meet >=2:
                        s "How many?"
                        menu:
                            "1" if True:
                                $ buy = 1
                            "5" if True:
                                $ buy = 5
                            "10" if True:
                                $ buy = 10
                            "Уйти" if True:
                                jump map1
                        if jane_inv.qty(coin) >=50*buy:
                            $ jane_inv.drop(coin,50*buy)
                            $ jane_inv.take(rum,buy)
                            s "Here is your rum."
                            "You get [buy] Fire rum."
                            jump Snow_menu
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump Snow_menu
                    "Уйти" if True:
                        jump Snow_menu
            "Find some topics to chat" if True:
                label Snow_chattree:
                    menu:
                        "Talk about the area" if Map.boss1 == 3 and Witer.squat < 4:
                            e 1 "So...you been here the longest right?"
                            s "That I have."
                            e 1 "Then, you’d probably have like a map of everything around here."
                            e 13 "I’m literally waving my sword in the fog whenever I go looking for something."
                            hide snow stand
                            show snow happy1 at center with dissolve
                            s "I never bothered to make a map. What with how the fog is unpredictable about when it opens and closes."
                            s "Sometimes, a familiar place is there one week, the next it’s like it was never there."
                            s "But I can tell you about the area around the tavern that I built over time."
                            e 1 "Sure."
                            hide snow happy1
                            show snow stand at center with dissolve
                            s "After Witer came he wanted somewhere to keep in shape."
                            s "So I let him use the barn to train."
                            s "It’s the large structure you see right outside the main hall."
                            s "We keep a few crates of heavy equipment there so he learnt how to work them to his needs."
                            s "If you take the door to my right, just down the hallway you will reach the bath house."
                            s "It’s shared by everyone so don’t be surprised if you meet someone inside."
                            s "There’s a sauna too."
                            e 7 "Well I haven’t taken a proper bath in a while, might want to visit that place later."
                            hide snow stand
                            show snow happy at center with dissolve
                            s "Of course, we can’t forget the wine cellar downstairs."
                            s "Witer and Hakan also share a room next to the wine cellar."
                            e 10 "Together? Why not give them a room upstairs like me?"
                            s "Upstairs is for guests only. I made an exception for you because technically you don’t work for me."
                            s "Hakan, on the other hand prefers a cold place to rest,{p}and enjoys the company of Witer so they decided to share a room."
                            e 1 "What about Chet? Where does he sleep?"
                            hide snow happy
                            show snow stand at center with dissolve
                            s "He was happy with just making the bottom of the stairs his own room."
                            e 13 "Hmm..."
                            s "I might add more facilities as time goes by, depending on how things go,{p}and if we have the resources."
                            s "Who knows,maybe if you stick around longer I can get you a special room too."
                            e 3 "Thanks for the offer Snow, but let's hope it doesn’t come to that."
                            jump Snow_chattree
                        "Talk about how long everyone has been here" if Map.boss1 == 3 and Witer.squat < 4:
                            e 1 "Just...how long have you all been here?"
                            hide snow stand
                            show snow happy1 at center with dissolve
                            s "It’s impossible to say. Time doesn’t work the same here as it does outside the fog."
                            s "I was the first to arrive here, then Chet. Whenever, the fog would clear I’d head out to restock supplies. "
                            s "Every time I went in and out the time gap was different."
                            s "Sometimes, months had passed when it only felt like days."
                            s "Then there were times when it was just a week when it felt like I’ve been here for a month."
                            e 1 "That doesn’t sound good."
                            e 5 "Wait what if the moment I leave years would have passed?"
                            "There’s a tremble in your voice."
                            hide snow happy1
                            show snow stand at center with dissolve
                            s "It has never happened before."
                            s "From my experience it the time jump never exceeds six months."
                            e 13 "Ok, I’ll keep that in mind."
                            e 1 "What about Witer and Hakan, how long have they been here?"
                            s "Witer arrived before Hakan, but it really doesn’t feel that way."
                            s "Their arrival could have been days apart or months apart. I can’t tell."
                            if Zalt.int >= 6:
                                "{b}{color=#19c22a}<Intelligence Check success>{/color}"
                                e 5 "Wait, you mentioned leaving when the fog clears, but you always never mention if Chet leaves. Does he?"
                                hide snow stand
                                show snow happy at center with dissolve
                                "Snow blinks at you, his mouth twists into a frown."
                                hide snow happy
                                show snow happy1 at center with dissolve
                                "He seems to struggle to come up with an answer."
                                s "I... I think so?"
                                e 1 "How can you not be sure?"
                                s "It’s not something I’ve thought about."
                                s "I’m usually busy thinking about keeping the tavern going."
                                s "I think he leaves too, but maybe you can check with him."
                                e 1 "...Ok? Thanks for the info."
                                hide snow happy1 with dissolve
                                "Snow continues to frown and mumbles to himself."
                                "He looks pretty disturbed that he cannot remember Chet’s whereabouts."
                                jump map1
                            elif True:
                                "{b}{color=#c22719}<Intelligence Check failed>{/color}"
                                e 1 "Ok, thanks for the info."
                                s "Sure."
                                jump Snow_chattree
                        "Talk about the fog" if Map.bulltribe >= 1 and Witer.squat < 4:
                            e 1 "Snow, you would not believe this."
                            e 1 "I found an entire tribe of bull men."
                            hide snow stand
                            show snow happy1 at center with dissolve
                            s "Ah, the path to the bull tribe has opened up again? Excellent."
                            s "They used to trade with us regularly, but suddenly stopped."
                            s "Even the path to their place disappeared."
                            e 1 "Yeah, that’s what has me wondering something about the fog."
                            s "Alright, shoot."
                            hide snow happy1
                            show snow stand at center with dissolve
                            e 13 "..."
                            e 1 "Finding the Bull tribe has the fur stand up on the back of my neck."
                            e 1 "Did you think the fog purposely lead me to find them?"
                            s "That’s hard to say, but I get what you’re saying."
                            s "Their reappearance timed in too well with your arrival to be a coincidence."
                            "Snow pats his chin with the tip of his hook, his eyes staring off at the ceiling."
                            e 5 "What?"
                            s "The last time we lost contact with the tribe, it was after Pierce went running out into the forest."
                            e 1 "No one thought of linking the two together?"
                            hide snow stand
                            show snow happy1 at center with dissolve
                            s "Of course not, Chet and I were more concerned with buffing up the tavern’s defenses in case that lunatic came back and decided he needed our blood for his deity."
                            e 13 "It just doesn’t make any sense..."
                            s "Nothing ever does. You’d be better off just rolling with the punches."
                            hide snow happy1 with dissolve
                            "You push the barstool you’re sitting on backward in a huff."
                            "Again, something else goes unanswered."
                            show snow stand at center with dissolve
                            "Snow rolls his eyes at you and sighs."
                            s "Kid, I can tell you want answers, but frustration is your enemy."
                            s "If a warrior lets his emotions get the best of him his blade won’t even cut through butter."
                            e 1 "(Father... he said something like that before, a long time ago.)"
                            s "I know it’s not easy to hear that you need to just take it easy."
                            s "No one can, you should have seen Witer when he first arrived."
                            s "The lizard was a mess, we had to tie him down before he calmed down."
                            hide snow stand
                            show snow laugh1 at center with dissolve
                            s "So, do what you can to relax, you’re not alone in this."
                            "It seems to be the bartender’s go-to technique, to have you not think about the fog or the situation at hand."
                            e 13 "... I’ll try."
                            hide snow laugh1
                            show snow stand at center with dissolve
                            s "Good, so what else do you need?"
                            jump Snow_chattree
                        "Opinion on bull tribe" if Witer.squat >= 4 and Thane.quest >= 5:
                            e 1 " I’ve met the bull tribe’s leader and his son, Thane."
                            show snow happy1 at center with dissolve
                            s "Huh, never met them before myself."
                            s "Just the traders that come by. What’s the chief like?"
                            menu:
                                "He’s huge" if True:
                                    e 1 "He’s a freaking huge bull."
                                    e 6 "Like literally, that was the biggest bulge I ever saw."
                                    s "Come on kid, is that really the first thing you notice about him?"
                                    e 5 "How can I not? He’s flaunting his package right in front of me."
                                    s "Well men with that kind of “gifts” are definitely going to be full of themselves."
                                    s "Probably flaunts his power a lot too."
                                    e 6 "You sound like you know a lot about well endowed men."
                                    show snow stand at center with dissolve
                                    "Snow is startled. He pauses and blinks at you for a few seconds."
                                    s "I-"
                                    "He coughs."
                                    show snow happy1 at center with dissolve
                                    s "That’s what I heard from rumors."
                                    s "That is all."
                                    s "Just be careful when dealing with someone of authority."
                                    s "You wouldn’t want them to start raiding the tavern because they don’t like you."
                                    s "That is all."
                                    "You wonder if that really is all."
                                    jump Snow_chattree
                                "He’s an asshole" if True:
                                    e 8 "He’s a pain to deal with."
                                    e 8 "He’s just so arrogant, and disrespectful."
                                    e 1 "I mean I’m no chief, but he could learn to be nicer to others. "
                                    e 1 "Doesn’t help that he has it out against the lizard tribe."
                                    s "You'll meet all kinds of types in this world."
                                    s "You just got to know how to deal with them."
                                    e 1 "You're saying he's allowed to hate the lizards?"
                                    show snow stand at center with dissolve
                                    s "Of course not, unjustified hate is as useless as a fire that won't cook meat right. "
                                    s "Regardless of what the chief believes in."
                                    s "I just hope that you don't lose yourself while dealing with these kinds of people. "
                                    e 13 "I don't know. He'll have me run jobs for him."
                                    e 13 "I fear I might cross a line I shouldn't."
                                    "Your hands close into fists under the bar."
                                    "Snow puts his hand on your shoulder and his eyes fall upon yours with a gentle look."
                                    s "You’ll be fine. I know when the time comes, you'll do the right thing [name]."
                                    "You feel Snow's support for you."
                                    jump Snow_chattree
                        "Opinion on lizard tribe" if Witer.squat >= 4 and Nauxus.meet >= 6:
                            e 1 "I found the lizard tribe near the swamp area."
                            e 1 "Nauxus turned out to be the chief of their tribe."
                            show snow happy1 at center with dissolve
                            s "Huh, a chief that comes by to do trading for his own tribe. Isn't that interesting."
                            e 6 "It could be he's pretty down to earth."
                            s "Possible, or he doesn't trust his people enough that he has to micromanage these sorts of things."
                            e 13 "Hmm, I didn't consider that. "
                            show snow stand at center with dissolve
                            s "But he is pretty charismatic, I'll give him that."
                            s "I'm sure even Chet has a hard time rejecting Nauxus's bargains."
                            s "But you should be fine with the lizard tribe."
                            s "I've been there before when I first explored the area. "
                            s "Of course if you ever get into trouble, we have a bed for you right here."
                            e 6 "Thanks, Snow."
                            jump Snow_chattree

                        "About the people living at the lake" if Ebb.meet != 0 and Ebb.tavern != 2:
                            e 1 "I found out about orca living at the cabin by the lake."
                            "Snow blinks and pulls out a rag to wipe the bar."
                            show snow stand1 at center with dissolve
                            e 13 "Yes, and I can’t believe you refused to help him."
                            hide snow stand1
                            show snow happy1 at center with dissolve
                            s "So you met Ebb huh?"
                            e 1 "Why didn’t you tell me about them? I could’ve helped them sooner."
                            s "The same reason applies to you, you’re my guest and I’m not gambling with your life."
                            s "I wanted to wait, give it another week then check up on Ebb. "
                            e 12 "Flo could be dead by then!"
                            hide snow happy1
                            show snow angrys1 at center with dissolve
                            s "Hey, you weren’t there. It was a difficult call I had to make."
                            s "I couldn’t risk anyone’s lives to attempt a rescue mission with a high chance of them not making it back alive!"
                            s "Then tell me if you would have done it?"
                            e 5 "..."
                            show snow stand at center with dissolve
                            s "... I’m sorry I shouldn’t have spoken like that to you."
                            e 13 "No, I’m the one to apologize, I shouldn’t have put you on the spot like that."
                            hide snow stand with dissolve
                            "You look down at your toes while rubbing the back of your arm."
                            show snow stand at center with dissolve
                            s "I’ve said this before, we’re all we got for now."
                            s "That includes you too. So, we have to look out for each other."
                            show snow happy1 at center with dissolve
                            s "I won’t say that I’m thrilled you went to find out about this, but knowing you I’m also not upset that you decided to help them."
                            "You look up at Snow with eyes beaming."
                            e 1 "You knew I took the job?"
                            show snow stand at center with dissolve
                            s "Just be safe out there, if you ever get into trouble come back here, we can help patch you up."
                            s "I don’t want to mount a rescue mission to go find your body."
                            "You nod, and smile a little at the bartender."
                            jump Snow_chattree
                        "Ask about Thane" if Thane.movein == 2 and Quest.fes_end == 2 and Snow.thanetavern == 0:
                            $ Snow.thanetavern = 1
                            show snow stand at center
                            e 1 "I haven’t seen those bull healers ever since they got here."
                            e 13 "Is everything alright with Thane?"
                            s "They come down on their own when no one is looking."
                            s "Last time they asked my permission to set up a camp in the back of the tavern."
                            s "They use it for cooking their meals, so as not to disturb the other patrons here."
                            s "I offered them the place but they really preferred to be alone."
                            e 13 "I want to at least know how Thane’s doing, but I can’t find a second to talk to them."
                            show snow stand1 at center with dissolve
                            s "Relax, it’s just Chief Axel gave them strict rules not to let anyone near Thane while he is recovering."
                            s "Give it some time. He’ll be back on his feet soon."
                            e 1 "I hope you’re right."
                            jump Snow_chattree
                        "Back" if True:
                            jump Snow_menu
            "< Give him the crate of rum >" if Snow.basement == 1:
                $ jane_inv_K.drop(Box_of_wine)
                e 1 "Here’s your rum."
                hide snow stand
                show snow happy1 at center with dissolve
                s "Thanks kid. You can keep that basement key."
                s "Consider it your reward for this job."
                s "Just don’t go bothering Witer and Hakan when they’re in their room."
                s "And, definitely no sneaking free drinks for yourself or that beer obsessed dragon."
                s "If I find even one bottle missing when it shouldn’t be-"
                hide snow happy1 with dissolve
                "Snow shows you his hook hand and flicks it up and down in the air."
                e 3 "You’ll wave your hook angrily at me?"
                show snow stand at center with dissolve
                s "I’ll shove my hook up your ass, kid."
                "You smile nervously and walk away."
                $ Snow.basement = 2
                jump map1
            "Ask about Hakan’s quest " if Hakan.quest >= 1 and Hakan.quest <= 2:
                if Hakan.quest == 1:
                    e 1 "I hear you found a way to make Hakan’s dream of getting drunk come true?"
                    s "You don’t mind helping him?"
                    e 6 "He’s a drinking buddy, I look out for all my friends."
                    s "Alright, then take a look at this."
                    hide snow stand with dissolve
                    "Snow pulls out a white flower you’ve never seen before from his pocket."
                    "Upon closer inspection you see that the flower is actually dried."
                    "Still, you smell an aroma that reminds you of vanilla wafting from the flower."
                    s "This here is the Raco flower. It glows in the dark and is toxic to almost every creature."
                    s "I plan to use it by crushing it into Hakan’s own personal supply of beer."
                    show snow happy1 at center with dissolve
                    s "I call it Dragon’s Bane beer."
                    e 1 "Alright, where can I find this thing?"
                    s "That’s the hard part, wherever this flower grows a tree monster will be there to protect it."
                    e 1 "A tree monster?"
                    s "Yes, the tree monster uses the flower as a way to lure in its victims."
                    s "Unsuspecting children have been known to follow the sweet scent the flower emanates before being devoured by the creature."
                    s "Leaving nothing but their dried up carcases."
                    s "..."
                    s "Make sure you’ll stay safe."
                    s "Just get back here if things turn messy."
                    menu:
                        "Father, I’ll be alright." if True:
                            e 1 "You don’t need to worry."
                            e 1 "I’ve faced dangerous creatures before. Father."
                            e 1 "I’ll be fine."
                            hide snow happy1
                            show snow angry1 at center with dissolve
                            s "Father?"
                            "Your fur stands on end. Snow’s piercing glare cuts you deep."
                            hide snow angry1 with dissolve
                            "Snow reaches out and pinches you by the ear."
                            "He tugs at your right ear hard."
                            show snow angry at center with dissolve
                            s "Ohh, sure kid. Then you listen to your “papa” well."
                            s "Don’t get cocky or you’re getting a spanking harder than that tree can ever give!"
                            e 9 "Ow, ow, ow! Not so hard. I get it, I’ll be careful."
                            s "And?"
                            "Snow pulls your ears harder."
                            e 9 "And you’re not my father. Honest mistake. Ow!"
                            hide snow angry
                            show snow stand1 at center with dissolve
                            "He lets go of your ear, but not before snickering at you."
                            s "You’ll find the tree creature in the deep forest west of here, but before you go, see Chet."
                            s "I’ve requested he make you some protection for this job."
                            $ Hakan.quest = 2
                            jump Snow_menu
                        "Don’t worry old man." if True:
                            e 1 "Don’t worry old man. I’ll take it down like any other enemy."
                            hide snow happy1
                            show snow stand at center with dissolve
                            s "Just don’t underestimate this thing."
                            s "It nearly cost me my other hand to snatch the flower off of it."
                            s "You’ll find the tree creature in the deep forest west of here, but before you go, see Chet."
                            s "I’ve requested he make you some protection for this job."
                            $ Hakan.quest = 2
                            jump Snow_menu
                elif True:
                    s "You’ll find the tree creature in the deep forest west of here, but before you go, see Chet."
                    s "I’ve requested he make you some protection for this job."
                    jump Snow_menu
            "< Give him the Raco flower >" if Hakan.quest == 5:
                $ jane_inv_K.drop(Raco_flower)
                e 1 "I’m back!"
                s "I’m glad you’re back in one piece."
                "You hand over the flowers to Snow."
                hide snow stand
                show snow stand1 at center with dissolve
                s "You did a good job kid."
                s "First round of drinks for you and Hakan will be on the house."
                e 3 "Yes!"
                hide snow stand1 at center with dissolve
                "Snow takes one of the flowers and crushes it into tiny pieces."
                "He then opens up a barrell and drops the torn flower into it."
                "He lifts the barrel and holds it over his head before proceeding to shake it vigorously."
                s "There, that should do it."
                scene black with dissolve
                "Some hours later."
                scene tavern 1 with dissolve
                if Time.hours >= 6 and Time.hours <= 16:
                    $ Time.hours = 19
                elif True:
                    $ Time.hours = Time.hours +3
                "He sets the barrel on the bar and pours a mug of its content."
                "Snow also pours you a mug of beer from another barrell."
                show snow stand at center with dissolve
                s "Go ahead and take a seat with Hakan."
                s "He’s basically drooling at us like he hasn’t had a meal in days."
                s "I’ll have Witer send the drinks over."
                $ Hakan.quest = 6
                jump map1

            "Ask about Witer" if Witer.sleep == 2:
                e 1 "Hey Snow, how are things with Witer?"
                hide snow stand
                show snow happy1 at center with dissolve
                s "Witer? Hmm, the boy’s moving a lot slower than usual, but other than that he seems fine."
                e 1 "So, he’s just working slower, nothing else?"
                hide snow happy1
                show snow stand at center with dissolve
                s "Not that I can tell, is there something I should know about?"
                e 6 "Nah, I’m just trying to make conversation."
                "Snow raises an eyebrow at you."
                s "Hmm, ok."
                "Looks like he doesn’t know anything about Witer’s sleepiness."
                "Maybe there’s someone else who’s seen Witer you can ask about."
                jump Snow_menu
            "Witer's request" if Witer.squat == 1:
                s "Witer wants to see you in the barn."
                s "You'll find him cleaning it in from 6 a.m. to noon."
                e 1 "Ok."
                jump Snow_menu
            "< Go to fish >" if Snow.fish == 1:
                if Time.hours >=6 and Time.hours <=12:
                    e 1 "I'm ready."
                    s "Good,let's go."
                    "You and Snow head out to the bank of the nearby lake."
                    $ Snow.fish = 2
                    $ Map.lakebank = 1
                    $ renpy.music.set_volume(0,0.5, channel = "Snow")
                    $ renpy.music.set_volume(0,0.5, channel = "Hakan")
                    $ renpy.music.set_volume(0,0.5, channel = "Witer")
                    pause 0.5
                    $ renpy.music.set_pause(True, channel='Witer')
                    $ renpy.music.set_pause(True, channel='Hakan')
                    $ renpy.music.set_pause(True, channel='Snow')
                    $ renpy.music.set_pause(False, channel='music')
                    $ renpy.music.set_volume(1, 5.5, channel = "music")
                    jump lake_bank
                elif True:
                    e 1 "I'm ready."
                    s "we’ll have to save the trip for morning. It’s way too late now."
                    s "Get some rest and we’ll head out together at 6 a.m."
                    e 7 "Alright. See you then."
                    jump Snow_menu
            "Thane’s materials" if Quest.bomb_end != 0 and Quest.bombt == 2:
                $ Quest.bombt = 3
                jump Snow_Thane
            "Thane moving in" if Thane.movein == 1:
                e 1 "Snow, I’ve got a favour to ask."
                s "What is it?"
                e 6 "Thane, you remember him?"
                s "Yeah the bull chief’s son. What about him?"
                e 6 "He’s looking for a place to stay."
                s "Well that depends, what happened to his old place?"
                e 1 "He had a falling out with his father."
                e 1 "So, he wants to move out."
                s "That’s terrible, I know a friend who went through the same thing."
                s "The whole ordeal was tough for him."
                s "Had to live off the streets until a kind soul offered him shelter."
                e 1 "So, Thane can stay here?"
                s "If he can pay for a room he can stay but, if he causes any problems while he’s here."
                s "I’ll kick him out, son of a chief or not."
                e 3 "Great, I’ll go get him."
                hide snow stand at center with dissolve
                scene black with vslow_dissolve
                "A few hours later..."
                $ Time.hours = Time.hours +2
                scene tavern 1 with vslow_dissolve
                show snow stand at left with dissolve
                show thane stand2 at right with slow_dissolve
                t "Thank you Master Snow for having me here."
                s "It’s just Snow, and I’m more than happy to provide you shelter."
                hide snow stand
                show hakan stand at left with dissolve
                h "Woah, he’s built like a house. What’s your training regiment?"
                t "Well I’ve made training equipment out of boulders around the village."
                t "It’s important to stay in shape especially with this fog around."
                hide hakan stand
                show witer stand at left with dissolve
                w "I hear you, I have my own equipment in the barn."
                w "Feel free to use it if you want to train."
                t "Thank you, I’d like that very much. Maybe we can train together one day."
                w "That would be wonderful."
                c "That’s a pretty interesting spear you got. How much for it?"
                t "Err... it’s not for sale, I made it myself."
                c "So it’s one of a kind, huh. I’ll give you 100 coins!"
                hide witer stand
                show thane stand2 at center with dissolve
                e 6 "Ok everyone, give Thane some space. Let him unpack first."
                t "Thank you again everyone for being so welcoming. I look forward to getting to know all of you."
                "With the introductions complete Thane heads upstairs to unpack."
                $ Thane.movein = 2
                jump map1
            "Ask Snow about the anvil" if NPC.anvil == 1:
                $ NPC.anvil = 2
                e 1 "I saw an anvil in the barn."
                s "Yeah it’s part of the equipment I brought over for weapon maintenance."
                s "We got strong monsters lurking about, so we need to maintain our weapons and even improve them from time to time."
                s "Feel free to use it whenever you want, everyone has access to it."
                s "But I won’t be supplying the maintenance materials, you’ll have to find them yourself."
                e 6 "Got it, thanks Snow."
                "{b}{color=#19c22a}You can now use the anvil to upgrade your gear.{/color}"
                jump map1
            "Ask about fishing equipment" if Parif.snow_fishrod == 1:
                e 1 "Snow I’m looking for tools to go fishing."
                e 1 "Would you happen to have anything for that?"
                show snow stand1 at center with dissolve
                s "I can lend you my spare fishing rod, and some worms for bait."
                s "The rest is on you."
                e 6 "I’ll take it."
                "<You get a fishing rod and 5 worm baits.>"
                $ Parif.snow_fishrod = 2
                $ jane_inv_M.take(worm_bait,5)
                $ jane_inv_K.take(fishing_rod)
                jump Snow_menu
            "Уйти" if True:
                hide snow stand with dissolve
                jump map1

label Snow_lake_bank_chat:
    menu:
        "Tell me about the person you love" if True:
            e 1 "Well tell me about the person you love."
            s "Oh, so you’re into tales of passion and heartache, huh?"
            show snow happy3 at center with dissolve
            s "Well my last love, it happened many years ago."
            s "It was a cold winter’s day, and I was on my way back to my village with a grand treasure when a heavy blizzard came my way."
            hide snow happy3 at center with dissolve
            "Snow thrusts his arms up high and throws it back down as he describes the blizzard."
            show snow stand2 at center with dissolve
            s "I felt the frigid air piercing my bones."
            s "Every step felt harder than the last, sucking the living breath out of me."
            s "I don’t know when but eventually my body gave in and I fell unconscious."
            "You nod and scootch closer to Snow, your eyes widen with anticipation."
            s "When I came to, I was sitting in front of a cosy hearth."
            s "Layers of blankets wrapped around me, my feet soaked in warm water, and resting on my arm was a beautiful woman."
            e 5 "Yeah? What did she look like?"
            "You come off a bit too enthusiastic as you smile enthusiastically at Snow."
            show snow happy3 at center with dissolve
            "The wolf eyes you suspiciously."
            s "...Like a pretty lady. That’s all you need to know."
            e 6 "Ah, right. Sorry, please continue."
            show snow stand3 at center with dissolve
            s "Anyways, when morning came, I found out that I passed out just outside of her place."
            s "A little logging community and the young beauty was the caretaker of the tavern there."
            s "Her business had practically halted with the winter season, no one was coming in or out of the town."
            "So we had the whole place to ourselves, fully stocked with food and beer."
            s "We shared some drinks and got to know each other better through our stories."
            s "She was a captivating person, laughing at my jokes and listening to my stories intently, and that smile."
            s "At some point I just wanted to talk to her just to get a glimpse at her smile."
            "You nod."
            show snow stand2 at center with dissolve
            s "So... one night, we didn’t have much to do."
            s "I offered to cook dinner and she said it was one of the best burnt meals she ever had."
            s "We both laughed about it."
            s "Then at night... she crept into my bed and we hugged, and one thing lead to another and we kissed... before we..."
            "You held your breath with anticipation."
            hide snow stand2 with dissolve
            "Snow chuckles and stares longingly at the lake."
            "He drinks his beer once more."
            "You both continue drinking your beer."
            show snow happy3 at center with dissolve
            s "Anyways after a night of hot steamy passion, the blizzard gave way a few days later."
            s "I left the treasure to her and told her that I’d find her one day, and we could run a tavern together."
            s "Sadly, when I came back to the town a few months later, the tavern had closed down."
            s "She couldn’t keep it open, and decided to sell the business off saying she wanted to find the guest she had in the winter."
            s "So, not long after I really put my heart into working up enough gold to build my own tavern."
            e 1 "And you picked inside the cursed fog forest to do it?"
            show snow stand2 at center with dissolve
            s "Obviously not, the fog’s just a roadblock at the moment, but it’ll give me a chance to practice my skills before the real thing."
            e 6 "You ever thought of having kids with her?"
            s "Well, I would like a daughter to love."
            e 5 "A d-daughter? Why not a son?"
            show snow stand3 at center with dissolve
            s "Because it’s none of your business kid."
            e 9 "But a son, I mean you can fish with him, you can teach him how to fight."
            s "I can do the same with a girl. Why all the concern about what kind of a kid I want?"
            e 6 "Nothing, just trying to make conversation."
            e 3 "Let’s just change topics."
            "You laugh nervously, but Snow still looks at you suspiciously."
            jump Snow_lake_bank_chat
        "Tell me about how you lost your hand" if True:
            e 3 "Tell me the story about how you lost your hand?"
            show snow happy3 at center with dissolve
            s "Now that’s an exciting tale."
            s "One day, a group of four hooded travelers came to me with a job."
            s "They said they needed a guide to a nearby ruin to find a rare treasure, the eye of the Divine Being of Creation."
            e 1 "The actual eye?"
            show snow stand2 at center with dissolve
            s "No, of course not, how would you even get a body part of a creature that is said to have created every mortal being?"
            s "It’s a relic made out of pure gold said to resemble the eye."
            show snow happy3 at center with dissolve
            s "Anyways, they claimed to be from a religious tribe that worshipped the Divine Being of Creation."
            s "And the relic was something they wanted to bring back to their village and protect."
            s "They paid handsomely of course."
            s "Enough gold to last me a year. So I took the job."
            s "They even had the map and equipment ready."
            s "It started out simple, just knocking out a few monsters and disarming some traps before reaching the chamber that housed the trinket."
            show snow stand2 at center with dissolve
            s "Turns out the eye was just a gold medallion with an eye etched into it."
            s "A bright red ruby was placed where the iris would be."
            s "I figured my job was done, but they wouldn’t let me leave."
            s "Their leader made some nonsense declaration that the eye would not reach its true potential without a sacrifice."
            s "That they needed the eye to destroy the followers of the other DIvine Beings."
            s "So, they turned on me and pulled out their weapons."
            s "Turns out that for a bunch of religious fanatics they were pretty strong fighters."
            s "As good as I was, taking four enemies at the same time was tough."
            s "I have stabs wounds that still hurt a bit when I laugh too hard. "
            s "At some point, I didn’t see one of them come at me from behind and it cost me my hand."
            s "I remember feeling so much anger blinding my senses at that time that I went into a rage and just ripped them apart with my bare hands."
            s "When the fight ended they were all dead and I was practically bathed in blood."
            s "I lost consciousness a bit later, but before everything went dark I could have sworn something came out of that eye, and whispered “Rest.”"
            show snow happy3 at center with dissolve
            s "The moment I came to I was in a temple wrapped up in bandages, my hand that was cut off was still missing though."
            s "The devotees of the temple told me they found me in front of their temple all cut and bruised, so they helped tend to my wounds."
            s "When I asked what temple this was, get a load of this, they were from followers of the Divine Being of Creation too."
            s "I nearly jumped out of my bed when I heard that, but they reassured me they meant no harm and weren’t related to the group I was with."
            s "After I got better, I left for the next big treasure, and that’s the end of that story."
            e 1 "Wow, what’d you think brought you to that temple?"
            show snow stand2 at center with dissolve
            s "Eh, the people there said it must have been the Divine Being of Creation’s own doing, as repayment for the sins of its followers."
            s "But I think I probably just forgot that I walked myself out of there and dreamt up that whole eye apparition. "
            e 1 "Did you ever go claim the treasure again?"
            show snow stand3 at center with dissolve
            s "Of course not, if their group knew their members were gone, they would have probably sent more in search of them there."
            s "I’d be digging my own grave."
            e 13 "Still an encounter with a Divine Being, that would be a legendary adventure."
            s "If it really happened."

            jump Snow_lake_bank_chat
        "That's enough" if True:
            pass
    hide snow stand3 with dissolve
    "You and Snow continue your conversation for a few hours, and manage to catch the two fish you need."
    show snow laugh3 at center with dissolve
    s "Luck is on our side today, I rarely get to catch the amount of fish I want."
    e 3 "That was fun too, listening to your stories. I’m glad I came."
    show snow stand2 at center with dissolve
    s "Yeah, if I ever need some help with some chores I might call you again if you’re up for it."
    e 1 "Sure, just give me a heads up when you need some help."
    show snow stand at center with dissolve
    s "Alright, let's pack up and head back."
    "Talking to Snow reminds you about how you should spend more time with your father when this is all over."
    "It’s been so long since the last time you did something together. "
    "Your father never shared about your mother or how he quit being an adventurer."
    "So you can’t tell if Snow’s experience has anything to do with your father back home."
    hide snow stand with dissolve
    with flashbulb
    "Just as you are about to turn away, a sharp glare catches the corner of your eye."
    "It’s coming from the little island. Is someone there?"
    with flashbulb
    "The shine appears again, your breathing slows and you instinctively think that you need to go after whoever that is."
    "But then a heavy blanket of fog rolls over, and you lose track of where the island even is."
    show snow stand at center with dissolve
    s "Hey, you coming or what?"
    "You rush over to Snow."
    e 5 "I think there’s someone watching us over there."
    hide snow stand with dissolve
    "You point towards the fog."
    show snow happy1 at center with dissolve
    s "Hmm... I don’t see anything."
    e 1 "I swear I saw the glare of someone using something to look at us."
    s "Are you sure it wasn’t just a reflection of the waters?"
    e 13 "I...I think so."
    show snow stand at center with dissolve
    s "Well if you can’t be sure we don’t have a reason to go after it."
    s "Look, we’ll be safer in the tavern, if trouble comes looking we’ll be safer in numbers."
    e 1 "Ok..."
    scene black
    play sound "music/foot1.ogg"
    "The two of you head back to the tavern."
    $ Snow.fish = 3
    $ Time.hours = Time.hours +5
    play sound "music/door.mp3"
    scene tavern 1 with dissolve
    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1

    jump map1




label pay_yes:
    scene tavern 1
    show snow happy1 at center with dissolve
    $ Items.key1 = True
    s "Here is the key,your room is on the second floor"
    "You get 'The room key'"
    s "Follow me,I will show you the room"
    hide snow happy1 with moveoutright
    jump showroom

label showroom:
    scene room 1
    play sound "music/door.mp3"
    show snow stand at center with slow_dissolve
    "You walk in a small room with Snow"
    hide snow stand
    show snow happy
    s "Here we are. I hope you like this room"
    e "Thank you.but.."
    hide snow stand
    show snow stand1 with dissolve
    s "What's up?"
    s "Do you sill wanna to play your 'Daddy and Son' game with me?"

    menu:
        "You should stop joke with me ,Dad" if True:

            e "You should stop joke with me ,Dad,it's not funny"
            e "There are only us here,You can tell me the trut——"
            hide snow stand
            show snow angry1
            s "Stop talking like that, I've NEVER had a kid"
            hide snow angry1
            show snow angry
            s "I need to go now,If you have any questions,come to the bar counter,I will be there"
            hide snow angry with moveoutright



            jump Room1
        "You look almost exactly like my father" if True:

            e "You look almost exactly like my father"
            s "Nyh,You look like me"
            s "If I have a son,maybe he will look like you."
            hide snow stand1
            show snow laugh1
            s "But I've never had a kid"

            s "A good rest will help heal your homesick heart"
            hide snow laugh1
            show snow laugh
            s "I need to go now,If you have any questions,come to the bar counter,I will be there"
            hide snow laugh with moveoutright

            jump Room1
        "..nevermind" if True:

            e "..nevermind"
            s "good,I need to go now,If you have any questions,come to the bar counter,I will be there"
            hide snow stand1 with moveoutright
            jump Room1






label choice1_done:



label Snow_twoletters:
    "You enter the tavern."
    scene tavern 1
    $ Time.mins = Time.mins +20
    "Snow stands by Hakan’s table with his arms crossed. "
    "You get the sense from his intimidating posture that he’s not exactly greeting you with good news."
    show snow stand at center with slow_dissolve
    "It looks like he’s been expecting you."
    hide snow stand
    show snow happy at center with dissolve
    s "You happen to know why a bull and a lizard ran up to me looking for you?"
    e 5 "What, are you ok? Did they do anything to you?"
    s "I’m fine, just surprised they'd jump out of the bush, ask for you, then toss me a letter to give to you."
    s "It was the strangest thing, first the bull comes out then he runs off."
    s "Then a lizard appears and does the same."
    show snow stand1 at center with dissolve
    s "Should I be concerned for you?"
    "He glares at you with stern eyes, the kind of eyes a father would give their child if he suspects that they were hiding something serious."
    "You want to tell him about the war, but the words are stuck behind your throat."
    e 9 "No. I am just doing some odd jobs for Nauxus and Axel. That's all."
    show snow angrys1 at center with dissolve
    show snow stand1 at center with slow_dissolve
    hide snow angrys1
    show snow stand1
    s "..."
    "He hands you the two sealed letters."
    hide snow stand1
    show snow happy at center with dissolve
    s "Alright."
    s "Now, if you’ll excuse me I have a bar to run."
    hide snow happy with slow_dissolve
    "Snow leaves you be."
    "You walk over to a corner of the drinking hall and keep your back turned to the rest."
    "The first letter reads ..."
    n "Come find me in the lizard tribe. We have something to discuss."
    "The next letter reads ..."
    a "Fleabag, get your ass over here. I have work for you."
    e 13 "(It’s never a good sign when both of them are looking for me. I better check out what they want.)"
    $ Quest.bomb_end = 1
    $ Quest.bomb = 1
    $ Quest.bomba = 1
    $ Quest.bombn = 1
    jump map1


label Snow_Thane:
    if Quest.bombt == 3:
        e 1 "Snow, do you happen to have any pepper, wheat flour and water you can spare?"
        show snow happy1 at center with dissolve
        s "I might, I do pride myself on having some of the coolest waters you can drink, but what is this for?"
        e 6 "Umm... I’ve got a friend coming over, we’re making something paper mache."
        hide snow happy1 with dissolve
        show snow stand1 at center with dissolve
        s "..."
        "His good eye falls on you, and you sense he’s trying to read deeper into your plans. "
        "You try to keep up a smile as to avoid getting Snow too involved in this whole debacle. "
        s "Well, I’m definitely not going to give my previous ingredients for art that easily."
        show snow happy1 at center with dissolve
        "Inside your heart, you breathe easily."
        e 1 "Ok, well what do you need?"
        s "Hmm... I got it. "
        hide snow happy1 at center with dissolve
        "Snow pulls from under his bar, a sword."
        show snow happy at center with dissolve
        s "I’ve been so busy with running the tavern lately I haven’t had the time to maintain my blade."
        s "Here, use these oils and concoctions, and start rubbing."
        hide snow happy1 at center with dissolve
        "He lays out a row of bottles in front of you."
        "With his finger, he signals to start from the furthest left bottle then to the right."
        "You pull up a chair and start to get to work."
        "The choice of oils Snow lines up matches the one you have back home. "
        "Pulling the sword from the bar, you are taken off guard by how heavy it is and the tip of the blade hits the floor loudly."
        s "Careful, that’s not a toy."
        "Snow pulls out a bag and starts measuring pepper by the spoonful."
        "You get started polishing his sword with a rough cloth."
        e 1 "..."
        "*squeak squeak*"
        e 6 "This thing’s bigger and heavier than I expected."
        s "You might need to use both hands, and really rub it good along the length of it."
        "*squeak squeak*"
        s "That’s it... rub the tip real good."
        e 5 "This is so hard, it’s just too big."
        "*squeak squeak*"
        s "Most men say the same when they get a good look at my sword."
        e 1 "How much oil should I put on?"
        s "Enough to lather the whole shaft. I want it to just slide right in when I sheath this big boy."
        show hakan stand at left with slow_dissolve
        "You focus on the job at hand. So much so that you didn’t notice Hakan coming up to you."
        h "Sweet, we got a weapon polishing boy now. You can do my axe later."
        h "You might need some more oils though."
        hide hakan stand with dissolve
        "He leans close and whispers into your ear."
        h "My bad boy’s bigger."
        show hakan stand at left with slow_dissolve
        "You feel your cheeks flush red."
        show snow happy1 at right with slow_dissolve
        s "Hands off him Hakan, I ain’t giving my oils away."
        s "You want to polish your weapon, you pay up your bar tab first."
        h "Have a heart Snow."
        "Snow gives him a look but Hakan just acts casually like he didn’t see Snow’s face."
        $ renpy.music.set_volume(0,4, channel = "Snow")
        "Just then, you all hear a knock from the main door."
        t "Hello? Can I come in?"
        h "What the?"
        h "Put me up for some blood cleaning too. I’ll check out who’s this weirdo knocking on our door."
        "You grab Hakan by the wrist and pull him back."
        e 1 "No wait, that’s Thane. "
        e 6 "Just come in Thane."
        hide hakan stand at left with slow_dissolve
        hide snow happy1 at right with slow_dissolve
        play sound "music/door.mp3"
        "The door opens and the bull politely bows before entering."
        "Witer is the first to greet him."
        show witer stand at left with slow_dissolve
        show thane stand at right with slow_dissolve
        w "Welcome to the Tavern of Spear."
        w "I’m Witer, would you be ordering anything today?"
        t "Oh... ah, no. I’m good."
        t "Thank you, I’m Thane. I just need to talk to [name]."
        "Thane waves at you from the entrance."
        hide witer stand with slow_dissolve
        show snow stand1 at left with slow_dissolve
        e 6 "I should go. Snow, I’m done polishing your sword."
        s "Alright, here’s the stuff you asked for."
        "You exchange the sword for the ingredients you need."
        e 1 "Thanks Snow."
        scene black with dissolve
        "You rush over to Thane and take him to the barn."
        play sound "music/door.mp3"
        scene barn 1 with slow_dissolve
        show thane stand at center with dissolve
        t "I’ve got my stuff."
        e 1 "Me too. "
        "You hand Thane the ingredients he needs."
        "The moment he plops himself on the floor his hands move in a flurry attaching the pieces of paper to make the fake bomb."
        "You watch intrigued by the bull’s movements until the bomb is completed."
        t "Done, and done. Here."
        show bullbomb2 at center with slow_dissolve
        "You receive the fake bomb from Thane."
        hide bullbomb2 at center with slow_dissolve
        t "That thing would still explode after it is lit, but all that will happen is a blast of pepper will come out of it."
        t "Let’s hope I did enough to mask its scent."
        t "Accept my father’s task then deliver the fake, along the way make sure you destroy the original bomb."
        t "After that, head straight for the lizard village to deal with Nauxus, do not delay."
        e 1 "Right, I’ll see you back in the bull village once its all done."
        t "Good luck [name]."
        hide thane stand at center with dissolve
        "You head out from the barn and return to the bull village."
        $ jane_inv_K.take(fake_bomb)

        jump forest_map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
