label Ebb_meet:
    stop music

    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    $ renpy.music.set_volume(0, 5, channel = "Chan2")

    $ renpy.music.set_pause(False, channel='Ebb')
    $ renpy.music.set_volume(0.8, 6, channel = "Ebb")

    $ Time.mins = Time.mins +5
    if Time.hours >= 6 and Time.hours <= 17:
        scene cabin 1 with slow_dissolve
    elif True:
        scene cabin 1n with slow_dissolve
    if Ebb.meet == 0:
        e 1 "Hello?"
        "The room is a mess, there’s only a couch here and everything else looks like a tornado swept in and smashed everything."
        "???" "YOU DARE COME BACK DEMON!" with vpunch
        "A dishevelled looking orca emerges from the side door swinging a wooden bat. "
        e 9 "Woah, calm down. I’m not a demon!"
        "You back away towards the exit."
        "???" "What?"
        show ebb stand at center with dissolve
        "The orca sops swinging his bat and looks at you."
        "Your eyes are drawn to his wide white eye patches that contort to form an expression of confusion."
        "Unknown Orca" "Master Snow? Is that you?"
        e 1 "Umm, no. I’m [name], from the tavern."
        hide ebb stand at center with dissolve
        "Upon hearing your introduction the orca sets the bat down, and straightens his coat."
        "He then tries to adjust an absent necktie, when he realizes what he’s doing he drops his hands and bows."
        show ebb stand at center with dissolve
        "Unknown Orca" "A warrior from the tavern! Please, forgive my unruly state."
        "Unknown Orca" "It would be an honour for me to offer Master [name] a cup of tea."
        "He gestures towards the beaten up sofa in the living room."
        "Somehow his silvery and low voice puts you at ease."
        "Which makes you more cautious of him than before."
        e 1 "No thank you. This is going pretty quick."
        e 1 "Before I start having anything from you, explain yourself, who are you and what are you doing here?"
        eb "Yes, I am Ebb, butler to Young Master Flo."
        eb "This is our humble abode for the time being until the fog lifts."
        e 1 "And you know about the tavern?"
        eb "Of course, it’s the first place we stopped by when we came. Is Master Snow in good health?"
        e 1 "Yeah, uhh everyone’s fine."
        "You ease your stance and sheath back your sword."
        e 1 "Sorry, just had to be careful with new faces around here."
        eb "It’s understandable, please have a seat at least."
        hide ebb stand at center with dissolve
        if Time.hours >= 6 and Time.hours <= 17:
            scene ebbroom 1 with slow_dissolve
        elif True:
            scene ebbroom 1n with slow_dissolve
        "Sensing no malice from the orca you follow the orca into another room."
        "A loom takes up most of the room, but the interior is far cleaner than the mess you just saw."
        "You take a seat in an empty chair."
        "While the orca stands from across the room, his hands folded in front."
        "Your body sinks into the cushions."
        show ebb stand at center with dissolve
        e 1 "Aren’t you going to sit down and join me?"
        eb "Your consideration is appreciated, Master [name], but it would be improper for a butler to sit with the guest."
        eb "Forgive me for my impudence, but I must ask."
        eb "Is Master [name]’s presence here means the tavern has decided to help me save my Young Master?"
        "You flinch back and look at the orca with a raised eyebrow."
        e 1 "Sorry what? Save who?"
        eb "I am truly sorry, I was under the impression that Master Snow sent you to help me with my problem."
        e 1 "Just start back from the beginning, what is this all about?"
        hide ebb stand at center with dissolve
        "Ebb clutches his hands and walks to the front of you."
        "He falls to his knees and grovels before you."
        "The prim and proper stature he had on shatters in an instance."
        eb "Please, I need help, I beg you, help me save my Young Master."
        eb "Time is running out, and I am at my wits ends."
        "You stand up and hold your hands in front of you waving them frantically."
        e 5 "Ebb, get up, I’ll hear you out, but you need to explain properly."
        "Ebb pulls himself up. He’s still sitting on his knees, but his face beams with hope."
        eb "Master [name], thank you. I shouldn’t let my desperation cloud my actions."
        eb "I still have to uphold Young Master Flo’s name."
        show ebb stand at center with dissolve
        "Ebb takes a deep breath and his face relaxes into his stoic expression again."
        eb "It happened about a week ago, it was the dead of night when I heard glass breaking from the Young Master’s room."
        eb "I ran from the couch into his room, and I saw a monster grabbing the terrified Young Master on it’s shoulder."
        eb "Before I could stop it the creature leapt at me and I fought it."
        eb "Master Flo was screaming for help but the creature was too strong."
        eb "It tore through the living room, breaking all our furniture. "
        eb "After it knocked me down it ran out of the house."
        eb "I tried to give chase, but I ended up triggering the traps I set on myself."
        eb "I was left badly injured, but I managed to drag myself to the tavern."
        eb "Snow and Witer helped to patch me up, but when I asked for their help to save the Young Master."
        eb "Master Snow refused saying it was too dangerous for him to risk the life of someone from the tavern."
        e 5 "That’s..."
        eb "It’s fine, I didn’t blame him, I wasn’t expecting anyone to put their life on the line on a possible suicide mission."
        hide ebb stand at center with dissolve
        "Ebb covers his eyes with his hands and shakes his head in defeat."
        show ebb stand at center with dissolve
        eb "Every minute that passes by, my heart aches in fear of what will happen to the Young Master."
        eb "I tried looking for help elsewhere, but the bull lizard attack me with no reason ,and the lizard tribe wouldn’t even let me in to speak to their chief."
        e 1 "..."
        eb "Dear god, how will I tell his father how I’ve failed his son."
        "The orca’s distraught stings your heart."
        "But even you find it hard to say anything hopeful for fear it will just be empty promises that will break him further."
        "All you know is that he needs help, and the longer time passes the slimmer the chances of bringing his Young Master back."
        e 13 "You’re thinking too far Ebb."
        e 13 "If what you say is true, then we haven’t much time left to save Flo. "
        eb "You really think he’ll be ok?"
        hide ebb stand at center with dissolve
        "You look to the floor, there’s no answer you could give that would make this situation any less dire."
        show ebb stand at center with dissolve
        e 13 "(Oh [name], Why do you always like to involve yourself in unnecessary trouble.)"
        e 1 "Stay strong Ebb, we’ll worry about his fate when we find him."
        e 1 "For now, I’ll help you get him back."
        hide ebb stand at center with dissolve
        "Ebb stands back up and pulls you in for a hug."
        "He starts sobbing and pressing you harder against his chest."
        eb "Thank you... thank you..."
        e 1 "Ebb, you’re welcome, but we need to work fast."
        eb "Right, I apologize, that was unbecoming of a butler."
        "He pulls away from the hug."
        show ebb stand at center with dissolve
        "Ebb stands up, turns away and looks up to the ceiling for a minute before facing you again."
        "The orca pulls out a pair of black gloves from his pocket and hands it to you."
        eb "That is the Young Master’s favourite gloves, you might be able to track him down using his scent."
        e 1 "What else should I know about Flo to track him down?"
        eb "He’s a young shark, 19 this year."
        eb "He should probably stand out if you find him."
        e 1 "Alright, sit tight, I’ll come back with news."
        eb "Thank you Master [name], and please hurry."
        scene black with dissolve
        "You nod and run out of the hut until you’re out of the forest."
        if Time.hours >= 6 and Time.hours <= 17:
            scene lakecabin 1 with slow_dissolve
        elif True:
            scene lakecabin 1n with slow_dissolve
        e 1 "(This fog has taken so much from the people around here.)"
        e 13 "(I can’t let another person suffer like this. I just hope I make it in time.)"
        "You take out the pair of gloves and take a deep whiff of its owner’s scent."
        "It smells like the sea, with a hint of an intoxicating flowery smell."
        "Sniffing around, your nose picks up the trail, it leads to the bridge behind the tavern."
        $ Ebb.meet = 1
        $ Ebb.kidnap = 1
        jump forest_map

label Ebb_talk0:
    show ebb stand at center with dissolve
    if Ebb.necklace == 0 and Map.undercity_auc_start == 1:

        e 1 "Ebb, I found Flo."
        eb "You did? Where?" with vpunch
        e 13 "He’s being held hostage as an auction item."
        eb "An auction item? What demons are these?" with vpunch
        e 1 "Literal demons, I need to buy his freedom back."
        eb "Wait, take this with you."
        "Ebb hands you a necklace."
        e 1 "What’s this?"
        eb "The only valuable item we have."
        eb "It’s a necklace from the Young Master’s family treasury."
        eb "Maybe you can sell it to get some coins."
        e 1 "Thanks, I think this will help."
        eb "Bring him home, [name]."
        $ jane_inv_K.take(ebb_necklace,1)
        $ Ebb.necklace = 1
        hide ebb stand with dissolve
        jump lakecabin_ebbroom
    elif True:
        if Ebb.kidnap == 4:
            eb "Thank you again Master [name]."
        elif True:

            eb "Master [name], any news on the Young Master?"
            e 1 "Not yet, the search will take some time."
            eb "Oh, I see. Please let me know if you find anything."
            eb "The longer the Young Master is missing my heart grows weary. "
            e 1 "Stay strong Ebb, we’ll get him back."

    hide ebb stand with dissolve
    jump lakecabin_ebbroom

label Ebb_kidnap_end:
    if Time.hours >= 6 and Time.hours <= 17:
        scene lakecabin 1 with vslow_dissolve
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
    elif True:
        scene lakecabin 1n with vslow_dissolve
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
    if Flo.meet == 1:
        "When you knock on the door of the hut you can hear the hurried footsteps of Ebb running to the door."
        play sound "music/door.mp3"
        "The door swings open."
        show flo stand01 with slow_dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        show ebb stand at right with dissolve
        eb "Young master! You’re safe!" with vpunch
        "The orca happily rushes forward and grabs Flo in his arms, swinging the smaller shark from side to side in a tight hug."
        eb "Young master! I was so worried."
        "Flo keeps slapping Ebb angrily by the shoulder. "
        f "Put me down, you!" with vpunch
        f "I don’t want to be hugged!"
        "Ebb does as he is commanded and lets go of Flo. "
        show flo stand01 with slow_dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        show ebb stand at right with dissolve
        f "Hmph. "
        "Flo turns to you."
        f "Thank you [name] for the rescue, I’ll leave it to this orca to carry on his transaction with you. "
        "He then turns to the orca."
        f "I’m going to be in my room. I need to sleep."
        "Flo pushes past his butler and heads into his room."
        hide flo stand01 with slow_dissolve
        hide ebb stand with dissolve
        pause 2
        play sound "music/door.mp3"
        show ebb stand at center with slow_dissolve
        pause 2
        eb "Please forgive the young master’s... demeanour."
        eb "He is a very noble gentleman actually."
        e 1 "I know it isn’t my business to pry, but are you two going to be ok?"
        e 13 "He didn’t seem that enthusiastic to come back here."
        eb "..."
        eb "Well, I think the young master is just in shock."
        eb "He just needs some rest."
        eb "Now before I forget."
        eb "Here, it isn’t much but take it as a reward for helping us out."

        "<You receive 500 coins from Ebb>."
        $ jane_inv.take(coin,500)
        "<[name] gained two Level-up-points.>"
        $ Zalt.points = Zalt.points +2
        $ Flo.room = 1
        e 1 "Thanks, I’ll head back to the tavern."
        e 1 "You’ll know where to find us if you need anything."
        eb "Of course, thank you again Master [name]."
        "You return to the tavern exhausted from today’s events."
        jump forest_map0



    elif Flo.meet == -1:

        "Upon reaching the dorosteps to Ebb’s hut, you just stand there, lost and afraid."
        "You failed to keep your promise."
        "It’s a struggle to even knock on the door, as though you have ice in your veins, choking you, but you know well that is the guilt you feel."
        "Knock. Knock."
        "Ebb answers the door."
        play sound "music/door.mp3"
        "He looks at you hopefully for a second, but he is quick to realize you are on your own."
        "His weak smile breaks, his mouth hands open slightly."
        show ebb stand at center with slow_dissolve
        eb "Where... where is the young master?"
        "His voice breaks near the end, the tears are building in him."
        pause 3
        e 13 "I... I’m sorry Ebb."
        pause 3
        eb "No... say it isn’t so. Please say it isn’t so."
        hide ebb stand at center with slow_dissolve
        "He grabs you by the shoulder and shakes you violently."
        "The tears start flowing down his cheeks."
        eb "No... no...no. YOUNG MASTER!"
        "His hold on you weakens as he collapses to his knees crying."
        "There’s nothing you can say."
        eb "I failed you! Why gods why? AGGGHHHH!"
        e 9 "Ebb-"
        eb "No! Leave, please... just leave me be..."
        play sound "music/door.mp3"
        "You lower your head."
        e 13 "I’m sorry."
        "With that you leave, the sound of Ebb’s tears echoes through the silent woods as you make your way back to the tavern."
        $ Ebb.cry = Time.days
        jump saveflo_end
    elif True:
        "bug"

label saveflo_end:
    scene black with dissolve
    $ Ebb.tavern = 1
    $ Zalt.hp = Zalt.maxhp
    $ Zalt.mp = Zalt.maxmp
    if Time.hours >=21:
        $ Time.days = Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
    elif True:
        $ Time.hours = 6
        $ Time.mins = 30
    stop music
    "Feeling exhausted from the day’s events, you head straight to sleep."
    pause 3
    "The next day."
    play sound "music/door.mp3"
    pause 1
    scene tavern 1 with slow_dissolve
    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
    "When you reach the foot of the stairs, Witer pulls you to the side."
    show witer stand at center with dissolve
    w "Hey sweetie."
    e 6 "Hey Witer, what’s up?"
    w "I saw you yesterday, and you looked worse than the broken toy my youngest brother found in the dump."
    "You scratch the back of your neck."
    e 6 "It’s not a big deal."
    w "Don’t give me that. We’re in a magical foggy forest full of monsters."
    w "Everything is a big deal."
    e 1 "Well-"
    h "Hey, you asked him yet what’s bugging him?"
    show hakan stand at left with dissolve
    show witer stand at right with dissolve
    "Hakan suddenly appears behind you."
    "Witer puts his hands on his hips and shakes his head at Hakan."
    w "I was just getting to it before you came."
    c "So you know what’s bugging [name] now?"
    "Now Chet pops out from his spandrel and joins in on the conversation."
    e 1 "Ok, who else wants to know what happened to me? "
    "Snow then pops out from under the bar and everyone looks at him."
    s "What? I dropped a spoon, honest."
    e 13 "Alright, everyone gather around. It’s a long story."
    hide hakan stand at left with dissolve
    hide witer stand at right with dissolve
    scene black with vslow_dissolve
    "After everyone gathers, you share with them your whole adventure in the city of demons, the auction, and what happened to Flo."
    pause 3
    scene tavern 1 with slow_dissolve
    if Flo.meet == 1:
        show hakan stand at left with dissolve
        show witer stand at right with dissolve
        w "Wait, wait, wait."
        w "So, there is an actual city full of demons? This is insane!"
        w "What if they come after us? Oh, no."
        h "Then I’ll cut them in half before they even set an inch on tavern grounds."
        h "We’ve got to start having patrols again."
        hide witer stand at right with dissolve
        show snow stand1 at right with slow_dissolve
        s "Agreed, now we know there is a possible threat we have to be prepared."
        s "For all we know they could be the ones behind the fog."
        e 1 "I haven’t got a chance to find out about the fog from them."
        s "Then you’ll have to, somehow."
        s "They’ve let you in, they probably don’t see you as a threat."
        s "Gain their trust, learn what you can about what’s going on with the fog."
        e 1 "I’ll see what I can do."
        s "In the meantime, I’ll set up night time patrols for the rest of us."
        c "We probably should do something about the orca and the shark guy."
        c "It isn’t safe for them to be out there on their own."
        e 1 "I agree, maybe they can stay here?"
        show snow stand1 at right with dissolve
        s "I won’t mind, but I’m running a business."
        s "They’d have to pay for lodgings like anyone else."
        s "[name], you can invite them over. Say I want to talk to them."
        e 6 "Alright."
        jump map1
    elif True:
        "Everyone sits in silence when you tell them that you could not save Flo."
        show hakan stand at left with dissolve
        show snow stand at right with dissolve
        w "[name]..."
        h "Don’t blame yourself Fuzzbutt, you did everything you could."
        e 13 "Did I? I’m more worried about Ebb."
        "Snow puts a hand on your shoulder, and pats you reassuringly. "
        s "Then go to Ebb. We shouldn’t leave him alone at a time like this."
        s "Just as important, we now know there are literal demons walking among us."
        s "This changes things. We need to be more vigilant from here on in."
        s "I’m restarting the night patrol, while [name] learns if these demons have anything to do with the fog."
        e 1 "You’re not really asking me to go back there?"
        s "I am, because it’s the only suspect we have for now. Please, it’s all we have."
        "You close your eyes, and see Flo’s horrified face from before."
        "You breathe deeply."
        e 1 "Ok, I’ll get in and learn what I can."
        s "Good. Then for now, go see Ebb. Convince him to come to the tavern."
        e 1 "Alright."
        hide snow stand at right with dissolve
        hide hakan stand at right with dissolve
        jump map1




    jump map1
label Ebb_hang:
    $ Map.bathroom_0 = 1
    $ Ebb.room = 0
    $ Flo.room = 0
    $ Ebb.tavern = 2
    $ EF.meko = 1
    if Flo.meet == 1:
        $ EF.witer = 1
        $ EF.hakan = 1
        play sound "music/door.mp3"
        "You hurry to the shark and orca’s hut."
        "They are surprised to see you back so soon."
        if Time.hours >= 6 and Time.hours <= 17:
            scene cabin 1 with slow_dissolve
        elif True:
            scene cabin 1n with slow_dissolve
        show flo stand with slow_dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        show ebb stand at right with dissolve
        eb "Master [name], welcome."
        f "[name], what brings you here?"
        e 1 "I’ve got a proposal from Snow."
        e 1 "He wants to invite you guys to stay in the tavern."
        e 1 "We would all be safer together and since the hut has been attacked before it might not be as safe."
        e 6 "And we have a few tavern mates already, everyone is nice."
        f "I take it we won’t be living there for free?"
        e 6 "Yeah... but knowing Snow he lets people stay if they are willing to work."
        eb "I think it would be a great idea, this will give young master the perfect chance to make friends."
        "Flo smacks himself in the forehead with his hand."
        show flo stand01 with dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        f "Orca, please don’t embarrass me."
        eb "..."
        eb "Sorry, young master."
        show flo stand with dissolve:
            xpos -0.1 ypos 0
            xzoom -1
        f "More importantly, I think moving is a good plan."
        f "Give us a few minutes to pack?"
        hide flo stand with dissolve
        hide ebb stand with dissolve
        scene black with slow_dissolve
        "You wait for Ebb and Flo to get their things before heading back to the tavern."
        pause 5
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0, 2, channel = "Chan1")
        scene tavern 1 with slow_dissolve
        play sound "music/door.mp3"
        play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
        "When you reach the tavern, you give the duo a quick introduction of everyone present."
        "Snow warmly greets the duo as well."
        show snow stand at left with dissolve
        show ebb stand at right with dissolve
        eb "The pleasure is ours Master Snow."
        hide ebb stand at right with dissolve

        show flo stand with slow_dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        f "Thank you for offering us shelter, we would be honoured to be among your staff."
        s "So polite for a young shark. Your parents raised you well."
        show flo stand01 with dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        pause 1
        show flo stand with slow_dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        f "Yeah..."
        "The tail fin on Flo’s head starts twitching."
        s "Is something wrong?"
        f "Oh no-"
        hide flo stand with dissolve
        "Flo grabs hold of his tail fin with both hands."
        show flo stand with slow_dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        f "It does that when it’s near a hot spring source, it’s an ability my family has had naturally."
        s "Really? Then that means, there’s a hot spring nearby!"
        f "I think so, it’s very close to get my fin to vibrate like this."
        s "Then I think I have the perfect job for you two."
        s "We’ll go and dig up this hot spring and extend the bath house so that we can fill it with the spring water."
        s "You both can run the bath house business, and I’ll take the payment from the work there as payment for room and board."
        s "Think you can handle running your own bath house business?"
        eb "We would be happy to help."
        show snow laugh at left with dissolve
        s "Great, then you can start with the bath house construction with us."
        s "We’ve got the tools and we can use the man power."
        show flo stand01 with slow_dissolve:
            xpos 0.35 ypos 0
            xzoom 1
        f "Hmm..."
        show snow stand at left with dissolve
        s "Yes Flo?"
        f "Do I at least get my own room?"
        show snow stand1 at left with dissolve
        s "Oh, don’t you want your butler with you at all times?"
        f "Please, it’s bad enough I got to work with him."
        f "I would really appreciate having some privacy."
        "Ebb lowers his head upon hearing his young master does not want to be with him."
        s "No problem, the bath house has enough empty rooms for both of you and the supplies to run the place."
        s "In fact lets get you two to your rooms, and start working."
        hide snow stand1 at left with dissolve
        hide flo stand01 at left with dissolve
        "Snow escorts the both of them to the bath house."
        "Maybe you should ask Snow about the bathroom later."
        play Snow "music/char_snow.ogg"
        play Hakan "music/char_hakan.ogg"
        play Witer "music/char_witer.ogg"
        play Chet "music/char_chet.ogg"
        play Thane "music/thane.ogg"
        $ Map.bathroom = "EbbFlo"
        jump map1
    elif True:
        $ renpy.music.set_volume(0, 0.1, channel = "Chan2")
        $ renpy.music.set_volume(0, 5, channel = "Chan1")
        "You reach the hut that Ebb lives in."
        "The door is unlocked so you step in."
        play sound "music/door.mp3"
        if Time.hours >= 6 and Time.hours <= 17:
            scene cabin 1 with slow_dissolve
        elif True:
            scene cabin 1n with slow_dissolve
        e 1 "Ebb? Ebb I came to check- "
        pause 5
        "You could not speak."
        scene black with slow_dissolve
        "The sight before you was a kind of horror that could never be truly understood fully by any living person."
        "It’s the kind of sight that the mind instantly reels back the moment it confronts it."
        "Dozens upon dozens of reasons could be theorized as to how such a tragedy could happen, but none could fully satisfy."
        "It is the kind of tragedy that no one would wish on another person or to the people around them."
        "One could only wish that help was given before such a tragedy befell."
        "But for now, you know this. Ebb ended his life by way of hanging."
        if jane_inv_K.qty(ebb_necklace) == None:
            pass
        elif True:
            $ jane_inv_K.drop(ebb_necklace)
            "You place the necklace the orca gave you inside his grave."
            "It didn’t feel right to hang on to it."
        "After burying his body you leave the hut feeling broken."
        "You cannot recall the walk back to the tavern."
        "Everything is so hazy."
        "Your conscience weighs heavily upon your shoulders."
        pause 5
        scene tavern 1 with slow_dissolve
        "When you arrive at the tavern, you tell everyone what happened."
        "Nothing. Not one of them said anything. "
        "Witer walks over and hugs you."
        "He tries to reassure you that it isn’t your fault, but all you feel is hollow."
        scene black with vslow_dissolve
        "You take a day off from exploring to collect yourself."
        pause 5
        $ Time.days = Time.days+1
        $ Time.days = Time.days+1
        $ Time.hours = 6
        $ Time.mins = 30
        "With the time you have, you convince yourself that you need to continue the search for freedom, despite everything."
        "You need to move forward, for those who remain."
        pause 3
        play sound "music/door.mp3"
        scene tavern 1 with slow_dissolve
        play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1

        "When you enter the tavern everyone goes about their business as usual."
        "You are unsure if they are putting up a front to retain some form of normalcy or that one more death means nothing when every day someone is bound to die in this forest."
        "Snow calls you to the counter."
        e 1 "Hello Snow."
        show snow stand1 at center with dissolve
        s "Good to see you are up and about."
        s "There’s something I wanted to share with you."
        s "It’s about the services in the tavern."
        s "With recent events, I think it’s more important now to provide a place for the customers to unwind, and more importantly to not stink up my bar."
        e 6 "Are you talking about a toilet?"
        show snow stand at center with dissolve
        s "No, we already have that. I mean reopening the bath house."
        s "We were fortunate this morning, Witer was helping move out some things from the bath house, mostly junk to be buried. "
        s "While we were digging, Witer actually discovered a source of natural hot spring water."
        s "So it’s been decided that the bath house will be renovated so that everyone can use the hot spring."
        s "Once it's ready, you can be the first customer."
        e 13 "That does sound nice, thanks Snow."
        s "Hey, take it easy kid. You’ve been through a lot lately."
        s "The guys and I talked, and we figure we best keep things normal for you."
        e 1 "I know, just give me some time. I don’t want you guys to worry too much either."
        s "Promise you’ll talk to us if something is bothering you?"
        e 13 "I promise."
        s "Good."
        hide snow stand at center with dissolve
        "Maybe you should ask Snow about the bathroom later."
        play Snow "music/char_snow.ogg"
        play Hakan "music/char_hakan.ogg"
        play Witer "music/char_witer.ogg"
        play Chet "music/char_chet.ogg"
        play Thane "music/thane.ogg"
        $ Map.bathroom = "None"
        jump map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
