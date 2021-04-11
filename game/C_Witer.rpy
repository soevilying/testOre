label Witer_meet:
    $ renpy.music.set_volume(0, 0.5, channel = "music")
    pause 0.5
    $ renpy.music.set_pause(True, channel='music')

    $ renpy.music.set_pause(False, channel='Witer')
    $ renpy.music.set_volume(1, 4, channel = "Witer")

    $ Time.mins = Time.mins +5
    scene tavern 1
    if EF.witer == 1:
        $ EF.witer = 2
        show witer stand at center with dissolve
        w "That Ebb and Flo look nice."
        e 6 "I’m sensing a “but” coming on."
        w "The only butt coming on is mine."
        "Witer spanks his own ass."
        w "But seriously, I don’t know, I mean he looks young, and he’s travelling with a butler?"
        w "I’m just wondering what happened to his family."
        e 13 "If there’s one thing I know, everyone who ends up in this forest has some kind of a story."
        e 1 "Maybe we’ll find out in due time."
        w "Yeah, I hope so. Anyways, need anything?"
        jump Witer_menu
    if Roushk.witer_e == 1:
        $ Roushk.witer_e = 2
        show witer stand at center with dissolve
        w "Aww, Roushk went back without letting me say goodbye to him."
        e 6 "I’m sure he knows we all will miss him."
        w "So what do you need?"
        jump Witer_menu
    if Roushk.witer == 1 and Roushk.barn ==1:
        show witer stand at left with dissolve
        show roushk stand at right with dissolve
        ro "So you’re Witer right?"
        w "At your services, Chief Roushk."
        w "I’ll make sure your stay here will be entirely satisfying."
        "Witer winks at Roushk."
        ro "Well I’ve been hungry for something really warm and filling."
        w "Oh, would it be a nice, long and hot sausage?"
        ro "You read my mind, a nice thick piece of meat will fill me up good."
        "Witer inches closer to Roushk."
        "Something about the way he looks at the red lizard makes you think he wants more than to just take his order."
        ro "With a nice golden glaze, and maybe filled with some salty cheese?"
        w "I might have some special oil for that."
        ro "Great, then bring me up a plate with a mug of beer."
        w "Huh?"
        hide roushk stand at right with dissolve
        "Roushk walks over to an empty table and sits down."
        "Witer turns to you with his head cocked to a side."
        show witer stand at center with dissolve
        w "What just happened?"
        e 6 "You heard the lizard, serve him his food. "
        "You laugh heartily at Witer."
        "He blushes and crosses his arms."
        w "Well what do you want?"
        $ Roushk.witer = 2
        hide roushk stand with dissolve
        jump Witer_menu
    if Chet.tree == 1:
        show witer stand1 at center with dissolve
        w "[name], that was… I mean, what can I do for you today?"
        jump Witer_menu
    elif Time.days >= 6 and Snow.basement >= 2 and Witer.sleep == 0:
        show witer sleep1 at center with dissolve
        w "Zzz..."
        w "Zzz......"
        e 1 "Witer!"
        hide witer sleep
        show witer stand1 at center with dissolve
        w "Huh? Huh? I’m awake, I’m awake."
        w "Yes uhh, I take orders."
        e 13 "Witer, are you ok? You were asleep while standing there."
        w "I am, I am. Just been tough getting some sleep lately."
        w "You know, Hakan snores, hehehe… So, what do you need?"
        "Witer looks like he hasn’t slept in days."
        show witer stand1 at center with dissolve
        $ Witer.sleep = 1
        jump Witer_menu
    elif Time.days >= 6 and Snow.basement >= 2 and Witer.sleep == 1:
        show witer sleep1 at center with dissolve
        w "Zzz......"
        e 8 "Not again, wake up Witer."
        hide witer sleep1 with dissolve
        "You pat him by the shoulder."
        show witer stand1 at center with dissolve
        w "Huh? Ahhh! Yes. I wasn’t- How can I take your order?" with vpunch
        e 9 "Witer, calm down, why are you screaming?"
        w "My bad, my bad. I was thinking about some scary stories. Silly me."
        "He says that in a very nervous tone for some reason."
        "You wonder if he’s hiding something. Maybe someone knows about this."
        e 1 "...Right. "
        w "So, what do you need?"
        $ Witer.sleep = 2
        jump Witer_menu
    elif Time.days >= 6 and Snow.basement >= 2 and Witer.sleep >= 2 and Witer.sleep <= 6:
        show witer sleep1 at center with dissolve
        w "Zzz..."
        w "Zzz......"
        e 1 "Witer!"
        hide witer sleep1
        show witer stand1 with dissolve
        w "Ahh, I wasn’t sleeping! Ah, what do you need?"
        jump Witer_menu

    if Quest.fes_end == 2 and Quest.fes_witer == 0:
        $ Quest.fes_witer = 1
        show witer stand at center with dissolve
        if Thane.movein != 2 and Quest.fes_result == Axel:
            e 13 "Witer… I-"
            "Witer pulls you in for a hug."
            w "Shh, you’re still hurting. I can see the look in your eyes."
            "You don’t say anything, and just rest your eyes while in the alligator’s embrace."
            w "Is it… is the trouble going to end?"
            e 13 "…"
            e 1 "Not yet, no."
            "Witer breathes deeply."
            w "Then I’ll be here to support you until it is."
            w "Be it hugs or supplies."
            e 1 "Thanks. I needed this."
        elif Thane.movein == 2 and Quest.fes_result == Axel:
            e 1 "Witer are you alright?"
            w "Yeah, strangely enough I am."
            w "What happened to Thane was horrible, but at least he’s stable now."
            e 13 "How are you so calm anyways? "
            w "Let's just say I have a lot of experience with patching up people."
            w "Walden always gets into fights with the other children in the town, and we couldn’t really afford a healer every time."
            w "That, and Hakan and Snow get into scrapes so often that Chet and I have a system for it now."
            w "Anyways, don’t worry about me. You need supplies."
        elif Thane.movein ==2 and Quest.fes_result == Nauxus:
            w "I still can’t get that image out of my head."
            w "Thane coming in here lookin like that."
            w "What’s worse is that whatever did that to him is still out there."
            e 1 "Whatever or whoever did it, I’ll make sure to stop them."
            e 13 "They won’t get away with hurting him or anyone else."
            w "Make sure you do."
            w "I’ll keep the supplies coming, so you can do your job."
        elif True:

            e 1 "I have some news. The lizard camp has been attacked. "
            w "Wha- how close is that to us?"
            e 13 "I am not sure, but we better be prepared in case the war ropes the tavern in."
            w "I need to make a list of supplies we need if we’re going to be in here for the long haul."
            w "You better stay safe while you’re out there."
            e 1 "No guarantees. You know me, I got to search out adventure."
            "Witer blinks at you."
            w "Oh honey if you wanted adventure."
            w "I’ll just put a little something into your food every time I serve."
            e 5 "Wait what?"
            "Witer winks at you and laughs."
            w "Just a joke to lighten the mood."
            w "Do your best out there, I believe in you."
            e 6 "Thanks Witer."
    elif True:

        if Parif.witer_first == 1:
            $ Parif.witer_first = 2
            show witer sleep1 at center with slow_dissolve
            "You find Witer yawning while standing at his spot."
            e 1 "...Witer?"
            show witer stand at center with dissolve
            w "Oh,hey!"
            if Witer.sleep == 7:
                e 5 "Don’t tell me you’re having ghost problems again."
                w "No, not this time."
                w "Parif just kept Snow and I up all night cooking his new jerky recipe."
            elif True:
                show witer stand at center with dissolve
                e 1 "What's wrong, Witer?"
                w "Parif just kept Snow and I up all night cooking his new jerky recipe."
            e 5 "What happened to the old jerky?"
            w "Turned into manure for farming."
            e 9 "That’s a shame, I mean it wasn’t fine dining but the old jerky was good."
            w "To be honest the new jerky tastes really good."
            e 1 "Really? Ok, I’ll try one."
            w "Be warned though, because Chef Parif didn’t want people to think his jerkies are the same as the previous batch."
            w "The price has been raised to match their higher quality."
            e 1 "By how much?"
            w "21 coins."
            e 8 "(21? That’s just one more coin than the original price.)"
            e 1 "I’ll think about it."
            show witer stand1 at center with dissolve
            w "Sure, so anything else you need?"
            jump Witer_menu
        elif True:
            show witer stand1 at center with dissolve
            if Roushk.fight == 1:
                w "My heart races whenever I remember what happened earlier."
                w "Please tell those lizards not to come bother us. "
                w "So, what do you need?"
            elif True:
                w "Hi there, what can I do for you?"


    label Witer_menu:
        menu:
            "Rocks for the bath house" if Map.bathroom_0 == 2 and Map.bathroom == "None":
                jump Snow_bathroom_questline
            "Order something" if True:

                e 1 "I need to order something."

                w "Sure, but I only sell foods."
                w "If you want some alcohol,go and ask Snow."
                menu:
                    "Jerky---$20" if Parif.witer_first != 2:
                        w "How many would you like?"
                        menu:
                            "1" if True:
                                $ buy = 1
                            "5" if True:
                                $ buy = 5
                            "10" if True:
                                $ buy = 10
                            "Leave" if True:
                                jump map1
                        if jane_inv.qty(coin) >=20*buy:
                            $ jane_inv.drop(coin,20*buy)
                            $ jane_inv.take(jerky,buy)
                            w "Here is your jerky."
                            "You get [buy] jerky."
                            jump Witer_menu
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump Witer_menu
                    "Jerky---$21" if Parif.witer_first == 2:
                        w "How many would you like?"
                        menu:
                            "1" if True:
                                $ buy = 1
                            "5" if True:
                                $ buy = 5
                            "10" if True:
                                $ buy = 10
                            "Leave" if True:
                                jump map1
                        if jane_inv.qty(coin) >=21*buy:
                            $ jane_inv.drop(coin,21*buy)
                            $ jane_inv.take(jerky_p,buy)
                            w "Here is your jerky."
                            "You get [buy] jerky."
                            jump Witer_menu
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump Witer_menu
                    "Leave" if True:
                        jump map1
            "Find some topics to chat" if True:
                label Witer_chattree:
                    menu:
                        "Talk about Witer" if Chet.slime <= 2 and Witer.bj == False and Witer.squat < 4 and Witer.sleep < 7:
                            e 1 "I err… never got a chance to talk to you last night."
                            w "Aww, you’re cute but I’m on the clock."
                            w "The old man will not be happy if he catches me chatting up the customers. "
                            w "Maybe next time handsome."
                            hide witer stand1
                            jump map1
                        "Ask about work" if Chet.slime < 2 and Witer.bj == False and Witer.squat < 4 and Witer.sleep < 7:
                            e 6 "Hey, I’m running out of coins again."
                            e 3 "I’m wondering if there’s any work I can do around here so I can keep the room."

                            w " Well I don’t have any work for you at the moment."
                            w "However, the old man told me Chet has an important job for you to take."
                            w "And needs you to deal with it as soon as possible before you do anything else."
                            w "Chet’s always on the lookout for someone to tell him to get his own personal goods."
                            w "And he has the coin to pay for it."
                            w "So, you can always him for other work too."
                            e 1 "Huh, ok. I’ll check him out."
                            $ Witer.meet = True
                            hide witer stand1
                            jump map1
                        "Opinion on Nauxus" if Nauxus.meet == 1 and Witer.bj == True and Witer.squat < 4:
                            e 1 "Hey, what do you think of Nauxus?"
                            w "Nauxus? Well he’s a pretty good lizard."
                            w "Loves his tribe like his own flesh and blood, and he’s always full of advice."
                            e 6 "Yeah, I guess he is."
                            e 1 "Do you know anything about his family?"
                            w "He doesn’t have one, that’s one of the things I have in common with him."
                            e 2 "Witer?"
                            w "It’s ok."
                            w "The only parent I ever knew was Mama Rose, the old lizard at the home for foster eggs."
                            w "She said the three of us came in a neat little basket with just a note saying, “Take care of them.”"
                            w "I was the first one to hatch back then."
                            w "It was kind of scary because as I grew up my brothers hatched later than me."
                            w "Even mama Rose had doubts if they were ever going to pop out of their egg."
                            w "But we all sensed life still inside them."
                            w "So I did everything I could to keep them warm, read them stories, hoping they’ll come out one day."
                            w "When I was twelve, Walden finally hatched from his egg."
                            w "He was a plump brown lizard."
                            w "Mama Rose was pretty surprised because he and I weren't of the same species."
                            w "But Mama Rose told me were siblings regardless, and I felt that way too."
                            w "We grew up together watching over Wally's egg until I turned eighteen."
                            w "That's when I decided to leave the home with Walden and egg Wally."
                            w "The kid really took his sweet time cause he only hatched two years later."
                            w "Just like Mama Rose said, he was a petite thing with bright light green scales, kinda like glass."
                            w "Still he was our little brother."
                            e 1 "Wow, that’s one heck of a family history."
                            e 1 "Mustn't have been easy on you either what with having to raise two siblings on your own."
                            "Witer smiles."
                            w "Yeah, I’m glad mama Rose taught me everything she knew about child rearing and being independent. "
                            w "It wasn’t easy those early years after the home, but I learned quickly to make sure we have a room to rent and full stomachs."
                            w "I’ll work my ass off for my family."
                            e 13 "Heh, a struggling single parent."
                            e 13 "Reminds me of my father, he wasn’t exactly equipped to be a stay at home parent."
                            e 13 "I remember he had to take me to our neighbour’s house every day for dinner."
                            e 13 "At one point, I thought my dad didn’t care about me and was slowly giving me away to the neighbour."
                            w "Was he?"
                            e 5 "Nooo, he went there to learn how to cook for kids, and other household things like sewing."
                            e 2 "Which mind you is not easy after he lost a hand."
                            w "I think that’s sweet."
                            e 1 "Yeah, I wouldn’t be who I am without his help."
                            w "Me too with Mama Rose."
                            w "So, to single parents or caretakers?"
                            hide witer stand1 with dissolve
                            "Witer raises an imaginary mugs of beer."
                            e "To single parents or caretakers."
                            "You play along and toast your imaginary mugs of beer."
                            jump Witer_chattree
                        "Ask about Witer’s escort service" if Witer.bj == True and Witer.squat < 4:
                            e 4 "Just now was…"
                            "Witer puts a finger to your lips."
                            w "You don’t need to say anything. It would be too awkward."
                            e 4 "Haha, yea. Have you always been an escort before the tavern?"
                            w "Yes and no, I had many jobs before coming here."
                            w "I was a waiter, a florist, an artist’s personal model, the list goes on."
                            w "The only thing they all had in common was they didn’t pay enough."
                            w "So, I had no choice, I had two little brothers to feed."
                            e 1 "How old are they?"
                            w "Wally’s eight and Walden is sixteen."
                            w "I was supposed to celebrate Wally’s Hatching Day when I ended up here."
                            hide witer stand with dissolve
                            "Witer looks to the floor with somber eyes."
                            "His voice cracks a little when he starts talking again."
                            show witer stand1 at center with dissolve
                            w "I… I don’t know how they are doing now."
                            w "Walden always acted more mature for his age."
                            w "Always wanting to help me out to get the coins to support our family,"
                            w "But I didn’t want him to abandon his apprenticeship with the local tailor."
                            w "And Wally well he’s the best of us, I managed to save up to send him to school. "
                            hide witer stand with dissolve
                            "Witer's voice lighter as he talks about his siblings."
                            "He breaks into a brief smile when he mentions the school."
                            show witer stand1 at center with dissolve
                            w "Sorry, you didn’t ask for my life story."
                            e 1 "It’s ok, I can relate to having to take care of a little one."
                            e 1 "The kids back in my village are like my family too. "
                            e 1 "And you can’t give up hope.We’ll get back home one day."
                            w "Yeah, thanks. Anyways, was there anything else?"
                            jump Witer_chattree
                        "Ask about the tavern’s history" if Witer.bj == True and Witer.squat < 4:
                            e 1 "What do you know about the tavern?"
                            w "About the same as you do. When I arrived here the only ones were Snow and Chet."
                            w "After they told me about the fog I didn’t dare to go out to explore."
                            e 1 "But you’re built like a warrior, I’m sure you can take a few hits."
                            w "Hey, this body as you already experienced, it’s well maintained for another reason."
                            w "Snow did share with me how he built the tavern."
                            w "He said he was headed to the nearby town to set up his business {p}when the fog covered the roads and he ended up lost in the woods."
                            w "He stumbled upon an abandoned barn, and used it as a shelter for a few days."
                            w "Then something compelled him to fix it up and built the tavern we are in now."
                            e 5 "Something compelled him?"
                            w "Yeah, I have no idea."
                            w "He was pretty hammered when he told me about it."
                            e 1 "That raises more questions than answers."
                            w "I find it easier not to think too much about it."
                            w "Just be glad we have a place to sleep in, away from what's outside."
                            e 6 "Yeah…"
                            w "Anything else you wanted to know?"
                            jump Witer_chattree
                        "Opinion on bull tribe" if Witer.squat >= 4 and Thane.quest >= 5:
                            e 1 "Witer, I finally gained entry to the bull tribe."
                            w "Oh dear, you better pack some extra health potions, those bull tribes are pretty hotheaded."
                            e 1 "You make it sound like they would attack me at random."
                            w "I’m not implying that, just well, the bulls that came to trade before were pretty rough even for traders."
                            w "I swear I couldn’t walk right for days."
                            e 5 "Excuse me?"
                            w "I couldn’t walk right for days, they had me wrestle them and my whole body was sore after getting slammed by their hard bodies repeatedly."
                            e 6 "Oh, that’s what you meant."
                            "Witer looks confused at your statement."
                            jump Witer_chattree
                        "Opinion on lizard tribe" if Witer.squat >= 4 and Nauxus.meet >= 6:
                            e 1 "So, I found the lizard tribe Nauxus comes from. Apparently he’s their chief."
                            w "Seriously? I never pictured him to be the leader kind of guy."
                            w "I thought he was a trader who likes seducing other people for fun."
                            e 6 "Nope, apparently he leads all of them."
                            e 1 "They seem like a friendly bunch."
                            w "I’ll take your word on it, I’ve never been to their tribe."
                            e 1 "Why not?"
                            w "Well other than not really having a reason to go there, it’s pretty dangerous going in blind."
                            e 1 "You mean the monsters?"
                            w "I mean the lizard people."
                            w "As far as I can tell Nauxus isn’t the same species of lizard as them, based on his smell."
                            e 1 "What?"
                            w "It’s basically like someone being in a restaurant long enough and their clothes starts smelling of the food."
                            w "His smell comes from the village he’s in but I can still pick up a scent that’s different coming from him."
                            w "That’s how I can tell he isn’t the same species as them. Am I right?"
                            e 13 "Now that I think about it, he is the only blue lizard there, and he does look different from the rest of them."
                            w "Yeah, makes you wonder why he’s the chief."
                            w "Some lizard tribes don't get along well with one another, and would kill on sight."
                            w "So, I rather play safe and stay away."

                            jump Witer_chattree
                        "About the people living at the lake" if Ebb.meet != 0 and Ebb.tavern != 2:
                            e 1 "Witer, did you know there were people living at the lake?"
                            show witer stand at center with dissolve
                            w "Gosh, you found Ebb? Was Flo with him?"
                            e 13 "No, Flo is still missing. I’m trying to find him."
                            w "Oh, thank goodness."
                            w "When Ebb came by that night, he was a mess, it took me two hours to clean his wounds."
                            w "Broke my heart when I heard Flo was taken, he just reminded me so much of my younger brothers."
                            w "I get why Ebb would want to go out in his beaten up state to save him."
                            w "But I had to agree with Snow that would have been a suicidal move."
                            e 1 "Why didn’t Snow just send someone to help Ebb?"
                            w "Snow just wanted to protect everyone here, he couldn’t agree to Ebb’s plan of just rushing into the monster’s nest blindly."
                            w "Are you going to help Ebb?"
                            e 1 "I am, I’ll do what I can to find Flo."
                            w "Here’s hoping that kid is ok."
                            w "If you need any help to keep you going on this mission just let me know. "
                            hide witer stand with dissolve
                            "Witer then steps close and pulls you into his chest and holds you tight."
                            "Your cheeks press against his well formed pecs."
                            e 5 "Witer?"
                            show witer stand at center with dissolve
                            "Just a good luck hug sweetie."
                            "I’m giving you all the luck I have to keep you safe."
                            "The way Witer’s pecs press up so softly against your face makes you feel warm and secure."
                            "You return his hug by holding him back and pressing him tightly against you."
                            e 13 "Thanks Witer."
                            "Witer strokes your head and frees you from his embrace."
                            w "Now go out there my hero."
                            jump Witer_chattree
                        "Back" if True:

                            jump Witer_menu
            "Tip 210 coins" if Chet.slime == 2 and Witer.bj == False:
                if jane_inv.qty(coin) >=210:
                    $ jane_inv.drop(coin,210)
                    e 1 "Hey Witer, get me a beer."
                    w "Coming right up."
                    hide witer stand1
                    "He quickly dashes behind to the bar to get your order."
                    show witer stand at center with dissolve
                    "Just as he returns and sets down your drink,{p}you slip a pouch of coins on his tray."
                    w "That’s a big tip."
                    e 4 "I’m expecting a big treat."
                    hide witer stand with dissolve
                    "Witer leans close to your right ear."
                    w "Leave your room door open and just relax by the bed.{p}I’ll take a short break."
                    show witer stand at center with dissolve
                    "He brushes his cheek against yours as he pulls away,{p}making you blush and your groin feels warm."
                    hide witer stand with moveoutright
                    e 1 "...."
                    scene black with vslow_dissolve
                    jump Witer_bj
                elif True:
                    e 6 "(Nah,I don't have the money.)"
                    jump Witer_menu
            "Ask about sex" if Witer.bj == True and Witer.cowboy != 1:
                if Witer.squat < 4:
                    e 7 "So, any chance for us to have another romp in my room?"
                    w "We literally just did it. Give a reptile some time, handsome."
                    e 2 "Not even if I have the coin now?"
                    w "Sweetie, the price just increased."
                    e 5 "Hey, how is that fair?"
                    w "Well if I give it to you whenever you want you won’t appreciate it."
                    w "Remember, it’s customary to tip your waiters."
                    w "Now, is there anything else?"
                    jump Witer_menu
                elif True:
                    e 6 "So, it’s been a while."
                    w "Mmmhmm. Been a while, since this?"
                    hide witer stand1 with dissolve
                    "He closes the distance between the two of you and reaches for your crotch, groping it lightly."
                    show witer stand1 at center with dissolve
                    e 10 "Ngh, yeah."
                    e 1 "Any chance we can get together soon?"
                    w "In a while cutie, work’s been keeping me away from my side job."
                    w "Hope you can wait a bit longer."
                    e 7 "It’ll be worth it for you."
                    w "You silver tongue."
                    jump Witer_menu

            "About the night time disturbances" if Witer.sleep >= 4 and Witer.sleep <= 6:
                if Witer.sleep >= 4 and Witer.sleep <= 5:
                    w "I haven't been able to sleep in my bed because of a rock outside my window that I swear is trying to break in and kill me."
                    w "Have you figured out how to deal with it?"
                    jump Witer_menu
                elif True:
                    e 1 "Witer, good news, I’ve dealt with the thing that’s messing with you at night."
                    w "Really? How?"
                    e 3 "Would you believe I learnt a spell to defeat ghosts from another ghost?"
                    w "No, not really, but I don’t care, I’m just glad it’s over."
                    w "It’s not been easy sleeping on the floor, I guess I really need my own bed to sleep in."
                    w "I keep getting these recurring nightmares while I was in your room."
                    w "That and I’ve been really stressed out worrying about that rock."
                    e 1 "Nightmares? What kind?"
                    w "It’s always the same scene, me running away from some large shadow."
                    w "I keep running through the forest but it keeps bringing me back to the tavern."
                    w "Then it gets me. That’s about it really."
                    e 13 "Hmm…"
                    w "Thank again [name]. I don’t know how to repay you."
                    e 3 "Just get enough sleep, and be the tavern’s number one waiter again."
                    w "You got it!"
                    "<[name] gained one Level-up-point.>"
                    $ Zalt.points = Zalt.points +1
                    $ Witer.sleep = 7
                    jump Witer_menu
            "Learn seduction skills" if Nauxus.meet >= 1 and Witer.cha <= 1 and Witer.cha_p == 1:
                if Witer.cha == 0:
                    e 1 "Hey, I learnt a new move from Nauxus to defend against monsters, you gotta see it."
                    w "Now why would I do that? I can’t stand fighting."
                    e 6 "Well I won’t really call it fighting."
                    e 7 "More…. Ummm, more like seducing them into not fighting you?"
                    w "You seduce the enemy? Now that I have to see."
                    w "I know a thing or two about mesmerizing people to get out of a sticky situation."
                    w "Maybe I can give you some tips."
                    e 1 "Why would you ever need to charm someone out of trouble?"
                    w "It’s not always me."
                    w "When you have hot headed siblings and your job is pleasuring other men."
                    w "You gotta be able to diffuse fights or someone's coming home with one finger short."
                    e 14 "Well, I can pull it off, just watch."
                    hide witer stand with dissolve
                    "You strike a few poses at Witer."
                    "He watches intently with a smile on his face."
                    show witer stand at center with dissolve
                    e 7 "So?"
                    w "I don’t know what to say. It was cute?"
                    e 5 "Cute? Were you even watching?"
                    w "Well it takes more than a bubble butt and some poses to get me excited."
                    e 8 "Then, what do I do?"
                    w "Mmm, well try to woo me with words."
                    w "Here, I’ll ask you a few questions."
                    w "And if you can attract me then you’re on the right track to being a master tease."
                    e 8 "Ok!"
                    w "A quick tip, ask yourself what the other person wants to hear."
                    $ Witer.cha = 1
                elif True:
                    w "Wanna another try?"
                    e 1 "Ok!"
                    w "A quick tip, ask yourself what the other person wants to hear."

                w "So, if we were on a date, what kind of present would you bring?"
                $ Witer.cha_p = 1
                menu:
                    "A bouquet of flowers." if True:
                        e 1 "A bouquet of flowers to match your eyes."
                        w "Aww, you’re making me blush."
                        $ Witer.cha_p = Witer.cha_p+1
                    "The evil eye of a slayed dragon." if True:
                        e 3 "The evil eye of a slayed dragon!"
                        w "Ah, thanks I guess."
                    "A sword." if True:
                        e 13 "A sword so we may hunt together."
                        w "Hmm, thanks."
                w "How would you plan a romantic meal with me?"
                menu:
                    "We can have a family meal." if True:
                        e 13 "I could come over and cook something for you, and for your brothers."
                        e 14 "Then while they eat, we sneak into your room, and make love until they notice we’re gone."
                        w "You wouldn’t? I like the sense of danger though."
                    "We can eat naked in bed" if True:
                        e 14 "You, me, naked and eating cream and sauce off each other’s naked bodies."
                        w "My, my, as a waiter I should be against treating food that way."
                        w "But the idea is just delicious."
                        $ Witer.cha_p = Witer.cha_p+1
                    "We can have a picnic under the falls." if True:
                        e 13 "We could pack a basket of food and drinks."
                        e 13 "Then sneak away to a hidden waterfall I know."
                        e 14 "Just us, no one else."
                        w "Mmm, tell me more."
                w "Last question."
                w "If we spent the night together, what would you do in the morning?"
                menu:
                    "Make you breakfast" if True:
                        e 13 "I will wake up early and make you breakfast in bed."
                        "Witer smiles warmly without saying anything."
                        $ Witer.cha_p = Witer.cha_p+1
                    "Hold you close." if True:
                        e 13 "I’d hug you, and just hold you close until you wake up."
                        "Witer smiles warmly without saying anything."
                    "Play with your morning wood." if True:
                        e 4 "I’d rub your hard-on until you wake up and we continue the fun."
                        "Witer smiles warmly without saying anything."
                if Witer.cha_p == 4:
                    hide witer stand with dissolve
                    "Witer takes a deep breath and fans himself with his hand."
                    show witer stand at center with dissolve
                    w "Impressive, you know your way with words."
                    w "I think you’re pretty charming already."
                    e 3 "And I didn’t even have to take my loincloth off."
                    "Your feel more confident in your ability to charm others."
                    "{b}{color=#19c22a}<[name]'s charm increase one point!>{/color}"
                    $ Zalt.cha = Zalt.cha+1
                    $ Witer.cha = 2
                    jump Witer_menu
                elif True:
                    w "Mmm, you got to work on it."
                    e 5 "Really? This is a lot harder than I thought."
                    w "Just keep trying, it’s part of seducing someone."
                    w "Trying to think about what they would like."
                    w "Sometimes you might get it wrong but that tells you a lot about them too."
                    $ Witer.cha_p = 1
                    jump Witer_menu
            "Leave" if True:
                jump map1


label Witer_bj:
    stop music
    $ renpy.music.set_pause(True, channel='Witer')
    "...{w}..."
    play sound "music/door.mp3"
    scene room 1 with vslow_dissolve
    "You walk back up to your room, chest pounding and palms sweaty."
    "Before you take a seat at the edge of your bed,{p}you put away your sword under your bed."
    "Then you hear a knock."
    "Your back stiffens up."
    play sound "music/door.mp3"
    show witer stand at center with dissolve
    "A scaly green hand pushes through and in comes Witer."
    "He smiles at you as he walks closer."
    "Standing right in front of you, you get a full view of his body."
    "His protruding brown pecs obscure your view of his face."
    w "How’d you know about my side business?"
    e 4 "A little birdie told me."
    w "Smart birdie. So…"
    "He leans in close and blows into your right ear."
    w "How can I serve you?"
    e 6 "Just…Do what you want."
    hide witer stand with dissolve
    "The alligator kisses you on the cheek and slides down along your chest."
    "His hand brushes against your nipples."
    "You gasp, and your pecs tremble at the touch."
    w "Are you sensitive there?"
    menu:
        "Yes" if True:
            $ Witer.nipplesen = 1
            e 7 "Very."
            "Witer smiles and he pinches both of your nipples tightly, squeezing and rolling the tips."
            e 4 "Oh..!"
            scene witer blowjob1 with dissolve
            "Your dick springs upward from your loincloth and bumps Witer in the face."
            e 7 "Sorry, it just feels so good."
            w "Don’t be, just enjoy it. I like a man with a sensitive spot."
            w "Makes it easier to turn him on."
            "He lets one hand rest against your pec and he squeezes it hard."
            "Your nipple is trapped between his middle and ring finger."
            "Witer licks his lips hungrily, enjoying how you squirm in his hands."
        "No" if True:
            $ Witer.nipplesen = 0
            e 6 "Not really. It tickles mostly."
            "Witer nuzzles his face against your bulge, sniffing the scent of your musk."
            w "Then let's try something else."
            w "I love your smell, it’s so thick and strong."
            e 2 "Sorry, I haven’t had a chance to clean myself up completely."
            w "It’s ok, I like it."
            scene witer blowjob1 with dissolve
            "He loosens your loincloth exposing your semi-hard dick."
            "Its pink head snakes forward and hardens until the shaft grazes the alligator’s face."

    "Your dick pulsates from the stimulation and smears Witer with a shot of warm pre."
    w "Can’t have that go to waste."
    "He licks the leaking pre from the tip of your dick"
    scene witer blowjob2 with dissolve
    play music"music/blowjob.ogg"
    "His tongue presses against your slit."
    "Your body trembles feverishly as his tongue forces its way into your hole."
    "Witer pulls his mouth away from your cockhead , licks along the shaft hungrily."
    "Your breathing grows short and heavy."
    "The face he is making is just too much."
    "The way his ember eyes shines in the candlelight hungry for your manhood brings out the hunter in you."
    "His face buries into your ballsack, you feel his hot breath on your dick. "
    "Slowly, you feel his longue and soft tongue wrap around your member and finally he has you completely in his mouth."
    "Your dick literally pulsates with each suck, the rhythm of his motions send waves of pleasure through your body."
    e 7 "Um...oh!"
    "You instinctively hold onto the alligator's hard shoulder blades for support."
    "Every fiber of muscle in your body tightens and beads of sweat drip along your forehead."
    "Witer struggles to drink the copious amounts of pre gushing from your cock."
    e 4 "I’m gonna...!"
    with flashbulb
    "Your orgasm reaches its peak and you unload you fill his mouth with ropes of thick, hot cum."
    with flashbulb
    with flashbulb
    scene witer blowjob3 with vslow_dissolve
    stop music
    "Witer pushes you back and swallows the mouthful of cum."
    w "Fuck, it's been long since I got to taste so much cum."
    "You breathe heavily in response."

    w "You know, I liked it so much even I got excited."
    scene room 1 with vslow_dissolve
    show witer stand_nude1 at center with dissolve
    "He stands up and the outline of his hard cock is visible through his loincloth."
    "You stare wide eyed at it and reach out for it, but Witer grabs your hand."
    w "Ah, ah. That’s going to cost extra, and a bouquet of flowers."
    w "Now, I got to go. Snow might be looking for me."
    hide witer stand_nude1
    show witer stand at center with dissolve
    e 5 "Wait, you’re leaving already?"
    w "Don’t worry big boy."
    w "I’m always downstairs to receive you."
    "Witer kisses you on the cheek and walks out of the room."
    hide witer stand
    play sound "music/door.mp3"
    "You wonder did all of that really just happen?"
    play music "music/tavern.ogg"
    $ sex = True
    $ Witer.bj = True
    $ Time.mins = Time.mins +40
    $ persistent.CG_witer_bj = True
    $ Zalt.sex = Zalt.sex +1
    $ Zalt.lust = 0
    jump Room1

label Witer_sw:
    scene basement 1 with dissolve
    show witer sleep at center with dissolve
    w "He doesn’t know…"
    w "We’ll get out of here soon…"
    "You decide to yell at Witer."
    e 1 "WITER!" with vpunch
    show witer stand at center with dissolve
    w "Ahh!" with vpunch
    "He flinches and quickly turns to face you."
    "The shock and bewilderment on his face is clearly seen."
    w "What? [name] what are you- What am I doing here?"
    e 13 "I was hoping you’d tell me."
    e 1 "You’ve been acting really weird Witer, and that worries me."
    e 1 "I heard something from down below on my way to the washroom so I came down to check."
    w "Oh, heh. Silly me, I must have been having such a wonderful dream I was sleepwalking. Hehehe…"
    "You sigh and cross your arms."
    w "I'm sorry to have made you worry about me."
    w "How about I take you back upstairs and treat you to some one on one time."
    "He tries to reach for your bulge but you grab him by the wrist."
    e 1 "Witer, what's really going on?"
    e 13 "You can't pretend there isn't something bothering you. I'm worried."
    w "…"
    w "… It's stupid. Don't worry about it."
    e 1 "Enough with telling me not to worry. Witer, please."
    hide witer stand with dissolve
    "Witer looks you in the eye with a soreful expression, almost teary."
    "The dark rings under his eyes look worse now."
    show witer stand at center with dissolve
    w "I think… there's a ghost that wants to kill me."
    e 5 "What?"
    w "It started a few nights ago."
    w "I was asleep as usual with Hakan when I heard a knocking from the basement window."
    w "I'm a light sleeper so I heard it too well."
    w "When I looked up, there was nothing there at first."
    w "So, I figured it was just my imagination."
    w "Then tap… then again and again… the tapping wouldn't stop."
    w "I kept turning in my bed just wishing it would stop."
    w "Then I … I saw it!" with vpunch
    w "A stone no bigger than the palm of my hand tapping itself against the glass."
    w "It was moving on its own!"
    w "I couldn't breathe. I tried to wake Hakan up but he just wouldn't budge."
    w "So, I spent the first night just shaking in my covers listening to it tap and I just prayed someone would make it go away."
    w "The next day I got Hakan to come with me to check the area around the window."
    w "He wasn't convinced but we gathered as many of the rocks there and tossed it into the river."
    w "But the damn tapping came back the next night. The rock was back!"
    w "Hakan didn't want to help me find it again, he said I was getting paranoid."
    w "I just… I don’t know what to do."
    w "Am I going crazy? Maybe I'm just losing it. "
    "Witer looks to the ground, shoulders drooping."
    "He looks like a completely different person than the alligator you first met."
    menu:
        "Hug him" if True:
            hide witer stand with dissolve
            "You release your hold on Witer's wrist and pull him in for a hug."
            e 1 "No, you're fine. I believe you and I'll help."
            w "Thank you."
            "It sounds like he is sniffling between your pecs."
            e 1 "For now, you can sleep in my room until I deal with this haunted rock thing."
            show witer stand at center with dissolve
            "Witer pushes himself away to look at you."
            w "I can't do that."
            e 1 "I insist. If anyone asks, just say I got you booked for a while."
            w "Hmm, I won't say it's not tempting."
            e 6 "Then just say yes you dummy."
            w "Ok, ok. But I'll take the floor."
            w "I prefer to lie on something hard anyways. "
            w "I promise you won't even know I'm there."
        "Don't hug him" if True:
            e 1 "..."
            e 1 "Why don’t you just sleep in my room for now?"
            w "I don’t know, I find it hard sleeping anywhere else but my room."
            e 1 "At least you’ll be far away from the thing."
            e 1 "If anyone asks, just say I got you for a few days."
            w "Ok, ok. But I'll take the floor."
            w "I prefer to lie on something hard anyways. "
            w "I promise you won't even know I'm there."
    e 1 "Alright. Get some rest. I'll go search the outside of the tavern."
    w "Be careful, you don't want your tombstone to say you lost to a rock."
    w "And one more thing, just keep this between us."
    w "I don't want to worry the rest too. "
    e 1 "Alright. Good night Witer."
    hide witer stand with dissolve
    $ Witer.sleep = 4
    jump T_basement

label Witer_barn:
    scene outdoor 1
    play music "music/char_witer.ogg"
    "Just as you come upon the barn door loud grunting noises are coming from the inside."
    "The doors are wide open, but as you come up to the entrance."
    "The grunting becomes clearer and you recognize it to be Witer’s."
    e 1 "Witer? I'm coming in."
    "You stand by the barn door transfixed by the sight in front of you."
    scene witer squat with dissolve
    "The alligator's side faces you."
    "You see him shouldering a large bundle of hay."
    "He grunts again as he stands up with the hay on his shoulders, then he squats back down. "
    e 5 "He’s working out!"
    "Witer’s green scales sparkle like emerald as the sunlight bounces off the sweat dripping down his body. "
    "His muscles seem larger and more defined than normal."
    "Your eyes trail down his muscular back all the way to his firm buttocks."
    "You move closer towards him but he doesn’t seem to notice you."
    e 1 "Witer!"
    w "Huh?"
    scene barn 1 with dissolve
    show witer stand at center with dissolve
    w "[name], thanks for coming."
    hide witer stand with dissolve
    "He drops the stack of hay onto the ground."
    "And it lands with a loud thud and sends vibrations through the wood floor."
    e 1 "How heavy is that?"
    show witer stand at center with dissolve
    w "Not sure, I load it up with random pieces of metal when I can."
    w "But that’s not important, I need your help."
    e 1 "What’s wrong? Sounds pretty serious if you can’t tell me in the tavern."
    w "Well, I stayed up later than usual to help Snow take stock of the tavern’s inventory."
    w "I didn’t notice it, but Chet must have snuck down to my room while I wasn't looking."
    w "When I was finally done with my shift and got back into my room I noticed my top drawer was opened slightly."
    w "So, I checked, and my favourite shirt was missing."
    e 1 "Are you sure you didn’t misplace it or something?"
    w "I would never misplace something so important to me."
    w "That’s the first thing Walden made after weeks of training to be a tailor."
    "You sigh, and rub your forehead with your right knuckle."
    e 1 "That still doesn’t mean Chet took it."
    w "Then you explain this."
    hide witer stand with dissolve
    "Witer drops his hands into his loincloth."
    e 5 "Witer, woah!"
    "He pulls out a small white fabric."
    "It looks to be no bigger than your thumb."
    show witer stand at center with dissolve
    e 6 "Where did you keep that?"
    w "Not important, look. Doesn’t it look familiar?"
    e 1 "What am I looking at?"
    w "It’s a piece of the bandage that Chet wears on his arms and legs."
    w "I found it on the floor near my door."
    w "I think he must have stepped on one of them while trying to make his getaway and forgot about it."
    w "Look, I haven’t told anyone about this, and I think you’re the best person to help me."
    w "I can’t face Chet, he’ll just talk his way out, and I’ll believe him somehow."
    w "Hakan-I don’t want him involved, he’ll just beat Chet up without giving him a chance to explain himself."
    w "And Snow already has a lot on his plate, he wouldn’t be happy to be disturbed by this."
    e 1 "Alright, I can’t say no to a friend in trouble."
    e 1 "I’ll talk to him."
    e 1 "Just stay away from him for now, so we can avoid anything worse happening."
    w "Thanks, I just want him to give it back and explain himself."
    w "Anyways, I better get back to cleaning this place."
    w "Snow will not be happy that I spent the morning working out."
    e 1 "Alright, see you soon."
    hide witer stand with dissolve
    $ Witer.squat = 2
    stop music fadeout 1
    jump T_barn




label Witer_meal:
    scene tavern 1
    "You find a seat and sit down."
    "A few time later."

    show witer stand1 at center with dissolve
    if Witer.meet==False:
        "An exposed chest area crocodile comes"
        "He is muscular,and his scales shimmered in the impression of perspiration."
        "???" "Welcome to The Tavern of Spear!"
        w "I'm Witer! The waiter of the tavern."
        w "So, What do you wanna order today?"
        "he gives you a big smile. And waiting for your order."
        $ Witer.meet = True

        jump Witer_meal1
    elif True:
        w "Hello,What do you wanna order today?"
        "Witer gives you a big smile. And waiting for your order."
        jump Witer_meal1




label Witer_meal1:
    scene tavern 1
    show witer stand1 at center
    menu:
        "menu" if True:
            jump rent_room
        "Leave" if True:

            jump map1
        "Leave" if True:
            jump map1

label Witer_sex:
    scene witer blowjob with dissolve
    w "Emmmm."
    w "I like your cock"

label witer_cowboy:
    stop Flo
    stop Ebb
    stop music
    $ renpy.music.set_pause(True, channel='Witer')
    $ renpy.music.set_volume(1, 0.5, channel = "music")
    "...{w}..."
    play sound "music/door.mp3"
    scene room 1 with vslow_dissolve
    "Witer drags you by the hand back to your room. "
    "As soon as the door closes, the scaly green hands rip off your loincloths, tossing them unceremoniously onto the ground."
    "You look into those amber eyes burning with the hunger of a predator."
    "The large alligator begins to grope your crotch."
    "His large paw wraps behind your fuzzy orbs and tugs on them gently. "
    w "Give me!"
    "The alligator pushes against you and growls, you gasp at how good his hand feels. "
    e 9 "W-Whoa…ah!"
    if Witer.nipplesen == 1:
        "Witer’s other hand rubs across your chest and begins playing with your nipple."

    "You can already start to feel yourself get hard."
    show witer stand_nude at center with slow_dissolve
    w "Come on, big boy. Let’s get ready to ride."
    hide witer stand_nude with dissolve
    "The hand on your chest pushes you onto the bed and then Witer starts to climb on top of you."
    show witer cowboy1 with vslow_dissolve
    "The gator grabs a bottle of oil from a hidden compartment built into the bed and slathers a quick coating onto your erection. "
    "The scaly man now leans closer towards your muzzle."
    "His amber eyes continue to burn with a need he would soon sate. "
    show witer cowboy2 with vslow_dissolve
    "As the big gator now straddles himself over your hips."
    "A shiver of pleasure jolts through your hard cock as the tip drags between the smooth, scaly underside. "
    "His hands steady themselves upon your chest while his crotch starts to press against yours."
    "With his snout almost touching against yours, he growls with hot breath."
    w "What are you waiting for? Put it in."
    menu:
        "Push into his ass" if True:
            play sound "<from 6 to 7>music/Fucking_Wet_Climax_01.ogg"
            show witer cowboyb3 with slow_dissolve
            "You push your hips up, feeling your tip catch right against the alligator’s pucker."
            "The alligator starts to moan softly as his ring begins to spread around your member. "
            "The slick oil made an effective lubricant and without much force."
            play sound "<from 6 to 7>music/Fucking_Wet_Climax_01.ogg"
            "The fat head of your cock pops right into the Witer’s tight ass."
            "Soon all you can feel is the hot and tight muscles of the waiter’s ass engulf your whole length as Witer leans back to sit on your dick."
            w "A-ah...yes…that’s it."
            show witer cowboyb4 with slow_dissolve
            "The alligator begins to rock his hips on your crotch. "
            "His powerful hands press against your chest to balance himself as he starts to grind into your cock."
            "Witer lets out another moan as the alligator’s genital slit begins to open and the reptile’s pink tip emerges along your belly."
            "You can feel his hot length continue to throb as he starts to smash his ass up and down your dick. "
            show witer cowboyass_slow with slow_dissolve
            play music "music/Fucking_Wet_Slow.ogg"
            "Witer begins to bounce against your hard cock."
            "The entire length sliding all the way till only the blunt tip remains before taking all of it back inside with one motion."
            "The alligator’s tight hole felt so good clenching and squeezing against your throbbing wolf cock. "
            "The two of you pant as he continues to ride on your wolf meat."
            "You start to pump back into Witer’s scaly ass, your furry balls smacking gently against his green cheeks."
            "The alligator throws his head back as he continues to drive your cock as far as it will go up his backside."
            w "Yeah, that’s the spot. Fuck me harder!"
            show witer cowboyass_fast with slow_dissolve
            play music "music/Fucking_Wet_Med_01.ogg"
            "The alligator starts to buck against you with greater force."
            "His mouth hangs open as he pants heavily."
            "The bed creaks and thumps against the wall of your room as Witer continues to bottom out upon your rod."
            "The slaps of his ass cheeks grow louder as you feel yourself quickly getting close to eruption."
            "You can see the candle light glisten as Witer's own hard cock leaks upon your belly."
            e 0 "I...ah, I'm gonna…"
            "You feel the gator's hole tighten as Witer slams down, pushing your cock as deep as it would go inside him. "
            w "Oh fuck yeah...fill me!"
            stop music fadeout 0.5
            play sound "<from 5 to 13>music/Fucking_Wet_Climax_01.ogg"
            with flashbulb
            with flashbulb
            show witer cowboyb6 with slow_dissolve
            "That was all it took to send you over the edge."
            "Your cock throbs harder as your seed starts to erupt inside the alligator’s depths."
            "Your body clenches, your back arches as you empty your balls into the gator."
            "As you pant hard, you feel something wet drip across your lips."
            "Witer's own cock starts to erupt and more ropes spurt across your chest."
            "Out of breath, Witer collapses on top of you."
            hide witer cowboyb6 with vslow_dissolve
            "Pinned beneath the alligator, he licks off some of his seed that stains your chin."
            "You feel another lick across your lips before Witer's mouth wraps around yours and begin to share a deep kiss."
            "Your tongues lap against one another before he pulls away slowly. "
        "Push into his cloaca" if True:

            play sound "<from 6 to 7>music/Fucking_Wet_Climax_01.ogg"
            show witer cowboya3 with slow_dissolve
            "You feel your slick tip run across the alligator’s genital slit."
            "The powerful beast presses you into the bed and starts to grind his hips into your crotch."
            "Slick with oil, your cock head starts to spread open Witer’s tight slit."
            "He gasps as you start to penetrate his sensitive opening."
            play sound "<from 6 to 7>music/Fucking_Wet_Climax_01.ogg"
            w "A-Ah!"
            show witer cowboya4 with slow_dissolve
            "The alligator’s cry of shock fades into a long and rumbling moan as he slid all the way down."
            "Witer sinks your entire length inside him. "
            "The tight, muscular walls hugs your cock and you can start to feel something firm start to bump against your tip inside the reptile that straddles you."
            "Witer grinds his crotch right into yours, you can feel his cockhead bump against yours as the two frot and rub inside the alligator’s slit."
            show witer cowboy_slow with slow_dissolve
            play music "music/Fucking_Wet_Slow.ogg"
            "Nothing else matches the feeling of a reptile’s cock grinding against yours, especially while still inside the scaly’s body."
            "The lube mixes with the Witer’s natural secretions inside his slit and you feel your dick sink further inside the gator."
            "The tightness of Witer’s slit and his hard cock throbbing against yours feels incredible."
            w "That’s it, fuck me!"
            show witer cowboy_fast with slow_dissolve
            play music "music/Fucking_Wet_Med_01.ogg"
            "He starts to hump against you harder."
            "The slick walls, made tighter by the gator’s hard cock rubbing against your member, felt amazing. "
            "Witer grunts and moans as he continues to grind his dick against yours."
            "The normally coy and playful waiter you knew is now a demanding predator that would get exactly what he wants from you."
            "His green scaly claws drag along your chest as he throws his head back in pleasure."
            "More of Witer’s hot gator cock rubs along yours."
            "The pulsing passage that trapps your cock against Witer’s feels like a large hand stroking you both in tandem."
            "You can tell Witer was getting close as he starts to grind his slit harder onto your dick."
            "The alligator huffs and moans on top as you start to feel a pressure build inside his slit."
            w "I’m c-cumming!"
            with flashbulb
            "The alligator lets out a deep and rumbling groan and you can feel his cock start to throb right against yours."
            "You could feel the pulse of hot gator seed starting to spill out and fill the stuffed slit."
            "This was enough to send you over the edge and you begin to empty your balls as well. "
            e 0 "Ngh..me too!"
            stop music fadeout 0.5
            play sound "<from 5 to 13>music/Fucking_Wet_Climax_01.ogg"
            with flashbulb
            show witer cowboya6 at center with vslow_dissolve
            "You feel your balls emptying their contents into Witer’s slit, alongside the gator’s still spurting cock."
            "It didn’t take long before the excess seed leaked out from the overstuffed slit."
            "The two of you moan softly, laying in a growing pool of sexual fluids."
            "As the afterglow of your post orgasm high starts to fade, Witer lays down next to you."
            "You could hear a soft slick pop as your still semi hard cock exits the alligator’s hole."
            "As you look over at the alligator, you can now see his cock had fully exited and dripping in wolf and gator cream."
            "He points to his still hard dick. "
            hide witer cowboya6 at center with slow_dissolve
            w "Clean it."
            "You lean over and slowly take the cum covered cock into your muzzle."
            "As soons lips close around his tip, another spurt of gator seed pushes out and splatters across your tongue."
            "A scaly green hand lays on the back of your head petting and pushing you gently as Witer humps into your muzzle."
            "You lap and suckle Witer’s cock till the exhausted gator pulls you off his now spotless dick. "
    "As you lay there exhausted after the alligator’s ride, Witer grabs his clothing and smiles at you. "
    show witer stand at center with slow_dissolve
    w "That was a fun romp."
    w "Now if you'll excuse me."
    e 5 "Leaving so soon?"
    w "Duty calls handsome."
    w "If you want another round, let's meet in the bath house again."
    w "I'll be more than willing to accompany you."
    hide witer stand at center with slow_dissolve
    play sound "music/door.mp3"
    "The alligator closes the door behind him."
    "You never seen Witer look that ‘hungry’ before."
    "The calm and flirty waiter turned power bottom excites you. "
    $ Witer.cowboy = 1
    $ Zalt.sex = Zalt.sex +1
    $ persistent.CG_witer_cowboy = True
    $ Zalt.lust = 0
    stop music
    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
    jump Room1
image witer cowboy_slow:
    "images/witer cowboya5-slow1.png"
    pause 2
    "images/witer cowboya5-slow2.png"
    pause 0.1
    "images/witer cowboya5-slow3.png"
    pause 0.1
    "images/witer cowboya5-slow4.png"
    pause 2
    "images/witer cowboya5-slow3.png"
    pause 0.1
    "images/witer cowboya5-slow2.png"
    pause 0.1
    repeat

image witer cowboy_fast:
    "images/witer cowboya5.png"
    pause 0.3
    "images/witer cowboya5-1.png"
    pause 0.1
    "images/witer cowboya5-2.png"
    pause 0.1
    "images/witer cowboya5-3.png"
    pause 0.3
    "images/witer cowboya5-2.png"
    pause 0.1
    "images/witer cowboya5-1.png"
    pause 0.1
    repeat

image witer cowboyass_slow:
    "images/witer cowboyb4-slow1.png"
    pause 2
    "images/witer cowboyb4-slow2.png"
    pause 0.1
    "images/witer cowboyb4-slow3.png"
    pause 0.1
    "images/witer cowboyb4-slow4.png"
    pause 2
    "images/witer cowboyb4-slow3.png"
    pause 0.1
    "images/witer cowboyb4-slow2.png"
    pause 0.1
    repeat

image witer cowboyass_fast:
    "images/witer cowboyb5.png"
    pause 0.3
    "images/witer cowboyb5-1.png"
    pause 0.1
    "images/witer cowboyb5-2.png"
    pause 0.1
    "images/witer cowboyb5-3.png"
    pause 0.3
    "images/witer cowboyb5-2.png"
    pause 0.1
    "images/witer cowboyb5-1.png"
    pause 0.1
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
