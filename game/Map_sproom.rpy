label Sproom_map:
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    window hide None
    $ renpy.music.set_volume(0.3, 1, channel = "music")
    if Map.sproom == 0:
        scene sproom 2 with dissolve
        if jane_inv_M.qty(torch) == None:
            e 1 "I need a light though. "
            "You can’t make out what’s inside. Looks like you need to come back with a torch."
            "Stepping back from the partition wall reforms in a blink of an eye."
            jump Temple_map
        elif True:
            $ jane_inv_M.drop(torch,1)
            "You pull out the torch you had with you and light it up."
            "The light reveals a scone nearby the entrance so you place your torch there."
            scene sproom 1 with dissolve
            "It’s a storage room with what looks like five framed paintings on the ground."
            e 1 "That’s weird, who goes through all that trouble to hide some paintings."
            "You crouch down and look at the painting nearest to you."
            e 5 "What? It’s all grey. "
            "Every single one of the paintings were nothing but grey."
            "You then remembered the emblem in your bag."
            "You pull it out and hold it close to the first painting."
            "Like ants scurrying away from danger the grey colour disappears as you bring the emblem closer until it forms a blue patch no larger than a gold coin."
            "You move the emblem around and wherever it goes it exposes the painting a little bit more."
            "But somehow your one emblem cannot reveal the whole painting."
            "You sigh and put the emblem back in your bag."
            e 13 "Maybe one emblem isn’t enough? "
            e 13 "Well all that was for nothing, unless if I find a way to collect more of these emblems."
            e 13 "Then just maybe, it might work. For now, this room will have to be kept a secret."
            e 13 "I still don’t know what those paintings are, and it’s too dangerous to expose anyone else to them."
            "Disappointed, you leave the secret room."
            $ Map.sproom = 1
            jump Temple_map


    if Items.em >= 2:
        jump painting_unlock
    scene sproom 1 with dissolve
    menu:
        "Check the paintings" if True:
            "There’s nothing to do here. The paintings are all still all blank."
            jump Sproom_map
        "Leave" if True:
            jump Temple_map

label painting_unlock:
    if Map.paintingroom == 0:
        scene sproom 1 with dissolve
        $ Map.paintingroom = 1
        "With the second emblem, the painting reveals its true form."
        "Like burning paper the picture spreads from the corners all the way to the middle of the portrait."
        "The portrait flashes brightly, forcing you to turn away."
        with flashbulb
        e 5 "This is-"
        scene sproom 3 with vslow_dissolve
        "They could lead to a way out of this fog, or at the least be worth some money."
        "With your emblems in one hand, you approach the paintings."
        "Which do you observe first?"
        jump painting_choose
    elif True:
        scene sproom 3 with slow_dissolve
        "Within the dimly lit secret chamber, there are five paintings laid out around the room."
        label painting_choose:
            $ renpy.music.set_volume(1, 5.5, channel = "music")
            menu:
                "Check the courtyard painting" if True:
                    if Map.first_world_touch == 0:
                        "You hold out your hand close enough that it almost touches the canvas."
                        "The glow of the painting causes you to gasp softly."
                        "Like a drop of paint in a pool of water."
                        "Colours spill throughout the canvas until a full image appears in the frame."
                        e 9 "What is this?"
                        "You reach your hand out to touch the painting, expecting to feel the texture of the paint on the canvas with your fingertips."
                        "But instead, your fingers go through it."
                        e 5 "Ahh!"
                        "Quickly you pull your hand back."
                        "Your fingers are still intact."
                        "Letting out a sigh of relief, you stand perplexed with what this painting is."
                        "You decide to test the painting further before interacting with it yourself. "
                        e 1 "I probably should test this out with some nonliving things first."
                        "Your sword comes to mind. Drawing your blade you carefully try to poke the painting."
                        "Again, the metal enters the painting like there’s nothing there."
                        "When you pull your blade back, it appears to still be intact. "
                        e 1 "So my items will pass through unharmed as well."
                        e 1 "I already know that my body can go in and out just fine, meaning I can probably return from the other side."
                        e 1 "Time to see what secrets this painting holds then."
                        $ Map.first_world_touch = 1
                    "Do you want to enter the painting?"
                    menu:
                        "Yes" if True:
                            if Map.first_world == 1:
                                e 13 "He is no ordinary person, and I’m getting some answers, no more leaving things in the dark."

                            scene black with vslow_dissolve
                            pause 3
                            jump courtyard_painting_world
                        "No" if True:
                            jump painting_choose
                "{s}Check the second painting" if True:

                    jump painting_choose
                "{s}Check the third painting" if True:
                    jump painting_choose
                "{s}Check the fourth painting" if True:
                    jump painting_choose
                "{s}Check the fifth painting" if True:
                    jump painting_choose
                "Leave" if True:
                    jump Temple_map
label courtyard_painting_world:
    $ renpy.music.set_volume(0, 5.5, channel = "music")
    if Map.first_world == 0:
        "The sensation of entering the picture is no different than entering the tavern from the outside."
        "Your eyes quickly adjust to the bright light of the sun."
        e 1 "The sun?"
        "It’s been so long since you could see clearly the morning skies."
        "What’s even stranger is how there’s not a hint of fog to where you stand."
        scene courtyard_world01 with vslow_dissolve
        "You’re standing on a cleanly cut grassy road."
        "It looks like a courtyard of some sort with a stone pathway leading forward."
        "But there is something odd about this world."
        "Objects in the distance look like they have no color, they are black and white and weirdly distorted. "
        "Your instincts tell you not to approach."
        "Your wonderment is cut short when you remember the world on the other side. "
        "You turn, and to your horror, there is no exit."
        e 9 "What?! "
        "Fear sets in and your mind goes blank."
    elif Map.first_world == 1:
        "You enter the courtyard again."
        scene courtyard_world01 with slow_dissolve
        "You turn around and unlike before, there is a painting frame projecting the image of the room you came from. "
        e 5 "The exit is here now."
    elif True:
        scene courtyard_world01 with slow_dissolve
    menu:
        "Enter the house" if True:
            jump courtyard_painting_world_house
        "Leave" if Map.first_world >= 1:
            scene black with vslow_dissolve
            pause 3
            jump painting_unlock
    label courtyard_painting_world_house:
        if Map.first_world == 0:
            "Without any other options you walk ahead. "
            scene black with slow_dissolve
            "There are paintings lining the walls of the entryway."
            "You walk straight and turn into the closest door. "
            scene courtyard_world02 with slow_dissolve
            "This room looks like a living room of sort with a wide open door leading to a garden."
            e 1 "This is-"
            "Suddenly, you feel a hand on your shoulder."
            "In your shock you bat the hand away and turn to see who it is."
            "Standing in front of you is a black dragon looking sternly at you."
            show long stand at center with slow_dissolve
            "Despite his tattered clothes his stature is imposing and monolithic. "
            "Your eyes are drawn to the cerulean blue stripes on his forearms."
            "Their shine reminds you of the stars set against the dark backdrop of his scales."
            "Dragon" "..."
            e 5 "What? Who are you? Where is this?"
            "Dragon" "You do not belong here, traveller."
            hide long stand at center with dissolve
            "He snaps his fingers and the painting frame from before appears and swallows you whole."
            with flashbulb
            scene black with dissolve
            e 9 "AHHH!" with vpunch
            pause 5
            scene sproom 3 with vslow_dissolve
            "When you reopen your eyes, you find yourself back in the room full of paintings."
            "You check every inch of fur on your body to make sure nothing is misplaced. "
            e 9 "What was all that? Who- who even was that dragon?"
            $ Map.first_world = 1
            jump painting_choose
        elif Map.first_world == 1:
            scene courtyard_world02 with slow_dissolve
            "The black dragon from before sits in front of you on an elegant stool while sipping a cup of tea."
            "He places his cup down on the table and looks at you with the briefest of curiosity before pouring himself another cup from the teapot."
            "Although you have never seen him, or he can be said to be very suspicious."
            "You believe he is harmless, don't know why."
            "You walk over to the dragon’s table."
            e 5 "Hey, I have a bone to pick with you."
            "He ignores you and takes a sip of tea."
            "His sleepy gaze is drawn to the butterflies flying around the garden."
            show long stand at center with slow_dissolve
            "Dragon" "You know, you are peculiar."
            "Dragon" "Most souls would approach the unknown with caution, but you dive into it."
            "Dragon" "Perhaps this is fate’s way of telling me that our meeting is inevitable."
            e 9 "Gee, thanks."
            e 13 "Look, weird things have been happening, and I need answers."
            e 1 "Please, lives are on the line."
            hide long stand at center with dissolve
            "The dragon sips his tea."
            "When he places his cup down, another identical one appears across from him."
            "Dragon" "Have a seat. Words go down smoother with a cup of tea."
            e 1 "Umm... ok."
            "You sit across from the dragon."
            "Dragon" "Today’s tea is a rarity."
            "Dragon" "The flower of the plant this tea is made from is said to bloom under moonlight once every eight months. "
            "Dragon" "Its leaves can be harvested throughout the year."
            "Dragon" "But the leaves that are harvested on the night the flowers bloom tastes richer than any other time of the year."
            e 1 "Fascinating, but I am looking for answers."
            show long stand at center with slow_dissolve
            "Dragon" "You know, often those that try to outrun the wind find themselves defeated from the start."
            show long stand01 at center with dissolve
            "Dragon" "That said, I understand that the finite seconds that make up your life are very precious to your kind."
            "Dragon" "So, ask away."
            $ Map.first_world = 2
        elif True:
            scene courtyard_world02 with slow_dissolve
            show long stand01 at center with dissolve
            "Dragon" "You come again traveler, what is it that you seek?"
        label courtyard_painting_world_talk:
            menu:
                "Who are you?" if True:
                    e 1 "Well obviously, who are you?"
                    "Dragon" "[name], I doubt knowing that answer will bring you any closer to what you’re looking for."
                    e 5 "I can’t even know your name?"
                    "Dragon" "Names are powerful things in this world."
                    show long stand at center with dissolve
                    "Dragon" "And I am just a nameless prisoner."
                    e 1 "..."
                    e 5 "(Wait, when did I give him my name?)"
                    jump courtyard_painting_world_talk
                "Where is this?" if True:
                    "Dragon" "It is my lovely garden, I tend to it myself."
                    "You cross your arms and frown."
                    show long stand01 at center with dissolve
                    "Dragon" "Well, what do you think this place is?"
                    e 1 "I don’t know, a portal to another world? A dream? Me going mad?"
                    "Dragon" "Possible. All true descriptions one would give to a book."
                    e 1 "What do you mean?"
                    "Dragon" "This place is my garden, but it is also part of a story."
                    "Dragon" "Through time those imbued with magic have within their limited capacity tried to peek into these stories of other worlds, or to even rewrite their own."
                    "Dragon" "They would have you believe that they had transcended the limits of humanity and became gods themselves."
                    "Dragon" "Not knowing that the hands of fate had already etched its own ending in the paintings they created."
                    show long stand at center with dissolve
                    "Dragon" "Forgive me, I digress, these paintings can be thought of as the doorways to other worlds."
                    "Dragon" "An opportunity to escape."
                    e 5 "Escape! I can have everyone escape through the paintings."
                    show long stand01 at center with dissolve
                    "Dragon" "If your friends have magic I don’t see why."
                    show long stand at center with dissolve
                    "Dragon" "However, are you sure that is what they want?"
                    "Dragon" "To leave behind the lives they’ve built here in this realm to run into another world?"
                    e 1 "..."
                    "The realization of what you’ve been told weighs heavily on you."
                    "You just sit and watch the dragon drink his tea."
                    jump courtyard_painting_world_talk
                "How do the exits work here?" if True:
                    e 1 "The last time I was here, you made the exit appear."
                    e 1 "How does that work?"
                    show long stand01 at center with dissolve
                    "Dragon" "I took some liberties with that."
                    "Dragon" "Like a book, I skipped to the ending, and that is where the exit lies."
                    e 1 "What? An ending?"
                    show long stand at center with dissolve
                    "Dragon" "Yes, despite what it looks like all who enter the paintings become scripted tools tasked with carrying out fate’s plans."
                    "Dragon" "If they are successful in carrying out the story until the end, the exit will open for them."
                    e 13 "Who decides these endings? "
                    show long stand01 at center with dissolve
                    "Dragon" "Who knows? Sometimes it would seem like the wishes of the painter are the endings themselves."
                    "Dragon" "Sometimes it seems like the world in the painting is reaching out for someone to complete its story."
                    e 1 "So, basically, just go with the flow of what’s happening in the painting."
                    "Dragon" "Correct."
                    jump courtyard_painting_world_talk
                "Why is he here?" if True:
                    e 1 "Why are you really here?"
                    e 1 "What you did when we first met, that isn’t something any ordinary person can do."
                    show long stand at center with dissolve
                    "He looks at you sternly while placing his cup down."
                    "Dragon" "I am here because there is nowhere else to go."
                    e 9 "Who put you here?"
                    "The dragon leans back and looks upward to the sky."
                    "Dragon" "If only I could tell you."
                    e 1 "I mean, you can. Just let me help you."
                    show long stand01 at center with dissolve
                    "Dragon" "Pleasant words, but no one can help me."
                    e 1 "Yes I can. I mean look I found these emblems."
                    e 1 "They have some kind of power, maybe I can use it somehow to free you?"
                    hide long stand01 at center with dissolve
                    "You pull out the emblems from your satchel to show the dragon."
                    "He merely looks on at the emblems in your hand and a smile creeps across his face."
                    show long stand01 at center with dissolve
                    "Dragon" "You are a more interesting person than I thought, [name]."
                    e 5 "What? "
                    "You keep the emblems away."
                    e 1 "You still won’t tell me what’s going on?"
                    show long stand at center with dissolve
                    "Dragon" "In due time. That is all I can say."
                    "You shake your head in defeat."
                    jump courtyard_painting_world_talk
                "Leave" if True:
                    e 1 "I have nothing more to ask."
                    "Dragon" "Then to your next visit then."
                    "You stand up and exit through the painting frame."
                    hide long stand01 at center with dissolve
                    hide long stand at center with dissolve
                    scene black with vslow_dissolve
                    pause 3
                    jump painting_unlock
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
