label castle_map0:
    stop music
    stop Thane
    stop Chan1
    stop Chan2
    $ renpy.music.set_volume(1, 1, channel = "Chan1")
    play Chan1[ "<silence 0.5>", "music/castle.ogg" ]fadein 3
    if Map.castle_0 == 0:
        scene black with vslow_dissolve
        "You enter a wide and deserted courtyard."
        "Everything from the walls to the floors and the fountain in the heart of the courtyard has been reclaimed by the glowing moss."
        scene castle 2 with slow_dissolve
        "The fur on your arm stands on end, there’s a strange scent permeating the air, like death and something darker."
        $ Map.castle_0 = 1

    jump castle_map


label castle_map:
    stop music
    $ Map.undercity_here = False
    $ Time.mins = Time.mins +10
    $ Zalt.dungeon = True
    $ config.rollback_enabled = False
    $ renpy.music.set_volume(1, 5, channel = "Chan1")
    $ renpy.music.set_pause(False, channel='Chan1')
    window hide None
    if Zalt.Dungeon_leave:
        jump Cave_leave
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Zalt.A_exp >= 100:
        $ Zalt.A_exp = Zalt.A_exp -100
        $ Zalt.A_lv = min(Zalt.A_lv + 1, 5)
        $ Zalt.AP = Zalt.AP +1
        "You get one AP, you have [Zalt.AP] now."
        "Your A-LV now is [Zalt.A_lv]"


    if Zalt.A_lv == 5:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 4:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 3:
        $ Zalt.A_exp_lv = 2
    elif Zalt.A_lv == 2:
        $ Zalt.A_exp_lv = 1.5
    elif Zalt.A_lv == 1:
        $ Zalt.A_exp_lv = 1.2
    elif True:
        $ Zalt.A_exp_lv = 1

    scene castle 1
    if Map.castle_3 != 2:
        show castle_fog_1
    if Map.castle_4 != 2:
        show castle_fog_2
    if Map.castle_7 !=2:
        show castle_fog_3
    if Map.castle_14 !=2:
        show castle_fog_4
    if Map.castle_44 !=2:
        show castle_fog_5
    if Map.castle_22 != 3:
        show castle_fog_6
    if Map.castle_8 !=2:
        show castle_fog_7
    if Map.castle_26 != 3:
        show castle_fog_8
    if Map.castle_29 != 1:
        show castle_fog_9
    if Map.castle_32 != 2:
        show castle_fog_10
    if Map.castle_31 != 2:
        show castle_fog_11
    if Map.castle_9 != 3:
        show castle_fog_12



    call screen castle_map with dissolve
    if _return == 'exit':
        jump belltower_map0
        return

    if _return == 'point 2':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if Map.castle_2 == 1:
            "You come upon what looks like a man made pond. "
            "Glowing white lilies float above the waters."
            "The large lily pads that grow beneath the flowers cover the bottom of the pond."
            "Your eyes are drawn to the large rock that sits in the middle of the pond."
            "From where you stand you can make out the words."
            "“Sage, thieves, knight, and priest” etched onto the stone."
            "You have no idea what they mean, but you feel at ease here. "
            "You can set up a campfire here"
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_2 = 2
            $ Map.castle_3 = 1
            $ Map.castle_4 = 1
            jump castle_map
        elif True:
            "This place looks safe to set up a campfire and rest."
            "You can also level up here."
        menu:
            "Rest (use 3 sticks and 2 rocks)" if jane_inv_M.qty(stick) >= 3 and jane_inv_M.qty(rock) >= 2:
                $ jane_inv_M.drop(stick,3)
                $ jane_inv_M.drop(rock,2)
                scene black
                "You rest a while, feel refreshed and full of energy."
                "HP and MP have been restored to maximum."
                $ Zalt.hp = Zalt.maxhp
                $ Zalt.mp = Zalt.maxmp
                $ Time.mins = Time.mins +30
                jump castle_map
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

                jump castle_map
            "Masturbate" if Zalt.lust >= 40:
                "You spend some time to deal with your desires."
                $ Zalt.lust = 0
                $ Time.mins = Time.mins+15
                jump castle_map
            "Leave" if True:

                jump castle_map


    if _return == 'point 3':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "Walking forward you become more aware of the emptiness of the castle."
        "All that can be heard are the sounds of your footsteps against the earthen floor."
        "There are dark stains splattered across the floor, dried blood perhaps?"
        "Broken potteries and faded paintings lie scattered in random bushes and across the floor."
        "As though people were in a rush to grab everything inside this castle and had to leave in a hurry."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.castle_3 = 2
        $ Map.castle_6 = 1
        jump castle_map


    if _return == 'point 4':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        if jane_inv_K.qty(leaf_key) == None:
            "The door is locked."
            "Just above the doorknob,you see a symbol in the shape of a leaf."
            jump castle_map
        elif jane_inv_K.qty(leaf_key) == 1:
            $ Map.castle_4 = 2
            $ Map.castle_5 = 1
            "The door is locked."
            "Just above the doorknob,you see a symbol in the shape of a leaf."
            "You open the door with the Leaf Key."
            $ jane_inv_K.drop(leaf_key)
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            jump castle_map
        elif True:
            jump castle_map
    if _return == 'point 5':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "The moment the door opens, your nose wrinkles from the musty stench coming out of it."
        "Stepping inside, you notice the layers of dust lining the shelves."
        "Across from the doorway, you notice the figure of a person sprawled on the floor ."
        "You quickly pull your torch upwards to illuminate the person."
        "It’s a skeleton!"
        "Around the body are a few bundles of rope and unlit torches."
        e 13 "Poor guy, getting trapped in here all alone."
        "You pick up the items."
        "You find 2 ropes, 2 torches and 1 bottles of HP potion in it."
        $ jane_inv.take(hp_potion,1)
        $ jane_inv_M.take(rope,2)
        $ jane_inv_M.take(torch,2)

        $ Map.castle_5 = 2
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump castle_map

    if _return == 'point 6':

        $ Time.mins = Time.mins +10

        play sound "music/foot1.ogg"
        "You come across a harrowing sight."
        "The skeletons of the inhabitants before lie sprawled across the courtyard in the same position they were killed in."
        "You approach a skeleton with a rusty sword piercing the back of its skull, the poor bastards probably didn’t even see it coming."
        "The clothes it wore have blackened and some of the moss even grew over the skeleton."
        "Still, there was no pattern you could see with these deaths."
        "There’s a pair of skeletons lying across from each other to your right."
        "One is wearing a metal armour that bears a faded crest that used to be painted on it. "
        "While the other one is dressed in regular clothes that resemble that of a lowly servant in a castle. "
        "Was it some kind of coup?"
        "To your left, is a skeleton in a woman’s dress, a dagger lies buried in its chest."
        "In its arms are smaller bones and a skull that could only belong to a baby. "
        "You face ahead. There’s a giant door tall enough to fit the entire tavern."
        "Large heavy looking chains criss cross from one side of the door to the other, with one massive lock holding it all in place."
        "As you look on at the door, your eyes widen at a horrifying sight."
        "What looks like a translucent but disembodied hand floats gently mid air just right outside the door."
        "Upon focusing your eyes, you notice that it’s waving at you."
        "You hold your breath as the rest of the figure appears like a drawing in midair."
        "In seconds, its form is complete, a creature whose face is distorted like a painting someone rubbed their hands over dressed in jester's clothing waves at you to come to him."
        "A cold shiver travels down your spine, at the back of your head you know him to be… a ghost."
        "He jumps about, letting the bells on his hat shake energetically, but there is no sound."
        "You gulp."
        "A sense of dread fills your stomach, something tells you that if you want to get to Flo you’ll need to head over to that figure."
        $ Map.castle_6 = 2
        $ Map.castle_9 = 1
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump castle_map

    if _return == 'point 7':
        $ Time.mins = Time.mins +10
        play sound "music/foot1.ogg"
        "You pass through the broken door."
        "The moment you step through to the other side, a strange alien feeling of dread grips your heart."
        e 9 "What is this?"
        "While clutching the left side of your chest, you look around for what could be causing this but you find nothing."
        "Cautiously, you walk inwards."
        $ Map.castle_7 = 2
        $ Map.castle_10 = 1
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump castle_map

    if _return == 'point 8':
        "The door here has been hacked into tiny pieces. You press onward."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        $ Map.castle_8 = 2
        $ Map.castle_26 = 1
        $ Map.castle_43 = 1
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump castle_map
    if _return == 'point 9':
        if Map.castle_9 == 1:
            $ Time.mins = Time.mins +10
            play sound "music/foot1.ogg"
            "You stand at an arm's length from the dancing figure."
            e 9 "Wh-what are you?"
            "Jester" "A visitor! A visitor! A visitor for the king!"
            "He performs a backflip and claps vigorously in the air. "
            e 5 "What are you talking about? What king?"
            "Jester" "Oh, you must be here to audition to be one of the troupe members."
            "He spins around and jumps one leg to another."
            e 9 "Please stop moving around, ghost."
            "Jester" "A ghost? You think I’m a ghost?"
            "Jester" "Well I have been eating less lately. I’m practically skin and bones."
            "Jester" "You’re the ghost, what with your pale white complexion,haha!"
            e 9 "Me?"
            e 9 "(No, not even that, he really is a ghost. Why is he acting like I’m the crazy one.)"
            e 1 "Look I don’t have time to argue with you."
            e 1 "I came looking for someone, and I need to get to the lower city."
            "Jester" "Well you see, something strange has happened."
            "Jester" "I lost my badge."
            e 1 "That's not I'm..."
            "Jester" "Heck, almost half of us here lost our badges."
            "Jester" "So be a dear, and bring me a badge. Doesn’t really matter which one."
            e 1 "...Where exactly am I going to find this badge of yours?"
            "Jester" "Definitely not here, I checked the courtyard and there’s not a single badge left."
            "Jester" "You might find one over there in the church or residential area."
            "He points to your left."
            "Jester" "Or maybe there are a few in the soldiers’ barracks or where the scholars usually work at."
            "He points to your right."
            e 13 "Hmm… fine. I’ll be back."
            "Jester" "Good luck! Haha! Good luck!"
            "He waves you away and does a jig while you walk away from him."
            $ Map.castle_7 = 1
            $ Map.castle_8 = 1
            $ Map.castle_9 = 2
            jump castle_map
        elif Map.castle_9 == 2:
            "Jester" "A visitor! A visitor! A visitor for the king!"
            "Jester" "I lost my badge!"
            "Jester" "I lost my badge, haha!"
            "Jester" "Bring me a badge, bring me a badge."
            menu:
                "Give it 'Jester badge'" if jane_inv_K.qty(jester_badge) == 1:
                    $ jane_inv_K.drop(jester_badge)
                    e 1 "I take that this would work?"
                    "Jester" "A jester badge! Just like the one I had before."
                    "Jester" "Yes, this will do quite nicely."
                    "Jester" "He snatches the badge from your hand."
                    "He holds the badge upwards with both hands and twirls on the spot."
                    e 13 "Ehem!"
                    e 1 "Again, I came looking for someone, and I need to get to the lower city."
                    "Jester" "Oh right, I was supposed to show you how to go to the underground city."
                    "Jester" "Simple, you just need to go through these doors, and you will find the entrance. "
                    "The ghost walks over to the large door and pulls out a ghostly key."
                    "He puts the key into the grand lock and turns it. "
                    "Amazingly, the lock clicks and drops to the floor."
                    "The jester turns to face you with a disturbing grin on his face. "
                    "Jester" "Say hello to the king for me. Toodaloo!"
                    "The ghost backflips and vanishes with the badge. "
                    e 9 "How can he do that, and still think he isn't a ghost?"
                    e 13 "I’ll never understand the supernatural."
                    $ Map.castle_9 = 3
                    $ Map.castle_41 = 1
                    jump castle_map
                "Give it 'Knight badge'" if jane_inv_K.qty(knight_badge) == 1:
                    $ jane_inv_K.drop(knight_badge)
                    e 1 "WIll this work?"
                    "Jester" "A knight badge, yes!"
                    "He snatches the badge from your hand."
                    "Jester" "This is my ticket to the good life!"
                    e 1 "What do you mean by that?"
                    "Jester" "Nothing, nothing. You just want to go down to the city right? Here."
                    "He hurries over to the large door behind him and pulls out a ghostly key."
                    "It fits into the large lock on the door, and unlocks it."
                    "Jester" "You can’t miss the entrance, it’s just straight ahead."
                    "Jester" "Say hi to the king for me too if he doesn’t bite your head off."
                    e 5 "Wait, wha-"
                    "But it’s too late, the ghost does a backflip and disappears with the badge. "
                    $ Map.castle_9 = 3
                    $ Map.castle_41 = 1
                    jump castle_map
                "Give it 'Prince badge'" if jane_inv_K.qty(prince_badge) == 1:
                    $ jane_inv_K.drop(prince_badge)
                    e 1 "WIll this work?"
                    "Jester" "A prince badge, yes!"
                    "He snatches the badge from your hand."
                    "Jester" "This is my ticket to the good life!"
                    e 1 "What do you mean by that?"
                    "Jester" "Nothing, nothing. You just want to go down to the city right? Here."
                    "He hurries over to the large door behind him and pulls out a ghostly key."
                    "It fits into the large lock on the door, and unlocks it."
                    "Jester" "You can’t miss the entrance, it’s just straight ahead."
                    "Jester" "Say hi to the king for me too if he doesn’t bite your head off."
                    e 5 "Wait, wha-"
                    "But it’s too late, the ghost does a backflip and disappears with the badge. "
                    $ Map.castle_9 = 3
                    $ Map.castle_41 = 1
                    jump castle_map
                "Leave it alone" if True:
                    jump castle_map

            jump castle_map
        elif True:
            jump castle_map
    if _return == 'point 10':
        "You stop in the middle of a long hallway. "
        "Turning to the right you see what looks like an empty room filled with dusty pews."
        "You turn to the left…"
        show castle_ghost
        hide castle_ghost with dissolve
        "A HORRIFIC FACE APPEARS RIGHT IN FRONT OF YOU! " with vpunch
        e 5 "AHHHHHHH!" with vpunch
        "You fall on your butt, and wave your hands frantically in front of you to shield you from... nothing?"
        "The specter is nowhere to be found. "
        e 9 "What is this?"
        "You stand up and hear the faint sound of children laughing in your ears."
        "You turn in every direction to find the source of the laughter, but there’s nobody here but you. "
        e 12 "Fuck this! I better get out of here quickly."
        "Looking upwards, you see the roof is broken. "
        $ Map.castle_10 = 2
        $ Map.castle_44 = 1
        $ Map.castle_11 = 1
        $ Map.castle_12 = 1
        $ Map.castle_13 = 1
        $ Map.castle_14 = 1
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump castle_map
    if _return == 'point 11':
        if Map.castle_11 == 1:
            "You enter what looks like a bedroom. "
            "Underneath the bed you find a box of props inside, some worn out juggling balls, a jester's hat with a broken bell."
            "And a book that contains some jokes inside."
            "You don’t find the jokes written that funny."
            "You walk about when you feel a loose tile under your feet."
            e 1 "Hmm?"
            "Moving the tile away you find a diary hidden beneath it."
            "The writing inside the diary is difficult for you to understand."
            "The writer keeps referring to a Lady Maria and the writing can go off tangent every few sentences."
            "The last record however, the story is very clear."
            "{u}{i}Lady Maria, Lady Maria.{/i}{/u}"
            "{u}{i}You would not believe the day I've had.{/i}{/u}"
            "{u}{i}Everyone was killing and robbing the rich worms in the castle just as planned.{/i}{/u}"
            "{u}{i}I thought I could’ve taken advantage of the chaos and swipe as many valuables as I can before leaving.{/i}{/u}"
            "{u}{i}But then… guess what I found in the Knight Commander’s office.{/i}{/u}"
            "{u}{i}Oh what joy, with a swipe here and a cut there, a chance for me to not just be rich but to live like a literal king.{/i}{/u}"
            "{u}{i}Now I got a lovely new badge. {/i}{/u}"
            "{u}{i}I won’t be needing two badges, the story will be too complicated.{/i}{/u}"
            "{u}{i}Best I get rid of it.{/i}{/u}"
            "{u}{i}The queen’s corpse hasn’t been found, but we will find it soon, with the knights out of the way she is foolish to try to stop us.{/i}{/u}"
            "{u}{i}I’m so sorry Lady Maria I must leave you here.{/i}{/u}"
            "{u}{i}No one must know my dirty little secret.{/i}{/u}"
            "{u}{i}I will think of you when I am in the arms of my new father.{/i}{/u}"
            "You drop the book and recoil upon realizing what this author recorded."
            e 1 "…"
            "You leave the room."
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_11 = 2
            jump castle_map
        elif Map.castle_11 == 2:
            "The diary is still here."
            "Do you want to read again?"
            menu:
                "Yes" if True:
                    "{u}{i}Lady Maria, Lady Maria.{/i}{/u}"
                    "{u}{i}You would not believe the day I've had.{/i}{/u}"
                    "{u}{i}Everyone was killing and robbing the rich worms in the castle just as planned.{/i}{/u}"
                    "{u}{i}I thought I could’ve taken advantage of the chaos and swipe as many valuables as I can before leaving.{/i}{/u}"
                    "{u}{i}But then… guess what I found in the Knight Commander’s office.{/i}{/u}"
                    "{u}{i}Oh what joy, with a swipe here and a cut there, a chance for me to not just be rich but to live like a literal king.{/i}{/u}"
                    "{u}{i}Now I got a lovely new badge. {/i}{/u}"
                    "{u}{i}I won’t be needing two badges, the story will be too complicated.{/i}{/u}"
                    "{u}{i}Best I get rid of it.{/i}{/u}"
                    "{u}{i}The queen’s corpse hasn’t been found, but we will find it soon, with the knights out of the way she is foolish to try to stop us.{/i}{/u}"
                    "{u}{i}I’m so sorry Lady Maria I must leave you here.{/i}{/u}"
                    "{u}{i}No one must know my dirty little secret.{/i}{/u}"
                    "{u}{i}I will think of you when I am in the arms of my new father.{/i}{/u}"
                    "You drop the book and recoil upon realizing what this author recorded."
                    jump castle_map
                "No" if True:
                    jump castle_map
        elif True:
            jump castle_map



        jump castle_map
    if _return == 'point 12':
        "You enter a room with a mattress on the floor and a single pillow."
        "Next to the mattress is a note."
        "{u}{i}Briareos,{/i}{/u}"
        "{u}{i}Your mother and I have decided that your skills would be better used if you joined the king’s men as a knight.{/i}{/u}"
        "{u}{i}My son, this is the best choice for you considering how you excel physically.{/i}{/u}"
        "{u}{i}This would also be good for our family’s honour,\nif you are accepted among the king’s men I can keep our business alive with the help of the many aristocrats that adorn the king’s court.{/i}{/u}"
        "{u}{i}Do this for our family, Briareos.{/i}{/u}"
        "{u}{i}Signed,\nFather.{/i}{/u}"
        if Map.castle_12 == 1:
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_12 = 2
        jump castle_map
    if _return == 'point 13':
        "A wall of rubble blocks your way forward. "
        e 1 "I need to find another way."
        e 1 "Maybe there’s something in this room that can help me get passed to the other side."
        jump castle_map
    if _return == 'point 14':
        if jane_inv_K.qty(lion_key) == None:
            "The door is locked."
            "On top of the keyhole is the symbol of a lion."
        elif True:
            "The door is locked."
            "On top of the keyhole is the symbol of a lion."
            "You open the door with the Lion Key."
            $ Zalt.A_exp = Zalt.A_exp + 20*Zalt.A_exp_lv
            $ PPEXP = 20*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ jane_inv_K.drop(lion_key)
            $ Map.castle_14 = 2
            $ Map.castle_15 = 1
        jump castle_map
    if _return == 'point 15':
        "The room appears to be the kitchen."
        "There is an unused hearth in the middle of the room."
        "All around there are pots, pans and all sorts of kitchen utensils messily laid out on the floor and the tables inside the kitchen."
        "All around are pots, pans and all sorts of kitchen utensils that are strewed on the floor and across the tables inside the room."
        "Not a single scrap of food remains."
        show black3 at center
        show wingkey at center with dissolve
        "While looking around, you find the Wing Key on the floor with a note attached to it."
        "{u}{i}One of the scholars dropped this.{/i}{/u}"
        "{u}{i}Remember to give it back to one of them.{/i}{/u}"
        "It won’t help them now, but hopefully this key will be of use to you."
        "< You get the Wing Key. >"
        $ jane_inv_K.take(wing_key)
        $ Map.castle_16 = 1
        $ Map.castle_15 = 2
        $ Map.castle_18 = 1
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump castle_map
    if _return == 'point 16':
        if jane_inv_K.qty(jewel_key) == None:
            "The door is locked."
            "On top of the keyhole is the symbol of a crown like jewel."
        elif True:
            "The door is locked."
            "On top of the keyhole is the symbol of a crown like jewel."
            "You open the door with the Jewel Key."
            $ Zalt.A_exp = Zalt.A_exp + 20*Zalt.A_exp_lv
            $ PPEXP = 20*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ jane_inv_K.drop(jewel_key)
            $ Map.castle_16 = 2
            $ Map.castle_17 = 1
        jump castle_map
    if _return == 'point 17':
        jump battle_kid
    if _return == 'point 18':
        "These doors are the grandest you’ve seen around here."
        "These doors are the most opulent that you’ve seen around here."
        "On the surface of the door is the carving of the castle inside the cave."
        "You open the doors to find a bedroom in ruins."
        "What you suspect was once a grand bed now is in taters and is more moss than bed."
        "There are dozens of empty bottles littering the floor."
        "The carpet has been torn, and whatever furniture that was in here has been hacked to pieces."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.castle_18 = 2
        $ Map.castle_19 = 1
        jump castle_map
    if _return == 'point 19':
        if Map.castle_19 == 1:
            "You walk over to the drawers and search each compartment for anything useful."
            "You then notice one compartment is slightly more shallow compared to the other."
            "Pressing your hand against the bottom of the compartment, you realize it’s a fake bottom."
            "Removing the fake bottom reveals a piece of paper stuck on the other side."
            "The paper reads…"
            "{u}{i}When the king returns from his hunt we all have to play our new parts. {/i}{/u}"
            "{u}{i}It worked like a charm. The king thinks I am the sweet little prince without even questioning it.{/i}{/u}"
            "{u}{i}His illness blinds him to the bodies we are unable to keep away in time, what a convenience.{/i}{/u}"
            "{u}{i}He held me in his arms and even tucked me to sleep in the queen’s chambers.{/i}{/u}"
            "{u}{i}My plan couldn’t be going better than this.{/i}{/u}"
            "{u}{i}But something strange is happening…{/i}{/u}"
            "{u}{i}My allies, who stood and waited for the king while holding onto our new badges, one by one they are nowhere to be found.{/i}{/u}"
            "{u}{i}Yet they leave behind their belongings…{/i}{/u}"
            "{u}{i}So faint, yet unmistakable it is the laughter of children. {/i}{/u}"
            "{u}{i}My plan couldn’t be going better than this.{/i}{/u}"
            "{u}{i}My plan couldn’t be going better {color=#781312}than this.{/i}{/u}{/color}"
            "{u}{i}My plan couldn’t be{color=#781312} going better than this.{/i}{/u}{/color}"
            "{u}{i}{color=#781312}It is driving me insane!{/i}{/u}{/color}"
            "You drop it on the floor and decide to leave the room as there’s nothing else left to search."
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_19 = 2
        elif True:
            "Do you want to read again?"
            menu:
                "Yes" if True:
                    "The paper reads…"
                    "{u}{i}When the king returns from his hunt we all have to play our new parts. {/i}{/u}"
                    "{u}{i}It worked like a charm. The king thinks I am the sweet little prince without even questioning it.{/i}{/u}"
                    "{u}{i}His illness blinds him to the bodies we are unable to keep away in time, what a convenience.{/i}{/u}"
                    "{u}{i}He held me in his arms and even tucked me to sleep in the queen’s chambers.{/i}{/u}"
                    "{u}{i}My plan couldn’t be going better than this.{/i}{/u}"
                    "{u}{i}But something strange is happening…{/i}{/u}"
                    "{u}{i}My allies, who stood and waited for the king while holding onto our new badges, one by one they are nowhere to be found.{/i}{/u}"
                    "{u}{i}Yet they leave behind their belongings…{/i}{/u}"
                    "{u}{i}So faint, yet unmistakable it is the laughter of children. {/i}{/u}"
                    "{u}{i}My plan couldn’t be going better than this.{/i}{/u}"
                    "{u}{i}My plan couldn’t be going better {color=#781312}than this.{/i}{/u}{/color}"
                    "{u}{i}My plan couldn’t be{color=#781312} going better than this.{/i}{/u}{/color}"
                    "{u}{i}{color=#781312}It is driving me insane!{/i}{/u}{/color}"
                    jump castle_map
                "No" if True:
                    jump castle_map
        jump castle_map
    if _return == 'point 20':
        "You enter the prayer hall. "
        "Your eyes widen at the sight of the rows of skeletons sitting on the pews."
        "Their bones are bathed in the blue glow of the moss growing on the side of the walls."
        "Once again, you hear the faint sound of children laughing."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.castle_20 = 2
        $ Map.castle_21 = 1
        $ Map.castle_22 = 1

        jump castle_map
    if _return == 'point 21':
        if Map.castle_22key == 0 and Zalt.agi < 6:
            "It's a dusty podium."
            "You take a minute to survey your surroundings."
            "From where you stand you can see carvings of tiny people along the ceiling walls."
            "It seems to depict the things the people here used to do."
            "Farmers carrying crops from place to place, people buying goods from the marketplace."
            "And the lines of people gathering to bow to their king."
            "All the skeletons that lie before you, you can only imagine what their lost thoughts were as they tried to find safety here."
            "There's nothing here of interest."
            jump castle_map
        elif True:
            $ Map.castle_22 = 2
            if Zalt.agi < 6:
                "According to the note there should be a button somewhere in this podium."
                "Your hand fiddles around beneath the podium’s top until you touch a circular bulge."
            elif True:
                "It's a dusty podium."
                "You take a minute to survey your surroundings."
                "From where you stand you can see carvings of tiny people along the ceiling walls."
                "It seems to depict the things the people here used to do."
                "Farmers carrying crops from place to place, people buying goods from the marketplace."
                "And the lines of people gathering to bow to their king."
                "All the skeletons that lie before you, you can only imagine what their lost thoughts were as they tried to find safety here."
                "There's nothing here of interest."
                "{b}{color=#19c22a}<Agile Check success>{/color}"
                e 1 "Wait,what's this?"
                "Your hand fiddles around beneath the podium’s top until you touch a circular bulge."
            "You press the button."
            "Click."
            "You hear a loud rumble from the left side of the hall. The locked door is now open."
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 20*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_21 = 2
        jump castle_map
    if _return == 'point 22':
        if Map.castle_22 == 1:
            "The stone door will not open."
            "You try to push it."
            "Yeah, it won't open."
        elif Map.castle_22 == 2:
            "You enter the room."
            "The castle crypt has only two coffins inside."
            "One on each side of an altar that sits in the middle of the room. "
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_22 = 3
            $ Map.castle_23 = 1
            $ Map.castle_24 = 1
            $ Map.castle_25 = 1

        jump castle_map
    if _return == 'point 23':
        "You find pieces of paper on top of this coffin."
        "They appear to be the same written document just made into multiple copies."
        "It reads…"
        "{u}{i}Fellow jesters, bards, fire eaters and poets of the king. {/i}{/u}"
        "{u}{i}We all know of the strange event that has befallen the castle.{/i}{/u}"
        "{u}{i}People’s badges have gone missing, and the king is on the loose.{/i}{/u}"
        "{u}{i}Those blasted knights only care about protecting the nobles, giving them all the replacement badges and leaving us to fend off for ourselves.{/i}{/u}"
        "{u}{i}Our lives are in jeopardy if the king finds us without our badges.{/i}{/u}"
        "{u}{i}I say we take what’s ours from those filthy nobles and protect ourselves.{/i}{/u}"
        "{u}{i}Meet me by the crypt tonight and together we will take what’s rightfully ours.{/i}{/u}"
        "{u}{i}————The Jester{/i}{/u}"
        e 1 "So the performers in the castle formed a coup."
        e 1 "Still, I doubt their powers alone could bring the castle to such a state."
        if Map.castle_23 == 1:
            $ Map.castle_23 = 2
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump castle_map
    if _return == 'point 24':
        if Map.castle_24 == 1:
            "You approach the altar and find a key on top of it."
            show black3 at center
            show jewelkey at center with dissolve
            "You pick up the key."
            "It has a beautiful jewel in the shape of a crown."
            "You obtain the Jewel Key."
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_24 = 2
            $ jane_inv_K.take(jewel_key)
        jump castle_map
    if _return == 'point 25':
        "You walk over to the other coffin."
        "The lid appears to be slightly ajar. "
        e 1 "Hmm. "
        "You push open the coffin lid and it falls with a heavy thud."
        "Inside, there is a skeleton."
        "Right on its chest you find a badge with a jester’s hat etched on it."
        e 5 "This is it!"
        "You get the Jester’s Badge."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ jane_inv_K.take(jester_badge)
        $ Map.castle_25 = 2
        jump castle_map
    if _return == 'point 26':
        if Map.castle_26 ==1:
            "The door here has a unique carving of a knight’s helm with two swords beneath it. "
            e 1 "Wonder who’s so special to get this room?"
            "You turn the doorknob but the door is locked."
            e 12 "Damn it!"
        elif Map.castle_26 ==2:
            "Your hand reaches for the doorknob but strangely the door eerily opens itself. "
            "Your eyes blink in disbelief."
            "Nevertheless, you steady your nerves as you enter the room."
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_26 = 3
            $ Map.castle_27 = 1
            $ Map.castle_28 = 1
        jump castle_map
    if _return == 'point 27':
        if Map.castle_27 == 1:
            "The room you enter looks like it used to be an office. "
            "Disregarding the glowing moss that has taken over half of the room, most of the things here appear neatly arranged."
            "You explore the room."
            "The bookshelf on the left of the door is filled with books related to combat and survival."
            "There are collections on swordsmanship, hand to hand combat, and even a section on cooking with deadly ingredients."
            "Walking over to the desk, there’s a journal opened to the first page amidst a stack of moss covered papers and books."
            "You flip through the journal but the rest of the pages are empty."
            "The first page writes…"
            "{u}{i}I fear that the kingdom is in peril.{/i}{/u}"
            "{u}{i}We should have suspected something since two months ago when a handful of the badges disappeared for no reason.{/i}{/u}"
            "{u}{i}The phenomenon escalated in intensity since then, every few weeks groups of people would report that their badges had disappeared.{/i}{/u}"
            "{u}{i}I sent all my men out to look for the culprit but there’s not even a clue of the culprit in sight. {/i}{/u}"
            "{u}{i}The castle staff have become desperate and unruly. {/i}{/u}"
            "{u}{i}We’re just unable to make the replacement badges in time for everyone. {/i}{/u}"
            "{u}{i}Hiding from the king is not an option, not for the staff, they need the work to survive.{/i}{/u}"
            "{u}{i}I’ve tried to pool as much resources from all available parties to aid those without badges, but the noblemen refuse to help. {/i}{/u}"
            "{u}{i}I worry for my Queen’s safety, and the safety of her children.{/i}{/u}"
            "{u}{i}The top entry ends there, and a shorter paragraph is written below that.{/i}{/u}"
            "{u}{i}I’ve sent HIM to guard the treasure room.{/i}{/u}"
            "{u}{i}There are too many problems going on in the castle for me to deal with his buffoonery.{/i}{/u}"
            "{u}{i}I need competent knights to manage the chaos, at least in the treasure room he cannot break anything anymore. {/i}{/u}"
            "{u}{i}I’d send him back to his parents but I doubt they’d care about him after they dumped him on me. {/i}{/u}"
            "{u}{i}These noble cats are a pain to deal with. {/i}{/u}"
            e 13 "Whoever owns this room must be in charge of the other knights."
            e 1 "And they were dealing with badges going missing, but why would that cause so much damage to the castle?"
            "You search around some more, but find no badge in here."
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_27 = 2
        elif Map.castle_27 == 2:
            "The journal is still here."
            "Do you want to read again?"
            menu:
                "Yes" if True:
                    "The first page writes…"
                    "{u}{i}I fear that the kingdom is in peril.{/i}{/u}"
                    "{u}{i}We should have suspected something since two months ago when a handful of the badges disappeared for no reason.{/i}{/u}"
                    "{u}{i}The phenomenon escalated in intensity since then, every few weeks groups of people would report that their badges had disappeared.{/i}{/u}"
                    "{u}{i}I sent all my men out to look for the culprit but there’s not even a clue of the culprit in sight. {/i}{/u}"
                    "{u}{i}The castle staff have become desperate and unruly. {/i}{/u}"
                    "{u}{i}We’re just unable to make the replacement badges in time for everyone. {/i}{/u}"
                    "{u}{i}Hiding from the king is not an option, not for the staff, they need the work to survive.{/i}{/u}"
                    "{u}{i}I’ve tried to pool as much resources from all available parties to aid those without badges, but the noblemen refuse to help. {/i}{/u}"
                    "{u}{i}I worry for my Queen’s safety, and the safety of her children.{/i}{/u}"
                    "{u}{i}The top entry ends there, and a shorter paragraph is written below that.{/i}{/u}"
                    "{u}{i}I’ve sent HIM to guard the treasure room.{/i}{/u}"
                    "{u}{i}There are too many problems going on in the castle for me to deal with his buffoonery.{/i}{/u}"
                    "{u}{i}I need competent knights to manage the chaos, at least in the treasure room he cannot break anything anymore. {/i}{/u}"
                    "{u}{i}I’d send him back to his parents but I doubt they’d care about him after they dumped him on me. {/i}{/u}"
                    "{u}{i}These noble cats are a pain to deal with. {/i}{/u}"
                    jump castle_map
                "No" if True:
                    jump castle_map
        jump castle_map
    if _return == 'point 28':
        if Map.castle_28 == 1:
            "Just as the door opens, a strong force resists your push and immediately slams the door back."
            "The strength of the force is unnatural to be the wind."
            e 5 "Huh? Hello? Is someone there?"
            "No reply. You can hear faint breathing coming from behind the door."
            "You try to force open the door again, but it only moves slightly allowing you to peek through the small opening that you opened. "
            "There’s a window at the far right of the room, and in front of the window is a large wall of bushes."
            e 1 "Those bushes look really familiar."
            e 13 "Where have I seen them before?"
            "You try again to push against the door with your shoulders, but whatever’s behind it will not budge."
            $ Map.castle_28 = 2
            $ Map.castle_30 = 2
        elif Map.castle_28 == 2:
            "You try again to push against the door with your shoulders, but whatever’s behind it will not budge."
            "There is a slight sob behind the door."
        elif Map.castle_28 == 3:
            "You opened this door, it looks like it’s not locked at all."
            $ Map.castle_28 = 4
        jump castle_map
    if _return == 'point 29':
        "29"
        jump castle_map
    if _return == 'point 30':
        if Map.castle_30 == 0:
            "It’s a wall of dense bushes."
            "Nothing need to pay attention to."
        elif Map.castle_30 == 2:

            "Armed with the knowledge of the window behind the bushes you cut down the vegetation with your sword."
            "The window is revealed."
            "Do you want to climb in?"
            menu:
                "Yes" if True:
                    "You smash the glass with the hilt of your sword and reach out with your hand to unlock the window."
                    "You try to enter through the window but the moment your leg enters the room you’re overcomed by a strong ringing sound."
                    "Your visions shakes."
                    $ Map.castle_30 = 3
                    $ _dismiss_pause = False
                    $ renpy.music.set_volume(0, 5, channel = "Chan1")
                    scene black with vslow_dissolve
                    jump castle_point29
                "No" if True:
                    jump castle_map
            label castle_point29:
                hide screen days
                "..."
                pause 3
                scene castle 7 with vslow_dissolve
                play sound "music/body_fall.mp3"
                show screen days_S
                "You land in the room with a hard thud." with vpunch
                "Basley" "Ugh."
                "A young lion cub in embroidered clothes rushes over to you."
                "You recognize him as your younger brother."
                "Mero" "Basley, what are you doing?"
                "Mero" "You shouldn’t be climbing the window still. You’ll get hurt."
                "You smile back at your twin. "
                "Basley" "But I’m bored. Asmund’s not even playing with us."
                play sound "music/door.mp3"
                "The door from across the room swings open and a wolf walks in."
                "His heavy armor makes a clacking sound as he moves. "
                "He smiles at the two of you, and you feel reassured by his presence. "
                show asmund stand at center with slow_dissolve
                "It’s the same reassuring smile that has kept watch over you and your brother for as long as you can remember."
                "Basley" "Asmund, Asmund! You’re finally going to play with us?" with vpunch
                "Mero" "Nuh uh, nothing can beat Captain Asmund."
                "He takes a knee and pats you gently on the head."
                show asmund stand1 at center with dissolve
                asm "Your highnesses, I’m sorry I wish I could play but there’s news of some trouble happening in the prison area."
                show asmund stand at center with dissolve
                asm "I need to leave the two of you for a while so I can check in on things."
                "Basley" "No,you can’t leave us!" with vpunch
                "Basley" "You promised you’d play with us today."
                show asmund stand1 at center with dissolve
                asm "I know, but duty calls. "
                show asmund stand at center with dissolve
                asm "But I want the two of you to promise me that you’ll keep the door locked, and if trouble comes, use this whistle to summon me."
                asm "I’ll come the moment I hear it."
                "The whistle is no longer than an adult’s forefinger, painted in black and made of metal."
                asm "I’ll see you both later."
                hide asmund stand at center with slow_dissolve
                play sound "music/door.mp3"
                "He stands up and leaves through the door."
                "..."
                scene castle 7a with vslow_dissolve
                "A bright light flashes and now the room has an eerie red glow around it."
                $ renpy.music.set_volume(1, 4, channel = "Chan1")
                play Chan1[ "<silence 0.5>", "castle.ogg" ]fadein 3
                pause 3
                "There's a loud banging sound from the door. "
                "You turn to your brother but he’s hiding under the bed already."
                "You dare not move, if someone breaks in, you can’t let them find your little brother. "
                play sound"music/bangdoor.wav"
                "BANG! " with vpunch
                pause 0.5
                "The door shudders."
                play sound"music/bangdoor.wav"
                "BANG!" with vpunch
                pause 0.5
                "You hold your breath and push the door hard."
                "Asmund’s whistle is still in your hands. Now is a good time to use it."
                play sound"music/bangdoor.wav"
                "BANG!" with vpunch
                pause 0.5
                play sound"music/bangdoor.wav"
                "BANG!" with vpunch
                pause 0.5
                play sound"music/bangdoor.wav"
                "BANG!" with vpunch
                "You panic and blow hard into the whistle. "
                "But not a single note comes out of the whistle."
                "Did Asmund lie to you about the whistle?"
                play sound"music/bangdoor.wav"
                "BANG! BANG! BANG!" with vpunch
                "Tears well up in your eyes, you blow desperately again, and again."
                "But there is no noise."
                scene black with vslow_dissolve
                play sound"music/door_slam.mp3"
                pause 4
                "The door slams open."
                "And the last thing you hear is your little brother’s scream."
                "...."
                hide screen days_S
                $ renpy.music.set_volume(0.5, 0, channel = "sound")
                pause 3
                scene castle 7b with vslow_dissolve
                show screen days
                "You awaken once more with your cheeks pressing against the cool bedroom floor, just under the window."
                "You stand up and as you do, you notice you're holding something hard in the palm of your right hand."
                "It’s a black coloured metal whistle."
                "The same one in the dream… no whatever it was you saw was too vivid to be a dream. "
                "You rub your aching neck and look around the bedroom. "
                "There are no clues here."
                "Even stranger, there's no sign of the children’s remains here."
                "You wonder if they were taken away."
                "The knight never came for those children."
                "Why would he promise them that he would come if they blow this?"
                "You put the whistle to your mouth and blow."
                play sound "music/whistle.mp3"
                "Wiiiiii!" with vpunch
                stop sound
                $ renpy.music.set_volume(1, 0, channel = "sound")
                e 9 "Ah, fuck!" with vpunch
                "You pull the whistle away, and you realize what it really is."
                "It’s a special kind of whistle that produces a frequency only canines can hear."
                e 13 "If this thing actually works, then why didn’t Asmund come back?"
                e 1 "He mentioned he had to deal with trouble in the prison."
                "You consider going to the prison area to look for clues."
                $ Map.castle_29 = 1
                $ Map.castle_28 = 3
                $ Map.castle_prison_7 = 3
                $ Zalt.A_exp = Zalt.A_exp + 20*Zalt.A_exp_lv
                $ PPEXP = 20*Zalt.A_exp_lv
                "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"

                jump castle_map


        jump castle_map
    if _return == 'point 31':
        "Ahead of this hallway you see a large door with a broken sign on top that writes “Library.”"
        "To your left the path leads to two other rooms."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.castle_31 = 2
        $ Map.castle_32 = 1
        $ Map.castle_34 = 1
        $ Map.castle_35 = 1
        jump castle_map
    if _return == 'point 32':
        if jane_inv_K.qty(wing_key) == None:
            "It looks like the door is locked."
            "Above the doorknob is the picture of a wing."
        elif True:
            "It looks like the door is locked."
            "Above the doorknob is the picture of a wing."
            "You open the door with the Wing Key."
            $ Zalt.A_exp = Zalt.A_exp + 20*Zalt.A_exp_lv
            $ PPEXP = 20*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ jane_inv_K.drop(wing_key)
            $ Map.castle_32 = 2
            $ Map.castle_33 = 1
        jump castle_map
    if _return == 'point 33':
        if Map.castle_33 == 1:
            "The library is in ruins. "
            "Some shelves have been moved to the side of the door."
            "Scraps of chopped wood and torn paper litter the floor."
            "It seems that all the tables and chairs were moved to the side to make space in the middle. "
            "There you see three skeletons huddled around the remains of a fireplace."
            e 1 "What do we have here?"
            "One of the skeletons holds a piece of paper."
            "It’s a map of what looks like a church."
            "The podium in the front of the church is circled and an arrow points to it."
            e 13 "I got to check this out."
            "You search the other skeletons, and find one of them hugging a book."
            e 1 "Why are you guarding this?"
            "Your inspection reveals it to be a diary."
            "The contents detailing the day to day of this person and his friends."
            "They used to be scholars who worked for the king."
            "You notice a page with a dog-ear."
            "It reads…"
            "{u}{i}King Harald grows impatient for our progress.{/i}{/u}"
            "{u}{i}He demands we find a way to stop his sickness.{/i}{/u}"
            "{u}{i}I swear he is becoming more unhinged as time passes.{/i}{/u}"
            "{u}{i}He killed the Chief Scholar right in front of us because he could not present his badge.{/i}{/u}"
            "{u}{i}No amount of yelling could have stopped him.{/i}{/u}"
            "{u}{i}His sickness makes him stronger, but it corrupts his mind. {/i}{/u}"
            "{u}{i}Dear gods, save us all.{/i}{/u}"
            "The diary ends here."
            e 1 "Their king sounds like trouble."
            $ Zalt.A_exp = Zalt.A_exp + 20*Zalt.A_exp_lv
            $ PPEXP = 20*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_33 = 2
            $ Map.castle_22key = 1
        elif Map.castle_33 == 2:
            "One of the skeletons holds a piece of paper."
            "It’s a map of what looks like a church."
            "It seems that all the tables and chairs were moved to the side to make space in the middle. "
            "and one of them hugging the diary"
            "Do you want to read it again?"
            menu:
                "Yes" if True:
                    "It reads…"
                    "{u}{i}King Harald grows impatient for our progress.{/i}{/u}"
                    "{u}{i}He demands we find a way to stop his sickness.{/i}{/u}"
                    "{u}{i}I swear he is becoming more unhinged as time passes.{/i}{/u}"
                    "{u}{i}He killed the Chief Scholar right in front of us because he could not present his badge.{/i}{/u}"
                    "{u}{i}No amount of yelling could have stopped him.{/i}{/u}"
                    "{u}{i}His sickness makes him stronger, but it corrupts his mind. {/i}{/u}"
                    "{u}{i}Dear gods, save us all.{/i}{/u}"
                    "The diary ends here."
                    jump castle_map
                "No" if True:
                    jump castle_map

        jump castle_map
    if _return == 'point 34':
        "You enter a room with three beds next to each other."
        "Looking around, you find nothing of importance except for another diary under one of the beds."
        "It has only one entry."
        "It reads…"
        "{u}{i}I surrender… There’s no curing the king’s ailment.{/i}{/u}"
        "{u}{i}His mind is lost and so are the lives of my former colleagues. {/i}{/u}"
        "{u}{i}I will join my colleagues in hiding soon.{/i}{/u}"
        "{u}{i}My only concern is where the other library key has disappeared to.{/i}{/u}"
        "{u}{i}I remember I had it last in the room in front of the queen’s quarters.{/i}{/u}"
        "There’s nothing left to be found in this room."
        if Map.castle_34 == 1:
            $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
            $ PPEXP = 10*Zalt.A_exp_lv
            "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
            $ Map.castle_34 = 2
        jump castle_map
    if _return == 'point 35':
        scene castle 5 with slow_dissolve
        "Before you can enter the room, a dark figure emerges from the ground and attacks you."
        $ Map.castle_ghost = 35
        jump battle_GhostC
    if _return == 'point 36':
        "The path ahead is blocked. A lone skeleton leans against the blockade."
        "It appears to be holding something in its hands."
        show black3 at center
        show leafkey at center with dissolve
        "It’s a key with a leaf shaped bow at its end."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "You get the leaf key."
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ jane_inv_K.take(leaf_key)
        $ Map.castle_36 = 2
        $ Map.castle_4key = 1
        jump castle_map
    if _return == 'point 37':
        "You enter a large space with nothing much inside."
        "Two targets are placed across the room, and you see broken training dummies lying on the floor."
        "This must have been the training room for the knights."
        "Looking around, you find nothing of importance."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.castle_37 = 2
        jump castle_map
    if _return == 'point 38':
        "This looks like the mess hall."
        "A long table stretches from one end of the room to the other. "
        "There are several bottles on the table that still contain some kind of liquid."
        "You pick a bottle up and uncork it."
        "Bringing your snout close to the mouth of the bottle, you sniff the content of the water."
        e 1 "It smells like beer? "
        e 13 "But this thing must have been here for hundreds of years how can it not go bad?"
        "You’re tempted to try a sip."
        "You bring the bottle close to your lips, but then you push it away."
        e 5 "No, no. I could get some weird sickness."
        e 5 "But then…"
        "You bring it close to you, then you push it away again."
        e 9 "No! [name], don’t."
        "The bottle tempts you. You find your willpower breaking."
        e 15 "Ughh! I’m thirsty!"
        "You take a swig from the bottle and you’re pleasantly surprised that it tastes like regular beer."
        e 6 "Not bad. Guess I’ll take some for the road."
        "You get 2 beer."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ jane_inv.take(beer,2)
        $ Map.castle_38 = 2

        jump castle_map
    if _return == 'point 39':
        "There are several beds inside this room. "
        "They all look unkept as though the owners were in a hurry when they left and never came back."
        "You look around the beds and manage to find a few bags of coins."
        "You get 120 coins."
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        $ Map.castle_39 = 2
        $ jane_inv.take(coin,120)
        jump castle_map
    if _return == 'point 40':
        if Map.castle_40 == 1:
            e 1 "It seems here is the way to the prison."
            "You head down to the prison area."
            $ Map.castle_40 = 2
            jump castle_map
        elif True:
            jump castle_prison

        jump castle_map
    if _return == 'point 41':
        $ renpy.music.set_volume(0, 4, channel = "Chan1")

        scene castle 6 with vslow_dissolve
        $ renpy.music.set_pause(True, channel='Chan1')
        "You enter a huge hall, its dimensions make it large enough to fit everyone from the bull tribe and then some."
        "The tapestries that hang by the walls now have lost their luster and are slowly being consumed by the moss."
        "Remnants of the dead have fused with the moss all around, giving you the sense of walking through a graveyard."
        "Of greater concern for you is what lies ahead."
        "The king’s throne and standing between you and it is the back of a solemn figure."
        play Chan2 "music/danger.ogg"
        $ renpy.music.set_pause(False, channel='Chan2')
        $ renpy.music.set_volume(0.5, 4, channel = "Chan2")
        "A long blue robe covers its form."
        e 5 "I’m surprised there’s still someone around here."
        "Without turning its back, you can see the figure’s hand move to its hip before drawing out a blade."
        "King" "Halt, who dares to approach the domains of King Harald?" with vpunch
        "King" "Present your badge or consider your life forfeited!"
        "King" "You have until the count of 3."
        "King" "1."
        "King" "2."
        menu:
            "Show 'Jester badge'" if jane_inv_K.qty(jester_badge) == 1:
                "King" "3!" with vpunch
                "You raise the Jester Badge."
                $ renpy.music.set_volume(1, 4, channel = "Chan2")
                "The moment the figure turns, your tail curls between your legs at the sight of his ghastly face."
                "Your right foot takes a step back."
                show harald stand1 at center with vslow_dissolve
                "King" "You! A jester! I thought I got rid of every last one of you since the last rebellion!"
                "King" "You have some balls to show up here."
                "His right eye glows a haunting blue and the sword he holds ignites with ethereal blue flames."
                e 9 "No, wait I’m not a jester!"
                "King" "The badge doesn’t lie!"
                hide harald stand1 with dissolve
                "The king rushes at you for an attack."
                e 9 "(What have I done?!)"
                "You felt the king’s anger, but now you can’t regret it!"
                "You draw your sword as he rushes towards you, ready to kill."
                $ Map.castle_king = "jester"
                jump battle_king
            "Show 'Knight badge'" if jane_inv_K.qty(knight_badge) == 1:
                "King" "3!" with vpunch
                "You raise the Knight Badge."
                $ renpy.music.set_volume(1, 4, channel = "Chan2")
                "The moment the figure turns, your tail curls between your legs at the sight of his ghastly face."
                "Your right foot takes a step back."
                show harald stand1 at center with vslow_dissolve
                "King" "Asmund..."
                "The king’s one good eye widens."
                "King" "You were supposed to protect the queen!"
                "King" "You were supposed to protect the people!"
                "King" "I know you are a loyal subordinate."
                "King" "But i have to punish you."
                "You feel his deep sadness."
                e 9 "No, wait I’m not Asmund!"
                "King" "Pay for your failure with your life."
                "His right eye glows a haunting blue and the sword he holds ignites with ethereal blue flames."
                hide harald stand1 with dissolve
                "The king rushes towards you for an attack."
                $ Map.castle_king = "knight"
                jump battle_king
            "Show 'Prince badge'" if jane_inv_K.qty(prince_badge) == 1:
                "King" "3!" with vpunch
                $ Map.castle_king = "prince"
                "You raise the Prince Badge."
                stop Chan2 fadeout 3
                "The moment the figure turns, you see the withered and tired face of a white lion."
                "The incredulous expression of his face highlights the tiredness in his blue eyes."
                show harald stand at center with slow_dissolve
                "King" "Mero? Is that you?"
                hide harald stand at center with slow_dissolve
                "The king drops his sword and he approaches you slowly."
                "King" "Mero my son."
                "He has his hands outstretched calling to you."
                "King" "Mero, come to papa. I thought I lost you."
                "You gulp and nervously approach the king."
                "He pulls you in for a hug and holds you tight."
                "King" "Thank goodness I’ve found you."
                "King" "Now that you’re back we can go find mama and Basil."
                "King" "We’ll be a family again."
                "Your heart feels heavy at his words."
                "You hesitate but you return his hug."
                show harald stand at center
                with flashbulb
                hide harald stand at center with vslow_dissolve
                "Then your body is bathed in yellow light and you watch awestruck as the king’s body disappears."
                "The loud noise of what sounds like gears turning draws your attention."
                "The stone throne in front of you splits into two and opens up a pathway."
                "There is something on the floor"
                show black3 at center
                show kidbook at center with dissolve
                "It's a storybook."
                e 13 "I wonder how many times I can meet people who aren’t really my father."
                "You pick up the storybook and leave."
                $ Zalt.A_exp = Zalt.A_exp + 50*Zalt.A_exp_lv
                $ PPEXP = 50*Zalt.A_exp_lv
                "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
                $ jane_inv_E.take(kid_book)
                $ Map.castle_42 = 1
                $ Map.castle_41 = 2
                jump castle_map
            "Show nothing" if True:
                "King" "3!" with vpunch
                $ renpy.music.set_volume(1, 4, channel = "Chan2")
                "The moment the figure turns, your tail curls between your legs at the sight of his ghastly face."
                show harald stand1 at center with slow_dissolve
                "King" "A monster! When will your kind stop pursuing me?!"
                e 9 "I’m no monster!"
                "King" "You’ve sealed your fate coming here, creature."
                "King" "I won’t let you break my kingdom again as you did on the day of my hunt!"
                "King" "Die!"
                hide harald stand1 with dissolve
                "The king’s blade is engulfed in ethereal blue flames."
                $ Map.castle_king = "monster"
                e 9 "(What have I done?!)"
                "You felt the king’s anger, but now you can’t regret it!"
                "You draw your sword as he rushes towards you, ready to kill."
                jump battle_king
        jump castle_map
    if _return == 'point 42':
        if Map.undercity_1 == 0:
            "You are leaving the dungeon area."
            "If you continue to move forward, your A-LV will reset back to 0."
            "Do you want to go forward?"
            menu:
                "Yes" if True:
                    $ Zalt.A_exp = 0
                    $ Zalt.A_lv = 0
                    $ Zalt.dungeon = False
                    $ Zalt.Dungeon_leave = False
                    "You leave the dungeon."
                    $ config.rollback_enabled = True
                "No" if True:

                    jump castle_map

            $ renpy.music.set_volume(0.1, 4, channel = "Chan1")
            scene black with slow_dissolve
            "You head down the secret passageway."
            "Its route is narrow and long, but all you are concerned about is reaching Flo."
            "Every step forward feels like you are plunging deeper into the depths of the earth."
            "When you come to the foot of the steps, a rusty metal gate blocks your way."
            $ Map.undercity_1 = 1
            $ Map.undercity_2 = 1
            jump undercity_map0
        elif True:
            $ Zalt.A_exp = 0
            $ Zalt.A_lv = 0
            $ Zalt.dungeon = False
            $ Zalt.Dungeon_leave = False
            $ config.rollback_enabled = True
            jump undercity_map0
    if _return == 'point 43':
        "You reach the center of the building."
        "Three paths branch out from where you stand. "
        "One path leads down a dark flight of stairs."
        "If this place is anything like the castles in the stories, going down would be where the knights keep their prisoners."
        $ Map.castle_43 = 2
        $ Map.castle_31 = 1
        $ Map.castle_36 = 1
        $ Map.castle_37 = 1
        $ Map.castle_38 = 1
        $ Map.castle_39 = 1
        $ Map.castle_40 = 1
        $ Zalt.A_exp = Zalt.A_exp + 10*Zalt.A_exp_lv
        $ PPEXP = 10*Zalt.A_exp_lv
        "{color=#19c22a}You get {b}[PPEXP]{/b} A-EXP.{/color}"
        jump castle_map
    if _return == 'point 44':
        scene castle 3 with vslow_dissolve
        "As you approach the entrance to the dark space, a phantom emerges from the ground and attacks you!"
        $ Map.castle_ghost = 44

        jump battle_GhostC
screen castle_map:

    imagemap:
        if Map.castle_42 == 2:
            idle 'castle_map1'
            hover 'castle_map1'
        else:
            idle 'castle_map'
            hover 'castle_map'
        if Map.castle_3 != 2:
            add "map/fog/castle_fog_1.png"
        if Map.castle_4 != 2:
            add "map/fog/castle_fog_2.png"
        if Map.castle_7 !=2:
            add "map/fog/castle_fog_3.png"
        if Map.castle_14 !=2:
            add "map/fog/castle_fog_4.png"
        if Map.castle_44 != 2:
            add "map/fog/castle_fog_5.png"
        if Map.castle_22 != 3:
            add "map/fog/castle_fog_6.png"
        if Map.castle_8 !=2:
            add "map/fog/castle_fog_7.png"
        if Map.castle_26 != 3:
            add "map/fog/castle_fog_8.png"
        if Map.castle_29 != 1:
            add "map/fog/castle_fog_9.png"
        if Map.castle_32 != 2:
            add "map/fog/castle_fog_10.png"
        if Map.castle_31 != 2:
            add "map/fog/castle_fog_11.png"
        if Map.castle_9 != 3:
            add "map/fog/castle_fog_12.png"

        vbox:
            xalign 0.52 ypos 0.81
            imagebutton:
                idle "UI/down button1.png"
                hover "UI/down button2.png"

                action Return("exit")


        vbox:
            xalign 0.425 ypos 0.783
            if Map.castle_2 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 2")
            elif Map.castle_2 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 2")
            else:
                pass
        vbox:
            xalign 0.425 ypos 0.6
            if Map.castle_3 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 3")
            else:
                pass
        vbox:
            xalign 0.365 ypos 0.68
            if Map.castle_4 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 4")

            else:
                pass
        vbox:
            xalign 0.32 ypos 0.66
            if Map.castle_5 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 5")
            elif Map.castle_5 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.427 ypos 0.46
            if Map.castle_6 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 6")
            elif Map.castle_6 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.325 ypos 0.51
            if Map.castle_7 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 7")
            elif Map.castle_7 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.53 ypos 0.51
            if Map.castle_8 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 8")
            elif Map.castle_8 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.45 ypos 0.4
            if Map.castle_9 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 9")
            elif Map.castle_9 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 9")
            else:
                pass
        vbox:
            xalign 0.165 ypos 0.51
            if Map.castle_10 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 10")
            else:
                pass
        vbox:
            xalign 0.13 ypos 0.5
            if Map.castle_11 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 11")
            elif Map.castle_11 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 11")
            else:
                pass
        vbox:
            xalign 0.13 ypos 0.6
            if Map.castle_12 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 12")
            elif Map.castle_12 == 2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 12")
            else:
                pass
        vbox:
            xalign 0.165 ypos 0.63
            if Map.castle_13 == 1 and Map.castle_14 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 13")
            elif Map.castle_13 == 1 and Map.castle_14 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.18 ypos 0.575
            if Map.castle_14 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 14")
            else:
                pass
        vbox:
            xalign 0.215 ypos 0.65
            if Map.castle_15 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 15")
            elif Map.castle_15 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.148 ypos 0.71
            if Map.castle_16 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 16")
            else:
                pass
        vbox:
            xalign 0.13 ypos 0.71
            if Map.castle_17 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 17")
            elif Map.castle_17 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.166 ypos 0.8
            if Map.castle_18 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 18")
            elif Map.castle_18 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.23 ypos 0.79
            if Map.castle_19 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 19")
            elif Map.castle_19 == 2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 19")
            else:
                pass
        vbox:
            xalign 0.165 ypos 0.4
            if Map.castle_20 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 20")
            elif Map.castle_20 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.165 ypos 0.22
            if Map.castle_21 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 21")
            elif Map.castle_21 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.13 ypos 0.18
            if Map.castle_22 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 22")
            elif Map.castle_22 == 2:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 22")
            else:
                pass
        vbox:
            xalign 0.13 ypos 0.1
            if Map.castle_23 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 23")
            elif Map.castle_23 == 2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 23")
            else:
                pass
        vbox:
            xalign 0.165 ypos 0.1
            if Map.castle_24 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 24")
            elif Map.castle_24 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.198 ypos 0.1
            if Map.castle_25 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 25")
            elif Map.castle_25 == 2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.582 ypos 0.54
            if Map.castle_26 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 26")
            elif Map.castle_26 ==2:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 26")
            else:
                pass
        vbox:
            xalign 0.59 ypos 0.61
            if Map.castle_27 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 27")
            elif Map.castle_27 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 27")
            else:
                pass
        vbox:
            xalign 0.61 ypos 0.64
            if Map.castle_28 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 28")
            elif Map.castle_28 ==2 or Map.castle_28 ==3:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 28")
            else:
                pass
        vbox:
            xalign 0.59 ypos 0.7
            if Map.castle_29 == 1:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.525 ypos 0.71
            if Map.castle_30 != 3:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 30")
            elif Map.castle_30 ==3:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.638 ypos 0.625
            if Map.castle_31 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 31")
            elif Map.castle_31 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.638 ypos 0.68
            if Map.castle_32 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 32")
            else:
                pass
        vbox:
            xalign 0.642 ypos 0.788
            if Map.castle_33 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 33")
            elif Map.castle_33 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 33")
            else:
                pass

        vbox:
            xalign 0.71 ypos 0.58
            if Map.castle_34 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 34")
            elif Map.castle_34 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 34")
            else:
                pass
        vbox:
            xalign 0.7 ypos 0.675
            if Map.castle_35 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 35")
            elif Map.castle_35 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.7 ypos 0.51
            if Map.castle_36 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 36")
            elif Map.castle_36 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.605 ypos 0.36
            if Map.castle_37 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 37")
            elif Map.castle_37 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.66 ypos 0.40
            if Map.castle_38 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 38")
            elif Map.castle_38 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.66 ypos 0.32
            if Map.castle_39 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 39")
            elif Map.castle_39 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.638 ypos 0.24
            if Map.castle_40 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 40")
            elif Map.castle_40 ==2:
                imagebutton:
                    idle "UI/up button1.png"
                    hover "UI/up button2.png"
                    action Return("point 40")
            else:
                pass

        vbox:
            xalign 0.427 ypos 0.23
            if Map.castle_41 == 1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("point 41")
            elif Map.castle_41 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.427 ypos 0.1
            if Map.castle_42 == 1:
                imagebutton:
                    idle "UI/up button1.png"
                    hover "UI/up button2.png"
                    action Return("point 42")
            else:
                pass

        vbox:
            xalign 0.64 ypos 0.51
            if Map.castle_43 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 43")
            else:
                pass

        vbox:
            xalign 0.165 ypos 0.45
            if Map.castle_44 == 1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("point 44")
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


label castle_prison0:
    stop music
    stop Thane
    stop Chan1
    stop Chan2
    $ renpy.music.set_volume(1, 1, channel = "Chan1")
    jump castle_prison


label castle_prison:
    stop music
    hide screen simple_stats_screen_s
    hide screen battle_menu_s
    $ Time.mins = Time.mins +10
    $ Zalt.dungeon = True
    $ config.rollback_enabled = False
    $ renpy.music.set_volume(1, 5, channel = "Chan1")
    $ renpy.music.set_pause(False, channel='Chan1')
    window hide None
    if Zalt.Dungeon_leave:
        jump Cave_leave
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    if Zalt.A_exp >= 100:
        $ Zalt.A_exp = Zalt.A_exp -100
        $ Zalt.A_lv = min(Zalt.A_lv + 1, 5)
        $ Zalt.AP = Zalt.AP +1
        "You get one AP, you have [Zalt.AP] now."
        "Your A-LV now is [Zalt.A_lv]"


    if Zalt.A_lv == 5:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 4:
        $ Zalt.A_exp_lv = 2.5
    elif Zalt.A_lv == 3:
        $ Zalt.A_exp_lv = 2
    elif Zalt.A_lv == 2:
        $ Zalt.A_exp_lv = 1.5
    elif Zalt.A_lv == 1:
        $ Zalt.A_exp_lv = 1.2
    elif True:
        $ Zalt.A_exp_lv = 1

    scene prison 1


    if Map.castle_prison_1 ==0:
        show prison_fog_1
    if Map.castle_prison_2 ==1:
        show prison_fog_2
    if Map.castle_prison_3 ==1 or Map.castle_prison_4 ==1:
        show prison_fog_3



    call screen castle_prison with dissolve
    if _return == 'P_exit':
        if Map.castle_prison_1 ==0:

            "You tread carefully down the flight of stairs."
            "The damp walls and musky smell of the lower area plays havoc with your senses."
            "With every step taken, you swear that you can hear another pair echoing from behind."
            "However you are met with nothing when you turn your head back."
            "You quicken your pace when you catch sight of the bottom of the staircase..."
            "Suddenly, your breath turns cold and something hits you hard on the back of the head." with vpunch
            $ _dismiss_pause = False
            scene black with vslow_dissolve
            play sound "music/body_fall.mp3"
            "Your vision blurs and you fall."
            hide screen days
            $ renpy.music.set_volume(0, 5, channel = "Chan1")
            "..."
            "...."
            pause 2
            scene prison 1a with vslow_dissolve
            "Your eyes flutter open."
            "It takes your brain a minute to register that your face is lying against the cold floor. "
            "You try to pick yourself up, but your arms wobble under the weight of your body."
            "Although you stumble on your feet you manage to move forward and grab onto the prison bars."
            "The hallway in front of you is well lit."
            "You try to call out for help, but your throat is too dry to make a sound."
            "You turn around desperate for some food or water. It’s been days since you’ve been in here."
            scene black with vslow_dissolve
            "..."
            "...."
            pause 2
            show screen days_S
            scene prison 1a with vslow_dissolve
            "Your captor never even bothered to keep you fed, forcing you to survive on the glowing moss that lines the inside of your jail cell."
            "It won’t be long before you succumb to exhaustion."
            scene black with vslow_dissolve
            "..."
            "...."
            pause 2
            scene prison 1a with vslow_dissolve
            "You must escape!"
            $ renpy.music.set_volume(1, 5, channel = "Chan1")
            "You reach for the cell door, and to your surprise it’s not locked."
            "This is your chance!"
            $ Map.castle_prison_1 = 1
            $ Map.castle_prison_2 = 2
            $ Map.castle_prison_3 = 1

            jump castle_prison
        elif True:
            jump castle_map
        return
    if _return == 'P_point 2':
        if Map.castle_prison_2 == 4:
            "It's the jail cell that you saw in that weird dream you had."
            "There's nothing of interest left in here."
            "But... there seems to be a little bit different here."
            "This room is even more dilapidated than you dreamed it."
            "As if it had been a long time."
            $ Map.castle_prison_2 = 5
        elif Map.castle_prison_2 == 5:
            "It's the jail cell that you saw in that weird dream you had."
            "There's nothing of interest left in here"
        jump castle_prison
        return
    if _return == 'P_point 3':
        if Map.castle_prison_3 == 1:
            "You push the door away and make your escape."
            "There’s a large bloodstain on the floor."
            "Too much to be a mere cut."
            "Strange, there isn’t a body anywhere."
            "If this was a usual situation you would be more concerned by what you found."
            "But all you have on your mind is to escape."
            "As you continue walking you sense something following you from behind."
            "Only your footsteps can be heard."
            $ Map.castle_prison_3 = 2
            $ Map.castle_prison_4 = 1
        elif Map.castle_prison_3 == 4:
            "It is an empty corridor. "
            "Clank!"
            "You jump up in surprise. It sounded like chains falling."
            "Considering what you've seen you rather not take a chance on what that sound really is."
            "You press on ahead."
            $ Map.castle_prison_2 = 4
            $ Map.castle_prison_3 = 5
        jump castle_prison
        return
    if _return == 'P_point 4':
        if Map.castle_prison_4 == 1:
            "You stop just before the corner when you hear the sound of heavy footsteps coming from the other side."
            jump battle_S_knight
        elif Map.castle_prison_4 == 3:
            "As you walk down the corridor you stop to notice a pile of glowing moss. "
            "The moss feels wet to the touch."
            "For a few seconds the part of the moss you touch loses its glow, but regains it later."
            "You smile a bit at how fun it is to touch the moss."
            "You spend some time touching the moss."
            "It helps to calm you down."
            $ Map.castle_prison_4 = 4
            $ Map.castle_prison_3 = 4
            if Map.castle_prison_7 == 0:
                $ Map.castle_prison_7 = 1

        jump castle_prison
        return
    if _return == 'P_point 5':
        if Map.castle_prison_5 ==1:
            "This room has a large table with several wooden plates, cups and cutlery covered in dust. "
            "Looking around you find a HP potion under the table with a note tied to it."
            "The note reads…"
            "{u}{i}Confiscated this item off the Duke Choron after arresting him for stabbing a duchess with a butter knife.{/i}{/u}"
            "{u}{i}Suspected he stabbed her for her badge.{/i}{/u}"
            "{u}{i}Put it in the evidence pile with the rest. {/i}{/u}"
            "{u}{i}P.S.\nThe duke and duchess didn’t have their badges on them.\n——————Harold{/i}{/u}"
            e 1 "What could have caused these people to stab each other for badges? "
            $ Map.castle_prison_5 = 2
        elif Map.castle_prison_5 ==2:
            "The note is still here."
            "Do you want to read it again?"
            menu:
                "Yes" if True:
                    "The note reads…"
                    "{u}{i}Confiscated this item off the Duke Choron after arresting him for stabbing a duchess with a butter knife.{/i}{/u}"
                    "{u}{i}Suspected he stabbed her for her badge.{/i}{/u}"
                    "{u}{i}Put it in the evidence pile with the rest. {/i}{/u}"
                    "{u}{i}P.S.\nThe duke and duchess didn’t have their badges on them.\n——————Harold{/i}{/u}"
                    jump castle_prison
                "No" if True:
                    jump castle_prison

        jump castle_prison
        return
    if _return == 'P_point 6':
        if Map.castle_prison_6 ==1:
            scene prison 5 with slow_dissolve
            "You enter a room with empty shelves lining the walls."
            "The doors that previously sealed this room lie broken on the floor."
            "There are deep gashes on the body of the door like someone took an axe and chopped at the door until it gave way."
            "You approach the shelve closest to the first door."
            "There are broken bottles and mismatched tools that shouldn’t be together."
            e 1 "A pair of scissors and a foot trap?"
            e 1 "Is that… a bag of moldy beans? "
            "This whole place used to be some kind of dungeon judging by the jail cells."
            "You imagine that they stored the criminals belongings or contrabands here. "
            "You walk over to the next shelf."
            "You reach out to touch the shelf when suddenly it morphs into a phantom’s maw."
            e 5 "!!"
            "You pull your hand back before it clamps onto it and quickly draw your sword."
            $ Map.castle_ghost = 61
            jump battle_GhostC
        elif Map.castle_prison_6 ==2:
            scene prison 5 with slow_dissolve
            e 13 "Great, so I got to be careful of inanimate objects now?"
            "You look at the remaining shelves in the room."
            "Should you check them?"
            menu:
                "Yes" if True:
                    "You gulp and towards the next shelf across the room."
                    "After all, you can’t be an adventurer if you didn’t take risks."
                    "You take a step forward and the shelf in front of you transforms into a phantom."
                    "It speeds towards you with an ear piercing screech."
                    $ Map.castle_ghost = 62
                    jump battle_GhostC
                "No" if True:
                    e 13 "No, it’s an unnecessary risk."
                    e 1 "This room has been raided anyways. "
                    jump castle_prison
        jump castle_prison
        return
    if _return == 'P_point 7':
        if Map.castle_prison_7 ==1:
            "It’s a skeleton."
            "It was cut by something in half."
            "You can't find its head."
        elif Map.castle_prison_7 ==3:
            "It’s a skeleton."
            "It was cut by something in half."
            "You can't find its head."
            "The whistle in your hand suddenly pulses." with vpunch
            e 5 "Huh?"
            "You sense that you need to use the whistle."
            menu:
                "Blow the whistle" if True:
                    "You bring it up to your mouth and blow the whistle."
                    jump battle_knight
                "Not yet" if True:
                    jump castle_prison
        jump castle_prison
        return
screen castle_prison:

    imagemap:
        idle 'prison_map'
        hover 'prison_map'
        if Map.castle_prison_1 ==0:
            add "map/fog/prison_fog_1.png"
        if Map.castle_prison_2 ==1:
            add "map/fog/prison_fog_2.png"
        if Map.castle_prison_3 ==1 or Map.castle_prison_4 ==1:
            add "map/fog/prison_fog_3.png"

        vbox:
            xalign 0.48 ypos 0.81
            if Map.castle_prison_1 ==0:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"

                    action Return("P_exit")
            elif Map.castle_prison_1 ==1:
                pass
            else:
                imagebutton:
                    idle "UI/down button1.png"
                    hover "UI/down button2.png"

                    action Return("P_exit")

        vbox:
            xalign 0.215 ypos 0.73
            if Map.castle_prison_2 ==1:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            elif Map.castle_prison_2 ==2 or Map.castle_prison_2 ==5:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            elif Map.castle_prison_2 ==4:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("P_point 2")
            else:
                pass
        vbox:
            xalign 0.3 ypos 0.68
            if Map.castle_prison_3 ==1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("P_point 3")
            elif Map.castle_prison_3 ==2 or Map.castle_prison_3 ==5:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            elif Map.castle_prison_3 ==4:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("P_point 3")
            else:
                pass
        vbox:
            xalign 0.35 ypos 0.35
            if Map.castle_prison_4 ==1:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("P_point 4")
            elif Map.castle_prison_4 ==2:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            elif Map.castle_prison_4 ==3:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("P_point 4")
            elif Map.castle_prison_4 ==4:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
        vbox:
            xalign 0.58 ypos 0.6
            if Map.castle_prison_5 ==1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("P_point 5")
            elif Map.castle_prison_5 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("P_point 5")

            else:
                pass

        vbox:
            xalign 0.58 ypos 0.18
            if Map.castle_prison_6 ==1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("P_point 6")
            elif Map.castle_prison_6 ==2:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("P_point 6")
            elif Map.castle_prison_6 ==3:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass

        vbox:
            xalign 0.18 ypos 0.35
            if Map.castle_prison_7 ==1:
                imagebutton:
                    idle "UI/button1.png"
                    hover "UI/button2.png"
                    action Return("P_point 7")
            elif Map.castle_prison_7 ==3:
                imagebutton:
                    idle "UI/ebutton1.png"
                    hover "UI/ebutton2.png"
                    action Return("P_point 7")
            elif Map.castle_prison_7 ==4:
                imagebutton:
                    idle "UI/button4.png"
                    hover "UI/button4.png"
            else:
                pass
    if Map.castle_prison_1 !=1:
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




label battle_S_knight:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 9999
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0
    scene prison 2 with slow_dissolve
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')
    $ _dismiss_pause = False
    $ Battle.holyfcd = 0
    stop music
    play Chan2 "music/danger.ogg"
    $ renpy.music.set_pause(False, channel='Chan2')
    $ renpy.music.set_volume(0.1, 1, channel = "Chan2")
    $ renpy.music.set_volume(1.8, 0, channel = "music")
    play music"music/metal_drag.ogg"
    "Turning around to your cell, your instincts tell you to run back, but it’s too late."
    "The sound is approaching."
    "..."





    jump battle_S_knight_loop


label battle_S_knight_loop:


    $ config.rollback_enabled = False
    show screen simple_stats_screen_s
    show screen battle_menu_s





    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False

        if res == "Recoil":
            "You flinch back in fear."
        if res == "Tremble":
            "You try to hide in a corner, holding onto your legs for your life."
            "You are unable to fight back."
        if res == "Cry":
            "You cry and beg for mercy."
        if res == "Scream":
            "You scream in terror."
        if res == "Run":
            "You try to run but your legs are paralyzed by fear, you’re unable to stand up."
        elif True:
            pass



        $ Battle.S_knight = Battle.S_knight +1
        if Battle.S_knight == 1:
            show nohead knight with vslow_dissolve:
                zoom 0.01
                xalign 0.5 yalign 0.45
            $ renpy.music.set_volume(0.3, 1, channel = "Chan2")
            "The footsteps grow louder and louder."
            pause 3
        elif Battle.S_knight == 2:
            show nohead knight with vslow_dissolve:
                zoom 0.05
                xalign 0.5 yalign 0.45
            $ renpy.music.set_volume(0.5, 1, channel = "Chan2")
            "The outline of the figure comes into view."
            pause 10
        elif Battle.S_knight == 3:
            show nohead knight with vslow_dissolve:
                zoom 0.5
            $ renpy.music.set_volume(0.8, 3, channel = "Chan2")
            "The figure emerges from the shadows, a headless warrior dragging his bloodied jagged sword on the ground approaches you."
            pause 10
        elif Battle.S_knight == 4:
            show nohead knight with vslow_dissolve:
                zoom 0.8
            "..........."
            $ renpy.music.set_volume(1, 3, channel = "Chan2")
            pause 4
        elif Battle.S_knight == 5:
            show nohead knight with vslow_dissolve:
                zoom 1.2
            "......"
            pause 4
        elif Battle.S_knight == 6:
            show red1 at center with slow_dissolve
            play sound "music/blood.ogg"
            "The headless warrior grabs you by the throat and throws you against a wall." with vpunch
            pause 4

        elif Battle.S_knight == 7:
            hide nohead knight with slow_dissolve
            show red2 at center with dissolve
            play sound "music/blood.ogg"
            scene black with dissolve
            $ renpy.music.set_volume(1, 0, channel = "music")
            stop music
            "The headless warrior raises his jagged blade and cuts you in half."
            pause 1
            play sound "music/blood.ogg"
            hide screen simple_stats_screen_s
            hide screen battle_menu_s
            pause 0.5
            "You" "AHHHHHHHHHHH!"

            play sound "music/blood.ogg"
            pause 0.5
            play sound "music/blood.ogg"
            "...."
            "..."
            ".."
            hide screen days_S
            pause 10
            $ renpy.music.set_volume(0, 4, channel = "Chan2")
            jump battle_S_knight_end






    if wolf_hp <= -1:
        if Zalt.hp <= -1:
            jump battle_S_knight_end
        elif True:

            jump battle_S_knight_end

    elif Zalt.hp <= -1:
        jump battle_S_knight_end
    elif True:

        jump battle_S_knight_end


label battle_S_knight_end:

    stop music fadeout 1

    stop Chan2
    $ _dismiss_pause = False
    hide red2 at center with dissolve
    "...."
    scene prison 1 with vslow_dissolve
    show screen days
    e 2 "Ugh, my head…"

    "You pick yourself back up from the floor. "
    $ renpy.music.set_pause(False, channel='Chan1')
    play Chan1[ "<silence 0.5>", "music/castle.ogg" ]fadein 3
    "Looking around you notice you’re at the foot of the stairs you were walking down from."
    "You scratch your head."
    e 13 "Was that all just a dream?"
    $ renpy.music.set_volume(0.2, 0, channel = "sound")
    "That whole experience, the jail, the creature, the ending… it was just too real."
    "You hold your neck."
    play sound "music/whistle.mp3"
    "Your ears then twitch to the sound of a whistle coming from upstairs. " with vpunch
    "Its high pitch hurts your ears."
    $ renpy.music.set_volume(1, 1, channel = "sound")
    e 9 "What the heck is that?"
    "The noise then stops and is replaced by the sound of a door slamming open."
    "Something upstairs has changed."
    $ Map.castle_prison_1 = 3
    $ Map.castle_prison_2 = 3
    $ Map.castle_prison_3 = 3
    $ Map.castle_prison_4 = 3
    $ Map.castle_prison_5 = 1
    $ Map.castle_prison_6 = 1
    $ Map.castle_26 = 2

    jump castle_prison

    return


screen simple_stats_screen_s:
    frame:
        xalign 0.02 yalign 0.95
        xminimum 220 xmaximum 220
        has vbox
        text "■■■■■■" size 22 xalign 0.5
        null height 5
        text "HP" size 16
        hbox:
            bar:
                xmaximum 130
                value 1
                range Zalt.maxhp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None

            null width 5


            text "1 / [Zalt.maxhp]" size 16
        text "MP" size 16
        hbox:

            bar:
                xmaximum 130
                value 0
                range Zalt.maxmp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None


            null width 5


            text " {color=#0080c0}0 / [Zalt.maxmp]{/color}" size 16
        text "HORROR" size 16
        hbox:

            bar:
                xmaximum 130
                value 100
                range 100
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None


            null width 5


            text "100 / 100" size 16


screen battle_menu_s:
    vbox:
        xalign 0.3 ypos 0.7
        hbox:

            frame:
                if Battle.S_knight < 6:
                    if players_turn:
                        textbutton "Recoil" action Return("Recoil") yminimum 40
                    else:
                        textbutton "Recoil" action None yminimum 40
                else:
                    if players_turn:
                        textbutton "Scream" action Return("Scream") yminimum 40
                    else:
                        textbutton "Scream" action None yminimum 40
    vbox:
        xalign 0.4 ypos 0.7
        hbox:

            frame:
                if Battle.S_knight < 6:
                    if players_turn:
                        textbutton "Tremble" action Return("Tremble") yminimum 40
                    else:
                        textbutton "Tremble" action None yminimum 40
                else:
                    if players_turn:
                        textbutton "Scream" action Return("Scream") yminimum 40
                    else:
                        textbutton "Scream" action None yminimum 40

    vbox:
        xalign 0.5 ypos 0.7
        hbox:

            frame:
                if players_turn:
                    textbutton "Scream" action Return("Scream") yminimum 40
                else:
                    textbutton "Scream" action None yminimum 40
    vbox:
        xalign 0.6 ypos 0.7
        hbox:

            frame:
                if Battle.S_knight < 6:
                    if players_turn:
                        textbutton "Cry" action Return("Cry") yminimum 40
                    else:
                        textbutton "Cry" action None yminimum 40
                else:
                    if players_turn:
                        textbutton "Scream" action Return("Scream") yminimum 40
                    else:
                        textbutton "Scream" action None yminimum 40

    vbox:
        xalign 0.7 ypos 0.7
        hbox:

            frame:
                if Battle.S_knight < 6:
                    if players_turn:
                        textbutton "Run" action Return("Run") yminimum 40
                    else:
                        textbutton "Run" action None yminimum 40
                else:
                    if players_turn:
                        textbutton "Scream" action Return("Scream") yminimum 40
                    else:
                        textbutton "Scream" action None yminimum 40

screen days_S:
    vbox:
        xalign 0.01
        yalign 0.01
        text "Day:??? / ??:??"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
