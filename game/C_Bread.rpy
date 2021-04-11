label Bread_meet:
    $ renpy.music.set_volume(0, 5, channel = "Chan1")
    "The badge fits the slot and you hear an inner mechanism click from behind the walls."
    "A roaring rumble permeates the walls of the cave as the sealed wall begins to split in half and move to its sides."
    "You watch in anticipation as heavy clouds of dust descend from the ceiling."
    "All of this security, it must have been for some kind of a treasure."
    "Your palms feel sweaty as you imagine the rich treasure inside."
    "Maybe a powerful weapon or even a mountain of gold!"
    "The door is now completely open."
    scene caveruin 2 with vslow_dissolve
    "You squint to take a better look through the settling dust. "
    "The glowing moss inside the room illuminates what looks like a suit of armour in the middle of the chamber."
    "You approach the suit of armour and kneel next to it to get a better look."
    "It looks like a regular set of armour made of steel. "
    "Why would anyone lock it up inside here?"
    show bread stand at center with dissolve
    "Your hand reaches out to touch the visor, when suddenly a pair of bright blue eyes open up from within the helmet."
    show bread shock at center
    e 9 "AHHHHHHH!" with vpunch
    "???" "AHHHHHHH!" with vpunch
    "The shock sends you tumbling back on your ass."
    "The knight flails his arms as he struggles to pick himself up."
    "You manage to get on your feet first and draw your sword, but the knight is up as well swinging his chain mace by his side."
    e 12 "Hold it spectre, or I’ll kick your ass like all the other phantoms in this castle!"
    "???" "Spectre? What’s that? I’m Bread."
    e 5 "What? You’re a piece of bread in a suit?"
    e 5 "What kind? A loaf? A baguette? A croissant? "
    b "A crow-what? No, my name is Bread, defender of the king’s treasure vault!"
    b "And I don’t know who you are, but I won’t let you have the king’s treasure!"
    b "Surrender raider!"
    e 9 "Raider? You got the wrong idea bub, and even if I were one, there’s no treasure left here."
    e 1 "This kingdom has been long abandoned, all the people probably died out."
    show bread sad at center with dissolve
    b "Dead?… No!"
    b "You’re lying, Aplistia would not fall to anyone."
    b "We’re the greatest kingdom there is."
    e 5 "Listen to me, there’s nobody here and there sure is no treasure left."
    e 5 "This place has been abandoned for hundreds of years!"
    "The knight grabs his helmet and tosses his head from side to side while growling in pain."
    show bread stand at center with dissolve
    b "YOU LIE! YOU WON’T TRICK ME YOU DIRTY RAIDER!" with vpunch
    "He charges at you!"
    "You sidestep to the left and dodge his swing."
    e 9 "Stop, we don’t need to fight!"
    b "Raargh!"
    "The knight won’t listen to reason."
    hide bread stand
    jump battle_bread

label battle_bread:
    hide screen bag
    hide screen inventory_screen
    hide screen EWinventory_screen
    hide screen EWinventory_view_new
    $ wolf_max_hp = 100
    $ wolf_hp = wolf_max_hp
    $ players_turn = False
    $ wolf_max_lust = 100
    $ wolf_lust = 0

    $ renpy.music.set_pause(True, channel='Chan1')
    $ renpy.music.set_pause(True, channel='Chan2')

    $ Battle.holyfcd = 0
    stop music


    jump battle_bread_loop


label battle_bread_loop:



    show screen simple_stats_screen
    show screen battle_menu
    show bread_fight at center
    play music"music/forest_fight_friend.ogg"





    while (wolf_hp > 0) and (Zalt.hp > 0) and(Zalt.lust <100):
        $ players_turn = True
        $ res = ui.interact()
        $ players_turn = False
        if res == "Holy Fist":
            $ red_damage = renpy.random.randint(Zalt.MATK*2, int((Zalt.MATK*2.5)+10))
            $ wolf_hp -= red_damage
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            $ Battle.holyfcd = 3
            $ Random = renpy.random.randint(1, 3)
            if Random == 1:
                "You dart forward and land a punch on the enemy."
            elif Random == 2:
                "You hit the enemy with your Holy Fist."
            elif True:
                "With blazing speed you hit the foe with Holy Fist."
            " (Damage dealt - [red_damage]hp)"

        if res == "Items":
            $ Zalt.hp = min(Zalt.hp +5, Zalt.maxhp)
            $ cookies_left -= 1
            "*Drink* 5hp restored"

        if res == "Attack":
            $ red_damage = renpy.random.randint(max(1,Zalt.ATK-20), Zalt.ATK)
            $ Random = renpy.random.randint(0, 100)
            if Random >= Zalt.CRIT:
                $ wolf_hp -= red_damage
                "You draw your sword and lunge in for an attack.\n(Damage dealt- [red_damage]hp)"
            elif True:
                $ qty = red_damage*2
                $ wolf_hp -= red_damage*2
                "You draw your sword and lunge in for an attack.\n{b}{color=#ffd65c}(Critical damage! -[qty]hp){/color}"

        if res == "Submit":
            e "I can't fight anymore.."
            "The enemy is too strong."
            "You’re knocked onto the ground."
            jump battle_bread_lose
        if res == "Flirt":
            $ Random = renpy.random.randint(1, 5)
            if Random == 1:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+5)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "You pin Bread onto the floor and grind your hips against his armour."
                "Bread groans loudly before kicking you in the groin forcing you to release him."
            elif Random == 2:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+5)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "Knocking the knight back with a strong push, you flash a confident smile before licking your lips sensually."
                "Bread groans loudly before kicking you in the groin forcing you to release him."
            elif Random == 3:
                $ Zalt.flirt = renpy.random.randint((Zalt.cha*2)+3, (Zalt.cha*2)+5)
                $ wolf_lust = wolf_lust+Zalt.flirt
                "Locking his arms and neck in a strong hold you whisper into his visor all the dirty things you can do to him while in his armour. "
                "Bread shakes his head and punches himself to focus, but you can see his eyes focusing on your crotch."
            elif True:
                $ Random = renpy.random.randint(1, 3)
                if Random == 1:
                    "You pin Bread onto the floor and grind your hips against his armour."
                    "Bread’s spike ball hits you in the stomach, stopping you from trying to seduce him."
                elif Random == 2:
                    "Knocking the knight back with a strong push, you flash a confident smile before licking your lips sensually."
                    "Bread’s spike ball hits you in the stomach, stopping you from trying to seduce him."
                elif True:
                    "Locking his arms and neck in a strong hold you whisper into his visor all the dirty things you can do to him while in his armour. "
                    "Bread’s spike ball hits you in the stomach, stopping you from trying to seduce him."
            if wolf_lust >= 100:
                hide screen simple_stats_screen
                hide screen battle_menu
                hide screen battle_skill
                hide screen battle_item

                stop music
                jump battle_bread_win
            elif True:
                pass
        if res == "Bind up":
            $ Zalt.heal = renpy.random.randint((Zalt.int*2)+20, (Zalt.int*2)+35)
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ Zalt.mp = min(Zalt.mp -20, Zalt.maxmp)
            "*Bind up* [Zalt.heal]hp restored"
        if res == "Hp potion":
            $ Zalt.heal = 60
            $ Zalt.hp = min(Zalt.hp+Zalt.heal, Zalt.maxhp)
            $ jane_inv.drop(hp_potion)
            "*Hp potion* [Zalt.heal]hp restored"
        if res == "Mp potion":
            $ Zalt.heal = 60
            $ Zalt.mp = min(Zalt.mp+Zalt.heal, Zalt.maxmp)
            $ jane_inv.drop(mp_potion)
            "*Mp potion* [Zalt.heal]mp restored"
        if res == "Escape":
            "You can't run!"
        elif True:
            pass

        $ Random = renpy.random.randint(1, 3)
        if Random == 1:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Bread swings his chain mace from a distance."
                "The metal chain extends outwards and sweeps across the space between the two of you."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(15, 45)
                $ Zalt.hp -= wolf_damage
                "Bread swings his chain mace from a distance."
                "The metal chain extends outwards and sweeps across the space between the two of you."
                "The spike ball hits you across the arm before you could block."
        elif Random == 2:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Bread swipes his claws at you."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(15, 35)
                $ Zalt.hp -= wolf_damage
                "Bread swipes his claws at you, cutting you deeply."
        elif True:
            $ Random = renpy.random.randint(1, 100)
            if Random <= Battle.dodge:
                "Bread rushes forward and swings for your head."
                "But you dodged his attack!"
            elif True:
                $ wolf_damage = renpy.random.randint(20, 40)
                $ Zalt.hp -= max(1,wolf_damage-Zalt.DEF)
                "Bread rushes forward and swings for your head."
                "You soften the blow by blocking with your sword but the impact still hurts."

        if Battle.holyfcd !=0:
            $ Battle.holyfcd = Battle.holyfcd-1





    if wolf_hp <= 0:
        if Zalt.hp <= 0:
            jump battle_bread_kill
        elif True:

            jump battle_bread_kill

    elif Zalt.hp <= 0:
        jump battle_bread_lose
    elif Zalt.lust >= Zalt.maxlust:
        "You're too horny to fight anymore."
        "You fall to the ground."
        jump battle_bread_lose
    elif True:
        jump battle_bread_loop


label battle_bread_kill:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    play sound "music/blood.ogg"
    "With one mighty swoop, your blade cuts across the knight’s neck, the metal cuts halfway through his neck."
    hide bread_fight with dissolve
    "His arms fall limp to the side."
    "He makes some weak guttural sound before his eyes close and his lifeless body collapses to the ground."
    "The battle is over."
    "Perhaps this is better, at least now he can be with his fallen brethren. "
    "You wipe the blood away from your sword and loot the body."
    "You get the Leopard Signet Ring."
    $ jane_inv_E.take(bread_ring)
    $ Bread_meet = -1
    jump Cave_map

    return

label battle_bread_win:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    "Bread’s movements are slowing down."
    "He charges at you while swinging his mace, but he seems preoccupied with hiding his codpiece behind his free hand."
    hide bread_fight with dissolve
    "You dodge his swing and trip him with your foot."
    "The knight tumbles forward and crashes into the wall behind you, face first." with vpunch
    "He staggers back a few steps before falling on his butt and then collapsing on his back."
    e 1 "Err… are you ok?"
    "No answer."
    "You walk over towards his body."
    "He’s still breathing, but he does not respond to you even when you kick him in the gut."
    "This knight’s unconscious."
    "Breathing a sigh of relief, you take away his weapon. "
    e 13 "Can’t just leave him here like this."
    "You plop his unconscious form against the wall and try to check for any injuries that need treatment."
    scene black with vslow_dissolve
    pause 3
    scene caveruin 2 with slow_dissolve
    "Sitting across from the knight you continue to watch him. "
    "His armour resembles the ones the creature deep inside the castle wore before. "
    "You recall him stating he was the treasure room guardian, but for how long?"
    "There’s not a shred of food or water inside this chamber."
    show bread sad at center with slow_dissolve
    b "Ughh…"
    e 1 "Well hello there sleeping beauty."
    hide bread sad
    show bread stand at center with dissolve
    "His blue eyes flutter as he awakens. "
    b "Ughh… what happened? Where’s… my mace?"
    "You wave his mace in front of him."
    e 1 "It’s right here, but I’m not giving it back to you until we talk. "
    hide bread stand with dissolve
    "Bread moves about , rubbing all over himself."
    b "Hey, my wounds have healed?"
    e 1 "Well yeah, I couldn't just leave you bleeding out here."
    "Bread gasps."
    show bread stand at center with dissolve
    b "That's…."
    show bread happy at center
    b "THE NICEST THING ANYONE'S DONE FOR ME." with vpunch
    b "THANK YOU BUDDY." with vpunch
    hide bread happy at center with dissolve
    "He lunges at you and traps you in a bearhug."
    "His hold on you is bone crushingly strong."
    e 9 "Guhh! too tight! Too tight!" with vpunch
    show bread happy at center with dissolve
    b "Sorry, I forget my own strength sometimes."
    "You look at him with a bewildered stare."
    e 5 "What’s your deal? One minute you can’t wait to bash my head in."
    e 5 "Now you’re acting all buddy buddy with me?"
    show bread stand at center with dissolve
    b "Now why wouldn’t I want to be your buddy?"
    show bread happy at center
    b "You helped me up, and good folk always help others, that’s what Nana taught me."
    b "You should meet her."
    e 13 "Right… Look, Bread I need you to really listen to me."
    hide bread happy with dissolve
    "You hold his shoulders and look soulfully into his eyes."
    show bread stand at center with dissolve
    e 1 "Bread, when we first spoke, you were very convinced that the kingdom is still alive."
    b "Well yeah, how can it not be? I’ve only been in here for two days."
    e 9 "Two days?"
    e 1 "Bread, just come with me and I’ll show you."
    hide bread stand at center with dissolve
    scene black with slow_dissolve
    "You take Bread to where the broken castle stands."
    scene belltower 1 with slow_dissolve
    "Along the way he seems unphased by the state of things around him."
    b "Wow, this whole place is a mess."
    b "The king will be most displeased when he hears how the groundskeepers have been slacking off."
    e 1 "..."
    scene black with slow_dissolve
    "Descending deeper, you both approach the castle."
    "Bread becomes considerably quieter while the both of you make your way down the belltower."
    "Once the castle comes into view, Bread stands stunned next to you."
    b "No… this can’t be real."
    b "No, no, no!" with vpunch
    "He tries to run towards the castle gates but you grab his hands and hold him back."
    e 9 "Stop Bread! There’s nothing left in there, only monsters and phantoms! "
    b "No! There has to be! Nana, has to be in there. " with vpunch
    b "Captain Asmund would have protected everyone!"
    "His strength drags your feet forward no matter how hard you dig your soles into the ground."
    e 1 "I’m telling you the truth, please there’s nobody left inside."
    e 13 "They’re all gone!"
    "Bread halts his movements and falls to his knees in tears."
    "His tears echo through the abandoned cave, calling out to those he knew, but none would ever answer back."
    "All you can do is watch in silence. "
    pause 3
    scene caveruin 2 with slow_dissolve
    "After Bread calms down, he asks to go back to his chamber."
    "You respect his choice and the both of you make your way back to the room."
    e 13 "Bread, I’m sorry for your loss."
    show bread sad at center with slow_dissolve
    b "..."
    hide bread sad with dissolve
    "He sighs and sits on the floor."
    e 1 "Hey, if you want, I know a place where you can get a room and something to eat."
    "Bread shakes his head."
    b "I don't think I am ready to leave yet. I need to mourn Nana and the Captain a bit longer. "
    e 13 "Ok, I might come by to check on you when I can."
    "You return the knight's weapon and take your leave."
    $ Bread_meet = 1

    jump Cave_map

    return

label battle_bread_lose:
    hide screen simple_stats_screen
    hide screen battle_menu
    hide screen battle_skill
    hide screen battle_item
    stop music fadeout 1
    hide bread_fight with dissolve
    "Bread comes charging at you and swings his mace over his head."
    "He lets loose his weapon, its chain extends outwards and circles around your blade."
    "You’re unable to use your weapon."
    scene black with vslow_dissolve
    "He pulls back with enough force to relinquish you of your sword."
    play sound "music/blood.ogg"
    "Defenceless, Bread unleashes a barrage of punches. "
    "Each hit he lands is like getting smacked repeatedly by a large rock."
    play sound "music/blood.ogg"
    "Your vision blurs and turns a dark shade of red as your blood flows from your cracked skulls down your face."
    "All your senses go numb and the last thing you ever see is the knight’s bloody fist slamming into you one more time."
    show red2 at center with dissolve
    "{b}{color=#c22719}<GAME OVER>{/color}"
    menu:
        "New game" if True:
            return
    stop music


label Bread_map_start:
    scene caveruin 2
    "Inside the empty chamber that is now the temporary home of the enigmatic Bread."
    "You find the knight slumped against a rock, looking at a piece of paper."
    e 1 "Hey Bread."
    b "…"
    "He clutches the paper tighter."
    e 6 "Are you ok?"
    "He doesn’t answer, instead you hear weak sobs coming out of his visor."
    e 1 "Bread?"
    show bread sad at center with slow_dissolve
    b "I found the map... but I don’t understand it."
    "You crouch down next to Bread, hesitating to reach out to him."
    b "I really am stupid. I thought I could find this treasure all on my own then… at least maybe that would make the captain happy in the afterlife."
    b "But I can't-"
    b "I don’t understand this map at all."
    b "Why did I think I could do this? Even Captain Asmund couldn’t solve it."
    b "Maybe at least he stood a chance, but I don’t."
    e 1 "Bread..."
    e 1 "Hey, hey, it’s not over yet. Maybe I can help, just let me take a look at the map."
    hide bread sad with dissolve
    "Bread pulls the map away."
    b "No, it’s... it’s knight’s property."
    e 1 "Well, what can I do to help?"
    "Bread sighs loudly."
    show bread stand at center with slow_dissolve
    b "I wish I had some bread to eat right about now."
    e 1 "So you’re finally hungry?"
    b "Not really, it’s just something nice to have when I’m down."
    b "The kitchen always had a nice warm pot of gruel and bread for me to eat back in the castle."
    b "Maybe that’s why I’m so fat."
    e 1 "Well stress eating would do that to someone."
    e 1 "There are other ways to manage your problems you know, like training."
    b "I train with my flail all the time."
    e 1 "Yeah, but have you considered working on your body?"
    b "I mean, sometimes?"
    e 1 "I’m not saying it’s bad to have some weight, it's just-"
    hide bread stand with dissolve
    "You reach out and poke the knight’s belly."
    e 0 "Oh!"
    "The softness of his fur and fat surprises you."
    "You poke again and again."
    "Before you know it, you’re just rubbing the knight’s belly."
    e 1 "You’re so soft."
    "Bread lets out a high pitched whine."
    show bread shock at center
    b "Please don’t touch me there. It tickles." with vpunch
    "You pull your hand away."
    show bread sad at center with dissolve
    b "But now that you've mentioned it, Captain Asmund did say I had to lose some weight so I can fit into my armour better."
    b "But I think I can fight well too."
    b "What do you think I should do?"
    e 1 "You're asking me? Well-"
    menu:
        "Encourage Bread to train his body" if True:
            $ Bread.train = 1
            e 1 "I'd say give it your best and train."
            e 1 "The fog is dangerous out there."
            e 1 "You'll need to be at your best to survive out there."
            show bread stand at center with dissolve
            b "If you say I got to train, then I will."
            e 1 "I didn't know you valued my opinion so much."
            b "Well, there's a reason for that."
            e 1 "And the reason is?"
            b "I'm not really a knight. More of a knight in training."
            b "I want to be a real knight [name], but I cannot do that alone."
            b "Captain Asmund was my trainer and he said he would tell me when I would be ready to be called a knight."
            b "He's gone now, but I want to complete my training and receive my knighthood."
            b "You've bested me in battle, so I have to admit you're strong."
            b "Plus you are kind to me, it reminds me a lot of Captain Asmund."
            show bread happy at center with dissolve
            b "So, I’ll pick you to be my new knight trainer."
            e 9 "What!? But I barely know anything about knights."
            b "You're just being modest, Master. "
            b "Ever since I fought you, I knew there was knight blood in you."
            e 1 "Knights don't have any different blood, Bread."
            e 1 "Look if you want more training, fine. I guess we can train."
            b "Yes!"
            e 1 "Then pack your things, and let's move out to the tavern."
            show bread stand at center with dissolve
            b "Err… can I stay here instead Master?"
            e 5 "Why would you want to stay here?"
            b "I'm scared. You said a lot of years have passed, I don't think I'll fit in."
            e 1 "Bread, there are nice people."
            e 1 "They might even be able to help with your map."
            show bread sad at center with dissolve
            b "No, I'm sorry Master, you may punish me as you like but I won't go."
            e 1 "Hmm."
            "It would seem that Bread is against joining the tavern."
            "If only there was something you could give to convince him it isn't all that bad to stay in the tavern."
        "Let Bread be" if True:
            e 1 "Well if you are comfortable and you’re sure you can fight still, I guess what you're doing isn't so bad."
            b "A force to be reckoned with, fat or no fat."
            show bread happy at center with dissolve
            b "Yeah, my chain mace training is always in top form."
            b "After the thousandth hit, I figured out how to hit the opponent instead."
            e 1 "That is not very reassuring, but yeah you have potential with that weapon."
            b "Then I’ll keep practising with my weapon."
            b "There’s also one more thing I wanted to ask."
            e 1 "What is it?"
            show bread stand at center with dissolve
            b "Would you be my mentor so that I can achieve knighthood?"
            e 1 "Excuse me?"
            b "I’m technically not a full fledged knight, more of a knight in training."
            b "Captain Asmund said I could not have the title of knight until he deemed me ready."
            b "And I doubt that’s possible now…"
            b "So, could you take me under your wing and allow me to earn the title of knight?"
            e 1 "I mean, I could just give it to you right now."
            b "That’s not how it works."
            b "I need to be tested, and only a true mentor can see if I am ready."
            e 6 "I don’t really know much about being a knight."
            show bread happy at center with dissolve
            b "It’s more than just a title, ever since we first fought, I could tell you have knight-like qualities in you."
            b "Please, let me train under you."
            e 1 "If it’s training you want, I can lend a hand in that."
            b "Thank you Master!"
            "You scratch the back of your right ear while you think about what you need to do with Bread."
            e 1 "Then let's go back to the tavern, you can at least ask around for help on figuring out the map."
            show bread shock at center with dissolve
            b "Umm, I am comfortable here, Master."
            b "I rather not cause any trouble at your place."
            e 1 "It won’t be any trouble at all, everyone is nice and the accommodations are plenty."
            hide bread shock at center with dissolve
            "Bread sighs heavily."
            show bread sad at center with dissolve
            b "You’ve told me many years have passed, I’m just afraid I won’t fit in with such a different world out there."
            show bread stand at center with dissolve
            b "It’s safer in here."
            e 1 "Bread…"
            "It would seem that Bread is against joining the tavern."
            "If only there was something you could give to convince him it isn't all that bad to stay in the tavern."
    "You get up."
    e 1 "Then we’ll continue this talk another time, till then, good luck."
    show bread happy at center with dissolve
    b "I’m on it, Master!"
    "He stands up to shake your hand but accidentally steps on his weapon and tumbles back down."
    b "Ahh!"
    e 8 "Oh, Bread."

    jump Cave_map
label Bread_talk:
    scene caveruin 2
    if jane_inv.qty(jam_oatmeal_bread) != None:
        e 1 "Hey Bread. "
        show bread stand at center with slow_dissolve
        e 1 "Look at what I got."
        e 6 "Delicious oatmeal bread from the tavern."
        e 3 "Mmm, bread. Your favourite."
        "You pull out the oatmeal bread and show it to the knight."
        b "Hmm…"
        "You split the bread in half to share it with him."
        "He accepts the bread and holds it to his face."
        "He sniffs the bread."
        e 1 "(How is he going to eat that?)"
        hide bread stand at center with dissolve
        "You blink."
        show bread happy at center with slow_dissolve
        "The bread in his hand is gone."
        e 9 "Mmm, not bad."
        "Your mind is baffled. Did he just eat that whole thing in a blink of an eye?"
        e 1 "Ah… So, did you enjoy it?"
        b "It’s really tasty. "
        e 1 "If you want more you can come to the tavern."
        e 1 "Then you’ll have bread almost every day."
        show bread shock at center with dissolve
        b "Bread every day?!"
        b "I don’t know… But it was really good. Ugh, no I got to control myself."
        e 1 "What if I bring a sweeter pastry?"
        show bread happy at center with dissolve
        show bread shock at center with dissolve
        "His eyes light up. You got him."
        b "N-no. I-I must train. Thank you."
        e 1 "No pressure, think about it. I’ll come back with something else soon."
        b "Master, you don’t have to do that."
        b "A knight must not be spoiled like this."
        e 1 "I’m not spoiling you, it’s just me sharing good food with a friend."
        e 1 "Ok? So, see you later."
        e 1 "(He liked the oatmeal bread but is still unsure.)"
        e 1 "(What else can I try to bring him to convince him?)"
        hide bread shock
    elif True:

        show bread stand at center with slow_dissolve
        e 1 "Are you sure there is nothing I can do to convince you to come to the tavern?"
        show bread shock at center with dissolve
        b "Absolutely nothing, my will is strong."
        b "That… and I won’t be able to fit in."
        e 1 "I’ll come back to you later Bread."
        show bread happy at center with dissolve
        b "See you later, Master."

    jump Cave_map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
