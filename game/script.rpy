
python early:
    config.searchpath.extend(['game//music','game/music','game//sounds','game//images//map','game//images//map//fog','game//images//icon','game//images//UI','game//images//items'])
init python:
    mp = MultiPersistent("b.w")
    toscrossld = MultiPersistent("tos.ld")

init -2 python:
    class GetInput(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)

init python in Zalt:
    pass

init python in Axel:
    pass

init python in Ludiko:
    pass

init python in NPC:
    pass

init python in Bread:
    pass

init python in Hakan:
    pass

init python in Snow:
    pass

init python in Thane:
    pass

init python in Item:
    pass

init python in Witer:
    pass

init python in Chet:
    pass

init python in Battle:
    pass

init python in Map:
    pass

init python in Foe:
    pass

init python in Nauxus:
    pass

init python in Parif:
    pass
init python in Selye:
    pass
init python in Time:
    pass
init python in Quest:
    pass
init python in Roushk:
    pass

init python in Ebb:
    pass
init python in Flo:
    pass

init python in Hellhound:
    pass


define e = Character("[name]",who_color = "#22a5f0",image="side")

image side side = "icon/side_0.png"
image side side 0 = "icon/side_0.png"
image side side 1 = "icon/side_1.png"
image side side 2 = "icon/side_2.png"
image side side 3 = "icon/side_3.png"
image side side 4 = "icon/side_4.png"
image side side 5 = "icon/side_5.png"
image side side 6 = "icon/side_6.png"
image side side 7 = "icon/side_7.png"
image side side 8 = "icon/side_8.png"
image side side 9 = "icon/side_9.png"
image side side 10 = "icon/side_10.png"
image side side 11 = "icon/side_11.png"
image side side 12 = "icon/side_12.png"
image side side 13 = "icon/side_13.png"
image side side 14 = "icon/side_14.png"
image side side 15 = "icon/side_15.png"


image castle_fog_1 = "map/fog/screen/castle_fog_1.png"
image castle_fog_2 = "map/fog/screen/castle_fog_2.png"
image castle_fog_3 = "map/fog/screen/castle_fog_3.png"
image castle_fog_4 = "map/fog/screen/castle_fog_4.png"
image castle_fog_5 = "map/fog/screen/castle_fog_5.png"
image castle_fog_6 = "map/fog/screen/castle_fog_6.png"
image castle_fog_7 = "map/fog/screen/castle_fog_7.png"
image castle_fog_8 = "map/fog/screen/castle_fog_8.png"
image castle_fog_9 = "map/fog/screen/castle_fog_9.png"
image castle_fog_10 = "map/fog/screen/castle_fog_10.png"
image castle_fog_11 = "map/fog/screen/castle_fog_11.png"
image castle_fog_12 = "map/fog/screen/castle_fog_12.png"

image prison_fog_1 = "map/fog/screen/prison_fog_1.png"
image prison_fog_2 = "map/fog/screen/prison_fog_2.png"
image prison_fog_3 = "map/fog/screen/prison_fog_3.png"



define lslow_dissolve = Dissolve(1)
define a = Character("Axel",who_color = "#edd72d")
define asm = Character("Asmund",who_color = "#7a9694")
define b = Character("Bread",who_color = "#ccb79d")
define c = Character("Chet",who_color = "#b3722d")
define f = Character("Flo",who_color = "#e38d24")
define s = Character("Snow",who_color = "#134ea1")
define l = Character("Ludiko",who_color = "#36282c")
define w = Character("Witer",who_color = "#006605")
define h = Character("Hakan",who_color = "#991f18")
define t = Character("Thane",who_color = "#965e0b")
define n = Character("Nauxus",who_color = "#60686e")
define m = Character("Meko",who_color = "#c3c7c9")
define p = Character("Parif",who_color = "#ede5d8")
define se = Character("Selye",who_color = "#612375")
define eb = Character("Ebb",who_color = "#0a8494")
define ro = Character("Roushk",who_color = "#bd190f")



define re = Character("Red lizard",who_color = "#ba2f25")
define bl = Character("Blue lizard",who_color = "#2759b8")

define config.default_music_volume = 0.8
define config.default_sfx_volume = 0.5
define config.default_voice_volume = 0.5
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')


default bag_menu = 1
default jane_inv = Inventory("Zalt")
default jane_inv_E = Inventory("E_Zalt")
default jane_inv_M = Inventory("M_Zalt")
default jane_inv_K = Inventory("K_Zalt")
default jane_equipment = M_Equipment("Equip_Zalt")

default Time.days = 1
default Time.hours = 6
default Time.mins = 30
default _dismiss_pause = False


default res = u"Attack"
default Zalt.str = 0
default Zalt.agi = 0
default Zalt.int = 0
default Zalt.end = 0
default Zalt.cha = 0
default Zalt.cor = 0

default Zalt.maxhp = 50
default Zalt.maxmp = 20
default Zalt.maxlust = 100
default Zalt.hp = Zalt.maxhp
default Zalt.mp = Zalt.maxmp
default Zalt.lust = 10

default Zalt.CRIT = 5
default Zalt.ATK = 15
default Zalt.DEF = 5
default Zalt.MATK = 15
default Battle.dodge = 0
default Zalt.drop = 30


default Zalt.lv = 1
default Zalt.maxlv = 15

default Zalt.exp = 0
default Zalt.maxexp = 250
default Zalt.points = 0

default Zalt.points1 = 0
default Zalt.perk_point = 0
default Zalt.sex = 0

default Zalt.Dungeon_unlock = False
default Zalt.Dungeon_leave = False

default Zalt.A_exp = 0
default Zalt.A_lv = 0
default Zalt.A_exp_lv = 1
default Zalt.AP = 0




default Battle.skill = False
default Battle.item = False
default Battle.flirt = False
default Battle.holyf = False
default Battle.holyfcd = 0
default Battle.S_knight = 0

default Zalt.public = True
default Zalt.dungeon = False




default Items.watch = 0
default Items.pbag = 0
default Items.pbag_n = 0
default Items.em = 0
default Items.accessories_quest = 0
default Items.mossb = 0


default Zalt.items = 1
default Items.key1 = False
default Items.sword = True
default Items.clothes = True
default Items.nude = False


default Items.rope = 0
default Items.torch = 0
default Items.pickaxe = 0
default Items.thread = 0
default Items.slime = 0
default Items.bullfur = 0
default Items.stone = 0
default Items.stick = 0
default Items.ectoplasm = 0
default Items.ironore = 0
default Items.lizardscale = 0
default Items.moss = 0

default Items.edit1 = 0

default Items.Murphy_Hand = 0
default Items.weapon = 0



default coin = Item("Coin", "The coins that are commonly used in many places.", "images/items/coins.png", 1,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"),note="Money,money.")
default hp_potion = Item("HP potion", "A small bottle of red potion, can restore 60 HP.", "images/items/hp_potion.png", 45,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default mp_potion = Item("MP potion", "A small bottle of blue potion, can restore 50 MP.", "images/items/mp_potion.png", 45,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default jerky = Item("Jerky", "A small piece of dried jerky, easy to be preserved, can restore 60 HP.\n(Can't be used in battle)", "images/items/jerky.png", 20,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default beer = Item("Beer", "A cup of plain ale, be careful, don't drink too much, can restore 60 MP.\n(Can't be used in battle)", "images/items/beer.png", 30,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,0,60,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default rum = Item("Rum", "A bottle of Fire rum, be careful, don't drink too much, can restore 80 MP.\n(Can't be used in battle)", "images/items/rum.png", 50,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,0,80,30,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default soul_solvent = Item("Corrupted Soul Solvent", "A vial of some kind of solution, it can completely restore HP and MP, but it will corrupt the user's soul.", "images/items/soul_solvent.png", 50,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,5,0,0,0,Zalt.maxhp,Zalt.maxmp,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default raspberry = Item("Raspberry", "A ripe, juicy raspberry. HP+5", "images/items/raspberry.png",0,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default mixed_green_salad = Item("Mixed green salad", "A healthy bowl of vegetables to get the appetite started. can restore 120 MP.\n(Can't be used in battle)", "images/items/salad.png", 0,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,0,120,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default roasted_potatoes = Item("Roasted potatoes", "Cooked to perfection by blasting potatoes with high heat strong enough to melt a blade, can restore 100 HP.(Can't be used in battle)", "images/items/rpotato.png", 0,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default jam_oatmeal_bread = Item("Jam oatmeal bread", "A beautiful loaf of bread with a jar of sweet jam, can restore 150 HP.\n(Can't be used in battle)", "images/items/jam_bread.png", 0,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default grilled_fish_skewer = Item("Grilled fish skewer", "A piece of fish grilled over a slow fire, can restore 90 MP.\n(Can't be used in battle)", "images/items/grilled_fish_skewer.png", 0,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,0,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default jerky_p = Item("Jerky", "Modified recipe by Parif. Compared to the original this one is tastier and more chewy, can restore \n80 HP and 10 MP. (Can't be used in battle)", "images/items/jerky_p.png", 21,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,80,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default h_coffee = Item("Coffee", "A cup of grinded coffee beans topped with Parif's artwork made from milk foam, can restore 80 MP.\n(Can't be used in battle)", "images/items/coffee.png", 0,True, 1, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,0,80,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


default sword = Item("Sword", "My sword, my father made it for me. \nATK +10", "images/items/sword.png", 0,False, 2,Show("inventory_popup", message="You wave the sword around wildly but nothing happens."),statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0])
default loincloth = Item("Loincloth", "My clothes \nDEF +5", "images/items/loincloth.png", 0, False,3,Show("inventory_popup", message="You wave the sword around wildly but nothing happens."),statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0])

default pocket_watch = Item("Pocket watch", "I can determine the specific time through this.\nMaxHP +5 MaxMP +10", "images/items/pocket_watch.png", 100,True, 5, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,5,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
default Roushk_bracelet = Item("Roushk’s bracelet", "A gift from Roushk the traveller from another world.\nEND + 1 ,CRIT + 5%", "images/items/bracelet.png", 300,True, 5, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,1,0,0,20,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0])
default Moss_bracelet = Item("Moss bracelet", "A bracelet made by Chet. It imitates the colour of moss to give it its lustrous look.\nDEF + 3", "images/items/moss_bracelet.png", 300,True, 5, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0])
default kid_book = Item("Storybook", "A storybook that looks like it was written for children. It has many drawings inside.\nCHA + 1", "images/items/kid_book.png", 0,True, 5, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0])
default bread_ring = Item("Leopard signet ring", "A ring which bears the symbol of a leopard family.\nATK + 3", "images/items/bread_ring.png", 0,True, 5, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0])
default murphy_hand = Item("Murphy’s Hand", "{size=-2}Fragments of an ancient demon.\nBy praying to it one can gain great power, but it will also gradually corrupt the user.{/size}\n{size=-4}(ATK +10, MATK +10, DEF +3. also COR +2 per battle.){/size}", "images/items/hand_bones.png", 0,True, 5, act=Show("inventory_popup", message="This item is only used in crafting"),statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,10,3,10,0,0,0,0,0,0,0,0,0,0])


default place = Item("", "", "images/items/placeholder.png",True, 4, act=Show("inventory_popup", message="This item is only used in crafting"), statsChange=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], note="You can't use it.")

default iron_ore = Item("Iron ore", "A chunk of iron, it can be fashioned into other items.", "images/items/ironore.png", 30,True, 6, note="If I can find the tools, I can refine it myself. I am proud of being the son of a blacksmith.")
default lizard_scale = Item("Lizard scale", "Pieces of scales from a lizard. It feels rough to the touch.", "images/items/lizardscale.png", 60,True, 6, note="Fortunately, it does not grow in reverse.")
default ectoplasm = Item("Ectoplasm", "You’re not sure what this does, but it feels slimy to touch.", "images/items/ectoplasm.png", 30,True, 6, note="The ashes of the..... ghost?")
default torch = Item("Torch", "Light up the darkness with a torch. Useful in dungeons.", "images/items/torch.png", 80,True, 6, note="Torches that can burn all day.")
default rope = Item("Rope", "A rope for climbing, it’s strong enough to support even the heaviest of bulls.", "images/items/rope.png", 60,True, 6, note="A reliable partner, should be able to come in handy.")
default slime_jewel = Item("Slime jewel", "A jewel dropped from slimes.", "images/items/slimejewel.png", 15,True, 6, note="Soft and slippery.")
default bull_fur = Item("Bull fur", "A tuft of fur from the bulls.", "images/items/bullfur.png", 40,True, 6, note="It smells like bulls.")
default stick = Item("Stick", "A stick, collect enough and you can make a fire.", "images/items/stick.png", 0,True, 6, note="It can be used to make a fire. I am glad that dad taught me how to make a fire before.")
default rock = Item("Rock", "A rock, collect enough and you can make a fire.", "images/items/stone.png", 0,True, 6, note="If it is flatter, I can use it to play 'stone skipping'.")
default moss = Item("Moss", "Moss that can be found on the bodies of gargoyles.", "images/items/moss.png", 100,True, 6, note="It will glow in the dark, maybe I can use it as a lantern after I go home?")
default blood_crystals = Item("Blood crystals", "Named because of the bloodshot color, it can be fashioned into other items.", "images/items/blood_crystals.png", 80,True, 6, note="This is precious material,I didn't expect i could see it here.")
default katos_horn = Item("Katos's horn", "A horn that occasionally sparks with lightning.", "images/items/katos_horn.png", 300,True, 6, note="Be careful, there is still electricity flashing on the horn.")
default lava_stone = Item("Lava stone", "A refined ore from the underground city, it contains the power of flames.", "images/items/lava_stone.png", 300,True, 6, note="The bell has rung...what?")

default seaweed = Item("Seaweed", "A piece of seaweed. Its taste reminds people of the ocean.", "images/items/seaweed.png", 5,True, 6, note="Maybe I should call this 'riverweed'.")
default worm_bait = Item("Worm bait", "an earthworm dug out from the soil, it can be used as bait.", "images/items/worm_bait.png", 5,True, 6, note="Squirming, squirming.")
default shiitake = Item("Shiitake", "A popular mushroom from a foreign kingdom. Some grill it and eat it with soy sauce.", "images/items/shiitake.png", 5,True, 6, note="Can eat.")
default toadstool = Item("Toadstool", "It’s bright red colour serves as a warning to others to not consume it. In large doses this mushroom can kill.", "images/items/toadstool.png", 5,True, 6, note="Can eat...?")
default lemon = Item("Lemon", "A sour fruit, but some people eat it with sugar as a dessert.", "images/items/lemon.png", 5,True, 6, note="I wonder howl, I wonder...what?")
default carrot = Item("Carrot", "Carrots, delicious on their own or when it's cooked.", "images/items/carrot.png", 5,True, 6, note="Collecting seven kinds of vegetables can realize your wish, funny.")
default potato = Item("Potato", "The humble potato, it’s a staple food in many kingdoms.", "images/items/potato.png", 5,True, 6, note="It seems to have begun to sprout.")
default cabbage = Item("Cabbage", "A fresh crisp cabbage, refreshing on a warm day.", "images/items/cabbage.png", 5,True, 6, note="Sweet!")
default tomato = Item("Tomato", "The plump round tomato bursting with sweet and sour juices.", "images/items/tomato.png", 5,True, 6, note="From heaven, harmful to little cute skull dragon.")
default coffee_beans = Item("Coffee beans", "A newly introduced ingredient to this part of the world, many are unaware of its aromatic goodness.", "images/items/coffee_beans.png", 45,True, 6, note="It says '100% made in 'hell'")
default grass_carp = Item("Grass carp", "It’s a grass carp, don’t feed it to herbivores.", "images/items/grass_carp.png", 5,True, 6, note="The most common fish, it really likes my tail.")
default morata_fish = Item("Morata fish", "The delicious meat of the morata fish is the key ingredient of the tavern jerky.", "images/items/morata_fish.png", 30,True, 6, note="Uncommon fish, my tail doesn't like it.")
default red_jam = Item("Red jam", "Raspberry jam, a nice condiment that can go with different dishes.", "images/items/red_jam.png", 30,True, 6, note="It's too sweet! I don't want to eat it directly.")
default oat_flour = Item("Oat flour", "The most common coarse oat flour.", "images/items/oat_flour.png", 30,True, 6, note="The staple food of herbivores, not really my type.")





default mining_permit = Item("Mining permit", "A permit that allows the user to mine a certain number of times in the bull village.", "images/items/permit.png", 0,True, 7, act=Show("inventory_popup", message="This item is only used in crafting"), note="This permit allows {u}[name]{/u}, to mine once a day in the bull village’s mountain area.\n\nShould he exceed the number of times mining is permitted,\n\n{u}[name]{/u} and all subsequent generations that follow him will forever be banned from entering the bull village. ")
default Mysterious_note_1 = Item("Mysterious note 1", "A note,found in a book in the temple.", "images/items/noteA.png", 0,True, 7, act=Show("inventory_popup", message="This item is only used in crafting"), note="{i}In the beginning there was only One.\n\nAn almighty and all power being that could shape the world how it saw fit, and destroy everything with a snap of its fingers.\n\nIt knew not its purpose for existence, and for thousands of years was revered and feared by the mortals of the earth.\n\nAt times it would be a merciful god and grant the mortals bountiful harvests or grant them immeasurable strength in their wars.\n\nIf scorn it would smite their cities with famine and sickness.\n\nTo the immortal being they were all just his play things.\n\nBut there was one thing its god like powers could not comprehend or have, the love and bond of mortals.\n\nFor all the miracles it could conjure, the mortals would never see the being as one of them, it was forever alone.{/i}")
default Mysterious_note_2 = Item("Mysterious note 2", "A note,found in the waterfall area.", "images/items/noteB.png", 0,True, 7, act=Show("inventory_popup", message="This item is only used in crafting"), note="{i}News has been spreading around the town about shadows kidnapping people off the street in the dead of night.\n\nIt’s gotten to the point that no one dares to be out when the sun goes down.\n\nThe king has made me his private inquisitor to investigate this strange case.\n\nA task I will carry out diligently.\n\nI swear upon the Divine Being of War’s blessing to bring this perpetrator to justice.\n\n- Razik Gallows{/i}")


default bullthread = Item("Ball of thread", "A ball of thread that can be used for sewing,made by 100% bull fur.", "images/items/bullthread.png", 300,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="It smells like BULLS!")
default pickaxe = Item("Pickaxe", "A tool to mine ores.", "images/items/pickaxe.png", 200,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Now I can use this to mine ore.")
default room_key = Item("Your room key", "The key to your room in the tavern. ", "images/items/room_key.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="My room key, my room is the right room on the second floor.")
default basement_key = Item("Basement key", "A key to open the door to the basement.", "images/items/basement_key.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="The basement key.")
default Box_of_wine = Item("Crate of rum ", "Snow’s crate of rum. Do not drink.", "images/items/box_wine.png", 300,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="I should give it to Snow.")
default Raco_flower = Item("Raco flower", "A toxic flower that also glows in the dark.", "images/items/white_flowers.png", 100,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="It smells good.")
default Fear_potion = Item("Fear potion", "A potion that can inflict fear onto specific people.", "images/items/fear_potion.png", 200,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Now I should go to see the tribe leader for the next step.")
default Skull_emblem = Item("Skull emblem", "A mysterious emblem of unknown origins or purpose.", "images/items/skull_emblem.png", 1000,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note=" Staring at this thing makes me shudder.")
default Soul_emblem = Item("Soul emblem", "A mysterious emblem of unknown origins or purpose.", "images/items/soul_emblem.png", 1000,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note=" Staring at this thing makes me feel sick.")
default Lizard_heart = Item("Bloody lizard heart", "The lizard spy’s heart, you swear you can feel it beating in your bag.", "images/items/bloody_heart.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note=".....")
default Lizard_dagger = Item("Bloody lizard dagger", "A dagger stained with the lizard spy’s blood.", "images/items/bloody_dagger.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="I should give this to Axel,but will it work?")

default potion_bag_1 = Item("Potion bag", "A bag to carry more potions safely. \nMax potion slots +2", "images/items/potion_bag.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Well,this is not a very fashionable style, but at least I can carry more potions.")

default selye_amulet = Item("Selye amulet", "An amulet that gives the wearer the appearance, ssssscent and feel of a lizard man. Even a ssssimpleton like you knows how to use it.", "images/items/selye_amulet.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Will thisssssssss thing really be useful?")
default real_bomb = Item("Bomb", "A small but powerful bomb developed by the bulls.", "images/items/real_bomb.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="I need to give it to the bull in the swamp.")
default fake_bomb = Item("Bomb?", "Is this a bomb? Maybe, but it sure looks like one.", "images/items/fake_bomb.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Achoo!")

default leaf_key = Item("Leaf key", "A key with a leaf design at the end.", "images/items/leaf_key.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="The leaf above seem to be alive,is this magic?")
default lion_key = Item("Lion key", "A key with a lion head at the end.", "images/items/lion_key.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="What a big kitty.")
default wing_key = Item("Wing key", "A key with a wing design at the end.", "images/items/wing_key.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="This key is very light.")
default jewel_key = Item("Jewel key", "A key with a beautiful jewel in the shape of a crown.", "images/items/jewel_key.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Is this real?")

default jester_badge = Item("Jester badge", "The wielder of this badge is the Royal Jester.", "images/items/jester_badge.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Jesters, they do get into trouble easily.")
default knight_badge = Item("Knight badge", "Knight Asmund’s Badge.", "images/items/knight_badge.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Faithful knight.")
default prince_badge = Item("Prince badge", "A badge that signifies the weilder is the son of the royal family.", "images/items/prince_badge.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="The holder can't become as majestic as the lion on the badge anymore.")
default queen_badge = Item("Queen badge", "A badge that signifies the weilder is the queen of the royal family.", "images/items/queen_badge.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="What will this use for?")
default sword_fragment = Item("Ethereal Blade piece", "A piece of the ghost king’s blade.\nIt emanates a dark energy full of the king’s resentment and ghostly power.", "images/items/sword_fragment.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="His anger will never go down.")

default sack = Item("Sack", "Burlap sacks big enough to carry hundreds of fruits.\nMight be heavy though.", "images/items/sack.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Thick, like Chet.")
default bevocr = Item("Bevocr", "Currency of the underground city, with a weird purple light.", "images/items/bevocr.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="It feels cold when touch.")
default ebb_necklace = Item("Ebb's necklace", "A necklace given by Ebb, pawn it to save Flo.", "images/items/ebb_necklace.png", 0,True, 6, act=Show("inventory_popup", message="This item is only used in crafting"), note="Salty, is this the feeling of the sea?")
default small_shovel = Item("Small shovel", "A small shovel that can be used to dig things.", "images/items/small_shovel.png", 5,True, 6, note="When you have to dig something up use a shovel.")
default fishing_rod = Item("Fishing Rod", "One of Snow’s fishing rods. Do not break it.", "images/items/fishing_rod.png", 500,True, 6, note="With it, I don’t need to use my tail anymore!")



default NPC.bullshop = 0
default NPC.lizardshop = 0
default NPC.anvil = 0
default NPC.anvil_1 = 0
default NPC.anvil_2 = 0
default NPC.anvil_need1_0 = 0
default NPC.anvil_need1_1 = 0
default NPC.anvil_need2_0 = 0
default NPC.anvil_need2_1 = 0
default NPC.anvil_name1 = 0
default NPC.anvil_name2 = 0
default NPC.weird_dream = 0

default NPC.cook_need1_0 = 0
default NPC.cook_need1_1 = 0
default NPC.cook_need2_0 = 0
default NPC.cook_need2_1 = 0
default NPC.cook_need3_0 = 0
default NPC.cook_need3_1 = 0
default NPC.cook_need4_0 = 0
default NPC.cook_need4_1 = 0

default Ludiko.meet = False

default Witer.meet = False
default Witer.bj = False
default Witer.cha = 0
default Witer.cha_p = 1
default Witer.sleep = 0
default Witer.squat = 0
default Witer.nipplesen = 1
default Witer.cowboy = 0
default Witer.bathsex = 0

default Snow.meet = False

default Hakan.meet = 0
default Hakan.quest = -1
default Hakan.sauna = 0
default Hakan.sauna_talk = 0

default Chet.win = 0
default Chet.cheat = False
default Chet.meet = False
default Chet.slime = 0
default Chet.bullfur = 0
default Chet.moreslime = 0
default Chet.tree = 0
default Chet.ectoplasm = 0
default Chet.past = 0
default Chet.snowsfood = 0


default Snow.hunt = True
default Snow.skullmonster = 0
default Snow.basement = 0
default Snow.fish = 0
default Snow.fishday = 0
default Snow.thanetavern = 0

default Meko.meet = 0
default Meko.lose = 0
default Meko.howdie = 0
default Meko.takeawalk = 0
default Meko.bathcomment = 0

default Nauxus.kiss = 1
default Nauxus.meet = 0
default Nauxus.s = 0
default Nauxus.artwork = 0
default Nauxus.artwork_p = 0
default Nauxus.talktree = 0

default Thane.join = 0
default Thane.meet = 0
default Thane.quest = 0
default Thane.mountain = 0
default Thane.temple = 0
default Thane.help = 0
default Thane.movein = 0
default Thane.talktree = 0

default Axel.meet = 0
default Axel.s = 0
default Axel.bullkid = 0
default Axel.talktree = 0

default Selye.meet = 0
default Selye.lizardask = 0
default Selye.past = 0

default Ebb.meet = 0
default Ebb.kidnap = 0
default Ebb.hang = 0
default Ebb.room = 1
default Ebb.cry = 999999
default Ebb.tavern = 0
default Ebb.necklace = 0


default Flo.meet = 0
default Flo.room = 0
default EF.witer = 0
default EF.hakan = 0
default EF.meko = 0





default Roushk.meet = 0
default Roushk.fight = 0
default Roushk.ke = 0
default Roushk.barn = 0
default Roushk.lizardtribe = 0
default Roushk.lizardtrio = 0
default Roushk.bulltribe = 0
default Roushk.snow = 0
default Roushk.hakan = 0
default Roushk.witer = 0
default Roushk.chet = 0
default Roushk.passoutguy = 0
default Roushk.thane = 0
default Roushk.meko = 0
default Roushk.endday = 0
default Roushk.party = 0
default Roushk.end = 0
default Roushk.snow_e = 0
default Roushk.hakan_e = 0
default Roushk.witer_e = 0
default Roushk.chet_e = 0
default Roushk.nauxus = 0


default Bread.meet = 0
default Bread.map = 0
default Bread.train = 0


default Parif.meet = 0
default Parif.cook_food = 0
default Parif.cook_helptime = 0
default Parif.witer_first = 0
default Parif.snow_first = 0
default Parif.hakan_first = 0
default Parif.chet_first = 0

default Parif.snow_fishrod = 0
default Parif.chet_shovel = 0

default Parif.cook_screen = "starter01"
default Parif.cook_info = 0
default Parif.cook_sjx = 0


default Parif.cook_Gsalad = 1
default Parif.cook_Rpotato = 1
default Parif.cook_Redjam = 1
default Parif.cook_Redjamcake = 1
default Parif.cook_Redjambread = 1
default Parif.cook_GFskewer = 1
default Parif.cook_Hcoffee = 0


default h1_name = u"Left Head"
default h2_name = u"Middle Head"
default h3_name = u"Right Head"

define h1 = Character("[h1_name]",who_color = "#8f524f")
define h2 = Character("[h2_name]",who_color = "#782723")
define h3 = Character("[h3_name]",who_color = "#520d0a")

default Hellhound_coffee_quest = 0
default Hellhound_energy = 0

default Map.river = 1
default Map.forest1 = 1
default Map.forest2 = 0
default Map.forest3 = 0
default Map.bulltribe = 0
default Map.roll = 1
default Map.boss1 = 1
default Map.bull1 = 1
default Map.crossroad = 0
default Map.lizard = 0
default Map.swamp = 0
default Map.bullforest = 0
default Map.mountain = 0
default Map.deepswamp = 0

default Map.lakecabin = 0
default Map.cave = 0

default Map.m1 = 0
default Map.m2 = 0
default Map.m3 = 0
default Map.m4 = 0
default Map.m5 = 0
default Map.m6 = 0
default Map.m7 = 0
default Map.m8 = 0
default Map.m9 = 0
default Map.m10 = 0

default Map.temple = 0
default Map.paintingroom = 0
default Map.first_world_touch = 0
default Map.first_world = 0

default Map.t1 = 0
default Map.t2 = 0
default Map.t3 = 0
default Map.t4 = 0
default Map.t5 = 0
default Map.t6 = 0
default Map.t7 = 0
default Map.t8 = 0
default Map.t9 = 0
default Map.t10 = 0
default Map.spring = 100
default Map.lakebank = 0


default Map.ca1 = 0
default Map.ca2 = 0
default Map.ca3 = 0
default Map.ca4 = 0
default Map.ca5 = 0
default Map.ca6 = 0
default Map.ca7 = 0
default Map.ca8 = 0
default Map.ca9 = 0
default Map.ca10 = 0
default Map.ca11 = 0
default Map.ca12 = 0
default Map.ca13 = 0
default Map.ca14 = 0
default Map.ca15 = 0
default Map.ca16 = 0
default Map.ca17 = 0
default Map.ca18 = 0
default Map.ca19 = 0
default Map.ca20 = 0
default Map.ca3garg = False
default Map.ca18garg0 = False
default Map.ca18garg = 0
default Map.ca8bull = 0

default Map.cak0 = 0
default Map.cak1 = 0
default Map.cak2 = 0
default Map.caj0 = 0
default Map.caj1 = 0
default Map.caj2 = 0
default Map.caj3 = 0
default Map.caj3g = 0


default Map.bt0 = 0
default Map.bt1 = 1
default Map.bt2 = 0
default Map.bt3 = 0
default Map.bt4 = 0
default Map.bt4bell = 0
default Map.bt5 = 0
default Map.bt6 = 0
default Map.bt7 = 0
default Map.bt8 = 0

default Map.castle_0 = 0
default Map.castle_1 = 0
default Map.castle_2 = 1
default Map.castle_3 = 0
default Map.castle_4 = 0
default Map.castle_4key = 0
default Map.castle_5 = 0
default Map.castle_6 = 0
default Map.castle_7 = 0
default Map.castle_8 = 0
default Map.castle_9 = 0
default Map.castle_10 = 0
default Map.castle_11 = 0
default Map.castle_12 = 0
default Map.castle_13 = 0
default Map.castle_14 = 0
default Map.castle_14key = 0
default Map.castle_15 = 0
default Map.castle_16 = 0
default Map.castle_17 = 0
default Map.castle_18 = 0
default Map.castle_19 = 0
default Map.castle_20 = 0
default Map.castle_21 = 0
default Map.castle_22 = 0
default Map.castle_22key = 0
default Map.castle_23 = 0
default Map.castle_24 = 0
default Map.castle_25 = 0
default Map.castle_26 = 0
default Map.castle_26key = 0
default Map.castle_27 = 0
default Map.castle_28 = 0
default Map.castle_28key = 0
default Map.castle_29 = 0
default Map.castle_30 = 0
default Map.castle_31 = 0
default Map.castle_32 = 0
default Map.castle_32key = 0
default Map.castle_33 = 0
default Map.castle_34 = 0
default Map.castle_35 = 0
default Map.castle_36 = 0
default Map.castle_37 = 0
default Map.castle_38 = 0
default Map.castle_39 = 0
default Map.castle_40 = 0
default Map.castle_41 = 0
default Map.castle_42 = 0
default Map.castle_43 = 0
default Map.castle_44 = 0
default Map.castle_ghost = 0
default Map.castle_king = 0

default Map.castle_prison_1 = 0
default Map.castle_prison_2 = 0
default Map.castle_prison_3 = 0
default Map.castle_prison_4 = 0
default Map.castle_prison_5 = 0
default Map.castle_prison_6 = 0
default Map.castle_prison_7 = 0

default Map.undercity_here = False
default Map.undercity_1 = 0
default Map.undercity_2 = 0
default Map.undercity_3 = 0
default Map.undercity_4 = 0
default Map.undercity_5 = 0
default Map.undercity_6 = 0
default Map.undercity_7 = 0
default Map.undercity_8 = 0
default Map.undercity_9 = 0
default Map.undercity_10 = 0
default Map.undercity_11 = 0
default Map.undercity_12 = 0
default Map.undercity_13 = 0
default Map.undercity_14 = 0
default Map.undercity_15 = 0
default Map.undercity_16 = 0
default Map.undercity_17 = 0

default Map.hellhound_meet = 0


default Map.undercity_auc_day = 99999
default Map.undercity_auc_day0 = 99999
default Map.undercity_auc_start = 0

default Map.undercity_worktime_time = 99999
default Map.undercity_worktime_check = False
default Map.undercity_worktime_bnous = False
default Map.undercity_worktime_earn = 0
default Map.undercity_worktime_sp = 1
default Map.undercity_worktime_maxsp = 1

default Map.undercity_auc_item_0 = 0
default Map.undercity_auc_item_1 = 0
default Map.undercity_auc_item_2 = 0
default Map.undercity_auc_item_3 = 0
default Map.undercity_auc_item_4 = 0
default Map.undercity_auc_item_5 = 1

default Map.undercity_auc_price_0 = 9999
default Map.undercity_auc_price_1 = 9999
default Map.undercity_auc_price_2 = 9999
default Map.undercity_auc_price_3 = 9999
default Map.undercity_auc_price_4 = 9999
default Map.undercity_auc_price_5 = 100

default Map.undercity_auc_round = 9999
default Map.undercity_auc_round_small = 9999
default Map.undercity_auc_bid_check = False
default Map.undercity_auc_bid1 = 9999
default Map.undercity_auc_bid2 = 9999
default Map.undercity_auc_giveup = False

default Map.undercity_pawn_pickaxe = 0
default Map.undercity_pawn_jester = 0
default Map.undercity_pawn_knight = 0
default Map.undercity_pawn_prince = 0
default Map.undercity_pawn_ethereal = 0
default Map.undercity_pawn_Skull = 0
default Map.undercity_pawn_necklace = 0

default Map.Cavetorch = 1
default Map.sproom = 0

default Map.bathroom_0 = 0
default Map.bathroom = 0
default Map.bathroom_openday = 0
default Map.first_bath = 0
default Map.free_bathday = 0

default Map.bathroom_ebbfirst = 0
default Map.bathroom_flofirst = 0

default Map.ore = 0

default Map.yourroom = 0


default Map.basement = 0


default Map.good_battle = False
default Map.f1_mushroom = 0
default Map.f1_carrot = 0
default Map.f2_mushroom = 0
default Map.f2_potato = 0
default Map.f3_mushroom = 0
default Map.f3_berry = 0
default Map.f4_carrot = 0
default Map.f4_potato = 0
default Map.f5_tomato = 0
default Map.f5_mushroom = 0
default Map.f6_lemon = 0
default Map.f6_cabbage = 0



default Foe.slime = False
default Foe.bullw = False
default Foe.bullwin = False
default Foe.ghostwin = False
default Foe.ghost_type = 0
default Foe.ghostappear = False
default Foe.ghostforest = 0
default Foe.lizardwin = False
default Foe.bulllick = False

default Foe.bullab = 0
default Foe.slimet = 0
default Foe.spydie = 0
default Foe.spylie = 0
default Foe.bullcamp = 0
default Foe.lizardcamp = 0

default name = u"Eyvind"
default sex = False
default Time.event1 = 9999
default Time.event2 = 9999
default Time.lizard = 9999
default Time.lizardgo = 9999
default Time.bull = 9999
default Time.aaxel = 9999
default Time.anauxus = 9999
default Time.athane = 9999
default Time.bullkid = 9999
default Time.nauxusart = 9999
default Time.bomb = 9999


default toscrossld.ld_lizard_ending = ""

default Quest.campw = 0
default Quest.campw1 = 0
default Quest.campb = 0
default Quest.campl = 0
default Quest.campt = 0
default Quest.campc = 0
default Quest.camp_n = 0
default Quest.camp_a = 0

default Quest.bomb_end = 0
default Quest.bomb = 0
default Quest.bomba = 0
default Quest.bombn = 0
default Quest.bombt = 0
default Quest.bomb_lizard = 0
default Quest.bomb_bull = 0
default Quest.bomb_result = 0


default Time.festival_day = 99999
default Quest.fes_end = -1
default Quest.fes = 0
default Quest.fesa = 0
default Quest.fesn = 0
default Quest.fest = 0
default Quest.fes_lizard = 0
default Quest.fes_bull = 0
default Quest.fes_result = 0
default Quest.fes_snow = 0
default Quest.fes_witer = 0
default Quest.fes_hakan = 0
default Quest.fes_chet = 0
default Quest.fes_meko = 0


default persistent.CG_goo_lose = False
default persistent.CG_bull_lose = False
default persistent.CG_bull_winA = False
default persistent.CG_bull_winB = False
default persistent.CG_tree_lose = False
default persistent.CG_ghost_lose = False
default persistent.CG_gargoyle_lose = False
default persistent.CG_gargoyle_win = False

default persistent.CG_eyvind_solo = False
default persistent.CG_eyvind_sell = False
default persistent.CG_lizard_win = False
default persistent.CG_lizard_lose = False
default persistent.CG_bull_lick = False

default persistent.CG_witer_bj = False
default persistent.CG_hakan_ride = False
default persistent.CG_roushk_top = False
default persistent.CG_roushk_bottom = False
default persistent.CG_hakan_sixnine = False
default persistent.CG_witer_cowboy = False

default input_code = ""






label main_menu:

    $ renpy.music.play("<loop 5.3194>music/tavern_menu_base.ogg","music", loop=True)

    jump main_menu_screen


label start:
    stop music
    $ renpy.music.play("<loop 5.3194>music/tavern_menu_base.ogg","Chan1", loop=True)
    $ renpy.music.play("<loop 5.3194>music/tavern_menu_drums.ogg","Chan2", loop=True)
    $ renpy.music.play("<loop 5.3194>music/tavern_menu_organ.ogg","Chan3", loop=True)
    $ renpy.music.set_volume(0, 0, channel = "Chan1")
    $ renpy.music.set_volume(0, 0, channel = "Chan2")
    $ renpy.music.set_volume(0, 0, channel = "Chan3")
    label enter_name:
        python:
            name = renpy.input(_("Введи свое имя здесь.{p}{size=-5}(Стандартное имя 'Эйвинд'.){/size}"))

            name = name.strip() or __("Eyvind")

        if name == u"Libra":
            "No."
            jump enter_name
        elif name == u"Caro":
            "*Skull dragon noise*"
            "{b}No."
            jump enter_name
        elif name == u"Witer":
            w "Why would you do this."
            jump enter_name
        elif name == u"Chet":
            c "You need to buy my copyright first!"
            jump enter_name
        elif name == u"Hakan":
            h "Ha! Don't even think about it."
            jump enter_name
        elif name == u"Selye":
            se "Interessssssting."
            jump enter_name
        elif True:
            pass

        "Ваше имя [name]"
        menu:
            "Да" if True:
                pass
            "Нет" if True:
                jump enter_name


    "Выберите свою статистику"
    "Это определит, что вы можете и не можете делать в игре."
    "Если вы не знаете, что такое статистика..."
    "Пожалуйста, проверьте раздел \"О программе\" в главном меню игры."
    if renpy.variant("pc"):
        "Вы также можете нажать кнопку \"H\", чтобы скрыть текстовое поле."
        "Это будет полезно, когда вы захотите посмотреть горячие сцены."
        "И \" Tab \" поможет вам пропустить диалог, который вы читали раньше."
    elif True:
        pass
    $ renpy.music.set_volume(1, 1, channel = "Chan2")

    call screen statspick

    if _return == 'start_1':
        jump start_1




label start_1:
    $ jane_equipment.weapon[0] = sword
    $ jane_equipment.armor[0] = loincloth
    $ jane_equipment.place[0] = place
    $ jane_inv_K.take(room_key)
    $ Zalt.hp = 20

    $ jane_inv.take(coin,100)
    $ jane_inv.take(jerky,2)

    $ Zalt.maxhp = 80+(Zalt.end-3)*20
    $ Zalt.maxmp = (Zalt.int-3)*10+20
    $ Zalt.CRIT = Zalt.CRIT+ (Zalt.agi-3)*2
    $ Zalt.ATK = Zalt.ATK+ (Zalt.agi-3)*1 +(Zalt.str-3)*3
    $ Zalt.MATK = Zalt.MATK+ (Zalt.int-3)*3
    $ Zalt.DEF = 5
    $ Battle.dodge = Zalt.agi*2 -5
    $ Zalt.hp = Zalt.maxhp
    $ Zalt.mp = Zalt.maxmp

    $ Zalt.maxlust = 100
    $ Zalt.lust = 10
    scene start_1
    with vslow_dissolve



    $ renpy.music.set_volume(1, 5, channel = "Chan3")
    $ config.rollback_enabled = True
    "Твое имя [name]."
    "Прошел целый год с тех пор, как ты покинул деревню в своем приключении."
    "Это традиция племени Потерянного Копья,{p}для каждого мужчины в возрасте 23 лет. "
    "Тебе интересно, как там все дома, особенно твой отец."
    "Как бы ты хотел, чтобы случилось что-то экстраординарное,{p}ознаменовавшее конец вашего путешествия, чтобы вы могли вернуться домой к своему народу."

    "Несколько дней спустя...{w}...."
    $ renpy.music.set_volume(0, 15, channel = "Chan2")
    $ renpy.music.set_volume(0, 5, channel = "Chan3")
    scene start_2
    with vslow_dissolve

    "Ваши уши навостряются при звуке темных облаков, катящихся над головой. "
    "За спиной видна приближающаяся стена дождя. "

    "На твоем лице появляется хмурое выражение, и ты пытаешься убежать от грохочущих шагов падающего дождя., {p}но ты быстро промок в воде."


    "...."
    $ renpy.music.set_volume(0.2, 0, channel = "music")
    play music "music/rainy.mp3" fadeout 1
    scene black
    with dissolve
    "Нет ни одного места, где можно укрыться. "
    $ renpy.music.play("<loop 5.2978>music/intro_rain1.ogg","Chan1", loop=True,fadein=5)
    $ renpy.music.play("<loop 5.2978>music/intro_rain2.ogg","Chan2", loop=True)
    $ renpy.music.set_volume(1, 5, channel = "Chan1")
    $ renpy.music.set_volume(0, 0, channel = "Chan2")
    "Слабые тени деревьев и кустарников попадают в поле зрения, когда вы идете вперед по мутной дороге."
    "Каждый шаг становится тяжелее и труднее сделать, когда грязь окутывает ноги."
    e 1 "Я вообще на дороге? "
    "....."
    "......"
    $ renpy.music.set_volume(1, 5, channel = "Chan2")
    define q_dissolve = Dissolve(0.5)

    define slow_dissolve = Dissolve(1.5)
    define vslow_dissolve = Dissolve(2.5)
    define vvslow_dissolve = Dissolve(4)
    scene start_3
    with vslow_dissolve

    "Тропинка впереди расплывается серым пятном, а дождь все льет и льет."
    "Ты продолжаешь идти, пока не замечаешь теплое желтое свечение, идущее со стороны тропинки. "
    "Его свечение…"
    "это кажется таким знакомым…"
    $ renpy.music.set_volume(0, 8, channel = "Chan1")
    $ renpy.music.set_volume(0, 4, channel = "Chan2")
    stop Chan1
    stop Chan2
    "...."
    pause .5
    stop music fadeout 1
    play sound "music/door.mp3"
    stop music fadeout 1
    scene black
    with vslow_dissolve
    "....."
    "......"
    "Грубый голос" "Эй!"
    "......"
    "Грубый голос" "ЭЙ! ВСТАВАЙ!"
    e 6 "А? Ч-где? Что?"
    "Этот голос мне так знаком. "
    "Это просто у тебя в голове, имя этого голоса."
    "Голова тяжелая, как будто кто-то ударил тебя камнем. "
    "Требуется некоторое время, чтобы ваше видение сфокусировалось."
    "Повернув голову влево, вы сильно ударяетесь мордой о ножку барного стула. "
    scene tavern 1
    with vslow_dissolve
    $ renpy.music.set_volume(0.8, 10, channel = "Chan1")
    $ renpy.music.set_volume(0, 0, channel = "Chan2")
    $ renpy.music.set_volume(0, 0, channel = "Chan3")
    $ renpy.music.play("<loop 5.3194>music/tavern_menu_base.ogg","Chan1", loop=True,fadein=0.1)
    $ renpy.music.play("<loop 5.3194>music/tavern_menu_drums.ogg","Chan2", loop=True)
    $ renpy.music.play("<loop 5.3194>music/tavern_menu_accordion.ogg","Chan3", loop=True)
    "....."
    "......"
    "- Дружище, поднимай свою задницу с пола."
    "- Если ты хочешь спать здесь, это тебе дорого обойдется."
    e 5 " Ладно, ладно. Просто дай мне секунду! "
    show snow stand at center with fade
    "Вы видите крепкого серого волка с кружкой в одной руке и крюком в другой."
    "Две белые косы, образовавшиеся из его бороды, спускались до середины груди. "
    "Его голубые глаза почти светятся, когда он смотрит на тебя. "
    $ renpy.music.set_volume(1, 10, channel = "Chan3")

    e 5 "Подожди...отец?"

    "Я не могу поверить в то, что вижу. Мой отец, Сноу, он прямо передо мной."
    "В пабе раздается взрыв смеха."
    "Клиент А" "Вау, Сноу! Мальчик назвал тебя папой!"
    "Клиент Б" "Старый Сноу! Я даже не знал, что у тебя есть ребенок!"
    hide snow stand
    show snow laugh1 at center with q_dissolve
    s "Отец? Парень, это падение, должно быть, вышибло тебе мозги."
    s "Я никогда в жизни тебя не видел."
    e 5 "Если ты пытаешься шутить, это не смешно. Отец, что ты здесь делаешь?"
    hide snow laugh1
    show snow stand at center with q_dissolve
    s "Я не твой отец! Меня зовут Сноу."
    s "Я бармен и владелец этого заведения."
    s "Или ты что-нибудь закажешь, или я вышвырну тебя обратно в лес."

    e 6 "Да, я знаю, что ты-Снег. "
    e 6 "Отец...папа. Что ты говоришь о том, чтобы быть барменом?"
    hide snow stand
    show snow happy1 at center with q_dissolve
    s "Хватит этого отцовского дерьма. Я буквально только сегодня тебя увидел"
    hide snow happy1
    show snow angrys at center with q_dissolve
    s "Если ты из тех, кто называет любого случайного незнакомца своим отцом, то у тебя есть проблемы, мальчик!"

    "Человек перед тобой выглядит и говорит как твой отец."
    "Но он, кажется, не лжет. "
    "Что ты собираешься делать?"

    menu:
        "Настаивать на том, что он твой отец." if True:

            e 2 "Послушайте, я не знаю, как еще мне убедить вас. "
            e 2 "Ты выглядишь как мой отец, говоришь как мой отец и пахнешь как мой отец. "
            e 1 "Пойдем со мной в деревню, мы найдем кого-нибудь, кто посмотрит на тебя и выяснит, что случилось."
            s "Я никуда с тобой не пойду. Пацан."
            s " Отдохни уже. Ты мешаешь другим клиентам."
            hide snow angrys
            "Он показывает на твою спину. "
            "Ты поворачиваешься и видишь спину красного дракона."
            "Мускулистый зеленый аллигатор, одетый в коричневую набедренную повязку, подходит к столу и ставит стакан."
            "Что-то движется справа, и вы видите зевающую гиену, сидящую под шпандрелем лестницы."
            "Гиена улыбается тебе, и вы оба обмениваетесь жестами."
            show snow angrys1 at center with q_dissolve
            "Повернувшись к бармену, вы видите, что он скрестил руки на груди и бросает на вас недовольный взгляд."
            e 6 "Father please, you need to remember I’m your son."
            e 6 "You made me this sword. You-"
            hide snow angrys1
            show snow happy at center with q_dissolve
            s "Oh,crap.."
            "He raises a hand and cuts you off."
            s "You know what? Sure, I’m your father"
            s "Now be a good boy and buy something already!"
            hide snow happy
            show snow happy1 at center with q_dissolve
            "The older wolf’s voice catches the attention of the others in the tavern."
            "All eyes are on you two now."
            e 1 "...."
            e 1 "....?!"
            "You gulp and reach for your pouch, but it’s not there."
            e 5 "Where’s my coin pouch?"
            s "Well here’s a life lesson for you, “son”."
            s "No money, no service."
            e 5 "...."
            hide snow happy
            show snow stand1 at center with q_dissolve
            s "Since, I’m feeling very 'fatherly'."

            $ renpy.music.set_volume(0, 5, channel = "Chan1")
            $ renpy.music.set_volume(1, 5, channel = "Chan2")

            s "I’ll give you a few pieces of coin if you head out and take down a few monsters."
            e 1 "Monsters? What kind?"
            hide snow stand1
            show snow happy1 at center with q_dissolve
            s "Just a few small ones, nothing to worry about."
            s "Hakan over there’s the one that usually deals with them so they leave the tavern alone."
            s "Hey, Hakan! Tell him what happened!"
            show hakan stand at left with q_dissolve
            "Hakan" "...."
            "The red dragon scowls back at Snow and turns back to his drink."
            hide hakan stand with q_dissolve
            s "Long story short he sprained his knee the last time out."
            s "So why don’t you get out there and put that sword of yours to good use."
            e 1 "Fine, but this isn’t over father."
            s "Well maybe those monsters can knock some sense into you before you come back. I’m not your father, kid."
            s "If you survive we can continue our “father-son” time."
            hide snow stand1 with moveoutright
            "Your ears droop, and you walk away from the bar."
            scene black with dissolve
            stop music fadeout 1
            "It looks like your “father” is fully committed to not knowing who you are."
            "Best to come back later to talk to him."
            play sound "music/door.mp3"


            jump battle_game_1
        "Play along with the bartender" if True:


            e 2 " I’m sorry. I… must have you confused with someone I know."
            hide snow angrys
            show snow happy at center with q_dissolve
            s " No problem stranger."
            s "Can I get you a drink or maybe you’re looking for a place to stay?"
            e 1 "Where is here actually? I can’t remember much except for a –"
            hide snow happy
            show snow stand1 at center with q_dissolve
            s "A yellow light. Most of the travelers that come here say the same thing."
            s "Well, this is the Tavern of Spear, we provide meals and a warm bed for any who can afford it."
            "You search your belt for your coin pouch but turn up empty"
            e 5 "I could have sworn I came with money, but it’s missing."
            s "No surprise, you came staggering in like an undead."
            s "I was considering having Hakan and Witer over there toss you back out if you so much as scratched the floorboards"
            "Snow points to the people behind you."
            hide snow stand1 with q_dissolve
            "A green muscular alligator in a loincloth serves a grumpy looking red dragon a mug of beer."
            "You notice the leather shoulder pads the dragon wears are covered in deep scratches."
            "The dragon eyes you menacingly from the corner of his eye. "
            "You try to avoid his gaze and turn back only to nearly bump into Snow’s face. He inches closer and whispers into your ear."
            show snow happy1 at center with q_dissolve
            s "Don’t worry, he’s much nicer once you get to know him.Anyway——"
            "The bartender pulls himself back and points at you."

            $ renpy.music.set_volume(0, 5, channel = "Chan1")
            $ renpy.music.set_volume(1, 5, channel = "Chan2")
            s "I have a proposition. Since you are short on coins I have a small job you can take."
            e 1 "A job? "
            e 7 "Hmm, I am kind of hungry. What do you need?"
            s "The monster around the forest have been moving closer to the tavern than I prefer."
            s "Hakan’s been out of action since his last encounter with them. "
            s "So, I need you to kill a few of these creatures so the rest of them will understand to stay away."
            s "I’ll pay you some coin for your help."
            e 1 "Sounds simple enough. Alright, I’ll take the job."
            hide snow happy1
            show snow laugh at center with q_dissolve
            s "Good on you stranger."
            s "Once you're done, then we can have a proper introduction, and get you settled for the next few days."
            e 1 "'Next few days?'"
            hide snow laugh with moveoutright
            scene black with dissolve
            stop music fadeout 1
            play sound "music/door.mp3"
            "Snow seems pretty confident that you will be here for a while."
            "What is he not telling? Best to come back later to find out."
            jump battle_game_1



screen map:

    imagemap:
        idle 'imagemap ground'
        hover 'imagemap hover'





        vbox:
            xalign 0.24 ypos 0.46
            if Hakan.quest != 7 and Time.hours >=4 and Time.hours <=21:
                imagebutton:
                    idle "NPC/hakan01.png"
                    hover "NPC/hakan02.png"

                    action Return("Hakan_meet")
            else:
                pass



        vbox:
            xalign 0.18 ypos 0.6
            imagebutton:
                idle "NPC/npc101.png"
                hover "NPC/npc102.png"

                action Return("Drunk_meet")




        vbox:
            xalign 0.65 ypos 0.4
            if Time.hours >=6 and Time.hours <=21:
                if Witer.squat <= 1 and Time.days > 9 and Time.hours <13:
                    pass
                else:
                    imagebutton:
                        idle "NPC/witer01.png"
                        hover "NPC/witer02.png"

                        action Return("Witer")
            else:
                pass

        vbox:
            xalign 0.68 ypos 0.36
            if Parif.meet == 1:
                imagebutton:
                    idle "UI/t_kitchen01.png"
                    hover "UI/t_kitchen02.png"

                    action Jump("Parif_talk")
            elif Parif.meet == 2:
                imagebutton:
                    idle "UI/t_kitchen00.png"
                    hover "UI/t_kitchen02.png"

                    action Jump("Parif_talk")
            else:
                pass



        vbox:
            xalign 0.77 ypos 0.51
            if Time.hours >=6 and Time.hours <=20:
                imagebutton:
                    idle "NPC/chat01.png"
                    hover "NPC/chat02.png"

                    action Return("Chet")
            else:
                pass


        vbox:
            xalign 0.52 ypos 0.4
            if Snow.hunt == False and Time.hours >=4 and Time.hours <=20:
                if Snow.fish == -1 and Time.days == Snow.fishday:
                    pass
                else:
                    imagebutton:
                        idle "NPC/snow01.png"
                        hover "NPC/snow02.png"

                        action Return("Snow_meet")
            else:
                pass





        vbox:
            xalign 0.415 ypos 0.424
            if Thane.movein == 2 and Time.hours >=6 and Time.hours <=21 and Quest.fes <1:
                imagebutton:
                    idle "NPC/thane_t01.png"
                    hover "NPC/thane_t02.png"
                    action Return("Thane_t")
            else:
                pass

        vbox:
            xalign 0.42 ypos 0.37
            if Map.basement == 1:
                imagebutton:
                    idle "UI/basement01.png"
                    hover "UI/basement02.png"

                    action Return("basement")
            elif Map.basement == 2:
                imagebutton:
                    idle "UI/basement03.png"
                    hover "UI/basement01.png"

                    action Return("basement")
            else:
                pass


        hotspot (1201, 182, 111, 153) action Return("room1")

        hotspot (586, 950, 561, 117) action Return("outdoor")
        hotspot (1175, 88, 46, 65) action Return("c14")


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



screen stats:
    zorder 1
    button:
        xalign 1.0 yalign 0.0
        add "UI/stats03.png"
        action Hide("tylos")
    vbox:
        xalign 0.01
        yalign 0.01
        if Items.watch ==2:
            text "Day:[Time.days] / [Time.hours]:[Time.mins]"
        if Zalt.dungeon == True:
            text ""
            text "A-EXP: [Zalt.A_exp] / 100"
            text "A-LV: < [Zalt.A_lv] >"
        if Map.undercity_here == True and Map.undercity_auc_start == 1:
            text ""
            text "SP: [Map.undercity_worktime_sp] / [Map.undercity_worktime_maxsp]"
    vbox:
        spacing 18
        text "STR:[Zalt.str]"
        text "AGI:[Zalt.agi]"
        text "INT:[Zalt.int]"
        text "END:[Zalt.end]"
        text "CHA:[Zalt.cha]"
        text "COR:[Zalt.cor]"
        text "LUST:[Zalt.lust]/[Zalt.maxlust]"

        area (1633, 400, 193, 492)
    vbox:
        spacing 22
        text "HP:[Zalt.hp]/[Zalt.maxhp]"
        text "MP:[Zalt.mp]/[Zalt.maxmp]"
        area (1384, 927, 198, 111)
    vbox:
        spacing 22
        text "Lv:  < [Zalt.lv] >"
        text "EXP:[Zalt.exp]/[Zalt.maxexp]"
        area (1140, 927, 198, 111)
    vbox:
        if Zalt.AP != 0:
            spacing 22
            text "AP:  < [Zalt.AP] >"
            area (1000, 927, 198, 111)
    frame:
        xalign 0.89 ypos 0.84
        imagebutton:
            idle "UI/stats01.png"
            hover "UI/stats02.png"

            action Hide("stats")



label map0:
    stop music
    play sound "music/door.mp3"
    scene black with dissolve
    scene tavern 1 with vslow_dissolve



    if Zalt.tut_win == True:
        show snow stand at center with dissolve
        s "You’re back. By the way things sounded from here it must have been a big slime."
        e 1 "It wasn’t a slime. I’m not sure what it was. "
        e 1 "Some kind of massive beast with a skull for a head.."
        hide snow stand
        show snow stand1 at center with q_dissolve
        s "Huh, that’s something new. At least you dealt with it."
        s "We’ll worry more about that later."
    elif True:
        show snow angrys at center with dissolve
        s "...It's weird,the monster has never been so close to the tavern."
        hide snow angrys
        show snow stand1 at center with q_dissolve
        s "Anything broken?"
        e 7 "No… thanks fa- Snow."
        s "I’m sorry I kind of put your life at risk there."
        s "Wasn’t expecting such a powerful enemy to appear."


    s "Anyways, here’s your reward."
    "[name] gains 200 coins."
    hide snow stand1
    show snow happy at center with q_dissolve
    s "Now, you’re just in luck."
    s "You have enough to rent a room for a night."
    e 1 "That will be more than enough. "
    e 1 "The weather was mostly foggy, it should be gone by tomorrow."
    hide snow happy
    "Snow bangs the table with his good hand and laughs loudly.{p}You sense the eyes of the others in the tavern falling on your shoulder."
    show snow laugh at center with q_dissolve
    s "That’s hilarious,do you really think you can leave the forest by tomorrow?"
    hide snow laugh
    show snow laugh1 at center with q_dissolve
    s "Boy, that fog is no ordinary fog."
    e 5 "....What do you mean?"
    "Snow points to the barstool and you take a seat."
    hide snow laugh1
    "Your left leg twitches and you wonder what bad news your father’s doppelganger is about to say."
    "He pulls out a mug and starts to clean it with a clean rag attached to his hook hand."
    show snow happy at center with q_dissolve
    s "The fog is like a living being."
    s "It decides on its own when to open up the exit out of this forest."
    s "Sometimes, it may be a few days, a few weeks, or a few months. "
    s "There’s no telling when really."
    e 5 "That’s insane. "
    e 5 "Even if it were true why can’t you just cut through the trees? {p}Eventually you’ll reach the main road."
    hide snow happy
    show snow stand1 at center with q_dissolve
    s "You think nobody’s ever tried that?"
    s "The last person to try it went hacking for four days and ended up back here as the hired muscle. "
    "He motions to the person he is talking about with a wave of his snout."
    "You see he means Hakan, now passed out on the table with half a dozen mugs on his table."
    e 5 "This can’t be, I can’t be here for months! I have people waiting for me back home. "
    hide snow stand1
    show snow happy1 at center with q_dissolve
    s "I don’t know what else to tell you boy other than just help around here."
    s "Keep yourself well fed and comfortable then go home when the fog clears."
    e 1 "You are way too calm about this."
    e 1 "How are you not freaking out more about this?"
    e 6 "More importantly, why are you still here?"
    "Snow smiles at you, but it feels like he isn’t looking at you but more through you."
    hide snow happy1
    show snow stand at center with q_dissolve
    s "As long as there are lost or abandoned souls."
    s "The tavern and I will always be here to keep them company."
    e 3 "…That doesn’t answer anything."
    "Your statement falls on deaf ears."
    "Snow puts aside the mug and pulls a key from below the counter. "
    s "Eh, maybe I’m getting too tired to make any sense."
    s "I don’t have the vigor of a young wolf like you do."
    hide snow stand
    show snow happy at center with q_dissolve
    s "Here, your room is the third door on the right. "
    "He places the key in front of you."
    hide snow happy
    show snow happy1 at center with q_dissolve
    s "If you feel hungry well too bad. Kitchen’s closed for the day, and Witer,"
    s "Witer,get your scaly ass over here!"
    "You see the green alligator from before is sitting on his own with a piece of paper and pencil near the door."
    show snow happy1 at left with move
    show witer stand at right with moveinright
    "He puts down his belongings and makes his way towards the counter. "
    hide snow happy1
    show snow stand1 at left with q_dissolve
    s "This here’s Witer, the tavern’s waiter."
    w "Hi, nice to meet a new face."
    "The alligator smiles warmly and reaches out for your hand to shake it."
    "His muscles were not just for show, you can feel his strong grip on the palm of your hand."
    e 1 "Nice to meet you. I’m [name]."
    hide snow stand1
    show snow happy at left with q_dissolve
    s "If you need to order anything you go through him"
    s "And if you have any more questions to ask about the place you can consult him too."
    s "Too much talking is exhausting, I rather do things with my hands."
    hide snow happy with moveoutleft
    show witer stand at center with move
    "Witer continues to shake your hand until you let go first."
    "He blushes as he seems to notice what he was doing."
    "While Snow leaves the counter Witer bends closer, his face is inches away from yours."
    w "Just knock on my door if you need anything else."
    "He walks away from you but your eyes trail onto him, transfixed by the motions of his hips and supple bottom."
    hide witer stand with moveoutright
    "Witer disappears into the top of the stairs and you decide to follow suit."
    "Hakan is still knocked out on his table."
    "You consider waking him, but his loud snore tells you to just leave him be."
    "Best to retire for the night."
    play sound "music/door.mp3"
    scene black with vslow_dissolve

    "....{w}...{w}..."

    $ Zalt.hp = Zalt.maxhp
    $ Zalt.mp = Zalt.maxmp

    "It’s a new day, maybe."
    "There’s no real indication of time around this tavern."
    "No clocks, no sun dials, nothing. "
    "You’re not even sure how long you’ve been asleep."
    scene room 1 with dissolve
    "Every inch of your body feels glued to the bed. "
    "Blinking at the ceiling a few times you roll about trying to fall asleep again, but to no avail."
    "You get up and get dressed before heading down to the bar."
    play sound "music/door.mp3"
    scene black with vslow_dissolve
    scene tavern 1 with dissolve
    "As you walk down the stairs you notice that Snow is not behind the counter. "
    "Hakan's sitting at the same table as last night but he’s having a hearty breakfast of eggs."
    show witer stand at center with dissolve
    "You walk over to Witer standing next to a hyena sitting underneath the stairs."
    w "Morning, handsome."
    e 1 "Morning Witer."
    e 1 "Where’s Snow?"
    w "He’s out doing the weekly ingredient hunt."
    w "So, I’m in charge of the tavern until he comes back. "
    "The smell of scrambled eggs wafting in the air stirs up your stomach. It growls loudly."
    e 3 "I’m hungrier than I expected."
    w "Well, you’re just in luck. What will you have?"
    "The meal nourishes you with energy to go about your day. "
    $ renpy.music.set_pause(True, channel='Snow')
    $ renpy.music.set_pause(True, channel='Hakan')
    $ renpy.music.set_pause(True, channel='Witer')
    $ renpy.music.set_pause(True, channel='Chet')
    $ renpy.music.set_pause(True, channel='Thane')
    play music [ "<silence 1.0>", "music/tavern.ogg" ]
    play Snow "music/char_snow.ogg"
    play Hakan "music/char_hakan.ogg"
    play Witer "music/char_witer.ogg"
    play Chet "music/char_chet.ogg"
    play Thane "music/thane.ogg"
    hide witer stand
    jump map1

label map1:
    if Time.hours >= 24:
        $ Time.hours = Time.hours - 24
        $ Time.days = Time.days + 1
    if Time.mins >= 60:
        $ Time.mins = Time.mins -60
        $ Time.hours = Time.hours +1
    $ Zalt.public = True

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
    $ renpy.music.set_pause(False, channel='music')
    $ renpy.music.set_volume(1, 5.5, channel = "music")

    if Ebb.kidnap == 4 and Ebb.tavern == 0:
        jump saveflo_end
    if Hakan.quest == 7 and  Time.days >= Time.event1 +3:
        $ Hakan.quest = 8
    if Roushk.meet == 0 and (Axel.bullkid == 1 or Nauxus.artwork == 1) and Hakan.quest != 7 and Hakan.quest != 8 and Time.event1 != Time.days and Meko.meet >= 1:
        $ Roushk.meet = 2
        jump Roushk_meet
    if Roushk.party == 1:
        scene tavern 1 with dissolve
        "The moment you exit your room, you are met with the smiles of all the tavern mates preparing for the party."
        show snow stand1 at center with dissolve
        s "Hey, [name]."
        s "Good, you’re still here, just want you to know the party should be ready by evening."
        s "Don’t miss it."
        e 6 "Thanks Snow, need any help setting up?"
        s "Nah, we have it under control over here."
        s "Go one and have your day. "
        e 1 "Right. I’ll just go see Roushk."
        hide snow stand1 at center with dissolve
        $ Roushk.party = 2
    if (Roushk.party == 2 or Roushk.party == 3) and Time.days == Roushk.endday and Time.hours >=18 and Time.hours <=22:
        jump Roushk_meko_battle_end
    if (Roushk.party == 2 or Roushk.party == 3):
        if Time.days == Roushk.endday and Time.hours >=23:
            jump Roushk_meko_battle_end2
        elif Time.days == Roushk.endday+1 and Time.hours >=0 and Time.hours <6:
            jump Roushk_meko_battle_end2
        elif Time.days >= Roushk.endday +1 and Time.hours >=6:
            jump Roushk_goodbye3

    if Roushk.nauxus == 2 and Quest.bomb == 0:
        jump Snow_twoletters
    if Map.boss1 == 2:
        scene tavern 1 with dissolve
        if Snow.skullmonster != 0 or Time.days >= 6:
            "You return to the tavern and rush over to report what you found to Snow."
            e 5 "Snow, I’m back from the slime investigation."
            s "Well you sure took your sweet time. "
            s "I can’t even remember when I sent you out to do that."
            s "Really kid, you need to work on your priorities."
            s "You’re lucky it wasn’t that big of a deal or someone here could have gotten hurt."
            e 9 "Well… I wouldn't really say it wasn’t a big deal."
            "You fake a chuckle but Snow is unamused."
            "He walks out of the bar and calls everyone together."
            "You all gather around "
            s "Listen up, [name] is going tell us what he found about the weird slimes I encountered before."
            show snow stand1 at left with dissolve
            show witer stand at right with dissolve
        elif True:
            "Everyone’s gathered by the bar as you enter."
            s "There he is."
            w "You’re back, we were so worried."
            c "Aha, my business might still survive."
            h "You were slow…"
            show witer stand at center with moveinright
            show witer stand:
                zoom 1.0
                linear 0.3 zoom 1.2
                linear 0.3 zoom 1.0
            "Witer rushes out and hugs you tightly."
            "Your heart feels at ease knowing that they were concerned about you. "
            show snow stand1 at left with moveinleft
            show witer stand at right with moveoutright
            "Snow walks over and pulls Witer back."
            s "So,how’d it went?"
        e 1 "I found the demon creature while exploring the woods."
        e 1 "I think it’s the cause of the slimes acting weird, because after taking it down most of them disappeared."
        hide snow stand1
        show snow angry1 at left with dissolve
        s "You went to fight the demon alone?"
        s "What is wrong with you? You could have gotten hurt or worse!"
        e 5 "I didn’t have a choice!"
        e 5 "It sprang up on me, I didn’t have time to run and get help."
        hide snow angry1
        show snow stand at left with dissolve
        s "You’re lucky you escaped with your tail intact."
        s "Still, best let Witer check you anyways for injuries."
        e 1 "That can wait. When the monster was taken out it dropped this."
        e 1 "It’s some kind of an emblem. Do you recognize it?"
        "You place the emblem on the bar."
        "All three of them lean close to examine it."
        s "Never seen it before. Not even sure what emblem it is supposed to be a piece of."
        c "Same here."
        w "What about you, Hakan? Know anything about it?"
        "Hakan shakes his head."
        e 1 "Well I also found this at the same place."
        e 1 "A note by someone with the initials P.D."
        e 1 "He claimed that to be looking for pieces of an emblem that will free him from the forest."
        s "Let me see that."
        "Snow snatches the piece of paper from your hand and looks through{p}its content with the rest standing beside him trying to read it."
        hide snow stand
        show snow happy1 at left with dissolve
        s "P.D… could it be Pierce Dagon?"
        s "Haven’t heard that name in a long time"
        c "Blegh, I never liked him."
        c "He came in all high and mighty about his clan’s divine connection to the Grand Creator!"
        "Chet rolls his eyes and does waving motions with his hands in the air."
        w "I never heard of this Pierce guy before."
        c "You and Hakan weren't here back then."
        c "He was this pompous looking antelope dressed in black robes with an eye shaped necklace as big as a fist."
        c "Came in claiming that his clan’s Grand Creator had summoned him to the tavern to vanquish the evil within. "
        hide snow happy1
        show snow happy at left with dissolve
        s "He wouldn’t listen to a thing I said."
        s "After one night he woke up exclaiming that his Grand Creator spoke to him in a dream about how to destroy the fog."
        s "The intensity in his eyes was just disturbing."
        s "He grabbed Chet off the ground and tossed him aside to take his axe and headed out, never to be seen again."
        h "You had an axe?"
        c "Emphasis on had, I never saw it again after that."
        s "We both assumed he just left the forest when the fog cleared, or the monsters took him."
        e 1 "So, this emblem thing. It’s…"
        hide snow happy
        show snow stand1 at left with dissolve
        w "Damn it, I was hoping for something magical to happen."
        h "Keep wishing green butt. Now, get me some beer."
        hide witer stand with dissolve
        show snow happy at center with moveinright
        s "Before I forget, here’s your reward."
        "[name] gains 200 coins."
        $ jane_inv.take(coin,200)
        s "And as I said,you can keep your room key."
        s "I decided to let you have your room for free for the rest of your stay here."
        s "Consider it part of the payment to help protect this place."
        s "Come see me later for some new work."
        s "For now, you earned your rest."
        hide snow stand1 with dissolve
        "Chet grabs the emblem and puts it into your hand."
        c "You know what, I’m feeling a bit sentimental."
        c "If you have the time and you find these emblems just grab them for me."
        c "I want some kind of compensation for my lost axe."
        e 6 "I didn’t take you for the type to collect things you can’t sell."
        c "I have my moments. Bring it back to me as you go."
        $ Map.boss1 = 3
        jump map1
    if Witer.squat == 0 and Time.days > 9 and Time.hours >=4 and Time.hours <=20:
        scene tavern 1 with dissolve

        show snow stand1 at center with dissolve
        $ renpy.music.set_volume(0, 0.5, channel = "music")
        pause 0.5
        $ renpy.music.set_pause(True, channel='music')

        $ renpy.music.set_pause(False, channel='Snow')
        $ renpy.music.set_volume(1, 4, channel = "Snow")
        "Snow talks to you as you enter the tavern."
        if Time.hours >= 6 and Time.hours <= 17:
            s "Hey, [name]. I’ve got a message for you from Witer."
            e 1 "A message? Why can’t he just talk to me about it."
            s "Not my business to pry, kid."
            s "He just said to meet him in the barn while he’s cleaning the place up."
            e 1 "Alright, thanks Snow."
            "Snow grunts affirmatively."
            $ Witer.squat = 1
            jump map1
        elif True:
            s "Hey kid, I got something to tell you."
            e 1 "You need me for something?"
            s "Not me, Witer. He wants to see you in the barn in the morning."
            e 1 "Can't he just tell me now? He's literally right there."
            "You turn to the alligator who's sneaking glances at Chet from behind his board."
            s "Well he said it's private."
            s "If you want to know more you go see him in the barn in the from 8 a.m. to noon."
            s "Just don't get in the way of his cleaning."
            e 1 "Ok, thanks for letting me know."
            $ Witer.squat = 1
            jump map1



    if Map.bathroom_openday <= Time.days and Map.bathroom_0 == 3:

        $ Map.bathroom_0 = 4
        if Map.bathroom == "EbbFlo":
            scene tavern 1 with dissolve
            "The drinking hall is dead quiet, absent are its usual occupants."
            e 1 "Where is everyone?"
            "The familiar creak of the trap door opening then calls your attention."
            "Hakan steps out first followed by Witer. "
            "The alligator looks none too pleased with the sleepy dragon."
            h "Ugh, quit staring daggers at me."
            h "Aren’t I paying with my hangover already?"
            "Witer saunters to Hakan’s side with his hands on his hips. "
            "A deep furrow forms in the space between his eyebrows if he had any."
            w "You still reek of beer. Why do you always have to drink until you blackout?"
            m "Indeed Hakan, moderation is key."
            "The sight of the ghostly horn resting on Hakan’s right shoulder surprises you."
            "Then you remember no one should be able to see him."
            h "Hey, I don’t tell you how much vegetables you can plant around the tavern."
            w "That’s completely different!"
            m "I fear this is escalating into something bigger."
            "You cough loudly to get the two reptiles’ attention."
            "They turn to you."
            show hakan stand at left with dissolve
            show witer stand at right with dissolve
            h "Oh hey, Fuzzbutt."
            w "[name], I was just about to get you."
            e 1 "Hey there you two. Trouble in paradise?"
            w "No! It’s just Hakan being his usual stubborn self, again. Hmph!"
            "Witer crosses his arms in a huff."
            "Hakan just yawns and acts as though he didn’t hear anything."
            w "Where is everyone else?"
            w "They’re waiting outside of the bath house."
            w "The grand opening ceremony is supposed to start around now."
            w "That’s why I had to drag this guy over here out of bed."
            hide witer stand at right with dissolve
            m "And I had to come along, it’s been ages since I’ve been to any opening festivities. "
            "He points with a wave of his thumb at Hakan."
            h "Well Snow didn’t tell you to talk my ears off in the process."
            h "Come on, we in a hurry or what?"
            hide hakan stand at left with dissolve
            "Hakan walks over to the entrance with Meko still on his shoulders."
            e 1 "Mmm…"
            "You decide not to say anything about it, and go along with the group to the ceremony."
        elif True:
            scene tavern 1 with dissolve
            "As you walk down the stairs to the drinking hall, you notice that no one is around, minus Hakan’s drinking buddy who’s passed out as usual."
            "From the foot of the stairs you see a note on the bar."
            "You pick up the piece of paper."
            "'[name], we all went to the bath house for the opening ceremony. Meet us there.'"
            "..."

        play sound "music/foot1.ogg"
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

        jump Snow_bathroom_questline
    elif True:

        show screen days
        window hide None
        call screen map with dissolve


    if _return == 'university':
        play music "music/rainy.mp3"
        call screen C_Snow with dissolve
        return
    if _return == 'Drunk_meet':
        scene tavern 1
        if Roushk.passoutguy == 1 and Roushk.barn ==1:
            show roushk stand at center with dissolve
            ro "Is this guy ok?"
            ro "Every time I see him, he's just asleep here."
            e 9 "Well."
            e 1 "Do you really want to know?"
            e 13 "To be honest..."
            e 7 "ι©ζ„­ζ†Ύε¨‘ε‰ζ†Ύε¨‘θΉ­η―ƒιƒγƒ§ζ³­ι°η†·εηΌζη�΅ι‚ζ¥€ε½ζµ ο½‡η²―ιΆε©ξ—“ιοΏ½."
            e 6 "åØ‘č¹­ēÆé¸ć§ę³­éˇ°ē†·å."
            e 9 "йђ©ж„­ж†ѕеЁ‘еЏ‰ж†ѕеЁ‘и№­зЇѓж¶”з†·о›§ж¶”з†»о›¦йЏѓгѓ§жі­йЋ°з†·еџЊзј€иЇІгЃ‰йЌ е‚њеЈ’жї®ж—Ђ."
            e 10 "ç«çƒ­ä¹Ÿå¦‚ä¹Ÿè¦è±†è…å¹²å¤§èŒƒç”˜è¿ªé«˜é£å‰²è±†è…å¹²è±†è…å¹²å¤§èŒƒç”˜è¿ªè­¦æ–¹ç»è¿‡è­¦æ–¹."
            "It seems Roushk is very surprised to hear this."
            ro "....I find it best not to think about it."
            $ Roushk.passoutguy = 2
            hide roushk stand with dissolve
        elif True:
            e 1 "The guy is still passed out."
            e 6 "I don't think I can wake him up."
        jump map1
        return
    if _return == 'Ludiko_meet':
        jump Ludiko_meet
        return
    if _return == 'Hakan_meet':
        jump Hakan_meet
        return
    if _return == 'Snow_meet':
        jump Snow_meet
        return
    if _return == 'room1':
        jump Room1_check
        return
    if _return == 'Witer':
        jump Witer_meet
        return
    if _return == 'Witer_meal':
        jump Witer_meal
        return
    if _return == 'Chet':
        jump Chet
        return
    if _return == 'key':
        scene tavern 1
        show chet sad at center
        c "...."
        e 1 "It's Snow's key,I shouldn't touch it."
        jump map1
        return
    if _return == 'outdoor':
        scene tavern 1
        play sound "music/door.mp3"
        jump T_outdoor
        return
    if _return == 'basement':
        scene tavern 1
        jump T_basement
        return
    if _return == 'c14':
        scene black
        jump c_code
        return
    if _return == "Thane_t":
        scene black
        jump Thane_tavern_talk
    return
label nude_no:
    scene black
    e 7 "....No,I don't think it's a good idea to take my clothes off in public."
    play music [ "<silence 1.0>", "music/tavern.ogg" ] fadeout 1
    jump map1


screen days:
    if Time.mins >0:
        vbox:
            xalign 0.01
            yalign 0.01
            if Items.watch ==2:
                text "Day:[Time.days] / [Time.hours]:[Time.mins]"
                if Map.undercity_here == True and Map.undercity_auc_start == 1:
                    text ""
                    text "SP: [Map.undercity_worktime_sp] / [Map.undercity_worktime_maxsp]"
            else:
                text ""
    else:
        vbox:
            xalign 0.01
            yalign 0.01
            if Items.watch ==2:
                text "Day:[Time.days] / [Time.hours]:00"
            else:
                text ""
label after_load:
    if Zalt.dungeon == False:
        $ config.rollback_enabled = True
    elif True:
        $ config.rollback_enabled = False
    if Zalt.maxlv != 15:
        $ Zalt.maxlv = 15
    if Map.boss1 >= 2 and Items.em == 0:
        $ Items.em = 1
    if Time.lizard == 9999 and Nauxus.meet == 6:
        $ Time.lizard = Time.days
    if Zalt.str +Zalt.agi +Zalt.int +Zalt.cha +Zalt.end >= 50:
        $ Zalt.hp = 0
    if Quest.bomb_end == 0 and Quest.bomb == 5 and Quest.bombt == 6 and Quest.fes_end == -1:
        $ Quest.fes_end = 0
        $ Time.festival_day = Time.days
    if Map.undercity_auc_start == 1:
        if Time.hours >= 6 and Time.hours <= 11:
            $ Map.undercity_worktime_time = "Morning"
        elif Time.hours >= 12 and Time.hours <= 17:
            $ Map.undercity_worktime_time = "Afternoon"
        elif Time.hours >= 18 and Time.hours <= 24:
            $ Map.undercity_worktime_time = "Night"
        elif True:
            $ Map.undercity_worktime_time = "Sleep"
    $ _dismiss_pause = False
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
