label camp_map:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    $ renpy.music.set_pause(True, channel='Axel')
    $ renpy.music.set_pause(True, channel='Thane')
    $ renpy.music.set_pause(True, channel='Nauxus')

    $ Time.mins = Time.mins +10
    window hide None
    stop music fadeout 1
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Quest.campb == 4 or Quest.campl == 4:
        scene black with dissolve
        "You rest for a night."
        "The next day.."
        if Quest.campb == 4 and Quest.campt != 4:
            $ Time.days = Time.days+1
            $ Time.hours = 11
            $ Time.mins = 10
        elif True:
            $ Time.days = Time.days+1
            $ Time.hours = 10
            $ Time.mins = 30
    if Time.hours >= 6 and Time.hours <= 17:
        scene forest 6 with dissolve
        play music "music/bird1.ogg"
    elif True:
        scene forest 6n with dissolve
        play music "music/bird1n.ogg"
    if Quest.campb == 4 or Quest.campl == 4:
        $ Quest.camp_n = 1
        $ Quest.camp_a = 1
        if Quest.campt == 4:
            if Quest.campb == 4:
                "Your party travels through the fog with you leading at the front. The fog gets thicker as you approach the campsite."
                "Something about the way the trees all bend to one direction makes the forest feel more unsettling than it already is."
                "The bulls behind you chat and joke with one another, unphased by where they are."
                "Upon nearing the campsite you turn to your team. "
                e 1 "The lizards are probably here by now, I’ll go ahead to scout out how many there are. When I whistle, just charge in."
                "The bulls nod and grin at each other. There’s excitement in their eyes at the prospect of fighting off some lizards."
                "You shake your head and make your way deeper inwards."
                "Just as you approach the campsite, you make out the shadows of lizard warriors gathered together."
                "You duck and quietly sneak into a bush."
                "They don’t seem to notice you, what are they doing?"
                "First Lizard Guard" "Hmm, how do we know if it’s working?"
                "Second Lizard Guard" "Beats me, I don’t know anything about this magic stuff."
                "Second Lizard Guard" "Selye just said to think about not letting those who wants to harm the lizards in."
                "Third Lizard Guard" "Hurry up, we’ve got two more runestones to plant."
                "This isn’t good, they’re almost done with their plans."
                "You let out a high pitch whistle in the direction of the bulls."
                "The lizards all turn towards your bush."
                "First Lizard guard: What the heck is that?"
                "Second Lizard Guard" "Never mind that, look!"
                "The ground shakes and out from the fog the bull warriors arrive brandishing their axes."
                "First Bull Warrior" "Hey, where’s the leader?"
                "Second Bull Warrior" "The lizards probably got him."
                "Third Bull Warrior" "You swamp trash!"
                "Without hesitation you toss the vial of Fear Potion from your spot, the bottle lands between the two groups and spills the content inside."
                "The potion evaporates instantly and a noxious odour fills the air."
                "Both sides stand frozen in place, staring blankly into space."
                "You cover your nose from the stench of rotten eggs and death."
                "Then, a lizard screams."
                "First Lizard Guard" "A giant wolf! Get out of the way."
                "His body suddenly spasms and he flips backwards crashing into a nearby tree."
                "Second Lizard Guard" "The wolf kicked him like a doll! We gotta get out of here."
                "The other lizards grab their unconscious friend and run off in the direction of the lizard village."
                "Your team of bulls aren’t doing so well either. They’re running in circles from an imaginary enemy."
                "Second Bull Warrior" "Come on, let’s just run!"
                "The bulls run off back to the village."
                "The coast looks clear, you step out of the bushes still covering your nose."
                e 1 "Thank goodness it worked. I better head back to Selye and Nauxus, but first-"
                "You take a deep breath and clench your right fist tightly."
                show red1 at center with dissolve
                "Steeling your resolve you punch yourself in the left eye. The force knocks you on your butt." with vpunch
                e 0 "Not yet. "
                show red2 at center with dissolve
                "You brace yourself again before punching yourself in the stomach as hard as you can." with vpunch
                "You wheeze and cough from the impact."
                "<You lose half of your HP>"
                scene black with slow_dissolve
                hide red1
                hide red2
                "Slowly picking yourself back up you clutch your stomach and make your way towards the bull tribe."
                "...."
                "......"

                $ Zalt.hp = Zalt.hp/2
                $ Quest.campb =5
                $ Quest.campt =5
                $ Axel.s = Axel.s + 2
                $ Nauxus.s = Nauxus.s + 1
                $ Quest.campw = 1
                $ Quest.campw1 = 1
                $ jane_inv_K.drop(Fear_potion)
                $ Thane.help = Thane.help +1
                jump Axel_camp_end

            elif Quest.campl == 4:
                "Your party travels through the fog with you leading at the front. The fog gets thicker as you approach the campsite. "
                "Something about the way the trees all bend to one direction makes the forest feel more unsettling than it already is."
                "The lizards behind you remain ever vigilant through your journey to the campsite."
                e 1 "We’re about to approach the campsite."
                e 1 "I’ll head ahead to scout the area. I’ll come back to get you guys if it's clear. "
                "Your team nods in understanding and head behind a tree to rest."
                e 13 "(Ok, everything’s working so far. Just need to get into position.)"
                "You travel inwards until you come upon a clearing with."
                "Thick bushes surround the empty space. "
                e 1 "This spot will do. "
                "You hide inside one of the bushes and lay waiting for the moment to strike."
                "Minutes pass, and you hear the lizards approaching from your right."
                "First Lizard Guard" "Where is he?"
                "Second Lizard Guard" "Did he get eaten by something?"
                "Third Lizard Guard" "Look!"
                "The third lizard guard points across them."
                "Large, heavyset figures break through the fog."
                "It’s Tomahawk and his gang!"
                "Tomahawk" "Look at what we found boys.This trip’s going to pay off."
                "You don’t give the two sides any opening to attack each other. From the bushes you toss out the vial."
                "The glass container shatters, its contents spills onto the dirt ground and instantly a noxious odour fills the air."
                "Neither side are moving. They’re just spacing out."
                "You cover your nose."
                "The smell of rotten eggs and death permeates the air, your eyes practically watering but you can’t move from your spot."
                "Through the leaves you see the potion take its effects."
                "The lizards and bulls are screaming in terror all while pointing and running away from an imaginary foe."
                "First Lizard Guard" "It’s a giant wolf! Run! Run!"
                "Tomahawk" "Ahh! It’s going to eat me. No!"
                "Tomahawk’s body suddenly convulses and his whole body suddenly flips in the air and lands with a loud crash."
                "First Bull Warrior" "Boss! We got to get out of here."
                "Second Bull Warrior" "Retreat! Don't let the giant wolf get you."
                "The bull warriors grab their fallen leader and make a hasty retreat back to their village."
                "Second Lizard Guard" "Let's get the heck out of here!"
                "Your team follows suit and runs back in the way they came."
                "The coast looks clear, you step out of the bushes still covering your nose."
                e 1 "Thank goodness it worked. I better head back to Selye and Nauxus, but first-"
                "You take a deep breath and clench your right fist tightly."
                show red1 at center with dissolve
                "Steeling your resolve you punch yourself in the left eye. The force knocks you on your butt." with vpunch
                e 0 "Not yet. "
                show red2 at center with dissolve
                "You brace yourself again before punching yourself in the stomach as hard as you can." with vpunch
                "You wheeze and cough from the impact."
                "<You lose half of your HP>"
                scene black with slow_dissolve
                hide red1
                hide red2
                "Slowly picking yourself back up you clutch your stomach and make your way towards the lizard tribe."
                "...."
                "......"
                $ Zalt.hp = Zalt.hp/2
                $ Quest.campl =5
                $ Quest.campt =5
                $ Nauxus.s = Nauxus.s + 2
                $ Axel.s = Axel.s + 1
                $ Quest.campw = 2
                $ Quest.campw1 = 2
                $ Thane.help = Thane.help +1
                $ jane_inv_K.drop(Fear_potion)
                jump Nauxus_camp_end
        elif True:

            $ Quest.camp_n = 1
            $ Quest.camp_a = 1
            if Quest.campb == 4:
                $ Nauxus.s = Nauxus.s + 3
                $ Quest.campw1 = 3
                $ Quest.campw = 3
                "Lead with the location of the campsite on your map, you and the four bulls travel through the foggy forest."
                "The others seem confident in the mission, joking around about how they would fight off the lizards."
                "They try to include you in the conversation, but you find it difficult to share about your favourite ways to end enemies."
                "You notice the trees as you approach the campsite, they all bend towards one side as though leading you to where you need to go."
                "In the distance you can make out voices coming from the campsite."
                "You sign to the other bulls to be quiet and to sneak along with you, using the dense bushes around the camp area to conceal your presence."
                "Through the thick fog you can make out three lizard warriors talking to each other."
                "First Lizard Warrior" "I can’t believe this thing would work."
                "Second Lizard Warrior" "Yeah, all we have to do is think about not letting any of our enemies into the area and the stone glows. It’s too easy."
                "Third Lizard Warrior" "Magic is convenient. We better hurry and set up all the stones around the area."
                "Third Lizard Warrior" "I don’t like the feel this fog is giving me."
                "They’re doing something with stones? Something to do with blocking others out from the area."
                "No time to waste, if they really are setting up a barrier you have to take them out now."
                "You signal to the group to rush them."
                "The bulls nod and stampede in with their axes ready. "
                "Caught off guard, the lizards are unprepared for the attack and narrowly escape the heavy bashing of the bulls."
                "You join the fight, with two bulls taking on one lizard, leaving you to deal with the third."
                "Third Lizard Warrior: You!"
                "You don’t give him the chance to speak, as you strike him with your blade."
                jump battle_lizardcamp

            elif Quest.campl == 4:
                "You and the three lizard guards follow the map to the proposed campsite location."
                "The fog feels eerily thick around here. "
                "You notice the trees as you approach the campsite, they all bend towards one side as though leading you to where you need to go."
                "Upon arrival at the campsite, you pull out one of the rune stones Selye gave you."
                "You turn to the other lizard guards."
                e 1 "I’ll start planting these runestones around."
                "Keep an eye out for anything that might be coming towards us."
                "They nod in response."
                "The campsite is a wide open area wide enough to build a house on it."
                "Thick and dense bushes surround this clean area."
                "You pinpoint four locations to plant the runestones."
                play sound "music/foot1.ogg"
                "Getting on one knee you hold the rune stone between your fingertips and begin to concentrate."
                "Images flash through your mind but you try to focus on the idea that anything that would want to harm the lizards and their allies need to be kept out."
                "You stare at the stone focusing completely on protecting the lizard tribe."
                "Behind you the guards are whispering to each other, wondering what you’re doing."
                with flashbulb
                "Suddenly you feel dizzy, and it looks as if the stone is draining your energy"
                e 5 "Wha-"
                "<You lose half of your HP>"
                $ Zalt.hp = Zalt.hp/2
                "The runestone heats up and a bright orange glow surrounds it."
                e 9 "I guess this means it’s on? "
                scene black with dissolve
                "You dig a hole and bury the runestone."
                play sound "music/foot1.ogg"
                scene forest 6 with dissolve
                "With the first stone buried you walk across from it until you reach a tree."
                with flashbulb
                e 9 "Ahhh"
                "First Lizard Guard" "Are you okay?"
                "<You lose half of your MP>"
                e 13 "This stone,just..let's hurry."
                $ Zalt.mp = Zalt.mp/2
                "Again you repeat the same steps as before and the stone glows."
                play sound "music/foot1.ogg"
                "Just as you are ready to head to the third point. A lizard guard shouts at you."
                "First Lizard Guard" "Look out! Behind you, it’s the bulls!"
                show bullw at center with dissolve
                "A bull leaps from the fog brandishing his axe."
                "The blade of the axe narrowly misses your foot as it comes crashing down upon you."
                "Leaping backwards, you draw your weapon."
                "First Bull Warrior" "Well boys, we came looking for lizards, but we found something much more interesting."
                "Second Bull Warrior" "You’ll pay for siding with them.Trai-"
                "You launch yourself forward and punch the bull in the jaw."
                "The lizards rush in and engage him in a fight."
                "Second Bull Warrior" "Argh! I’ll kill you all."
                "Amidst the chaos you’re quick enough to notice the first bull charging at you. "
                "You slide to the right and slash at him, but he dodges."
                "You can’t let the bulls report this back to Chief Axel, don’t let any bulls survive!"
                $ Quest.campw1 = 4
                $ Quest.campw = 4
                $ Axel.s = Axel.s + 3
                jump battle_bullcamp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
