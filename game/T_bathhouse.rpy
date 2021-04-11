label T_bathhouse0:
    if Map.bathroom == "EbbFlo":
        $ Bath_npc = renpy.random.randint(1, 2)
        $ Bath_npc = renpy.random.randint(1, 2)

    jump T_bathhouse

label T_bathhouse:
    if Witer.bathsex == 2 or Witer.bathsex == 3:
        jump bathhouse_witer_bath_together_after
    $ renpy.music.set_pause(True, channel='Ebb')
    $ renpy.music.set_pause(True, channel='Flo')
    $ renpy.music.set_volume(0, 0.1, channel = "Ebb")
    $ renpy.music.set_volume(0, 0.1, channel = "Flo")
    $ renpy.music.set_pause(True, channel='Ebb')
    $ renpy.music.set_pause(True, channel='Flo')
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    elif True:

        pass
    window hide None
    stop music fadeout 1
    if Time.hours >= 6 and Time.hours <= 17:
        scene bathroom 1 with dissolve
    elif True:
        scene bathroom 1n with dissolve


    call screen bathhouse_bar with dissolve
    window show None
    show screen days
    stop music fadeout 1

    if _return == 'lockerroom':
        e 6 "Well, I should pay first before entering."
        jump T_bathhouse
        return

    return

label bathhouse_coinbox:
    if Map.first_bath == 0:
        "There’s a note on the counter."
        "{u}{i}If this is the first time you’re using the bath today, then it’s free. Same rules apply if you have a friend with you. "
        "{u}{i}If this isn’t your first time today, pay the fee of 100 coins if you’re here alone."
        "{u}{i}Or 200 coins if you’re with a friend."
        "{u}{i}Just leave the money in the box."
        "{u}{i}XOXO Chet"
    elif True:
        pass
    menu:
        "Use the bath alone (Free)" if Map.free_bathday <= Time.days:
            "You write your name inside the guest book, and head into the locker room."
            $ Map.free_bathday = Time.days +1
            jump bathhouse_bath_alone
        "Use the bath alone (100 coins)" if Map.free_bathday > Time.days:
            if jane_inv.qty(coin) >=100:
                "You write your name inside the guest book and drop the 100 coins needed inside the metal box."
                "After which you head over to the locker room."
                $ jane_inv.drop(coin,100)
                jump bathhouse_bath_alone
            elif True:
                e 6 "(Nah,I don't have the money.)"
                jump bathhouse_coinbox
        "Invite someone to bath together(200 coins)" if True:

            menu:
                "Hakan" if Hakan.quest >= 10:
                    if jane_inv.qty(coin) >=200:
                        $ jane_inv.drop(coin,200)
                        "You write down both you and your companion’s name inside the guest book."
                        "You place 200 coins inside the metal box."
                        jump bathhouse_hakan_sauna
                    elif True:
                        e 6 "(Nah,I don't have the money.)"
                        jump bathhouse_coinbox
                "Witer" if Witer.squat >= 4 and Witer.sleep >= 7:
                    if jane_inv.qty(coin) >=200:
                        $ jane_inv.drop(coin,200)
                        "You write down both you and your companion’s name inside the guest book."
                        "You place 200 coins inside the metal box."
                        jump bathhouse_witer_bath_together
                    elif True:
                        e 6 "(Nah,I don't have the money.)"
                        jump bathhouse_coinbox
                "Leave" if True:

                    jump bathhouse_coinbox
        "Leave" if True:
            jump T_bathhouse


label bathhouse_ebbtalk:
    $ renpy.music.set_volume(0, 0.5, channel = "music")
    pause 0.5
    $ renpy.music.set_pause(True, channel='music')

    $ renpy.music.set_pause(False, channel='Ebb')
    $ renpy.music.set_volume(1, 4, channel = "Ebb")

    show ebb stand_b at center with slow_dissolve
    eb "Welcome to the bath house, Master [name]."
    if Map.bathroom_ebbfirst == 0:
        e 5 "Wow, nice clothes Ebb."
        eb "Thank you, Master [name]."
    label bathhouse_ebbtalk1:
        menu:
            "Use the bath alone (Free)" if Map.free_bathday <= Time.days:

                e 1 "Just me for now."
                eb "Then just sign in here, and you may head in."
                eb "Leave your belongings in the locker room, then you may use the bath first, followed by the sauna."



                $ Map.free_bathday = Time.days +1
                jump bathhouse_bath_alone
            "Use the bath alone (100 coins)" if Map.free_bathday > Time.days:
                if jane_inv.qty(coin) >=100:
                    "You pay 100 coins. "
                    eb "Then just sign in here, and you may head in."
                    eb "Leave your belongings in the locker room, then you may use the bath first, followed by the sauna."
                    $ jane_inv.drop(coin,100)
                    jump bathhouse_bath_alone
                elif True:
                    e 6 "(Nah,I don't have the money.)"
                    jump bathhouse_ebbtalk1
            "Invite someone to bath together(200 coins)" if True:

                e 6 "I’ll invite a friend."
                eb "Excellent, just write their name in the guest book too, I’ll let them know that you invited them."
                eb "Who will you be joining you today?"
                menu:
                    "Hakan" if Hakan.quest >= 10:
                        if jane_inv.qty(coin) >=200:
                            $ jane_inv.drop(coin,200)
                            eb "That will be 200 coins."
                            "You pay the fee and enter the locker room."
                            jump bathhouse_hakan_sauna
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump bathhouse_ebbtalk1
                    "Witer" if Witer.squat >= 4 and Witer.sleep >= 7:
                        if jane_inv.qty(coin) >=200:
                            $ jane_inv.drop(coin,200)
                            eb "That will be 200 coins."
                            "You pay the fee and enter the locker room."
                            jump bathhouse_witer_bath_together
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump bathhouse_ebbtalk1
                    "Leave" if True:

                        jump bathhouse_ebbtalk1
            "Find some topics to chat" if True:

                label Ebb_chattree:
                    menu:
                        "Ask about Ebb’s new clothes" if True:
                            e 1 "Where did you get those new clothes?"
                            eb "These? These aren’t new. I brought them from home."
                            eb "Consider it my formal work clothes."
                            e 6 "They look so elegant and regal."
                            e 6 "I wouldn’t mind having a set of clothes like that."
                            eb "Thank you Master [name] I think you would look great in our traditional clothes too."
                            eb "Does your tribe have any special clothes?"
                            e 1 "Not that I am aware of."
                            e 1 "Our clothing choices are usually pretty limited."
                            e 6 "As long as it doesn’t restrict our movements we will wear them."
                            eb "Indeed comfort and movement is important."
                            eb "I refuse to wear anything that will impede my ability to work."
                            e 1 "Oh? Why not go full on naked then?"
                            eb "That would save me time when I start work."
                            e 5 "No Ebb, I was joking. Don’t take it so seriously."
                            eb "A joke, of course. Apologies Master [name]."
                            jump Ebb_chattree
                        "Ebb and Flo’s place of origin" if True:
                            e 1 "Where are you guys really from?"
                            e 1 "I don’t recognize the decor in the bath house, nor your clothes."
                            eb "We hail from the west."
                            eb "More specifically we are from a fishing village."
                            e 1 "The west? That's like a whole new world."
                            e 1 "I've never even seen most of this kingdom. Tell me more about your country."
                            eb "Well the weather is more tropical than here."
                            eb "We don't get much fog since it is usually sunny or rainy."
                            eb "What else is there to say?"
                            eb "Ever since our kingdom opened its ports to the world we've been trading our spices and minerals with other kingdoms."
                            eb "So much of the culture from other kingdoms such as the clothing and lingo has seeped into ours. "
                            e 1 "Huh, is that suit of yours something that has catched on in your kingdom?"
                            eb "Oh that, no I bought that when I first arrived here. To better blend in with the crowd."
                            e 1 "Clever."
                            jump Ebb_chattree
                        "Ebb’s work with Flo" if True:
                            e 1 "If you don’t mind me asking, how’d you end up working for Flo?"
                            eb "It’s not so much work, but the honour of those in my family to work for young Master Flo’s family."
                            eb "My family serves the Yuf family ever since they established the fishing village back in the homeland."
                            eb "It is the responsibility of my family to take care of the head of the Yuf family."
                            eb "Since I was a teen I was given the task of protecting and serving Young Master Flo and his family."
                            e 1 "Does the job pay well?"
                            eb "I get paid enough, and I have my own place and personal belongings."
                            eb "The Yuf family understands the need for their servant to be in tip top shape, to reflect their prosperity and their standing with the God of the Sea."
                            e 1 "God of the Sea?"
                            eb "Ah, that’s just something our people believe in. "
                            e 1 "Ok, thanks for sharing."
                            jump Ebb_chattree
                        "Ebb’s relationship with Flo" if True:
                            e 1 "I know this might sound rude, but it doesn’t look like Flo likes you very much."
                            eb "Hmm…"
                            e 1 "I know you said before it was because he just got back from being kidnapped, but… he doesn’t even call you by name."
                            eb "It’s complicated."
                            eb "My relationship with Young Master Flo… it’s marred by unfortunate events."
                            eb "Let’s leave it at that for now."
                            e 1 "I understand Ebb."
                            jump Ebb_chattree
                        "Leave" if True:
                            jump bathhouse_ebbtalk1
            "Leave" if True:
                e 1 "I gotta go. Mind if we pick this up some other time?"
                eb "Anytime, Master [name]."
                hide ebb stand_b at center with dissolve
                jump T_bathhouse



label bathhouse_flotalk:
    $ renpy.music.set_volume(0, 0.5, channel = "music")
    pause 0.5
    $ renpy.music.set_pause(True, channel='music')

    $ renpy.music.set_pause(False, channel='Flo')
    $ renpy.music.set_volume(1, 4, channel = "Flo")


    show flo stand at center with slow_dissolve
    f "Hey there [name], here for a bath?"
    if Map.free_bathday <= Time.days:
        f "Looks like you haven’t used your daily free bath yet."
    f "How about it, want to use the bath on your own or with a friend?"

    label bathhouse_flotalk1:
        menu:
            "Use the bath alone (Free)" if Map.free_bathday <= Time.days:

                e 1 "Just me for now Flo."
                f "Alright, just sign your name in here first."
                $ Map.free_bathday = Time.days +1
                jump bathhouse_bath_alone
            "Use the bath alone (100 coins)" if Map.free_bathday > Time.days:
                if jane_inv.qty(coin) >=100:
                    "You pay 100 coins."
                    f "Alright, just sign your name in here first."
                    $ jane_inv.drop(coin,100)
                    jump bathhouse_bath_alone
                elif True:
                    e 6 "(Nah,I don't have the money.)"
                    jump bathhouse_flotalk1
            "Invite someone to bath together(200 coins)" if True:

                e 6 "I would like to invite a friend."
                f "Sure, no problem."
                f "Who am I looking out for exactly?"
                menu:
                    "Hakan" if Hakan.quest >= 10:
                        if jane_inv.qty(coin) >=200:
                            $ jane_inv.drop(coin,200)
                            f "I’ll let him know that you’re already inside when he gets here."
                            f "That will be 200 coins."
                            "You pay the fee of 200 coins and step into the locker room."
                            jump bathhouse_hakan_sauna
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump bathhouse_flotalk1
                    "Witer" if Witer.squat >= 4 and Witer.sleep >= 7:
                        if jane_inv.qty(coin) >=200:
                            $ jane_inv.drop(coin,200)
                            f "I’ll let him know that you’re already inside when he gets here."
                            f "That will be 200 coins."
                            "You pay the fee of 200 coins and step into the locker room."
                            jump bathhouse_witer_bath_together
                        elif True:
                            e 6 "(Nah,I don't have the money.)"
                            jump bathhouse_flotalk1
                    "Leave" if True:

                        jump bathhouse_flotalk1
            "Find some topics to chat" if True:

                label Flo_chattree:
                    menu:
                        "Where Flo came from" if True:
                            show flo stand at center
                            e 1 "Well where are you from?"
                            f "I hail from the magical kingdom of Deval."
                            f "Where every street is made of gold, and everyone can fly."
                            e 5 "Really? That's amazing!"
                            show flo happy at center with dissolve
                            f "Err, no I was just joking."
                            e 8 "Oh…"
                            "Your ears droop when you find out there are no flying people."
                            show flo stand at center with dissolve
                            f "There's not much to say about where I'm from."
                            f "It is just a fishing village from the west."
                            e 1 "Still, you have a butler that follows you around."
                            e 6 "Not every family has that."
                            show flo stand01 at center with dissolve
                            f "Personally, I wish he wasn't around."
                            "Flo sighs defeated."
                            jump Flo_chattree
                        "Reason Flo is here" if True:
                            show flo stand at center
                            e 1 "Why are you all the way here?"
                            f "Would you believe me if I say it was to get away from that orca?"
                            "You half expect Flo to say it is a joke but he remains stoically silent."
                            e 1 "What… what errr is so bad about Ebb?"
                            show flo stand01 at center with dissolve
                            f "You don't need to know. It's personal."
                            jump Flo_chattree
                            e 1 "Ok."
                            "You nod your head submissively."
                            jump Flo_chattree
                        "Flo relationship with Ebb" if True:
                            show flo stand at center
                            e 1 "I know this isn’t my place to comment, but you don’t seem to like Ebb that much."
                            f "I never tried to hide it."
                            e 1 "Why don’t you call him by name?"
                            show flo stand01 at center with dissolve
                            f "{size=-12}He is a thief."
                            e 9 "What?"
                            f "Let’s just drop it. I shouldn’t have said anything."
                            e 1 "Flo…"
                            show flo stand at center with dissolve
                            f "It’s ok, just there’s nothing to say about that orca right now."
                            "You wish to find out more, but now isn’t the time."
                            jump Flo_chattree
                        "Leave" if True:
                            jump bathhouse_flotalk1
            "Leave" if True:
                e 1 "I think that’s it for now. I’ll talk to you later."
                f "You know where to find me."
                hide flo stand at center with dissolve
                hide flo stand01 at center with dissolve
                jump T_bathhouse


label bathhouse_bath_alone:
    $ renpy.music.set_pause(True, channel='Ebb')
    $ renpy.music.set_pause(True, channel='Flo')
    $ renpy.music.set_volume(0, 0.1, channel = "Ebb")
    $ renpy.music.set_volume(0, 0.1, channel = "Flo")

    if Map.bathroom == "None":
        if Map.first_bath == 1:
            "Do you want to skip the scene?"
            menu:
                "Yes" if True:
                    "You take a pleasant shower and soak in the hot spring."
                    "After a trip to the sauna you are fully rejuvenated."
                    "Invigorated by the trip to the bath house, your HP temporarily increases to X."
                    jump bathhouse_bath_alone_end
                "No" if True:
                    pass
        elif True:
            $ Map.first_bath = 1
    elif True:

        if Map.bathroom_flofirst == 0 and Bath_npc == 2:
            $ Map.bathroom_flofirst = 1
            f "You can keep your stuff in the locker room."
            f "Then feel free to enjoy the hot spring and sauna. "
            f "As part of hot spring etiquette you’re encouraged to take a shower before entering the hot spring and after the sauna."
            e 1 "Gotcha, are you going to join me?"
            "Flo laughs heartily."
            f "Sorry man, I’m on the clock."
            e 6 "Right, see you later then."
            hide flo stand with dissolve
        if Map.bathroom_ebbfirst == 0 and Bath_npc == 2:
            $ Map.bathroom_ebbfirst = 1
            "After you sign the guest book Ebb hands you a towel and guides you to the locker room."
            eb "As per the rules you may only bring in the towel while in this area."
            e 1 "Ok, what else I should know about the customs of this bath house?"
            eb "Well an important thing to remember is to shower before entering the hot spring, and after using the sauna."
            eb "This is to help keep the hot spring clean for other users."
            eb "You can find the showers right through the locker room."
            eb "I’ll be here if you need anything."
            e 6 "Thanks Ebb."
            "Ebb bows humbly and holds his hand out towards the door to the left, signaling to you to enter."
            hide ebb stand_b with dissolve
        elif True:
            "Do you want to skip the scene?"
            menu:
                "Yes" if True:
                    jump bathhouse_bath_alone_end
                "No" if True:
                    pass

    scene black with dissolve
    pause 2
    scene locker room with slow_dissolve
    "You walk over to the other room, the fresh smell of soap and shampoo is pleasantly inviting."
    "After stripping off your clothes and equipment, you head to the shower room to clean yourself."
    scene black with slow_dissolve
    "The soapy smell is stronger in here as you find each shower stall has its own handmade soap in the shape of a seashell, and a small cup of a floral smelling liquid."
    "Once you’re done lathering yourself up with it, you pull on the lever that tips the bucket of water hanging above you. "
    "The rush of lukewarm water against your fur feels invigorating."
    "You repeat the scrubbing and washing of your fur several more times until you’re satisfied with the cleanliness of it all."
    "A quick dry up later and you enter the hot spring area."
    scene hotspring with slow_dissolve
    "The air in the room is warm from the spring waters, but the stone floors themselves are cold. "
    "A cool chill spreads up your spine the moment you step into the room, it causes your fur to stand on end for a second."
    "You test the water by dipping your left foot into the bath. "
    e 9 "Hot!"
    play sound "music/wave.ogg"
    "The concentrated heat on the tip of your toe forces you to pull your foot back."
    "You then try again but this time you dip your whole foot in before immersing your whole body inside the hot spring."
    e 3 "Hssssss. That feels so good."
    "The searing heat becomes a gentle tingle as the warm spring water embraces your naked form."
    e 0 "Ah! So warm."
    "You lean back against the pool and just soak up the ambience."
    "You take your time to indulge in the spring waters, even giving yourself a nice foot rub as well."
    "…"
    "…"
    stop sound
    "Satisfied, you come out of the hot spring and head for the sauna."
    scene sauna with slow_dissolve
    "The sauna is a comfortably large room."
    "In the middle are the sauna rocks you helped to collect, and a bucket of water."
    "You pour a ladle full of water over the stones and enjoy the comforting steam."
    "For the first time in a long time, it doesn’t feel too bad to sweat and enjoy the peace."
    "Following the sauna, you take another shower. "
    "You then head back to the counter once you’ve put on your clothes and gear. "
    scene black with slow_dissolve

    label bathhouse_bath_alone_end:
        if Map.bathroom == "EbbFlo" and Bath_npc == 2:
            "Feeling well rested, your trip to the bath house ends with Flo giving you a cold dessert."
            "It’s a green jelly that has the faint bitterness of tea."
        if Map.bathroom == "EbbFlo" and Bath_npc == 1:
            "Feeling well rested, your trip to the bath house ends with Ebb giving you a nice cold drink of beer."
        if Map.bathroom == "None":
            "There are a few clean mugs lined up behind the counter. "
            "You grab one and fill it with beer from the keg kept below."
            "In less than a minute, the whole mug of cold beer is down your throat."
            e 13 "Ah, refreshing."
            "You place the mug in the bucket designated for used mugs."
            "Ready to continue on your adventure, you leave the bath house."
        jump bathhouse_bath_end

    label bathhouse_bath_end:
        if Map.bathroom == "EbbFlo" and Bath_npc == 2:
            "{color=#19c22a}Invigorated by the trip to the bath house completely restores you HP and MP."
            "{color=#19c22a}Your MP also temporarily increases by 1.8 times."
            $ Zalt.hp = Zalt.maxhp
            $ Zalt.mp = int(Zalt.maxmp*1.8)
        if Map.bathroom == "EbbFlo" and Bath_npc == 1:
            "{color=#19c22a}Invigorated by the trip to the bath house completely restores you HP and MP."
            "{color=#19c22a}Your HP also temporarily increases by 1.8 times."
            $ Zalt.mp = Zalt.maxmp
            $ Zalt.hp = int(Zalt.maxhp*1.8)
        if Map.bathroom == "None":
            "{color=#19c22a}Invigorated by the trip to the bath house completely restores you HP and MP."
            "{color=#19c22a}Your HP and MP also temporarily increases by 1.5 times."
            $ Zalt.hp = int(Zalt.maxhp*1.5)
            $ Zalt.mp = int(Zalt.maxmp*1.5)
        jump T_bathhouse

screen bathhouse_bar:

    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'bathhouse ground'
            hover 'bathhouse hover'

            vbox:
                xalign 0.69 ypos 0.455
                if Map.bathroom == "None":
                    imagebutton:
                        idle "NPC/coin_box01.png"
                        hover "NPC/coin_box02.png"

                        action Jump("bathhouse_coinbox")
                else:
                    pass

            vbox:
                xalign 0.72 ypos 0.3645
                if Map.bathroom == "EbbFlo" and Bath_npc == 1:
                    imagebutton:
                        idle "NPC/ebb_01.png"
                        hover "NPC/ebb_02.png"

                        action Jump("bathhouse_ebbtalk")
                else:
                    pass

            vbox:
                xalign 0.72 ypos 0.433
                if Map.bathroom == "EbbFlo" and Bath_npc == 2:
                    imagebutton:
                        idle "NPC/flo_01.png"
                        hover "NPC/flo_02.png"

                        action Jump("bathhouse_flotalk")
                else:
                    pass
        else:
            idle 'bathhouse groundn'
            hover 'bathhouse hovern'

            vbox:
                xalign 0.69 ypos 0.455
                if Map.bathroom == "None":
                    imagebutton:
                        idle "NPC/coin_box01n.png"
                        hover "NPC/coin_box02n.png"

                        action Jump("bathhouse_coinbox")
                else:
                    pass

            vbox:
                xalign 0.72 ypos 0.3645
                if Map.bathroom == "EbbFlo" and Bath_npc == 1:
                    imagebutton:
                        idle "NPC/ebb_01n.png"
                        hover "NPC/ebb_02n.png"

                        action Jump("bathhouse_ebbtalk")
                else:
                    pass

            vbox:
                xalign 0.72 ypos 0.433
                if Map.bathroom == "EbbFlo" and Bath_npc == 2:
                    imagebutton:
                        idle "NPC/flo_01n.png"
                        hover "NPC/flo_02n.png"

                        action Jump("bathhouse_flotalk")
                else:
                    pass





















        hotspot (1009, 376, 171, 346) action Return("lockerroom")
    frame:
        xalign 0.81 ypos 0.84
        imagebutton:
            idle "UI/outdoor01.png"
            hover "UI/outdoor02.png"

            action Jump("T_outdoor")

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








label Snow_bathroom_questline:
    if Map.bathroom_0 == 1:
        $ Map.bathroom_0 = 2
        if Map.bathroom == "EbbFlo":
            e 1 "How are things going with the bath house renovation?"
            s "Last I checked those two have already started renovating the place based on my layout plans."
            s "But now that you’ve mentioned it, I should probably see if they need any help."
            e 1 "Let me come with, they might need some help."
            s "Alright, come on."
            hide snow stand at center with dissolve
            play sound "music/foot1.ogg"
            if Time.hours >= 6 and Time.hours <= 17:
                scene outdoor 1 with slow_dissolve
            elif True:
                scene outdoor 1n with slow_dissolve
            $ renpy.music.set_volume(0,0.5, channel = "Snow")
            $ renpy.music.set_volume(0,0.5, channel = "Hakan")
            $ renpy.music.set_volume(0,0.5, channel = "Witer")
            $ renpy.music.set_volume(0,0.5, channel = "Chet")
            $ renpy.music.set_volume(0,0.5, channel = "Thane")
            pause 0.5
            $ renpy.music.set_pause(True, channel='Witer')
            $ renpy.music.set_pause(True, channel='Hakan')
            $ renpy.music.set_pause(True, channel='Snow')
            $ renpy.music.set_pause(True, channel='Chet')
            $ renpy.music.set_pause(True, channel='Thane')
            $ renpy.music.set_pause(True, channel='music')
            "Just outside of the bath house Flo and Ebb are in the middle of a heated discussion."
            f "{size=+8}When will you get it through your thick head?{/size}" with vpunch
            f "{size=+8}I can handle serving the customers on my own. You just man the counter.{/size}"
            eb "Young Master I am just trying to make your life easier. It’s backbreaking work handling the guests."
            f "And you think it’s smart to leave the counter unmanned? "
            eb "But- Oh, Master Snow and Master [name]."
            show snow stand at left with slow_dissolve
            show flo stand01 with dissolve:
                xpos 0.3 ypos 0
            show ebb stand with dissolve:
                xpos 0.55 ypos 0
            "The duo end their conversation upon noticing you and Snow’s presence. "
            e 6 "Hey you two."
            s "How goes the renovation?"
            eb "The renovation is progressing smoothly."
            eb "Hakan has been helping us with the heavy lifting."
            e 1 "That’s pretty nice of him."
            show flo stand with dissolve:
                xpos 0.3 ypos 0
            f "He only offered to help after I promised him half a dozen free beers at the end of the day."
            e 8 "Wha! That’s a lot."
            f "I have the gold to spare, plus he’s a hard worker."
            show snow laugh1 with dissolve
            s "That’s good to hear, that means we’ll have this place running in no time."
            show flo stand01 with dissolve:
                xpos 0.2 ypos 0
                xzoom -1
            "Flo crosses his arms and turns his head to Ebb."
            f "It would go a lot faster if you let me help out more."
            f "How many times am I supposed to be building this counter?"
            eb "Young Master, you need not trouble yourself with such demeaning work."
            f "Hey, I can help ok." with vpunch
            f "You don’t need to babysit me all the time. This is the hut all over again."
            show snow stand with dissolve
            s "Ehem!"
            show flo stand01 with dissolve:
                xpos 0.3 ypos 0
                xzoom 1
            "The duo remember that there are others around them."
            f "Sorry, didn’t mean to go off topic."
            s "Is there anything else that you two need?"
            show flo stand with dissolve:
                xpos 0.3 ypos 0
            f "Well now that you’ve mentioned it, we could use some help getting some rocks for the sauna."
            e 1 "Why rocks?"
            f "The right rocks can help to produce heat in the sauna."
            f "If you pour water on them, they can even give out steam. "
            e 1 "Alright, I can find them."
            e 1 "How many do you need?"
            show flo stand01 with dissolve:
                xpos 0.3 ypos 0
                xzoom 1
            f "Orca, tell him."
            eb "About 20 will do for now. "
            e 9 "That many?"
            eb "Only the highest quality rocks can be used for the sauna."
            eb "We need something dense and non-porous. Kind of like this."
            "He shows you a rock."
            e 1 "I recognize that."
            eb "Good, then just bring 20 of these rocks to us. "
            s "I’ll pay you for the job [name]."
            show flo stand with dissolve:
                xpos 0.3 ypos 0
                xzoom 1
            f "Nonsense, Mr. Snow, you put me and Ebb in charge of how the bath house is run."
            f "It’s on us to compensate for any work we ask of others."
            show snow stand1 with dissolve
            s "Well done, I won’t say no to saving some coins."
            e 1 "Sounds good. "
            f "Good luck man, if you need anything just come and ask."
            f "We will wait for you at the entrance of the bathhouse."
            hide ebb stand
            hide snow stand1
            hide flo stand
            jump T_outdoor
        elif True:
            e 1 "Snow, you mentioned that Witer found a hot spring last time and was working on renovating the bath house."
            e 1 "How’s that going?"
            s "Last time I spoke to Witer, he was just negotiating with Chet on the materials to decorate the bath house. "
            s "Now that you’ve brought it up, I should check up on how they’re doing."
            s "Witer, Chet. Up front."
            "They both approach the bar counter."
            show snow stand at left with slow_dissolve
            show chet happy with dissolve:
                xpos 0.4 ypos 0.124
            show witer stand with dissolve:
                xpos 0.55 ypos 0.03
            c "What’s up chief?"
            s "Just checking in, how are things with the bath house renovation?"
            show chet stand with dissolve:
                xpos 0.4 ypos 0.124
            w "Well Chet has been a dear renting out the materials to renovate the bath house based on the design I described."
            w "I had a customer once that always invited me over to this sex spa."
            e 9 "{size=-13}A sex spa?"
            w "Yeah, beautiful place,you’d believe you’re in another country when you enter it."
            w "So I am renovating the place as close as I possibly can to make it look and function like that."
            e 9 "{size=-3}A sex spa!"
            show chet happy with dissolve:
                xpos 0.4 ypos 0.124
            c "I love it!"
            c "The more stuff bubble butt here orders, the more I get to charge for rent."
            c "The Water Gem is running fine, so the showers should work."
            w "Indeed, we tested it ourselves."
            s "What do you mean by, together?"
            show chet stand with dissolve:
                xpos 0.4 ypos 0.124
            c "No, not even close Snow, it was just a pleasant shower-individually, but we don’t have the sauna up and running yet."
            w "We need some sauna rocks, lots of it."
            show snow happy1 with dissolve
            s "How many exactly?"
            w "Maybe 20, just to be safe."
            s "Well you heard the waiter, help them out with the rocks."
            e 3 "{size=+5}For the sex spa!"
            "The surprise in your voice every time you bring up the fact that they are building a sex spa goes unnoticed by the rest."
            show chet happy with dissolve:
                xpos 0.4 ypos 0.124
            w "I don’t see why you’re so surprised by it. It was Snow’s idea."
            "You shoot the tavern master a dirty look."
            show snow stand at left with dissolve
            "Snow scratches the back of his head with his hooked hand and gives you a goofy grin."
            s "Now, no one is telling you how to use the spa. Besides,"
            s "I know you protest now, but deep down you are going to be in that spa most of all, what with all your “friends”."
            e 10 "I..."
            e 10 "(Damn it, this horny old man knows me too well.)"
            "You turn to Witer to dodge answering Snow."
            e 6 "I will get the rocks. "
            w "Great, just talk to me when you're done collecting them."
            w "They look like these."
            "Witer shows a simple looking rock, it resembles most rocks that ghosts would possess from time to time. "
            w "Until you're done, we'll continue testing and making sure the rest of the bath house is working."
            s "Alright, let's move people."
            "The short meeting ends."
            hide chet happy
            hide snow stand
            hide witer stand
            jump map1


    elif Map.bathroom_0 == 2:
        if Map.bathroom == "EbbFlo":
            show ebb stand at center with dissolve
            eb "We can’t get the sauna going without the sauna rocks."
            eb "Bring back 20 of those rocks, and we can start business."
            if jane_inv_M.qty(rock) >= 20:
                "Do you want to give them the rocks?"
                menu:
                    "Yes" if True:
                        e 1 "Here you go, 20 rocks."
                        eb "Excellent."
                        "<You get 400 coins.>"
                        "The orca places the rocks into a bucket."
                        eb "I’ll check and test them with the sauna later."
                        e 1 "Sounds good, where’s Flo by the way?"
                        eb "As per the Young Master’s request for more responsibilities."
                        eb "I had him go broker a deal with Master Chet for materials to decorate the interior of the bath house."
                        e 6 "Ok, maybe I’ll catch him on the way there."
                        "Ebb nods politely at you."
                        e 1 "How long do you think it’ll take before the bath house is up and running?"
                        eb "I predict it will take one more days."
                        e 1 "One more days, sounds good."
                        e 1 "WIll you guys need anymore help?"
                        eb "I think we have it covered from here Master "
                        e 1 "Catch you later then."
                        $ jane_inv_M.drop(rock,20)
                        $ jane_inv.take(coin,400)
                        $ Map.bathroom_openday = Time.days+1
                        $ Map.bathroom_0 = 3
                        jump T_outdoor
                    "No" if True:
                        e 6 "On it."
                        jump T_outdoor
            elif True:
                e 6 "On it."
                jump T_outdoor
        elif True:
            w "Remember we need 20 rocks for the bath house sauna."
            if jane_inv_M.qty(rock) >= 20:
                "Do you want to give him the rocks?"
                menu:
                    "Yes" if True:
                        e 1 "I’ve got the rocks."
                        show witer stand with dissolve
                        w "Great, I’ll sort through these and test them out."
                        w "Here, a little something for your troubles."
                        "<You get 200 coins.>"
                        e 1 "Any idea when the bathhouse will be up and running?"
                        w "Probably in one day if nothing else goes wrong."
                        e 1 "Tomorrow, that’s pretty quick."
                        e 1 "Do you need help with anything else Witer?"
                        w "Nah, I can take it from here."
                        w "Just be there for the opening ceremony."
                        e 6 "I’ll see if I can make it."
                        $ jane_inv_M.drop(rock,20)
                        $ jane_inv.take(coin,200)
                        $ Map.bathroom_openday = Time.days+1
                        $ Map.bathroom_0 = 3
                        jump map1
                    "No" if True:
                        jump Witer_menu
            elif True:
                jump Witer_menu
    elif Map.bathroom_0 == 4:
        scene black with slow_dissolve
        if Map.bathroom == "EbbFlo":
            if Time.hours >= 6 and Time.hours <= 17:
                scene outdoor 1 with dissolve
            elif True:
                scene outdoor 1n with dissolve

            "At the opening ceremony Ebb and Flo stand in front of the bath house entrance while Snow and Chet watch them."
            show snow stand at left with slow_dissolve
            show flo happy with dissolve:
                xpos 0.3 ypos 0
            show ebb stand with dissolve:
                xpos 0.55 ypos 0

            s "There you all are. Come on, let’s get this show on the road."
            "Everyone gathers around the two new tavern guests."
            eb "Presenting Young Master Flo! "
            "Flo shakes his head, and walks forward while biting his bottom lip."
            f "Welcome everyone, thank you for coming to the grand reopening ceremony of the Tavern of Spear’s bath house."
            f "Why don’t we all go inside."
            f "We have snacks, and I honestly don’t want to give any formal speeches."
            f "Come on."
            "Everyone follows the pair into the bath house."
            hide snow stand at left with dissolve
            hide flo happy with dissolve
            hide ebb stand with dissolve
            pause 1
            play sound  "music/door.mp3"
            if Time.hours >= 6 and Time.hours <= 17:
                scene bathroom 1 with vslow_dissolve
            elif True:
                scene bathroom 1n with vslow_dissolve
            w "Woah!"
            show witer stand with moveinright
            hide witer stand with moveoutleft
            show snow laugh1 at right with slow_dissolve
            s "This place is way better than before!"
            hide snow laugh1 with slow_dissolve
            "The tavern master walks about the newly renovated room, feeling the smoothness of the walls, and the soft padding of the carpet that is laid out for the guests."
            eb "Please take a seat around the table."
            "The four of you struggle to make sufficient space around the table due to your large builds."
            "Chet is forced to share the side of the table with you, but he doesn’t seem to mind it."
            "He rests his head against your shoulder, and places on hand against your thigh."
            c "I like it, it’s so cozy. "
            "You chuckle back at him but then a cold chill flows down your spine."
            "Hakan is sitting across from you, but he’s just munching on the stack of jerky on the table."
            "No, the imposing aura is coming from the ghostly horn on his shoulder."
            e 9 "(Oh boy.)"
            "You gently nudge Chet back to his side of the seat."
            "You take a minute to take in your surroundings."
            "Further behind Hakan is a counter where Ebb is standing behind."
            "To his left is a curtain hanging above a door."
            "It has a pattern on it you’ve never seen before."
            "Your tail wags a little, curiosity filling your head, wondering what else is there about this new establishment."
            "Flo walks over to your right and addresses the group."

            show flo happy with dissolve:
                xpos 0.3 ypos 0
            show witer stand at left with slow_dissolve
            f "Pretty cool, right? We modeled the place after the bath houses back from where I’m from."
            f "And used the materials we brought over from the hut and anything we can find available around here."
            w "The interior decoration is so quaint. "
            f "Well your pointers came in handy Mr. Witer."
            hide witer stand at left with dissolve
            show snow stand at left with slow_dissolve
            s "The waiting room looks great."
            s "So how are you two running the place?"
            show flo stand with dissolve:
                xpos 0.3 ypos 0
            f "Right, so whenever anyone comes down, they head over to the counter over there. "
            "Flo points to the counter to his right."
            f "You just need to sign the guest book, and your first hour is free."
            f "If you come with another guest you have the first two and a half hours to yourselves."
            f "Anything more than that will cost you."
            f "100 coins if you are on your own, and 200 if you are bringing a guest."
            hide snow stand at left with dissolve
            show witer stand at left with dissolve
            w "I can’t wait to dip my toes into the hot spring!"
            w "It’s been ages since I got to take a proper bath."
            s "Mmm, mmm."
            "Snow nods agreeably."
            s "Yup, I expect everyone to take a regular shower."
            s "Finally my bar won’t reek of sweaty males."
            hide witer stand at left with dissolve
            hide flo stand with dissolve
            "Chet leans close to you to whisper into your ear."
            c "Doesn’t he also get a lion's share of the profits from here?"
            "You whisper back."
            e 6 "Right?"
            show flo happy at center with dissolve
            f "Well I think that’s all for the introduction."
            f "Enjoy the snacks, and we’ll be happy to start taking customers after we clean up here."
            hide flo happy at center with dissolve
            "A loud burping noise draws everyone’s attention."
            pause 1
            "Hakan holds out an empty bowl in his hands."
            h "You might want to get more of these."
            "After the brief opening celebration, everyone heads back to the tavern."
            "Some like Witer are already making plans to try to convince Hakan to bathe with him."
            "You decide to check out the bath house when you are free."
            play Ebb "music/char_ebb.ogg"
            play Flo "music/char_flo.ogg"
        elif True:

            if Time.hours >= 6 and Time.hours <= 17:
                scene outdoor 1 with dissolve
            elif True:
                scene outdoor 1n with dissolve

            "In front of the bath house Chet and Witer are already waiting for everyone."
            "They smile and wave as the three of you approach."
            c "Finally, we can get this show on the road."
            c "Come on in. It’ll be easier to explain things inside. "
            "Everyone heads into the bath house."
            pause 2
            play sound  "music/door.mp3"
            if Time.hours >= 6 and Time.hours <= 17:
                scene bathroom 1 with vslow_dissolve
            elif True:
                scene bathroom 1n with vslow_dissolve
            e 5 "Wow."
            "The interior is comfortably warm and smells of fragrant flowers."
            "Chet and Witer are standing in front of a counter."
            "Above the counter is a beautiful painting of a tree. "
            "Your eyes are then drawn to the curtains that cover the doorway to the next room."
            "Its pattern is foreign to you."
            "Somehow the ambience in the bath house put you at ease."
            show hakan stand at left with slow_dissolve
            show chet happy with dissolve:
                xpos 0.4 ypos 0.124
            show witer stand with dissolve:
                xpos 0.55 ypos 0.03
            c "Alright, let’s get this tour going so that we can head back to our usual jobs. "
            "Witer grabs a locked metal box from the counter."
            w "Since we’ll be busy with our full time jobs, we’ll be using an honour system to run the bath."
            w "You just need to sign the guest book, and your first hour is free."
            w "If you come with another guest you have the first two and a half hours to yourselves."
            w "Anything more than that will cost you. 100 coins if you are on your own, and 200 if you are bringing a guest."
            w "Just drop the coins into this metal box."
            h "What’s stopping anyone from not paying?"
            w "Well nothing, but Chet gets a cut from the bath house money box, and if it isn’t enough to pay back the cost of renting out the equipment from him-"
            show chet stand with dissolve:
                xpos 0.4 ypos 0.124
            c "I’ll take it all back, and you’ll be licking each other clean!"
            "Chet’s sudden intimidating voice catches you by surprise."
            e 9 "We’ll pay, we’ll pay."
            c "Great, well through the curtains are the locker room. "
            "From there you have access to the showers, the hot spring and the sauna."
            w "As an added bonus, we’ve got some cool kegs of beers kept under the counter which you can have some after using the baths."
            h "Alright, beer!"
            w "Non Dragons’ Bane Beer mind you."
            h "What? Talk about dull."
            w "And always mind the proper etiquette while using the bath house."
            "All clothes and equipment are to be stored in the locker rooms."
            w "Take a bath before entering the hot springs and at the end after using the sauna, then take another one before leaving."
            c "And of course all funny business is allowed, nay, encouraged!"
            hide hakan stand
            show snow stand at left with slow_dissolve
            s "I better not find you peeking at us while we’re in there."
            c "I wouldn’t dream of it. I would rather be in the action myself."
            w "Ehem, anyways that’s all for the opening ceremony."
            w "Give us some time to make sure everything is running right one last time, and everyone can start bathing."
            hide snow stand at left with dissolve
            hide chet stand with dissolve
            hide witer stand with dissolve
            "The grand opening ceremony ends, and everyone returns to the tavern."
            "Now you can visit the bath house to unwind, and even bring someone along if you feel like it."

        jump T_bathhouse0



label bathhouse_witer_bath_together:
    $ renpy.music.set_pause(True, channel='Ebb')
    $ renpy.music.set_pause(True, channel='Flo')
    $ renpy.music.set_volume(0, 0.1, channel = "Ebb")
    $ renpy.music.set_volume(0, 0.1, channel = "Flo")
    $ Witer.bathsex = 1
    "..."
    scene locker room with slow_dissolve
    ""
    stop music fadeout 1
    $ renpy.music.set_volume(1, 0.5, channel = "music")

    "While you wait for Witer in the locker room, you decide to undress before he arrives."
    "You remove your sword and satchel to place in the locker."
    "Your fingers reach the knot that keeps your loincloth tied together, and you undo them."
    "The cloth slips across your thighs exposing your bare bottom to the warm air."
    w "Nice view."
    "The alligator’s smooth voice steals your attention."
    "You turn to the entrance with your loincloth still in your hand."
    show witer stand at center with slow_dissolve
    e 6 "Witer, you’re here."
    w "Indeed, and I see you’ve started without me."
    hide witer stand with slow_dissolve
    "The alligator pulls down his pants."
    "His naked form fizzles out your brain."
    "Your jaw drops and you blink surprised by the waiter’s bravery for being in the nude. "
    "Witer walks closer to you, his hips almost seem to sway from to side as he does so."
    e 6 "I didn’t expect you to be here so soon. "
    "He stands inches away from you and leans close to your face."
    show witer stand_nude at center with slow_dissolve
    w "I never keep a client waiting. That would be bad business practice."
    e 1 "Well, since I called you over... "
    "You cross your arms."
    e 1 "You get to pick what we do now. Hot spring or sauna?"
    "Witer puts a finger under his chin as he thinks."
    w "If I get to choose, then I pick the hot springs."
    w "My tired bones could use a nice soak."
    e 6 "Then to the shower first."
    e 1 "Oh, there’s not enough space in there for the both of us at the same time."
    e 1 "Why don’t you shower first?"
    w "Don’t mind if I do. Don’t peek-"
    hide witer stand_nude at center with slow_dissolve
    "He hands you his pants and takes a towel from the bench."
    "His head turns slightly so he can see you through the corner of his eyes."
    w "Or do, I don’t mind an audience."
    "You gulp and grab a towel to cover your groin."
    scene black with slow_dissolve
    "After a few minutes of struggling as to whether you’re going to play peeping tom."
    "Witer steps out dripping wet from top to bottom. "
    scene locker room with slow_dissolve
    show witer stand_bath at center with dissolve
    "Your heart feels like it stopped for a second."
    w "Well I’ll see you in the hot spring. "
    hide witer stand_bath at center with slow_dissolve
    "He smacks your bottom with a swing of his tail and walks off into the hot spring area."
    "Cheeky alligator."
    scene black with slow_dissolve
    "The cold shower helps to calm your senses."
    "Once you have scrubbed yourself clean, you walk over to the hot spring area with your towel in hand."
    pause 2
    scene hotspring with slow_dissolve
    "Through the warm white spring fumes, you spot the alligator already in the waters."
    "His towel has been folded up and placed neatly on top of his head."
    play sound "music/wave.ogg"
    "He has his arm stretched out to the side of the pool and is just taking in the moment."
    w "Come in, the water’s fine."
    "You didn’t need to be told twice."
    "Matching Witer’s way of handling his tower you fold yours and put it over your head."
    e 0 "Ah… This is the best."
    "The waters’ warm embrace holds you still and you feel your muscles finally release the tension that has been building up inside."
    show witer stand_bath at center with dissolve
    w "Mmhmm. This takes me back to the days I would service my client in such a bath house."
    e 6 "That sounds wonderful if you get to use the hot spring every day."
    w "Yup, but I had to bring my own eggs to eat."
    e 1 "Eggs?"
    "You look at the relaxing gator with a raised eyebrow."
    w "Hard boiled eggs, you can cook them inside a very hot pool. Never tried it before?"
    e 6 "No, actually."
    w "It’s pretty tasty, plus if you have a bowl and some bread you can smoosh it together into a crude scrambled egg sandwich."
    e 1 "You think we can do that here?"
    if Map.bathroom == "None":
        w "I might run the place, but I don’t play favourites."
        w "No food or drinks in the hot spring."
    elif True:
        w "I think Ebb or Flo will charge us a fortune if they catch us doing that."
    w "Anyways-"
    "He looks at you now with a gentle glint in his eyes."
    "You look like you have something on your mind."
    e 1 "Well..."
    label bathhouse_witer_bath_together_talk:
        menu:
            "Ask how are things in the tavern" if True:
                w "Same old same old mostly. "
                w "Hakan’s drinking away at his supply of beers."
                w "And I’ve been helping Snow out with keeping the stocks in check and that the place clean."
                w "Oh, Chet’s been working Hakan’s butt off to gather materials for him."
                e 6 "Wonder why’s that."
                w "Probably to keep up with your requests, and if you need more stuff in the future."
                w "While Snow’s been working hard on making sure we have enough food in case new guests come too."
                hide witer stand_bath at center with slow_dissolve
                "He turns and looks longingly at the white steam floating above the pool."
                w "I honestly feel like I should be doing more."
                "Witer sighs."
                w "You know it’s not easy for me to not be ok around people."
                w "But after how you’ve helped me, I trust that you can keep this just between us?"
                e 1 "Well sure."
                w "I really feel like I’m not doing much for the tavern or for you."
                "You nod to indicate that you hear him and that you want to know more."
                w "Everyone’s doing something big to help out, but I’m just cleaning up stuff or serving people."
                w "Maybe I’m just dead weight. "
                e 1 "Hmm…"
                "You raise your right hand and splash hard on the water, sending a wet slap across of Witer’s face."
                w "Hey! What’s that for?" with vpunch
                e 1 "That’s for insulting yourself."
                e 1 "What happened to you saying that you're strong?"
                w "I am strong."
                e 3 "Oh yeah? Well I don’t see it. "
                "Witer gasps and proceeds to splash water back at you."
                e 5 "Ah! No, no. Remember no rough housing in the hot spring."
                "Witer crosses his arms in a huff."
                w " I wasn’t going to, and I am strong."
                show witer stand_bath at center with dissolve
                w "I just- I’m just unsure if I am doing enough."
                e 13 "Well I think you don’t give yourself enough credit."
                e 1 "If it wasn’t for you, who’s going to keep everyone in check?"
                e 1 "Who's going to make sure the tavern stays in shape or who’s going to make sure Hakan and Chet eat healthy and drink right? Who’s-"
                w "Ok, ok. Gosh, it’s embarrassing to hear you say such things about me."
                "The alligator’s cheeks turn red, but you’re not sure if it’s because of the hot water or how he’s feeling."
                w "But what I say is valid too."
                w "I’m not fishing for compliments, I want to do more, especially for you."
                e 10 "Oh."
                "Now you feel yourself turning red."
                w "I want to support you out there."
                e 7 "Hey, knowing you are safe here is enough support for me."
                e 1 "That said, I wouldn’t say no to more help."
                w "Well I’ve been thinking, and maybe there are a few things I could consider."
                w "I could be a tailor and make light armour for you?"
                e 1 "Let me guess, you learnt it from your brother."
                w "Actually, we learnt it together."
                w "When Walden was starting up, his mentor taught him some light armour crafting skills too."
                w "So, when I had the time, I would practice with him."
                w "Oh, and I do know how to craft tiny mechanisms that can be used against enemies."
                e 1 "What sort of tiny mechanisms? Like bugs?"
                w "Kind of, I could make them look like that."
                w "Back in the city, it can be dangerous for someone like me to walk around the streets."
                w "If it’s not the soldiers trying to grope me up for a free ride."
                w "Then it’s the local perverts who think I’m free land to plant their seed."
                w "So, I met an inventor and in exchange for some favours."
                w "He taught me how to make some self defence tools out of random materials."
                w "It’s pretty handy."
                e 5 "Woah, a jack of all trades I see."
                e 1 "Yeah, you can totally help out with those smarts of yours."
                "Witer’s face beams from the compliment."
                w "I’ll think about it."
                w "I mean after all, you did say you’re happy with me just being safe… "
                w "But maybe, if it’ll make you happier."
                "You smile back at him and give him a thumbs up."
                w "What else is on your pretty little head?"
                jump bathhouse_witer_bath_together_talk
            "Ask about Witer’s dreams" if True:
                e 1 "We’ve been here for quite some time now."
                w "That we have."
                e 1 "You ever think about the future? Like what you want after all of this is over?"
                w "Hmm…"
                hide witer stand_bath at center with slow_dissolve
                "Witer sinks deeper into the water until only the top half of his head is seen."
                "He closes his eyes and makes bubbles on the water’s surface."
                e 1 "Witer?"
                "He reemerges."
                show witer stand_bath at center with dissolve
                w "I imagine that you’ll go on more crazy adventures and you’ll attract more tough guys like yourself on your journey."
                w "Then you’ll need a base of operations."
                w "So you’ll make base at Snow’s tavern. "
                e 5 "Woah, Snow’s tavern?"
                "You nearly laugh and so does Witer but he carries on."
                w "Then you’ll buy your gear from the town’s most famous shopkeeper, Chet."
                w "His emporium will sell you all sorts of goods."
                e 6 "Possible, possible. "
                w "And if you’re in need of new clothes, new healing materials or just a beautiful bouquet for someone special, you can come to Witer & Brothers."
                "You laugh out loud."
                e 3 "Then where’s the rest?"
                w "I never really thought that far."
                w "It would be great if Hakan joins your adventuring team."
                w "But I don’t know if he would prefer to continue on his mercenary work."
                w "Either way, I wish that even after all of this is over, we’d all still be together in some way."
                e 13 "Yeah, I’d like that too."
                w "Anything else?"
                jump bathhouse_witer_bath_together_talk
            "Ask about Witer’s family" if True:
                e 1 "Hey, have you ever been curious about your parents?"
                w "My parents? Hmm, it’s been so long since I last thought about them."
                w "Honestly, I want to know more about Walden and Wally’s origins."
                e 1 "Your brothers? How come?"
                w "Well, it’s more that when Wally was seven, he started school."
                w "He saw all the kids were talking about what their parents did or how great their family heritage was."
                w "So like kids do, he got curious and asked about where he came from? Then Walden did the same."
                "The alligator splashes his face with some water."
                w "Ugh, can you imagine being bombarded with the same question for an entire week?"
                e 1 "Then how’d you got them to stop?"
                w "I just told them the truth. I didn’t know, and that was the end of it."
                w "They were disappointed, but we eventually got busy with work and class, so it didn’t last really long."
                e 1 "So, if given a chance you would want to find out about their past."
                w "Yeah, at least what tribe they’re from."
                w "That would be a good starting point, because believe me I tried asking around."
                w "But no one has ever seen their kind before."
                e 6 "Interesting."
                e 1 "Well, keep a chin up, maybe luck might have it someone here might know."
                w "Yeah, just maybe. I’ll have to ask around."
                w "Anything else you want to talk about?"
                jump bathhouse_witer_bath_together_talk
            "Nothing to ask" if True:
                e 1 "Nah, I’m good. Let’s just enjoy the bath."
                "You both sit together in silence and just enjoy being with each other."
                pass
    hide witer stand_bath at center with slow_dissolve
    scene black with slow_dissolve
    "..."
    "..."
    if Witer.bj:
        $ Witer.bathsex = 2
    elif True:
        $ Witer.bathsex = 3

    jump bathhouse_bath_end

    label bathhouse_witer_bath_together_after:
        pause 2
        scene hotspring with slow_dissolve
        if Witer.bathsex == 2:
            "Then you feel a hand reach out to yours."
            "Your fingers interlock."
            "You turn to Witer who gives you a knowing smile. "
            "His gaze speaks to you of his desire. "
            "Your groin stirs in anticipation."
            "Succumbing to your passion"
            show witer stand_bath at center with slow_dissolve
            w "Why don’t we continue this somewhere more comfortable?"
            $ Witer.bathsex = 0
            menu:
                "My room’s free" if True:
                    e 7 "My room’s free."
                    w "Shall we?"
                    hide witer stand_bath at center with slow_dissolve
                    "He stands up and leads you by the hand out of the hot spring."
                    scene black with slow_dissolve
                    "Your hard dick bobbles as you walk, but you don’t mind showing it. "
                    "After another shower, the two of you leave the hot spring and head for your room."
                    pause 5
                    jump witer_cowboy
                "Maybe next time" if True:
                    e 6 "Maybe next time."
                    w "Ok."
                    w "Thanks for the invite. "
                    "He raises his tail and suggestively waves his butt from side to side in front of you."
                    w "If you ever want some more company, just leave a handsome tip."
                    w "You know where to find me."
                    "You smile and watch as the muscular alligator walks out of the hot spring."
                    "When it’s finally your turn to leave the hot spring, you find that Witer had already left."
                    "So you take a shower before putting your gear back on."
                    $ Witer.bathsex = 0
                    jump T_bathhouse
        elif Witer.bathsex == 3:
            "After a few minutes, Witer stands up and gives you a nice view of his ass."
            "He turns to you."
            show witer stand_bath at center with slow_dissolve
            w "Thanks for the invite. "
            "He raises his tail and suggestively waves his butt from side to side in front of you."
            w "If you ever want some more company, just leave a handsome tip."
            w "You know where to find me."
            "You smile and watch as the muscular alligator walks out of the hot spring."
            "When it’s finally your turn to leave the hot spring, you find that Witer had already left."
            "So you take a shower before putting your gear back on."
            "You leave feeling invigorated but yet somehow sexually frustrated."
            $ Witer.bathsex = 0
        elif True:
            "Bug here pls report."
            $ Witer.bathsex = 0

        jump T_bathhouse




label bathhouse_hakan_sauna:
    $ renpy.music.set_pause(True, channel='Ebb')
    $ renpy.music.set_pause(True, channel='Flo')
    $ renpy.music.set_volume(0, 0.1, channel = "Ebb")
    $ renpy.music.set_volume(0, 0.1, channel = "Flo")
    "..."
    scene locker room with slow_dissolve
    "You waited inside the locker room for your companion to arrive. "
    "Several minutes passes… then you hear Hakan’s voice coming from the counter."
    "The red dragon then steps through the doorway."
    show hakan stand at center with slow_dissolve
    h "Kept you waiting, huh?"
    e 6 "Well you’re worth the wait."
    hide hakan stand at center with dissolve
    "Hakan walks closer and turns to the locker across from yours."
    "He starts to undress himself, starting with removing his bracers."
    h "I wasn’t expecting that invite from you."
    e 1 "What can I say? I needed someone to wash my back."
    h "Oh, is that so?"
    "You hear the gentle thud of Hakan’s locker, then you are caught off guard when his arms wrap around you from behind."
    h "Are you sure that’s all you want me to do from behind?"
    "You feel something warm pressing and grinding against your bare naked behind."
    e 10 "What else do you have in mind?"
    "With your right hand you reach backwards and grope the dragon’s half erect cock through the towel."
    show hakan stand_bath at center with slow_dissolve
    h "Let's find out where we can go after this shower then."
    hide hakan stand_bath at center with dissolve
    "He holds your hand as you let go of his hardening dick, and leads you to the shower room."
    "When Hakan opens the door to the shower he stops walking."
    e 1 "What’s wrong?"
    h "Fuzz Butt, did you know the shower stall is big enough for one guy?"
    e 5 "Wait really?"
    "You bend down and poke through Hakan’s right arm to look."
    e 5 "I never noticed that before. Will it be a pro- ugh!"
    "Hakan locks your neck between his arms."
    h "Not if you don’t mind us only being half clean, or perhaps…"
    "He releases your neck from his hold."
    show hakan stand_nude2 at center with slow_dissolve
    "You step back a bit and stand up and he turns to face you."
    h "Perhaps you can lick me clean?"
    "Hakan wets his lips with his long tongue while he looks at you hungrily."
    menu:
        "Yes" if True:
            $ Hakan.sauna = 1
            e 10 "Don’t mind if I do."
        "Let's talk about something else" if True:
            $ Hakan.sauna = 0
            e 10 "Wha- are you crazy? No."
    "Hakan laughs loudly at your response. "
    show hakan stand_bath at center with slow_dissolve
    h "I’m joking, man you fell for that so easily."
    h "You go in and shower first. I’ll go after you. "
    "He spanks you in the butt to which you reply with a soft growl."
    hide hakan stand_bath at center with slow_dissolve
    "You enter the shower stall and take your shower."
    "When it is Hakan’s turn you wait patiently while he bathes."
    "Throughout his shower you can hear him humming a song."
    "After his shower Hakan exits with a confident smile."
    "The red scales on his massive frame shines brightly like a newly polished ruby."
    "Hakan notices you watching and flexes his left arm."
    "His arm bulges upwards, it is thick with his powerful muscle."
    show hakan stand_bath at center with slow_dissolve
    h "Whatcha think?"
    e 6 "Looking good, so where do you want to head to next?"
    e 6 "The hot spring or the sauna."
    "Hakan crosses his arms."
    h "Definitely the sauna. If I want to relax I prefer to sweat out my stress."
    e 1 "Then let’s go."
    hide hakan stand_bath at center with dissolve
    "You both head over to the sauna room."
    scene sauna with slow_dissolve
    "The instant you open the door to the sauna a warm cloud of steam washes over your face."
    "The warm interior of the sauna is pleasantly inviting."
    "You both take your seats next to each other."
    "In the middle of the room is a wooden box that holds the sauna rocks."
    "On the seat Hakan lies on his side like he was on a bed."
    "He supports his head with one hand so he can look up at you."
    "You on the other hand sit casually."
    "The sauna room is very stuffy, but you don’t mind it."
    show hakan stand_bath at center with slow_dissolve
    h "Now this is the stuff, I didn’t have this even back in my home city."
    "Maybe this is the time to know him better?"
    if Hakan.sauna_talk == 3 and Hakan.sauna == 1:
        menu:
            "Find some topic to chat" if True:
                $ Hakan.sauna_talk = 0
                jump bathhouse_hakan_talk
            "Skip the topic" if True:
                $ Hakan.sauna_talk = 3
                jump bathhouse_hakan_sixnine
    jump bathhouse_hakan_talk
    label bathhouse_hakan_talk_check:
        hide hakan stand_bath at center with dissolve
        $ Hakan.sauna_talk = Hakan.sauna_talk +1
        if Hakan.sauna_talk == 0 or Hakan.sauna_talk == 1 or Hakan.sauna_talk == 2:
            "Hakan grabs a ladle of water using his tail."
            "He pours the liquid over the hot rocks, releasing more steam inside the room."
            show hakan stand_bath at center with dissolve
            pass
        elif Hakan.sauna_talk >= 3:
            $ Hakan.sauna_talk = 3
            "It’s getting warmer inside the sauna room."
            "The heat takes its effect on you. Sweat begins to form all over your body and Hakan’s."
            "This time you pick up the ladle to add more steam."
            jump bathhouse_hakan_sixnine
    label bathhouse_hakan_talk:
        menu:
            "Ask where Hakan is from" if True:
                e 1 "Where are you from exactly?"
                "Hakan pats his belly with his other hand. "
                h "Salekvard."
                e 1 "Salekvard? That’s a surprise you look more like-"
                h "Like someone from a tough clan? Sorry to disappoint you."
                e 6 "It’s just Salkvard, it’s a very fancy city."
                h "No one picks where they are raised. "
                e 1 "Then why did you leave to become a mercenary?"
                h "Lets just say I didn’t belong."
                h "I got what I needed to survive there on my own and left."
                h "It was easier for me to make my own life than to stay there."
                e 1 "Interesting that you picked being a mercenary."
                h "We all have our reasons for the work we choose to do."
                h "Being a mercenary means more than the usual brute that kills things."
                h "I hope you understand that at this point."
                h "Besides, being a mercenary meant the caravans will take u travel all round the world."
                h "The good thing about going from place to place, is that you don’t get any unnecessary baggage to hold you back."
                e 1 "What do you mean?"
                h "Just a little something I picked up after I left Salekvard."
                e 1 "Do you ever think about settling down?"
                h "I… did…"
                "His voice softens."
                h "The thought crossed my mind once or twice."
                h "I’d go for one big haul and finally retire in some tropical kingdom."
                e 1 "Why didn’t you?"
                hide hakan stand_bath at center with dissolve
                "Hakan’s eyes look away from you."
                h "… Something… happened."
                "You sense that discussing this has brought back some unhappy memories for the dragon."
                e 0 "Sorry."
                h "No, it’s fine. "
                show hakan stand_bath at center with dissolve
                "He uses his forefinger and thumb to massage his eyes."
                h "I bet you have your reasons for being an adventurer."
                e 13 "It’s not really a job."
                e 1 "This is just what I need to do now as part of my rite of passage."
                h "Then what will you do after that? Once it’s all done."
                e 9 "I… don’t know."
                h "Something to think about there."
                h "You might even consider doing something that involves adventuring."
                h "It seems to suit you."
                e 6 "Maybe, I’ll think about it."
            "Ask how long Hakan has been a mercenary" if True:

                e 1 "How long have you been doing this job?"
                h "Let me think."
                "He counts the years with his free hand."
                h "Hmm, nope. Can’t remember."
                e 1 "What? Well, how old are you now?"
                h "Hmm, eighty maybe ninety years old."
                h "Give or take a few years."
                e 9 "Eighty to ninety?"
                e 9 "What the heck? You don’t look that old."
                h "That’s nice of you to say, but us dragons have a longer lifespan than other species. "
                e 6 "You’re practically old enough to be a grandfather."
                h "Hey, I’m still stronger than you and most fighters."
                if Hakan.quest >= 11:
                    h "I’m sure how I pounded your ass before is good enough proof of that."
                    e 10 "I- I guess so."
            "Ask about Hakan being drunk" if True:
                e 1 "I see you’ve really been hitting the bottle."
                h "How can I not? Getting drunk is the best!"
                h "I’ve seen travellers get drunk so often, and I’ve always wondered what it felt like."
                h "And now I know. All your worries just wash away, and you feel indestructible."
                e 1 "…"
                h "But I think I am running low on my supply of beer. Time to save up!"
            "Ask him about his old partner" if True:
                e 1 "There’s something I want to ask about Pierro."
                h "I want more steam."
                "Hakan grabs the ladle and adds more water to the rocks, effectively ending the conversation there."

        jump bathhouse_hakan_talk_check
    label bathhouse_hakan_sixnine:
        if Hakan.sauna == 0:
            scene black with slow_dissolve
            "You spend the next few minutes chatting with Hakan."
            "Once you both reach your limits you end your trip to the hot spring with another shower."
            "Hakan happily accepts the free beer at the counter and thanks you for inviting him."
            "Your hot spring day with Hakan ends."
        elif True:

            h "Hey, about earlier."
            e 1 "Hmm?"
            h "I asked if you could give me a tongue bath and you said yes."
            e 10 "I..."
            "Hakan raises an eyebrow and smiles at you smugly."
            "You look away at the door, blushing."
            "It's too embarrassing to look at him directly."
            "Then there’s the sound of fabric moving."
            e 1 "Huh?"
            "You turn to face Hakan and your cheeks burn even redder, and your eyes widen in surprise. "
            scene hakan_sauna01 with slow_dissolve
            "Hakan has disrobed, exposing his naked form to you."
            "His chest rumbles as he smiles at you."
            "You are at a loss for words."
            "There is a dryness in your throat forcing you to gulp."
            "The heat of your desire swells up inside you."
            h "Well? Get to it then. Use that tongue and clean me."
            "You nod and undo the knot on your towel, letting the fabric fall and freeing your throbbing hard cock."
            "Hakan licks his lips hungrily and spreads his leg wider inviting you to have a taste."
            "You drop to your knees and close your eyes."
            scene black with slow_dissolve
            "Your nose is inches away from brushing against Hakan’s sweaty ass."
            "All you can feel is the creamy white of his plump, juicy behind."
            "Its voluptuousness is akin to a pair of ripe grapefruits. "
            "Drawn in by your growing passion you reach out with both hands and grab the dragon’s ass."
            "His buttcheeks are smooth and meaty to touch just like the rest of him."
            h "You just going be on your knees staring or-"
            h "Woah!"
            "You plant your snout deep between his ass cheeks."
            "The pungent, earthy smell that fills your nostrils intoxicates you."
            "This is Hakan’s smell."
            "So deep, so masculine, you twist and turn your head burying your nose deeper inside his ass."
            "Hakan gasps and moans loudly. His body shudders wildly while you invade him with your face."
            "The more he groans and shudders the more you enjoy it."
            "You pull yourself back to look at the naked dragon, your raging boner is dripping pre onto the wooden bench."
            "Bending down you face the base of his thick tail."
            "You stick your tongue out and start licking the sweat off of Hakan."
            h "Fuck, your tongue is hot!"
            "The taste on your tongue is mild but familiar."
            e 0 "Salty."
            h "I got something more salty up here. Come get it."
            "You continue licking Hakan’s tail but slowly, you inch upwards."
            "You savour the saltiness as you climb the heights of pleasure, wanting more and more."
            "Your tongue travels upwards and brushes against Hakan’s balls."
            "The line of fur along his sack tickles your nose, but it doesn’t stop you."
            "Opening your mouth you suckle on Hakan’s sweet balls."
            "They fill your mouth and fan your flames of desire for what lies even higher."
            "No treat in the kingdom could compare to the salty orbs inside your mouth. "
            "You use your tongue to fondle each testicle, savoring his taste in your mouth."
            "Hakan lets out a deep growl. You can hear him breathing heavier and faster."
            "While you suck on Hakan’s balls you feel something wet and hard swipe up across your nose."
            scene hakan_sauna02 with slow_dissolve
            "You open your eyes and see Hakan’s dick rising to full mass."
            "From where you’re standing the dragon’s member towers over your face like a giant’s dick."
            "You stare in awe at his shaft not realizing that you’ve stopped licking his balls."
            "Hakan’s hand reaches out and grabs his thick shaft."
            "He swings his member from side to side slapping your nose with his hot member."
            "He smears your nose with the wet pre that leaks from the tip of his dick."
            h "You ready to finish the job Fuzz Butt?"
            "You lick off the pre from your nose and nod obediently."
            "The heat of the sauna is nothing compared to the heat of your loins desiring more of Hakan’s meat club."
            h "Let me help you out then."
            scene sauna with slow_dissolve
            "He stands up to his full height while all you do is watch his glistening sweaty muscles."
            "Hakan grabs you by the armpits and lifts you up with ease before lying you down where he was."
            "The bench is wet from Hakan’s sweat. "
            h "Open wide."
            scene hakan_sauna03 with slow_dissolve
            "Hakan lies on top of your body with his huge cock hovering right on top of your face."
            "Tiny beads of sweat drip along his shaft."
            "You open your mouth and let the sweat drip onto your tongue."
            "A tingling sensation from your dick then grabs your attention."
            "It feels like a tongue playfully trying to penetrate your cockhead."
            "You arch your head slightly and see Hakan grabbing your dick with one hand and is slowly sucking you off."
            "You gasp as your cock slowly enters his mouth."
            "Hakan is mumbling something with his mouth full."
            "You open your mouth ready to receive the dragon’s leaking cock."
            scene hakan_sauna04 with slow_dissolve
            "Hakan pulls his mouth away from your wet cock."
            "Just then his entire cock enters your mouth."
            e 0 "Mmmph!"
            scene hakan_sauna05 with slow_dissolve
            "Hakan licks his lips hungrily at you."
            h "Take it all in Fuzz Butt."
            h "Yeah, taste my cock. You love having my cock in your mouth as much as it is in your ass don’t you?"
            "Your mouth is too full to speak."
            "Instead you respond by bobbing your head back and forth along the dragon’s dick."
            h "Ngh! Use your tongue Fuzz Butt."
            "You use your tongue to play with Hakan’s tip like he did yours."
            "His beatial growl tells you he likes it a lot."
            "Hakan then grabs your cock again and sucks hard on your member."
            "Your entire body tenses up. Waves of pleasure flood your body from both ends."
            "Still, you cannot stop, Hakan won’t let you."
            pause 1
            "You are lost in a sea of pleasure, and pleasure tastes like Hakan’s precum."
            "As you suck his dick you swallow the rich nectar that pours from the dragon’s cock."
            e 0 "Hngh!"
            "Suddenly, Hakan’s hips start bucking and he is fucking your mouth wildly."
            h "Yes, more! More! Keep going. I’m close!"
            "While he fucks your face, he continues to furiously jerk your cock."
            "You succumb to the pleasure."
            "You’re not even able to tell if you remember to breath, all you can do is suck and get sucked. "
            "Your balls tighten and retract inside you. "
            "You’re so close!"
            "Hakan suddenly plunges into your ass deep enough to reach your prostate."
            "He massages your spot expertly pushing you to the point of no return."
            with flashbulb
            with flashbulb
            scene hakan_sauna06 with vslow_dissolve
            "Both you and Hakan release your built up seed with tremendous force."
            "You’re practically drowning in dragon cum inside your mouth, hot cum gushes down your throat with the force of the falls."
            "His thick and viscous cum forces its way inside you."
            "The saltiness of his seed is stronger than his pre."
            "You try as much as you can to down every drop of the dragon’s cum but it is too much! "
            "It’s leaking out of the sides of your mouth."
            "The sheer rush of euphoria numbs your whole body."
            "You don’t even notice that your cock is spraying hot semen all over Hakan’s face."
            h "Fuck!"
            "Shot after shot of semen flies over Hakan, some even landing on your stomach."
            "After what feels like an eternity, both your orgasms subside."
            "Hakan pulls his cock out of your mouth and stands up."
            scene sauna with vslow_dissolve
            "You sit back up and both of you look at each other panting like dogs."
            e 0 "That was…"
            "There’s cum all over Hakan and yourself. "
            "The entire sauna now smells of sex and sweat."
            "Hakan chuckles softly then breaks out into a rowdy laugh."
            h "We got to do that again!"
            e 10 "Yeah, I’m up for it if you are."
            h "Come on, we better take a shower again."
            scene black with slow_dissolve
            "You nod and follow Hakan to the showers."
            "After you both get cleaned you both exit the bathing area."
            pause 3
            $ persistent.CG_hakan_sixnine = True
            $ Zalt.lust = 0
            if Map.bathroom == "EbbFlo" and Bath_npc == 2:
                "While walking out to the counter Flo winks at you while you leave. "
                "You blush and walk out quickly."
            if Map.bathroom == "EbbFlo" and Bath_npc == 1:
                "While walking out to the counter Ebb winks at you while you leave. "
                "You blush and walk out quickly."
            $ Zalt.sex = Zalt.sex +1
        jump bathhouse_bath_end
    $ Hakan.sauna_talk = Hakan.sauna_talk +1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
