label Temple_map:
    stop Thane
    $ renpy.music.set_volume(1, 5.5, channel = "music")
    $ Time.mins = Time.mins +10
    window hide None
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1

    if Time.hours >= 6 and Time.hours <= 17:
        scene temple 1 with dissolve
    elif True:
        if Thane.temple == 2:
            $ Thane.temple = 3
            $ Map.t8 = 2
            scene temple 1 with dissolve
            "Thane walks over to the pile of camp equipment and grabs a few mats and blankets."
            t "Just make the tent cozy for us, I’ll go get our dinner and some firewood."
            e 1 "That sounds like you’re doing most of the work."
            t "Oh, right I’m so used to being told to do this, kinda flew over my head that you’re here."
            t "Then you’ll set up the campfire and the camp, and I’ll get the food."
            "You give Thane a thumbs up and follow him out of the temple."
            "He makes his way around the lake facing the back of the temple. "
            "You on the other hand drop off the mats and blankets at the campsite before beginning your search for some tinder and kindle."
            "The process takes longer than expected due to the cooler climate up on the mountain."
            "By the time you have the fire started your hands are sore from all the wood rubbing you had to do."
            "You slump back onto the ground to enjoy the warmth of your hard work."
            "Just then, your ears perk up to the sound of dripping water. "
            "Thane appears from behind soaked from head to toe."
            "In his right hand he holds four fishes that appear to have been gutted and cleaned. "
            e 5 "What happened to you?"
            "You ask bewildered by his appearance."
            "He gives you a look with his eyes half closed then he looks away before he speaks to you."
            t "I err, speared a fish and thought it was dead... I was wrong."
            t "It slapped me in the face with its tail and I fell into the lake."
            "You accidentally let out a chuckle."
            t "..."
            e 3 "Hahaha. I'm sorry. I just... hahaha."
            "Thane snorts and drops the fish on the ground."
            "He pulls you to your feet by the shoulders and traps you in a tight bear hug."
            e 10 "Waah!"
            "After a brief tussle with Thane you two finally get down to cooking the fishes. "
            $ renpy.music.set_volume(0.5, 5.5, channel = "music")
            scene temple 1n with vslow_dissolve
            "Night time comes before the two of you even notice."
            "Thane sits across you from the campfire, lying on his back watching the skies."
            "The stars shine bright across the silent night's sky."
            "It feels like you're the closest you've ever been to touching those sparkling spheres in the sky."
            "You feel completely exhausted from your day's events."
            "You wonder if Thane feels the same."
            t "Hey."
            e 1 "Yeah?"
            t "What do you think of the place?"
            e 1 "I have tons of questions to ask. It's nothing like anywhere I've been before."
            t "Yeah. What you wanna know about?"
            menu:
                "The glowing spring" if Map.t7 >= 2:
                    e 1 "What's with the glowing spring, it looks different from the rest of the lake."
                    t "Mmmm. Well it's what we believe can cure a person of their corruption?"
                    e 1 "Corruption? What's that?"
                    t "We're told from young that certain creatures they corrupt us from the inside."
                    t "If we ever lose to them in battle or if they infect our minds when we are most vulnerable."
                    e 1 "What does that mean though?"
                    t "Not sure myself, the elders say if we get too corrupted it be easier for those with dark magic to manipulate us."
                    t "Like take away our free will or worse."
                    e 1 "So, the spring it-"
                    t "It washes the corruption once, but I have never seen anyone use it before though."
                    e 13 "Losing to monsters huh, have I been corrupted?"
                    "You whisper softly to avoid Thane from hearing you."
                    t "Anyways, I think I'll head to sleep. I am fucking beat."
                    e 5 "Oh... ok, I'll take first watch."
                    t "Thanks."
                    scene black with slow_dissolve
                    "And so the night ends with you both taking turns watching over the fire and for any danger."
                    "Fortunately, nothing happens."
                "The people who lived here before" if True:
                    e 1 "I'm really curious about who were the people who lived here."
                    e 13 "I mean why is the temple like this?"
                    e 13 "What did they use this place for before?"
                    t "I can't tell you much, man."
                    t "I remember the books in the back room made reference to mages."
                    t "But it could even be just a group of people who collect those books."
                    e 1 "Yeah,man I wish I could find out more."
                    t "Well you do that, and I'll head to sleep."
                    e 1 "Ok, I'll take first watch."
                    t "Thanks."
                    scene black with slow_dissolve
                    "And so the night ends with you both taking turns watching over the fire and for any danger."
                    "Fortunately, nothing happens."
                "The back room" if Map.t4 >= 2:
                    e 1 "What's with the back room?"
                    t "The back room? Nothing really."
                    t "It's just a room with damaged books."
                    t "I mean there is that odd partition that seems to not fit with the rest of the wall."
                    t "But last time we tried to break it down, the wall just reformed itself."
                    e 5 "Woah, that’s some insane magic then."
                    e 5 "There’s got to be something there then?"
                    t "Maybe,but no one has been able to undo it because there are no mages in our tribe."
                    t "So we just decided to leave it be. It's not like it's hurting anyone."
                    e 1 "Right."
                    t "Anyways, I think I'll head to sleep. I am fucking beat."
                    e 1 "Oh... ok, I'll take first watch."
                    t "Thanks."
                    scene black with slow_dissolve
                    "And so the night ends with you both taking turns watching over the fire and for any danger."
                    "Fortunately, nothing happens."
            stop music fadeout 1
            "The next day, you both make your way down the mountain before the break of dawn."
            $ Time.days = Time.days+1
            $ Time.hours = 9
            $ Time.mins = 30
            $ Thane.quest = 7
            $ Quest.campb = 1
            $ Quest.campl = 1
            if Time.bull == 9999 and Thane.quest == 7:
                $ Time.bull = Time.days
            if Time.lizard == 9999 and Thane.quest == 7:
                $ Time.lizard = Time.days
            play sound "music/foot1.ogg"
            scene mountain 1 with slow_dissolve
            ""
            play sound "music/foot1.ogg"
            scene bulltribe 1 with slow_dissolve
            ""
            scene tent 1 with slow_dissolve
            show thane stand at center with dissolve
            t "Thanks for keeping me company up there."
            e 1 "You're welcome, it was fun."
            e 1 "You think I could go back up there to explore?"
            t "As long as Chief Axel stays friendly with you, you should be fine."
            t "Just be mindful of the time to enter the temple"
            e 1 "Ok, thanks."
            t "I'll head back to my hut and sleep a bit more."
            t "You can find me near the chief’s tent later."
            jump Bull_tribe_map0
        elif True:


            scene temple 1n with dissolve
    call screen temple_map with dissolve
    if _return == 'mountain':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        play music [ "<silence 1.0>", "music/bulls_mountain_path.ogg" ] fadein 1
        jump Mountain_map
        return

    if _return == 'point 1':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.t1 == 0 and Time.hours >= 6 and Time.hours <= 17 and Thane.temple == 1:
            t "This is the camping grounds where we’ll be spending the night together."
            t "He points to an erected tent. It looks ancient like it has been here for many years."
            t "In front of the tent is a dirty burnt spot on the ground, probably where the campfire should be."
            e 1 "There’s barely anything here, and we definitely didn’t pack anything to get us through the night."
            t "Don’t worry, there are mats and blankets kept inside the temple."
            e 9 "It be easier to sleep inside the temple, compared to...this."
            "You point towards the tent with a worried expression."
            t "It would but it defeats the purpose of this place."
            t "The temple is the seat of the great power that emanates upon the peak of this mountain."
            t "It is to be respected."
            e 6 "I didn't think of that."
            "Thane walks off towards the temple and you follow from behind."
            $ Map.t1 = 1
            $ Map.t2 = 1
            jump Temple_map
        elif Map.t1 == 0 and Time.hours < 6 or Time.hours > 17 and Thane.temple == 1:
            t "It’s dark and we can’t go inside the temple until sunrise."
            e 5 "Seriously? Who made such a weird rule."
            t "The temple did. We literally cannot go inside."
            e 3 "You’re just messing with me for the tip thing aren’t you."
            "You walk over to the temple entrance but just as you set foot inside, your entire sense of time and space feels distorted."
            "Just as you blink you find yourself facing Thane, and the temple entrance is behind you."
            e 5 "Huh? "
            "He looks at you with a tired expression on his face."
            t "See, you’re just wasting your time."
            t "No one can go in until there’s sunlight."
            t "You can try again, the temple will just turn you around."
            e 13 "Good grief, fine! We’ll wait for sunrise."
            scene black with slow_dissolve
            "Thane leads you to the tent in the campsite and you both rest until morning comes."
            "Because you are too tired, you fall asleep very soon."
            $ Time.days = Time.days+1
            $ Time.hours = 6
            $ Time.mins = 30
            "..."
            "......"
            scene temple 1 with slow_dissolve
            "And it's the next day."
            "You climb out of the tent and found that Thane was already waiting for you outside."
            $ Map.t1 = 1
            $ Map.t2 = 1
            jump Temple_map
        elif True:
            "Here is the tent."
            menu:
                "Rest" if True:
                    scene black
                    "You sleep for 3 hours, feel refreshed and full of energy."
                    "HP and MP have been restored half of the maximum."
                    $ Zalt.hp = min(Zalt.hp+Zalt.maxhp/2, Zalt.maxhp)
                    $ Zalt.mp = min(Zalt.mp+Zalt.maxmp/2, Zalt.maxmp)
                    $ Time.hours = Time.hours+3

                    jump Temple_map

                "Sleep" if Time.hours < 6 or Time.hours >=21:
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

                    jump Temple_map
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

                    jump Temple_map
                "Уйти" if True:
                    jump Temple_map

            jump Temple_map
        return
    if _return == 'point 2':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.t2 == 1 and Time.hours >= 6 and Time.hours <= 17:
            e 1 "Finally, we get to see what’s inside this weird temple."
            t "Well I’m glad you’re enjoying being here."
            "Thane walks ahead."
            $ Map.t2 = 2
            $ Map.t3 = 1

            jump Temple_map
        elif True:
            "You walk over to the temple entrance but just as you set foot inside, your entire sense of time and space feels distorted."
            "Just as you blink you find the temple entrance is behind you."
            $ Map.t2 = 2
            jump Temple_map
        return
    if _return == 'point 3':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "Your eyes glisten as you enter the temple."
        "The walls that looks so pristine almost ethereal from far away is actually stained by dirt. "
        "Just from standing in the middle of the foyer your mind runs with questions about what this temple once was in its glory days."
        "Nothing remains of this place now."
        "Thane looks towards a doorway in front of him, his broad back facing you."
        "He turns to face you with a serious expression."
        t "I’ll be meditating in the room behind me."
        t "It’s the prayer hall. To your left is the back room, it houses some old books that we believe belonged to whoever owned this temple."
        t "And over there-"
        "He points to the right."
        "That's a tree."
        e 1 "Remarkable."
        "Thane turns to face you. His hands on his hips."
        t "You’re welcome to join me for my meditation if you have nothing to do."
        t "When I’m done we’ll get ready for the night."
        e 1 "Alright, I’ll see you later."
        "Thane heads for the prayer room leaving you alone to do your own thing."
        $ Thane.temple = 2
        $ Map.t3 = 2
        $ Map.t4 = 1
        $ Map.t7 = 1
        jump Temple_map
        return
    if _return == 'point 4':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "You enter the back room, it is just a small musty room only slightly larger than your bedroom in the tavern."
        e 1 "Cabinets of old books, maybe there’s some hidden treasure map or something in them."
        $ Map.t4 = 2
        $ Map.t5 = 1
        $ Map.t6 = 1
        jump Temple_map
        return
    if _return == 'point 5':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        jump Temple_book
        return
    if _return == 'point 6':
        $ Time.mins = Time.mins +20
        play sound "music/foot1.ogg"
        if Map.t6 == 1 and Map.boss1 < 2:
            "There’s something off about this part of the wall."
            "It looks like someone cut into the wall in the shape of a large door. "
            e 1 "Can I move this?"
            "You press your hands against the alien wall and push as hard as you can."
            "It doesn't budge."
            e 12 "Dang it!"
            jump Temple_map
        if Map.t6 == 1 and Map.boss1 >= 2:
            "There’s something off about this part of the wall."
            "It looks like someone cut into the wall in the shape of a large door. "
            e 1 "Can I move this?"
            "You press your hands against the alien wall and push as hard as you can."
            "It doesn't budge."
            e 12 "Dang it!"
            e 5 "Hmm?"
            "Your ears perk upwards, you hear a high pitched ring."
            e 5 "What the heck is that?"
            "Where's the source of the sound?"
            "It's ring is so loud you swear someone's standing next to you playing the blasted noise."
            "Looking down you wonder is the sound coming from your pouch?"
            "You open it and find the emblem from before, the ring is deafening while the item is in your hands."
            "Suddenly, the partition before you rumbles and fades away, revealing a hidden room."
            e 5 "Woah! Tha- no wait, he’s meditating... and who knows what’s in there."
            e 5 "Maybe even... treasure! But also, maybe a nest for the undead."
            "You return the emblem back into your bag."
            "This could be the big break you need, if there are valuables inside you will at least have something to bring back to the village once this is all over."
            "Then it hits you."
            "Memories of the past days, the note, Meko’s possession, the warning about a spirit among your friends."
            "Your heart sinks a little, so much has been going on lately you nearly forgot that you’re actually trapped in this land of fog. "
            "Now that this emblem has revealed to hide some kind of secret, what do you do with it?"
            "Maybe Chet would know, he’s looking for these, or maybe Snow, he’s the de facto leader of the tavern."
            "You take a deep breath and steady your resolve, for now you’re determined to investigate the room."
            $ Map.t6 = 2
            jump Temple_map
        elif Map.t6 == 2:
            jump Sproom_map
        elif True:
            jump Temple_map

        return
    if _return == 'point 7':
        $ Time.mins = Time.mins +20
        play sound "music/foot1.ogg"
        if Map.t7 == 1:
            "You enter the prayer hall. It’s a wider room compared to the foyer."
            "Unlike the rest of the temple the prayer hall has half a roof covering it."
            "Above the ceiling you can see the remains of the pinnacle you saw from afar."
            if Thane.temple == 2:
                "In the far end of the room you see Thane sitting cross legged in front of a spring."
                "An unusual glow emanates from the pool in front of him."
            "Your pupils widen and you find yourself drawn to the luminous spring."
            if Thane.temple == 2:
                "Tiptoeing quietly you walk around the side of the room until you stand across from Thane."
                "He doesn’t seem to know you’re there. "
            "Looking at the pool the water looks no different from the lake, but what’s making that unusual glow in that one spot? "
            "You scratch your head unable to think of a reason."
            if Thane.temple == 2:
                "Maybe you can ask Thane about it when he is done meditating."
            "You wonder what you want to do now."
            if Thane.temple == 2:
                $ Map.t8 = 1

            $ Map.t7 = 2
            $ Map.t9 = 1
            jump Temple_map
        return
    if _return == 'point 8':
        $ Time.mins = Time.mins +20
        play sound "music/foot1.ogg"
        "Do you want to join Thane in meditation?{p}(This action will push the time into the evening.)"
        menu:
            "Join Thane in meditation." if True:
                "You decide to join Thane in meditation. You move to his side and meditate with him."
                scene black with slow_dissolve
                "..."
                "......"
                "..."
                $ Time.hours = 18
                $ Time.mins = 0
                scene temple 1 with dissolve
                "Thane lets out a loud yawn, breaking your flow of concentration."
                t "Oh, you’re here."
                e 1 "Mmmhmm. How’s the nap?"
                t "I wasn’t napping. I was in a deep meditative state that made it look like I was napping."
                t "Now, come on we better set up camp for the rest of the night."
                t "We’ll head back to the village come morning."
                e 1 "Sounds good."
                jump Temple_map
            "Look around." if True:
                jump Temple_map
        return
    if _return == 'point 9':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        if Map.spring > 0:
            "An unusual glow emanates from the pool."
            "Your pupils widen and you find yourself drawn to the luminous spring."
            "Do you want to drink some water?"
            menu:
                "Yes" if True:
                    if Zalt.cor >0:
                        if Zalt.cor >= Map.spring:
                            $ cor = Map.spring
                            $ Map.spring = max(Map.spring-Zalt.cor,0)
                            $ Zalt.cor = Zalt.cor -cor
                        elif True:
                            $ Map.spring = Map.spring-Zalt.cor
                            $ Zalt.cor = 0
                        "You drink some water and feel the disgusting smell in your body dissipated."
                        "But you find that the light of the spring is weakened."
                    elif True:
                        "You drink some water."
                        "But you didn't feel any effect."
                    jump Temple_map
                "No" if True:

                    jump Temple_map
        elif True:
            "The spring no longer glows and looks just like a regular spring."
            jump Temple_map

        return
    if _return == 'point 10':
        $ Time.mins = Time.mins +30
        play sound "music/foot1.ogg"
        return

label Temple_book:
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Map.t5 == 1:
        "There are several cabinets in here, but many of them are empty or filled with really old looking books."
        "You flip through a few, many are unreadable as some would disintegrate from your touch, if not, the ink used to write in them are barely legible."
        "However, you manage to find three books with a few readable pages in them."
        $ Map.t5 = 2
    elif True:
        "The three books are still there."
    "Do you want to read the books?"
    menu:
        "Read the first book." if True:
            "This book is called, “Art: A Window to Other Worlds,” by Gallahan.No last name."
            "There’s only one page in the end that can be read."
            "{u}{i}In summation, following my mentor, the once great Haylid Stach’s departure from the study of creating new magic.{/i}{/u}"
            "{u}{i}I have taken it upon myself to revive his greatest failure, the Fate Painting Spell.{/i}{/u}"
            "{u}{i}Only this time, I’ve altered the spell to allow the mage to travel to different and far off worlds.{/i}{/u}"
            "{u}{i}The risks are there-{/i}{/u}"
            "The next few bodies of lines are unreadable, you scan the page for the next part to read."
            "{u}{i}-or to a brand new world to explore.{/i}{/u}"
            "{u}{i}All without the cost of exhausting one’s self to near death or risking ruining one’s life by simply picking up a bucket.{/i}{/u}"
            "{u}{i}Additionally, the paintings appear to last after repeated uses.{/i}{/u}"
            "{u}{i}Oh the books I can write about the things I’ve seen in those other worlds. {/i}{/u}"
            "{u}{i}This spell may have numerous potential in sustaining our kind’s survival and possibly opening us to new realms of magic.{/i}{/u}"
            "You close the book and leave."
            $ Time.mins = Time.mins +10
            jump Temple_book
        "Read the second book." if True:
            "The book is called, “Society” by Abel Lynx."
            "{u}{i}Our world embodies the phrase, “the strong eat the weak.”{/i}{/u}"
            "{u}{i}If there is a Grand Creator somewhere it has a sick sense of humour.{/i}{/u}"
            "{u}{i}In this book I discuss the history and hierarchy of our society.{/i}{/u}"
            "{u}{i}We know our groups by the foods they eat, carnivores, herbivores, and omnivores.{/i}{/u}"
            "{u}{i}The carnivores and omnivores naturally larger and stronger than the rest dominate the hierarchy.{/i}{/u}"
            "{u}{i}And would hold positions of power, kings, queens, and nobles.{/i}{/u}"
            "{u}{i}While herbivores would usually serve the carnivores and omnivores as servants.{/i}{/u}"
            "{u}{i}Or work the farms or at most rise to be shop or innkeepers.{/i}{/u}"
            "{u}{i}Then there are those who possess and aptitude for magic and those who don’t. {/i}{/u}"
            "{u}{i}Children born with the power to manipulate magic are sent away from birth to select kingdoms built and run by magic users.{/i}{/u}"
            "{u}{i}For as magic users we stand above the common folk.{/i}{/u}"
            "{u}{i}The nobles may run their cities, but we shape the world.{/i}{/u}"
            "The next page,"
            "{u}{i}Breeding, our greatest and strangest of miracles.{/i}{/u}"
            "{u}{i}Cross breeding between species is a futile effort, as no offspring can be produced.{/i}{/u}"
            "{u}{i}Then again the whole concept of procreation is ridiculous to me, but nonetheless it must be discussed in this book.{/i}{/u}"
            "{u}{i}All species are capable of producing children with intellect and those without, that we dub ferals. {/i}{/u}"
            "{u}{i}Although ferals have similar appearances to their parent species, they do not have the ability to speak.{/i}{/u}"
            "{u}{i}And barely possess the ability to reason.{/i}{/u}"
            "{u}{i}In a sense, they are flawed and are mostly inferior even to the lowest of herbivores.{/i}{/u}"
            "The next page,"
            "{u}{i}We as mages serve a great cause although the feeble minds of those without magic may not see rhyme or reason for our actions, in the long run we are the superior species, {/i}{/u}"
            "{u}{i}Transcending the barriers that divide the rest of our world.{/i}{/u}"
            "{u}{i}With our magic we will show them all the way.{/i}{/u}"
            "You close the book and leave."
            if jane_inv_K.qty(Mysterious_note_1) == None:
                "Wait, what's this?"
                "You find a Mysterious Note."
                "The top half where the date would be has been torn off."
                "It looks like a segment of a story."
                "{u}{i}In the beginning there was only One.{/i}{/u}"
                "{u}{i}An almighty and all power being that could shape the world how it saw fit, and destroy everything with a snap of its fingers.{/i}{/u}"
                "{u}{i}It knew not its purpose for existence, and for thousands of years was revered and feared by the mortals of the earth.{/i}{/u}"
                "{u}{i}At times it would be a merciful god and grant the mortals bountiful harvests or grant them immeasurable strength in their wars.{/i}{/u}"
                "{u}{i}If scorn it would smite their cities with famine and sickness.{/i}{/u}"
                "{u}{i}To the immortal being they were all just his play things.{/i}{/u}"
                "{u}{i}But there was one thing its god like powers could not comprehend or have, the love and bond of mortals.{/i}{/u}"
                "{u}{i}For all the miracles it could conjure, the mortals would never see the being as one of them, it was forever alone.{/i}{/u}"
                "The note ends here."
                $ jane_inv_K.take(Mysterious_note_1)
            $ Time.mins = Time.mins +15
            jump Temple_book
        "Read the third book." if True:
            "The title of the book is “Paintings Through Time”"
            "It appears to be written in the style of a journal, by someone called Haylid Stach, Grand Magister."
            "One page reads,"
            "{u}{i}At the heart of all magic spells is the idea of equivalent exchange.{/i}{/u}"
            "{u}{i}If one is ingenuous and creative enough to discover what should be sacrificed to create a spell, they can rule the world.{/i}{/u}"
            "{u}{i}Of course, it goes without saying that the greater the spell’s effect the higher the cost.{/i}{/u}"
            "{u}{i}I in this book shall document my exploits in creating the greatest spell of all time, the spell to traverse back in time.{/i}{/u}"
            "Another page reads,"
            "{u}{i}After months of toiling with different spells and runes, I know now how to give this spell form! {/i}{/u}"
            "{u}{i}It’s so simple, we can’t travel back in time like hopping back and forth from town to town.{/i}{/u}"
            "{u}{i}Considering such an idea in the first place would be utterly foolish and pointless.{/i}{/u}"
            "{u}{i}But one can approach such an idea by putting their fates on the line.{/i}{/u}"
            "{u}{i}The idea came to me like a bolt of lightning while I watched my assistant Gallahan paint one of his ridiculous paintings of the lake.{/i}{/u}"
            "{u}{i}The painter puts his life into every stroke, every colour, the painting is a reflection of the person’s life.{/i}{/u}"
            "{u}{i}So, what if I were to do the same with magic.{/i}{/u}"
            "{u}{i}We can already project memories as visual construct of light. {/i}{/u}"
            "{u}{i}So, why not take it one step further, and make those memories into a gateway to the past.{/i}{/u}"
            "{u}{i}If one pours their entire being into a picture.{/i}{/u}"
            "{u}{i}Every drop of magic to create a certain moment in time.{/i}{/u}"
            "{u}{i}Then maybe, just maybe one can step into that painting and shape the past how they see fit.{/i}{/u}"
            "The next page,"
            "{u}{i}It worked... the accursed painting that took so much out of me that it kept me unconscious for days.{/i}{/u}"
            "{u}{i}...But all it lead to was ruin.{/i}{/u}"
            "{u}{i}I chose to paint a simple scene, one that I knew would not jeopardize the future of any person.{/i}{/u}"
            "{u}{i}My mother back when I was a mere hatchling cooking for me a bowl of her lentil and potato soup.{/i}{/u}"
            "{u}{i}It was the most extravagant meal we could have afforded back then.{/i}{/u}"
            "{u}{i}She came by the recipe simply by pure imagination. I loved that soup. {/i}{/u}"
            "{u}{i}So, I stepped into the painting and I was back at the gates of my old house.{/i}{/u}"
            "{u}{i}In that rundown shack with its barely growing potato farm.{/i}{/u}"
            "{u}{i}Mother would leave the bucket of potatoes she would cook with outside the house.{/i}{/u}"
            "{u}{i}I took it before leaving the painting.{/i}{/u}"
            "{u}{i}I was so full of myself, it’s just a mere prank technically.{/i}{/u}"
            "{u}{i}Nothing would have changed really.{/i}{/u}"
            "{u}{i}Upon my return from the painting I could still retain my original memories of the event, of mother cooking that bowl of soup for me for the first time.{/i}{/u}"
            "{u}{i}Then... when I returned to my home in my original time what do I find?{/i}{/u}"
            "{u}{i}My mother with her right hand was replaced by a wooden prosthetic!{/i}{/u}"
            "{u}{i}That one bucket of potatoes, it cost my mother her arm.{/i}{/u}"
            "{u}{i}Because she had to feed us, that day she offered her hand to the local alchemist to buy us food. {/i}{/u}"
            "{u}{i}The painting burned itself up after I exited.{/i}{/u}"
            "{u}{i}I can’t even recreate it anymore no matter how clearly I remember the original event, the painting will not form!{/i}{/u}"
            "{u}{i}Curse this useless spell, the chaos of changing one’s fate cannot be controlled.{/i}{/u}"
            "{u}{i}She doesn’t even remember creating the recipe for bloody sake. My soup!{/i}{/u}"
            "The last page is just a summary,"
            "{u}{i}Fate Painting Spell{/i}{/u}"
            "{u}{i}It allows the user to enter a past moment of their life via a painting created by their very life essence. {/i}{/u}"
            "{u}{i}Only a lived experience can be painted.{/i}{/u}"
            "{u}{i}Changes to events in the past lead to unpredictable changes in the future of the one who painted the painting in some aspect of their life.{/i}{/u}"
            "{u}{i}Upon exiting the painting, it will destroy itself, and the same painting cannot be painted by the same mage.{/i}{/u}"
            "{u}{i}The spell is useless, and only opens one up to danger.{/i}{/u}"
            "You close the book and leave."
            $ Time.mins = Time.mins +20
            jump Temple_book
        "Уйти" if True:
            jump Temple_map

screen temple_map:
    imagemap:
        if Time.hours >= 6 and Time.hours <= 17:
            idle 'templemap'
            hover 'templemap'
        else:
            idle 'templemapn'
            hover 'templemapn'

        vbox:
            xalign 0.25 ypos 0.66
            imagebutton:
                idle "UI/down button1.png"
                hover "UI/down button2.png"

                action Return("mountain")
        vbox:
            xalign 0.27 ypos 0.57
            if Map.t1 >= 0:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 1")
            else:
                pass
        vbox:
            xalign 0.35 ypos 0.52
            if Map.t2 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 2")
            elif Map.t2 >= 2 and Time.hours < 6 or Time.hours > 17:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 2")
            elif Map.t2 >= 2 and Time.hours >= 6 and Time.hours <= 17:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.465 ypos 0.38
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.t3 == 1:
                    imagebutton:
                        idle "UI/button1.png"
                        hover "UI/button2.png"
                        action Return("point 3")
                elif Map.t3 == 2:
                    imagebutton:
                        idle "UI/button4.png"
                        hover "UI/button4.png"
                else:
                    pass
            else:
                pass
        vbox:
            xalign 0.414 ypos 0.32
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.t4 == 1:
                    imagebutton:
                        idle "UI/button1.png"
                        hover "UI/button2.png"
                        action Return("point 4")
                else:
                    pass
            else:
                pass
        vbox:
            xalign 0.4 ypos 0.28
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.t5 >= 1:
                    imagebutton:
                        idle "UI/button1.png"
                        hover "UI/button2.png"
                        action Return("point 5")
                else:
                    pass
            else:
                pass
        vbox:
            xalign 0.44 ypos 0.28
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.t6 == 1:
                    imagebutton:
                        idle "UI/button1.png"
                        hover "UI/button2.png"
                        action Return("point 6")
                elif Map.t6 == 2:
                    imagebutton:
                        idle "UI/up button1.png"
                        hover "UI/up button2.png"
                        action Return("point 6")
                else:
                    pass
            else:
                pass
        vbox:
            xalign 0.52 ypos 0.32
            if Map.t7 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 7")
            else:
                pass
        vbox:
            xalign 0.52 ypos 0.32
            if Time.hours >= 6 and Time.hours <= 17:
                if Map.t8 == 1:
                    imagebutton:
                        idle "UI/button1.png"
                        hover "UI/button2.png"
                        action Return("point 8")
                elif Map.t8 == 2:
                    imagebutton:
                        idle "UI/button4.png"
                        hover "UI/button4.png"
                else:
                    pass
            else:
                pass



        vbox:
            if Time.hours >= 6 and Time.hours <= 17:
                xalign 0.54 ypos 0.29
                if Map.t9 >= 1:
                    imagebutton:
                        idle "UI/button1.png"
                        hover "UI/button2.png"
                        action Return("point 9")
                else:
                    pass
            else:
                pass

        vbox:
            if Time.hours >= 6 and Time.hours <= 17:
                xalign 0.48 ypos 0.275
                if Map.t10 >= 1:
                    imagebutton:
                        idle "UI/button1.png"
                        hover "UI/button2.png"
                        action Return("point 10")
                else:
                    pass
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
