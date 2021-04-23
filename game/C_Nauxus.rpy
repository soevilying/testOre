label Nauxus_meet:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Nauxus')
    $ renpy.music.set_volume(1, 4, channel = "Nauxus")
    $ Time.mins = Time.mins +5
    if Nauxus.meet == 0:
        if Time.hours >= 6 and Time.hours <= 17:
            scene outdoor 1 with dissolve
        elif True:
            scene outdoor 1n with dissolve

        "Just as you enter the outside area of the tavern you bump into someone."
        e 9 "Oof!"
        e 6 "Sorry, I wasn’t looking where I was going."
        show nauxus black at center with dissolve
        "???" "Hmm? Oh, hello stranger."
        "The large black figure turns around."
        hide nauxus black
        show nauxus stand at center with dissolve
        $ renpy.music.play("music/char_nauxus.ogg","Nauxus", loop=True,fadein=1)
        "It’s a lizard man."
        "He has a large quiver of arrows on his back, its strap hugs his meaty chest tightly. "
        "His eyes hypnotize you in away as you can’t keep your eyes away from him."
        "You’ve never met someone with bright yellow eyes and blue pupils."
        "He cocks his head at you."
        "He’s giving you an odd look. Did he notice you’re staring at him?"
        e 9 "I.. I’m [name]."
        n "Hello [name], I’m Nauxus."
        n "I’ve never seen you before [name], are you a new guest in the tavern?"
        e 2 "Wouldn’t really call it being a guest- I’m stuck here until the fog lifts."
        e 1 "Do you live here too?"
        "Nauxus shakes his head."
        n "I live with my tribe in the swamp area, not too far from here."
        n "We’ve traded with the tavern master ever since the fog came about."
        n "Just where are you headed to in such a rush?"
        menu:
            "Finding a way out of the fog" if True:
                e 1 "I’m trying to look around for some clues, maybe there’s something that gets rid of the fog."
                e 1 "Someone or something must be controlling the fog."
                e 1 "Even if it were a living being there is a way to kill it."
                n "Reckless."
                e 5 "What?"
                n "You, are reckless."
                n "You sound like you’re just going to run about and kill anything that gets in your way."
                e 12 "Well I have to do something!"
                n "Calm yourself young wolf, you need to understand your enemy before you track it down."
                n "Going in blind will just get you hurt or you’ll miss important clues."
                n "Trust me, I’ve regretted my hasty choices in my youth."
                n "I lead my group into an ambush because I was preoccupied with taking down a bandit leader."
                e 13 "..."
                menu:
                    "Admit your past mistake" if True:
                        e 14 "I may have... let a thief got away because he was posing as someone who got robbed."
                        e 14 "I... attacked the actual victim who fought him off."
                        "Nauxus tries to cover his mouth so you won’t see him laughing, but you can hear him giggling."
                        n "G-good. Then let me help you. "
                    "Nothing to say" if True:
                        e 6 "I can’t say I can relate."
                        "Nauxus frowns, as though he knows you are hiding something from him."
                        n "Then I guess I wouldn’t need to teach you anything."
                        n "You can handle yourself, right."
                        e 5 "No, wait. I... can take any help I can get. Please teach me."
            "Exploring the lands" if True:
                e 1 "I’m going to look around, trying to figure out how much is actually covered by this fog."
                e 13 "I know Snow says it’s a forest, but it feels like almost like we’re on an entire separate island."
                n "You can try, my kind have stopped trying to map out the area."
                n "Over time we learnt that what remains in the forest doesn’t stay forever."
                n "It picks and chooses what it wants to have within itself."
                e 1 "It being the fog?"
                n "Yes, but I see the spirit of adventure inside you."
                n "I know that feeling all too well. It was all I ever wanted to do when I was younger."
                e 1 "So, what made you stop exploring?"
                n "Obligations to the tribe came up. We need each other more than ever now."
                n "Still, let me help you on your exploration. I have something you might need."
            "I don’t know" if True:
                e 13 " I don’t know. Just felt like walking about."
                e 13 "It feels like a lot has happened, and I’m not sure where to go."
                n "Well I can’t have that."
                n "Snow will have me skinned if he knew I let one of his guests go out ill equipped."
        hide nauxus stand with dissolve
        scene black with dissolve
        "Nauxus waves at you to follow him to a more secluded part of the road."
        if Time.hours >= 6 and Time.hours <= 17:
            scene forest 1
        elif True:
            scene forest 1n
        show nauxus stand at center with dissolve
        n "There are monsters roaming these parts."
        n "Some of which my kind has never seen, and who knows what else lurks among the fog."
        n "You’ll need a way to defeat the monsters."
        e 1 " Well my sword is pretty effective at that so far."
        n "You won’t be able to fight your way out of every thing."
        n "There are some monsters that show signs of intelligence like us, they offer an opportunity to try a different tactic."
        n "Seduce them."
        e 10 "You’re serious?"
        n "Yes, my kind developed the technique to confuse our foes."
        n "When they are in a state of lustful bliss we finish them off."
        e 7 "So, get them horny then kill them?"
        n "The alternative is just as effective."
        "Nauxus winks at you."
        n "Now watch my demonstration."
        hide nauxus stand with dissolve
        "He takes a few steps away from you and starts with a sensual lick of his bulging right bicep."
        "Your face instantly flushes red."
        "Nauxus grins and turns around, he raises his tail and splits his buttcheeks giving you full view of his luscious butthole."
        e 10 "Huff!"
        "Your breathing becomes shallow, and you’re filled with thoughts of wanting Nauxus to grab you and fuck you relentlessly."
        "You gulp and feel your left hand twitch as you resist the desire to grab your hardening cock."
        "Nauxus moves closer to you, his pecs bounces with every step."
        "You then feel him pulling you in by the hip. He caresses the back of your hip all the way down to your ass before he grabs your right buttcheek tightly."
        "A gasp escapes your lips."
        "Both of your faces are so close to one another you feel that even if you were to breathe your lips would touch his."
        "It feels like the world is frozen over as the two of you stand perfectly still looking at each other."
        $ Nauxus.kiss = 0
        if Zalt.cha > 4:
            menu:
                "Kiss him" if True:
                    "You lean forward and plant a deep kiss on Nauxus’s mouth."
                    "Your tongues dance and wrap around each other in a battle of dominance."
                    "His forked tongue pushes yours up to the roof of your mouth and lathers itself along your tongue."
                    "Something warm and wet brushes up your loincloth and presses against your erection, snapping you out of the kiss."
                    "You break the kiss and see Nauxus standing with his dick poking out of his cloth."
                    e 5 "I’m so sorry. I-"
                    n "No, it’s fine. If you hadn’t done it, I probably would."
                    $ Nauxus.kiss = 1
                "Don’t kiss him" if True:
                    "Nauxus pulls away from you and releases his hold."
        elif True:
            "Nauxus pulls away from you and releases his hold."
        show nauxus stand at center with dissolve
        n "Anyways, that’s just one way to seduce your opponent."
        n "You have to find your own way. Let’s review the basics."
        hide nauxus stand with dissolve
        "Nauxus goes through the seduction technique again with you, by the end of it you have created your own lustful dance."
        if Time.hours >= 6 and Time.hours <= 17:
            scene outdoor 1 with dissolve
        elif True:
            scene outdoor 1n with dissolve
        show nauxus stand at center with dissolve
        n "I should probably go, my tribe will be worried if I am gone for too long."
        n "If you ever need more training come by the swamp."
        e 4 "Ok, teacher."
        "You laugh off the teacher comment but Nauxus seems to enjoy being called that."
        "He waves goodbye and walks away."
        stop Nauxus fadeout 1
        $ Nauxus.meet = 1
        $ Battle.flirt = True
        $ Time.mins = Time.mins +40
        jump T_outdoor
    elif Nauxus.meet == 2:
        if Foe.spydie == 0:
            show nauxus stand at center with dissolve
            "You see a familiar face."
            hide nauxus stand with dissolve
            "Nauxus is standing in front of what looks like a pathway through the trees."
            "With him is a female lizard clutching the hand of a smaller lizard no taller than Nauxus’s knees."
            "You overhear their conversation as you approach them."
            n "I don’t know what else you want me to tell you Clarise."
            n "I have sent out most of the men to scout every possible area he could be."
            n "All we can do is wait."
            "Female lizard" "Everywhere but the bull tribe!"
            "Female lizard" "How could you not send anyone out there?"
            "Female lizard" "He could be dying as we speak!!"
            n "Clarise, calm yourself."
            n "This is no way to talk in front of your child."
            "The little lizard looks at Nauxus with wide eyes."
            "She doesn’t seem to understand what the adults are talking about, but she is worried."
            "Female lizard" "I wouldn’t have to talk about this if you didn’t sent him out on a suicide mission."
            "Female lizard" "What kind of a chief does that?"
            "Nauxus frowns, effectively silencing the female."
            "She pulls her child along and disappears into the pathway."
            "Nauxus then notices your presence."
            show nauxus stand at center with dissolve
            n "[name]! I’m sorry I didn’t notice you were here."
            e 1 "It’s ok, what was that about? "
            n "Oh, you saw that. It’s complicated."
            e "Just as complicated as you secretly being the Chief of this tribe?"
            n "I wasn’t purposely keeping that a secret."
            n "It just didn’t seem important at the time."
            e 1 "Chief or not, you look like you could use some help."
            n "I do, you may or may not know that there is a bull tribe southeast of the tavern."
            n "Our relationship with them has ceased to be friendly."
            n "I sent the husband of the female you saw to scout the area, and he hasn’t returned."
            n "I have the others search everywhere possible, but there have been no leads."
            n "Sending anyone else to the bull tribe area will also put them at risk of being captured or worse."
            n "That’s the last thing I need."
            n "But, you-"
            e 1 "Me?"
            n "The bull tribe doesn’t know your affiliation to us, and they are neutral with the tavern people."
            n "You might be our best choice in trying to find this agent."
            e 1 "I’m all for helping, but this sounds like I will be getting involved with your tribe’s politics."
            n "You know what you’re doing is not for your loyalty to anyone."
            n "This is simply someone in need that needs your help."
            n "I implore you to reunite this family."
            e 1 "... Fine."
            n "Thank you. When you see him tell him this phrase."
            n "“The nimble hen drinks ale under the moonlight.”"
            e 1 "What is that supposed to mean?"
            n "It means he can trust you."
            n "Now I wish you the best, I expect good news when you’re back."
            e 5 "Wait, you’re not even giving me any clues about what he looks or smells like?"
            e 5 "How am I supposed to find him?"
            n "He’s a lizard man near a tribe of bulls I am sure he will stick out."
            n "As for scent, I’m afraid my agent took the precaution of masking his scent before he left."
            n "The bulls would easily sniff our kind out anywhere."
            n "So any item of the agent would be of no use for now."
            n "You’ll have to find something on his person while he is scouting the area."
            n "Even I don’t know what his scent is like now."
            n "We’ll save the village tour until you come back with news on my man."
            n "Good luck [name]."
            $ Nauxus.meet = 3
            jump swamp
        elif True:
            $ renpy.music.play("music/char_nauxus.ogg","Nauxus", loop=True,fadein=1)
            show nauxus stand at center with dissolve
            "You see a familiar face."
            hide nauxus stand with dissolve
            "Nauxus is standing in front of what looks like a pathway through the trees. "
            "A female lizard is standing next to Nauxus."
            "Judging from their facial expressions, she isn’t happy to be with him."
            "Female lizard" "No!"
            "She slaps Nauxus and runs into the village in tears."
            e 5 "Hey, you alright?"
            show nauxus stand at center with dissolve
            "Nauxus turns to you while rubbing his cheek."
            "I’m fine, if I get taken down by a slap this village won’t last very long."
            e 1 "You make it sound like you run this place."
            n "I do. Sorry, I didn’t mean to keep it a secret when we first met."
            n "It just didn’t seem like it fit our conversation."
            e 5 "Wow, I really don’t know you."
            n "We’ll get to know each other in due time."
            e 1 "So, what was that all about earlier?"
            n "She’s the wife of an agent I sent out to the bull tribe who has never returned."
            n "I fear the worst has happened, and she couldn’t take it when I told her that."
            e 1 "...?"
            e 5 "...!?"
            "You recall the lizard spy you killed before this."
            "Was he the husband she was crying for?"
            e 13 "I... oh no..."
            n "[name]? What’s wrong? You’re suddenly pale."
            e 13 "I.. I think I..."
            e 13 "The bulls had me kill a lizard near their tribe."
            e 13 "I didn’t know, I-"
            hide nauxus stand with dissolve
            "Nauxus raises his hand to stop you from talking."
            show nauxus stand at center with dissolve
            n "Stop, I don’t need to hear the rest ..."
            n "... How did they get you to do it?"
            e 13 "They said the lizard belonged to a tribe who kidnapped and killed the children of the bull tribe."
            e 13 "I didn't know it meant here, I thought it was another criminal."
            n "Typical... "
            hide nauxus stand with dissolve
            "Nauxus’s expression darkens."
            "Your body freezes as Nauxus’s predatory gaze falls upon you."
            n "The bulls will say and do anything to cover their tracks."
            n "Those children? How dare they lie about the fact that they are the kidnappers."
            n "THEY took our children, and they DARE to play the victim?!"
            n "GAHHH!"
            "You retreat back a bit by the lizard chief’s sudden yell."
            show nauxus stand at center with dissolve
            n "[name], I don’t blame you."
            n "You didn’t know, and they tricked you."
            n "I’ll make sure they pay for this."
            hide nauxus stand with dissolve
            "He takes a deep breath, and his expression relaxes to the old Nauxus you knew."
            show nauxus stand at center with dissolve
            n "Look, I know this isn’t much, but you could use some rest by the look on your face."
            e 13 "Yeah... I think I do."
            n "Come, I will provide you a place to rest during your stay here."
            "He turns and enters the village, you follow him from behind."
            $ Nauxus.s = Nauxus.s + 1
            $ Nauxus.meet = 5
            jump Lizard_tribe_map0



    elif Nauxus.meet == 3:
        show nauxus stand at center with dissolve
        n "We’ll save the village tour until you come back with news on my man."
        n "Good luck [name]."
        jump swamp
    elif Nauxus.meet == 4:
        if Foe.spydie == 1:
            "You return to the lizard village and find Nauxus waiting at the entrance."
            show nauxus stand at center with dissolve
            n "How’d it go?"
            menu:
                "The bulls killed him (lie)" if True:
                    e 1 "The bulls got to him before I could."
                    e 1 "They tore his body to shreds."
                    "Nauxus crosses his arms never taking his eyes off of you."
                    n "How did he die?"
                    e 1 "They... they set a trap for him and the moment he was caught in it they ambushed him."
                    n "And where were you when all this happened?"
                    e 13 "I was tracking his scent."
                    "Nauxus’s nostrils flare up."
                    n "So, you weren’t near him when they killed him?"
                    e 1 "No."
                    n "I see."
                    "He scratches his chin and just looks at you."
                    "You feel uncomfortable by the way he looks at you as though he’s waiting for your to say something."
                    "As much as you want to avert your gaze you force yourself to maintain your poker face."
                    n "Well..."
                    "Nauxus drops his large hands to the side."
                    n "We’ve lost a good man, but he knew the risks when he took on the role of spy."
                    n "I’m sure you did everything you could [name]. "
                    n "Thank you, I am not looking forward to delivering this new to the wife."
                    n "But it's best she hears it from me."
                    e 1 "..."
                    "You look towards the ground feeling your heart aches like someone rammed a steak through it."
                    n "Don’t look so glum, your sympathy is appreciated but it’s not needed."
                    n "Our tribe has bounced back from far worse things."
                    n "Now follow me, you’ve come for a visit and the least I can offer is a place to stay."
                    "Nauxus puts his thumb and forefinger on your chin and pull your face upwards to meet his."
                    "He’s smiling but his eyes they feel hollow."
                    "He turns and enters the village, you follow him from behind."
                "..." if True:
                    e 13 "..."
                    "Your ears droop and you shake your head."
                    n "Oh... I see."
                    "The lizard chief’s voice is barely audible."
                    "He looks up and takes a deep breath."
                    "He looks back at you with a sullen expression."
                    n "How did he die?"
                    e 1 "They... they set a trap for him and the moment he was caught in it they ambushed him."
                    n "And where were you when all this happened?"
                    e 13 "I was tracking his scent."
                    "Nauxus’s nostrils flare up."
                    n "So, you weren’t near him when they killed him?"
                    e 1 "No."
                    n "I see. Thank you for telling me this [name]."
                    n "I will bring the news to the widow myself."
                    n "For now, please follow me."
                    n "You must be tired, I took the liberty of setting a hut aside just for your use."
                    "He turns and enters the village, you follow him from behind."
            $ Foe.spylie = 1
            $ Nauxus.s = Nauxus.s + 2
            $ Nauxus.meet = 5
            jump Lizard_tribe_map0
        elif True:
            "You return to the lizard village and find Nauxus and the spy waiting at the entrance."
            "Nauxus is glowing with a warm smile."
            show nauxus stand at center with dissolve
            n "There he is! I knew I picked the right wolf for the job."
            "Lizard spy" "[name], I’m glad you made it out of there alive, that means our plan worked!"
            e 6 "It did, I’m just glad no one had to die today."
            "Lizard spy" "You don’t know how happy I am to be able to hold my little girl’s hand again, and kiss my wife."
            "Lizard spy" "This isn’t much, but please accept our token of appreciation."
            "<[name] gained 150 coins and 500 EXP>"
            $ Zalt.exp = min(Zalt.exp+500, Zalt.maxlv*250+100*(Zalt.maxlv-1))
            $ jane_inv.take(coin,150)
            n "Also, I’m more than happy to welcome you into our village."
            n "Word of your deed has spread among the village folk."
            n "They should have no problem with you around."
            n "I’ve reserved a tent for you to rest."
            n "Get some sleep then come find me after that."
            n "We have much to discuss."
            n "Nauxus pats you on the head and walks off chuckling with the spy following him by his side."
            "You feel good about yourself and follow the two into the village."
            $ Foe.spylie = -1
            $ Nauxus.meet = 5
            jump Lizard_tribe_map0

        jump swamp
    elif True:

        pass
label Nauxus_event_1:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Nauxus')
    $ renpy.music.set_volume(1, 4, channel = "Nauxus")
    "When you walk into the village,A lizard warrior calls out to you."
    "Lizard Guard" "Halt! Are you [name]?"
    e 1 "Yeah that’s me."
    "Lizard Guard" "Chief Nauxus is ready to receive you, come with me."
    "The guard escorts you to the doorway."
    scene lizardtribe 1 with dissolve
    "In front of your hut you see Nauxus waiting. He waves to you from a distance, and you wave back."
    "The lizard guard bows and takes his leave, leaving you two alone."
    show nauxus stand at center with dissolve
    n "You’re here, I must apologize for keeping you waiting for so long."
    n "I know I asked you to come to find me before but, I didn’t expect your welcoming celebration preparations to take so long."
    hide nauxus stand with dissolve
    "You bow and get on one knee, you aren’t sure how the lizard tribe greeted their chief."
    "But you figure your tribe’s usual method shouldn’t cause much trouble."
    e 1 "Chief Nauxus, I am honoured by the opportunity to be in your presence."
    "Nothing, he isn’t saying anything, did you do something wrong?"
    show nauxus stand at center with dissolve
    "You look up to see Nauxus scratching the side of his head. His face looks confused."
    n "Hmm, that’s nice and all, but you don’t need to be so formal with me."
    "He holds out his hand towards you, and you grab it. Nauxus pulls you back to your feet."
    if Foe.spydie == 0:
        n "After how you’ve helped me I would like to consider you a friend."
        n "My people may call me chief, but feel free to just call me Nauxus."
        e 1 "Right, Nauxus. Thanks."
        n "As I was saying, the preparations for your welcoming party is complete."
        n "The bulk of the time was taken up trying to figure out what would be suitable for you to eat."
        e 9 "This is flattering, but is it really necessary?"
        n "Of course, I insisted upon it."
        n "It’s not only a good way to celebrate saving a member of our tribe."
        n "It’s a way for the tribe to get to know you, and to boost morale."
        n "I think the tribe would be glad to know we have a friend outside even with all that is happening."
        n "My advisors thinks so too."
        e 1 "Advisors?"
        n "Yes, you didn’t really think I run this whole place on my own, did you?"
        n "You’ll meet them later."
    elif True:
        n "I have no right to pull rank on you after what happened. You’ve been through a lot, and the least I can do is extend my friendship."
        n "Call me Nauxus."
        e 1 "Right, Nauxus. Thank you."
        n "As I was saying, the preparations for your welcoming party is complete."
        n "The bulk of the time was taken up trying to figure out what would be suitable for you to eat."
        e 9 "This is flattering, but is it really necessary?"
        n "Very, you remember the wife and child of the spy you failed to save?"
        "The dreaded memory from before awakens from the deepest darkest recesses of your mind. "
        "Your hands tremble as flashes of you slicing the dead lizard open and grabbing his heart replays in your head."
        e 13 "I can't forget them..."
        n "Well, the widow has fallen into depression following news of her husband's demise."
        n "And depression like that can spread like wildfire unless I inspire the tribe somehow."
        n "So, what better distraction is there than to welcome a new ally to the tribe. "
        n "Don't you think so?"
        e 1 "..."
        e 1 "I guess so."
        n "That’s great. I think the tribe would be glad to know we have a friend outside even with all that is happening."
        n "My advisors thinks so too."
        e 1 "Advisors?"
        n "Yes, you didn’t really think I run this whole place on my own, did you? You’ll meet them later."
    n "Anyways, it’ll take them some time to completely prepare everything."
    n "Why don’t we take a walk around the village, it’s pretty quiet this time since everyone’s off preparing for the celebration."
    "Nauxus’s eyebrows, or where you assume he would have eyebrows if he could grow hair rises and falls."
    "It feels like he is trying to tell you something."
    e 6 "Umm, sure, why not?"
    "Nauxus smiles and leads you out."
    hide nauxus stand with dissolve
    "As he said the village is almost empty, except for a few guards patrolling the walkways."
    "You both mostly walk in silence."
    "The walkways aren't that suitable to accommodate you and Nauxus's girth, forcing you to walk closer to the lizard chief."
    "Ever so often your hands would brush up against one another."
    "You do everything you can to avoid accidentally clasping onto Nauxus’s large hand."
    "But you suspect that Nauxus is trying to bump into you more intentionally."
    "He takes you around the village, pointing out who lives where, and what kind of life they live."
    "You try your best to keep up with all the information Nauxus is sharing but by the third house you have given up."
    "The tour goes on for a few hours."
    "Ever so often you’d see a lizard person walking off towards the doorway to Nauxus’s hut."
    scene lizardtribe 1n with dissolve
    "Before you know it the sun has set. "
    show nauxus stand at center with dissolve
    n "Looks like it’s time, and we’ve just finished the last house too. How was the tour?"
    e 6 "Ah, it was very enlightening? "
    "Nauxus crosses his arms and smiles at you."
    n "Then you won’t mind me quizzing you on what I’ve just explained?"
    hide nauxus stand with dissolve
    "He puts his thumb under your chin and pushes your face upwards to meet his."
    "His face is close. So, close!"
    n "If you get anything wrong, how should I punish you?"
    e 9 "N-Nauxus!"
    "Your cheeks begin to warm the longer you look at his."
    "His mesmerizing stare makes it hard for you to think straight."
    "He breaks the mood when he suddenly laughs. "
    show nauxus stand at center with dissolve
    n "I’m just joking, boy your face is priceless."
    n "Of course, I knew you won’t remember everything, it took me months to just remember the guards’ names."
    e 6 "Hahaha, yeah."
    e 1 "It’s pretty impressive though that you took the time to know your people."
    n "All part of being the chief, and don’t worry I’ll make sure we get more one on one time to fill you up on all things about us."
    n "You’ll be part of the tribe in no time."
    "You nod confidently, but you wonder what he meant by more one on one time."
    n "Listen, we’re entering dangerous times ahead."
    n "I need all the allies I can gather for what is to come."
    n "I hope I can count on you when that time comes?"
    e 1 "What are you asking me to do?"
    n "To help me keep my people safe."
    e 1 "..."
    e 1 "You have my word that I will do what is necessary. "
    n "That’s all I ask, I trust you’ll make the right decision."
    n "Alright, we should head over to where the celebration is."
    n "We've a large terrace built above the trees for such events and other rituals."
    n "Come, I'll take you there."
    hide nauxus stand with dissolve
    "Nauxus leads you back to the doorway to his hut. "
    "You’re puzzled by why he leads you here."
    "The guards open the doorway and you see a flight of stairs leading upwards and spiraling around a gigantic tree stump."
    show nauxus stand at center with dissolve
    e 5 "Woah, how did I not notice all of this? "
    n "The dense trees and fog help to keep it hidden from view, or perhaps you were distracted by another view?"
    "Nauxus turns to you and grins."
    stop Nauxus fadeout 5
    $ renpy.music.set_volume(0, 5, channel = "music")
    e 5 "No! You think I have all that free time just trying to find you."
    "Craning your neck upwards, you hear the sound of drumbeats and wind instruments fill the air."
    "The shadows of people dancing can be seen even from where you stand."
    n "Come on, the party’s started."
    hide nauxus stand with dissolve
    scene black with dissolve
    play music "<loop 12.4405>music/lizard_party.ogg"
    $ renpy.music.set_volume(0.3, 10, channel = "music")
    "Nauxus leads the way up the stairs."
    "As you climb upwards the grand scale of the gigantic stump becomes clearer."
    "Its trunk is gargantuan, wide enough to house an entire village on it."
    "It's no wonder they would build a platform on top of it."
    e 1 "I wonder how old this stump is, it must have taken ages for it to grow this big."
    n "I'm not really sure but this tree has always been here since I was here."
    n "Come, sounds like the crowd is already started."
    "As you circle around the stump, you find another massive structure nearby."
    "It’s a tree standing proudly above the platform like a giant watching over those beneath it."
    "Just slightly higher from the platform there is a tree house built into the taller tree. "
    "Suspended bridges connect the tree house to the platform and another house in the distance."
    "Nauxus walks ahead up the staircase and you follow him from behind."
    $ renpy.music.set_volume(1, 2, channel = "music")
    "When you reach the top, the music grows into a thunderous roar."
    scene lizardtree cle with dissolve
    "The crowd erupts into a cheer for Nauxus as he makes his way to a grand chair decorated with beads and shiny rocks."
    "He smiles confidently and waves to his people."
    "You are unsure if the crowd really is here to celebrate you or him."
    "The crowd forms a semicircle on the left and right around a grand throre."
    "A large bonfire sits in the middle of the terrace."
    "As Nauxus rises to the throne, the guards beneath the seat prevent you from moving forward."
    "Instead, they ask you wait for Nauxus to speak."
    show nauxus stand at center with dissolve
    n "My tribe!"
    "The crowd falls silent, all eyes are on him now."
    n "We're gathered here today to celebrate and welcome our new friend."
    n "Times are hard now, but we have each other, and the help of our wolf from the tavern."
    n "Together, we'll overcome this fog and those that hide in its shadows."
    n "We do this not only for our future, but for those we've lost... our children."
    hide nauxus stand with dissolve
    "The silence shatters as the lizards turn to each other, murmuring among themselves."
    "Random lizard" "Death to the bulls!"
    "That one person's cry sparks the rest. The crowd starts to chant"
    "'Death to the bulls!'" with vpunch
    "'Death to the bulls!'" with vpunch
    "Your head feels like a dark cloud is blanketing over it."
    show nauxus stand at center with dissolve
    n "SILENCE! " with vpunch
    "His booming voice cuts through the chant and the crowd is silenced."
    n "Your pain and anger resonates with my soul. Those children deserve redemption! Their futures were dashed too soon."
    n "I swear as your chief, we will reclaim their lives and put an end to the perpetrators so no lizard will ever live in fear again."
    n "For that, tonight we celebrate our resolve and each other!"
    hide nauxus stand with dissolve
    "Nauxus throws his fist in the air and the crowd erupts into cheers again and the drum beats fill the air."
    "For now, the crowd has forgotten their rage temporarily."
    "Lizard people from the crowd come towards you and pull you towards the bonfire."
    "Before you know it, you're dancing along with the other lizard people."
    "They spin you around from person to person, stopping only for a few seconds to perform a complicated hand gesture with you."
    "In the midst of the dancing and cheers you see Nauxus sitting alone on the throne."
    "He rests his head against his chin and he looks on as though he’s disappointed in something."
    scene black with dissolve
    "Regardless, someone pulls you into another dance, and you move from partner to partner, dancing the night away. "
    stop music fadeout 5
    "Once the party ends you’re unable to find Nauxus again, so you return to your hut in the village."
    $ Time.days = Time.days + 1
    $ Time.hours = 8
    "The next day."
    "...."
    "......."
    scene room 4 with dissolve
    e 1 "That was some welcome party, my feet are sore like never before."
    "Knock, knock."
    "There’s someone at the door. You answer the call and meet the sleepy gaze of a lizard guard."
    "Lizard guard" "Hello, I am here to escort you to the council chamber."
    e 1 "Huh? Why?"
    "Lizard guard" "I am told a meeting with the advisors is about to begin, and Chief Nauxus requests your presence. Please follow me."
    "The guard walks off and you decide to follow him."
    scene lizardtribe 1 with dissolve
    "He leads you to the stairway up to the platform from yesterday."
    scene black with dissolve
    "He walks across the platform and up the stairs to the tree house."
    scene lizardtree 1 with dissolve
    "You find yourself in a hall filled with other lizard warriors going about their business."
    "They all look at you curiously. "
    "Lizard guard" "Over here, [name]."
    "Your escort invites you to enter a doorway."
    "You pat down your fur making sure you look neat before stepping inside. "
    "The door closes behind you."
    scene meetingroom with dissolve
    show nauxus stand at center with dissolve
    n "Good to see you can join us, [name]."
    "You nod meekly. Nauxus’s other guests don’t seem to be interested in your presence."
    hide nauxus stand with dissolve
    scene meetingroom 1 with dissolve
    "The lizard chief sits on a grand throne overseeing a round table."
    "There are two male lizards wearing a piece of paper partially covering their faces."
    "One has a red paper while the other has a blue paper."
    "Sitting across from one another, they seem preoccupied with their own thoughts."
    "Their paper masks perplex you, but one reptile draws your attention to him."
    "A tall figure sits to the left of Nauxus, he looks nothing like the other lizards or Nauxus."
    "Tall spiky fins protrude from behind his head and along his slightly hunched back."
    "His body is muscular but he looks slimmer standing next to Nauxus’s wide frame."
    "The reptile slithers forward revealing his snake like lower half. He’s a naga."
    scene meetingroom with dissolve
    show selye stand at right with dissolve
    show nauxus stand at left with dissolve
    "Naga" "Why is he here?"
    n "Be nice, Selye. I invited [name]. Today’s discussion will be important for him too, so it’s only natural he be present to see the outcome."
    n "[name], these are my advisors. The one’s with paper over their faces are the representatives chosen by the people to speak on their behalf. "
    n "Selye here is my trusted advisor, he is wise in all things magic."
    n "And yes before you ask, he is not of our tribe, but he is a valuable ally that I trust."
    n "His advice has been most helpful to the tribe."
    "Red lizard" "Chief Nauxus, shall we begin the proceedings?"
    n "Lets."
    hide nauxus stand with dissolve
    hide selye stand with dissolve
    scene meetingroom 1 with dissolve
    "Nauxus points to the empty seat next to Selye."
    "You take your place next to Selye but the naga brushes you with his scepter to sit further away."
    "You roll your eyes at him but pull your seat away anyhow. "
    n "Advisors to the lizard tribe, as you all are aware, the bull tribe have re emerged from the fog."
    n "There are no clues to the whereabouts of the children taken."
    n "I’m afraid after so long, we have to presume they didn’t make it."
    n "We are gathered here today to decide whether to advance our plans to take down the bull tribe. "
    re "I for one am thoroughly for it."
    re "We can get our hands on the resources that the bull tribes have, their weapon blueprints,and that mysterious temple they keep hidden."
    re "It’ll be good business all around."
    bl "No, we can’t think about profit alone."
    bl "Chief Nauxus, this plan is too drastic."
    bl "We have yet to identify the culprit, is it fair to punish an entire tribe for the actions of one or two bulls?"
    n "Snip it at the bud, I say. That’s the best way to crush your enemies."
    bl "This is a rash decision. We have to consider the consequences of going to war with them."
    se "You dare doubt the wisdom of the chief?"
    se "While you wait with your indecisions, more and more children live in fear waiting for when it will be their turn to be ssssnatched in the night away from their families!"
    n "Yes, what Selye says is true."
    n "The bull tribe refuses to allow an investigation, and we have weeping families with no news of their children."
    n "We are not safe until we know the perpetrator is dealt with once and for all!"
    n "We have enough evidence to know it’s one of the bulls, the horn that was knocked off, hoof prints, and the tuft of bull fur."
    n "If Chief Axel refuses to hand a suspect over to us, we will have to find them ourselves by any means necessary."
    n "Our people deserve that much. Once we have the bull tribe under our control we can launch a full scale investigation into the culprit’s whereabouts."
    n "If the bulls choose to resist, then well, that’s just unfortunate."
    se "We must trust in Chief Nauxus’s wisdom. Justice needs to be sssserved."
    se "The bulls need to be taught to know their place, and not to disrupt the natural order of things."
    bl "There must be a more peaceful way!"
    se "There isn't! The bulls only understand that might is right."
    se "Chief Nauxus understands that we need to sssspeak their language in return for them to understand that they need to answer for the actions of their kind."
    re "Come on Blue, the chief always has his way. It’s just a few bulls, our warriors can take them down easy."
    bl "..."
    "The atmosphere in the room is tense. Nauxus leans back in his chair and rubs his hands together. "
    "The advisors refuse to look at Nauxus while Selye is practically growling at Blue."
    "He eyes his advisors with a calculative gaze. "
    n "Blue, how are things with your son?"
    bl "He’s fine, why do you ask?"
    n "That’s good, the kids have been so afraid lately they can’t even come out to play."
    n "Can you imagine what it feels like to be so scared to be a child, and what of the parents who are trying to do whatever they can keep their children safe."
    bl "I understand that but-"
    n "And also, Blue, I’ve heard that you have a special bunker for your son."
    "Blue gasps."
    n "Now, everyone is basically in panic trying to find a safe space."
    n "What do you think will happen if word got out that you have one, but you didn’t share."
    "Blue’s jaws tremble. He looks like he wants to say something, but he can’t find the strength to form the words."
    "The lizard with the red paper crosses his arms."
    "Blue looks at him, but Red shakes his head, as though telling him not to fight back."
    "Nauxus keeps his eyes glued onto Blue, you can feel his piercing gaze pressing in on Blue’s squirming body."
    "Blue gulps."
    bl "If it’s for the children... then I support the decision."
    n "Excellent."
    "Nauxus claps his hands once. He smiles at his advisors."
    scene meetingroom with dissolve
    show selye stand at right with dissolve
    show nauxus stand at left with dissolve
    n "The tribe will be more confident knowing we’ve reached a unanimous decision."
    n "Selye, you will coordinate the missions with [name]."
    if Thane.quest == 7:
        $ Selye.lizardask = 1
        n "[name],find Selye at his hut, he’s reachable via the suspending bridge from here to the hut right behind the platform."
        n "Lastly, [name], come by the council chambers after your first mission."
    se "As you command, Chief Nauxus."
    e 1 "Understood."
    n "Then this meeting is adjourned. The rest of you may leave, I need to speak to [name] in person."
    hide nauxus stand with dissolve
    hide selye stand with dissolve
    "Blue drags his tail against the floor while Red pats him on the back."
    "Selye looks back at you with narrowed eyes once more before he too leaves the room."
    "Alone with Nauxus, he looks at you and lets out a long breath. "
    show nauxus stand at center with dissolve
    n "That was intense."
    e 6 "Very."
    n "Anyways I had to pull you away to discuss a private problem that you may need to be aware of."
    n "Let me borrow your map."
    hide nauxus stand with dissolve
    "You pass Nauxus your map and he marks a location."
    show nauxus stand at center with dissolve
    n "This here is the dark swamp. No one from the tribe is allowed to go there."
    e 1 "Are there dangerous monsters in there?"
    n "In a way, rogue lizard warriors hide in the swamps depths."
    e 1 "Rogue lizard warriors? Why would there be rogue lizard warriors?"
    n "Lets just say not everyone was happy when I first came to power, and they made it their life’s mission to take me out."
    n "They don’t dare to attack the village for fear of injuring their fellow lizards."
    n "However, that’s not stopping them from having their spies to try to get at me when I’m not looking."
    e 1 "That doesn’t sound like a comfortable way to live."
    n "All part of the job I say."
    n "Right now, I’m letting you know to be careful if you go to the dark swamp you will be attacked."
    n "They probably know that you are my friend and guest, and will try to get to me through you."
    n "So, if they do attack, don’t hesitate to fight back."
    n "You’ll be doing me a favour. Cut down as many of the rogue lizards as you can."
    e 1 "If it comes to it, I’ll know what to do. Thanks for the warning."
    n "Good, then that will be all. I’ll talk to you later."
    hide nauxus stand with dissolve
    scene lizardtree 1 with dissolve
    e 1 "(That was a crazy meeting. Nauxus wants to invade the bull tribe?)"
    e 1 "(That’s insane, I can't imagine this is something Nauxus would think of)"
    e 13 "(Then again... do I know him well enough? )"
    e 1 "Not to mention now I need to be careful not to get ambushed by those rogue lizards in the dark swamp. "
    e 1 "I could really use a drink, but for now I need to find out what mission Selye has for me at his hut. "
    e 13 "Or maybe I can also go to the bull tribe to see what they want.?"
    $ Map.deepswamp = 1
    $ Selye.meet = 1
    if Quest.campb == 0:
        $ Quest.campb = 1
    if Quest.campl == 0:
        $ Quest.campl = 1
    play Chan1[ "<silence 0.5>", "music/lizard_village.ogg" ]fadein 3
    play Chan2[ "<silence 0.5>", "music/bird1n.ogg" ]fadein 3
    jump Lizard_tribe_tree0

label Nauxus_camp_end:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Nauxus')
    $ renpy.music.set_volume(1, 4, channel = "Nauxus")
    window hide None
    stop music fadeout 1
    $ Zalt.public = True
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    scene meetingroom with slow_dissolve
    if Time.nauxusart == 9999:
        $ Time.nauxusart = Time.days
    if Quest.campl > Quest.campb and Quest.campt >=5:
        $ Time.hours = Time.hours +3
        "You hobble your way up the stairs towards the council chamber."
        "While still clutching your stomach you can feel your eye throb in pain."
        show selye stand at right with dissolve
        show nauxus stand at left with dissolve
        "Nauxus sits upon his throne with Selye at his side."
        "The three lizard guards that were accompanying you are all trying to tell their chief what they saw."
        "Second Lizard Guard" "It was horrifying, a giant wolf with bloody teeth and claws as sharp as razorblades."
        "First Lizard Guard" "It was so strong, when it beat me with its paw I thought I got smashed by a flying tree."
        "Third Lizard Guard" "You got to stay away from that place. It’s not safe. We didn’t even see the creature coming. "
        "Third Lizard Guard" "It’s like it just materialized out of nowhere."
        se "Calm down, calm down."
        se "How is Chief Nauxus ssssupposed to understand all of this if you’re all talking to quickly."
        "Nauxus notices your presence in the distance and smiles."
        "He gets up as though he wants to head towards you, but composes himself."
        n "You three have done your part, head to the barracks to get your wounds treated, and some much earned rest."
        n "[name], come forth. I am glad you’ve returned."
        hide selye stand with dissolve
        hide nauxus stand with dissolve
        "You walk forward towards the blue lizard while the other three leave the room."
        show selye stand at right with dissolve
        show nauxus stand at left with dissolve
        "Selye crosses his arms and gives you a disgusted glare."
        se "Alone, and without his team. One can’t help but think he abandoned them."
        e 13 "Hey, I didn’t abandon anyone. I went to scout ahead and I was attacked."
        se "The other guards said you were nowhere to be found when the giant wolf attacked."
        e 1 "When I came to I was in a bunch of bushes away from the campsite."
        e 1 "I remember I was knocked unconscious when I reached the campsite."
        e 1 "It felt like something heavy stomped on me. Maybe it was the wolf."
        se "Why would there be a giant wolf living there, without anyone knowing?"
        e 13 "Maybe it’s something from out of the fog."
        e 13 "You know weird creatures have been roaming the forests every since the fog came."
        se "I ssssay it’s too convenient, it could be a trick by the bulls."
        n "Not possible, remember the team said they encountered the bulls before the giant wolf appeared and the creature attacked the bulls as well."
        n "The bulls may be unrefined but they aren’t stupid enough to unleash a trap on themselves."
        n "This puts a dent on our plans Selye, caution the others from going near that place. "
        n "As for you [name]."
        "He pauses and looks at you intensely, as though he’s expecting you to say something."
        hide selye stand
        hide nauxus stand
        show nauxus stand at center with dissolve
        n "A giant wolf in the woods, a very remarkable incident I would say."
        n "Now, both the lizards and bulls are without a strategic campsite."
        n "What do you think about that?"
        menu:
            "Stay silent" if True:
                e 1 "..."
                n "..."
                n "No comment, I see."
            "I’d consider it a victory" if True:
                e 1 "No one had to die, that’s a win in my books."
                n "Perhaps, but consider this."
                n "In a game where neither side can advance, the game will go on until one side falls from exhaustion."
                n "A worse fate than a swift death. Won't you agree?"
                e 13 "I... wouldn't know. Is there anything else?"
                n "No."
        hide nauxus stand
        show selye stand at right with dissolve
        show nauxus stand at left with dissolve
        n "We’ll have to find you another chance to help out."
        n "For now, you have my thanks."
        n "Take this for your troubles."
        "<[name] gained 200 coins>"
        "<[name] gained one Level-up-point.>"
        $ jane_inv.take(coin,200)
        $ Zalt.points = Zalt.points +1
        n "This meeting is adjourned."
        n "Selye, begin preparing for the next phase of the war plans as we discussed."
        se "As you command Chief Nauxus. "
        "You nod and take your leave from the council chamber. "
        $ Quest.campl =6
        $ Quest.campt =6
        $ Quest.camp_n = 2
        play Chan1[ "<silence 0.5>", "music/lizard_village.ogg" ]fadein 3
        play Chan2[ "<silence 0.5>", "music/bird1n.ogg" ]fadein 3
        jump Lizard_tribe_tree0
    elif Quest.campl < Quest.campb and Quest.campt >=5:
        show nauxus stand at center with dissolve
        "You find Nauxus sitting alone in the council chamber. He stares absentmindedly at the wall."
        n "Oh, [name]. I wasn’t expecting you."
        "He sighs. "
        e 1 "Are you ok?"
        n "I would rather you not see me like this, but yes, there is something troubling me."
        n "We launched the first phase of our plans against the bull tribe, but it was halted by an unforeseen giant enemy."
        e 9 "Oh, that’s unfortunate."
        n "Very, and I be lying if it wasn’t a blow to my confidence."
        n "I am not used to losing, [name]."
        "Nauxus stands from his seat and puts his hands on your shoulders."
        "He looks at you almost pouting."
        n "We could have used your help out there. Maybe things would have turned out differently."
        "His words sting your heart."
        e 13 "You sound like you’re expecting me to say something."
        n "Yes, say you’ll fight with me."
        n "You say you’ll do the right thing.I know you have the tavern to protect but can you really stand idle while this war goes on?"
        n "You don’t know if the tavern will be safe as this war goes on, the only way to keep everyone safe is to end it quickly."
        n "It is the best choice you have [name], and I’m offering it to you."
        n "No one died this time, but what if they did, and you had every chance to prevent it, but you didn’t."
        n "Say you’ll be my warrior. "
        "He pauses and clears his throat."
        n "Think about it, ok?"
        "He wants you to be his ally and side with him, but what will that cost? Do the bulls deserve to be taken down? "
        "Moving on, is there something you want to talk about?"
        $ Quest.camp_n = 2
        jump Nauxus_tribe_talk1
    elif Quest.campl > Quest.campb and Quest.campt <5:
        "Upon reaching the council chamber Nauxus and Selye are already there waiting for you."
        show selye stand at right with dissolve
        show nauxus stand at left with dissolve
        n "[name], what do you have to report?"
        "You bow."
        e 1 "Nauxus, the campsite has been established, the runestones have created a protective barrier around the site."
        n "Good, Selye send our troops out with supplies and equipment to fortify the campsite."
        se "At once, Chief Nauxus."
        hide selye stand at right with dissolve
        hide nauxus stand at left with dissolve
        "The naga slithers pass you. His face stoic as ever like the day you met him."
        "After he leaves Nauxus rushes from his throne and embraces you in a powerful hug, lifting you off the floor." with vpunch
        n "I knew you could do it [name]."
        e 10 "Woah, woah!"
        show nauxus stand at center with dissolve
        "He spins you around before putting you back on the floor."
        n "I knew I picked the right person for this job."
        e 6 "Thanks, your confidence in me means a lot."
        n "And as thanks for your good work, you deserve a little reward."
        "<[name] gained 500 coins>"
        "<[name] gained one Level-up-point.>"
        $ jane_inv.take(coin,500)
        $ Zalt.points = Zalt.points +1
        n "Selye will call you for your next mission, and while you wait I might have our first lesson plan ready."
        e 1 "What exactly are we doing during these lessons time?"
        n "Nothing too strenuous just helping you improve your skills, I’m very excited to fill you with as much as I know."
        "Your tail wags and your face turns a slight shade of pink."
        n "Anyways, that’s all for now."
        n "Feel free to find me here if you have something you want to talk about."
        n "If not, you could always visit Selye, I can tell you two need more time together to grow closer."
        e 6 "Yeah, maybe..."
        "The idea of getting closer to that egotistical naga fills you with dread."
        $ Quest.campl =6
        $ Quest.camp_n = 2
        play Chan1[ "<silence 0.5>", "music/lizard_village.ogg" ]fadein 3
        play Chan2[ "<silence 0.5>", "music/bird1n.ogg" ]fadein 3
        jump Lizard_tribe_tree0
    elif Quest.campb > Quest.campl and Quest.campt <5:
        "Nauxus and Selye are alone in the council room."
        "The moment you enter Selye hisses at you."
        "Nauxus watches you in silence as you approach."
        "You sense the tension in the room surrounding you."
        show selye stand at right with dissolve
        se "You have ssssome nerve strolling in here sssso casually. "
        e 1 "I wanted to talk to Nauxus, and last I checked, no one tried to stop me from coming in."
        show nauxus stand at left with dissolve
        n "Selye be polite, but he is right, now isn’t the best time for idle conversation [name]."
        n "I just received word that we lost a potential camp area to the bull tribe, and all three of my men have been taken out."
        e 13 "My condolences."
        n "Yes, it’s a waste of good men. "
        se "Those bulls got lucky, they must have found them before they could set up the barrier."
        n "This is a heavy lost, they turned our plans against us."
        se "We’ll get them next time. They’ll pay for stealing from the lizard tribe. "
        n "Then let us begin the planning for the next phase, and [name]-"
        e 1 "Yes?"
        "Nauxus takes a deep breath."
        "His eyes, there’s a certain coldness and tiredness to them."
        "He notices you’re looking at him and he puts on his serious expression that he uses to talk to his advisors."
        n "I just hope you’ll be able to help us with the next mission."
        n "I'll call you when it's time for our lessons. Good bye."
        hide nauxus stand with dissolve
        "He walks past you.A chill grasps your heart."
        "No, a sting like the pain of someone who doesn’t even want to be near you anymore, or are you just overthinking things?"
        hide selye stand with dissolve
        "Selye follows Nauxus, and you leave a short while after they depart."
        $ Time.anauxus = Time.days
        $ Quest.camp_n = 2
        jump Lizard_tribe_meetingroom
label Nauxus_tribe_talk:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Nauxus')
    $ renpy.music.set_volume(1, 4, channel = "Nauxus")

    if Quest.bomb_end != 0 or (Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bomb_lizard ==2):
        jump Nauxus_letter
    if Quest.fes_end == 0 and Quest.fesn >= 1:
        jump Nauxus_festival
    show nauxus stand at center with dissolve
    n "[name], welcome. Is there something you need? I have some time to spare. "
    jump Nauxus_tribe_talk1
label Nauxus_tribe_talk1:
    if Nauxus.talktree == 1:
        menu:
            "Invite Nauxus on a date" if Nauxus.s <=2:
                show nauxus stand at center with dissolve
                e 1 "Nauxus, you got a minute?"
                n "I always have time for you [name]. What's on your mind?"
                e 13 "Ummm..."
                "You grip your fingers behind your back but your hand keeps sliding off the other from how sweaty your palms are."
                "Nauxus raises an eyebrow while smiling at you mischievously."
                e 13 "We’ve been spending time together, and I get this feeling like..."
                n "Like?"
                "He crosses his arms. You notice his chest flares out a bit more and his muscular arms bulge out."
                e 14 "Like, like..."
                "You turn your head to the side to hide your blushing cheeks."
                e 7 "I get a feeling that you like to spend time with me."
                n "What if I do?"
                e 6 "Well ... would you want to... "
                "You turn to face Nauxus."
                e 7 "Go on a date with me?"
                "Nauxus chuckles and rests his hands."
                "He smiles a bit more and you notice the tip of his tail thumping against his throne much like how you would wag your tail when you’re excited."
                n "Where would you want to go on this date?"
                e 6 "I was thinking maybe a picnic by the lake. "
                n "The lake. Hmm... I’ll think about it."
                e 13 "I mean you can just say no."
                n "I didn’t say that."
                "Nauxus reaches out with one hand to stop you."
                "He quickly notices what he did and pulls back his hand."
                n "Ehem, I would like some time to prepare."
                n "So, please DO ask me again when I have my things sorted out."
                "Now it’s your turn to raise your eyebrow at the chief. "
                e 7 "Ok, I’ll ask you again later."
                n "Thank you. I appreciate it."
                jump Nauxus_tribe_talk1
            "New training" if True:
                n "[name], I’ve been doing some thinking and I think you’re ready for the next stage of your training."
                e 1 "I’m ready when you are."
                n "I’ll have Selye set up the training course for you then."
                e 5 "Selye? Woah, wait a second, are you sure about this?"
                n "Of course I’m sure."
                n "It’s just setting up some obstacles to train your agility."
                n "What’s the worst he could do?"
                e 1 "A lot, you know he doesn’t like me."
                n "I trust he will be able to stay professional."
                n "In any case, I’ll watch over your training when it starts."
                n "Selye will summon you when he is ready."
                e 1 "Hmm..."
                jump Nauxus_tribe_talk1
            "Discuss about Selye" if Selye.past == 1:
                e 1 "Nauxus, I can’t really grasp what’s Selye’s agenda."
                n "Oh."
                "Nauxus’s eyes dart from left to right before narrowing at you."
                n "Tell me more."
                e 1 "He’s like juggling two different ideologies at the same time."
                e 13 "One minute he’s saying if you aren’t born strong, give up trying."
                e 1 "Then you hear about his origins and he is all about getting stronger to defeat his rival.\nWhich is he?"
                "Nauxus scratches his chin."
                n "I think he has already told you the truth about who he is. "
                e 5 "What? Where?"
                n "I’ll leave that to you to figure it out."
                n "Let’s just say some people lie to themselves because they desperately want to believe in the truth."
                n "Now which is which I will let you decide."
                jump Nauxus_tribe_talk1
            "Уйти" if True:

                jump Lizard_tribe_meetingroom
    elif True:
        menu:
            "Ask about the fog" if True:
                e 1 "I know you’re in the middle of a war, but can you tell me anything about this fog? "
                n "I’m afraid there isn’t much we know."
                n "It came just came one day and strange things have been happening since."
                n "The fog probably poisoned the bulls’ minds, and lead them on this path of bloodshed."
                e 1 "But you don’t need to stay here. Snow says the fog clears up eventually for people to leave."
                n "We are aware of this random moment where the fog lifts."
                n "When we first heard about it from, Snow? I think."
                n "Those who wanted to leave were free to leave."
                n "The lizards you see here now are those who choose to stay and protect their home, and their ancestors home for many decades ago."
                n "For a time, we were trying to figure this out, but we made no progress on it, then the attacks on the children began. "
                e 6 "Sounds like you forgot it was Snow for a minute there."
                n "No, it’s just my head was fuzzy for a second there."
                n "Anyways, long story short, is we’re putting our priority on protecting the village, before making plans to take down the fog."
                jump Nauxus_tribe_talk1
            "Ask about Nauxus’s council members" if True:
                e 1 "You have a very colourful group of counselors."
                n "Indeed, Red and Blue are very trusted, they have their own priorities when it comes to running the village."
                n "But in the end they understand what is best for the people."
                e 1 "What about Selye?"
                n "Selye may have a seat with my council but isn’t officially one of my advisors."
                n "He is more of a trusted ally, like you."
                e 6 "That’s a lot of trust to have him plan out your war strategies."
                n "Oh, you’re mistaken."
                n "Selye and I go through the plans together, he helps me carry out the plans, and encourages me when I’m in doubt."
                e 1 "I see. Then how you two meet?"
                n "I’ll leave that to him to answer for you."
                jump Nauxus_tribe_talk1
            "Ask about the proof of the kidnappings." if True:
                e 1 "All of this started because of the kidnappings, I get the village is mad for answers but are you sure you have enough to put the blame on the bulls?"
                n "Careful, questions like that people might think you’re bound to betray us."
                e 13 "That’s not what I mean, I just want to know why you are so sure it’s them."
                n "Aside from the evidence we already have, I was there during one of the kidnappings. "
                n "It all happened so quickly."
                n "The village was on high alert after the first kidnapping."
                n "And I had just returned from the failed negotiations with Axel to allow us to investigate his village folk."
                n "A yell rang out through the village, it was the scream of a child."
                n "The kidnapper leapt roof to roof with the child screaming for help."
                n "I and a few of the guards chased after the kidnapper, but it moved so fast we struggled to keep up with it."
                n "It ran into the forest, the child’s scream was all I could hear."
                n "I could make out the figure of the bull through the darkness and what little light the moon shed. "
                n "I managed to keep up with the kidnapper, my hands was just so close grab the little lizard, but then the bull threw a kick, and I was knocked back. "
                n "It was too late, the child screamed but I couldn’t catch up anymore."
                hide nauxus stand with dissolve
                "Nauxus looks to the floor, his hands tremble."
                show nauxus stand at center with dissolve
                n "I was so close... and the look in the kid’s eye, he needed me, and I couldn’t save him."
                e 13 "Nauxus..."
                "He slams his right fist on the arm of his throne."
                n "And that bastard Axel, he dared to look me in the eye and denied all of it!"
                n "Just thinking about it makes my blood boil."
                n "I swear from that day on, I’ll make him all his tribe answer for what they did to that child."
                n "I swear it."
                e 1 "..."
                n "I’m sorry. I... got overly emotional. Can we talk about something else?"
                jump Nauxus_tribe_talk1
            "Ask about Nauxus’s plans after the war" if Nauxus.s <=2:
                e 1 "What do you plan to do once the war is over?"
                n "It’s premature to think about that right now, the war’s only just begun."
                n "But once I ensure my people’s safety, maybe I’ll put my focus on finding a partner."
                e 1 "A partner to help manage the village?"
                hide nauxus stand with dissolve
                "Nauxus chuckles and walks over to you. "
                show nauxus stand at center with dissolve
                n "Well managing the village with me is one thing, but more importantly I want someone who could manage me inside the bedroom and out."
                n "Would you happen to know anyone like that?"
                e 6 "I... I wouldn’t know. I’m not that popular with the girls."
                n "It doesn’t have to be a woman. "
                "Nauxus’s eyes falls on you, his eyes trace the curve of your muscles from top to bottom."
                hide nauxus stand with dissolve
                "You instinctively put your hands over Nauxus’s eyes."
                e 10 "What are you implying? "
                show nauxus stand at center with dissolve
                "The chief chuckles deeply and holds your hand. "
                n "I’m saying I can go either way, and the tribe has no issues with that."
                n "There have been chiefs with same sex partners."
                n "Your heart’s racing, I can feel it in your pulse. Are you ok?"
                "He holds your wrist firmly, with a broad smile."
                e 10 "I-I’m fine! Just, it’s so sudden that you tell me you’re into men."
                n "Why wouldn’t I be? I can always appreciate a man with a good heart, supple lips-"
                hide nauxus stand with dissolve
                "His hand pulls back from your wrist and he clamps onto the palm of your hand."
                "More heat rises from your neck towards your face. He’s not being subtle at all!"
                n "And most importantly if he can keep up with me and my needs. So-"
                e 10 "So..."
                n "You think Witer would be interested in me?"
                e 1 "..."
                e 1 "I think I’m done here."
                "Nauxus laughs loudly, and pats you on the back, knocking the wind out of you with just one hit."
                show nauxus stand at center with dissolve
                jump Nauxus_tribe_talk1
            "Уйти" if True:
                jump Lizard_tribe_meetingroom
label Nauxus_artwork:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Nauxus')
    $ renpy.music.set_volume(1, 4, channel = "Nauxus")
    e 1 "Hey there Nauxus."
    show nauxus stand at center with dissolve
    n "Ah, [name], you’ve arrived at a perfect time."
    n "Take the seat next to me, I was just about to summon you."
    hide nauxus stand with dissolve
    "You sit down next to Nauxus."
    "You notice he has pieces of paper on the table, and a wooden pallet with red paint next to it."
    e 1 "What are we doing today?"
    n "Today, we are having your first lesson with me. Now, pay attention. "
    "He turns to you and gives you a firm look. "
    show nauxus stand at center with dissolve
    n "While you’re here, I figure I will teach you some of the tricks that came in handy for me, when I was just one of the tribe warriors."
    e 5 "Ok, sounds like it can be handy. What’s today’s lesson then?"
    n "A little something to train your intelligence."
    n "Picture this scenario, your allies have uncovered secret information that could turn the tide of battle."
    n "But to keep it secure it’s written in code, or you only have a split second to decipher a message before it gets destroyed."
    n "So, I’m going to show you some images, and I want you to tell me what’s going on in them."
    e 1 "Bring it on then."
    hide nauxus stand with dissolve
    "You clap your hands confident in your abilities."
    "Nauxus rubs his chin with a mischievous smile."
    show nauxus stand at center with dissolve
    n "Confident eh, well of course I’m going easy on you, my masterful art skills is so detailed that you really have to try to get it wrong."
    n "In a real battlefield the codes will be coded in the craziest of ways."
    e 1 "Then we’ll make a bet then."
    n "A gambling wolf are we, well if you insist. What shall we wager?"
    e 3 "Loser has to do one thing the winner says."
    n "Deal, it’s all or nothing. You have to get all three pictures correct or I win."
    "You ball your right hand into a fist and beat your chest with confidence to show you’re ready."
    hide nauxus stand with dissolve
    "Nauxus turns to the paper and pulls out what you assume is a small piece of coal, you can’t see clearly."
    "You crane your neck to try to get a peek."
    n "Hey, no peeking."
    "The lizard chief pulls the paper close to himself."
    "You laugh and sit back against your chair."
    "Nauxus moves like a flurry as he works on all three drawings."
    n "Done!"
    show nauxus stand at center with dissolve
    e 5 "That was quick."
    n "In a real situation you won’t have the luxury to paint a clear message."
    n "But no matter, my artistic skills are the best in the tribe."
    n "So, speed and precision are my forte. "
    n "Now tell me what you see."
    $ Random = renpy.random.randint(4, 5)
    if Random == 4:
        show black2 with dissolve
        show art01 with dissolve
        e 1 "..."
        e 1 "(Ugh...)"
        e 9 "(Did he really draw this?)"
        n "This is super easy. Note my use of lines."
        e 9 "(Lines? They’re all lines...)"
        menu:
            "A lizard on fire while someone is lying on the ground to not get burnt." if True:
                e 9 "This is...ehh...A lizard on fire while someone is lying on the ground to not get burnt?"
            "Nauxus training lizards to do push ups." if True:
                e 9 "This is...ehh...You are training lizards to do push ups.?"
                $ Nauxus.artwork_p = Nauxus.artwork_p +1
            "A lizard with red hair watching another lizard doing push ups." if True:
                e 9 "This is...ehh...A lizard with red hair watching another lizard doing push ups.?"
    elif True:
        show black2 with dissolve
        show art02 with dissolve
        e 1 "..."
        e 1 "(Ugh...)"
        e 9 "(Did he really draw this?)"
        n "This is super easy. Note my use of lines."
        e 9 "(Lines? They’re all lines...)"
        menu:
            "Nauxus hiding behind a tree while a bull looks at a pile of rocks.." if True:
                e 9 "This is...ehh...You are hiding behind a tree while a bull looks at a pile of rocks?"
            "Nauxus meeting a bull in secret while the bull looks at a burnt up campfire." if True:
                e 9 "This is...ehh...You are meeting a bull in secret while the bull looks at a burnt up campfire?"
            "Nauxus spying on a bull from behind a tree who found a pile of coins." if True:

                $ Nauxus.artwork_p = Nauxus.artwork_p +1
                e 9 "This is...ehh...You are spying on a bull from behind a tree who found a pile of coins.?"
    n "Really? I thought I made it pretty obvious what it is. Here comes another."
    hide art01
    hide art02
    $ Random = renpy.random.randint(2, 3)
    if Random == 2:
        show art03 with dissolve
        e 5 "I... have nothing to say about his art skills."
        ""
        menu:
            "Red and Blue kissing and Nauxus is watching them in the bushes" if True:
                e 9 "...Red and Blue kissing and Nauxus is watching them in the bushes?"
                $ Nauxus.artwork_p = Nauxus.artwork_p +1
            "A sick and angry lizard butting heads on a carpet." if True:
                e 9 "...A sick and angry lizard butting heads on a carpet?"
            "A lizard wearing a red hat and a lizard wearing a blue hat holding hands and talking to each other." if True:
                e 9 "...A lizard wearing a red hat and a lizard wearing a blue hat holding hands and talking to each other.?"
    elif True:

        show art04 with dissolve
        n "Don’t overthink it."
        ""
        menu:
            "Three lizards standing around" if True:
                e 9 "It must be...Three lizards standing around!"
            "The lizard trio relaxing" if True:
                e 9 "It must be...Three lizards standing around!"
            "The lizard trio practising their signature poses" if True:

                $ Nauxus.artwork_p = Nauxus.artwork_p +1
                e 9 "It must be...Three lizards standing around!"
    n "Good, keep it up."
    hide art03
    hide art04
    n "You know this one."
    show art05 with dissolve
    ""
    menu:
        "Nauxus and I walking along the village" if True:
            n "Come on, you were there when it happened."
        "The tour we took" if True:
            $ Nauxus.artwork_p = Nauxus.artwork_p +1
            n "See, you remember."
        "I leading Nauxus towards battle" if True:
            n "Come on, you were there when it happened."
    hide art05 with dissolve
    hide black2 with dissolve
    if Nauxus.artwork_p == 3:
        "You somehow saw the truth behind Nauxus’s paintings, you feel empowered."
        "{b}{color=#19c22a} <[name] gained one Level-up-point.>{/color}"
        $ Zalt.points = Zalt.points +1
        n "Ah, perfect marks. I shouldn’t have been so soft on you."
        e 9 "Yeah... piece of cake."
        n "Well, I’m a lizard of my word. What is your request?"
        hide nauxus stand with dissolve
        "Nauxus tosses the papers he used across the table, he leans back against his throne and spreads his rock solid arms."
        "Giving you a full view of his masculine chest, and his cobblestone abs."
        "Your eyes fall on the shirtless lizard man’s body and an idea strikes."
        e 3 "I know what I want, since you got to show off your art skills, I want to show you mine."
        n "Oh? Sounds simple enough I have some pap-"
        e 1 "No, I want to draw on you."
        n "On me? You’re asking the chief of an entire lizard tribe to let you put paint on this temple of a body?"
        "He raises both of his arms and flexes them, his biceps and triceps bulge with power making you break into a smile."
        "You subtly cross your legs and look away meekly."
        "Nauxus puts his arms down and winks at you."
        n "Alright I’ll allow it. Show me your masterpiece."
        "The brawny lizard grabs the palette of red paint and puts it next to you."
        "Your heart leaps and sores with excitement. You eagerly pull your seat closer. "
        "Nauxus lies back on his seat and rests his arms behind his head."
        "The sight of Nauxus’s body on display all for you makes your heart skip."
        "Your right hand reaches out and you press between his meaty pecs. "
        "Slowly, your hand caresses lower, your fingers feel the groove of his hard abs. "
        n "Admiring your canvas I see?"
        e 4 "As would any artist do. "
        "You reach for the palette and dip your forefinger in it."
        e 1 "Now hold still."
        "With your finger dripping with red paint you touch his right pec."
        "Nauxus’s sudden gasp causes you to pull your hand back."
        e 5 "Something wrong?"
        n "No, it’s just... I haven’t been touched for so long. I’m sorry, please continue."
        "He closes his eyes and cranes his neck upwards."
        "You continue where you left off, on his right pec you swirl your fingers."
        "Nauxus bites his lips but you can still hear a muffled groan."
        "There’s something about his reactions that spurs you to take it slow and to see how far you can push his buttons."
        "Once the swirly circle is complete you draw four squiggly lines around it, completing your red sun."
        n "Ah, are you purposely drawing so slowly?"
        "You grin at Nauxus, but he looks mildly annoyed at you."
        "Dipping two fingers into the palette again, you rub Nauxus’s abs, making him grunt louder than before."
        "His mighty pectorals rise and fall and his face flushes red as he turns away and looks at you with one eye."
        "You flash a cheeky grin and get to work on the river you want to draw."
        "Running your hand across his stomach, where your finger feels the rise of his abs you draw little curves to symbolize waves."
        n "Mmm, whatever you’re making, do more."
        "Next, you refresh your paint, and finish off with painting a single tree, its branches reaching upwards brushing against just under Nauxus’s left pec."
        "Nauxus lets out a huff, and flexes his pecs in response."
        "The sun you drew ripples with his muscle."
        "You laugh a little, and proceed to finish up the drawing."
        scene black with vslow_dissolve
        "..."
        e 1 "There, done."
        $ Time.hours = 19
        scene meetingroom n with vslow_dissolve
        "Nauxus breathes heavily and stands up."
        "He looks down on his torso turning his head left and right trying to see the picture."
        n "What is it?"
        e 6 "It’s a tree by the river that I used to visit with my friends."
        e 1 "It was the best swimming spot."
        e 1 "We’d dive in on a hot day, and maybe even catch a fish or two if we’re lucky."
        n "Hmm, sounds like a fun place. I wouldn’t mind visiting it one day."
        e 1 "You should, I’d give you the whole tour of the village too."
        n "Would the tour include your own bedroom?"
        "Your jaw drops and you give Nauxus a look that he replies with a deep chuckle. "
        e 10 "I wouldn't say no to that."
        "That’s good, maybe I’ll give you a chance to spend time in my room too. "
        e 5 "I... I’d like that."
        "You’re both standing close to each other, you can feel the heat radiating from his body."
        "Nauxus rubs the back of his neck, and gives you a smile."
        n "I should go wash up, the paint’s starting to harden."
        e 1 "Oh, I can help you if you like."
        n "Heh, that’s sweet, but I’m afraid my shower’s not going to be big enough for both of us."
        n "Maybe next time [name]."
        "The lizard chief holds your paint covered hand and brings it up to his face."
        show nauxus stand at center with dissolve
        n "Don’t forget to clean up yourself, my dirty canine."
        "He chuckles and leaves up the flight of stairs."
        "You rub the back of your hand that Nauxus held with a satisfied smile."
        play Chan1[ "<silence 0.5>", "music/lizard_village.ogg" ]fadein 3
        play Chan2[ "<silence 0.5>", "music/bird1n.ogg" ]fadein 3
        jump Lizard_tribe_tree0
    elif True:
        "You found the strength not to laugh at Nauxus’s badly drawn paintings."
        "The strength to be socially tactful is stronger now."
        "{b}{color=#19c22a} <[name] gained one Level-up-point.>{/color}"
        $ Zalt.points = Zalt.points +1
        n "Hmm, too bad my friend, it looks like it’s my win."
        hide nauxus stand with dissolve
        "Your ears droop to the side and you sigh."
        "How you wish you could say something about the drawings, but you figure that would be a terrible idea."
        "Still, your eyebrow twitches as Nauxus looks at you with his smug grin, and his arms crossed."
        "You have a bad feeling about what he’s going to come up with."
        show nauxus stand at center with dissolve
        e 11 "So... so what do you want me to do?"
        hide nauxus stand with dissolve
        "Nauxus leans in close, his eyes locked into yours."
        n "I want you all to myself tonight."
        "You gulp."
        show nauxus stand at center with dissolve
        n "You and I are going to spend the whole night cramming on deciphering different cryptographs. "
        e 9 "Wh-What?"
        n "Then we’ll run through the practice again until you get it all right."
        n "I am going to cram your ass with so much knowledge, you’ll be deciphering codes wherever you go."
        e 9 "I don’t think that’s going to be useful."
        n "No more talking, we start now!"
        hide nauxus stand with dissolve
        scene black with dissolve
        "Nauxus orders his guards to bring their training books, and as he instructed he makes you sit through hours of his lecture and training."
        "By the time night falls you’re slumped over the table and your eyelids struggle to stay awake."
        "Nauxus is still drawing beside you, the candlelight illuminates his tired but satisfied face."
        "You blink, his face blurs away."
        "You blink, maybe just a little rest won’t hurt."
        "You close your eyes."
        $ Time.days = Time.days +1
        $ Time.hours = 7
        scene meetingroom with vslow_dissolve
        "Come morning, you awaken on the council's table. "
        "Your neck aches a bit from the improper sleep, but you feel comfortably warm with this grey blanket over you."
        e 1 "Where's Nauxus? Where did I get this blanket?"
        "You spot a piece of paper in front of you. It reads:"
        "Dear [name],"
        "I had to head out to join the morning hunt. Didn’t want to wake you up."
        "Just leave my cloak on the chair, I’ll pick it up later."
        "Let’s hope all that practice helped your code breaking skills."
        "XOXO Nauxus"
        "So this blanket is actually Nauxus’s cloak."
        "You bring the cloth up to your nose and take a deep sniff, it smells just like him, musky like the swamp."
        "You leave his cloak on your seat as instructed and get ready to start your day."
        $ Time.hours = 9
        jump Room4
label Nauxus_roushk:
    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ renpy.music.set_pause(False, channel='Nauxus')
    $ renpy.music.set_volume(1, 4, channel = "Nauxus")
    $ Time.mins = Time.mins +5
    "You enter the council room to see Nauxus rubbing his forehead."
    "He looks very tired."
    e 5 "Nauxus!"
    show nauxus stand at center with dissolve
    n "Hmm? Oh, [name]. Hello. "
    e 1 "You look beat, where’ve you been this whole time?"
    n "It’s a long story my friend."
    n "You won’t believe this, but I actually travelled to another world called Aigran."
    e 5 "You did? Hey, I met someone from another world too."
    e 6 "His name’s Roushk. Maybe you guys switched places or something."
    e 1 "You got to tell me what happened on your trip."
    if toscrossld.ld_lizard_ending == "Bad":
        n "There’s not much to say, the place I found was mostly abandoned."
        n "It was supposed to be a temple full of lizardmen, but they all died out due to a corruption curse."
        e 5 "Wait... died out?"
        e 12 "That can’t be, Roushk left just recently."
        e 13 "How can they all be dead?"
        n "I’m sorry [name], but there were no more lizards there."
        e 13 "This is ... no... I need a minute."
        n "Alright."
        e 13 "Roushk..."
        n "Will you be alright [name]?"
        e 13 "I just can’t believe he’s gone just like that."
        e 1 "What was the point in me helping him go home, if all it did was just send him to his death?"
        n "You can’t blame yourself for this, you didn’t know what would happen at the other side. "
        e 12 "Still!"
        "Nauxus puts an arm on your shoulder."
        n "You can’t blame yourself. "
        e 13 "I hope he got to at least be with Othra again."
        n "Maybe they did."
        "You stand in silence before deciding to leave the conversation."
        "For now, your heart aches for what happened to Roushk."
    elif toscrossld.ld_lizard_ending == "Good":
        n "Roushk? Huh, I did meet a Roushk."
        n "Tall, red lizard, the leader of the lizardmen?"
        e 5 "That’s him! How was he? "
        n "Well he looked perfectly healthy to me, but he didn’t mention ever coming to the forest here, or you."
        e 5 "What? We did so much together, how could he have forgotten me."
        n "Well it’s not necessarily he forgot you, he looked like he had a lot on his plate at the time."
        n "Their tribe is dealing with some kind of corruption curse."
        e 5 "Wow, he goes home, and he’s already working on saving his tribe."
        e 1 "What a guy. What else happened in your travels?"
        n "Well why don’t we save that story for a later time."
        n "I need some rest, but if there is something important you need, just say so."
    elif toscrossld.ld_lizard_ending == "":
        n "Sorry [name], I didn’t meet anyone from there with that name."
        e 5 "Really? Damn that’s a shame. I think you two would have gotten along really well."
        n "I’ll make sure to find him the next time I go to that world."
        e 8 "You cheeky lizard."
        n "So, did you need anything else?"
    elif True:
        n "Sorry [name], I didn’t meet anyone from there with that name."
        e 5 "Really? Damn that’s a shame. I think you two would have gotten along really well."
        n "I’ll make sure to find him the next time I go to that world."
        e 8 "You cheeky lizard."
        n "So, did you need anything else?"
    hide nauxus stand at center with dissolve
    jump Lizard_tribe_meetingroom

label Nauxus_letter:
    if Quest.bombn == 1:
        "Nauxus appears deep in thought when you enter the council chambers."
        e 1 "Nauxus?"
        show nauxus stand at center with dissolve
        n "[name], good you’re here."
        e 1 "Is this a bad time? You look busy."
        n "It’s fine, I’m merely making plans for the upcoming mission."
        n "I summoned you as part of the next phase of the war."
        e 1 "..."
        e 1 "What do you need me to do?"
        n "The bulls outpower my men easily, but any brute will fall if you stab it enough times."
        n "That’s why I need a way to increase the number of soldiers at my disposal."
        n "I'm going to the dark swamp to negotiate with the rogues for peace between us."
        n "With their help, my tribe will stand a better chance at taking the bulls down. "
        e 9 "You want to go into there, alone? That’s suicide."
        n "And that is the reason why I have asked you to accompany me."
        n "I want you to watch my back."
        n "I cannot vouch for your safety, but I can rest easy knowing I have someone beside me."
        e 1 "What are you going to do to convince them to come back to the tribe?"
        n "That depends on what their demands are. If we’re lucky we’ll have a little friendly conversation."
        n "Worse case scenario, nothing changes."
        e 1 "Or you die there before you can even get the chance to open your mouth."
        n "That might happen, but regardless I want to try."
        n "I’m not expecting all of them to be so eager to accept my offer, but they have family and friends they’ve left behind."
        n "That alone, can be a very convincing factor."
        n "Talk to Selye if you decide to help, but I’ll understand if you choose not to."
        n "Just let me know your decision after you speak to him."
        n "In the meantime I’ll need to plan out what to say when I meet those rogues."
        hide nauxus stand at center with dissolve
        "Nauxus then sits quietly with his chin resting on one of his fists."
        "Best to leave him time to think."
        $ renpy.music.set_pause(True, channel='Nauxus')
        $ renpy.music.set_pause(True, channel='Selye')
        scene black with dissolve
        "..."
        play sound "music/door.mp3"
        scene lizardtree 1 with slow_dissolve
        $ Quest.bombn = 2
        if Quest.bomba == 1:
            e 1 "(Nauxus needs my help to negotiate with the rogue lizards so he can expand his army.)"
            e 13 "(I mean, it's good he’s reuniting the tribe but, why for war....)"
            e 1 "(I best find out what Axel needs first before I do anything.)"
        elif True:
            e 13 "Great, so I have one chief that wants to bomb a village, and the other wants to recruit more lizards for his army."
            e 1 "(Do I pick a side or see Thane for his advice?)"
            $ Quest.bombt = 1
            $ Quest.bomb = 2
        jump Lizard_tribe_tree
    elif Quest.bomba == 1 and Quest.bombn == 2:
        show nauxus stand at center with dissolve
        n "Hey,[name]."
        n "Talk to Selye if you want to accompany me to the dark swamp for the negotiations with the rogue lizards."
        hide nauxus stand at center with dissolve
        "Nauxus sits quietly with his chin resting on one of his fists."
        "Best to leave him time to think."
        jump Lizard_tribe_meetingroom
    elif Quest.bomb == 3 and Quest.bombn == 3:
        $ Quest.bombn = 4
        if Quest.bombt ==4:
            "Loud tapping noises can be heard even from outside the door."
            "But you need to see Nauxus, so you don’t think much of it and enter as you normally would. "
            e 1 "Hey Nauxus. Woah, you look sick."
            "Nauxus notices you and his face instantly sours."
            show nauxus stand at center with dissolve
            n "Achoo!" with vpunch
            e 5 "Woah, cover your mouth man."
            n "That’s Chief Nauxus, warrior. Achoo!"
            e 1 "Well you never seemed to have any problems with me. "
            n "What’s your name, warrior? Ah-"
            hide nauxus stand at center with dissolve
            n "Ah-"
            n "Achoo!" with vpunch
            show nauxus stand at center with dissolve
            e 5 "Woah, calm down Nauxus. It’s me."
            "You take off the amulet."
            "Nauxus’s eyes widen. "
            n "[name]? What?"
            hide nauxus stand at center with dissolve
            show amulet at center with dissolve
            "He walks over briskly, and you show him the amulet Selye gave you."
            "Nauxus sniffles and looks at the Items."
            hide amulet at center with dissolve
            show nauxus stand at center with dissolve
            n "Selye made this for you?"
            e 6 "Yeah, it’s supposed to hide my identity later. I would look, smell and even sound like a lizard."
            n "Huh, he actually surpassed my expectations."
            "Nauxus returns the amulet to you and pulls his face back as though he is holding back a big sneeze. "
            "You cover your face, but Nauxus manages to cancel his sneeze."
            n "Put it on, we should go. The longer I stay here the more I’m going to sneeze."
            e 1 "What’s up with that anyways?"
            n "Some miscreant threw a huge ball of pepper on the ceremonial stage."
            n "Damn thing went up my nose when I went to check on the commotion."
            e 1 "That sounds terrible. Did you find out who did that? "
            n "There’s no clue on the bomb itself. The pepper made everyone’s sense of smell go haywire. "
            n "My men are chalking it up as a prank by the kids, and I’m inclined to believe it."
            e 5 "Yeah, it’s possible. Now, you were saying about heading out?"
            n "Yes, let’s go."
            "You put on the amulet and the two of you make your way to the dark swamp."
        elif True:
            "You enter the council chambers as you normally would. "
            "Nauxus is resting his head on his hand, he can be seen mumbling to the ceiling."
            e 1 "Nauxus? You ok?"
            show nauxus stand at center with dissolve
            "He turns to you and his eyes narrow."
            n "That’s Chief Nauxus, warrior."
            e 5 "You’re joking right? I thought you were always fine with me just calling you by name."
            n "Where do you get off-"
            "He looks seriously perplexed by your statement."
            n "What unit are you from? I have half a mind to have you and your superior punished for your audaciousness."
            e 5 "(Ok, I don’t think he’s joking around anymore. Does he really not recognize me?)"
            e 6 "Woah, calm down Nauxus. It’s me."
            "You take off the amulet."
            "Nauxus’s eyes widen."
            n "[name]? What?"
            "He walks over to you briskly."
            n "How’d you do it?"
            e 6 "It’s this amulet from Selye."
            e 1 "It’s supposed to hide my identity, and makes me appear as a lizard warrior to everyone else."
            n "Amazing."
            hide nauxus stand at center with dissolve
            show amulet at center with dissolve
            "He holds the amulet like an explorer discovering a new treasure."
            n "Lets see it again. Here, put it on."
            hide amulet at center with dissolve
            "Nauxus hands you the amulet and you wear it again."
            "A wide smile is plastered across his face. He is very much amused."
            show nauxus stand at center with dissolve
            e 6 "How do I look?"
            n "This is incredible."
            "He circles you like a hunter surrounding his prey."
            "He stands behind you and grabs your shoulder. "
            n "Your body, it looks and feels so scaly."
            hide nauxus stand at center with dissolve
            "With his right hand, he feels your chest and slowly glides downwards to your stomach."
            "You let out a soft huff as you feel his tender touch."
            "His face presses close against your neck, and he takes a deep breath."
            n "You even smell like a lizard. "
            e 7 "Oh... do you like it?"
            "Nauxus smells your neck again. "
            n "Mmm."
            "His hand now inches away from your crotch is sliding back and forth careful not to touch your loin cloth."
            if Nauxus.kiss == 1:
                menu:
                    "Encourage Nauxus to touch you lower" if True:
                        e 14 "Y-you’re free to explore lower if you want."
                        "Your voice comes out almost like a whisper into his ear."
                        "He presses his body close to you and you feel a familiar warmth pressing against your buttcheeks."
                        "Nauxus breathes into your neck."
                        n "You’re always taking advantage of the situation ever since we first met."
                        "You huff."
                        e 7 "And you’re always teasing me."
                        "His hand slips down through your loin cloth and you feel his rough scaly touch against your semi hard dick."
                        "You moan and your body goes limp against Nauxus’s broad shoulders."
                        "He strokes your member by rubbing his fingers along the length of your shaft."
                        "You can’t help but wonder what he is feeling down there."
                        "Suddenly, he pulls his hands away and steps back."
                        "He looks strangely bashful as he avoids your gaze."
                        e 1 "Something the matter?"
                        show nauxus stand at center with dissolve
                        n "It’s just... Well I expected when I did bed you, I’d be looking at the real you rather than a lizard copy."
                        e 5 "Bed me?"
                        "You turn to face Nauxus."
                        e 1 "I thought you were into Witer."
                        n "Oh, you still think about that? "
                        "Nauxus is smiling gleefully."
                        n "I just said that to get a reaction out of you."
                        "Your jaw drops. "
                        "He laughs and you feel embarrassed that you were actually jealous of Witer for a while."
                        n "I’m very much interested in you, [name]. I am hoping you feel the same about me."
                        "Before you can answer, Nauxus turns to the door."
                        n "For now, let's leave it at that. We have more pressing matters to attend to. "
                        hide nauxus stand at center with dissolve
                        scene black with dissolve
                        "Follow my lead while we’re in the dark swamps."
                        "You nod and go along with Nauxus."
                        jump Nauxus_darkswamp
                    "Tell Nauxus to focus on the plan" if True:
                        e 6 "Maybe we should focus on the mission?"
                        n "Oh... yes."
                        show nauxus stand at center with dissolve
                        "Nauxus pulls himself away."
                        "He turns to the door."
                        n "Follow me. Just play along while we’re in the dark swamps."
                        hide nauxus stand at center with dissolve
                        scene black with dissolve
                        "You nod and follow Nauxus as he leaves the room."
                        jump Nauxus_darkswamp
            e 6 "Maybe we should focus on the mission?"
            n "Oh... yes."
            show nauxus stand at center with dissolve
            "Nauxus pulls himself away."
            "He turns to the door."
            n "Follow me. Just play along while we’re in the dark swamps."
            hide nauxus stand at center with dissolve
            scene black with dissolve
            "You nod and follow Nauxus as he leaves the room."
            jump Nauxus_darkswamp



    elif Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bomb_lizard ==2:
        $ Nauxus.talktree = 1
        if Quest.bomb_bull == 3:
            $ Time.bomb = Time.days
        if Quest.bomb_result == Axel:
            $ Quest.bomb_lizard = 3
            $ Time.anauxus = Time.days
            scene black
            "You head for the council chambers."
            "While you climb up the stairs you see spots of dried blood leading up to the ceremonial stage."
            "A tired looking lizard warrior walks past you, not giving you a chance to ask him what happened here."
            "You climb higher and eventually reach the ceremonial stage."
            "Your eyes bulge out in surprise. "
            stop Chan1
            stop Chan2
            if Time.hours >= 6 and Time.hours <= 17:
                scene lizardtree 2 with slow_dissolve
            elif True:
                scene lizardtree 2n with slow_dissolve
            "There’s a large burnt crater where the bomb hit, and more blood is splattered around the point of impact. "
            "The traces of heat left from the bomb envelopes your body as you walk away from the spot."
            if Time.hours >= 6 and Time.hours <= 17:
                scene meetingroom with slow_dissolve
            elif True:
                scene meetingroom n with slow_dissolve
            "As you enter the council chamber you see Nauxus’s advisors Red and Blue sitting next to the chief."
            "The air in the room is heavy. Nauxus himself hides his face behind his hand."
            "He uncovers his face and turns to Red."
            n "Send the guards out to help with the funeral rights, Red."
            n "Blue, have some supplies set aside to be given to the families of the deceased."
            n "I’ll personally see them when I’m ready."
            "Red and Blue nod and take their leave."
            "Nauxus still doesn’t look at you."
            n "Is there something you want [name]?"
            e 6 "I came to ask if you’re still going to meet the rogues?"
            n "No, that plan has been cancelled."
            n "If you haven’t noticed there’s a gaping hole on the ceremonial stage."
            e 13 "Yeah... I saw."
            e 1 "Were there casualties?"
            n "...Yes, I lost three of my best men in an explosion."
            e 13 "I’m so sorry."
            n "..."
            show nauxus stand at center with dissolve
            n "Where were you when the explosion happened?"
            e 9 "I was ... out gathering materials."
            n "You sound unsure. "
            e 5 "I was just surprised by the question."
            n "Mmhmm, then the set of wolf like footprints we found on the way to the broken catapult, was that you?"
            "You freeze."
            e 9 "(I thought I covered my tracks...)"
            "Your heart beat races. You need to say something or it will be even more suspicious."
            e 5 "(Does he really have something on me or is this a bluff?)"
            e 13 "You’re probably thinking about the road... that I usually take to get here."
            e 1 "Maybe it’s just a coincidence that I passed by that area, but I really didn’t see anything then."
            n "Hmm..."
            n "Very well. Then that will be all. We can talk some other time, I will be busy dealing with all of this."
            e 1 "Very well."
            "You bow and take your leave. Best to come back later if you need to talk to him."
            hide nauxus stand at center with dissolve
            play Chan1[ "<silence 0.5>", "music/lizard_village.ogg" ]fadein 3
            play Chan2[ "<silence 0.5>", "music/bird1n.ogg" ]fadein 3
            jump Lizard_tribe_tree0
        elif Quest.bomb_result == Nauxus:
            $ Quest.bomb_lizard = 3
            n "This is a great day [name]. We’ve finally gotten back members of our tribe to come back to the village."
            show nauxus stand at center with dissolve
            e 6 "That is good, too bad not all of them joined."
            n "It’s to be expected.\nIt takes a lot of courage to admit when you’re fighting a losing war."
            n "Some just double down on it."
            e 1 "When we were in the dark swamp... they called you an usurper."
            e 1 "What did you do to get the title of chief?"
            "Nauxus breathes and leans back against his throne."
            n "I did what I had to do, [name]."
            n "... It’s not something I wish to share right now."
            n "If you really want to know about it then you can ask me again when the war is over. "
            e 1 "Nauxus ..."
            n "Don’t look so glum. Today’s success calls for a celebration."
            n "Which reminds me, the Feast of Frolic is coming soon."
            e 1 "Doesn’t ring a bell. Is it like a harvest festival?"
            n "Actually, it’s a special ritual, we give thanks to our ancestors for all that we enjoy today."
            n "I’ll check on the logistics of it, and call you when the time is right."
            n "So, what else do you want to talk about?"
            jump Nauxus_tribe_talk1



        elif Quest.bomb_result == Thane:
            $ Quest.bomb_lizard = 3
            $ Time.anauxus = Time.days
            n "[name], I thought I told you I need some time to myself. "
            show nauxus stand at center with dissolve
            e 13 "I’m sorry, it’s just... I know how important getting your new recruits were."
            e 13 "I don’t know what else to say."
            "Nauxus sighs and wipes his face."
            n "I know you tried... I just need time."
            n "Maybe it’s best if we pretend none of this happened..."
            n "I don’t think it would be good for either of us if we don’t move past this."
            n "Maybe you should come back after tomorrow. I think I’ll be over it by then ...."
            "And then he leaves."
            jump Lizard_tribe_meetingroom
        elif True:
            e 1 "I should go do my quest first."
            jump Lizard_tribe_meetingroom
            return
    elif True:
        jump Lizard_tribe_meetingroom

label Nauxus_darkswamp:
    stop Nauxus fadeout 4
    scene swamp 2 with slow_dissolve
    "Walking side by side with Nauxus, you both enter the eerie dark swamp."
    "The mist that keeps you all hostage in this maze of a forest continues to be a hindrance."
    "You take comfort in Nauxus’s presence as it helps you ignore the sensation that you’re being watched."
    scene swamp 3 with slow_dissolve
    "Nauxus leads you deeper into the swamp."
    "He would occasionally stop near some rocks that have been slashed across their surfaces."
    "Based on how Nauxus would sniff around the gash and instantly know where to go, these must be some kind of markers for the rogue lizards to find their base."
    "You continue down the winding path into the heart of the swamp when suddenly a spear flies through the mist and narrowly misses your right ear."
    e 5 "It’s an ambush! Get to cover!"
    "You both manage to get behind some trees before a flurry of spears fly out from every side and pierce the earth where Nauxus stood."
    "Voice in the trees" "Finally come here to die, you usurper?"
    "The disembodied voice sounds taut and husky."
    "You peek from behind your hiding spot to find the attackers but they haven’t made themselves visible yet."
    show nauxus stand at center with dissolve
    n "I’d sooner have my own head on a bull’s spear than forfeit my life to you lot."
    "Voice in the trees" "Oh, we can make all of that happen. "
    "Voice in the trees" "After you tore apart our kind, death is the only sensible punishment you deserve."
    n "Well if I die now, it won’t change a thing."
    n "The tribe still won’t let you back, and you all will infamously be known as the rogues who left the village in the middle of a war without a leader."
    n "I come here offering you all an alternative. I’m offering you the chance to return home, no strings attached!"
    hide nauxus stand at center with dissolve
    "The sound of murmurs breaks through the quiet swamp."
    "Voice in the trees" "Silence!"
    "The whispers stop."
    "Voice in the trees" "You expect us to believe such a cheap trick?"
    show nauxus stand at center with dissolve
    n "It’s not a trick. I come with only one comrade."
    n "Listen to reason, the lizard tribe is at war, it’s time to put an end to this feud. "
    n "I know some of you have been separated from family and friends for too long."
    n "If there are willing lizards who would aid me in this fight, I will see that their past transgressions are pardoned."
    hide nauxus stand at center with dissolve
    "The murmurs rose again at an even louder level."
    "Voice in the trees" "SILENCE!"
    "The murmurs continue but at a lower volume."
    show nauxus stand at center with dissolve
    n "You’re losing them. Now do you want to talk?"
    "he voice makes a loud grunt and you see a lizard leap out of the cover of the mist."
    "He brandishes a long spear, and appears visibly enraged."
    "Rogue Lizard Leader" "Show yourself Nauxus!"
    "You look to Nauxus and he gives you a reassuring nod."
    hide nauxus stand at center with dissolve
    "He stands up and walks with confidence to the other lizard."
    "You follow from behind."
    "Nauxus stands a few feet from the lizard, only the rows of spears piercing the earth separates the both of them."
    "Rogue Lizard Leader" "I don’t know what you’re up to, but it’s not going to work, Nauxus!"
    n "Why don’t we let them decide?"
    "Nauxus spreads his arms out wide."
    n "My brothers. We were once united under one flag and lived in peace. We can still return to that."
    n "Your people need you to stand against the tyranny of the bulls!"
    n "Make the right choice, let’s end this feud once and for all!"
    "Rogue Lizard Leader" "Don’t listen to him! Never forget what he did to our old advisors from before. He-"
    n "I didn't come here to talk about the past. I’m here to pave the way to the future. "
    n "The past doesn’t have to define you."
    n "Now’s your chance at claiming back your lives in the village, and start anew."
    "The murmurs rise like the coming of the climax of a rousing song."
    "Even you feel slightly inspired by Nauxus."
    "Rogue Lizard Leader" "No! He is not our chief! He stole that title, and he’s never rightfully completed the chief’s rite of passage!"
    "Nauxus crosses his arms and his pupils sharpen."
    n "The rite of passage you say... Very well, if that is what it takes to convince you all, I’ll gladly take the rite of passage in front of everyone here. "
    "Nauxus points to the rogue leader."
    n "I’m sure you’ll be executing the ritual fairly? "
    n "Wouldn’t want everyone here to think they're following a hypocrite crusade, now would we?"
    "The rogue leader snarls at Nauxus."
    "Rogue Lizard Leader" "Fine! The rite of passage will be done as our forefathers did before us!"
    "Rogue Lizard Leader" "Select one lizard that will complete the rite of passage with you."
    n "I choose my ally, here."
    show nauxus stand at center with dissolve
    "He turns to you, and you nod."
    "Rogue Lizard Leader" "Then let the ritual commence. Prepare the ring!"
    "More lizards leap out from their hiding spot and rush over to clear the spears before hiding back among the trees."
    "You take the chance to whisper to Nauxus."
    e 1 "Nauxus... What is this whole rite of passage thing?"
    n "Don’t worry. It’s just two tests that are supposed to prove my ability to lead."
    n "The first one’s a fight, then the other ... \nWell, we’ll worry about that when we get there."
    e 5 "Nauxus!"
    hide nauxus stand at center with dissolve
    "Two rogue lizards brandishing their weapons come forth and stand next to their leader."
    "Rogue Lizard Leader" "Let the first trial commence! The test of strength! If you and your ally cannot overcome the strongest of our group, you are not fit to lead."
    "The rogue leaders leaps back behind the cover of the trees while the other two approach you both with their weapons ready."
    n "I’ll take the one on the left! Go!"
    if Quest.bombt ==4:
        e 13 "(I can’t purposely lose here.\nIf I do, it might cost me my life."
        e 1 "(I’ll need to wait for another chance.)"
    jump battle_lizard
    label Nauxus_rite1:
        show nauxus stand at center with dissolve
        "Nauxus manages to defeat his foe the same time as you do."
        "They collapse onto the muddy ground before another pair of lizards come by and pick them."
        "The crowd speaks with surprised tones about Nauxus’s victory."
        "The rogue leader emerges, his face twisted into a scowl of discontent."
        "Rogue Lizard Leader" "Pure luck."
        n "If that’s the best you all have, maybe I should reconsider my offer."
        "Rogue Lizard Leader" "Onward to the next trial!"
        "Two lizards come forth. Each of them take their place in front of you and Nauxus."
        "In their hands they hold a small cup. "
        "You’re unable to pick up any smells from the drinks they hold."
        "Rogue Lizard Leader" "Have your poison, and if Nauxus is worthy of being chief, he won’t let you die."
        "Your eyes widen in shock."
        e 5 "Die?!"
        n "Yes, but it won’t come to that. Still, how do I know you didn’t just upped the dosage on these?"
        "Rogue Lizard Leader" "Yes, how would you."
        n "Toss those cups out and pour them again in front of me."
        "Rogue Lizard Leader" "Tsk. Paranoid as always."
        n "Well if you are so sure you are guilt free."
        n "Please, drink out of one of them now. "
        "Rouge Lizard Leader" "Hngh... Toss the cups!"
        "Some in the hidden crowd jeer towards their leader. "
        "Nauxus smirks mockingly at the embarrassed leader."
        "New cups are brought forth, and you both watch while the concoction is made but with poisons from different jars."
        "Rogue Lizard Leader" "Now drink, and Nauxus will guide you to the cure, if he is able to."
        "Nauxus picks up one cup and you do the same."
        n "Cheers."
        hide nauxus stand at center with dissolve
        "You gulp down the entire drink in one go. At first you feel fine."
        e 1 "Well that wasn’t so-"
        show red1 at center with dissolve
        e 9 "?!" with vpunch
        "Then it hits you like a ton of bricks falling on your shoulders."
        "Your whole body becomes excessively heavy. "
        e 0 "Hngh!"
        "You struggle to even stay upright."
        "Nauxus himself is hunched over, and is sweating profusely."
        e 12 "Did he ss-sabotage the trial?"
        n "N-no. This is- ugh normal."
        n "Looks to the leader."
        n "Where are the paths you crazy lizard."
        "The leader points to his back. There are two paths leading further into the swamp."
        "Rogue Lizard Leader" "Don’t forget the rules."
        "Rogue Lizard Leader" "You are to only find and pick up the ingredients for the other lizard’s poison."
        "Rogue Lizard Leader" "You cannot cure yourself."
        "Rogue Lizard Leader" "Once you return you can brew the ingredients and apply the antidote."
        "You feel an immense weight upon your chest."
        n "I’m going to ugh, read you the ingredients. You need to find them for my poison."
        e 12 "Ok, let’s gggo."
        n "You need a blue azalea, one vine from the swamp trees, and a blue swamp lily. "
        n "Don’t pick the yellow swamp lilies, as they’ll make the antidote slow to react. "
        n "Now go, I know- gahhh! I know what to get for yours."
        scene black with slow_dissolve
        play sound "music/foot1.ogg"
        "You nod, and struggle to walk down the right path."
        "Every step feels harder than the next, but you need to keep going."
        "The vines are the easiest to find since they are everywhere. "
        "Yet, the moment you try to pull one apart, the poison kicks in and you lose all feeling in your left arm."
        "It falls to your side like there are no bones in your arm."
        show red2 at center with dissolve
        "Panic sets in, forcing you to make haste and find the other ingredients."
        "You swipe the blue azalea not too far from where you got the vine. "
        scene swamp 4 with slow_dissolve
        show red1 at center
        show red2 at center
        "As you plunge further into the swamp, you find bushes of swamp lilies."
        "Blue and yellow lilies grow all over."
        "There’s no time for you to relax as your left leg is already slowly lagging behind."
        if Quest.bombt ==4:
            $ jane_inv_K.drop(selye_amulet)
            $ Time.anauxus = Time.days
            "You reach out for the yellow lily, but stop yourself just inches away."
            "Doubt clouds your thoughts. This may prevent a war, but you will end up hurting Nauxus. "
            "The antidote made from the yellow lily will work, but at a slower rate."
            "Would you and Nauxus be able to escape while he recovers?"
            "The sudden sting across your chest snaps you out of your thoughts."
            scene black with slow_dissolve
            show red1 at center
            show red2 at center
            "You hastily grab the yellow lily and make your way back to the starting point."
            scene swamp 3 with slow_dissolve
            show red1 at center
            show red2 at center
            "Once you return to the opening, Nauxus is hunched over a boiling pot."
            "In front of him is the rogue leader watching him intensely."
            show nauxus stand at center with dissolve
            show red1 at center with dissolve
            show red2 at center
            "He turns to you and hands you a vial of golden liquid."
            n "Quick, take your antidote and pass me the ingredients."
            "You hand Nauxus everything you have in exchange for the vial. "
            "You down the contents on the vial, and your body feels limber again."
            hide red1 with dissolve
            n "What? This is a yellow lily [name]. I can’t use this."
            e 9 "I’m sorry. I-I panicked-"
            n "[name]! I told you it was the blue lily." with vpunch
            hide red2 with dissolve
            "Rogue Lizard Leader" "Then the rite of passage is over. You’ve failed, Nauxus."
            "Through the mist the rogue lizards surround the both of you with their weapons ready and bloodlust in their eyes."
            n "Damn it!"
            "Rogue Lizard Leader" "I knew you were nothing more than a sham Nauxus."
            "Rogue Lizard Leader" "You are no chief! Let us relieve you of your duties."
            e 5 "No wait, you can’t do this!"
            "Rogue Lizard Leader" "Attack!"
            hide nauxus stand at center with dissolve
            "Nauxus roars and throws something on the ground. "
            "Whatever it was explodes and releases a large grey cloud that instantly consumes the entire area." with vpunch
            "You are grabbed by the wrist in all the confusion."
            "You recognize it’s Nauxus’ hand."
            n "Run!" with vpunch
            "Rogue Lizard Leader" "After them!"
            "You hear the sound of skulls knocking into one another as the rogue lizards try to find you."
            scene black with dissolve
            "Somehow you both manage to ram through the crowd and run as fast as you can towards the entrance of the dark swamp."
            "The rogue lizards didn’t give chase, and even if they did the two of you are way ahead from them."
            "You both keep running until you reach the entrance to the lizard village."
            scene swamp 2 with slow_dissolve
            "Exhausted, you both stop and are frantically gasping for air."
            show nauxus stand at center with dissolve
            hide nauxus stand at center with dissolve
            "Nauxus takes a seat on a large root of a mangrove tree."
            "You bend over next to him. Every breath you take feels like you’re gulping down mouthfuls of water."
            "Nauxus coughs."
            e 9 "We... we.... Need to get inside. You need the antidote!"
            "Nauxus pants and looks at you with a dark expression."
            "He pulls out an empty vial from his satchel."
            e 5 "When did you?"
            show nauxus stand at center with dissolve
            n "I had it on me from the start. Wasn’t expecting that I needed to use it though."
            "He shakes his head."
            e 9 "I..."
            "Nauxus raises his hand to silence you."
            n "How could you have messed that up? It was just one colour."
            n "Was it the poison? Did that freak out at the last minute?"
            e 5 "..."
            n "Look, I need some time to process what just happened."
            n "You don’t need to find me. I need to be alone for a while."
            e 13 "Nauxus..."
            hide nauxus stand at center with dissolve
            "He stands up and pulls the amulet off of your neck."
            "A part of your heart is tugged away as he walks off with his cold eyes."
            "You wonder as you stood there alone, did you make the right choice this time? "
            "Feeling defeated, you decide to head back to Thane and report on what happened."
            $ Quest.bomb_end = 0
            $ Quest.bomb_lizard= 2
            $ Quest.bomb_bull= 2
            $ Quest.bombn = 5
            $ Quest.bomb = 5
            $ Quest.bomb_result = Thane
            $ Nauxus.s = Nauxus.s + 2
            $ Axel.s = Axel.s + 2
            $ Quest.bombt = 5
            $ Thane.help = Thane.help +1
            jump forest_map0
        elif True:
            scene black with slow_dissolve
            show red1 at center
            show red2 at center
            "You grab the blue lily without hesitation, and drag yourself back to the starting point."
            scene swamp 3 with slow_dissolve
            show red1 at center
            show red2 at center
            "Once you return to the opening, Nauxus is hunched over a boiling pot."
            show nauxus stand at center with dissolve
            show red1 at center with dissolve
            show red2 at center
            "In front of him is the rogue leader watching him intensely."
            "He turns to you and hands you a vial of golden liquid."
            n "Quick, take your antidote and pass me the ingredients."
            "You hand Nauxus everything you have in exchange for the vial. "
            "You down the contents on the vial, and your body feels limber again."
            hide nauxus stand at center with dissolve
            "Nauxus dumps all the ingredients into the pot and stirs it."
            hide red1 with dissolve
            "He staggers a bit every few seconds, but manages to complete the concoction."
            hide red2 with dissolve
            "He takes a drink from the pot with his ladle, and proudly raises it into the air."
            "A mix of cheers and jeers erupts all around you."
            "Nauxus tosses the ladle aside, and begins to address the lizards hidden in the mist."
            show nauxus stand at center with dissolve
            n "It’s done! Are you not satisfied? I’ve proven my right to be chief by the old ways."
            "Rogue Lizard Leader" "No, no no! This means nothing! I will not accept it, and neither will we!"
            "Nauxus points accusingly at the rogue leader."
            n "That’s not for you to decide."
            n "I ask again, who among you will pledge your loyalty to me now, and return to the village a free lizard?"
            "Rogue Lizard leader" "Don’t listen to him! It’s all a trick."
            "Rogue Lizard leader" "It’s all just his ploy to get rid of us. "
            "Rogue Lizard Leader" "We won’t fall for your deception! Everyone else, leave!"
            hide nauxus stand at center with dissolve
            "The rogue leader runs into the fog and you hear the sound of hurried footsteps coming from on top the trees."
            e 5 "What the heck? Come back!"
            scene black with slow_dissolve
            "Your voice is drowned by the pitter-patter of feet running through the trees."
            "As the sounds dwindle away, Nauxus notices something."
            scene swamp 3 with slow_dissolve
            show nauxus stand at center with dissolve
            n "Wait, someone’s coming."
            "From the mists a single lizard appears unarmed."
            "He appears unsure of what to do."
            "Rogue Lizard" "Umm... were you being honest about letting us go back to our families?"
            n "Yes, help me defend the village. That’s the reason I became chief."
            n "I just want to protect the same people we love and care about. And we can’t do it without each other."
            "The lizard looks to the ground then back to Nauxus."
            "Rogue Lizard" "Then I pledge my allegiance to you, Chief Nauxus."
            "The rogue lizard gets on one knee and bows lowly."
            "Nauxus" "Rise my warrior."
            e 13 "What are you going to do with just one guy?"
            "Rogue Lizard" "It isn’t just me, there are others who believe in your words and long to return."
            "Rogue Lizard" "Allow me to rally them."
            n "Very well. Then you’ll meet me outside at the swamp just before the lizard village."
            n "Make haste, I will only give you one hour to be there."
            "The lizard nods and returns into the depths of the swamp."
            scene black with slow_dissolve
            "Nauxus leads you back out of the dark swamp and you both return to the lizard village."
            scene lizardtribe 1 with slow_dissolve
            "Back at the entrance to the village, Nauxus summons Blue and Red."
            "He instructs them to prepare for the returning lizards."
            "In the meantime, the chief pulls you aside to speak personally."
            show nauxus stand at center with dissolve
            n "I couldn’t have done this without your help."
            n "I’ll need some time helping these new lizards settle in, so for now, take this."
            "<[name] gained 300 coins>"
            "<[name] gained one Level-up-point.>"
            $ jane_inv.take(coin,400)
            $ Zalt.points = Zalt.points +1
            $ jane_inv_K.drop(selye_amulet)
            e 1 "Well I couldn’t have done it without Selye’s help. He did make this amulet and all. "
            n "Right, then I will make sure to give him the proper thanks."
            e 1 "Could you give this back to him too?"
            "You take off the amulet and hand it to Nauxus."
            n "Are you actually asking the chief to be an errand boy for you?"
            e 5 "Oh, I forgot myself there. I’m sorry."
            "Nauxus laughs."
            n "I’m just pulling your leg. I’ll hang on to this as part of my collection."
            n "Thank you [name]."
            $ Quest.bomb_end = 0
            $ Quest.bomb_lizard= 2
            $ Quest.bomb_bull= 2
            $ Quest.bombn = 5
            $ Quest.bomb = 5
            $ Quest.bomb_result = Nauxus
            $ Axel.s = Axel.s + 3
            $ Quest.bombt =5

            "You smile warmly at Nauxus and take your leave."
            jump Lizard_tribe_map0


label Nauxus_festival:
    if Quest.fesn ==1:
        "Upon entering the council chambers you see Red speaking to Nauxus who sits on his throne."
        "The advisor is howling his concerns at the chief."
        "Red" "It will be impossible for us to gather back all those fruits in time for the ceremony."
        n "What about our regular supply of food?"
        "Red" "Come on chief, think about the kids."
        "Red" "They’ve been cooped up for so long, they at least need one day of fun."
        "Red" "Simple grains aren't going to cut it."
        n "And you’re sure the bulls didn’t steal the fruits last night?"
        "Red" "I’m sure. Here, look at this bite mark."
        "Red" "Whatever it is isn’t bull or lizard."
        "Red hands Nauxus a half eaten green apple."
        n "Alright, I’ll look into it Red."
        n "Make sure the festival preparations go as plan, but we’ll hold off the real celebration until we can get the fruits back."
        "Red" "Will do Chief Nauxus."
        "Red takes his leave."
        "Nauxus then waves at you to come to him."
        show nauxus stand at center with dissolve
        e 1 "Hey Nauxus, so I hear you’ve hit a snag."
        n "A big snag."
        if Quest.bomb_result == Axel:
            n "Right on the heels of the bulls’ attack."
            "Nauxus slams his right fist on the arm of his throne and proceeds to massage the side of his eyes."
            n "I cannot let this festival fail."
            n "My people need it now more than ever!"
            e 13 "I’m sure the people will understand."
            e 13 "Besides, if there are hurt or even... dead warriors from the explosion, isn’t now too soon for a celebration?"
            n "It’s not only a celebration, it’s a chance for everyone to gather, and to remember the ones we’ve lost."
            n "Especially... especially for those children who are newly orphaned."
            "Nauxus looks up to the ceiling for a second and inhales deeply."
            e 13 "Right..."
        elif Quest.bomb_result == Nauxus:
            n "The timing cannot be worse."
            n "After all it took to recruit the rogue lizards back into the tribe."
            n "I don’t want them to doubt their decision to join us just because I can’t pull off a festival."
            e 6 "I’m sure it’ll take more than that to have them lose faith in you so quickly."
            n "An optimistic thought [name], but it’s a risk I’m not willing to take."
        elif True:
            n "The success of this festival is important to the war efforts."
            n "I won’t let my people’s morale fall because of a few fruits."
        n "[name], I’m counting on you to get those fruits back."
        e 1 "No offense, but why can’t you get Selye to conjure up some new fruits instead?"
        "Nauxus rolls his eyes at you."
        n "Because he can’t. When I first met that naga he told me he only knows magic relevant to combat."
        e 6 "And making food isn’t relevant to combat? "
        n "Not to him. So, I- nay, the whole village really needs your help."
        n "I’d send my men but they are preoccupied with keeping guard of the other supplies and helping with the preparations."
        n "So will you take the job?"
        label Nauxus_festival_start:
            menu:
                "Yes" if True:
                    e 1 "I’ll take the job."
                    n "Good, then speak to the shopkeeper."
                    n "She will provide you with a sack to carry back the fruits."
                    n "It’s a lot, about 500 pieces if whatever that stole them hasn’t eaten most of it."
                    e 1 "Alright. "
                    n "Take this with you. It might help."
                    "Nauxus hands you the half eaten fruit."
                    hide nauxus stand at center with dissolve
                    "He then summons one of the guards into the council room."
                    n "Mention to the shopkeeper that I instructed [name] to go to where the theft occurred."
                    n "Have her provide him with the tools and directions he will need. "
                    n "Also update the guards outside of the storage hut about [name]’s involvement."
                    n "They are not to hinder his investigation."
                    "The guard nods and leaves the room."
                    "Nauxus walks closer to you and puts a hand on your shoulder."
                    "Up close, the dark rings under Nauxus’s eyes can be seen as clear as day."
                    show nauxus stand at center with dissolve
                    n "I’ll hold off the start of the festival until you return."
                    n "Now go, I have some work to deal with."
                    e 1 "Yeah, I’ll do my best."
                    "Nauxus nods and you take your leave."
                    $ Quest.fesn = 3
                    if Quest.fesa >= 3:
                        if Quest.bomb_result == Axel:
                            scene lizardtree 2 with slow_dissolve
                        elif True:
                            scene lizardtree 1 with slow_dissolve
                        e 13 "Both villages have been hit by the fruit thief."
                        e 13 "The timing is way too perfect to be coincidental."
                        e 1 "Not to mention..."
                        "You pull out the half eaten fruits you got from both villages."
                        e 1 "The bite marks on these two fruits are identical."
                        e 13 "So, I’m just dealing with one monster. "
                        e 1 "Any path I take to track down the creature won’t matter then."
                        jump Lizard_tribe_tree0
                    jump Lizard_tribe_meetingroom
                "No" if True:
                    e 6 "I’ll need some time to prepare before I can accept the job."
                    n "Very well. Come find me when you’re ready."
                    $ Quest.fesn = 2
                    hide nauxus stand at center with dissolve
                    jump Lizard_tribe_meetingroom
    elif Quest.fesn ==2:
        show nauxus stand at center with dissolve
        n "Are you ready to help us take back our festival fruits?"
        jump Nauxus_festival_start
    elif Quest.fesn >=3 and Quest.fesn <=5:
        show nauxus stand at center with dissolve
        n "The shopkeeper will provide you a sack to carry the fruits."
        n "I’m sure the creature must have left some sort of a trail for you to follow."
        hide nauxus stand at center with dissolve
        jump Lizard_tribe_meetingroom
    elif True:
        jump Lizard_tribe_meetingroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
