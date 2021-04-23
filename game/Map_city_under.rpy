label undercity_map0:
    stop music
    stop Thane
    stop Chan1
    stop Chan2
    $ renpy.music.set_volume(1, 1, channel = "Chan1")
    if Map.undercity_3 == 2:
        play Chan1[ "<silence 0.5>", "music/undercity.ogg" ]fadein 3
    elif True:
        stop Chan1 fadeout 4
    jump undercity_map


label undercity_map:
    $ Map.undercity_here = True
    stop music
    $ Time.mins = Time.mins +10
    $ Zalt.dungeon = False
    $ config.rollback_enabled = True
    $ renpy.music.set_volume(1, 5, channel = "Chan1")
    $ renpy.music.set_pause(False, channel='Chan1')
    window hide None


    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1

    if Zalt.lust <= 20:
        $ Zalt.lust = 20
    if Map.undercity_auc_start == 1:
        if Time.hours >= 6 and Time.hours <= 11:
            $ Map.undercity_worktime_time = "Morning"
        elif Time.hours >= 12 and Time.hours <= 17:
            $ Map.undercity_worktime_time = "Afternoon"
        elif Time.hours >= 18 and Time.hours <= 24:
            $ Map.undercity_worktime_time = "Night"
        elif True:
            $ Map.undercity_worktime_time = "Sleep"
        if Zalt.end >= 6 and Zalt.end <8:
            $ Map.undercity_worktime_maxsp = 6
        elif Zalt.end >= 8:
            $ Map.undercity_worktime_maxsp = 7
        elif True:
            $ Map.undercity_worktime_maxsp = 5
        if Map.undercity_auc_day+8-Time.days == 0:
            $ Map.undercity_auc_start = 2
            scene undercity 1 with dissolve
            jump undercity_auction_start
        elif Map.undercity_auc_day+8-Time.days <0:
            $ Map.undercity_auc_start = 2
            scene undercity 1 with dissolve
            jump undercity_auction_start_lag
        elif True:
            pass
        if Zalt.cor >= 100:
            scene black with vslow_dissolve
            "..."
            e 11 "So heavy... so h- horny."
            "Your shoulders feel unusually heavy."
            "Yet this is not the weight of exhaustion but the burden of the growing lust inside you."
            "The corruption... there is too much of it."
            "Your mind is gripped by a dark miasma planting lewd thoughts and desires into you."
            e 11 "Must... have...sex."
            "You collapse onto all fours, breathing heavily."
            "The demons begin to surround you."
            "They smell the corruption on you and you have no will fight it."
            "The demons take you."
            "{b}{color=#c22719}<GAME OVER>{/color}"
            menu:
                "New game" if True:
                    return
                "New game" if True:
                    return
        if Zalt.lust >= 100:
            scene black with slow_dissolve
            e 11 "Fuck!"
            "You can’t hold it in any longer, you are too horned up."
            "You run to a secluded area that no demon can see you."
            "You undo your loincloth and jerk off."
            "It costs you half the day to relieve your lust."
            "Influenced by the city, when you are in the city, your minimum lust won't be less than 20."
            $ Time.hours = Time.hours+6
            $ Zalt.lust = 20
            jump undercity_map
    scene undercity 1
    if Map.undercity_3 != 2:
        show city_fog_1


    call screen undercity_map with dissolve
    if _return == 'exit':
        jump castle_map0
        return

    if _return == 'point 2':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.undercity_2 == 1:
            "You take a step forward to touch the gate when suddenly two dark shadows sprout out from the earth, and take form."
            "The shadows solidify and take on the form of metal knights."
            "Where their eyes would be only dark eyes with yellow pupils look back at you."
            "They each hold flaming swords which they hold towards you to keep you away."
            "First Guard" "What do we have here? I think it’s a mortal adventurer."
            "Second Guard" "Now how did such a little thing get pass that monster guarding the entrance?"
            "You pull out your sword."
            e 12 "What are you? More ghosts?"
            "First Guard" "Ghosts? You'd be lucky if we were"
            "First Guard" "You best step away unless you are willing to pay with your life."
            "Second Guard" "Yeah, doesn't matter how you took care of the guy blocking this pathway earlier."
            "Second Guard" "But we aren't letting you through if you don't meet our terms."
            e 12 "That's what took Flo?"
            "First Guard" "Hahahah. Look at em he looks like he's going to piss his loincloth."
            "Second Guard" "That's right wolf, you best turn around or else!"
            "You look back at the path you came and back at the guards wielding flaming sword at you."
            e 12 "No! I don't care what you are. You took an innocent life and I want him back."
            "Second Guard" "Is he talking about that pound of flesh that was picked for the auction?"
            "First Guard" "I think so."
            e 5 "Wh-what auction?"
            "First Guard" "It's our tradition that we do every 10 years."
            "First Guard" "An auction where the biggest bidder gets the most delicious feast, a mortal's soul and body to do as they please."
            "They both laugh maniacally."
            e 1 "...Can I join the auction too?"
            "First Guard" "Woah, woah woah. If you really want to go in that badly we’d let you in if you have the ticket on you."
            e 1 "Ticket? You mean gold coins?"
            "First Guard" "We don’t have use for your useless mortal currencies. We barter with something better."
            "First Guard" "We need corrupted souls!"
            label guard_coccheck:
                "The second guard waves his hand and a dark aura envelops your body."
                "Second Guard" "Let's test how much Corruption you have now."
                with flashbulb
                pause 3
                if Zalt.cor < 15:
                    "Second Guard" "Yikes. Sorry bub, you’re not the type of our people."
                    "Second Guard" "Can’t let you through."
                    e 5 "What? How do I earn more then?"
                    "First Guard" "Oh, there’s so many ways."
                    "First Guard" "Why don’t you try selling your body to dark creatures?"
                    "First Guard" "I hear that once they get their hands on your body, it stains the soul really well."
                    e 9 "I need to fuck a slime or a ghost?"
                    "First Guard" "Hah, you wish you could."
                    "First Guard" "No, you got to let them inside you, let them CORRUPT your soul."
                    "The guards laugh again."
                    "You reluctantly sheet your sword and decide to head back."
                    "If what they’re saying is true, they won’t let you in without greater Corruption."
                    $ Map.undercity_2 = 2
                elif True:
                    "First Guard" "Would you look at that, we’ve got here a very rich, very Corrupted soul."
                    "Second Guard" "You’ll be perfect now. Enjoy the auction."
                    "The guards’ swords disappear and they step aside to open the gate for you."
                    "You can now enter the underground city."
                    "That is, until the second guard steps in front of you."
                    e 5 "Hey!"
                    "Second Guard" "I need to read you the rules first before you can go in bub."
                    "Second Guard" "Mortal or not, no one breaks the rules here."
                    e 1 "Fine."
                    "Second Guard" "Which one do you want to hear first?"
                    $ Map.undercity_2 = 3
                    $ Map.undercity_3 = 1
                    jump undercity_guard_talk
                jump undercity_map
            jump undercity_map
        elif Map.undercity_2 == 2:
            jump guard_coccheck
        elif True:
            jump undercity_guard_talk
            label undercity_guard_talk:
                menu:
                    "Security rules" if True:
                        "Second Guard" "We run a strict rule abiding city down here."
                        "Second Guard" "That means no hacking and slashing with your sword."
                        "Second Guard" "Even if you try, I think you know how it will end."
                        "Second Guard" "Only us guards get that privilege."
                        "Second Guard" "So, when you’re in the city you might feel like you’ve become more agreeable to the people and the rules of the city."
                        e 5 "To hell with that. I won’t be made to obey so easily."
                        "Second Guard" "Trust me, you won’t have a choice."
                        jump undercity_guard_talk
                    "Auction rules" if True:
                        e 1 "Tell me how to take part in the auction."
                        "Second Guard" "As we said, gold coins don’t have value here."
                        e 1 "So you use the Corruption?"
                        "Second Guard" "No, no. That was just a security thing."
                        "Second Guard" "We use these purple coins for business."
                        "The guard pulls a purple coin from thin air."
                        "The round coin looks no different from a common gold coin but what gives it its purple hue."
                        e 5 "How do I get these coins?"
                        "Second Guard" "You work like everybody else."
                        e 1 "Sounds easy enough."
                        "Second Guard" "Oh yeah? Well first you gotta get your worker’s permit from the boss himself."
                        e 5 "Boss? The guy in charge of all this chaos? The fog even?"
                        "Second Guard" "I dunno anything about the fog, but the Boss runs this city."
                        "Second Guard" "You want to work, talk to him first."
                        "Second Guard" "He’s also the guy in charge of the auction."
                        "Second Guard" "So registration and fee goes to him."
                        jump undercity_guard_talk
                    "Pawn shop rules" if True:
                        "Second Guard" "If you got the goods you can exchange them for some of the city’s currency at the pawn shop."
                        "Second Guard" "It’s the shop to your right when you reach the lower level."
                        "Second Guard" "Many leave their earthly possessions behind there, got to have the coins to survive after all."
                        e 1 "Alright. I’ll check that out."
                        jump undercity_guard_talk
                    "Уйти" if True:
                        e 1 "I don’t need to know anything more."
                        "Second Guard" "Then it’s your own funeral. Off you go."
                        "He steps aside allowing you to walk through."
                        jump undercity_map

            jump undercity_map
    if _return == 'point 3':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_3 == 1:
            "Through the gate, you spot some kind of a door that you’ve never seen before. "
            "It leads into what looks like a well lit box of some kind that can fit several people inside."
            "Around the box is a metal cage."
            "Looking back, you see the guards snicker at you."
            "There’s no point in turning back. You head closer to the box."
            "You walk around the box. You inch around the contraption."
            "It’s made from some cool metal. On its sides and back are gears that guide the movement of a steel cable."
            "Back to the front, you find a panel with two buttons, Up and Down."
            "At the front, you find a panel with two buttons, “Up” and “Down”."
            "First Guard" "Just go down already.\nHaven’t you seen a damn elevator before?"
            "The guards laugh patronizingly at you."
            "You curse them under your breath and enter the elevator box."
            "Inside, the same “Up” and “Down” buttons are presented to you."
            scene black with dissolve
            "You press the Down button."
            "The gears on the outside turn and you hear the unmistakable hiss of steam."
            "*clink clank clink clank*"
            pause 2
            "The elevator descends downwards."
            "You’ve heard of such technology but have never seen it before. "
            "Some cities around the world have adopted new steam technology, building their empires from metal and gears."
            "Your gut screams at you that this place isn’t one of them."
            "A red hue then fills the elevator. "
            scene undercity 1
            show city_fog_1
            pause 0.5
            hide city_fog_1 with vslow_dissolve
            play Chan1[ "<silence 0.5>", "music/undercity.ogg" ]fadein 3
            "You turn from the door and stare dumbfounded."
            "Overhead through the transparent walls of the elevator, lies a sprawling city of flames and metal that comes into view."
            "Tall, mighty buildings of unknown function form the labyrinth of a city."
            "The magma oozing from the pores of the earth gives the city the impression that the earth is bleeding."
            "*Ding*"
            "The elevator comes to a halt and the door opens."
            "A sense of dread fills your heart."
            e 13 "Nowhere left but forward."
            $ Map.undercity_3 = 2
            $ Map.undercity_4 = 1


            jump undercity_map
        elif True:
            "This place looks safe to set up a campfire and rest."
            "You can also level up here."

    if _return == 'point 4':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_4 == 1:
            "You step out of the elevator and a warm fuzzy feeling grips your brain."
            "It’s as though you’re drunk, but you’re still very much aware of your surroundings and actions."
            "It’s just... everything feels so nice now."
            "You don’t even notice how hot the whole area is with the flowing magma."
            "Your whole body feels like warm fingers clasping every side of you."
            "Your loins shudder, and you have a growing urge to touch yourself."
            e 11 "Right what was I? Flo... right, got to save Flo."
            "(Influenced by the city, when you are in the city, your minimum lust won't be less than 20.)"
            "Fighting through your sudden lustful desires, you explore the city."
            $ Map.undercity_4 = 2
            $ Map.undercity_5 = 1
            $ Map.undercity_6 = 1
            $ Map.undercity_10 = 1
            $ Map.undercity_12 = 1

            jump undercity_map
        elif True:
            "This place looks safe to set up a campfire and rest."
            "You can also level up here."
    if _return == 'point 5':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_5 == 1 and Map.hellhound_meet == 0:
            "On the ground floor, you follow a path that extends to the back of the elevator."
            "You walk straight and encounter what looks like a shop. "
            "It has a sign that reads “Pawn Shop”."
            "When you approach the door to the shop, you find out that it’s locked. "
            "Then, you hear a loud gasp coming from inside."
            e 1 "Hello? Is anybody inside?"
            "You press your ears to close against the door."
            "You hear a longer gasp this time, followed by intermittent moans and cries of pleasure."
            "Your cheeks turn red and you bite down on your lower lip."
            "Then there’s the clank of metal pieces falling and the creek of a table moving across the floor slightly. "
            e 10 "What are they doing in there?"
            e 10 "What am I doing?"
            "While you are listening to the people behind the door, one of your hands has been busily groping and jerking your growing erection."
            "You pull yourself away from the door, and decide to come back later."
            jump undercity_map
        elif Map.undercity_5 == 1 and Map.hellhound_meet == 1:
            "You enter the pawn shop."
            "Rows of shelves welcome you from the side of the shop, forming a sort of barricade leading you straight to the counter. "
            "Closer inspection reveals that these rows are lined with random objects that have not much value at all."
            "A broken necklace, a fork, a wanted poster and so forth."
            "You head to the counter and ring the bell."
            "*Ding*"
            "A swirl of dark smoke appears before you and takes on the form of a broad gentleman in a fine suit."
            "Like the other residents of this city, he has blood red fur and you cannot make out his face. "
            "Pawn" "Welcome, welcome. A new face, hello, I am Pawn."
            e 1 "Pawn? That’s your real name?"
            "Pawn" "Of course not, but you know, pawn shop, pawnbroker... I figured why not, right?"
            e 1 "Err... ok. So what can I buy or sell here?"
            "Pawn" "Now hang on, I didn’t even know how to call you yet. What’s the rush? We’re all here for all of eternity."
            e 1 "Not me, I rather not get too comfortable here. But if you must ask, my name is [name]."
            "Pawn" "Hmm, judging by your smell I take it you are not native."
            e 13 "No, I am not."
            "Pawn" "Ah, excellent. Then you must have all kinds of wares to sell. "
            "Pawn" "Demons usually aren’t that interested in the items of mortals."
            "Pawn" "I will offer you a loan in exchange for any item you have."
            "Pawn" "Of course you will be getting our special currency."
            "Pawn" "You can buy back your items, but don’t expect them to come cheap, I got to make a profit after all."
            e 1 "Can’t I get some gold coins? "
            "Pawn" "I can never understand you mortals’ obsessions with gold, but fine, just for you, I will let you exchange our “Bevocr” for some gold coins."
            e 1 "Be-what?"
            "He points to the purple coin."
            e 1 "Oh ok."
            "The pawn shop is able to buy some kinds of items from your inventory, including key items."
            "Sell key items you don't need or want here in exchange for Bevocr, the underground city's currency."
            "You can exchange Bevocr for gold, and even buy back items you sold before, but they are sold at three times the coins you got for it."
            e 1 "Is there any other way for me to earn Bevocr?"
            "Pawn" "Sure you can, go sell that sweet ass in the red light district."
            "He laughs heartily."
            e 10 "You’re joking."
            "Pawn" "Nope, you’d make a good bitch, and demons would pay well for that."
            "Pawn" "Let me show you where to go."
            "He claps his hands and you get a vision of the part of the city you need to go to. "
            "There are bright lights everywhere in that section of the city."
            "Pawn" "You’re welcome."
            "You can now go to the red light district."
            $ Map.undercity_5 = 2
            $ Map.undercity_13 = 1
            jump undercity_pawn
        elif True:
            label undercity_pawn:
                menu:
                    "Sell items" if True:
                        "You need to spend three times the price to buy back."
                        menu:
                            "Pickaxe" if jane_inv_K.qty(pickaxe) != None:
                                $ Map.undercity_worktime_earn = 10
                                "Pawn" "A rusted pickaxe."
                                "Pawn" "I’ve seen golden pickaxes, but never a rusted one before."
                                "You get [Map.undercity_worktime_earn] Bevocr."
                                $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                                $ jane_inv_K.drop(pickaxe,1)
                                $ Map.undercity_pawn_pickaxe = 1
                                jump undercity_pawn
                            "Jester Badge" if jane_inv_K.qty(jester_badge) != None:
                                $ Map.undercity_worktime_earn = 20
                                "Pawn" "An amusing looking badge, I’d say it came from thousands of years ago."
                                "Pawn" "Assuming if I’m right."
                                "You get [Map.undercity_worktime_earn] Bevocr."
                                $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                                $ jane_inv_K.drop(jester_badge,1)
                                $ Map.undercity_pawn_jester = 1
                                jump undercity_pawn
                            "Knight Badge" if jane_inv_K.qty(knight_badge) != None:
                                $ Map.undercity_worktime_earn = 20
                                "Pawn" "I sense this badge has a lot of story to tell."
                                "Pawn" "Thank you for this rare trinket."
                                "You get [Map.undercity_worktime_earn] Bevocr."
                                $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                                $ jane_inv_K.drop(knight_badge,1)
                                $ Map.undercity_pawn_knight = 1
                                jump undercity_pawn
                            "Prince Badge" if jane_inv_K.qty(prince_badge) != None:
                                $ Map.undercity_worktime_earn = 20
                                "Pawn" "My, my."
                                "Pawn" "You must have ransacked every nook and cranny of the castle up above."
                                "You get [Map.undercity_worktime_earn] Bevocr."
                                $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                                $ jane_inv_K.drop(prince_badge,1)
                                $ Map.undercity_pawn_prince = 1
                                jump undercity_pawn
                            "Ethereal Blade piece" if jane_inv_K.qty(sword_fragment) != None:
                                $ Map.undercity_worktime_earn = 30
                                "Pawn" "Another ethereal blade piece to add to my collection. "
                                "You get [Map.undercity_worktime_earn] Bevocr."
                                $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                                $ jane_inv_K.drop(sword_fragment,1)
                                $ Map.undercity_pawn_ethereal = 1
                                jump undercity_pawn
                            "Skull emblem" if jane_inv_K.qty(Skull_emblem) != None:
                                $ Map.undercity_worktime_earn = 5
                                "Pawn" "A normal emblem."
                                "Pawn" "Well, fine I’ll take it."
                                "You get [Map.undercity_worktime_earn] Bevocr."
                                $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                                $ jane_inv_K.drop(Skull_emblem,1)
                                $ Items.em =Items.em-1
                                $ Map.undercity_pawn_Skull = 1
                                jump undercity_pawn
                            "Ebb’s necklace" if jane_inv_K.qty(ebb_necklace) != None:
                                $ Map.undercity_worktime_earn = 60
                                "Pawn" "What a beautiful piece of jewellery."
                                "Pawn" "I can offer you something for it."
                                "You get [Map.undercity_worktime_earn] Bevocr."
                                $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                                $ jane_inv_K.drop(ebb_necklace,1)
                                $ Map.undercity_pawn_necklace = 1
                                jump undercity_pawn
                            "Back" if True:
                                jump undercity_pawn
                    "Buy back items" if True:
                        menu:
                            "Pickaxe" if Map.undercity_pawn_pickaxe == 1:
                                $ Map.undercity_worktime_earn = 30
                                if Map.undercity_worktime_earn > jane_inv_K.qty(bevocr):
                                    "You need [Map.undercity_worktime_earn] Bevocr to buy this back."
                                    jump undercity_pawn
                                elif True:
                                    "You buy this item back."
                                    $ jane_inv_K.drop(bevocr,Map.undercity_worktime_earn)
                                    $ jane_inv_K.take(pickaxe,1)
                                    $ Map.undercity_pawn_pickaxe = 0
                                    jump undercity_pawn
                            "Jester Badge -60B" if Map.undercity_pawn_jester == 1:
                                $ Map.undercity_worktime_earn = 60
                                if Map.undercity_worktime_earn > jane_inv_K.qty(bevocr):
                                    "You need [Map.undercity_worktime_earn] Bevocr to buy this back."
                                    jump undercity_pawn
                                elif True:
                                    "You buy this item back."
                                    $ jane_inv_K.drop(bevocr,Map.undercity_worktime_earn)
                                    $ jane_inv_K.take(jester_badge,1)
                                    $ Map.undercity_pawn_jester = 0
                                    jump undercity_pawn
                            "Knight Badge -60B" if Map.undercity_pawn_knight == 1:
                                $ Map.undercity_worktime_earn = 60
                                if Map.undercity_worktime_earn > jane_inv_K.qty(bevocr):
                                    "You need [Map.undercity_worktime_earn] Bevocr to buy this back."
                                    jump undercity_pawn
                                elif True:
                                    "You buy this item back."
                                    $ jane_inv_K.drop(bevocr,Map.undercity_worktime_earn)
                                    $ jane_inv_K.take(knight_badge,1)
                                    $ Map.undercity_pawn_knight = 0
                                    jump undercity_pawn
                            "Prince Badge -60B" if Map.undercity_pawn_prince == 1:
                                $ Map.undercity_worktime_earn = 60
                                if Map.undercity_worktime_earn > jane_inv_K.qty(bevocr):
                                    "You need [Map.undercity_worktime_earn] Bevocr to buy this back."
                                    jump undercity_pawn
                                elif True:
                                    "You buy this item back."
                                    $ jane_inv_K.drop(bevocr,Map.undercity_worktime_earn)
                                    $ jane_inv_K.take(prince_badge,1)
                                    $ Map.undercity_pawn_prince = 0
                                    jump undercity_pawn
                            "Ethereal Blade piece -90B" if Map.undercity_pawn_ethereal == 1:
                                $ Map.undercity_worktime_earn = 90
                                if Map.undercity_worktime_earn > jane_inv_K.qty(bevocr):
                                    "You need [Map.undercity_worktime_earn] Bevocr to buy this back."
                                    jump undercity_pawn
                                elif True:
                                    "You buy this item back."
                                    $ jane_inv_K.drop(bevocr,Map.undercity_worktime_earn)
                                    $ jane_inv_K.take(sword_fragment,1)
                                    $ Map.undercity_pawn_ethereal = 0
                                    jump undercity_pawn
                            "Skull emblem -15B" if Map.undercity_pawn_Skull == 1:
                                $ Map.undercity_worktime_earn = 15
                                if Map.undercity_worktime_earn > jane_inv_K.qty(bevocr):
                                    "You need [Map.undercity_worktime_earn] Bevocr to buy this back."
                                    jump undercity_pawn
                                elif True:
                                    "You buy this item back."
                                    $ jane_inv_K.drop(bevocr,Map.undercity_worktime_earn)
                                    $ jane_inv_K.take(Skull_emblem,1)
                                    $ Items.em =Items.em+1
                                    $ Map.undercity_pawn_Skull = 0
                                    jump undercity_pawn
                            "Ebb’s necklace -180B" if Map.undercity_pawn_necklace == 1:
                                $ Map.undercity_worktime_earn = 180
                                if Map.undercity_worktime_earn > jane_inv_K.qty(bevocr):
                                    "You need [Map.undercity_worktime_earn] Bevocr to buy this back."
                                    jump undercity_pawn
                                elif True:
                                    "You buy this item back."
                                    $ jane_inv_K.drop(bevocr,Map.undercity_worktime_earn)
                                    $ jane_inv_K.take(ebb_necklace,1)
                                    $ Map.undercity_pawn_necklace = 0
                                    jump undercity_pawn
                            "Back" if True:
                                jump undercity_pawn
                    "Уйти" if True:

                        jump undercity_map


            jump undercity_map
    if _return == 'point 6':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_6 == 1:
            "You come by a secluded area."
            "It appears to be a run down building. Inside there is a bored looking demon flipping through a book behind a counter."
            "The sign above the establishment is broken in half."
            "What remains standing reads “Inn F-”"
            "You decide to check the place out."
            e 1 "Hello."
            "Innkeeper" "Mmhmm."
            e 1 "Is this an inn?"
            "Innkeeper" "Mmhmm."
            "The innkeeper doesn’t even bother to look past his book."
            e 6 "Can I stay here?"
            "Innkeeper" "Mmhmm."
            e 1 "How much?"
            "The innkeeper clearly frustrated by your questions rolls his eyes and closes his book."
            "He forms a circle with his right thumb and forefinger. "
            e 9 "Why is staying here free?"
            "Innkeeper" "Ngh..."
            "Innkeeper" "Easier for them to get back to work."
            e 1 "Never mind then. Not a chatty bunch, these demons."
            $ Map.undercity_6 = 2
            jump undercity_room1
        elif True:
            label undercity_room1:
                if Map.undercity_6 == 3:
                    scene room 6 with slow_dissolve
                menu:

                    "Rest to afternoon" if Map.undercity_worktime_time == "Morning"and Map.undercity_auc_start == 1:
                        scene black
                        "You sleep for 6 hours, feel refreshed and full of energy."
                        "Your Stamina points has been restored 2 points."
                        $ Map.undercity_worktime_sp = min(Map.undercity_worktime_sp+2, Map.undercity_worktime_maxsp)
                        $ Zalt.hp = Zalt.maxhp
                        $ Zalt.mp = Zalt.maxmp
                        $ Time.hours = Time.hours+6
                        $ Zalt.lust = Zalt.lust + 10
                        jump undercity_room1_rest
                    "Rest to night" if Map.undercity_worktime_time == "Afternoon"and Map.undercity_auc_start == 1:
                        scene black
                        "You sleep for 6 hours, feel refreshed and full of energy."
                        "Your Stamina points has been restored 2 points."
                        $ Map.undercity_worktime_sp = min(Map.undercity_worktime_sp+2, Map.undercity_worktime_maxsp)
                        $ Zalt.hp = Zalt.maxhp
                        $ Zalt.mp = Zalt.maxmp
                        $ Time.hours = Time.hours+6
                        $ Zalt.lust = Zalt.lust + 10
                        jump undercity_room1_rest

                    "Sleep until morning." if (Map.undercity_worktime_time == "Night" or Map.undercity_worktime_time == "Sleep") and Map.undercity_auc_start == 1:
                        scene black
                        "You sleep until morning, feel refreshed and full of energy."
                        if Map.undercity_worktime_time == "Night":
                            "Your Stamina points has been restored 5 points."
                            $ Zalt.lust = Zalt.lust + 40
                            $ Map.undercity_worktime_sp = min(Map.undercity_worktime_sp+5, Map.undercity_worktime_maxsp)
                            $ Time.days = Time.days+1
                            $ Time.hours = 6
                            $ Time.mins = 30
                        if Map.undercity_worktime_time == "Sleep":
                            "Your Stamina points has been restored 2 points."
                            $ Zalt.lust = Zalt.lust + 20
                            $ Map.undercity_worktime_sp = min(Map.undercity_worktime_sp+2, Map.undercity_worktime_maxsp)
                            $ Time.hours = 6
                            $ Time.mins = 30
                        $ Zalt.hp = Zalt.maxhp
                        $ Zalt.mp = Zalt.maxmp
                        jump undercity_room1_rest
                    "Rest" if Map.undercity_auc_start != 1:
                        scene black
                        "You sleep for 3 hours, feel refreshed and full of energy."
                        "HP and MP have been restored half of the maximum."
                        $ Zalt.hp = min(Zalt.hp+Zalt.maxhp/2, Zalt.maxhp)
                        $ Zalt.mp = min(Zalt.mp+Zalt.maxmp/2, Zalt.maxmp)
                        $ Time.hours = Time.hours+3

                        jump undercity_map
                    "Rest until evening" if Time.hours >= 6 and Time.hours <15 and Map.undercity_auc_start != 1:
                        scene black
                        "You sleep until evening, feel refreshed and full of energy."
                        "HP and MP have been restored to maximum."
                        $ Zalt.hp = Zalt.maxhp
                        $ Zalt.mp = Zalt.maxmp

                        $ Time.hours = 18
                        $ Time.mins = 0

                        jump undercity_map

                    "Sleep" if (Time.hours < 6 or Time.hours >=21) and Map.undercity_auc_start != 1:
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

                        jump undercity_map
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


                        jump undercity_map
                    "Masturbate" if Zalt.lust >= 40:
                        "You spend some time to deal with your desires."
                        "Influenced by the city, when you are in the city, your minimum lust won't be less than 20."
                        $ Zalt.lust = 20
                        $ Time.mins = Time.mins+15
                        jump undercity_map
                    "Уйти" if True:
                        jump undercity_map


            label undercity_room1_rest:
                if Map.undercity_6 == 2:
                    scene black with dissolve
                    "The innkeeper snaps his fingers and you are teleported to a room."
                    scene room 6 with slow_dissolve
                    "A single lightbulb hangs above the room."
                    "Its light illuminates the sad looking mattress on the floor and the one beaten up pillow on it."
                    "There’s a single window that when you walk up close gives you a bird’s eye view of the entire city."
                    "You sigh and decide to rest."
                    $ Map.undercity_6 = 3
                elif True:
                    jump undercity_map
                scene black with dissolve
                "You rest and leave."
                jump undercity_map

            jump undercity_map
    if _return == 'point 7':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_7 == 1 or Map.undercity_7 == 2:
            if Map.undercity_worktime_time == "Sleep":
                "This work place is closed now, come back later."
                jump undercity_map
            if Map.undercity_7 == 1:
                "A short and stout looking red dragon dressed in coal stained clothes stands in front of a door with the sign, “MINE” written above."
                "Next to him are bags of minerals you have never seen before."
                "Dragon Miner" "Welcome to the mines. You got strong hands, we got work."
                e 1 "What’s the job and what’s the pay?"
                $ Map.undercity_7 = 2
            $ Map.undercity_worktime_earn = 8
            "Dragon Miner" "I need you to mine for the ores inside here."
            "Dragon Miner" "The pay is [Map.undercity_worktime_earn] Bevocr for every bag of ores you hand in."
            "Do you want the job?"
            menu:
                "Yes (STR check)" if True:
                    if Map.undercity_worktime_sp < 1:
                        "You don't have enough stamina point."
                        jump undercity_map
                    e 1 "I’ll take the job."
                    if Map.undercity_14 < 3:
                        "Dragon Miner" "Sorry,kid. You don't have the work permision."
                        "(You need to start the working week first.)"
                        jump undercity_map
                    elif True:
                        "The demon conjures up a pickaxe and an empty sack and gives it to you."
                        "You work several hours to fill the empty bag."
                        $ renpy.music.set_volume(0, 2, channel = "Chan1")
                        scene black with slow_dissolve
                        play sound "music/anvil.ogg"
                        pause 7
                        $ renpy.music.set_volume(1, 3, channel = "Chan1")
                        scene undercity 1 with dissolve

                    if Zalt.str >= 7:
                        $ Map.undercity_worktime_check = True
                    elif True:
                        $ Map.undercity_worktime_check = False

                    if Map.undercity_worktime_time == "Morning":
                        $ Map.undercity_worktime_bnous = True
                    elif True:
                        $ Map.undercity_worktime_bnous = False


                    if Map.undercity_worktime_check == False:
                        "Dragon Miner" "Sorry chap, there’s not that many ores in this bag."
                        "Dragon Miner" "Try to get stronger and mine more."
                        $ Map.undercity_worktime_earn = Map.undercity_worktime_earn - 2
                    elif True:
                        "Dragon Miner" "Mmm, good. Here’s your pay."
                    if Map.undercity_worktime_bnous == True:
                        "Dragon Miner" "By the way, since you worked so hard this time I will give you a bonus."
                        "Dragon Miner" "Consider it an incentive to keep coming here at the same time. I could use the help."
                        $ Map.undercity_worktime_earn = (Map.undercity_worktime_earn)*2

                    "You get [Map.undercity_worktime_earn] Bevocr as reward."
                    $ Zalt.lust = Zalt.lust + 10
                    $ Map.undercity_worktime_sp = Map.undercity_worktime_sp -1
                    $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                    $ Time.hours = Time.hours + 6
                    jump undercity_map
                "No" if True:




                    e 6 "Maybe not today."
                    jump undercity_map

        jump undercity_map

    if _return == 'point 8':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_8 == 1 or Map.undercity_8 == 2:
            if Map.undercity_worktime_time == "Sleep":
                "This work place is closed now, come back later."
                jump undercity_map
            if Map.undercity_8 == 1:
                "Bartender" "Welcome to the Three Hounds Bar."
                "A talking flame dressed in a black and white suit stands behind a bar."
                "You approach the bartender."
                e 1 "What work do you have?"
                $ Map.undercity_8 = 2
            $ Map.undercity_worktime_earn = 8
            "Bartender" "I need someone quick on their feet to help me take orders and to hand out the food and drinks."
            "Bartender" "The pay is [Map.undercity_worktime_earn] Bevocr for one shift."
            "Do you want the job?"
            menu:
                "Yes (AGI check)" if True:
                    if Map.undercity_worktime_sp < 1:
                        "You don't have enough stamina point."
                        jump undercity_map
                    e 1 "I’ll take the job."
                    if Map.undercity_14 < 3:
                        "Bartender" "Sorry. You don't have the work permision."
                        "(You need to start the working week first.)"
                        jump undercity_map
                    elif True:
                        e 1 "Bring it on."
                        "You rush through the orders at blazing speeds."
                        "Hours pass until you finish your shift."
                        $ renpy.music.set_volume(0, 2, channel = "Chan1")
                        scene black with slow_dissolve
                        play sound "music/foot1.ogg"
                        pause 2
                        play sound "music/foot1.ogg"
                        pause 2
                        play sound "music/foot1.ogg"
                        pause 2
                        $ renpy.music.set_volume(1, 3, channel = "Chan1")
                        scene undercity 1 with dissolve

                    if Zalt.agi >= 7:
                        $ Map.undercity_worktime_check = True
                    elif True:
                        $ Map.undercity_worktime_check = False

                    if Map.undercity_worktime_time == "Night":
                        $ Map.undercity_worktime_bnous = True
                    elif True:
                        $ Map.undercity_worktime_bnous = False


                    if Map.undercity_worktime_check == False:
                        "Bartender" "I’m afraid you were too slow."
                        "Bartender" "I got a ton of complaints from customers who didn’t get their food in time."
                        $ Map.undercity_worktime_earn = Map.undercity_worktime_earn - 2
                    elif True:
                        "Bartender" "Not bad. Here’s the cash."
                        "Bartender" "Come again if you want more work."
                    if Map.undercity_worktime_bnous == True:
                        "Bartender" "Thank you very much for being able to help me at this time."
                        "Bartender" "Night time is an insane rush. Consider this your tip for helping."
                        $ Map.undercity_worktime_earn = (Map.undercity_worktime_earn)*2

                    "You get [Map.undercity_worktime_earn] Bevocr as reward."
                    $ Zalt.lust = Zalt.lust + 10
                    $ Map.undercity_worktime_sp = Map.undercity_worktime_sp -1
                    $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                    $ Time.hours = Time.hours + 6
                    jump undercity_map
                "No" if True:

                    e 6 "Maybe not today."
                    jump undercity_map

        jump undercity_map


    if _return == 'point 9':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_9 == 1 or Map.undercity_9 == 2:
            if Map.undercity_worktime_time == "Sleep":
                "This work place is closed now, come back later."
                jump undercity_map
            if Map.undercity_9 == 1:
                "You reach what can only be described as the slums of the city."
                "The smell of rotting flesh and filth lingers in the air."
                "No wonder, there are piles upon piles of trash lying about."
                "There’s a red octopus with a broom sweeping up the place."
                "His black overall has the words CLEANER on the back."
                e 1 "Hey, do you need any help around here?"
                "Cleaner" "Really? You’re offering to help? Is this some kind of a trick?"
                e 6 "No, no. I’m looking for work. "
                "Cleaner" "Ah, well I could always use an extra pair of hands to clean this area up."
                "Cleaner" "It’s basically the dumping site of the city’s denizens, every day there will be new filth."
                "Cleaner" "If I can clean up more of this area, I get paid more for that day."
                $ Map.undercity_9 = 2
            $ Map.undercity_worktime_earn = 8
            "Cleaner" "You look like you can endure some bad smells."
            "Cleaner" "Want to work with me? The pay would be [Map.undercity_worktime_earn] Bevocr."
            "Do you want the job?"
            menu:
                "Yes (END check)" if True:
                    if Map.undercity_worktime_sp < 1:
                        "You don't have enough stamina point."
                        jump undercity_map
                    e 1 "I’ll take the job."
                    "Cleaner" "Good, then let’s get you a broom."
                    if Map.undercity_14 < 3:
                        "Cleaner" "Wait, you have the work permission right?"
                        e 9 "Ehh,not yet."
                        "Cleaner" "Go to get the permission first!"
                        "(You need to start the working week first.)"
                        jump undercity_map
                    elif True:
                        "You work with the cleaner scraping, sweeping and mopping up all the vile, rotten and disgusting trash that you could find for a few hours."
                        $ renpy.music.set_volume(0, 2, channel = "Chan1")
                        scene black with slow_dissolve
                        play sound "music/foot1.ogg"
                        pause 2
                        play sound "music/foot1.ogg"
                        pause 2
                        play sound "music/foot1.ogg"
                        pause 2
                        $ renpy.music.set_volume(1, 3, channel = "Chan1")
                        scene undercity 1 with dissolve

                    if Zalt.end >= 7:
                        $ Map.undercity_worktime_check = True
                    elif True:
                        $ Map.undercity_worktime_check = False

                    if Map.undercity_worktime_time == "Morning":
                        $ Map.undercity_worktime_bnous = True
                    elif True:
                        $ Map.undercity_worktime_bnous = False


                    if Map.undercity_worktime_check == False:
                        "You can't stand the smell of these garbage at all, you spend a lot of time vomiting."
                        "Cleaner" "Man, where is your endurance?"
                        "Cleaner" "You barely picked up any trash."
                        "Cleaner" "This is your pay."
                        $ Map.undercity_worktime_earn = Map.undercity_worktime_earn - 2
                    elif True:
                        "Cleaner" "Not bad,I could always use your help again."
                        "Cleaner" "As promised, here is your pay."
                    if Map.undercity_worktime_bnous == True:
                        "Cleaner" "Thanks for helping me out in the day, these demons always complain if they smell any trash throughout the day."
                        "Cleaner" "It’s such a headache how more and more trash keeps piling up because of the night time carnival."
                        "Cleaner" "Here are your tips."
                        $ Map.undercity_worktime_earn = (Map.undercity_worktime_earn)*2

                    "You get [Map.undercity_worktime_earn] Bevocr as reward."
                    $ Zalt.lust = Zalt.lust + 10
                    $ Map.undercity_worktime_sp = Map.undercity_worktime_sp -1
                    $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                    $ Time.hours = Time.hours + 6
                    jump undercity_map
                "No" if True:

                    e 6 "Maybe not today."
                    jump undercity_map

        jump undercity_map

    if _return == 'point 10':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "It’s an onyx black slate with inscriptions on it that you do not recognize."
        "Around the slate, various assortments of food and flowers are placed all over."
        e 1 "I wonder what this is for."

        jump undercity_map
    if _return == 'point 12':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_12 == 1:
            "A wave of people fill the streets."
            "If you could call them people, their bodies are red as the blood that courses through your veins."
            "Some even hide themselves behind knee long cloaks."
            "They come and go uninterested in you and your needs."
            "They would even bump into you but remain unfazed."
            "The people of this town seem more preoccupied with getting to where they need to go. "
            e 1 "Hey you got a minute?"
            "You grab a person by the shoulder and they turn."
            "Your mind instantly reels back in shock. The person’s face cannot be seen!"
            "It is as though their eyes are lost in darkness, leaving only a nose and a mouth."
            e 9 "Err... nothing."
            "The person turns away and walks off."
            "You then spot someone dressed like the guards before."
            e 9 "Hey, guard!"
            "Guard" "Muhh..."
            e 1 "I’m looking for the guy who runs this place."
            "The guard points to a large colosseum like building."
            "It stands rather intrusively in the middle of the city."
            "Like a giant watching the masses."
            e 5 "That looks like a lot of steps to climb."
            "Guard" "Buhh..."
            e 1 "Oh, thanks."
            "The guards walks away."
            "Time to go to meet the boss."
            $ Map.undercity_12 = 2
            $ Map.undercity_14 = 1

            jump undercity_map
        elif True:
            "This place looks safe to set up a campfire and rest."
            "You can also level up here."


    if _return == 'point 13':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_13 == 1 or Map.undercity_13 == 2:
            if Map.undercity_worktime_time == "Sleep":
                "This work place is closed now, come back later."
                jump undercity_map
            if Map.undercity_13 == 1:
                "This part of the city is illuminated with bright light bulbs of varying colours."
                "There is a long line of cloaked figures heading towards the doorstep to one of the buildings."
                "The bright red sign says Love Hotel."
                e 1 "What is this place?"
                "Just as you ask that question, a wisp of red smoke circles around you and a tall cloaked figure appears."
                "Unlike the others, this one’s robes are decorated in gold."
                "Its imposing stature is alarming."
                "Peak" "Welcome to my domain little pup."
                "Peak" "The name’s Peak, and I own the Love Hotel."
                e 1 "Errr, sure. Maybe I’m in the wrong place."
                "Peak" "Oh quite contrary, I think you are in the right place."
                "Peak" "I can see it in your eyes that you are in need of some Bevocr."
                e 6 "You mean you have a job here?"
                "Peak" "Of course! There’s plenty of work here."
                "Peak" "We have demons and demons have needs, sexual needs."
                "Peak" "I think you are just the right person to give them what they want."
                e 10 "What?!"
                "Peak" "You are different, you’re a mortal."
                "Peak" "Do you know how much these demons would pay to spend a night with a mortal?"
                e 1 "Err..."
                "Peak" "Mortal flesh is rare, just imagine it."
                "Peak" "If they can’t win a mortal of their own at the auction, they can at least spend a night with one."
                "Peak" "I’ll only take a very small percentage of your earnings, and I will ensure you get paid handsomely and that you are safe while working for me."
                e 1 "Just how much are we talking here?"





                $ Map.undercity_13 = 2
            $ Map.undercity_worktime_earn = 15
            "Peak" "You will get 10 Bevocr for one round of work."
            "Peak" "What do you say? Interested?"
            "Do you want to take the job?"
            menu:
                "Yes" if True:
                    if Map.undercity_worktime_sp < 1:
                        "You don't have enough stamina point."
                        jump undercity_map
                    if Map.undercity_14 < 3:
                        "(You need to start the working week first.)"
                        jump undercity_map
                    elif True:
                        e 11 "Beggars can’t be choosers. I’ll take the job."
                        "Peak" "Excellent. I’ll send you straight away to your room."
                        "Peak" "Don’t worry you’ll be brought back out when time’s up."
                        "He claps his hands and a swirl of black smoke floods your vision. "
                        $ renpy.music.set_volume(0, 2, channel = "Chan1")
                        scene black with slow_dissolve
                        play sound "music/foot1.ogg"
                        pause 2
                        jump undercity_eyvind_sell
                        label undercity_eyvind_sell_end:
                            $ renpy.music.set_volume(1, 3, channel = "Chan1")
                            scene undercity 1 with dissolve
                            if Map.undercity_worktime_time == "Night":
                                $ Map.undercity_worktime_bnous = True
                            elif True:
                                $ Map.undercity_worktime_bnous = False

                            "You reemerge outside of the Love Hotel."

                            if Zalt.lust < 40:
                                "Peak is standing with his arms crossed, shaking his head disapprovingly at you."
                                e 10 "What?"
                                "Peak just sighs."
                                e 10 "Was my performance not lustful enough? Do I need more lust?"
                                "Peak nods."
                                "He hands you a bag of Bevocr and disappears."
                                $ Map.undercity_worktime_earn = Map.undercity_worktime_earn - 8
                            elif Zalt.lust > 80:
                                "Peak stands in front of you clapping."
                                e 10 "What?"
                                "Peak gives you a thumbs up."
                                e 10 "Are they saying I did good?"
                                "Peak makes a heavy sack of Bevocr appear and hands it to you."
                                e 1 "Umm... thanks?"
                                "Peak then vanishes in a puff of smoke."
                                $ Map.undercity_worktime_earn = Map.undercity_worktime_earn + 8
                            elif True:
                                "Peak stands in front of you, grinning."
                                "Peak" "Heh..."
                                "You look at your body, and it is all clean."
                                "You even have your clothes and equipment back."
                                e 10 "That was-"
                                "Peak hands over a small pouch to you. "
                                e 1 "Umm... thanks?"
                                "Peak bows and disappears into the darkness."
                            if Map.undercity_worktime_bnous == True:
                                "There is a long line of demons still waiting to get inside."
                                e 6 "Huh, guess he’s too busy to talk."
                                e 1 "This feels like a lot maybe working at this time is more profitable."
                                $ Map.undercity_worktime_earn = (Map.undercity_worktime_earn)*2
                            "You get [Map.undercity_worktime_earn] Bevocr as reward."
                            "Influenced by the city, when you are in the city, your minimum lust won't be less than 20."
                            $ Map.undercity_worktime_sp = Map.undercity_worktime_sp -1
                            $ persistent.CG_eyvind_sell = True
                            $ Zalt.lust = 20
                            $ Zalt.cor = min(Zalt.cor +10, 100)
                            $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                            $ Time.hours = Time.hours + 6
                            jump undercity_map
                "No" if True:

                    e 6 "I'll have to think about it."
                    "Peak" "Of course beautiful."
                    "Peak" "Come find me when you decide to change your mind."
                    jump undercity_map

        jump undercity_map


    if _return == 'point 14':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_14 == 1:
            "As you stand at the foot of the door, the guard there greets you with a salute."
            "He doesn’t get in your way so you step through the doorway."
            "The moment you cross the border, the environment around you blurs away, and you find yourself standing in a long and dark corridor."
            "Rows of sconces then light up along the walls leading to a grand door."
            "You continue on forward and open the grand door."
            $ renpy.music.set_volume(0, 5, channel = "Chan1")
            $ renpy.music.set_pause(True, channel='Chan1')
            scene office 1 with slow_dissolve
            play sound "music/phonebell_1.ogg"
            "At first glance, the rows of books that line the walls make you think you’ve entered a library, but there right in front of you, lies a daunting sight. "
            "Behind a great oak table, sits a three headed hellhound."
            "Surrounding the office are these strange metallic boxes with number platings on them, and what looks like a metallic banana rests on top of each one."
            "The boxes make loud ringing sounds that echo throughout the office."
            "On its table, there is a nameplate made in bronze with the words."
            "“Boss” emblazoned on it."
            "You approach the desk with caution."
            "From where you stand, the hound’s middle and left head are busily looking at the document in front of them and muttering to each other in an unknown language of grunts and growls."
            "Meanwhile the right head is fast asleep."
            e 5 "Excuse me? Are you the one who runs this city?"
            h2 "Hummm?"
            h1 "We have a guest."
            h2 "HANG ON."
            "With a snap of its fingers the ringing stops, but the metallic boxes continue to shake about."
            "You assume the hellhound merely took away their sound."
            "The hellhound sits upright, revealing its barrel chest, and muscular arms. "
            show hellhound stand at center with slow_dissolve
            "You look at him carefully."
            "They look very tired and have very severe dark circles."
            "The right head sniffles and continues snoring."
            h2 "Yes, unknown speck. What is it that you want from the ruler of this city?"
            e 1 "I’m here to collect the shark named Flo."
            e 1 "One of the demons took him."
            "The middle head turns to the one on the right."
            h2 "Do we have someone called Flo here?"
            h1 "We have a Florance, or Madam Florine."
            h2 "Yes her, tall proper demon. She was always so full of herself."
            h1 "Indeed, what an elegant demon."
            e 1 "Excuse me! I am looking for Flo the shark."
            e 12 "He doesn’t belong here, and you demons took him."
            h2 "Flo, and a fish, ok."
            hide hellhound stand at center with slow_dissolve
            "Hellhound turned and walked to a pile of paper like a mountain, took out a piece of paper and started reading."
            h1 "He must mean that fish we took for the auction."
            h2 "Is it the fish boy?"
            e 1 "Yes, now give him back."
            show hellhound stand at center with slow_dissolve
            h2 "Well you can’t have him. He’s the main attraction at the auction."
            e 12 "You can’t sell him away. He’s a living person, doing that will make you-"
            h1 "What? Demons? That’s pretty obvious."
            label hellhound_first_talk:
                menu:
                    "Continue to demand for Flo" if True:
                        e 12 "I don’t care, I want him released to me!"
                        "The two heads blink at you, they appear surprised that you spoke to them in such a manner."
                        h1 "You know, he’s right. What we did was wrong."
                        h2 "You think?"
                        h1 "Yes, we should give him the “shark”."
                        hide hellhound stand at center with slow_dissolve
                        "The hellhound snaps his finger and a dismembered shark head flops in front of your feet."
                        e 9 "Aaah!!" with vpunch
                        "You back away in a panic and accidentally step on your tail causing you to trip backwards."
                        e 9 "Flo!" with vpunch
                        "Both heads laugh in unison."
                        "Gripping their stomach while they point at you."
                        "The commotion even causes the right head to stir awake for a second before quickly dozing off again."
                        "With another snap of their finger, the head disappears."
                        show hellhound stand at center with slow_dissolve
                        h2 "Foolish mortal. You think you can demand anything from us?"
                        h2 "We rule this city, and here you play by our rules."
                        h1 "So if you want your friend back, you better get some coins and be ready to join the auction."
                        e 12 "Damn it."
                        jump hellhound_first_talk
                    "Ask about the Auction" if True:

                        e 13 "Fine, then let me register for the auction. I’ll win his freedom."
                        h1 "Ah, that we can do."
                        h2 "First, we bet you don’t have even a single Bevocr on you."
                        h2 "So, you’ll need a work permit to start earning."
                        hide hellhound stand at center with slow_dissolve
                        "The hound snaps their finger again before a piece of parchment and a quill pen appears in front of you."
                        show hellhound stand at center with slow_dissolve
                        h2 "Put your name on the dotted line, and sign next to it."
                        "Briefly skimming through, you recognize the parchment is a registration form for a work permit."
                        "With the pen, you sign the document."
                        "The parchment erupts into flames and disappears in a puff of smoke along with the quill pen."
                        h2 "There we go, you are now a registered worker here."
                        h2 "Go to any establishment and you can take on any jobs."
                        e 1 "And the auction?"
                        h2 "Right, the auction, it’s a fun affair so many things to get your hands on if you have the coin for it."
                        h2 "But head our warning, the treasures for auction are not cheap."
                        h1 "The auction is scheduled to start in a week."
                        h1 "You might just make it in time if you sign up now."
                        h2 "But, whether you make enough money by then is up to you."
                        h2 "So, are you sure that you want to join?"
                        e 1 "I’m joining."
                        "The hellhound writes something down."
                        h2 "And done, we’ll be seeing you in a week."
                        e 1 "Wait... err... what do I call you?"
                        h2 "We are the Boss of course."
                        e 8 "No, I mean you the middle head specifically."
                        hide hellhound stand at center with dissolve
                        "The two heads turn to one another then back to you with a cocky grin plastered on their faces."
                        show hellhound stand at center with dissolve
                        "The third sleeping head just snores."
                        h2 "We’ve always been Boss, nothing more, nothing less."
                        e 8 "Well you can’t go around calling yourself Boss, that will confuse people."
                        e 1 "Like say I want to talk to the Boss."
                        h2 "Yea?"
                        e 1 "No, I meant the left one."
                        h1 "This is a problem we never thought about before."
                        h2 "Very well, then you mortal shall have the honour of bestowing us names."
                        h2 "If that will finally end this dreaded conversation."
                        h1 "Yes, yes. We have a lot of work to attend to."
                        play sound "music/phonebell_2.ogg"
                        "Just as the head said that, several portals appear above the desks that drop piles of paper on top of the already existing piles on the desks."
                        "Both heads groan at the sight of the work."
                        h1 "Now give us our names and go."
                        label Hellhound_name_1:
                            $ h1_name = renpy.input("What is the name of the Left Head?",length = 12,exclude = ".?!")

                            if h1_name == u"":
                                $ h1_name = u"Left Head"
                                h1 "What's wrong, didn't you say you want to name us?."
                                jump Hellhound_name_1

                        label Hellhound_name_2:
                            $ h2_name = renpy.input("What is the name of the Middle Head?",length = 12,exclude = ".?!")


                            if h2_name == u"":
                                $ h2_name = u"Middle Head"
                                h2 "What's wrong, didn't you say you want to name us?."
                                jump Hellhound_name_2

                        label Hellhound_name_3:
                            $ h3_name = renpy.input("What is the name of the Right Head?",length = 12,exclude = ".?!")

                            if h3_name == u"":
                                h2 "What's wrong, didn't you say you want to name us?."
                                jump Hellhound_name_3
                        h1 "Now that is settled. Now with that settled."
                        h1 "Off with you. We have a lot of work."
                        h2 "Come back when we're free if you wish to speak."
                        e 5 "Wait-"
                        "With a wave of its hand, you are teleported back outside of the building."
                        with flashbulb
                        scene undercity 1 with slow_dissolve
                        "The auction will begin after 7 days."
                        "The moment you sign up for the auction, the timer will begin."
                        "Use the time you have to earn as much Bevocr by doing odd jobs around the city. "
                        "You are free to leave the demon city even during the 7 days."
                        "In one day you have the morning, afternoon and night time to carry out your jobs."
                        "Depending on the time of day, certain jobs may pay more."
                        "But remember to keep track of your Stamina points (SP)."
                        "Every time you do an activity, it will cost you SP."
                        "Be on the lookout for places to recharge your SP. "
                        "Now you can go around the city to check the work places first."
                        "Click the office point again when you're ready to join the auction."
                        $ Map.undercity_14 = 2
                        $ Map.hellhound_meet = 1

                        $ Map.undercity_7 = 1
                        $ Map.undercity_8 = 1
                        $ Map.undercity_9 = 1
                        $ Map.undercity_15 = 1
                        $ Map.undercity_16 = 1
                        jump undercity_map

        elif Map.undercity_14 == 2:
            label undercity_auc_ready:
                "Do you want to start the working week?"
                "(This action will push the time into the next day moring.)"
                menu:
                    "Start the working week." if True:
                        scene black with slow_dissolve
                        "You rest to the next day morning."
                        $ Map.undercity_auc_start = 1
                        $ Map.undercity_auc_day = Time.days
                        $ Map.undercity_14 = 3
                        $ Time.days = Time.days+1
                        $ Time.hours = 6
                        $ Time.mins = 30
                        $ Map.undercity_auc_item_1 = renpy.random.randint(1, 2)
                        $ Map.undercity_auc_item_2 = renpy.random.randint(1, 2)
                        $ Map.undercity_auc_item_3 = renpy.random.randint(1, 2)
                        $ Map.undercity_auc_item_4 = renpy.random.randint(1, 2)
                        $ Map.undercity_auc_price_1 = renpy.random.randint(20, 30)
                        $ Map.undercity_auc_price_2 = renpy.random.randint(25, 35)
                        $ Map.undercity_auc_price_3 = renpy.random.randint(65, 75)
                        $ Map.undercity_auc_price_4 = renpy.random.randint(45, 55)

                        $ Map.undercity_worktime_sp = 5
                        $ Map.undercity_worktime_maxsp = 5

                        jump undercity_map
                    "Not yet." if True:
                        jump undercity_map
                    "Read the rule again." if True:
                        $ Map.undercity_auc_day0 = Time.days + 8
                        "The auction will begin after 7 days.\n(If you start it today, it will begin at Day[Map.undercity_auc_day0])"
                        "The moment you sign up for the auction, the timer will begin."
                        "Use the time you have to earn as much Bevocr by doing odd jobs around the city. "
                        "You are free to leave the demon city even during the 7 days."
                        "In one day you have the morning, afternoon and night time to carry out your jobs."
                        "Depending on the time of day, certain jobs may pay more."
                        "But remember to keep track of your Stamina points (SP)."
                        "Every time you do an activity, it will cost your SP."
                        "Be on the lookout for places to recharge your SP. "
                        "Now you can go around the city to check the work places first."
                        jump undercity_auc_ready
        elif Map.undercity_14 == 3:
            if Map.undercity_auc_start == 2:
                jump Hellhound_meet
            elif True:
                $ Map.undercity_auc_day0 = Map.undercity_auc_day+8-Time.days
                "Guard" "The Boss has no time for visitors."
                if Map.undercity_auc_start == 1:
                    "Guard" "The auction will start in [Map.undercity_auc_day0] days."
                jump undercity_map
        elif True:

            jump undercity_map

    if _return == 'point 15':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_15 == 1 or Map.undercity_15 == 2:
            if Map.undercity_worktime_time == "Sleep":
                "This work place is closed now, come back later."
                jump undercity_map
            if Map.undercity_15 == 1:
                "You come upon a busy part of the city."
                "There are many demons hanging around either talking to each other or going from building to building with more bags."
                "This place gives off the feeling like demons come here to shop and to relax."
                "In front of you, you see a empty box."
                "You are struck with an idea to make more Bevocr."
                "You grab the box and find a spot where everyone can see you."
                "As you prepare the box on the floor you wonder if you should make some kind of announcement."
                "But you are overcome with embarrassment the moment you think you have to say something out loud like that."
                "But you need the money."
                e 1 "Should I really do this?"
                e 1 "If I put on a good show maybe I can get Bevocr from the crowd."
                $ Map.undercity_15 = 2
            $ Map.undercity_worktime_earn = 8
            "Do you want the job?"
            menu:
                "Yes (CHA check)" if True:
                    if Map.undercity_worktime_sp < 1:
                        "You don't have enough stamina point."
                        jump undercity_map
                    if Map.undercity_14 < 3:
                        "The guard appeared and kicked your box over."
                        "(You need to start the working week first.)"
                        jump undercity_map
                    elif True:
                        e 1 "Demons young and old! Come and see a show from the mortal world! "
                        "Your announcement draws the eyes of many of the demons nearby."
                        "It almost hurts to keep up the smile, but you do it for the audience."
                        $ renpy.music.set_volume(0, 2, channel = "Chan1")
                        scene black with slow_dissolve
                        play sound "music/foot1.ogg"
                        pause 2
                        play sound "music/foot1.ogg"
                        pause 2
                        play sound "music/foot1.ogg"
                        pause 2
                        $ renpy.music.set_volume(1, 3, channel = "Chan1")
                        scene undercity 1 with dissolve

                    if Zalt.cha >= 7:
                        $ Map.undercity_worktime_check = True
                    elif True:
                        $ Map.undercity_worktime_check = False

                    if Map.undercity_worktime_time == "Afternoon":
                        $ Map.undercity_worktime_bnous = True
                    elif True:
                        $ Map.undercity_worktime_bnous = False


                    if Map.undercity_worktime_check == False:
                        "You start off poorly by singing off key."
                        "The demons that watch you are now laughing their heads off."
                        "The embarrassment is physically painful to experience, but you are forced to go on."
                        "The performance is pretty much downhill from there."
                        "You failed to be charming to attract the audience."
                        $ Map.undercity_worktime_earn = Map.undercity_worktime_earn - 2
                    elif True:
                        "You start with a song you know most familiar with."
                        "Your voice captures the audience's interest."
                        "One by one they gather around to hear your song."
                        "Thanks to your charming performance you made a nice profit."
                    if Map.undercity_worktime_bnous == True:
                        "Also, it seems that there are more passersby in the afternoon than the rest of the day, this could be a good time to make more money."
                        $ Map.undercity_worktime_earn = (Map.undercity_worktime_earn)*2

                    "You get [Map.undercity_worktime_earn] Bevocr as reward."
                    $ Zalt.lust = Zalt.lust + 10
                    $ Map.undercity_worktime_sp = Map.undercity_worktime_sp -1
                    $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                    $ Time.hours = Time.hours + 6
                    jump undercity_map
                "No" if True:

                    "You think again and decide not to go through with putting on a street show. "
                    "You leave the downtown area."
                    jump undercity_map

        jump undercity_map
    if _return == 'point 16':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"

        if Map.undercity_16 == 1 or Map.undercity_16 == 2:
            if Map.undercity_worktime_time == "Sleep":
                "This work place is closed now, come back later."
                jump undercity_map
            if Map.undercity_16 == 1:
                "You reach a run down looking building. "
                "Its walls are the colour of bronze, the sign above the entrance has already faded, but by squinting hard enough you can read the words."
                "LIBRARY."
                "You enter the library."
                "The moment you step inside, you are greeted by rows filled with shelves of books on the left and right side of the room."
                "Along the middle, there are tables and chairs filled with more books. "
                "The floor itself is littered with the same thing. Books."
                e 1 "What happened here?"
                "With a thunderous clap, a tall owl figure in a black coat appears. "
                "Librarian" "Hooo!"
                e 5 "Uhh, I’m just here looking for work."
                "Librarian" "Hoo."
                "Librarian" "Apologies for the mess I always forget to clean up after my daily reading session."
                $ Map.undercity_16 = 2
            $ Map.undercity_worktime_earn = 8
            "Librarian" "You look smart enough."
            "Librarian" "Well I need you to rearrange all the books according to the library’s indexing system."
            "Librarian" "Get them wrong and I will know."
            "Do you want the job?"
            menu:
                "Yes (INT check)" if True:
                    if Map.undercity_worktime_sp < 1:
                        "You don't have enough stamina point."
                        jump undercity_map
                    if Map.undercity_14 < 3:
                        "(You need to start the working week first.)"
                        jump undercity_map
                    elif True:
                        e 1 "I’ll do the work."
                        "Librarian" "Excellent. I will return when you are done. "
                        "The owl’s body swirls into a vortex and disappears just as quickly as he appeared."
                        "You then begin to pick up the books all around and sort them as per the owl’s instructions."

                        $ renpy.music.set_volume(0, 2, channel = "Chan1")
                        scene black with slow_dissolve
                        play sound "music/foot1.ogg"
                        pause 2
                        play sound "music/foot1.ogg"
                        pause 2
                        play sound "music/foot1.ogg"
                        pause 2
                        $ renpy.music.set_volume(1, 3, channel = "Chan1")
                        scene undercity 1 with dissolve

                    if Zalt.int >= 7:
                        $ Map.undercity_worktime_check = True
                    elif True:
                        $ Map.undercity_worktime_check = False

                    if Map.undercity_worktime_time == "Afternoon":
                        $ Map.undercity_worktime_bnous = True
                    elif True:
                        $ Map.undercity_worktime_bnous = False


                    if Map.undercity_worktime_check == False:
                        "Librarian" "I see you misplacing some books in the wrong sections."
                        "Librarian" "Not good enough I must say."
                        $ Map.undercity_worktime_earn = Map.undercity_worktime_earn - 2
                    elif True:
                        "After a few hours your task is complete."
                        "Librarian" "Not a book out of place, good."
                        "Librarian" "Here is your payment."
                    if Map.undercity_worktime_bnous == True:
                        "Librarian" "Thanks for helping me at this time, I can have a break tonight."
                        "Librarian" "Here are your tips."
                        $ Map.undercity_worktime_earn = (Map.undercity_worktime_earn)*2

                    "You get [Map.undercity_worktime_earn] Bevocr as reward."
                    $ Zalt.lust = Zalt.lust + 10
                    $ Map.undercity_worktime_sp = Map.undercity_worktime_sp -1
                    $ jane_inv_K.take(bevocr,Map.undercity_worktime_earn)
                    $ Time.hours = Time.hours + 6
                    jump undercity_map
                "No" if True:

                    e 6 "Sorry, not now."
                    "Librarian" "Well the books will always be here."
                    "Librarian" "Do come again if you change your mind."
                    jump undercity_map

        jump undercity_map

screen undercity_map:

    imagemap:
        idle 'city_map'
        hover 'city_map'
        if Map.undercity_3 != 2:
            add "map/fog/screen/city_fog_1.png"
        vbox:
            xalign 0.76 ypos 0.02
            imagebutton:
                idle "UI/up button1.png"
                hover "UI/up button2.png"

                action Return("exit")


        vbox:
            xalign 0.68 ypos 0.15
            if Map.undercity_2 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 2")
            elif Map.undercity_2 ==2 or Map.undercity_2 ==3:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 2")
            else:
                pass
        vbox:
            xalign 0.61 ypos 0.14
            if Map.undercity_3 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 3")
            elif Map.undercity_3 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.59 ypos 0.465
            if Map.undercity_4 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 4")
            elif Map.undercity_4 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            elif Map.undercity_4 == 0:
                pass
            else:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 4")
        vbox:
            xalign 0.66 ypos 0.3
            if Map.undercity_5 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 5")
            elif Map.undercity_5 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 5")
            else:
                pass
        vbox:
            xalign 0.69 ypos 0.42
            if Map.undercity_6 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 6")
            elif Map.undercity_6 == 0:
                pass
            else:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 6")

        vbox:
            xalign 0.73 ypos 0.62
            if Map.undercity_auc_start == 2:
                pass
            else:
                if Map.undercity_7 == 1:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 7")
                elif Map.undercity_7 == 0:
                    pass
                else:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 7")
        vbox:
            xalign 0.585 ypos 0.69
            if Map.undercity_auc_start == 2:
                pass
            else:
                if Map.undercity_8 == 1:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 8")
                elif Map.undercity_8 == 0:
                    pass
                else:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 8")
        vbox:
            xalign 0.48 ypos 0.78
            if Map.undercity_auc_start == 2:
                pass
            else:
                if Map.undercity_9 == 1:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 9")
                elif Map.undercity_9 == 0:
                    pass
                else:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 9")

        vbox:
            xalign 0.42 ypos 0.54
            if Map.undercity_10 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 10")
            elif Map.undercity_10 == 2:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 10")
            elif Map.undercity_10 == 0:
                pass
            else:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 10")
        vbox:
            xalign 0.34 ypos 0.54
            if Map.undercity_12 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 12")
            elif Map.undercity_12 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            elif Map.undercity_12 == 0:
                pass
            else:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 12")
        vbox:
            xalign 0.5 ypos 0.2
            if Map.undercity_auc_start == 2:
                pass
            else:
                if Map.undercity_13 == 1:
                    imagebutton:
                        idle "UI/ebutton1.png"
                        hover "UI/ebutton2.png"
                        action Return("point 13")
                elif Map.undercity_13 == 0:
                    pass
                else:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 13")

        vbox:
            xalign 0.35 ypos 0.2
            if Map.undercity_14 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 14")
            elif Map.undercity_14 == 2:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 14")
            elif Map.undercity_14 == 3:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 14")
            elif Map.undercity_14 == 0:
                pass
            else:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 14")
        vbox:
            xalign 0.25 ypos 0.45
            if Map.undercity_auc_start == 2:
                pass
            else:
                if Map.undercity_15 == 1:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 15")
                elif Map.undercity_15 == 0:
                    pass
                else:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 15")
        vbox:
            xalign 0.1 ypos 0.45
            if Map.undercity_auc_start == 2:
                pass
            else:
                if Map.undercity_16 == 1:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 16")
                elif Map.undercity_16 == 0:
                    pass
                else:
                    imagebutton:
                        idle "UI/wbutton1.png"
                        hover "UI/wbutton2.png"
                        action Return("point 16")


        vbox:
            xalign 0.24 ypos 0.52
            if Map.undercity_auc_start == 2 and Hellhound_coffee_quest >= 1:
                if Hellhound_coffee_quest == 1:
                    imagebutton:
                        idle "UI/ebutton1.png"
                        hover "UI/ebutton2.png"
                        action Jump("city_shop")
                else:
                    imagebutton:
                        idle "UI/button1.png"
                        hover "UI/button2.png"
                        action Jump("city_shop")
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

label city_shop:
    "Shopkeeper" "Welcome, what will you have?"
    e 1 "What do you have?"
    "Shopkeeper" "Take a look."
    menu:
        "Bitter beans(8 bevocrs)" if True:
            if jane_inv_K.qty(bevocr) < 8:
                "You don't have enough bevocrs!"
            elif True:
                "You get a bag of bitter beans."
                if Parif.cook_Hcoffee == 0:
                    $ Parif.cook_Hcoffee = 1
                $ jane_inv_K.drop(bevocr,8)
                $ jane_inv_M.take(coffee_beans)
            jump undercity_map
        "Уйти" if True:
            jump undercity_map
label undercity_auction_start:
    h1 "Hello? Is this thing on?"
    "It’s the voice of [h1_name]!"
    "You look around but he isn’t here yet, his voice rings clear in your head."
    h1 "Citizens! It’s that exciting time that comes once every ten years."
    h1 "The grand auction will now begin!"

    if jane_inv_K.qty(bevocr) <= 50:
        h2 "Ooh, I’m sorry. It looks like you don’t have enough Bevocr to join the auction."
        h2 "But feel free to watch from afar as we conduct the auction in front of city hall!"
        "The voice cuts out."
        e 9 "No, how can I not have enough?"
        "{b}{color=#c22719}<GAME OVER>{/color}"
        menu:
            "New game" if True:
                return
            "New game" if True:
                return
    elif True:
        "A black vortex opens up beneath your feet and you fall through."
        e 9 "Aaah!!" with vpunch
        $ renpy.music.set_volume(0, 2, channel = "Chan1")
        play Chan1[ "<silence 0.5>", "music/noisy_people.ogg" ]fadein 3
        scene black with slow_dissolve
        pause 7
        $ renpy.music.set_volume(0.8, 5, channel = "Chan1")
        scene auction 1 with slow_dissolve
        "You reemerge sitting down on a chair alongside many other cloaked figures."
        "Looking around, you recognize the familiarity of this place, it’s just right outside the hellhound’s office."
        "You are sitting on the far left of the front row, you have to crane your neck to the right to see the whole stage."
        "Standing behind a podium is the Hellhound grinning from ear to ear."
        "The sleeping head continues to snore while the other two speak."
        play music "music/hammer_stop.ogg"
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
        pause 8
        stop music
        scene auction 2 with slow_dissolve
        show hellhound stand at center with slow_dissolve
        h2 "Welcome everyone to the auction!"
        h2 "I won’t bore you with a long opening speech."
        h2 "We all know why you’re here, for the goods!"
        "He snaps his finger and a piece of paper appears in everyone’s hands."
        "It documents the hundreds of items on auction, their estimated values and the minimum bid."
        "At the very bottom of the list is something called “Shark”."
        e 5 "(That must be Flo!)"
        h2 "As always, we’ve saved the best for last!"
        h2 "A chance to own your very own mortal servant to do with as you please."
        h2 "The rules of the auction are simple, the item on auction will be presented on stage, and everyone can make a bid for it."
        h2 "The highest bid wins the item."
        h1 "Without further ado, let’s begin!"
        hide hellhound stand at center with slow_dissolve
        "The crowd erupts in a cheer."
        "At first glance the crowd is nothing more than excited demons ready to bid, but each one of them poses a threat to you rescuing Flo."
        "You need to play it smart with your Bevocr."
        scene black with slow_dissolve
        "..."
        pause 3
        play Chan1[ "<silence 0.5>", "music/undercity.ogg" ]fadein 3
        $ renpy.music.set_volume(0.5, 5, channel = "Chan1")
        "The auction continues with several more items you have no interest in."
        "You yawn, it bores you to wait until something importsnt appears."
        "So you leave them be."
        "But there are still a few things that attract your attention."
        scene auction 2 with slow_dissolve
        $ Map.undercity_auc_round = 1
        jump undercity_auction_start_round




label undercity_auction_start_round:

    if Map.undercity_auc_round == 1:
        h1 "Let’s begin with this beautiful item. "
        show hellhound stand behind soul_solvent with slow_dissolve:
            xpos 0.25 ypos 0
            zoom 1
        show black2 with dissolve
        show soul_solvent with q_dissolve:
            xpos 0.3 ypos 0.35
            zoom 1.3
        h1 "A rare Soul Solvent."
        h1 "You should have seen the things this soul did to get this corrupted."
        h1 "If you need a quick pick me up, use a Corrupted Soul Solvent."

        h1 "The starting bid is 5 Bevocr!"




        $ Map.undercity_auc_bid1 = 5
        $ Map.undercity_auc_bid2 = Map.undercity_auc_bid1
        $ Map.undercity_auc_round_small = 1
        $ qty = jane_inv_K.qty(bevocr)
        hide soul_solvent_1 with dissolve



    elif Map.undercity_auc_round == 2:
        hide soul_solvent
        h2 "The next item is this Lava Stone."
        show hellhound stand behind lava_stone with slow_dissolve:
            xpos 0.25 ypos 0
            zoom 1
        show black2 with dissolve
        show lava_stone with q_dissolve:
            xpos 0.3 ypos 0.35
            zoom 1.3
        h2 "Love the heat of the lava flowing through the city?"
        h2 "Don’t want to miss it’s radiant redness at all times?"
        h2 "Then come on and get a Lava Stone."
        h2 "Concentrated demon flames that take on the colour of lava."
        h2 "The starting bid is 10 Bevocr!"




        $ Map.undercity_auc_bid1 = 10
        $ Map.undercity_auc_bid2 = Map.undercity_auc_bid1
        $ Map.undercity_auc_round_small = 1
        $ qty = jane_inv_K.qty(bevocr)
        hide soul_solvent_1 with dissolve
    elif Map.undercity_auc_round == 3:
        hide lava_stone
        h2 "Now here’s a beauty, and a one of a kind treasure."
        show hellhound stand behind hand_bones with slow_dissolve:
            xpos 0.25 ypos 0
            zoom 1
        show black2 with dissolve
        show hand_bones with q_dissolve:
            xpos 0.3 ypos 0.35
            zoom 1.3
        h1 "Murphy’s Hand!"
        h1 "Don’t ask us who Murphy was, but his hand will be very ‘handy’ to anyone who likes to brawl."
        h1 "The starting bid is 20 Bevocr!"




        $ Map.undercity_auc_bid1 = 20
        $ Map.undercity_auc_bid2 = Map.undercity_auc_bid1
        $ Map.undercity_auc_round_small = 1
        $ qty = jane_inv_K.qty(bevocr)
        hide soul_solvent_1 with dissolve
    elif Map.undercity_auc_round == 4:
        hide hand_bones
        h2 "Now here’s a beauty, and a one of a kind treasure."
        show hellhound stand behind soul_emblem with slow_dissolve:
            xpos 0.25 ypos 0
            zoom 1
        h1 "We’re nearing the main event item, but don’t miss out on a once in a lifetime chance to own this."
        show black2 with dissolve
        show soul_emblem with q_dissolve:
            xpos 0.3 ypos 0.35
            zoom 1.3
        "The Hellhound holds out a small stone in his hand, it’s an emblem."
        h1 "A handcrafted emblem of unknown origin."
        h2 "It would look great on any demon’s cloak."
        h2 "Let’s start the bid at 15."




        $ Map.undercity_auc_bid1 = 15
        $ Map.undercity_auc_bid2 = Map.undercity_auc_bid1
        $ Map.undercity_auc_round_small = 1
        $ qty = jane_inv_K.qty(bevocr)
        hide soul_solvent_1 with dissolve
    elif Map.undercity_auc_round == 5:
        hide soul_emblem
        h2 "Here’s the item you’ve all been waiting for."
        h2 "Your chance to own your very own mortal!"
        "A tower of black smoke erupts on the stage."
        show flo hide04 with slow_dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        show hellhound stand at right with slow_dissolve
        "Once the smoke lifts, a young shark sits on his knees. "
        e 5 "(Flo...!)"
        "His hands are shackled and he just stares at the crowd with mouth agape."
        "You see his eyes are red and there are bags underneath them, how long hasn’t he slept?"
        h2 "For this rare beauty, let's start the bidding at 50."
        hide flo hide04 with slow_dissolve
        hide hellhound stand with slow_dissolve




        $ Map.undercity_auc_bid1 = 50
        $ Map.undercity_auc_bid2 = Map.undercity_auc_bid1
        $ Map.undercity_auc_round_small = 1
        $ qty = jane_inv_K.qty(bevocr)
        hide soul_solvent_1 with dissolve
    elif True:
        "You see this mean it's a bug!."
        "Pls report to Caro, thx!"
        return
    label undercity_auction_start_bid0:
        if Map.undercity_auc_round == 1:
            hide soul_solvent with q_dissolve
        elif Map.undercity_auc_round == 2:
            hide lava_stone with q_dissolve
        elif Map.undercity_auc_round == 3:
            hide hand_bones with q_dissolve
        elif Map.undercity_auc_round == 4:
            hide soul_emblem with q_dissolve
        hide hellhound stand at center with dissolve
        hide black2 with q_dissolve
        if Map.undercity_auc_bid2 > jane_inv_K.qty(bevocr):
            e 5 "Damn, I can't afford it anymore."
            jump undercity_auction_start_bid_lose
        show screen undercity_auction_start_bid1
        show screen undercity_auction_start_bid2
        show screen undercity_auction_start_bid3
        show empty_bag:
            xpos 0.32 ypos 0.72
            zoom 1
        if Map.undercity_auc_round == 1:
            show soul_solvent:
                xpos 0.32 ypos 0.72
                zoom 1
        elif Map.undercity_auc_round == 2:
            show lava_stone:
                xpos 0.32 ypos 0.72
                zoom 1
        elif Map.undercity_auc_round == 3:
            show hand_bones:
                xpos 0.32 ypos 0.72
                zoom 1
        elif Map.undercity_auc_round == 4:
            show soul_emblem:
                xpos 0.32 ypos 0.72
                zoom 1

        if Map.undercity_auc_giveup == False:
            label undercity_auction_start_bid01:
                menu:
                    "-1" if True:
                        $ qty = jane_inv_K.qty(bevocr)
                        $ Map.undercity_auc_bid2 = max(Map.undercity_auc_bid1, Map.undercity_auc_bid2-1)
                        jump undercity_auction_start_bid01
                    "-5" if True:
                        $ qty = jane_inv_K.qty(bevocr)
                        $ Map.undercity_auc_bid2 = max(Map.undercity_auc_bid1, Map.undercity_auc_bid2-5)
                        jump undercity_auction_start_bid01
                    "+1" if True:
                        $ qty = jane_inv_K.qty(bevocr)
                        $ Map.undercity_auc_bid2 = min(Map.undercity_auc_bid2+1, jane_inv_K.qty(bevocr))
                        jump undercity_auction_start_bid01
                    "+5" if True:
                        $ qty = jane_inv_K.qty(bevocr)
                        $ Map.undercity_auc_bid2 = min(Map.undercity_auc_bid2+5, jane_inv_K.qty(bevocr))
                        jump undercity_auction_start_bid01
                    "Bid" if Map.undercity_auc_bid1 != Map.undercity_auc_bid2:
                        $ Map.undercity_auc_round_small = Map.undercity_auc_round_small + 1
                        $ qty = jane_inv_K.qty(bevocr)
                        $ Map.undercity_auc_giveup = False

                        hide screen undercity_auction_start_bid1
                        hide screen undercity_auction_start_bid2
                        hide screen undercity_auction_start_bid3
                        $ Random = renpy.random.randint(1, 10)
                        $ Random = renpy.random.randint(1, 3)

                        if Map.undercity_auc_round == 1:
                            hide soul_solvent
                            hide empty_bag

                            show hellhound stand behind soul_solvent with dissolve:
                                xpos 0.25 ypos 0
                                zoom 1
                            show soul_solvent with q_dissolve:
                                xpos 0.3 ypos 0.35
                                zoom 1.3
                        elif Map.undercity_auc_round == 2:
                            hide lave_stone
                            hide empty_bag

                            show hellhound stand behind lava_stone with dissolve:
                                xpos 0.25 ypos 0
                                zoom 1
                            show lava_stone with q_dissolve:
                                xpos 0.3 ypos 0.35
                                zoom 1.3
                        elif Map.undercity_auc_round == 3:
                            hide hand_bones
                            hide empty_bag

                            show hellhound stand behind hand_bones with dissolve:
                                xpos 0.25 ypos 0
                                zoom 1
                            show hand_bones with q_dissolve:
                                xpos 0.3 ypos 0.35
                                zoom 1.3
                        elif Map.undercity_auc_round == 4:
                            hide soul_emblem
                            hide empty_bag

                            show hellhound stand behind soul_emblem with dissolve:
                                xpos 0.25 ypos 0
                                zoom 1
                            show soul_emblem with q_dissolve:
                                xpos 0.3 ypos 0.35
                                zoom 1.3
                        elif True:
                            hide empty_bag
                            show hellhound stand with dissolve:
                                xpos 0.25 ypos 0
                                zoom 1
                        "You raise your hand and make the bid."
                        if Random == 1:
                            h2 "We have [Map.undercity_auc_bid2] Bevocr."
                            h2 "Do I hear a higher bid? "
                        elif Random == 2:
                            h2 "So, that’s [Map.undercity_auc_bid2] Bevocr. "
                            h2 "Anyone interested in competing?"
                            pause 1
                            h2 "Anyone?"
                            pause 1
                            h2 "It’s a rare item, don’t miss this chance."
                            h2 "If there are no bids then the customer wins the item."
                        elif True:
                            h2 "That’s [Map.undercity_auc_bid2] Bevocr."
                            h2 "Surely there are others interested in owning this rare item."
                            h2 "Any higher bids?"
                        h2 "Going once." with vpunch
                        pause 1
                        h2 "Going twice." with vpunch
                        pause 2
                        jump undercity_auction_start_bid
                    "Give up" if Map.undercity_auc_bid1 == Map.undercity_auc_bid2:

                        $ Map.undercity_auc_round_small = 0
                        $ qty = jane_inv_K.qty(bevocr)
                        $ Map.undercity_auc_giveup = True
                        jump undercity_auction_start_bid
        elif True:
            "BUG!"

    screen undercity_auction_start_bid1:
        vbox:
            xalign 0.345
            yalign 0.69
            if Map.undercity_auc_round_small != 0:
                text "{size=-8}Round:[Map.undercity_auc_round_small]{/size}"

    screen undercity_auction_start_bid2:

        vbox:
            xalign 0.45
            yalign 0.8
            text "{size=-4}Current Bid:{/size}"
            text "{size=-4}      Your Bid:{/size}"
            text "{size=-4}          Bevocr:{/size}"
    screen undercity_auction_start_bid3:

        vbox:
            xalign 0.53
            yalign 0.8
            text "{size=-5}  [Map.undercity_auc_bid1]{/size}"
            text "{size=-5}  [Map.undercity_auc_bid2]{/size}"
            text "{size=-5}  [qty]{/size}"

    label undercity_auction_start_bid:
        if Map.undercity_auc_giveup == True:
            jump undercity_auction_start_bid_lose
        label undercity_auction_start_bid111:
            if Map.undercity_auc_round == 1:
                $ Map.undercity_auc_price_0 = Map.undercity_auc_price_1
                if Map.undercity_auc_item_1 == 1:
                    $ Map.undercity_auc_item_0 = 1
                elif True:
                    $ Map.undercity_auc_item_0 = 2
            elif Map.undercity_auc_round == 2:
                $ Map.undercity_auc_price_0 = Map.undercity_auc_price_2
                if Map.undercity_auc_item_2 == 1:
                    $ Map.undercity_auc_item_0 = 1
                elif True:
                    $ Map.undercity_auc_item_0 = 2
            elif Map.undercity_auc_round == 3:
                $ Map.undercity_auc_price_0 = Map.undercity_auc_price_3
                if Map.undercity_auc_item_3 == 1:
                    $ Map.undercity_auc_item_0 = 1
                elif True:
                    $ Map.undercity_auc_item_0 = 2
            elif Map.undercity_auc_round == 4:
                $ Map.undercity_auc_price_0 = Map.undercity_auc_price_4
                if Map.undercity_auc_item_4 == 1:
                    $ Map.undercity_auc_item_0 = 1
                elif True:
                    $ Map.undercity_auc_item_0 = 2
            elif Map.undercity_auc_round == 5:
                $ Map.undercity_auc_price_0 = Map.undercity_auc_price_5
                $ Map.undercity_auc_item_0 = 1
            elif True:
                "bug!"
                return
            if Map.undercity_auc_item_0 == 2:
                if Map.undercity_auc_round_small <= 3:
                    if Map.undercity_auc_bid2 >= Map.undercity_auc_price_0*0.6:
                        jump undercity_auction_start_bid_win
                    elif True:
                        $ Map.undercity_auc_bid2 = renpy.random.randint(Map.undercity_auc_bid2+1, Map.undercity_auc_bid2+5)
                        $ Map.undercity_auc_bid1 = Map.undercity_auc_bid2
                        $ Random = renpy.random.randint(1, 10)
                        $ Random = renpy.random.randint(1, 5)
                        if Random == 1:
                            "A shadow raises its bidding board."
                            h1 "We’ve got a counter bid! [Map.undercity_auc_bid2] Bevocr!"
                            h2 "Will anyone bid higher?"
                        elif Random == 2:
                            "A shadow raises its bidding board."
                            h2 "That’s [Map.undercity_auc_bid2] Bevocr!"
                            h2 "The item is now [Map.undercity_auc_bid2] Bevocr!"
                        elif Random == 3:
                            "A shadow raises its bidding board."
                            h2 "I hear a bigger bid!"
                            h2 "[Map.undercity_auc_bid2] Bevocr!"
                            h2 "Do I hear anything higher?"
                        elif Random == 4:
                            h2 "Wait, someone wants to bid?"
                            "A lady raises her bidding board."
                            h2 "That’s [Map.undercity_auc_bid2] Bevocr!"
                            h1 "You sir are a braver demon than I."
                            h2 "Anyone else want to bid higher?"
                        elif True:
                            h2 "Wait! I see a counter offer from the demon behind."
                            "Demon" "[Map.undercity_auc_bid2] Bevocr."
                            h2 "Yes, do I hear anything higher?"
                            h1 "Going once!"
                        jump undercity_auction_start_bid0
                elif True:
                    if Map.undercity_auc_bid2 >= Map.undercity_auc_price_0*1.5:
                        jump undercity_auction_start_bid_win
                    elif True:
                        $ Map.undercity_auc_bid2 = renpy.random.randint(Map.undercity_auc_bid2+1, Map.undercity_auc_bid2+5)
                        $ Map.undercity_auc_bid1 = Map.undercity_auc_bid2
                        $ Random = renpy.random.randint(1, 10)
                        $ Random = renpy.random.randint(1, 5)
                        if Random == 1:
                            "A shadow raises its bidding board."
                            h1 "We’ve got a counter bid! [Map.undercity_auc_bid2] Bevocr!"
                            h2 "Will anyone bid higher?"
                        elif Random == 2:
                            "A shadow raises its bidding board."
                            h2 "That’s [Map.undercity_auc_bid2] Bevocr!"
                            h2 "The item is now [Map.undercity_auc_bid2] Bevocr!"
                        elif Random == 3:
                            "A shadow raises its bidding board."
                            h2 "I hear a bigger bid!"
                            h2 "[Map.undercity_auc_bid2] Bevocr!"
                            h2 "Do I hear anything higher?"
                        elif Random == 4:
                            h2 "Wait, someone wants to bid?"
                            "A lady raises her bidding board."
                            h2 "That’s [Map.undercity_auc_bid2] Bevocr!"
                            h1 "You sir are a braver demon than I."
                            h2 "Anyone else want to bid higher?"
                        elif True:
                            h2 "Wait! I see a counter offer from the demon behind."
                            "Demon" "[Map.undercity_auc_bid2] Bevocr."
                            h2 "Yes, do I hear anything higher?"
                            h1 "Going once!"
                        jump undercity_auction_start_bid0
            elif True:
                if Map.undercity_auc_bid2 >= Map.undercity_auc_price_0:
                    jump undercity_auction_start_bid_win
                elif True:
                    $ Map.undercity_auc_bid2 = renpy.random.randint(Map.undercity_auc_bid2+1, Map.undercity_auc_bid2+5)
                    $ Map.undercity_auc_bid1 = Map.undercity_auc_bid2
                    $ Random = renpy.random.randint(1, 10)
                    $ Random = renpy.random.randint(1, 5)
                    if Random == 1:
                        "A shadow raises its bidding board."
                        h1 "We’ve got a counter bid! [Map.undercity_auc_bid2] Bevocr!"
                        h2 "Will anyone bid higher?"
                    elif Random == 2:
                        "A shadow raises its bidding board."
                        h2 "That’s [Map.undercity_auc_bid2] Bevocr!"
                        h2 "The item is now [Map.undercity_auc_bid2] Bevocr!"
                    elif Random == 3:
                        "A shadow raises its bidding board."
                        h2 "I hear a bigger bid!"
                        "Do I hear anything higher?"
                    elif Random == 4:
                        h2 "Wait, someone wants to bid?"
                        "A lady raises her bidding board."
                        h1 "You sir are a braver demon than I."
                        h2 "Anyone else want to bid higher?"
                    elif True:
                        h2 "Wait! I see a counter offer from the demon behind."
                        "Demon" "[Map.undercity_auc_bid2] Bevocr."
                        h2 "Yes, do I hear anything higher?"
                        h1 "Going once!"
                    jump undercity_auction_start_bid0
        jump undercity_auction_start_bid0
label undercity_auction_start_bid_win:
    hide screen undercity_auction_start_bid1
    hide screen undercity_auction_start_bid2
    hide screen undercity_auction_start_bid3
    play sound"music/hammer_yes.ogg"
    if Map.undercity_auc_round == 1:
        h1 "The winning bid goes to the wolf in the front row!"
        h2 "You can collect the Corrupted Soul Solvent after the auction."
        h2 "I’ll tell you this solvent is a blast to have, it makes you feel all powerful like you’re on top of the world."
        $ jane_inv_K.drop(bevocr,Map.undercity_auc_bid2)
        $ jane_inv.take(soul_solvent,1)
    elif Map.undercity_auc_round == 2:
        h1 "Do I hear any rival bids?"
        h2 "If there are no more bids, then the Lava Stone goes to the wolf over here! "
        h2 "It will be very handy on those long camping trips, but I hear rumors that some people use it to craft weapons and armour."
        h2 "A very malleable tool I say."
        $ jane_inv_K.drop(bevocr,Map.undercity_auc_bid2)
        $ jane_inv_M.take(lava_stone)
    elif Map.undercity_auc_round == 3:
        h2 "Big money! Big money! Who is going to outmatch this bid?"
        h2 "No one?"
        h2 "Then congratulations, wolf."
        h2 "Pat yourself on the back for a good bid, or rather let Murphy’s Hand do it for you."
        h1 "Just be careful where you aim this thing."
        h2 "It’s a piece of history, and it really gives you the boost in battle."
        h2 "The power it holds is unlike anything you’ll ever see."
        $ jane_inv_K.drop(bevocr,Map.undercity_auc_bid2)
        $ jane_inv_E.take(murphy_hand)
        $ Items.Murphy_Hand = 1

    elif Map.undercity_auc_round == 4:
        h2 "Looks like there are no other bids."
        h1 "Congratulations wolf, you get a one of a kind hand carved emblem."
        h2 "Remember to pick it up after the auction."
        $ jane_inv_K.drop(bevocr,Map.undercity_auc_bid2)
        $ jane_inv_K.take(Soul_emblem)
        $ Items.em =Items.em+1
    elif Map.undercity_auc_round == 5:
        $ jane_inv_K.drop(bevocr,Map.undercity_auc_bid2)
        jump undercity_auction_save_Flo
    elif True:
        "You see this mean bug"
        return

    scene black with dissolve
    pause 3
    scene auction 2 with slow_dissolve
    $ Map.undercity_auc_giveup = False
    $ Map.undercity_auc_round = Map.undercity_auc_round + 1
    jump undercity_auction_start_round
label undercity_auction_start_bid_lose:
    hide screen undercity_auction_start_bid1
    hide screen undercity_auction_start_bid2
    hide screen undercity_auction_start_bid3
    hide soul_solvent
    hide empty_bag
    play sound"music/hammer_yes.ogg"
    if Map.undercity_auc_round == 1:
        hide soul_solvent
        hide empty_bag

        show hellhound stand behind soul_solvent with dissolve:
            xpos 0.25 ypos 0
            zoom 1
        show soul_solvent with q_dissolve:
            xpos 0.3 ypos 0.35
            zoom 1.3
    elif Map.undercity_auc_round == 2:
        hide lave_stone
        hide empty_bag

        show hellhound stand behind lava_stone with dissolve:
            xpos 0.25 ypos 0
            zoom 1
        show lava_stone with q_dissolve:
            xpos 0.3 ypos 0.35
            zoom 1.3
    elif Map.undercity_auc_round == 3:
        hide hand_bones
        hide empty_bag

        show hellhound stand behind hand_bones with dissolve:
            xpos 0.25 ypos 0
            zoom 1
        show hand_bones with q_dissolve:
            xpos 0.3 ypos 0.35
            zoom 1.3
    elif Map.undercity_auc_round == 4:
        hide soul_emblem
        hide empty_bag

        show hellhound stand behind soul_emblem with dissolve:
            xpos 0.25 ypos 0
            zoom 1
        show soul_emblem with q_dissolve:
            xpos 0.3 ypos 0.35
            zoom 1.3
    elif True:
        hide empty_bag
        show hellhound stand with dissolve:
            xpos 0.25 ypos 0
            zoom 1


    if Map.undercity_auc_round == 1:
        show hellhound stand behind soul_solvent with dissolve:
            xpos 0.25 ypos 0
            zoom 1
        show soul_solvent with q_dissolve:
            xpos 0.3 ypos 0.35
            zoom 1.3
        h2 "And the item goes to the handsome demon in the back!"
        hide soul_solvent with q_dissolve
        hide hellhound stand with dissolve
        "The Corrupted Soul Solvent is lost to you forever."
    elif Map.undercity_auc_round == 2:
        h2 "You know what, this item is pretty useful."
        h2 "Maybe I’ll- oh, I see a hand."
        h1 "Any counter offers? No?"
        h1 "Alright you sir, won the bid."
    elif Map.undercity_auc_round == 3:
        h2 "It’s going, going, gone to the highest bidder in the front row!"
        "The Murphy's Hand will serve another master now."

    elif Map.undercity_auc_round == 4:
        h2 "No more bids."
        h2 "The winner is the lady in the red cloak!"
        h2 "Enjoy ma’am. The emblem would look great on you."
    elif Map.undercity_auc_round == 5:
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
        $ renpy.music.set_volume(1, 5, channel = "Chan2")
        play Chan2[ "<silence 0.5>", "music/noisy_people.ogg" ]fadein 1
        h2 "We have the winning bid."
        "The demon in the back can claim the item after the auction."
        "Demon" "Food!"
        h2 "That’s it for our auction."
        hide hellhound stand with slow_dissolve
        play music "music/hammer_stop.ogg"
        $ renpy.music.set_volume(0.5, 5, channel = "Chan2")
        pause 8
        stop music
        h2 "Come back in another century for a new chance to win fabulous prizes."
        e 9 "(No! Flo!)"
        scene auction 1 with slow_dissolve
        "The stage and the hellhound then disappear in a cloud of smoke, but is quickly replaced with a table with the hellhound sitting behind it."
        "They are giving out the prizes."
        "You rush over to the line of demons, pushing through them all to get to the front of the line."
        e 12 "Wait, you can’t give Flo away. I need him back."
        show hellhound stand with slow_dissolve
        h2 "Afraid not, you heard the rules."
        h1 "The demon won the prize fair and square."
        e 9 "I can pay you more, please you can’t do this."
        h1 "We can and we have."
        h2 "You should have saved more money before coming into the auction."
        e 12 "I refuse to accept this! Hand Flo over to me now!"
        h2 "We don't need you to accept this, and quite frankly your rudeness is tiresome."
        h1 "Away with you."
        hide hellhound stand with slow_dissolve
        with flashbulb
        e 5 "Wha——"
        scene black with slow_dissolve
        "With a wave of their hand, dark shackles form on your wrists and ankles."
        "The items tug you upwards into the air."
        e 9 "Wait, no!"
        "Slowly your binds float you away from the table in the direction of the elevator."
        $ renpy.music.set_volume(1, 5, channel = "Chan1")
        "You scream and struggle to break free but nothing works."
        "The hellhound continues giving out the prizes."
        "Then Flo emerges, chained by the neck."
        "He is handed over to one of the demons."
        "You yell Flo's name and for a second he sees you with tears in his eyes."
        "He mouths, 'Save me.' Before he and the demon disappear in the dark smoke."
        e 9 "FLO!"
        "You are chucked at the top of the cliff where the elevator began."
        "You frantically try to run back to the panel to summon the elevator."
        scene undercity 1 with slow_dissolve
        "Maybe just maybe you can still save Flo."
        "But you get no chance to reach the panel."
        "A demon guard appears from thin air and blocks your way."
        "Demon Guard" "Grr... back!"
        e 12 "But-"
        "Demon Guard" "BACK!"
        "The guard pulls out his weapon."
        "Your ears fall and you hide your tail between your legs as you run back."
        "There’s nothing else you can do but run back to Ebb."
        stop Chan2
        $ Map.undercity_auc_start = 2
        $ Flo.meet = -1
        $ Ebb.kidnap = 3
        jump forest_map0
    elif True:

        "You see this mean bug"
        return
    scene black with dissolve
    pause 3
    scene auction 2 with slow_dissolve
    $ Map.undercity_auc_giveup = False
    $ Map.undercity_auc_round = Map.undercity_auc_round + 1
    jump undercity_auction_start_round
label undercity_auction_start_lag:
    "You are too late. The auction should have already begun."
    "From the descending elevator you see a large crowd dispersing from the city hall."
    "Quickly you run to the city hall."
    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    $ renpy.music.set_volume(1, 5, channel = "Chan2")
    play Chan2[ "<silence 0.5>", "music/noisy_people.ogg" ]fadein 1
    "Pushing against the many demons walking in the opposite direction you reach the heart of the crowd."
    scene auction 1 with slow_dissolve
    "The hellhound is sitting behind a table while he shakes the hand of another demon."
    "Your heart sinks, the demon is holding onto Flo’s chain."
    e 9 "Wait!"
    "You don’t even have a chance to reach them."
    "The demon and Flo disappear in a cloud of smoke."
    e 9 "Where are they going? I need to get Flo."
    show hellhound stand with slow_dissolve
    h1 "Sorry my boy, but the auction is over."
    h1 "I summoned every eligible bidder when the auction started, but you weren’t there."
    e 9 "I can pay you double what he paid. Please!"
    h1 "Nope, that is against the rules. Maybe better luck next auction."
    e 12 "No! There is no next auction! I have to save Flo!"
    "You try to run to find the demon that has Flo."
    hide hellhound stand with slow_dissolve
    with flashbulb
    "Snap."
    "Heavy chains materialize around your wrists and ankles, freezing you on the spot."
    "The hellhound reemerges in front of you."
    show hellhound stand with slow_dissolve
    h2 "Woah, woah, woah, if you’re going to cause trouble in our city, think again."
    "You can’t say a word or move any parts of your body."
    h2 "You’re getting a one day banishment."
    h2 "We expect you to better behave when you come back next time."
    "The three heads lean in close towards you."
    hide hellhound stand with slow_dissolve
    h2 "But don’t even think about finding your shark any longer."
    h2 "Thing is demons are very rough with mortals, that’s why they tend to break easily here."
    h2 "Now begone!"
    scene undercity 1 with vslow_dissolve
    "Your whole body is flung into the air at breakneck speed sending you to the entrance where the elevator starts."
    "The binds disappear and you can move again."
    e 12 "Flo!" with vpunch
    "You turn to the elevator but a demon guard blocks your way."
    "Demo Guard" "BACK!"
    "He threatens you with his weapon."
    "There’s nothing more you can do. You’ve failed to save Flo."
    "You drag yourself back from where you came from, it's time to tell Ebb."
    stop Chan2
    $ Map.undercity_auc_start = 2
    $ Flo.meet = -1
    $ Ebb.kidnap = 3
    jump forest_map0



label undercity_auction_save_Flo:
    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    play Chan2[ "<silence 0.5>", "music/noisy_people.ogg" ]fadein 3
    h2 "And the winner is, number 69."
    "You slump back against your seat."
    "Relief feels your lungs, letting you breathe normally again."
    play music "music/hammer_stop.ogg"
    $ renpy.music.set_volume(0.8, 5, channel = "Chan2")
    pause 8
    stop music
    show hellhound stand with slow_dissolve
    h2 "Ladies and gentlemen, the auction has come to an end."
    h2 "Please come to the counter to collect your prizes."
    hide hellhound stand with slow_dissolve
    scene auction 1 with slow_dissolve
    "The hellhound snaps his fingers and the binds on Flo's wrists disappear, but before he can stand up, he is transported along with the entire stage to the far right."
    $ renpy.music.set_volume(1, 5, channel = "Chan2")
    "Now a table appears with the hellhound sitting behind it."
    "The bidders who won things are now lining up."
    "You walk over and join the line."
    "It doesn't take long before you reach the front of the line."
    show hellhound stand with slow_dissolve
    h2 "Congratulations! You know, I’m amazed you had that much to bid. "
    h2 "Well we are demons of our word. The shark is yours."
    h1 "Along with your other prizes."
    show flo hide04 with slow_dissolve:
        xpos -0.1 ypos 0
        xzoom -1
    show hellhound stand at right with slow_dissolve
    "With a snap of their fingers, Flo reappears."
    show flo hide03 with slow_dissolve:
        xpos -0.1 ypos 0
        xzoom -1
    "The shackles on Flo’s wrists melt away and he rushes over to you."
    f "Thank you, thank you stranger. I’m forever in your debt. "
    h2 "One minute before you go."
    hide flo hide03 with dissolve
    show hellhound stand at center with slow_dissolve
    "Flo flinches and rushes behind you."
    "He grabs your right bicep tightly and whispers to you.."
    f "{size=-6}Don’t let him take me.{/size}"
    "You can feel his body trembling against yours."
    h1 "You can’t leave without that shark’s equipment."
    hide hellhound stand with dissolve
    "*snap*"
    "A quick glance behind you and Flo is now dressed."
    show hellhound stand at center with dissolve
    h2 "And don’t forget your receipt. "
    hide hellhound stand with dissolve
    "The hellhound hands you a small piece of paper with the details of your bids."
    show hellhound stand at center with dissolve
    h2 "And here is your warranty card, and you have a three-day return period."
    h2 "If you are not satisfied with the product, you can return it for store credit, this includes the shark over there. "
    "They point to Flo behind you and chuckle."
    e 9 "Ehh, no, I won't be needing this."
    hide hellhound stand with dissolve
    "You tear off the warranty card and receipt and glare angrily at the hellhound."
    show hellhound stand at center with dissolve
    h2 "My, my, something the matter, wolf?"
    e 12 "How do I know you or any of the other demons won’t come after Flo again?"
    "Crossing their arms, the hellhound gives you a smug smile."
    h1 "You need not worry about that, no one has any interests in another’s sloppy seconds."
    e 12 "And what about the rest of us? What’s stopping you all from trying to go after us?"
    h2 "Well we just finished one auction, we are definitely not interested in going for another scavenger hunt for rare items."
    h2 "That said, we can’t speak for the other demons."
    "They chuckle menacingly at you both. "
    e 12 "If any of you come at us when we are up above, I’ll make sure you won’t come back here."
    h2 "Threatening, but we are still honourable hosts, if you ever feel like visiting, please do come again."
    "You roll your eyes at the hellhound."
    h1 "Come now, we cannot understand why you are so upset over what is practically our tradition."
    f "Traditions that involve sacrificing a person are bull crap."
    "Flo comes out of covering before you and speaks with determination at the hellhound."
    h1 "Hmph, such insolence. "
    hide hellhound stand with slow_dissolve
    "Not wanting to risk your chances, you grab Flo by the hand and make haste to get away from the crowd as quick as possible."
    scene black with slow_dissolve
    "You and Flo don’t say a word to each other until you both are inside the elevator and you command it to take you both up."
    stop Chan2 fadeout 3
    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    pause 5
    "..."
    play music "music/rail.ogg"
    scene undercity 1 with slow_dissolve
    "You and Flo don’t say a word to each other until you both are inside the elevator and you command it to take you both up."
    "Flo is the first to break the silence."
    f "Before we go further, not that I don’t appreciate the help."
    f "But, why did you save me, stranger?"
    e 1 "Call me [name]."
    e 1 "As for why I saved you well... your butler Ebb was the one that told me that you were taken."
    f "Damn it, {size=-10}it had to be him.{/size}"
    e 1 "Sorry?"
    "Flo grits his teeth as though you just insulted him."
    "He takes a deep breath and shakes his head."
    f "It’s nothing. This is all a lot to process."
    f "What has been happening outside?"
    f "Did the fog finally stop?"
    e 13 "No, the fog hasn’t changed."
    e 13 "We’re all still trapped here."
    f "Ugh..."
    pause 1
    "The both of you look at each other tiredly. "
    "The look of resignation in Flo’s eyes, you sense that he too wishes for freedom as badly as you."
    "The clinks and clanks of the gears turning comes to a halt."
    "You’ve arrived at the top."
    stop music fadeout 3
    show flo stand01 at center with slow_dissolve
    f "You’re taking me back to that orca aren’t you?"
    e 1 "Yup, he’s worried about you, but I sense you have some gripe about him."
    hide flo stand01 at center with dissolve
    f "I don’t want to talk about it. "
    "You noticed that although the shark is almost too weak to stand, his weak body still exudes a strong emotion."
    "Hate."
    e 1 "Oh... ok."
    e 13 "Alright, then let's just walk back."
    e 13 "Keep your eyes peeled for danger."
    "You and Flo walk back to Ebb."
    $ Map.undercity_auc_start = 2
    $ Flo.meet = 1
    $ Ebb.kidnap = 3
    jump forest_map0

label undercity_eyvind_sell:
    scene black
    "Once it clears, you find yourself stripped of your clothes and items, and you are lying on a very plump red mattress."
    "A single orange glass bulb hangs above just barely illuminating the room."
    show eyvind sell01 with slow_dissolve:
        zoom 0.6905
    "You lie back against the soft cotton bed and spread your legs open in an inviting manner."
    "Then you hear the sound of someone materialising inside the room."
    e 0 "Wh-who is it?"
    "The stranger shushes you."
    "Your gulp and instantly obey."
    "You raise both your legs in the air for the demon to see."
    "His baritone chuckle fills the air."
    "Your face flushes red, but you strangely enjoy pleasing the demon."
    "Then a pair of warm claws rests upon your shoulders."
    "He is standing right on top of you."
    "Your heart races."
    "How you wish the demon’s hands would reach down and massage your chest."
    e 0 "Ah... that feels good."
    "His right hand slides down along your bare chest."
    "As he moves lower, his hanging ball sack inches closer and closer towards your face."
    "The sweaty scent of his body fills your nostrils. It’s intoxicating."
    "As you wish he would come closer, you let out a whimper while the fur on your abs brushes against his warm fingers."
    "Then, you feel his hand clamping around your soft member."
    "At the same time, his sweaty ball sack now presses against your nose and mouth."
    "The sweat from his scrotum is so inviting to your dry lips."
    "He strokes your dick lightly, pressing his thumb against your dickhead."
    "You moan from the touch and feel your toes curl up."
    "His touch is mind numbing."
    "The more the demon strokes, the harder your dick grows to full mass."
    "Your cock stands erect, dribbles of pre starts leaking from the tip."
    e 0 "What the?"
    show eyvind sell02 with slow_dissolve:
        zoom 0.6905
    "One of the demon’s hands reaches for your inner thigh and hoists you upwards into its arms."
    "You feel the demon’s powerful arms lifting you without so much of an effort, as if you weighed less to nothing."
    "His broad shelf like pectorals rests on top of your snout."
    "He smells of coal."
    "Demon" "Grr..."
    "He lands on top of your mattress and his brawny body becomes your new cushion."
    "Kicking your legs in the air you yelp a bit when you land on top of your tail."
    "The demon then grabs you by the armpits and locks you in place."
    "Demon" "Ngh."
    e 0 "Yes..."
    "You scoot your butt to the right until your hole aligns with the base of the demon’s dick."
    "His body oozes power as you cannot break free from his hold, not that you even want to."
    "You feel his face pressed up against your neck, and his warm nose breaths in your scent."
    e 0 "Ngh..."
    "Your whole body is heating up."
    "Then the room fills with the same sound when the demon first appeared."
    "Second Demon" "Hehe...."
    "The third demon licks his lips loudly."
    "Fourth Demon" "As..."
    "The fifth demon doesn’t speak but you hear his lustful moans to your left."
    "With their presence, you feel the room shrink as the demons all circle in around you both."
    "Their body heat makes you sweat."
    "Plop."
    "You roll your eyes upwards and realize someone placed their dick on your forehead."
    "The demon moans loudly."
    e 0 "Wait-"
    with flashbulb
    show eyvind sell03 with slow_dissolve:
        zoom 0.6905
    "Without warning the demon beneath you rams his dick into your ass."
    e 0 "FUCK!" with vpunch

    play Chan2[ "<silence 0.5>", "music/slap01.ogg" ]fadein 3
    play Chan3[ "<silence 0.5>", "music/slap02.ogg" ]fadein 3
    show eyvind sell03 with dissolve:
        zoom 0.6905
    show eyvind sell04 with dissolve:
        zoom 0.6905
    "The club sized member forces its way into your unlubed hole filing you like someone shoved an entire log inside you."
    "Second Demon" "Hurr..."
    "The demon stops pushing in his dick half way through."
    show eyvind sell03 with dissolve:
        zoom 0.6905
    show eyvind sell04 with dissolve:
        zoom 0.6905
    "Your lungs begin to strain as you pant heavily."
    "Through the weak lighting, you watch with a perverse glee that the other demons have their cocks out."
    show eyvind sell03 with q_dissolve:
        zoom 0.6905
    show eyvind sell04 with q_dissolve:
        zoom 0.6905
    "All eyes watch you with great attention while their hands are kept busy stroking their own members. "
    "Third Demon" "Fuck!"
    show eyvind sell03 with q_dissolve:
        zoom 0.6905
    show eyvind sell04 with q_dissolve:
        zoom 0.6905
    "The cock on your head is burning hot drops of its pre leaks down your forehead."
    "Demon" "Not a chance! Damn, your ass is tight pup."
    e 0 "Ngh!"
    "The whole room begins to stink of the combined musk of everyone inside."
    "You are intoxicated by the smell and the feeling of the throbbing cock lodged inside your anus."
    "Demon" "Ragh!"
    show eyvind sell03 with q_dissolve:
        zoom 0.6905
    show eyvind sell04 with q_dissolve:
        zoom 0.6905
    show eyvind sell03 with q_dissolve:
        zoom 0.6905
    show eyvind sell04 with q_dissolve:
        zoom 0.6905
    "The demon that binds your arms starts thrusting his hips."
    "He starts by slowly pulling out his hard manhood part way out of your hole, then slamming his cock back inside you."
    "You roar with ecstasy!"
    "His thick and long cock brushes against your sensitive spot with ease."
    "Hot steam escapes the demon’s nostrils."
    e 0 "Ah...ah...ah!"
    show eyvind sell_dongtu with q_dissolve:
        zoom 0.6905
    "You’re unable to utter a single sensible word."
    "Your brain is clouded by pleasure and desire."
    "The fourth demon roars."
    "One of the demons reaches out to pinch your butt cheeks, making you yelp in surprise."
    "The demon picks up his pace, and rides your ass with increasing vigor. "
    "The rich pre leaking into you helps to ease the pressure of getting fucked to oblivion by the demon's dick."
    "The other demons moan and hiss."
    "Their sentences are merely one worded sounds of excitement."
    "They are all focused on the show before them and the act of pleasuring themselves."
    "The third demon growls pleasurably. "
    "You reply with weak gasps."
    "The group begins to close in on you. "
    "Some even shoot ropes of pre all over your body."
    "Your legs begin to go numb."
    "With your cock throbbing mad you grit your teeth. "
    "Your shaft is red hot ready to burst!"
    e 0 "I’m close!"
    "You then feel your captor’s hold on you tighten. "
    "His thrusts begin to slow, but you can tell he is about to cum too."
    play Chan2[ "<silence 0.5>", "music/slap03.ogg" ]fadein 3
    "Second Demon" "Cum! Cum!"
    "The other demons growl loudly and aim their cocks at you."
    show eyvind sell_dongtu_q with q_dissolve:
        zoom 0.6905
    with flashbulb
    with flashbulb
    show eyvind sell05 with slow_dissolve:
        zoom 0.6905
    stop Chan2 fadeout 1
    stop Chan3 fadeout 1
    "Everyone in the room releases their loads at the same time."
    "Hot cum erupts from the other demon’s cocks, painting your body white."
    "You have to close your eyes when the demon resting his dick on your head unleashes his load."
    "Then the demon fucking inside you fills you with so much cum that a torrent of semen gushes from your ass while he continues to unload inside you."
    "All you can feel is the heat of their lust bathing over you both on the inside and outside."
    "Your body shudders from the overwhelming burst of milky pleasure inside your anus."
    "Your nose is stuffed with the smell of cum and sweat now."
    show eyvind sell06 with slow_dissolve:
        zoom 0.6905
    "The demon inside you pulls his dick out and slaps your taint with a wet slap."
    "Your hole is still twitching weakly."
    "Through cum covered eyes, you can see the other demons backing away and cleaning their dicks."
    "You feel your body shifting around, the demons’ cocks are hard as rock again."
    e 0 "Guys-"
    hide eyvind sell06 with slow_dissolve
    "You are interrupted by a large wisp of smoke covering your entire body."
    "As you disappear you hear the demons angrily shouting incoherently."
    e 0 "Wo-woah!"
    jump undercity_eyvind_sell_end

image eyvind sell_dongtu:




    "images/eyvind sell03.png" with dissolve
    pause 1
    "images/eyvind sell04.png" with dissolve
    pause 1
    repeat
image eyvind sell_dongtu_q:




    "images/eyvind sell03.png" with q_dissolve
    pause 0.2
    "images/eyvind sell035.png" with q_dissolve
    pause 0.2
    "images/eyvind sell04.png" with q_dissolve
    pause 0.2
    "images/eyvind sell035.png" with q_dissolve
    pause 0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
