label Chet:
    $ renpy.music.set_volume(0, 0.5, channel = "music")
    pause 0.5
    $ renpy.music.set_pause(True, channel='music')

    $ renpy.music.set_pause(False, channel='Chet')
    $ renpy.music.set_volume(1, 4, channel = "Chet")
    $ Time.mins = Time.mins +5
    if Items.pbag==0 and Time.days > 5:
        jump Chet_pbag1
    if Items.mossb == 0 and Time.days > 9 and jane_inv_E.qty(Moss_bracelet) == None:
        $ Items.accessories_quest = 1
        scene chet with dissolve
        c "[name], I’ve got a new sale plan you can’t miss out on."
        c "You know how you’ve been helping me collect some materials along the way?"
        c "Some slime jewels, bull fur, stuff like that."
        c "Well I decided to expand my services and make items for sale based on the materials I ask you to gather for me."
        c "I mean, I’ve been watching you for some time and as much as I enjoy seeing you barely dressed, you could always add more sex appeal with accessories. "
        c "But if you’re not interested in the accessories, then it’s fine. I’ll still offer my information services too."
        c "Just think of this as an additional incentive... plus it’s cheaper than me giving you gold every time."
        c "So for now, I’m offering a one of a kind moss bracelet."
        c "Bring me 3 moss, and I’ll let you have it for sale."
        c "Do you want the job?"
        menu:
            "Yes" if True:
                c "Excellent, moss can be found on the bodies of gargoyle enemies."
                c "They usually avoid sunlight so you might want to check dark places like caves."
                c "But watch out, even I don’t dare to get too close to them."
                c "I’ll see you when you come back with the 3 moss."
                $ Items.mossb = 2
            "No" if True:
                c "Some other time then, but think about it. It’s a good offer."
                $ Items.mossb = 1


    if Roushk.chet_e == 1:
        $ Roushk.chet_e = 2
        scene chet with dissolve
        c "I can’t believe he can leave." with vpunch
        c "Now I’ll never collect back all the money I lost to him!" with vpunch
        e 6 "There there Chet. You gotta let it go."
        c "Ugh, so what do you want?"
    if Roushk.chet == 1 and Roushk.barn ==1:
        hide witer stand
        hide hakan stand
        show roushk stand at right with dissolve
        hide roushk stand at right with dissolve
        "You find that Roushk is talking with Chet."
        scene chet with dissolve
        c "Hello, you sir look like a dapper lizard."
        c "Might I interest you in one of our high grade HP potions?"
        c "You won’t get it anywhere in your world."
        ro "My, my a tradesman. Sadly I don’t carry your form of currency here."
        c "Well, what do you have on you?"
        ro "Hmm..."
        "Roushk looks through his satchel and pulls out a small black rock."
        ro "This is diabosite, it is one of the rarest and strongest metal ore in my world."
        ro "It is perfect for armour and weapons. "
        c "Let me take a good look at that."
        "Chet examines the piece of diabosite closely, even licking it at one point."
        c "There’s enough here to make a small knife I think."
        c "Hmm... I can give you 20 coins for it."
        "Roushk turns to you with an unsure look on his face."
        ro "What do you think? Is that a lot in your world?"
        "You shake your head and turn to Chet."
        e 8 "Chet give him a fair deal."
        c "I am giving him a fair deal, I don’t see anyone else offering him gold for his ore."
        e 1 "Then I will buy it for 100 gold coins."
        ro "What?"
        c "Yeah, what the heck, [name]?"
        e 1 "Well you said no one is making an offer, well I am."
        e 1 "I’m sure an ore that exists from another world would fetch a high price."
        "Chet looks at you with his mouth open, surprised by your sudden involvement."
        c "150 coins!"
        e 1 "200 coins!"
        c "250 coins!"
        e 1 "300 coins!"
        c "325 coins!"
        e 1 "500 coins!"
        c "What? You don’t have 500 coins." with vpunch
        e 1 "Oh I have it, and unless you can bid any higher that ore is mine."
        "Chet scratches his head furiously, almost pulling the fur off his scalp, the sheer thought of losing out on a profit appears to have him on edge."
        c "600 coins and a HP potion!"
        e 3 "Woo, too rich for my blood."
        ro "Then it’s a deal."
        "Roushk trades his diabosite for Chet’s offer."
        "Chet looks at the small black ore in his hand, but looks defeated somehow."
        c "Oh, you’re going to pay for this one day, [name]."
        c "Now what do you want? This isn’t a museum, buy something!"

        $ Roushk.chet = 2
        hide roushk stand with dissolve
    if Chet.meet==False:
        scene tavern 1
        "You take a seat in front of the spandrel."
        scene chet with slow_dissolve
        window hide None
        "Hyena" " Welcome, welcome."
        "Hyena" "I’ve been wondering when you’d come over to talk to me."
        $ Chet.meet = True
        e 1 "Hey, nice to meet you."
        "Hyena" "Nice to meet you too, I don’t get that many customers around here."
        "Hyena" "Maybe my location isn’t that good."
        "He sounds cheery and excited to meet you."
        "His brown bushy tail taps loudly against the floor. "
        e "The name’s [name]."
        c "Chet, so what do you need buddy? You look like a rope kind of guy."
        c "Every good adventurer needs rope."
        "He pulls out a coarse rope from his bag and attempts to tie it into a knot."
        c "Good for catching your prey in the forest, and in bed."
        "Chet punctuates the word “bed” by strongly tugging at both ends of the rope,"
        "Letting you hear the fibers of rope tighten."
        e 7 "Um, yeah. I actually came to talk about something else."
        if Witer.meet == True:
            e 1 "Witer said you might have a job for me to do."
        elif True:
            e 1 "I’m looking for work, you know any ways I could make some coin?"
        c "I do, but I don’t think you’re up for it."
        e 1 "What? Why?"
        c "Well, these items I need are not only heavy, but they are very delicate."
        c "They have a tendency to pop if enough pressure is applied."
        "Chet rummages through his bag and pulls out what looks like a ball of slime."
        "He holds it close to your face."
        "A strong minty scent emanates from the ball."
        c "This here is a Slime Jewel."
        c "It’s like a kind of adhesive that’s handy for fixing anything here."
        c "I can personally recommend it as a substitute for lube too."
        e 5 "Wait, what?"
        "Chet doesn’t seem to hear you, and carries on talking."
        c "They are pretty sensitive during the first hour they are extracted from the slime monsters"
        c "So they risk popping and turning into nothing."
        c "If you’re up for the job bring 2 of them back to me."
        c "You can find slimes that carry these things in the forest to the west of the tavern."
        c "They only come out during the day because they rely on heat to maintain movement."
        e 1 "I can handle that."
        c "Then all the best to you."
        c "If you come back bruised and battered."
        c "I’d be happy to rub some healing cream all over you."
        "Chet winks at you before turning his attention back to rearranging his items on display."
        $ Chet.slime = 1
    if Witer.squat == 4 and Time.days > 14 and Chet.snowsfood == 0:
        $ Chet.snowsfood = 1
        scene chet with slow_dissolve
        c "If it isn’t the big man himself, I’ve been waiting for you to turn up."
        e 1 "Why’s that?"
        "Chet beckons you with a wave of his hand."
        "You lean closer to hear him."
        c "Soooo... you remember how last time, you helped with the Witer problem?"
        e 1 "Yeah, and...?"
        c "So, Snow is always on the lookout for people to try his next recipes."
        c "I figured maybe it would be nice to help him out with that at least once."
        e 6 "Basically you want me to join you to taste test Snow’s new recipes?"
        c "Eiyup. In exchange, I’ll let you have a peek at the book of Chet."
        e 1 "The book of Chet?"
        c "I’ll share my past with you. That was our deal."
        jump Chet_snowsfood
    elif True:

        scene chet with dissolve
        window hide None
    if Quest.fes_end == 2 and Quest.fes_chet == 0:
        $ Quest.fes_chet = 1
        scene chet with dissolve
        window hide None
        if Thane.movein != 2:
            c "Any idea when the whole bull vs lizards thing is going to end?"
            c "I’d like to restart stocking my materials from their place."
            e 1 "You will need to wait a little longer."
            e 13 "Things have turned for the worse."
            c "Damn it. Anyways, business must go on."
            c "What do you need?"
        elif True:
            c "Good grief, I lost a pretty good tarp covering all that blood Thane lost. "
            e 5 "Chet, a good friend of mine nearly died. You mind?"
            c "I’m joking, I’m joking."
            c "Everyone is just so sombre since then, makes the whole tavern feel like it’s stuck in a bubble of sadness."
            c "Disgusting."
            c "So what do you need?"

    call screen chet
    window show None

    if _return == 'Chet_mossb':
        label Chet_mossb:
            c "Do you want to buy a moss bracelet? It only costs 300 coins."
            menu:
                "Yes" if True:
                    if jane_inv.qty(coin) >=300:
                        $ jane_inv_E.take(Moss_bracelet)
                        $ jane_inv.drop(coin,300)
                        c "Pleasure doing business with you."
                        "You get the moss bracelet."
                        $ Items.mossb=4
                        jump Chet
                    elif True:
                        e 6 "(Nah,I don't have the money.)"
                        jump Chet
                "No" if True:
                    c "Aww, don’t you have enough coins to afford this little ol’ thing?"
                    jump Chet

    if _return == 'Chet_pbag1':
        label Chet_pbag1:
            if Items.pbag==0:
                scene chet with dissolve
                c "It looks like you’re having a hard time carrying more potions."
                e 13 "Well there’s only so much I can put in my satchel."
                c "Well I know another way you can carry more potions."
                "Chet winks at you with a sly smile."
                e 5 "No!"
                c "Woah, I wasn’t going there. I meant buy a potion bag."
                c "Here, I have one lying around for sale."
                c "It only costs 500 coins."
                e 5 "That’s expensive! Can’t you bring the price down a bit?"
                c "I mean you could pay me in another way."
                "Chet looks at you with half closed eyes and a lecherous smile."
                "He motions you closer by flicking his finger."
                "You approach the hyena and he whispers in your ear."
                "..."
                "..."
                "You practically jumped away from Chet and shake your head."
                "He pouts at you."
                c "Aww, but I promise I’ll use a lot of lube."
                c "You’d be surprised how much a person’s anus can stretch."
                e 9 "I’m good with 500 coins."
                c "You’re no fun."
                $ Items.pbag=1
                jump Chet
            elif True:
                c "Potion bag! Potion bag! Increase your potion carrying skills with a potion bag."
                c "Only 500 coins. You sir, will you be buying this beauty?"
            menu:
                "Yes" if True:
                    if jane_inv.qty(coin) >=500:
                        $ jane_inv_K.take(potion_bag_1)
                        $ jane_inv.drop(coin,500)
                        $ Items.pbag_n = Items.pbag_n +2
                        c "Pleasure doing business with you."
                        "You get the Potion Bag. Now you can carry more potions."
                        $ Items.pbag=2
                        jump Chet
                    elif True:
                        e 8 "(Nah,I don't have the money.)"
                        jump Chet
                "No" if True:
                    c "You will be back good sir."
                    c "There’s no better Potion Bag in this whole forest."
                    jump Chet

        jump Chet_talk
        return

    if _return == 'Chet_watch':
        label Chet_watch:
            if Items.watch==0:
                c "Now then, my big, tall and handsome customer. I’ve got something for you."
                e 1 "What is it?"
                c "Well you know how we’re all stuck here with all the time in the world right?"
                e 13 "Yeah, I’m not even sure if time is even moving around here."
                c "Eiyup, which makes work kind of hard cause you won’t really know how long you’ve done something."
                c "Which would be great if you were in bed, catch my drift?"
                e 10 "Maybe..."
                c "Anyways, I have this special watch I made for everyone in the tavern. "
                c "It may not accurately depict the time in the outside world, but we all agreed on what time it should be so we can keep track of things."
                c "I highly recommend you get it honey. I’ve sold this to a whole lot of people."
                c "Unless you want to be lost in time as well."
                c "It’s only 100 coins. I have it on display with the rest of my items."
                $ Items.watch=1
            elif True:
                c "It’s a pocket watch that tells time even while in the fog."
                c "It costs 100 coins. Do you want it?"
            menu:
                "Yes" if True:
                    if jane_inv.qty(coin) >=100:
                        $ jane_inv_E.take(pocket_watch)
                        $ jane_inv.drop(coin,100)
                        c "Pleasure doing business with you."
                        "You get the Pocket Watch. Now you can keep track of time."
                        $ Items.watch=2
                        jump Chet
                    elif True:
                        e 6 "(Nah,I don't have the money.)"
                        jump Chet
                "No" if True:
                    c "Aww, don’t you have enough coins to afford this little ol’ thing?"
                    jump Chet

        jump Chet_talk
        return
    if _return == 'Chet_talk':
        jump Chet_talk
        return
    if _return == 'Chet_dice':
        jump Chet_dice
        return
    if _return == 'Chet_bye':
        jump map1
        return
    if _return == 'Chet_shovel':
        label chet_shovel:
            e 1 "Chet where did you get that shovel from?"
            c "I found it while cleaning the barn."
            c "Interested? I’ll sell it to you for 300 coins."
            menu:
                "Buy" if True:

                    if jane_inv.qty(coin) >=300:
                        $ jane_inv_K.take(small_shovel)
                        $ jane_inv.drop(coin,300)
                        e 1 "Better to have it and not need it."
                        e 6 "Plus, I could use it to dig up some buried treasure."
                        c "You can bury me under your ass."
                        e 1 "What?"
                        c "I said here is your shovel."
                        "<You get a shovel.>"
                        $ Parif.chet_shovel = 2
                        jump Chet
                    elif True:
                        e 6 "(Nah,I don't have the money.)"
                        jump Chet
                "Leave" if True:

                    e 1 "I’ll think about it."
                    jump Chet

        return
    if _return == 'hp_potion_buy':
        c "Do you want this? It costs you 45 coins."
        if Zalt.cha >=8:
            "{b}{color=#19c22a}<Charm Check success>{/color}"
            c "But for a handsome guy like you, I can give you an extra discount."
            c "30 coins will be okay."
            "Chet winks at you."
            e 7 "Well..thanks?"
        elif True:
            pass
        menu:
            "Buy" if True:
                c "How many do you buy?"
                menu:
                    "1" if True:
                        $ buy = 1
                        if jane_inv.qty(hp_potion) >2+Items.pbag_n:
                            e 6 "Well,I can't take so many potions."
                            jump Chet
                        elif True:
                            pass
                    "3" if True:
                        $ buy = 3
                        if jane_inv.qty(hp_potion) >Items.pbag_n:
                            e 6 "Well,I can't take so many potions."
                            jump Chet
                        elif True:
                            pass
                    "Leave" if True:
                        jump Chet
                if jane_inv.qty(coin) >=40*buy and Zalt.cha <8:
                    $ jane_inv.drop(coin,40*buy)
                    $ jane_inv.take(hp_potion,buy)
                    "You get [buy] HP potion."
                    jump Chet
                elif jane_inv.qty(coin) >=30*buy and Zalt.cha >=8:
                    $ jane_inv.drop(coin,30*buy)
                    $ jane_inv.take(hp_potion,buy)
                    "You get [buy] HP potion."
                    jump Chet
                elif True:
                    e 6 "(Nah,I don't have the money.)"
                    jump Chet
            "Leave" if True:
                jump Chet
        return
    if _return == 'mp_potion_buy':
        c "Do you want this? It costs you 45 coins."
        if Zalt.cha >=8:
            "{b}{color=#19c22a}<Charm Check success>{/color}"
            c "But for a handsome guy like you, I can give you an extra discount."
            c "35 coins will be okay."
            "Chet winks at you."
            e 7 "Well..thanks?"
        elif True:
            pass
        menu:
            "Buy" if True:
                c "How many do you buy?"
                menu:
                    "1" if True:
                        $ buy = 1
                        if jane_inv.qty(mp_potion) >2+Items.pbag_n:
                            e 6 "Well,I can't take so many potions."
                            jump Chet
                        elif True:
                            pass
                    "3" if True:
                        $ buy = 3
                        if jane_inv.qty(mp_potion) >Items.pbag_n:
                            e 6 "Well,I can't take so many potions."
                            jump Chet
                        elif True:
                            pass
                    "Leave" if True:
                        jump Chet
                if jane_inv.qty(coin) >=45*buy and Zalt.cha <8:
                    $ jane_inv.drop(coin,45*buy)
                    $ jane_inv.take(mp_potion,buy)
                    "You get [buy] MP potion."
                    jump Chet
                elif jane_inv.qty(coin) >=35*buy and Zalt.cha >=8:
                    $ jane_inv.drop(coin,35*buy)
                    $ jane_inv.take(mp_potion,buy)
                    "You get [buy] MP potion."
                    jump Chet
                elif True:
                    e 6 "(Nah,I don't have the money.)"
                    jump Chet
            "Leave" if True:
                jump Chet
        jump Chet_dice
        return
    return

screen chet:

    imagemap:
        idle 'chet ground'
        hover 'chet hover'

        hotspot (674, 37, 547, 732) action Return("Chet_talk")

        hotspot (268, 874, 120, 65) action Return("Chet_bye")
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
    vbox:
        xalign 0.36 ypos 0.75
        imagebutton:
            idle "items/hp_potion_1.png"
            hover "items/hp_potion_2.png"

            action Return("hp_potion_buy")
    vbox:
        xalign 0.45 ypos 0.75
        imagebutton:
            idle "items/mp_potion_1.png"
            hover "items/mp_potion_2.png"

            action Return("mp_potion_buy")
    vbox:
        xalign 0.68 ypos 0.5
        if Items.watch ==2:
            pass
        else:
            imagebutton:
                idle "items/chet_watch.png"
                hover "items/chet_watch1.png"

                action Return("Chet_watch")

    vbox:
        xalign 0.55 ypos 0.75
        if Parif.chet_shovel !=1:
            pass
        else:
            imagebutton:
                idle "items/chet_shovel.png"
                hover "items/chet_shovel1.png"

                action Return("Chet_shovel")


    vbox:
        xalign 0.732 ypos 0.558
        if Items.mossb ==3:
            imagebutton:
                idle "items/chet_mossb.png"
                hover "items/chet_mossb1.png"

                action Return("Chet_mossb")
        else:
            pass
    vbox:

        xalign 0.2 ypos 0.64
        if Items.pbag==1:
            imagebutton:
                idle "items/chet_bag1.png"
                hover "items/chet_bag2.png"

                action Return("Chet_pbag1")
        else:
            pass
label Chet_talk:
    scene chet
    menu:
        "Find some topics to chat" if True:
            label Chet_chattree:
                menu:
                    "I want to buy something." if True:
                        e 1 "I want to buy something."
                        c "I've put everything I'm selling in front of me."
                        jump Chet

                    "About the fog" if Witer.squat < 4:
                        e 1 "So..how’s the fog?"
                        c "Thick, like me."
                        "He raises his right arm and flexes."
                        e 6 "Right... and how did you know that from down here?"
                        c "Well it’s no challenge if you know which hole to peek through and who to prod. In this case."
                        c "I overheard Snow talking to Witer about the fog before he left."
                        e 1 "Damn it, then I can’t leave yet."
                        c "Oh, cheer up, you can pass the time with one of my toys here. Like this stone."
                        "He pulls out a phallic shaped grey stone, rubbing it in a suggestive manner."
                        e 4 "Err... maybe later."
                        jump Chet_chattree
                    "Ask about Chet’s past" if Witer.squat >= 4:
                        if Chet.snowsfood != 3:
                            e 1 "How are things between you and Witer?"
                            c "Aww, aren’t you cute checking up on me."
                            c "Well we’re doing good, he smiles a lot more near me lately."
                            e 3 "That’s good to hear, maybe you guys got a little closer. "
                            c "Mmhmm."
                            e 1 "Look, it’s not my place to pry, but you said something about wanting to know what it meant to be loved."
                            e 1 "If you think you’re comfortable to talk about it, maybe you could-"
                            c "No."
                            c "It’s not comfortable to talk about it."
                            c "It’s painfully annoying to even think about it."
                            c "But, I’ll make an exception, since you helped me out, and I appreciate that you care."
                            c "On one condition."
                            e 1 "What is it?"
                            c "I want you to help me get closer with everyone else here."
                            c "We’ve been here for a while, and I don’t think they see more than just the sex guy who wants their money."
                            e 5 "What brought this on all of a sudden?"
                            c "Just... something felt different when I opened up to Witer, it felt good."
                            c "I just wonder if I can be closer to everyone else too."
                            e 1 "Sure, I’ll help you out."
                            c "Then we have a deal."
                            c "So, I’ll let you ask me one personal question for now."
                            c "Can’t reveal all my cards too soon, that’s not good business."
                            e 1 "Alright, where are you from?"
                            "Chet leans back against the wall behind him and looks upwards with misty eyes."
                            c "I was born and raised on the streets."
                            c "At least, that’s when my life actually began."
                            c "Home... I never had a home."
                            c "Just a house with an angry drunk who claimed to be my father."
                            c "And a woman who regretted ever giving up her rich inheritance to be with him and become mother to his son."
                            c "There was never a second without fighting."
                            c "How they hated each other, how they made unkept promises and ruined each other’s life."
                            c "Then there were the beatings... if he wasn’t hitting my mother."
                            c "He’d be hitting me, he had his way to make sure not to leave a mark on us."
                            c "Wouldn’t want to embarrass him in front of his more well-to-do friends."
                            c "So the moment I was 10, I took what little money I could stuff into my pockets and snuck into a carriage heading out of town when no one was looking."
                            c "It was the first time I stole something, and it wouldn’t be my last."
                            e 13 "What did you do after that to survive?"
                            c "Ah, ah. We agreed one personal question only."
                            c "You’ll have to help me out next time, and maybe we’ll talk more about the past."
                            e 1 "Really?"
                            "You sigh."
                            e 1 "Fine, a deal's a deal. Thank you anyways for being willing to share."
                            c "Don’t mention it. As in really, keep it between us."
                            c "I don’t need the world to know my backstory."
                            e 1 "Alright."
                        elif True:
                            e 1 "Alright, where are you from?"
                            "Chet leans back against the wall behind him and looks upwards with misty eyes."
                            c "I was born and raised on the streets."
                            c "At least, that’s when my life actually began."
                            c "Home... I never had a home."
                            c "Just a house with an angry drunk who claimed to be my father."
                            c "And a woman who regretted ever giving up her rich inheritance to be with him and become mother to his son."
                            c "There was never a second without fighting."
                            c "How they hated each other, how they made unkept promises and ruined each other’s life."
                            c "Then there were the beatings... if he wasn’t hitting my mother."
                            c "He’d be hitting me, he had his way to make sure not to leave a mark on us."
                            c "Wouldn’t want to embarrass him in front of his more well-to-do friends."
                            c "So the moment I was 10, I took what little money I could stuff into my pockets and snuck into a carriage heading out of town when no one was looking."
                            c "It was the first time I stole something, and it wouldn’t be my last."

                            "Chet leans back against the wall."
                            c "Well you know that I ran away from home."
                            c "Thing is, I left without a plan."
                            c "After one long ride I decided to hop off the moment I entered a new town."
                            c "Didn’t know anyone, and I sure as heck didn’t have a coin to my name."
                            c "The first two days were the worst. I looked around,asking, pleading for help but everyone ignored me."
                            c "Then one night, I was cuddled up in a dirty alley ready to faint from exhaustion when a group of rough looking foxes approached me."
                            c "They gave me a piece of bread and a drink from their water pouch."
                            c "I was so thankful that I could never reject what they offered me next."
                            c "A chance to survive in the town if I joined their gang."
                            c "Turns out they were a group of thieves, and they always needed smaller recruits for the harder to reach places."
                            c "I ended up being their servant boy, serving their every whim to keep them satisfied. "
                            c "Bring food Chet! Bring the beer Chet! Take off your clothes Chet..."
                            "You can see him struggling to swallow."
                            "His hands open and close repeatedly like it’s the only thing that is keeping him in his seat."
                            c "If I did a good enough job, then I wouldn’t go hungry that night."
                            c "Eventually I learnt how to pickpocket from them, and most importantly what to do when the law gets their hands on me."
                            c "You can imagine how being there for so many years meant that I learnt to appreciate every morsel of food I can get."
                            "He clutches his fists tightly."
                            c "And most importantly, how those without money are basically walking ghosts to the world."
                            e 13 "... I can’t imagine what you went through."
                            c "Yeah, well that’s my story, for now. Keep it to yourself ok."
                            e 1 "Sure. Thanks for sharing."
                            c "Yeah well, I’m going to count my slime jewels while I burn off this meal."
                            c "I’ll call you again if there’s someone in the tavern we can help on."
                            c "If you still want to?"
                            e 1 "Depends, I’ll have to think about it when the time comes."
                            "Chet nods."
                        jump Chet_chattree
                    "About the people living at the lake" if Ebb.meet != 0 and Ebb.tavern != 2:
                        e 1 "Chet, what do you know about Ebb and Flo?"
                        c "I think the shark has the hots for the butler."
                        c "Yeah, I think it's a whole master-servant thing."
                        c "Where one guy-"
                        e 8 "No, not what I meant. I mean as people, what do you know?"
                        c "Well, Flo’s definitely rich or at least born into money to have a butler to lug his luggage around. "
                        c "But judging by how protective that butler was, I doubt he’d let the shark spend his money willy-nilly."
                        c "Ahh, the things I could buy if I had his money."
                        e 1 "Chet."
                        c "My personal chariot, a personal rider, a mansion-"
                        e 8 "Ok, I’ll just wait."
                        c "A gold spoon, a personal bath house..."
                        "You listen to Chet listing all the things he could ever want, by the time he finishes you can’t remember what you wanted to ask him."
                        jump Chet_chattree
                    "Back" if True:
                        jump Chet_talk
        "About the work." if Chet.slime < 2:
            if Chet.slime == 0:
                if Witer.meet == True:
                    e 1 "Witer said you might have a job for me to do."
                elif True:
                    e 1 "I’m looking for work, you know any ways I could make some coin?"
                c "I do, but I don’t think you’re up for it."
                e 1 "What? Why?"
                c "Well, these items I need are not only heavy, but they are very delicate."
                c "They have a tendency to pop if enough pressure is applied."
                "Chet rummages through his bag and pulls out what looks like a ball of slime."
                "He holds it close to your face."
                "A strong minty scent emanates from the ball."
                c "This here is a Slime Jewel."
                c "It’s like a kind of adhesive that’s handy for fixing anything here."
                c "I can personally recommend it as a substitute for lube too."
                e 5 "Wait, what?"
                "Chet doesn’t seem to hear you, and carries on talking."
                c "They are pretty sensitive during the first hour they are extracted from the slime monsters"
                c "So they risk popping and turning into nothing."
                c "If you’re up for the job bring 2 of them back to me."
                c "You can find slimes that carry these things in the forest to the west of the tavern."
                c "They only come out during the day because they rely on heat to maintain movement."
                e 1 "I can handle that."
                c "Then all the best to you."
                c "If you come back bruised and battered."
                c "I’d be happy to rub some healing cream all over you."
                "Chet winks at you before turning his attention back to rearranging his items on display."
                $ Chet.slime = 1
                jump Chet_talk
            elif Chet.slime == 1 and jane_inv_M.qty(slime_jewel) < 2:
                c "You already have a quest."
                c "Go to the forest and find 2 Slime Jewels for me."
                jump Chet_talk
            elif Chet.slime == 1 and jane_inv_M.qty(slime_jewel) >= 2:
                c "You made it back!"
                c "I knew those monsters didn’t stand a chance against you."
                $ jane_inv_M.drop(slime_jewel,2)
                $ jane_inv.take(coin,100)
                "<[name] gains 200 EXP>"
                $ Zalt.exp = min(Zalt.exp+200, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                "[name] receives 100 coins."
                c "I might have some other odd jobs in the future."
                c "If you ever need some coin just come by."
                c "I’ll even sweeten the deal, with each successful quest I can tell you some interesting things."
                e 1 "What kind?"
                c "People, monsters, this tavern, maybe even sex positions?"
                "Chet winks at you again."
                e 7 "If I didn’t know any better, I think you’re trying to seduce me."
                c "Am I?"
                menu:
                    "Ask him if he wants to have sex" if True:
                        e 4 "I have my own room, and a big enough bed for the two of us."
                        c "Aww, you’re sweet, but it takes more than just a wolf in a hot bod to get me going."
                        e 1 "... What will it take?"
                        c "Where’s the fun in that if I tell you."
                        c "You got to find out for yourself."
                        c "Anyways, since you helped me with this job."
                        c "Here’s something you should know."
                        c "That alligator is pretty discreet."
                        c "Try leaving him a tip of 210 coins, and he might open up to you more."
                        e 5 "...Okay?"
                        c "Now, is there anything else you need?"
                        $ Chet.slime = 2
                        $ Snow.hunt = False
                        jump Chet_talk
                    "Turn down the idea of sex with Chet" if True:
                        e 6 "I don’t have the time for that right now."
                        c "That’s right, time is money and you need more of it."
                        c "Anyways, since you helped me with this job."
                        c "Here’s something you should know."
                        c "That alligator is pretty discreet."
                        c "Try leaving him a tip of 210 coins, and he might open up to you more."
                        e 5 "...Okay?"
                        c "Now, is there anything else you need?"
                        $ Chet.slime = 2
                        $ Snow.hunt = False
                        jump Chet_talk
            elif True:
                c "I don't have things for you to do now, maybe later."
                jump Chet_talk
        "About the work." if Chet.slime == 2 and Thane.meet >= 1:
            e 1 "Hey Chet, got any work for me?"
            c "You’re just in luck, which one do you want to take on?"
            menu:
                "Collect Bull Fur" if Chet.bullfur < 2:
                    if Chet.bullfur == 0:
                        c "So you’ve met the bulls huh."
                        c "Lucky you, lucky for all of us."
                        e 1 "How did you know that?"
                        c "You reek of bull musk."
                        c "Their kind are always well known for their powerful scents."
                        c "Can’t wash it off no matter how hard they try, which they rarely do."
                        c "Anyways, I need you to get for me 5 bundles of bull fur."
                        c "Their fur is a key ingredient in the health potions I sell, and I am running low on it."
                        e 5 " Let me stop you there, are you sure that’s a good idea?"
                        e 5 "The tribe members don't necessarily like us, you really think me cutting off their fur is a good idea?"
                        c "Come on, there's always going to be someone who doesn't like you."
                        c "Look at me, no one can stand me."
                        c "I say why not just turn that hate to a lucrative opportunity."
                        e 1 "..."
                        c "Look, if it makes you feel any better, the bulls live by a system that{p}the winner can claim anything from the one who loses to them in battle."
                        c "They will be glad if all you take is their fur."
                        c "They usually hunt in the forest near their village during the day."
                        c "That’s your best chance to catch them off guard."
                        e 1 "Huh, then that’s not so bad."
                        c "Try not to get bashed into the ground getting them."
                        $ Chet.bullfur = 1
                        jump Chet_talk
                    elif Chet.bullfur == 1:
                        if jane_inv_M.qty(bull_fur) >= 5:
                            $ jane_inv_M.drop(bull_fur,5)
                            $ jane_inv.take(coin,200)
                            $ jane_inv.take(hp_potion,3)
                            c "You’re back with my fur."
                            c "Excellent, this will keep me in stock with health potions for a while."
                            c "Here’s your reward."
                            "<[name] gains 240 EXP>"
                            $ Zalt.exp = min(Zalt.exp+240, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                            "<[name] receives 200 coins.>"
                            c "And as a bonus, have 3 health potions."
                            "<[name] receives 3 health potions>"
                            c "If you come across anymore of these I’ll happily take them off your hands for a few coins."
                            $ Chet.bullfur = 2
                            jump Chet_talk
                        elif True:
                            c "Hmm? I’m still waiting on those items."
                            c "Keep finding them, then come back to me."
                            jump Chet_talk


                "Collect more Slime Jewels" if Chet.moreslime < 2:
                    if Chet.moreslime == 0:
                        c "We’re running low on Slime Jewels again. 5 more should do."
                        e 1 "Really? It feels like I just got them."
                        c "What can I say, we have things to glue and slick."
                        c "Now, chop chop get to it."
                        c "Any longer and Snow’s going to bust a nut over the bar."
                        e 5 "Wait, what?"
                        c "I meant a literal nut."
                        $ Chet.moreslime = 1
                        jump Chet_talk
                    elif Chet.moreslime == 1:
                        if jane_inv_M.qty(slime_jewel) >= 5:
                            $ jane_inv_M.drop(slime_jewel,5)
                            $ jane_inv.take(coin,150)
                            c "Thanks buddy, here’s your reward."
                            "<[name] gains 200 EXP.>"
                            $ Zalt.exp = min(Zalt.exp+200, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                            "<[name] receives 150 coins>"
                            c "Here’s some information for you."
                            c "Did you know if you go hunting, closing off the escape routes of your prey{p}makes it easier for you to catch them or finish them off?"
                            e 13 "Err... yeah I already know that."
                            c "Oh, woops."
                            c "Well, give me some time to get you something new."
                            c "Think of this one as a refresher for ya anyways. Right, buddy?"
                            e 8 "No, it’s actually pretty useless info for me, and if I let it slide you would be scamming me."
                            e 8 "Give me something else."
                            c "Ugh, fine. You can have this."
                            if jane_inv.qty(mp_potion) >1+Items.pbag_n:
                                c "Looks like you can’t carry anymore potions."
                                c "I’ll give you some coins instead then."
                                "<[name] receives 90 coins.>"
                                $ jane_inv.take(coin,90)
                            elif True:
                                $ jane_inv.take(mp_potion,2)
                                "<[name] receives 2 mana potions>"
                            c "If you come across anymore of these I’ll happily take them off your hands for a few coins."
                            $ Chet.moreslime = 2
                            jump Chet_talk
                        elif True:
                            c "Hmm? I’m still waiting on those items."
                            c "Keep finding them, then come back to me."
                            jump Chet_talk
                "Collect Ectoplasm" if Chet.ectoplasm < 2 and Witer.sleep >= 7:
                    if Chet.ectoplasm == 0:
                        $ Chet.ectoplasm = 1
                        c "Word in the tavern is that you fought some rather interesting enemies lately."
                        c "Of the otherworldly kind specifically."
                        e 1 "Witer told you about the ghost rock?"
                        c "Maybe, or maybe he said it pretty loud after he and Hakan made their beds squeak for an hour in their bedroom."
                        "Your face flushes red."
                        e 10 "I don't even want to know. "
                        e 1 "So what about the ghost?"
                        e 1 "I have a feeling more will be after me after what I did to the last one."
                        c "Well do they leave any valuable loot behind after you beat them?"
                        e 1 "Just this."
                        "You show Chet the ectoplasm you picked up."
                        c "Hmm, interesting. It glows, and it has a very slime like feel to it. Any ideas what it does?"
                        e 6 "Not a clue."
                        c "Hmm, alright bring me 5 Ectoplasms."
                        e 5 "Why? You can't even use it."
                        c "For now, I need plenty of it to test what this thing can do."
                        c "For all we know, it could be the next lube, or even the perfect molding material for a realistic dildo, or-"
                        e 5 "Ok,Ok. I'll get the ectoplasm for you."
                        c "Come back soon, my hands are itching to play with them."
                        jump Chet_talk
                    elif Chet.ectoplasm == 1:
                        if jane_inv_M.qty(ectoplasm) >= 5:
                            $ jane_inv_M.drop(ectoplasm,5)
                            $ jane_inv.take(coin,250)
                            c "Excellent, Here’s your reward."
                            "<[name] gains 400 EXP>"
                            $ Zalt.exp = min(Zalt.exp+400, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                            "<[name] receives 250 coins.>"
                            c "Here’s a little bonus."
                            c "During one of my earlier travelers,I found a very interesting hut nearby the lake."
                            e 1 "Any idea who set the traps?"
                            c "Not a clue, I haven’t seen a single shadow move about there."
                            c "And as long as they aren’t messing with us I am fine with just letting them be."
                            c "Besides, the way those traps were set, it made it seem more like it was to keep something inside that hut from getting out than for someone to get into it."
                            $ Chet.ectoplasm = 2
                            jump Chet_talk
                        elif True:
                            c "Bring back 5 Ectoplasms for me to study."
                            c "I'll be waiting for you cutie."
                            "Chet winks at you."
                            jump Chet_talk
                    elif True:
                        "Bug here,pls report.!"
                        jump Chet_talk
                "Leave" if True:
                    jump Chet_talk

        "Sell monster material" if Chet.slime >= 2:
            jump Chet_sellM
        "New item quests" if Items.accessories_quest != 0:
            jump Chet_accessories
        "About Snow’s request" if Hakan.quest == 2:
            e 1 " I’m here about the item Snow requested to beat the tree creature."
            c "And I am glad you came to pick it up."
            "Chet pulls out from his bag a jar full of glowing green slime inside."
            e 1 "....What’s that?"
            c "The thing Snow requested."
            c "This will help you in your fight against the tree creature."
            e 1 "Ok, do I just throw it at him?"
            "You reach out to grab the jar but Chet pulls his hand away from yours."
            c "Nope, this isn’t a weapon, it’s armour."
            c "You need to apply to it all over yourself or you won’t survive the creature’s vines."
            e 13 "How’s covering myself in goo supposed to help me?"
            c "Simple, the goo is super slippery."
            c "If the creature grabs you with its vines you’ll still be able to escape."
            e 1 "That sounds way too simple."
            c "Hey, you’ll need it. Nothing escapes that thing’s vines."
            c "So it’s a few hours of feeling slimy or your life!"
            e 13 "...."
            e 1 "Fine! Give it to me!"
            "Chet look at you with a toothy grin."
            e 5 "What?"
            "Something about the way he’s looking at you feels like he has you right where he wants you. "
            c "I would be happy to give it to you [name]."
            c "But I’ve got to be the one to apply it on you."
            c "All. Over. You."
            "You flinch with your arms thrown back."
            e 9 "Wh- wha- what? I can apply the stuff on my own!"
            c "Not according to the deal I made with Snow."
            c "I agreed to make this stuff."
            c "In exchange that I get to test it out on whoever’s going to fight the tree."
            c "That includes putting it on."
            "You turn to look at Snow, but he quickly averts his gaze the moment he sees your face."
            c "So, what will it be? Do I rub ya down or not?"
            menu:
                "Yes" if True:
                    e 9 "..."
                    e 13 "..."
                    e 8 "..."
                    e 12 "Fine, just come on! Let's get this over with."
                    "You turn towards the start of the stairs but Chet pulls you by the wrist."
                    c "I can’t go to your room."
                    e 5 "What, why?"
                    c "All my stuff is here."
                    c "I can’t leave it unguarded, no matter how much I trust everyone here."
                    c "That’s just bad business."
                    e 9 "You-are you for real?"
                    e 9 "You can’t just undress me and rub me down here in front of everyone."
                    c "Well it’s that or no armour."
                    e 12 "Argh!"
                    scene tavern 1 with dissolve
                    "You turn to the rest of the tavern’s patrons. Your cheeks flush red with embarrassment."
                    e 12 "None of you better look!"
                    "Closing your eyes you turn back to Chet."
                    e 13 "Just do it!"
                    c "Heh, with pleasure."
                    stop music fadeout 1
                    scene black with dissolve
                    play sound "music/goochet.ogg"
                    "[name]" "..."
                    "[name]" "It feels cold."
                    "[name]" "Mmm... ah! No, not there."
                    c "Shh, just let the master work his magic."
                    "[name]" "Where are you grabbing?!"
                    "[name]" "Noooooo, so slimy and wet... please slow down Chet."
                    c "Quit your squirming, you’re getting goo all over me!"
                    c "Now spread them legs!"
                    "[name]" "Ah! I’m sensitive there."
                    "[name]" "Hah...hah... hah... hah!"
                    c "Wow, I expected you to be big down there, but not this big."
                    "[name]" "Ngh, I think it’s dripping into my ass."
                    c "Good, can’t forget that part. Now spread them wide."
                    "[name]" "AIYEE!"
                    stop sound fadeout 1
                    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
                    scene tavern 1 with dissolve
                    w "Wow, [name]."
                    s "Ehem..."
                    h "Hahahahaha!"
                    c "Heh."
                    "The embarrassment you feel is palpable."
                    "Your face is stuck in a blank expression."
                    "You’re still fully clothed, but your fur now feels sleek and slippery."
                    "Under the tavern light, your coat glistens."
                    "You cough, that’s the best you can say after that humiliating display."
                    "Silently, you head out of the tavern."
                    "{b}{color=#19c22a}<You’ve gained the goo armour! {p}Now you take less damage against vine attacks.>{/color}"
                    $ Hakan.quest = 3
                    $ Chet.tree = 1
                    $ Map.crossroad = 1
                    jump T_outdoor
                "No!!" if True:
                    e 9 "No thanks, I’ll do this without the goo."
                    c "Alright, your funeral."
                    c "I’ll be here if you change your mind."
                    $ Hakan.quest = 3
                    $ Map.crossroad = 1
                    jump Chet_talk
        "About goo armour" if Hakan.quest >= 3 and Hakan.quest <= 4 and Chet.tree == 0:
            c "So,do you change your mind?"
            menu:
                "Yes" if True:
                    e 9 "..."
                    e 13 "..."
                    e 8 "..."
                    e 12 "Fine, just come on! Let's get this over with."
                    "You turn towards the start of the stairs but Chet pulls you by the wrist."
                    c "I can’t go to your room."
                    e 5 "What, why?"
                    c "All my stuff is here."
                    c "I can’t leave it unguarded, no matter how much I trust everyone here."
                    c "That’s just bad business."
                    e 9 "You-are you for real?"
                    e 9 "You can’t just undress me and rub me down here in front of everyone."
                    c "Well it’s that or no armour."
                    e 12 "Argh!"
                    scene tavern 1 with dissolve
                    "You turn to the rest of the tavern’s patrons. Your cheeks flush red with embarrassment."
                    e 12 "None of you better look!"
                    "Closing your eyes you turn back to Chet."
                    e 13 "Just do it!"
                    c "Heh, with pleasure."
                    scene black with dissolve
                    stop music fadeout 1
                    "[name]" "..."
                    "[name]" "It feels cold."
                    "[name]" "Mmm... ah! No, not there."
                    c "Shh, just let the master work his magic."
                    "[name]" "Where are you grabbing?!"
                    "[name]" "Noooooo, so slimy and wet... please slow down Chet."
                    c "Quit your squirming, you’re getting goo all over me!"
                    c "Now spread them legs!"
                    "[name]" "Ah! I’m sensitive there."
                    "[name]" "Hah...hah... hah... hah!"
                    c "Wow, I expected you to be big down there, but not this big."
                    "[name]" "Ngh, I think it’s dripping into my ass."
                    c "Good, can’t forget that part. Now spread them wide."
                    "[name]" "AIYEE!"
                    scene tavern 1 with dissolve
                    w "Wow, [name]."
                    s "Ehem..."
                    h "Hahahahaha!"
                    c "Heh."
                    "The embarrassment you feel is palpable."
                    "Your face is stuck in a blank expression."
                    "You’re still fully clothed, but your fur now feels sleek and slippery."
                    "Under the tavern light, your coat glistens."
                    "You cough, that’s the best you can say after that humiliating display."
                    "Silently, you head out of the tavern."
                    "{b}{color=#19c22a}<You’ve gained the goo armour! {p}Now you take less damage against vine attacks.>{/color}"
                    $ Chet.tree = 1
                    jump T_outdoor
                "SUPER NO!!" if True:
                    c "Alright, your funeral."
                    c "I’ll be here if you change your mind."
                    jump Chet_talk
        "Ask about Witer" if Witer.sleep == 2:
            e 1 "You know anything about why Witer is acting all nervous and sleepy?"
            c "Shh, shh. Look."
            "Chet points behind you."
            scene tavern 1 with dissolve
            show witer sleep1 at center with dissolve
            "You turn to see Witer standing at his usual spot asleep and drooling."
            e 6 "Wi-"
            scene chet with dissolve
            hide witer sleep1 with dissolve
            "Chet’s hands extend from behind and covers your mouth."
            c "Shh! This is perfect eye candy material."
            c "Don’t ruin it for me before I’m done sketching him."
            e 5 "What? Why don’t you do that when he’s awake."
            c "Cause he charges a fortune. Now shh!"
            c "Chet’s no help. Is there anyone else who might know about Witer?"
            jump Chet_talk
        "Talk about Witer’s missing shirt" if Witer.squat >= 2 and Witer.squat <= 3:
            if Witer.squat == 2:
                e 1 "So, Witer asked me to talk to you."
                c "He did? If he’s looking for a threesome, count me in,handsome."
                e 3 "Hahahaha, no. This is serious, he is missing his favourite shirt."
                e 1 "Know anything about that?"
                c "I... can’t say that I do."
                c "I’ve been here the whole time, selling my wares at the best prices."
                c "Speaking of best prices, I have a special buy one get one free on dildos."
                c "You wouldn’t believe who they are molded from."
                e 13 "Chet, you’re just trying to change the topic."
                e 1 "You do know what happened to his shirt, don’t you?"
                c "No! Why are you interrogating me?"
                "His eyes dart away from you, he keeps looking down at this merchandise and avoids your gaze."
                "You sigh."
                e 1 "Look."
                "You pull out the piece of white bandage Witer gave you and show it to Chet."
                "Chet is taken aback, he turns to his left foot, and clear enough there is a tear where his bandage ends."
                e 1 "Witer knows you were the one who took the shirt."
                e 1 "He just wants it back with an apology."
                c "I can’t..."
                "His voice is so soft it’s almost inaudible."
                e 1 "What?"
                c "I said I can’t!"
                e 5 "Why the hell not?"
                "Chet sighs and looks past your shoulder."
                scene tavern 1 with dissolve
                show witer stand1 at center with dissolve
                "You turn slightly to see he’s looking at Witer."
                hide witer stand1 at center with dissolve
                "The moment the alligator walks towards Hakan."
                "Chet turns to his bag and pulls out a brown leather pouch."
                scene chet with dissolve
                "He opens it and you see a brown shirt, but the sleeves are ripped apart."
                e 5 "Chet, the shirt is in pieces! What happened?"
                c "Shh, not so loud."
                e 1 "Well you definitely can’t give this back to him in this state."
                e 1 "You gotta fix this."
                c "I can still fix this. I just need some thread and I can sew it back up."
                e 1 "Alright, then go get it."
                c "I know ok, just lay off my case."
                e 5 "What? I’m trying to help you."
                c "I fucked up alright, just give me some space and I’ll figure it out myself."
                c "Telling me to fix it, isn’t helping."
                "He crosses his arms and angrily turns away from you."
                "His ears are drawn back, and his tail curls up around his leg."
                e 1 "..."
                "There’s a strange feeling of uneasiness forming between the two of you."
                e 1 "That was uncalled for, sorry, I didn’t mean to pressure you like that."
                e 1 "I just want to help, however I can."
                "Chet sighs and drops his arms."
                "He turns to you with half-opened eyes."
                c "Why? There’s nothing in it for you even if you help me."
                e 1 "I’m doing this to keep friends together."
                e 1 "If you didn’t care enough about Witer."
                e 1 "You wouldn’t be trying to take it all on yourself to fix your mistake."
                e 1 "Now let me help you."
                c "..."
                c "Fine, the thread I need is in the bull village."
                c "The shopkeeper should have some."
                c "Can you help me get it? It’ll be dangerous for me to go in there alone."
                e 1 "Alright, I will."
                e 1 "Just get ready to fix that shirt and to apologize to Witer."
                c "I will... and thanks [name]."
                $ Witer.squat = 3
                jump map1
            elif True:
                if jane_inv_K.qty(bullthread) == None:
                    c "Do you have the thread?"
                    e 1 "No, not yet."
                    c "Then quit wasting time and go buy one."
                    c "The bull tribe should have some."
                    jump Chet_talk
                elif True:
                    $ jane_inv_K.drop(bullthread)
                    c "Did you get it?"
                    e 1 "Here."
                    "You pull out the ball of thread."
                    scene tavern 1 with dissolve
                    "Chet snatches it away and quickly closes the curtain on his spandrel."
                    "Witer looks at you with a raised eyebrow, you shrug back at him."
                    scene chet with dissolve
                    "After a few minutes Chet pulls the curtain open and you see the shirt now back in one piece in his leather pouch."
                    "You smile at Chet for his good work."
                    c "Ok, so ummm, can you take it to him?"
                    c "I don’t think he would want anything to do with me."
                    c "Just say his next purchase of lube will be on the house."
                    "He has that salesman smile again, but it lacks the usual cheer he has when he makes his sales pitch."
                    e 13 "Chet, you gotta do it."
                    e 1 "Witer will be upset, but I think if you’re honest with him he’ll give you a chance."
                    c "You think so?"
                    "His left foot is tapping quickly."
                    e 1 "Yes, come on, I’ll be by your side."
                    scene tavern 1 with dissolve
                    "Chet gulps nervously, but pulls himself out of the spandrel."
                    c "..."
                    show chet sad at center with dissolve
                    "You wonder what Chet is thinking about as he gets closer to the muscle-bound alligator."
                    hide chet sad with moveoutleft
                    "You watch from the side as the hyena walks up slowly to Witer."
                    show witer stand at left with dissolve
                    show chet stand at right with dissolve
                    c "Witer."
                    w "Chet."
                    "Witer looks at Chet sternly while the hyena has a nervous smile on his face."
                    c "Umm, here."
                    "He hands over the pouch to Witer who opens it to investigate the content of the bag."
                    "From the bag Witer pulls out the brown shirt."
                    w "My shirt."
                    c "Yeah, I took it."
                    c "Sorry, I just wanted to see this treasure you said your brother gave you."
                    show chet sad at right with dissolve
                    c "And I figured one little peek wouldn’t hurt right... {p}No, that’s not why I took it."
                    "Chet looks at his shuffling feet."
                    c "I took it because... I felt jealous you had something so special from someone you love and who loves you back."
                    c "I just wanted to see what something that valuable looked like."
                    c "Maybe I was hoping I’d get to feel what being loved would be like if I held it in my hands."
                    c "Sorry, I’m not trying to make an excuse for what I did."
                    "Witer puts his hands on Chet’s shoulder."
                    "The hyena looks up at the taller alligator with tired eyes."
                    w "Chet, I’m upset you took my shirt, but I’m willing to accept your apology."
                    w "If there’s anything a person should never be short of it’s food and love. "
                    w "I don’t know what happened in your past, but I care for you too."
                    w "And really- love isn’t this shirt, I loved the effort Walden put into it."
                    w "It was never about the item itself, and sweetie, you have love too, every time I’m reminding you to eat your meals."
                    w "Every time Snow nags at you to clean your spot, every time Hakan asks you to drink with him."
                    w "That’s how we show love too."
                    show chet stand at right with dissolve
                    "Chet’s ears perk up and his tail starts to wag, his face blushes but he’s trying to keep a straight face."
                    hide witer stand with dissolve
                    hide chet stand with dissolve
                    "Witer pulls Chet in for a hug."
                    "The hyena’s face only reaching the alligator’s stomach."
                    "They hug each other for a good minute before pulling apart."
                    show witer stand at left with dissolve
                    show chet stand at right with dissolve
                    w "But a crime still needs to be punished. How much did it cost to fix this shirt?"
                    c "Wait, you know I fixed it?"
                    w "Well of course, the sleeves actually stuck on when I pulled it out."
                    w "Even when Walden made it for me the sleeves fell apart, but I decided to keep it as it is to remind him how far he's come in his job."
                    c "Then that means... I fixed it for nothing?"
                    w "Oh, you deserve it, Mister. And you-"
                    "Witer turns his attention to you."
                    "With his hands on his hips the waiter radiates an imposing aura."
                    e 1 "Umm, err, me?"
                    w "You thought it was broken, but didn't think to tell me?"
                    e 5 "Hey, I was just looking out for your feelings."
                    "Witer steps closer towards you."
                    w "You really think my heart is that fragile?"
                    "He smiles at you."
                    w "That's sweet."
                    "Witer kisses you on your cheeks and you blush a little."
                    w "But you need to spend more time with me to see how strong I am. "
                    e 10 "Maybe I do."
                    "Chet fakes a cough to get both of your attention."
                    w "Oh right, so how much was it?"
                    e 1 "350 coins for the thread."
                    w "Alright, then Chet, pay [name] back 500 coins."
                    c "500? For a mending job I didn't even need to do?" with vpunch
                    c "That'll put me out of business!"
                    w "No it won't."
                    w "At most, you'll be having plain jerky for your meals for a few days."
                    show chet sad at right with dissolve
                    c "Ughh!"
                    "You and Witer laugh out loud. It seems this conflict has found its resolution."
                    "<You receive 500 coins from a reluctant Chet and gained 500 EXP>."
                    hide chet sad with q_dissolve
                    hide witer stand with q_dissolve
                    $ Zalt.exp = min(Zalt.exp+500, Zalt.maxlv*250+100*(Zalt.maxlv-1))
                    $ jane_inv.take(coin,500)
                    $ Witer.squat = 4
                    jump map1
        "Ask about brewing a Fear Potion" if Quest.campc != 0 and Quest.campc <4 and Quest.campb !=6 and Quest.campl !=6:
            if Quest.campc == 1:
                e 13 "Chet."
                c "Hey good looking, why the long face?"
                e 1 "..."
                e 1 "I’m going to ask you something serious."
                e 1 "It has to do with stopping the lizard and bull tribe from going to war."
                c "Seriously? "
                "Chet strokes his chin while making a soft “hmm” sound."
                c "A war could help to generate sales for my products."
                e 9 "Chet, you can’t be serious?"
                c "Of course I’m not. My customers won’t be happy to know I moved."
                c "Alright then, what do you need from me?"
                e 1 "I need you to brew me a Fear Potion so I can stop both sides from advancing their plans."
                c "A Fear Potion eh, can’t say I haven’t had experience brewing one, but making it won’t be easy without access to the usual ingredients."
                e 1 "Is there some way to substitute it?"
                if Chet.ectoplasm == 2:
                    c "You’re just in luck, remember the ectoplasm I had you find for me before? "
                    c "I tinkered with it and learnt that it has the same properties as the ingredients for a Fear Potion."
                    c "Thing is one glob of ectoplasm barely has enough of the juices I need to make a whole vial of Fear Potion."
                    c "You’ll need to gather 2 ectoplasm, and I’ll need 2 bundles of bull fur and 2 lizard scales to make it."
                    e 1 "Wow, thanks. I should be able to get all the items."
                    c "No problem, and whatever you do, do not eat that ectoplasm. You’ll see some freaky stuff."
                    e 1 "Why would I eat something from a ghost’s bo- Oh, you didn’t, did you?"
                    c "Hey, don’t you judge me. I did it for the sake of knowledge! Now, chop chop. The longer you take, the sooner we end up under the thumb of one of those two tribes."
                    if jane_inv_M.qty(ectoplasm) < 2 or jane_inv_M.qty(bull_fur) < 2 or jane_inv_M.qty(lizard_scale) < 2:
                        c "Rremember it’s 2 ectoplasm, 2 bundles of fur and 2 scales from the lizards."
                        c "Good luck, handsome."
                        $ Quest.campc = 2
                        jump Chet_talk
                    elif True:
                        $ jane_inv_M.drop(ectoplasm,2)
                        $ jane_inv_M.drop(bull_fur,2)
                        $ jane_inv_M.drop(lizard_scale,2)
                        $ jane_inv_K.take(Fear_potion)
                        e 1 "Here, I already have the things on hand."
                        c "Excellent, let me just brew it up for you."
                        c "Let me check the things first."
                        $ Quest.campc = 4
                        jump Chet_fear_potion
                elif True:
                    c "Not likely, the original list of ingredients was Horror root, essence of red carrot, iron ore, and the essence of the target’s species."
                    e 1 "I have no clue what you just listed."
                    c "You don’t have to, because I have it right here."
                    "He pats his hefty backpack with a prideful grin."
                    e 3 "That’s great then!"
                    c "Oh, no, no my friend. This is my last stock most probably, so it’s not going to be cheap to craft this."
                    e 5 "Chet, this is about preventing a war, and saving innocent lives."
                    c "Well, what makes you think your plan will work? If you fail, and the war really happens, the tavern might be at risk."
                    c "For all we know we’ll have to bargain our way for our safety."
                    c "So, I’m just taking precautions."
                    e 1 "Fine, how much?"
                    c "400 coins for the basic ingredients, and you’ll have to get me something from the bodies of those you want to scare off."
                    e 1 "So like, if I want to scare the lizards and the bulls then-"
                    c "Then bring me 2 bundles of fur from the bulls, and 2 scales from the lizards."
                    c "This is the only way to make sure the potion doesn’t go wild and affect you when you use it."
                    if jane_inv_M.qty(bull_fur) < 2 or jane_inv_M.qty(lizard_scale) < 2 or jane_inv.qty(coin) <400:
                        e 1 "Alright, I’ll go get the materials ready."
                        c "Alright, remember it’s 400 coins, two bundle of fur and two scales from the lizards."
                        c "Good luck, handsome."
                        $ Quest.campc = 3
                        jump Chet_talk
                    elif True:
                        $ jane_inv_M.drop(bull_fur,2)
                        $ jane_inv_M.drop(lizard_scale,2)
                        $ jane_inv_K.take(Fear_potion)
                        $ jane_inv.drop(coin,400)
                        e 1 "Here, I already have the things on hand."
                        c "Excellent, let me just brew it up for you."
                        c "Let me check the things first."
                        $ Quest.campc = 4
                        jump Chet_fear_potion
            if Quest.campc == 2:
                if jane_inv_M.qty(ectoplasm) < 2 or jane_inv_M.qty(bull_fur) < 2 or jane_inv_M.qty(lizard_scale) < 2:
                    c "Rremember it’s 2 ectoplasm, 2 bundles of fur and 2 scales from the lizards."
                    c "Good luck, handsome."
                    jump Chet_talk
                elif True:
                    $ jane_inv_M.drop(ectoplasm,2)
                    $ jane_inv_M.drop(bull_fur,2)
                    $ jane_inv_M.drop(lizard_scale,2)
                    $ jane_inv_K.take(Fear_potion)
                    c "Ah, you’re back. I trust you have everything I need to make a Fear Potion?"
                    "You nod."
                    c "Good, then let me just brew it up for you."
                    c "Let me check the things first."
                    $ Quest.campc = 4
                    jump Chet_fear_potion
            if Quest.campc == 3:
                if jane_inv_M.qty(bull_fur) < 2 or jane_inv_M.qty(lizard_scale) < 2 or jane_inv.qty(coin) <400:
                    c "Rremember it’s 400 coins, 2 bundles of fur and 2 scales from the lizards."
                    c "Good luck, handsome."
                    jump Chet_talk
                elif True:
                    $ jane_inv_M.drop(bull_fur,2)
                    $ jane_inv_M.drop(lizard_scale,2)
                    $ jane_inv_K.take(Fear_potion)
                    $ jane_inv.drop(coin,400)
                    c "Ah, you’re back. I trust you have everything I need to make a Fear Potion?"
                    "You nod."
                    c "Good, then let me just brew it up for you."
                    c "Let me check the things first."
                    $ Quest.campc = 4
                    jump Chet_fear_potion

        "Snow taste test" if Chet.snowsfood == 2:
            c "You and I should help Snow out with taste testing his new recipes."
            c "What do you say?"
            jump Chet_snowsfood
        "Leave" if True:

            hide screen chet
            scene tavern 1
            window hide None
            jump map1

label Chet_fear_potion:
    scene tavern 1 with dissolve
    "Chet draws the curtain to cover his shop as he begins work on the potion."
    "You tap your feet, the restlessness builds in you as time passes."
    scene chet with dissolve
    c "And I’m done!"
    "Chet pulls away the curtains with a vial the size of a beer bottle in hand."
    "Green liquid sloshes inside the container."
    e 1 "So, how do I use this?"
    "You pick up the vial and observe it close to your face, you smell no odor coming from the vial."
    c "Just drop it from somewhere high enough that the vial will break."
    c "The potion will evaporate turn into a thick miasma that will instantly affect any of the lizards and bulls nearby."
    c "What they see or feel, however, is out of my control, just know it will be something scary."
    e 1 "Let’s hope this works."
    c "No worries, I’ve made these dozens of times."
    c "If it fails, I’ll ensure you get your money back."
    "He winks at you with his usual salesman like smile."
    scene tavern 1 with dissolve
    "You tuck the vial away and turn towards the door."
    "Then something pulls you back by the wrist. "
    "You turn to see Chet looking at the floor while he holds your wrist."
    c "... "
    c "Make sure you come back, I still have lots of jobs that need doing."
    "You smile, grateful for the hyena’s concern."
    e 6 "I will."
    "Chet lets go of you, and you leave the tavern."
    if Quest.campl == 3:
        "You now have the Fear Potion."
        "Time to return to Thane, you’re worried that his attempts to get information from his father may land him in deep trouble."
    if Quest.campb == 3:
        "You now have the Fear Potion."
        "Thane will want to see this, and hear about the lizard’s time of attack."
    $ Quest.campt = 2
    $ renpy.music.set_pause(True, channel='Chet')
    jump T_outdoor


label Chet_sellM:
    menu:
        "Slime Jewels- 15 coins" if jane_inv_M.qty(slime_jewel) > 0:
            $ qty = jane_inv_M.qty(slime_jewel)
            c "You have [qty] Slime Jewels."
            c "I will take them for 15 gold coins each. Deal?"
            menu:
                "Yes" if True:
                    c "Nice! Here is your money."
                    $ jane_inv.take(coin,qty*15)
                    $ Items.dash = qty*15
                    $ jane_inv_M.drop(slime_jewel,qty)
                    "You get [Items.dash] coins!"
                    jump Chet_talk
                "No" if True:
                    jump Chet_talk
        "Bull Furs - 40 coins" if jane_inv_M.qty(bull_fur) > 0:
            $ qty = jane_inv_M.qty(bull_fur)
            c "You have [qty] of Bull Furs."
            c "I will take them for 40 gold coins each. Deal?"
            menu:
                "Yes" if True:
                    c "Nice! Here is your money."
                    $ jane_inv.take(coin,qty*40)
                    $ Items.dash = qty*40
                    $ jane_inv_M.drop(bull_fur,qty)
                    "You get [Items.dash] coins!"
                    jump Chet_talk
                "No" if True:
                    jump Chet_talk
        "Iron ore - 30 coins" if jane_inv_M.qty(iron_ore) > 0:
            $ qty = jane_inv_M.qty(iron_ore)
            c "You have [qty] of Iron ore."
            c "I will take them for 30 gold coins each. Deal?"
            menu:
                "Yes" if True:
                    c "Nice! Here is your money."
                    $ jane_inv.take(coin,qty*30)
                    $ Items.dash = qty*30
                    $ jane_inv_M.drop(iron_ore,qty)
                    "You get [Items.dash] coins!"
                    jump Chet_talk
                "No" if True:
                    jump Chet_talk
        "Lizard scale - 60 coins" if jane_inv_M.qty(lizard_scale) > 0:
            $ qty = jane_inv_M.qty(lizard_scale)
            c "You have [qty] of Lizard scales."
            c "I will take them for 60 gold coins each. Deal?"
            menu:
                "Yes" if True:
                    c "Nice! Here is your money."
                    $ jane_inv.take(coin,qty*60)
                    $ Items.dash = qty*60
                    $ jane_inv_M.drop(lizard_scale,qty)
                    "You get [Items.dash] coins!"
                    jump Chet_talk
                "No" if True:
                    jump Chet_talk
        "Ectoplasm - 30 coins" if jane_inv_M.qty(ectoplasm) > 0:
            $ qty = jane_inv_M.qty(ectoplasm)
            c "You have [qty] of Ectoplasm."
            c "I will take them for 30 gold coins each. Deal?"
            menu:
                "Yes" if True:
                    c "Nice! Here is your money."
                    $ jane_inv.take(coin,qty*30)
                    $ Items.dash = qty*30
                    $ jane_inv_M.drop(ectoplasm,qty)
                    "You get [Items.dash] coins!"
                    jump Chet_talk
                "No" if True:
                    jump Chet_talk
        "Moss - 100 coins" if jane_inv_M.qty(moss) > 0:
            $ qty = jane_inv_M.qty(moss)
            c "You have [qty] of Moss rocks."
            c "I will take them for 100 gold coins each. Deal?"
            menu:
                "Yes" if True:
                    c "Nice! Here is your money."
                    $ jane_inv.take(coin,qty*100)
                    $ Items.dash = qty*100
                    $ jane_inv_M.drop(moss,qty)
                    "You get [Items.dash] coins!"
                    jump Chet_talk
                "No" if True:
                    jump Chet_talk

        "Blood crystals -80 coins" if jane_inv_M.qty(blood_crystals) > 0:
            $ qty = jane_inv_M.qty(blood_crystals)
            c "You have [qty] of Blood crystals."
            c "I will take them for 80 gold coins each. Deal?"
            menu:
                "Yes" if True:
                    c "Nice! Here is your money."
                    $ jane_inv.take(coin,qty*80)
                    $ Items.dash = qty*80
                    $ jane_inv_M.drop(blood_crystals,qty)
                    "You get [Items.dash] coins!"
                    jump Chet_talk
                "No" if True:
                    jump Chet_talk
        "Leave" if True:

            jump Chet_talk


label Chet_accessories:
    menu:

        "Moss bracelet" if Items.mossb == 1 or Items.mossb == 2:
            if Items.mossb == 1:
                c "So for now, I’m offering a one of a kind moss bracelet."
                c "Bring me 3 moss, and I’ll let you have it for sale."
                c "Do you want the job?"
                menu:
                    "Yes" if True:
                        c "Excellent, moss can be found on the bodies of gargoyle enemies."
                        c "They usually avoid sunlight so you might want to check dark places like caves."
                        c "But watch out, even I don’t dare to get too close to them."
                        c "I’ll see you when you come back with the 3 moss."
                        $ Items.mossb = 2
                        jump Chet_talk
                    "No" if True:
                        c "Some other time then, but think about it. It’s a good offer."
                        jump Chet_talk
            elif Items.mossb == 2:
                if jane_inv_M.qty(moss) < 3:
                    "You’ll need to hand in 3 moss before I can make the moss bracelet for you to buy."
                    jump Chet_talk
                elif True:
                    $ jane_inv_M.drop(moss,3)
                    $ Items.mossb = 3
                    c "Perfect, this shouldn’t take too long."
                    c "You can check my special box of accessories when I’m done and you can buy the item."
                    jump map1
        "Leave" if True:


            jump Chet_talk


label Chet_snowsfood:
    menu:
        "Let’s do it now" if True:
            e 1 "Alright, let’s do it."
            scene tavern 1 with slow_dissolve
            "Chet wags his tail and crawls out of his spandrel."
            "The both of you walk over to the bar."
            show snow stand at left with dissolve
            show chet happy at right with dissolve
            c "Hey Snow, I brought over a new vict- "
            c "I mean volunteer to test your new recipes with."
            e 9 "Excuse me?"
            show snow happy1 at left with dissolve
            s "Don’t scare him away Chet. My cooking is pretty decent."
            show snow stand at left with dissolve
            s "Thank you two for volunteering."
            s "I’d ask Hakan and Witer but they keep avoiding me whenever I bring up my new recipes. "
            c "Teehee."
            "Chet smiles happily while his tail wags."
            hide snow happy1 at left with dissolve
            s "Give me some time and I’ll bring the dishes out."
            hide chet happy at right with dissolve
            "You and Chet wait while Snow cooks. "
            "From behind the bar, you guys can hear the clank of pots and pans, and the smell of something sizzling from the kitchen."
            "When Snow reenters the bar he is carrying a plate in each hand."
            "He places the plates in front of you both and smiles gleefully."
            show snow happy1 at center with dissolve
            s "Gentlemen, I have here what I like to call the “Cheezy Bomb”."
            hide snow happy1 at center with dissolve
            show cheezy_bomb with dissolve:
                xpos 0.4 ypos 0.3
                zoom 0.8
            "The dish on your plate looks like a purple blob."
            "Purple vapors are rising from the top of the dish."
            "The left side of your face twitches as you look at the dish then back at Snow."
            hide cheezy_bomb with dissolve
            pause 1
            e 9 "Wha-what is this?"
            show snow laugh1 at center with dissolve
            s "I don’t want to ruin the surprise."
            s "Give it a taste first."
            hide snow laugh1 at center with dissolve
            "You move your head slowly at Chet but he is already spoons deep into the glob."
            "He eats with amazing speed."
            e 8 "Huh."
            "You grab a spoonful of the goop and take a bite."
            pause 3
            "The goop is chunky like an omelette, and is actually salty and savoury like cheese."
            show snow stand1 at center with dissolve
            e 1 "Is this a cheese omelette?"
            show snow happy1 at center with dissolve
            s "It’s like cheese. I found out that the slime jewel, once mixed with a certain combination of fruit, changes texture and tastes like other foods."
            e 5 "Wow, that’s amazing."
            e 6 "I mean this thing looks “unique” but it really tastes good."
            show snow stand at left with moveinright
            show chet happy at right with dissolve
            c "Seconds please!" with vpunch
            "Chet stands up from his seat and hands Snow his empty plate, licked clean to the last goop."
            e 1 "Chet, slow down. Here you can have half of mine if you want."
            show snow happy1 at left with dissolve
            s "I’d take that offer, I don’t have any more slime jewels to make a second batch."
            show snow happy1 at left with q_dissolve
            hide chet happy at right with dissolve
            c "Hmm..."
            e 1 "Chet?"
            "You look at the hyena thinking with the spoon in his mouth."
            "Chet takes the spoon out of his mouth and looks to Snow with bright eyes."
            show chet stand at right with dissolve
            c "Tell ya what, I usually have a lot of extra slime jewels lying around."
            c "Why don’t I trade you some every two weeks?"
            c "And in return I can have this special jewel meal, on the house?"
            s "A fresh supply of jewels to experiment with from my most loyal taste tester, how could I say no?"
            show chet happy at right with dissolve
            c "Sweet! We got a deal."
            hide snow stand at left with q_dissolve
            hide chet happy at right with dissolve
            "Chet takes your plate and continues to scarf down the remainder of the food."
            "You try to grab another bite but Chet swats your hand away."
            "In a few minutes, Chet is done with his meal."
            "He lets out a hiccup while rubbing his bloated belly."
            show snow stand at left with dissolve
            show chet happy at right with dissolve
            s "So, what’s the verdict boys?"
            e 6 "Well from the bite I had, I say it’s good, but the presentation needs work. "
            show chet stand at right with dissolve
            c "Ditto."
            "Snow scratches the back of his neck."
            s "What does it matter what it looks like?"
            s "It’s the taste that people care about."
            c "Not if it looks like it’ll jump off the plate and attack you at any moment."
            c "I mean I know how you cook, but you won’t get any new customers with this."
            s "These hands aren’t made for such delicate work."
            s "Mending a blade yes, but food presentation just isn’t for me."
            s "Now if Parif was here."
            show chet happy at right with dissolve
            c "Yeah, Parif would have turned this into a work of art."
            c "And he’d serve your head next to it for presenting this in the first place."
            "The two of them break into laughter."
            e 1 "Err, Parif?"
            show snow happy1 at left with dissolve
            s "Oh yeah, you don’t know him. "
            s "He’s the tavern’s chef. One of the first few residents that ended up here."
            s "He left long ago, but he keeps coming back here every few months."
            e 1 "Wait, what?"
            s "Yeah, he said without him, everyone who comes to this tavern will starve if they have to eat my cooking."
            s "I’d sock him for saying that but he does cook like a master."
            show chet stand at right with dissolve
            c "I think he just likes the attention he gets whenever he is around, because he will bring tons of new ingredients from the outside."
            e 1 "So he’s part of this crusade to help those who are stuck here?"
            s "Correct."
            e 6 "I’d like to meet him one day, or maybe I wouldn’t want that cause that would mean I’ve been here for too long."
            "Chet rubs his belly again and stands up from his seat."
            c "Well I’m stuffed."
            s "Thanks again both of you for helping out."
            s "Can I count on you guys again for another round of taste testing?"
            c "I’ll always be there. [name]?"
            e 5 "Yeah sure, I’d be happy to."
            s "And Chet, let me know what you want to have made next, I’ll make sure you’ll be the first to taste your own slime jewels."
            c "You got it, Chief."
            hide snow stand at left with q_dissolve
            hide chet stand at right with dissolve
            "Chet and you then head back to the spandrel and sit down to talk."
            scene chet with slow_dissolve
            c "Thanks for helping me out."
            e 1 "Didn’t look like you needed much help though."
            c "Well you came along willingly."
            c "Hakan and Witer chickened out from the sight of Snow’s test foods."
            c "They didn’t even try to taste the food."
            e 1 "Meanwhile you ate it all up with gusto, and even volunteered to help supply Snow with the ingredients he needs to keep making new stuff."
            e 6 "How sweet."
            c "I’m not sweet! It’s just good business."
            c "I get to eat for free and I get to unload leftover products."
            "He crosses his arms and turns his face from you, but you can see his cheeks turn a slight shade of pink."
            e 1 "So how’d you get such a big appetite anyway?"
            c "Funny you should ask, will that be your one question about me you wish to know?"
            e 1 "Sure."
            "Chet leans back against the wall."
            c "Well you know that I ran away from home."
            c "Thing is, I left without a plan."
            c "After one long ride I decided to hop off the moment I entered a new town."
            c "Didn’t know anyone, and I sure as heck didn’t have a coin to my name."
            c "The first two days were the worst. I looked around,asking, pleading for help but everyone ignored me."
            c "Then one night, I was cuddled up in a dirty alley ready to faint from exhaustion when a group of rough looking foxes approached me."
            c "They gave me a piece of bread and a drink from their water pouch."
            c "I was so thankful that I could never reject what they offered me next."
            c "A chance to survive in the town if I joined their gang."
            c "Turns out they were a group of thieves, and they always needed smaller recruits for the harder to reach places."
            c "I ended up being their servant boy, serving their every whim to keep them satisfied. "
            c "Bring food Chet! Bring the beer Chet! Take off your clothes Chet..."
            "You can see him struggling to swallow."
            "His hands open and close repeatedly like it’s the only thing that is keeping him in his seat."
            c "If I did a good enough job, then I wouldn’t go hungry that night."
            c "Eventually I learnt how to pickpocket from them, and most importantly what to do when the law gets their hands on me."
            c "You can imagine how being there for so many years meant that I learnt to appreciate every morsel of food I can get."
            "He clutches his fists tightly."
            c "And most importantly, how those without money are basically walking ghosts to the world."
            e 13 "... I can’t imagine what you went through."
            c "Yeah, well that’s my story, for now. Keep it to yourself ok."
            e 1 "Sure. Thanks for sharing."
            c "Yeah well, I’m going to count my slime jewels while I burn off this meal."
            c "I’ll call you again if there’s someone in the tavern we can help on."
            c "If you still want to?"
            e 1 "Depends, I’ll have to think about it when the time comes."
            "Chet nods."
            "<[name] gained one Level-up-point.>"
            $ Zalt.points = Zalt.points +1
            $ Chet.snowsfood = 3
            jump Chet
        "Maybe later" if True:
            $ Chet.snowsfood = 2
            e 6 "Perhaps at another time. I have something to deal with now."
            c "Alright, you know when and where to find me."
            c "I think Snow would appreciate having more than one person to comment on his stuff."
            jump Chet
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
