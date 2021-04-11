label Parif_meet:
    "On your way back to the tavern all is calm as can be."
    e 1 "Wonder what I should get today."
    w "AHHHHH! Not the tail! Not the tail!" with vpunch
    w "{size=+8}It’s coming off!{/size}" with vpunch
    e 5 "What?!"
    s "I’m sorry!{size=+8} Please, no!{/size}" with vpunch
    scene black with dissolve
    "Your fighting instincts kick in and you draw your sword."
    play music [ "<silence 1.0>", "music/tavern.ogg" ]
    play sound "music/door.mp3"
    scene tavern 1 with slow_dissolve
    e 12 "{size=+8}Hang on!"
    "Using your shoulder you ram through the tavern door to find-"
    "A large deer in a brown apron holding onto Witer’s tail with one hand."
    "Witer is desperately tugging at the other end of his tail trying to break free."
    "Snow is on his knees in front of the deer."
    "His eyes are wide open with horror, ears flat and every part of his body trembles more than a leaf against the wind."
    e 5 "Stop! Put down your weapon! Your… pan?"
    "Yes, the deer was angrily pointing at Snow with a pan."
    "Deer" "How dare you soil my precious ingredients by using them for your disgusting jerky?!" with vpunch
    s "{size=-7}The recipe was too complicated to follow.{size=-9}So I just simplified it."
    "Deer" "{size=+12}You fool!{/size}" with vpunch
    "The deer tugs at Witer's tail even harder causing the gator to scream."
    w "No, no please. I beg of you, don’t pull on it or you’ll make me-"
    w "{size=+8}Ahhh, not so hard!{/size}" with vpunch
    "Deer" "Don’t think you’re off the hook."
    "Deer" "I taught you how to make my dishes too, and you let him cook up this inedible trash!"
    "Hakan who's sitting next to you is just slapping his knee laughing at the spectacle before him."
    e 9 "Err… is this still an assault?"
    h "Not even close. It’s just that Parif’s back."
    "You store away your sword and approach the three of them."
    e 9 "Excuse me-"
    show parif stand at center with slow_dissolve
    p "Who’s this coconut?"
    p "Can’t you see I’m trying to discipline my irresponsible sous-chefs? "
    s "[name], this is Chef Parif."
    s "Chef, this is [name], a new tavern visitor."
    if Chet.snowsfood == 3:
        e 6 "I know you. Snow mentioned your name during the last food t-"
        "Snow frantically draws a line across his neck with his hand."
        "You think he is trying to tell you not to say anymore."
    p "A new visitor?"
    p "You poor soul, you mean you’ve been stuck here eating the foul abominations these two have been making?"
    e 9 "Well I wouldn’t call them abominations. They’re pretty tasty."
    hide parif stand with dissolve
    "Parif lets go of Witer’s tail. "
    "The alligator turns around and hugs the tip of his tail, massaging it as if it were a hurt pet."
    show parif stand at left with slow_dissolve
    show witer stand at right with slow_dissolve
    p "So someone defends Snow’s cooking, eh?"
    p "Alright, bring me one of those jerkies, Witer."
    w "Ah, yes Chef!" with vpunch
    hide witer stand with q_dissolve
    "Witer rushes to the back of the bar and pulls one out from a jar."
    s "{size=-7}Can I get up now?"
    p "I don’t see why not. "
    hide parif stand with dissolve
    "Parif puts the pan on the bar counter, and Witer quickly snatches it before he can use it again."
    "Parif grabs the jerky from Witer and sniffs at it."
    p "Get some bread."
    w "What?"
    p "Bread, two slices. Here on this counter top, now! "
    "Witer flinches and quickly pulls out a plate of two slices of bread."
    "He looks at the slices of bread intently before turning to Snow."
    show parif stand at left with slow_dissolve
    show snow stand at right with slow_dissolve
    p "Did you make the bread?"
    show snow stand1 at right with dissolve
    show snow happy1 at right with dissolve
    s "Umm, {size=-4}yeah I did{/size}. {size=-5}It’s a new recipe I’ve been experimenting on.{/size}"
    "Parif pokes the bread then turns his attention back at the jerky."
    "The deer starts biting into the jerky."
    hide parif stand at left with dissolve
    "You can see Snow holding his breath with intense anticipation."
    hide snow happy1 at right with dissolve
    $ renpy.music.set_volume(0.4, 5, channel = "music")
    "You’re unsure if your comment earlier had put them into further hot water."
    "Once Parif is done with the jerky, his mouth curves upwards into an almost unnerving smile."
    $ renpy.music.set_volume(0, 5, channel = "music")
    p "Come here Snow."
    "Snow approaches the chef."
    pause 1
    "Parif takes the two pieces of bread and slaps them on the sides of Snow’s face."
    pause 2
    "Everyone else gasps."
    p "{size=+12}That tasted like I was eating a stick of salt.{/size}" with vpunch
    p "{size=+12}I wouldn’t feed that to a monster out there.{/size}" with vpunch
    s "{size=-3}I-"
    p "{size=+8}And the fact that you and Witer can make something so unpalatable makes me feel stuck."
    p "{size=+12}Like I’m the meat in an idiot sandwich!{/size}"
    s "{size=-5}But I-"
    p "{size=+8}No! You’ve made such a mess of this kitchen you’re the whole{/size}{size=+12} IDIOT SANDWICH!{/size}"
    s "{size=-8}I-"
    p "{size=+8}What are you?{/size}"
    s "An… {size=-12}Idiot Sandwich...{/size}"
    p "{size=+12}IDIOT SANDWICH WHAT?{/size}" with vpunch
    s "{size=+12}An Idiot Sandwich, Chef Parif!{/size}" with vpunch
    "Parif pulls the two pieces of bread away and puts them back on the plate."
    show parif stand at left with slow_dissolve
    show witer stand at right with slow_dissolve
    $ renpy.music.set_volume(1, 5, channel = "music")
    p "And get rid of that bread, it’s gone stale."
    w "{size=+8}Yes Chef!" with vpunch
    hide witer stand at right with q_dissolve
    "Witer grabs the plate and runs off into the kitchen."
    "Poor Snow, he’s just standing there, stunned."
    show parif stand at center with slow_dissolve
    "The deer then walks over to you and puts his arms over your shoulder."
    p "As for you coconut, I apologize for the utter incompetence my staff made you eat while I’ve been away. "
    e 9 "Staff?"
    p "Yes, the kitchen is my domain."
    p "Snow may own the tavern, but anything culinary related needs my say so."
    p "Isn’t that right, Snow?"
    hide parif stand at center with slow_dissolve
    "Snow just stands at his spot staring at the floor muttering something softly over and over again."
    "You think he’s saying, “Idiot Sandwich.”"
    show parif stand at center with slow_dissolve
    p "Don’t worry though, I’ll make new jerkies for everyone and personally take over the cooking role here."
    e 9 "I guess that’s… great?"
    "You fear saying anything against the deer."
    "He exudes an overwhelming aura."
    p "You know if I take a good look, you bear a heavy resemblance to Snow over there."
    p "You’re his kid aren’t you?"
    e 5 "I-"
    show parif stand at left with slow_dissolve
    show snow angrys1 at right with slow_dissolve
    s "He is not my son. "
    "The tavern master rolls his one eye at Parif."
    p "Ha, really? You always said you wanted a kid."
    p "Well no matter. What’s his role here?"
    show snow stand at right with dissolve
    s "He’s helping out with any jobs we have around, the usual monster extermination, discovering new resources for use."
    s "And also trying to get rid of this fog faster."
    p "Ambitious, I like it! Then you won’t mind being my ingredient supplier."
    e 9 "You need me to sell ingredients?"
    p "Think of it as a trade off. "
    p "I came back with the ingredients but most of them were taken away by the monsters on the way here."
    p "And, this silly puppy and his green lizard almost wasted all of the food reserves we have."
    show snow stand1 at right with dissolve
    "Parif clenched his fist and hammered Snow on the head."
    "Snow's tail stands erect and you can see him struggling to keep his mouth shut."
    p "I need ingredients to make dishes."
    p "And this forest is the perfect place for a chef such as myself."
    e 9 "Sure, I’m happy to help."
    p "Good."
    hide parif stand at left with dissolve
    hide snow stand at right with dissolve
    p "{size=+5}Hey, Hakan, you booze hound!"
    "Parif shouts over to Hakan."
    p "You still a fan of a Triple-Decker Meat Party Platter?"
    h "{size=+12}Hell yeah!"
    p "Then help me unload these new ingredients into the kitchen."
    "The deer then heads out with Hakan to get the ingredients."
    "You can hear them talking loudly even from inside."
    e 9 "Wait a minute-"
    "You walk over to Snow."
    "He looks a little frustrated about what just happen, but soon regains his usual composure."
    show snow stand at center with slow_dissolve
    e 1 "He’s here."
    show snow stand1 at center with dissolve
    s "Yeah?"
    e 5 "I mean, he got in here."
    e 5 "That means the fog came down for him to come in."
    show snow happy1 at center with dissolve
    s "Sorry [name], but that’s not how it works."
    s "Parif came in just like how you did, in a daze and knocked out when he reached the tavern grounds."
    s "The fog never once lifted from our side."
    e 13 "Damn it."
    show snow stand at center with dissolve
    s "Relax, be glad Parif came in with new supplies."
    s "Now you get to eat something tasty while waiting for the fog to blow off."
    "You nod dejected, but not defeated yet."
    s "Anyways, Witer and I better prep the kitchen and Parif’s room."
    s "You can visit Parif in the kitchen later. "
    e 6 "Sure, if I have the time."
    $ renpy.music.set_pause(True, channel='Snow')
    $ renpy.music.set_pause(True, channel='Hakan')
    $ renpy.music.set_pause(True, channel='Witer')
    $ renpy.music.set_pause(True, channel='Chet')
    $ renpy.music.set_pause(True, channel='Thane')
    play Snow "music/char_snow.ogg"
    play Hakan "music/char_hakan.ogg"
    play Witer "music/char_witer.ogg"
    play Chet "music/char_chet.ogg"
    play Thane "music/thane.ogg"
    hide snow stand at center with slow_dissolve
    $ Chet.snowsfood = 3
    $ Parif.witer_first = 1
    $ Parif.snow_first = 1
    $ Parif.hakan_first = 1
    $ Parif.chet_first = 1
    jump map1


label Parif_talk:
    $ renpy.music.set_volume(0.3, 1, channel = "music")
    play sound "music/door.mp3"
    if Time.hours <6 or Time.hours >20:
        scene tavern kitchen with dissolve
        "No one is here."
        "Maybe you should come here later."
        jump map1
    scene tavern kitchen with slow_dissolve
    if Parif.meet == 1:
        $ Parif.meet =2
        $ renpy.music.set_volume(0.1, 1, channel = "music")
        p "Welcome to my kitchen, eggshell."
        e 5 "Hello Chef, just came to see if you need anything."
        show parif stand at center with slow_dissolve
        p "Just call me Parif, my staff calls me Chef."
        "The chef crosses his arms and leans against the kitchen wall casually."
        "Feeling more at ease, you relax your stance."
        e 6 "Ok, sure. Parif it is then."
        e 1 "And...wow, I really can’t believe I’m meeting you. "
        p "How so eggshell?"
        e 1 "You’re the chef that left and keeps coming back here."
        e 13 "I’m sorry, but… are you insane?"
        "Parif shrugs nonchalantly."
        p "Maybe, but I didn’t come back for the laughs."
        p "This place is rich with ingredients, perfect for me to come up with new recipes."
        p "And more importantly, those idiots can't survive without me."
        e 1 "You really came back for Snow and the others?"
        p "How could I not? The boys especially Snow helped me out of a very dark place when we first met."
        p "They’re good people, and they convinced me that other good folk might end up here, and they’ll need help too."
        e 1 "I see. I’m sorry for saying you’re insane just now."
        e 13 "It’s just this whole thing is just-"
        p "It’s alright, I got the same reaction from the rest when I came back the first time. "
        e 6 "Well, I’ll be happy to help you out while you’re here."
        p "If you are looking for work, my offer to track down ingredients is still on the table."
        e 1 "Anything specific you’re looking for?"
        p "Well, I have cooked up some ideas and wrote it down on this menu here and the things I would need to create them."
        p "But, I’ll leave it to you to decide which to work on first."
        p "Just ask about my cooking, and I’ll let you know what kind of ingredients are needed for me to cook that specific dish."
        p "If you have something specific you want, but it’s not on the menu, you can ask me, I might even add it to the menu if it works out well."
        e 1 "Sounds like a good deal."
        p "Trust me, once you have a taste of my food, you wouldn’t want anything else."
        p "Those that sleep with me say the same thing."
        e 5 "The- what?"
        p "You know, banging, or are you too young to know about this yet?"
        e 10 "No, I know what it is."
        e 6 "I’m just shocked you suddenly brought it up."
        "Parif laughs loudly."
        p "It’s just a simple comparison."
        e 8 "(This guy… is a bit eccentric.)"
        e 6 "Looking forward to it, and to getting to know you better."
        p "Well you can ask me anything. I’m an open book."
        p "{color=#19c22a}You can talk to that hyena about the shovel, and the silly puppy should have a spare fishing rod."
        p "if you suspect something is an ingredient, check it out."
        "{color=#19c22a}(Now you can bring ingredients here to let Parif make cookings.)"
        "{color=#19c22a}(When you order one of Parif’s cookings for the first time, \nyou will get a permanent stat boost.)"
        $ Parif.snow_fishrod = 1
        $ Parif.chet_shovel = 1
    elif True:
        show parif stand at center with dissolve
    p "Now, what do you need from my kitchen, eggshell?"
    label Parif_talk_tree01:
        menu:
            "Order Parif's cooking" if True:
                e 1 "I’d like to order one of your dishes."
                p "I’ve got the best ingredients there is, once you dig into any one of my dishes, you won’t settle for anything less than the best."
                jump cook_screen
            "Ingredient Hunting" if True:
                e 1 "Let me track down some ingredients."
                p "Here is the menu. I've got the ingredients I need listed there."
                menu:
                    "Leave" if True:
                        jump Parif_talk_tree01
            "Find some topic to chat" if True:
                label Parif_talk_tree02:
                    menu:
                        "Where do you come from" if True:
                            e 1 "Where did a big deer like you come from?"
                            p "Nowhere really special."
                            p "Outside of the tavern, I just run a simple farm on my own."
                            e 1 "That's interesting. How did you come by to own a farm?"
                            p "Well it cost me everything, literally. "
                            p "I just needed a fresh start from my old life."
                            e 1 "What was your old life about?"
                            p "Oh, it’s nothing important. You wouldn’t be interested."
                            e 1 "Ok…?"
                            "You sense some resistance from the chef."
                        "Where did you learn to cook" if True:

                            e 1 "Where did you learn to cook?"
                            p "I just picked it up while working in my clan’s kitchen when I was young."
                            e 1 "How young are we talking about?"
                            p "About seven years old."
                            e 9 "That must have been hell, cooking at the age of seven? "
                            p "What? Learning to cook was like playing with my toys. It was pretty easy to pick up the skills."
                            p "What made it frustrating was how slow the rest of the staff was."
                            "Parif puts his hooves on his side and shakes his head."
                            p "They couldn’t even make fish broth fast enough."
                            p "Even after I told and guided them through a one hundred step recipe."
                            e 6 "A hundred steps seems a bit much."
                            p "Not in the cooking world it isn’t."
                            p "The other chefs there were good at teaching me the basics, but I really had to figure the rest out on my own."
                            e 1 "I guess you were some kind of a cooking prodigy."
                            p "Perhaps, but what matters now is what new recipes I can create."
                        "Ask about tracking down ingredients" if True:
                            e 1 "Any tips on looking for ingredients?"
                            p "What you’ve never gone looking for ingredients before?"
                            menu:
                                "Yes, I have" if True:
                                    e 5 "Of course I’ve done it before."
                                    e 5 "I’m just checking to see if you know how."
                                    "Parif scoffs at you."
                                    jump Parif_talk_tree02
                                "No, I haven't" if True:
                                    e 6 "No, I have never picked any ingredients before."
                                    "Parif laughs at you while patting your back."
                            p "You youngins have it too easy."
                            p "Listen up, to be the best in foraging for ingredients you need to have the right equipment."
                            p "Get your shovel for fruits and vegetables, and get a fishing rod for catching fish."
                            p "{color=#19c22a}You can talk to that hyena about the shovel, and the silly puppy should have a spare fishing rod."
                            p "Other than that, you got to pay attention to your surroundings."
                            p "You’re looking for ingredients in the wild, they tend to blend in with the rest of the place."
                            p "if you suspect something is an ingredient, check it out."
                            p "That’s all you need to know."


                        "Ask if he met Ebb and Flo" if Map.bathroom == "EbbFlo":
                            e 1 "Have you met the new tavern residents?"
                            p "Yeah, the mini shark and the butler orca."
                            p "Saw them at the bath house while I was unloading my stuff. "
                            e 1 "I wouldn’t call Flo small, he’s a literal adult shark."
                            p "Maybe on the outside, but inside, he’s pretty much a kid."
                            p "Those two don’t seem to get along well."
                            e 6 "Is it that obvious?"
                            p "Well what matters more is that I can get that orca to taste test some of my new cooking and maybe even have him teach me some of his own."
                            e 1 "Yeah, Ebb looks like a pretty accommodating guy."
                            e 1 "Hey, maybe your cooking can help the two of them to at least sit down without having an argument for five minutes."
                            p "You have a better chance to get them to eat each other out."
                            e 1 "Why?"
                            p "If I know butlers, which I do. They’re very attentive with what the master eats."
                            p "If Ebb isn’t cooking for Flo, he’d have a list full of do’s and don’ts for me when I cook for the little runt."
                            e 6 "You’re kidding."
                            "Parif then pulls out a piece of rolled up paper and it unfurls all the way down to his hips."
                            p "He’s already done it."
                            e 9 "Yikes."
                            p "Don’t worry, I’m charging them extra."
                        "Leave" if True:




                            jump Parif_talk_tree01
                    jump Parif_talk_tree02
            "Leave" if True:
                hide parif stand at center with dissolve
                scene tavern 1
                jump map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
