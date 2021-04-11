label meko_meet:
    $ Time.mins = Time.mins +5
    if Meko.meet == 0:
        scene basement 1 with dissolve
        play music "music/drip.ogg"
        "You walk down and find someting looks like a stack of barrels."
        "On the side of the barrel you see the words."
        "“Rum” scratched into it as if by a knife or some sharp object."
        $ Snow.basement = 1
        "Just as you reach out to grab the crate and leave, you hear a voice.."
        play music "music/whoisthere.ogg"
        "..."
        "Something faintly whispers into your ear."
        "You turn around but there’s nothing there."
        "???" "My..."
        "There it is again, but it’s clearer."
        "???" "My...lo......"
        e 5 "Who’s there? Show yourself!"
        "Only silence replies you."
        "Suddenly, from the corner of your eye you notice an orange light flickers."
        show black2 at center with dissolve
        show candle01 at center with dissolve
        "You turn and find a candle between the barrels."
        "Was that always there?"
        "Your face tenses up, and you stare in wide eyed terror."
        e 5 "..."
        show candle02 at center with dissolve
        "The warm orange glow fills the entire basement, illuminating all the barrels and doors."
        "You feel your heart pounding against your chest,desperate to run away."
        "But you’re frozen in place."
        "From the candle’s flames, a part of it breaks away and floats towards you."
        "Growing ever so slightly as it gets closer."
        e 5 "(Come on move! Move legs!)"
        "Still your body refuses to budge."
        show candle03 at center with dissolve
        "The floating orange flame is so close to you now, you can feel the heat radiating off of it."
        play music "music/ohmeko.ogg" fadeout 2
        hide candle01
        hide candle02
        hide candle03 with dissolve
        "POOF."
        hide black2 with dissolve
        "The flame erupts in a puff of white smoke."
        "And in its place, a floating war horn?"
        show meko stand at center with dissolve
        "???" "My love! [name]!"
        "???" "You’ve finally come back to me."
        e 5 "..."
        "You stare in disbelief, the war horn is talking to you."
        "There’s no one holding the war horn but sound is clearly coming from it."
        "???" "Finally, after so long we can be together again."
        "???" "Just like you promised."
        "???" "Hmm? Why aren’t you saying anything [name]?"
        e 5 "Wh-Wh What the hell are you?"
        m "It’s me, Meko. Remember?"
        m "The last time we met, you said."
        m "“Come back to me, it’s us against the world,and no monster, no time,{p} will stop us from being together again.So, come back.”"
        "The horn’s voice... it’s distorted somehow."
        "Like someone with a deeper voice echoes back the words it says."
        "Making it sound like two people talking simultaneously. "
        e 5 "You’re crazy. I’ve never met a talking horn mug in my life."
        "You try to move your legs, but not even your toes would curl."
        m "Hmm, am I mistaken? Aren’t you my [name]?"
        e 9 "I’m a mad [name]. Why can’t I move?"
        e 9 "This is insane. Snow! Hakan!"
        m "They can’t hear you."
        m "If you haven’t noticed you’re trapped in a magical barrier."
        m "That’s why you’re not moving either."
        e 9 "What! Let me go you monster!"
        m "Monster? Ok, ok."
        m "I just didn’t want you to run off if you saw me like this, but I mean you no harm. "
        m "There, I just want to talk."
        "It doesn’t look like he did anything to you physically."
        "The horn continues to hover in front of you."
        "You sense no malice coming from it."
        menu:
            "Attack the horn." if True:
                hide meko stand
                "You pull out your sword and swing at the horn."
                "The blade hits him right in the middle."
                "But you feel a powerful force emanating from the point of impact."
                "You’re unable to press the blade through."
                "The force blasts your sword away and sends it flying towards a pile of barrels behind you."
                "The horn makes a sound like a sigh."
                show meko stand at center with dissolve
                m "Had enough? Now, let's be mature and just talk."
            "Talk to the horn." if True:
                e 9 "How do I know you’re not going to pull off some kind of mind trick on me."
                e 9 "You magic types can’t be trusted."
                m "Well, if I could I would have already done it."
                m "And if I did, it would’ve been a pretty shitty mind control spell cause you won’t listen to me."
                m "Trust me, if I was messing with your mind, you wouldn’t even question it."
                m "Now, let's be civilized and talk."
        "You tsk."
        "Looks like you have to talk to him now."
        $ Meko.meet = 1


    elif Meko.meet != 0 and Meko.howdie == 1 and Time.days >= 5:
        scene basement 1 with dissolve
        show meko stand at center with dissolve
        m "Aha! You've come at an opportune time."
        m "I've discovered a source of power I thought long lost since my time."
        m "Show me your map."
        e 1 "What is this about?"
        m "What is this about? This is about getting out of this foggy forest. How can you forget?"
        e 5 "Right, sorry I’ve been caught up in this war between the lizards and the bulls."
        e 2 "I just sort of forgot."
        m "I’m worried about you [name]."
        m "It’s starting to feel like the longer you’re here, the less you want to go home."
        e 5 "What? No, it can’t be. I still want to leave."
        e 1 "We all do. There’s just nothing much to go on right now."
        m "Hmm, well pull out your map. I’ll show you what I found."
        "Meko levitates upwards while you pull out your map and lay it out on top of the barrel."
        "He spins and points at a spot with the tip of his reed."
        m "My clairvoyance showed me that it's a tribe of bulls."
        m "Somewhere, in a broken temple I sense a familiar magic."
        if Map.sproom == 0:
            m "It’s the same kind of magic we used before to create paintings to other worlds."
            m "If you can find these paintings and a source of magical power, you could escape."
            e 1 "Wait, what about the rest?"
            m "I didn’t think about that part."
            m "They won’t be able to use those paintings unless they have some source of magic. "
            e 1 "..."
            e 13 "We’ll have to think of something else."
            m "[name], think this through, I’m offering you a way out."
            e 1 "And I’m not taking it, it’s all of us or it’s none of us. I’m sorry, Meko."
            "Meko sigh."
            m "You never change,[name]."
            m "Alright, I’m not going to argue about your choice, should’ve known you’d never try to take the easy route."
            m "But try to find those paintings."
            m "Even if you’re not going to use them to escape, we can’t let them fall into the wrong hands."
            e 1 "Right, I’ll look out for them."
            "Meko floats back down onto his barrel."
            "Now, what else do you want to talk about?"
        elif True:
            m "It’s the same kind of magic we used before to create paintings to other worlds."
            m "If you can find these paintings and a source of magical power, you could escape."
            e 1 "Paintings? As in the paintings at the bull temple?"
            e 6 "I found them already."
            m "No way!"
            m "Well this is embarrassing. Sorry, I’m not much help."
            "Meko floats away from you, and he lets out a long drawn out sigh."
            e 5 "Meko, it’s fine, you did the best you could."
            m "I could do more if I was alive, or if I had all my powers again."
            e 13 "Meko..."
            m "I’m sorry I wasted your time, it’s no wonder you’d want to forget me."
            e 1 "That’s not true. I hear you’re hurting, but I never once said I didn’t appreciate your help."
            e 1 "In fact, I’m glad I know someone else knows about that room, because there’s so much I want to know about that place."
            m "Well, what do you want to know?"
            e 1 "What are they for?"
            m "Well they’re supposed to be portals to other worlds."
            m "Magic users used to use them to look into other worlds and learn their secrets, some even moved to those strange lands if they liked it enough."
            e 5 "Then that means it’s a way out! "
            m "No, not really. You’ll need a source of magic to get those paintings to open up and go through it."
            m "And I doubt anyone else in this tavern knows anything about magic."
            e 13 "Damn it."
            e 1 "We’ll have to think of something else."
            m "Alright, but if you find some way to unlock those paintings, let me know."
            e 1 "Right."
            "Meko floats back to his barrel."
            m "Well I feel a bit better, anything else you want to talk about?"
        $ Meko.howdie = 2
        jump meko_talk
    elif True:


        if Roushk.meko == 1:
            scene basement 1 with dissolve
            show meko stand at center with dissolve
            m "[name]! I have good news."
            e 13 "Finally a break, so far looking for other ways to get rid of the curse has been a bust."
            m "The curse removal spell is ready."
            m "Bring Roushk over when you are ready."
            $ Roushk.meko = 2
            jump meko_talk
        elif Roushk.meko == 2 or Roushk.meko ==3:
            scene basement 1 with dissolve
            show meko stand at center with dissolve
            m "The curse removal spell is ready."
            m "Bring Roushk over when you are ready."
            e 1 "Alright."
            jump meko_talk
        elif True:
            pass
    jump meko_talk

label meko_talk:
    scene basement 1
    if EF.meko == 1:
        $ EF.meko = 2
        e 1 "Meko."
        "Meko’s horn glows and fires a red translucent demonic hand that grabs you by the throat."
        m "Demon! You dare come here to take me back? I’m not going just yet!"
        e 9 "Meko! Meko! It’s me!"
        show meko stand at center
        m "[name]?"
        "Meko undoes the demonic hand."
        "You gasp for air while rubbing your neck."
        e 9 "What the hell was that?"
        m "I’m sorry, I just sensed the presence of a demon, and acted on instinct."
        e 9 "Wait, do I have a demon on me?"
        m "Hmm... no, just some residue."
        m "Like how you pick up a smell after being in a room for a while, same thing with being near a demon."
        m "What happened?"
        e 1 "Well long story short I found a city of demons. "
        m "No way, crap, crap. You have to make sure they don’t come find me."
        e 1 "Why?"
        m "I’m afraid they will try to bring me back to the afterlife."
        e 1 "The demons are in charge of that?"
        m "Perhaps, but I don’t want to take my chances."
        m "Death and demons go hand in hand, and it’s not like I have experience coming back from the dead."
        e 13 "Ok, I’ll keep that in mind."
        m "So, is there something else you need?"
        jump meko_talk_horn


    if Quest.fes_end == 2 and Quest.fes_meko == 0:
        $ Quest.fes_meko = 1
        if Thane.movein != 2:
            e 1 "Meko you wouldn’t have a spell that can make two sides not go to war right?"
            m "If I did, it would have saved me a whole lot of time. "
            m "Has the conflict between the two tribes reached boiling point?"
            e 13 "Boiling point and beyond."
            e 1 "There is no way to make them see rason now."
            e 1 "Look, I’ll look into this war as much as I can, but if I don’t make it."
            m "No!"
            e 5 "I was going to say-"
            m "I know what you will say, my love, but dying in battle is not an option."
            m "Say that you will figure this out, and you will come back and we’ll find a way to free you from this fog."
            e 13 "Meko..."
            m "Say it."
            e 1 "Ok. I’ll come back."
            m "Good, now you got anything else to talk about?"
            jump meko_talk_horn
        elif True:
            m "There’s a lot of commotion today."
            e 1 "Well Thane-"
            m "Was injured, I know."
            m "I was there while the tavern folk was tending to him."
            e 13 "I just feel so angry and useless right now."
            e 1 "Why did it have to be Thane? "
            m "No one could have predicted it would have happened to him."
            e 13 "Still, I’m the one who convinced him to come stay here."
            e 1 "Maybe if he stayed behind none of this would have happened."
            m "We don’t know that. "
            m "I hear the hurt in your heart my love."
            m "It pains me to see you blame yourself."
            e 1 "Meko..."
            m "Don’t lose hope, let this moment strengthen your resolve to free everyone from this fog as soon as possible."
            m "You are [name], I know you can do it."
            e 13 "Thanks."
            m "Is there anything else you want to talk about?"
            jump meko_talk_horn
    if Meko.bathcomment == 0 and Map.bathroom_0 == 4:
        $ Meko.bathcomment = 1
        show meko stand at center with dissolve
        m "I can’t believe it, a brand new bath house!"
        e 6 "Technically, it’s the old one but better."
        m "We should go together."
        e 9 "Are you sure that’s a smart move? "
        e 1 "They would be wondering who Meko is in the guest book."
        e 6 "More importantly, can you even feel the water?"
        m "To a degree I can feel it."
        m "My senses are mostly dulled."
        m "Still, it would be nice to do something fun together."
        e 1 "It does sound like fun."
        m "Be more fun if I had a body back."
        m "I could hold you close, brush your fur, and even kiss you again. "
        e 1 "... "
        e 1 "Yeah... "
        "His words speak of a time long forgotten, of a memory that you do not possess."
        "It aches your heart to see the spirit who’s been helping you all this while hanging on to a hope that he would see his beloved again."
        "Yet, you don’t remember anything about him. "
        jump meko_talk_horn
    show meko stand at center with dissolve
    m "[name]! I’m so happy to see you again. What do you need?"
    label meko_talk_horn:
        menu:
            "Is there an afterlife?" if Meko.lose == 1:
                e 1 "If you’re here, does that mean there’s something after death?"
                m "I don’t think you would want to know that."
                e 13 "Of course I do if you can be here. Then my mom-"
                m "No, [name]. The dead should stay dead."
                m "There’s a heavy price to pay to break that rule."
                e 13 "Right."
                m "But I can tell you this much, instead of worrying about what’s to come after life."
                m "I find living in the moment is the best experience there is."
                e 1 "I’ve been hearing that a lot."
                m "It’s sage advice, you should listen to it."
                jump meko_talk
            "What do you want?" if Meko.lose == 0:
                e 1 "What is it you want from me?"
                m "Want? I don’t want anything really other than to be with you again."
                e 9 "That’s not possible, don’t ghosts have unfinished business or hold some kind of grudge?"
                e 9 "That’s why you can’t move on."
                m "Hmm... not really. I lived a pretty fulfilling life."
                m "I wanted to come back because of the promise I made to you."
                m "But now that you’ve mentioned it."
                m "I wish you quit trying to get rid of me."
                m "I thought you’d be used to talking to spirits."
                e 1 "What are you talking about?"
                e 1 "You’re the first ghost I’ve ever met."
                stop music fadeout 2
                m "That can’t be right."
                m "I’ve been keeping an eye on you since you came to this tavern."
                m "You’ve been talking to a ghost this whole time."
                play music "music/him.ogg" fadeout 2
                e 5 "What? Who?"
                m "You know-"
                show black2 at center with dissolve
                show meko stand1 at center with dissolve
                "Meko starts to screech in a shrill voice."
                "The body of his horn turns into a dark hue like it’s made completely of shadows."
                e 5 "Meko! Meko, what’s wrong?"
                "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Woopsie, that was a close one.{/color}{/b}"
                "This isn’t Meko’s voice."
                "It sounds like someone younger, and more high pitched."
                "But you don’t recognize this voice."
                "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Wouldn’t want him to give away the ending so soon.{/color}{/b}"
                "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Don’t worry I’ll just wipe our little friend’s memory, and he’ll be all well.{/color}{/b}"
                e 12 "What the hell are you?"
                e 12 "Are you the one behind those monsters and the fog?"
                "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Hmm? You don’t need to worry your pretty little butt about that,[name].{/color}{/b}"
                "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Just keep doing what you’re doing, and we’ll all get along,[name].{/color}{/b}"
                e 12 "Answer me!"
                "{color=#7d0004}???{/color}" "{b}{color=#7d0004}No,no,no,no. I don’t need to tell you anything,[name].{/color}{/b}"
                "{color=#7d0004}???{/color}" "{b}{color=#7d0004}You’re just here for my entertainment,[name].{/color}{/b}"
                "{color=#7d0004}???{/color}" "{b}{color=#7d0004}Consider yourself lucky I am making it a rule not to mess with your pretty little head,[name].{/color}{/b}"
                e 12 "You won’t get away with this. I’ll find you."
                hide meko stand1 with dissolve
                "The voice laughs loudly at you. Its laughter grows louder, forcing you to cover your ears."
                "Your head feels like it's going to burst from the sound."
                e 9 "Aaaaahh!"
                stop music fadeout 1
                "The laughter dies out."
                hide black2 with dissolve
                show meko stand at center with dissolve
                "Meko's horn changes back to its original colour. He floats in silence."
                e 12 "... What?"
                m "[name]? Why do you look so freaked out."
                e 9 "Meko? Is that you?"
                m "Yeah, it’s me. What’s wrong?"
                e 5 "Meko, don’t you remember?"
                e 5 "You were possessed by something just now."
                m "Possessed? That can’t be. I was just floating here."
                e 5 "No, you were."
                e 5 "You were about to tell me about who’s the spirit I’ve been talking to."
                e 5 "Then you turned green, and it was someone else's voice coming out through you."
                m "[name] are you all right?"
                m "I don’t remember seeing you talk to any other spirits here."
                e 5 "..."
                "That thing changed his memory."
                m "Now, now, don’t look so glum."
                m "Maybe our reunion has tired you out."
                m "You should get some rest."
                e 13 "..."
                "You frown at Meko."
                "It doesn’t look like pressing him for answers will get you anywhere for now."
                e 13 "(Maybe I better deliver the rum to Snow first.)"
                $ jane_inv_K.take(Box_of_wine)
                $ Meko.lose = 1
                jump T_basement
            "You need to be kept a secret." if Meko.lose == 1:
                e 1 " I’ve got nothing to talk about."
                e 1 "You... you better stay hidden."
                e 1 "If you cause any trouble, or if anyone finds out, I will find someway to end you."
                m "So, it’s like we have to meet in secret?"
                m "Like just us? The world never knowing about us? "
                "He plays a cheerful toot."
                e 5 "Shhhhh! What are you doing? Someone’s going to hear you."
                m "Don’t worry, I take the precaution of enchanting the area around us."
                m "Whenever we are around, no one will want to come down here."
                e 8 "It didn’t keep whatever it was possessing you earlier from coming."
                jump meko_talk
            "Why are you out in the open now?" if Meko.lose == 1:
                e 1 "Meko what are you doing?"
                m "Just talking to you."
                e 13 "No, I mean why is your horn out in the open here on top of the barrel."
                m "It’s no big deal."
                e 1 "Yes, it’s a big deal."
                e 8 "Someone’s going to ask why is there a horn mug here."
                m "Just tell them you like playing the horn mug when you’re free."
                e 5 "No one will believe that!"
                e 5 "And if they did they probably think I’m a weirdo playing a horn mug down here."
                m "Relax, if it bothers you that much."
                m "I’ll just make myself visible to you only."
                e 1 "You can do that?"
                m "It’s pretty basic magic."
                e 1 "Oh, hmm. Ok then."
                m "No problem, is there anything else you want to talk about?"
                jump meko_talk
            "How did you die?" if Meko.lose >= 2 and Meko.howdie != 2:
                e 1 "Meko, err I want to ask you something personal?"
                m "Sure, if you'll answer my questions about the state of the world."
                e 5 "The state of the world? Why?"
                m "Well I am more curious about where we are."
                m "Ever since I appeared I have this feeling that something's not right."
                m "Like some larger force is acting all around us."
                e 1 "You're not wrong."
                e 1 "Ok, answer me first and I'll tell you what's going on."
                m "Alright, what's the question?"
                e 1 "How did you die?"
                m "I died... because of a broken heart."
                m "You weren't there when I came back from the war."
                m "So, I went into a depression I never recovered from."
                e 9 "Err..."
                m "Just kidding."
                m "I lived a full life, and died peacefully in my sleep when I was fifty."
                e 13 "Never knew someone to joke about their own death."
                m "[name],I've been dead for hundreds of years."
                m "You eventually learn to let it go and embrace the afterlife."
                m "Now tell me, what's happening around this tavern?"
                e 13 "Well, there's a mysterious fog surrounding this area."
                e 13 "It looked like it was just a forest."
                e 1 "But the more I explore, the more I find hidden around here."
                e 1 "So far I've found a tribe of bulls and lizard men living to the east and west of the tavern."
                e 1 "We're all just buying time until the fog opens up and we can leave."
                m "Hmm... this is most troubling to hear [name]."
                e 13 "It is, but at least everyone in the tavern is taking it well."
                m "Maybe I can help."
                e 1 "How?"
                m " I'll explain once I find out if it will work."
                m "Don't want to get your hopes up."
                m "Come back a few days and ask me again about it."
                m "It'll take all my energy to check this out."
                m "For now, we can talk about other stuff. "
                $ Meko.howdie = 1
                jump meko_talk
            "Did you have a family before you die?" if Meko.lose >= 2 and Meko.howdie != 2:
                e 1 "Before you died, did you have a family?"
                m "You mean like a wife, and children?"
                e 1 "Yeah."
                m "Some part of me wishes I could have had that."
                m "I think many people wanted that for me, but I couldn’t lie to myself."
                m "Not after meeting you."
                e 1 "..."
                e 13 "I’m sorry, you make it sound like we had some deeper connection, but I barely know you."
                m "I’m trying to understand that too."
                m "It pains me that you can’t remember."
                e 13 "It’s just..."
                e 6 "I would be hundreds of years old, if what you’re saying is true."
                m "Maybe you’re a mage like me?"
                e 6 "I can’t cast a spell to save my life."
                e 6 "Maybe you should consider that you have the wrong guy."
                m "Oh..."
                e 1 "Meko?"
                m "..."
                e 13 "Meko?"
                m "Sorry... I was lost in thought."
                m "Could we maybe talk about something else?"
                e 1 "Oh, yeah sure."
                e 13 "(He sounds upset. Did I say something wrong?)"
                jump T_basement
            "Ask how Meko’s holding up." if Meko.takeawalk == 0 and (Quest.campb == 6 or Quest.campt == 6 or Quest.campl ==6):
                e 1 "How are you holding up? Looks pretty dull sitting here all day."
                m "Oh, it’s not that bad. I’ve got the occasional bugs scurrying about."
                m "I like to pretend they’re like my neighbours and I make up stories about their day to day activities."
                e 1 "Ok..."
                m "I’m being sarcastic if you can’t tell."
                m "Honestly, I’m bored to death down here."
                m "Helping you out kills some time, but there’s really nothing to do. That and-"
                m "It’s not like I have you to talk to."
                e 1 "That’s not right, I come by. I visit."
                m "Yeah, but you’re not my [name]."
                hide meko stand with dissolve
                "The horn floats upwards until your eye level."
                show meko stand at center with dissolve
                m "Do you know why I’m a horn?"
                e 1 "I... no, I don’t know."
                m "Yeah, the you I knew might know."
                hide meko stand with dissolve
                "You avert your gaze from Meko, the awkwardness makes it hard to look him in the eye, wherever his eyes are."
                "Brushing your right arm up and down, you think hard about what to say."
                "The way he speaks about you, about the life he had with you, it makes you feel slightly guilty for disappointing him."
                "The sound of Hakan laughing loudly above echoes through the floorboards above."
                show meko stand at center with dissolve
                m "Huh, sounds like they’re having fun up there."
                e 5 "Hey, I’ve got an idea!"
                e 1 "If you can make your presence not be noticed, maybe you could go up and see what the others in the tavern are doing."
                m "Really? You won’t mind?"
                menu:
                    "Yes" if True:
                        e 6 "Just make sure they don’t find out about you, I’ve haven’t found the right time to explain your presence."
                        m "I promise, you won’t even know I’m there. Thanks [name]."
                        m "Anything else on your mind?"
                        $ Meko.takeawalk = 1
                    "No" if True:
                        e 3 "Ehhh,just kidding!"
                        e 4 "Is this joke making u happier?"
                        m "[name]."
                        e 2 "Sorry."
                jump meko_talk

            "Ask about Meko’s powers" if Quest.campb == 6 or Quest.campt == 6 or Quest.campl ==6:
                e 1 "How is it every time I come down here, you have some kind of brand new power?"
                m "You expect anything else from one of the greatest Enchanter of all time?"
                e 6 "Sounds like you're tooting your own horn."
                hide meko stand with dissolve
                "You grin at Meko as he lets out a long drawn horn blow."
                show meko stand at center with dissolve
                m "I'll pretend I didn't hear that."
                m "But yes,at the peak of my prime I was quite skilled with magic."
                m "Now without a body, it's like relearning everything again, and even then some spells just don't work."
                m "So, I guess we both will have to find out together what I can do."
                "You nod and look at Meko with tired eyes."
                hide meko stand with dissolve
                "The memory of when he first appeared before you reemerges."
                "Ever since then it’s just been you and him trying to figure a way out of the fog."
                "An almost depressing but also reassuring thought, that you aren’t in this alone. Reaching out you gently stroke the horn."
                show meko stand at center with dissolve
                m "Hmm? You look troubled [name]. "
                e 13 "It’s just, I realized I wouldn’t even know there’s something dark behind the fog if you didn’t turn up."
                m "You mean the thing that took away my memory about the suspicious spirit in the tavern?"
                e 1 "Yeah."
                m "Hmm, I'm still not convinced about this enemy thing, but the fog is weird. "
                "Sighing loudly you shake your head. "
                e 1 "What's it going to take to convince you that we are in danger?"
                m "Nothing, I've learnt from a lifetime of magic that not everything is as it seems, and you have to take a leap of faith sometimes."
                m "So, if you say there's an enemy out there, I believe you my love."
                e 7 "That was very corny, but thanks."
                m "If I had eyeballs I would be rolling them at you."
                "You laugh and feel a sense of reassurance fill your heart."
                e 13 "But there is one thing that still bugs me."
                m "What?"
                e 1 "I don’t know what to do if I find the supposed spirit among us."
                e 1 "You’re a ghost, what do you suggest? "
                m "Well I’m a biased source, but I’d hear the soul out."
                m "Even if they're dead, they were people too, give them a fair trial and all that."
                m "If that doesn’t work, a charged punch should take them out."
                "Your face darkens and you look to your hands, clenching it tightly."
                jump meko_talk




            "Ask about Witer" if Witer.sleep >= 2 and Witer.sleep <= 3:
                if Witer.sleep == 2:
                    e 1 "Hey, you notice anything weird about Witer?"
                    e 13 "He looks like he’s not getting enough sleep, but he keeps brushing it off."
                    m "This Witer is that green alligator, correct?"
                    m "The one who sleeps with the red dragon?"
                    "You nod."
                    m "Now that you’ve brought it up."
                    m "I've actually been watching him lately, and wanted to let you know if I found out why he’s doing his unusual conversations at night."
                    e 1 "What do you mean?"
                    m "Since last week, at 3 a.m. he’d leave his room and faces the barrels near the wall."
                    m "He just sits there and acts like he’s having a conversation with someone."
                    m "He would make mentions of, “The plan is set...”, “We’ll get out of here soon...” or “It’s dangerous to go alone...”"
                    m "It’s completely unsettling, and I’m the one back from the dead."
                    "A ghost he says."
                    e 5 "You think he’s maybe communicating with another spirit? Like you?"
                    m "I wouldn't rule it out without any proof."
                    m "Despite my time in the afterlife I am still new about coming back to the mortal plane."
                    m "If there really are spirits talking to him, they’re hiding their presence pretty well."
                    m "Anyways, he’ll just talk to those barrels for an hour before going back into his room."
                    e 13 "Hmm, alright, keep a lookout if anything happens."
                    e 1 "I’ll think about what I need to do for now."
                    m "Alright, anything else?"
                    $ Witer.sleep = 3
                    jump meko_talk
                elif True:
                    m "That alligator keeps talking to the wall for an hour at 3 a.m. every night."
                    m "You might want to check it out."
                    jump meko_talk
            "How to defeat a ghost?" if Witer.sleep == 5:
                e 5 "Meko, I need you!"
                m "I’m ready. Just make sure to prepare some lubrication or this is going to hurt for both of us."
                e 8 "What? Meko, get your head out of the gutter."
                m "How? I don’t have a head now."
                e 12 "Ughh, now is not the time for jokes!"
                e 1 "There’s a ghost possessing rocks, and I need a way to defeat it."
                m "Oh, that is serious. Someone could step on it and get hurt."
                e 5 "Meko... why are you being so cheeky all of a sudden?"
                m "Well maybe if I had a nice room to be in..."
                "You cock your head sideways unsure of what Meko is trying to say."
                e 1 "What do you mean?"
                "A long sigh hisses out of the horn."
                m "You loveable idiot. So a ghost rock, and you need a way to defeat it?"
                e 1 "Yes."
                m "It just so happens I do know a spell to allow you to fight spirits like that."
                m "But for it to work, I will have to share some of my own magic to help you use it."
                e 1 "Alright, what do I have to do?"
                m "You need to blow me."
                e 1 "..."
                e 1 "I’m sorry, I think you just said blow you?"
                m "Well look who has his head in the gutter now. I’m a horn [name]."
                m "You’re not giving me a blowjob."
                e 7 "Oh! Ok, I can do that."
                hide meko stand at center with dissolve
                "You pick up Meko with both hands and bring him close to your face."
                "Swallowing your saliva you have some apprehension to put your lips on his reed."
                m "Get on with it back there, you’ve put worse things in your mouth."
                e 5 "Wait how did you know?"
                m "JUST DO IT!"
                "You close your eyes and take the plunge wrapping your lips around the reed and blowing as hard as you can."
                with flashbulb
                "The blow of the horn is ridiculously loud, thank goodness for the magic that keeps Meko a secret."
                "From the other end of the horn a blue wisp of flame floats out and suspends itself in mid air before it breaks apart and flows like a stream of blue energy into your chest."
                "The energy flow feels warm and comforting like a cup of hot chocolate on a cold winter’s night."
                "Once the blue energy disappears, Meko floats off your hand and lands back on his barrel."
                show meko stand at center with dissolve
                m "There you should be able to use the skill now."
                m "By sharing my magic you should know how to use the spell."
                "You ball your right hand into a fist and feel energy coursing through your veins."
                "Like a memory lay dormant for ages newly awaken you feel fresh clarity and confidence to cast this spell."
                "Sparks of energy pop and crackle around your fist, you push your concentration further and the sparks covers your hold hand like a glove."
                m "Behold, the anti-ghost spell, the ‘Holy Fist’."
                e 1 "That's... a pretty lame name."
                m "If you don’t like it, I can take it back."
                e 5 "No, it’s perfect. Thank you, Meko."
                m "You’re welcome, stay safe using that thing."
                "{b}{color=#19c22a}<You’ve learnt how to use Holy Fist. Now you can inflict damage to ghosts.>{/color}"
                "Time for a rematch with that rock."
                $ Battle.holyf = True
                jump T_basement
            "Goodbye." if Meko.lose >= 1:
                e 1 "That’s all. I’ll talk to you later."
                m "Alright, you know where to find me."
                if Meko.lose == 1:
                    $ Meko.lose = 2
                jump T_basement
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
