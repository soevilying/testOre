

init python:
    import renpy.store as store

    class Item(store.object):
        def __init__(self, name, desc, icon=False, value=0,canUse=False, type=0, act=Show("inventory_popup", message="Nothing happened!"), recipe=False,statsChange = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], note="Nothing happened!"):
            global cookbook
            self.name = name 
            self.desc = desc 
            self.icon = icon 
            self.value = value 
            self.canUse = canUse 
            self.act = act 
            self.type = type 
            self.recipe = recipe 
            self.statsChange = statsChange 
            self.note = note
            if recipe:
                cookbook.append(self)
                cookbook.sort(key=lambda i: i.name) 
        
        def change(self, name, desc=False, icon=False, value=False,canUse=False, type=False, act=False, recipe=False,statsChange = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]):
            self.name = name
            if desc:
                self.desc = desc
            if icon:
                self.icon = icon
            if value:
                self.value = value
            if canUse:
                self.canUse = canUse
            if type:
                self.type = type
            if act:
                self.act = act
            if recipe:
                self.recipe = recipe
            if statsChange:
                self.statsChange = statsChange

    class M_Equipment(store.object):
        def __init__(self, name):
            self.name = name
            self.weapon = [Null]
            self.armor = [Null]
            self.place = [Null]
            self.accessories = [[Null],[Null],[Null]]
            self.grid_view = True
        
        def equip(self, item):
            jane_inv_E.drop(item[0])
            changeStats(item[0].statsChange)
            if item[0].type == 2:
                if self.weapon[0] == Null:
                    self.weapon[0] = item[0]
                    return
                else:
                    jane_inv_E.take(self.weapon[0])
                    backStats(self.weapon[0].statsChange)
                    self.weapon[0] = item[0]
                    return
            if item[0].type == 3:
                if self.armor[0] == Null:
                    self.armor[0] = item[0]
                    return
                else:
                    jane_inv_E.take(self.armor[0])
                    backStats(self.armor[0].statsChange)
                    self.armor[0] = item[0]
                    return
            
            if item[0].type == 4:
                if self.place[0] == Null:
                    self.place[0] = item[0]
                    return
                else:
                    jane_inv_E.take(self.place[0])
                    backStats(self.place[0].statsChange)
                    self.place[0] = item[0]
                    return
            
            if item[0].type == 5:
                for num in range(0,3):
                    if(self.accessories[num][0] == Null):
                        self.accessories[num][0] = item[0]
                        return
                jane_inv_E.take(self.accessories[0][0])
                backStats(self.accessories[0][0].statsChange)
                self.accessories[0][0] = item[0]
                return
        
        def unequip(self, item):
            backStats(item[0].statsChange)
            if item[0].type == 2:
                jane_inv_E.take(item[0])
                self.weapon[0] = Null
                return
            if item[0].type == 3:
                jane_inv_E.take(item[0])
                self.armor[0] = Null
                return
            
            if item[0].type == 4:
                return
            
            if item[0].type == 5:
                for num in range(0,3):
                    if(self.accessories[num][0] == item[0]):
                        jane_inv_E.take(item[0])
                        self.accessories[num][0] = Null
                        return



    class Inventory(store.object):
        def __init__(self, name, money=0, barter=100):
            self.name = name
            self.money = money
            self.barter = barter 
            self.inv = []  
            self.sort_by = self.sort_name
            self.sort_order = True 
            self.grid_view = True
        
        def buy(self, item, price):
            self.deposit(price)
            self.take(item[0])
        
        def check(self, item):
            if self.qty(item):
                for i in self.inv:
                    if i[0] == item:
                        return self.inv.index(i) 
        
        def check_recipe(self, item): 
            checklist = list()
            for i in item.recipe:
                if self.qty(i[0]) >= i[1]:
                    checklist.append(True)
            if len(checklist) == len(item.recipe):
                return True
            else:
                return False
        
        def craft(self, item):
            for line in item.recipe:
                self.drop(line[0], line[1])
            self.take(item)
            message = "Crafted a %s!" % (item.name)
            renpy.show_screen("inventory_popup", message=message)
        
        def deposit(self, amount):
            self.money -= amount
        
        def drop(self, item, qty=1):
            if self.qty(item):
                item_location = self.check(item)
                if self.inv[item_location][1] > qty:
                    self.inv[item_location][1] -= qty
                else:
                    del self.inv[item_location]
        
        def qty(self, item):
            for i in self.inv:
                if i[0] == item:
                    return i[1] 
        
        def sell(self, item, price):
            self.withdraw(price)
            self.drop(item[0])
        def type_filter(self):
            return self == 1
        
        def sort_name(self):
            self.inv.sort(key=lambda i: i[0].name, reverse=self.sort_order)
        
        def sort_qty(self):
            self.inv.sort(key=lambda i: i[1], reverse=self.sort_order)
        
        def sort_value(self):
            self.inv.sort(key=lambda i: i[0].value, reverse=self.sort_order)
        
        def sort_type(self):
            self.inv.sort(key=lambda i: i[0].type, reverse=self.sort_order)
        
        def take(self, item, qty=1):
            if self.qty(item):
                item_location = self.check(item)
                self.inv[item_location][1] += qty
            else:
                self.inv.append([item,qty])
        
        def withdraw(self, amount):
            self.money += amount


    def calculate_price(item, buyer):
        if buyer:
            price = item[0].value * (buyer.barter * 0.01)
            return int(price)

    def money_transfer(depositor, withdrawer, amount):
        if depositor.money >= amount:
            depositor.deposit(amount)
            withdrawer.withdraw(amount)
        else:
            message = "Sorry, %s doesn't have %d!" % (buyer.name, amount)
            renpy.show_screen("inventory_popup", message=message)

    def trade(seller, buyer, item):
        seller.drop(item[0])
        buyer.take(item[0])

    def useItem(inv, item):
        changeStats(item[0].statsChange)
        inv.drop(item[0])

    def changeStats(statsChange):
        Zalt.str += statsChange[0];
        Zalt.agi += statsChange[1];
        Zalt.int += statsChange[2];
        Zalt.end += statsChange[3];
        Zalt.cha += statsChange[4];
        Zalt.cor += statsChange[5];
        
        Zalt.maxhp += statsChange[6];
        Zalt.maxmp += statsChange[7];
        Zalt.maxlust += statsChange[8];
        Zalt.hp += statsChange[9];
        Zalt.mp += statsChange[10];
        Zalt.lust += statsChange[11];
        
        Zalt.CRIT += statsChange[12];
        Zalt.ATK += statsChange[13];
        Zalt.DEF += statsChange[14];
        Zalt.MATK += statsChange[15];
        Battle.dodge += statsChange[16];
        Zalt.drop += statsChange[17];
        
        
        
        
        
        
        
        
        
        
        if Zalt.hp > Zalt.maxhp:
            Zalt.hp = Zalt.maxhp
        if Zalt.hp < 0:
            Zalt.hp = 0
        if Zalt.lust > Zalt.maxlust:
            Zalt.lust = Zalt.maxlust
        if Zalt.lust < 0:
            Zalt.lust = 0
        if Zalt.mp > Zalt.maxmp:
            Zalt.mp = Zalt.maxmp
        if Zalt.mp < 0:
            Zalt.mp = 0
        if Zalt.cor > 100:
            Zalt.CRIT = 100
        if Zalt.cor < 0:
            Zalt.CRIT = 0
        if Zalt.CRIT > 100:
            Zalt.CRIT = 100
        if Zalt.CRIT < 0:
            Zalt.CRIT = 0
        if Zalt.drop > 100:
            Zalt.drop = 100
        if Zalt.drop < 0:
            Zalt.drop = 0
        if Zalt.ATK <1:
            Zalt.ATK = 1
        if Zalt.MATK <1:
            Zalt.MATK = 1
        if Battle.dodge >100:
            Battle.dodge = 100
        if Battle.dodge <0:
            Battle.dodge =0


    def backStats(statsChange):
        Zalt.str -= statsChange[0];
        Zalt.agi -= statsChange[1];
        Zalt.int -= statsChange[2];
        Zalt.end -= statsChange[3];
        Zalt.cha -= statsChange[4];
        Zalt.cor -= statsChange[5];
        
        Zalt.maxhp -= statsChange[6];
        Zalt.maxmp -= statsChange[7];
        Zalt.maxlust -= statsChange[8];
        
        Zalt.hp -= statsChange[9];
        Zalt.mp -= statsChange[10];
        Zalt.lust -= statsChange[11];
        Zalt.CRIT -= statsChange[12];
        
        Zalt.ATK -= statsChange[13];
        Zalt.DEF -= statsChange[14];
        Zalt.MATK -= statsChange[15];
        
        Battle.dodge -= statsChange[16];
        Zalt.drop -= statsChange[17];
        
        if Zalt.hp > Zalt.maxhp:
            Zalt.hp = Zalt.maxhp
        if Zalt.hp < 0:
            Zalt.hp = 0
        if Zalt.lust > Zalt.maxlust:
            Zalt.lust = Zalt.maxlust
        if Zalt.lust < 0:
            Zalt.lust = 0
        if Zalt.mp > Zalt.maxmp:
            Zalt.mp = Zalt.maxmp
        if Zalt.mp < 0:
            Zalt.mp = 0
        if Zalt.cor > 100:
            Zalt.CRIT = 100
        if Zalt.cor < 0:
            Zalt.CRIT = 0
        if Zalt.CRIT > 100:
            Zalt.CRIT = 100
        if Zalt.CRIT < 0:
            Zalt.CRIT = 0
        if Zalt.drop > 100:
            Zalt.drop = 100
        if Zalt.drop < 0:
            Zalt.drop = 0
        if Zalt.ATK <1:
            Zalt.ATK = 1
        if Zalt.MATK <1:
            Zalt.MATK = 1
        if Battle.dodge >100:
            Battle.dodge = 100
        if Battle.dodge <0:
            Battle.dodge =0


    def swap(source, target, item):
        if item[0].type > 1 and item[0].type < 7:
            for each_element in target.inv:
                if each_element[0].type == item[0].type:
                    target.drop(each_element[0])
                    source.take(each_element[0])
            source.drop(item[0])
            target.take(item[0])

    def transaction(seller, buyer, item):
        price = calculate_price(item, buyer)
        if buyer.money >= price:
            seller.sell(item, price)
            buyer.buy(item, price)
        else:
            message = "Sorry, %s doesn't have enough money!" % (buyer.name)
            renpy.show_screen("inventory_popup", message=message)

    def equip(item):
        jane_equipment.equip(item)


    def unequip(item):
        jane_equipment.unequip(item)


    transfer_amount = 0



screen bag:
    add "UI/gallery_bg2.png"
    add "UI/gallery_bg0.png"
    button:
        xalign 1.0 yalign 0.0
        add "UI/Bag.png"
        action Hide("tylos")

    imagebutton:
        xalign 0.547 yalign 0.025
        idle "UI/bag_icon_1.png"
        hover "UI/bag_icon_1a.png"
        action Hide("inventory_screen"),Show("inventory_screen", first_inventory=jane_inv)
    imagebutton:
        xalign 0.547 yalign 0.125
        idle "UI/bag_icon_2.png"
        hover "UI/bag_icon_2a.png"
        action Hide("inventory_screen"),Show("inventory_screen", first_inventory=jane_inv_E)
    imagebutton:
        xalign 0.547 yalign 0.225
        idle "UI/bag_icon_3.png"
        hover "UI/bag_icon_3a.png"
        action Hide("inventory_screen"),Show("inventory_screen", first_inventory=jane_inv_M)
    imagebutton:
        xalign 0.547 yalign 0.315
        idle "UI/bag_icon_4.png"
        hover "UI/bag_icon_4a.png"
        action Hide("inventory_screen"),Show("inventory_screen", first_inventory=jane_inv_K)

    frame:
        xalign 0.97 ypos 0.84
        imagebutton:
            idle "UI/bag01.png"
            hover "UI/bag02.png"

            action Hide("bag"),Hide("inventory_screen"),Hide("EWinventory_screen"),Hide("EWinventory_view_new"),Hide("clothes_une"),Hide("clothes_1"),Hide("clothes_2"),Hide("beer"),Hide("jerky"),Hide("hp_potion"),Hide("mp_potion"),Hide("rum")


    grid 5 3:
        align (0.965,0.05)
        xysize (770,450)
        spacing 35
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"

    grid 2 2:
        align (0.4,0.55)
        xysize (770,450)
        spacing 35
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
        add "items/empty_bag.png"
    grid 1 1:
        align (0.538,0.619   )
        xysize (770,450)
        spacing 35
        add "items/empty_bag.png"

    add "images/items/eyvind.png" xalign 0.01 yalign 0.04
    imagebutton:
        xalign 0.547 yalign 0.435
        idle "UI/log_icon_1.png"
        hover "UI/log_icon_1a.png"
        action Notify("Coming soon.")


    vbox:
        xalign 0.38 yalign 0.025
        xminimum 220 xmaximum 220
        vbox:
            text "{b}[name]{/b} < Lv:[Zalt.lv] >" size 22 xalign 0.1
            null height 5
            text "HP" size 16
            hbox:
                bar:
                    xmaximum 130
                    value Zalt.hp
                    range Zalt.maxhp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5


                text "[Zalt.hp] / [Zalt.maxhp]" size 16
            text "MP" size 16
            hbox:

                bar:
                    xmaximum 130
                    value Zalt.mp
                    range Zalt.maxmp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None


                null width 5


                text " {color=#0080c0}[Zalt.mp] / [Zalt.maxmp]{/color}" size 16
            text "LUST" size 16
            hbox:

                bar:
                    xmaximum 130
                    value Zalt.lust
                    range Zalt.maxlust
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None


                null width 5


                text "[Zalt.lust] / [Zalt.maxlust]" size 16

    vbox:
        xalign 0.35 yalign 0.252
        spacing 2
        text "STR:{b} [Zalt.str]{/b}" size 22
        text "AGI:{b} [Zalt.agi]{/b}" size 22
        text "INT:{b} [Zalt.int]{/b}" size 22
        text "END:{b} [Zalt.end]{/b}" size 22
        text "CHA:{b} [Zalt.cha]{/b}" size 22

    vbox:
        xalign 0.43 yalign 0.252
        spacing 2
        text "Dodge:{b} [Battle.dodge]%{/b}" size 22
        text "CRIT:{b} [Zalt.CRIT]%{/b}" size 22
        text "ATK:{b} [Zalt.ATK]{/b}" size 22
        text "DEF:{b} [Zalt.DEF]{/b}" size 22
        text "MATK:{b} [Zalt.MATK]{/b}" size 22

    vbox:
        xalign 0.49 yalign 0.02
        xminimum 220 xmaximum 220
        text "EXP:[Zalt.exp]/[Zalt.maxexp]" size 22

screen tooltip(item=False, seller=false):
    if item:
        button:
            xalign 0.873 yalign 0.47
            add "UI/bag_info.png"
        text ("{size=+12}[item[0].name]{/size}") area (1138, 475, 737, 112)
        hbox:
            area (1136, 560, 748, 171)
            if seller:
                text ("[item[0].name]: [item[0].desc] \n{size=-5}(Sell Value: " + str(calculate_price(item, seller)) + "){/size}")
            else:
                text "[item[0].desc]\n{size=-5}(Value: [item[0].value]){/size}"

screen inventory_screen(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = False

    modal False tag menu
    hbox:
        spacing 35
    vbox:
        xalign 0.955 ypos 0.02
        if second_inventory:
            frame:
                style_group "invstyle"
                has hbox:
                    spacing 25
                vbox:
                    label first_inventory.name
                    if second_inventory:
                        use money(first_inventory, second_inventory, bank_mode)
                    use inventory_view(first_inventory, second_inventory, trade_mode)

                    textbutton "Close" action Hide("inventory_screen")
                vbox:
                    label second_inventory.name
                    use money(second_inventory, first_inventory, bank_mode)
                    use inventory_view(second_inventory, first_inventory, trade_mode)

                if crafting_screen:
                    use crafting(first_inventory)
        else:
            hbox:
                spacing 25
                vbox:

                    if second_inventory:
                        use money(first_inventory, second_inventory, bank_mode)
                    use inventory_view(first_inventory, second_inventory, trade_mode)
                    use sort_nav(first_inventory)

                if crafting_screen:
                    use crafting(first_inventory)




screen inventory_view(inventory, second_inventory=False, trade_mode=False):
    vbox:
        xalign 0.55 ypos 0.03



        style_group "invstyle"
        area (0, 0, 730, 450)
        vpgrid id ("vp"+inventory.name):
            draggable True
            mousewheel True
            xsize 770 ysize 460
            if inventory.grid_view:
                cols 5 spacing 55
            else:
                cols 1 spacing 40
            for item in inventory.inv:
                $ name = item[0].name
                $ desc = item[0].desc
                $ value = item[0].value
                $ qty = str(item[1])

                $ type = item[0].type
                hbox:
                    if item[0].icon:
                        $ icon = item[0].icon
                        $ hover_icon = im.Sepia(icon)

                        imagebutton:
                            idle LiveComposite((100,100), (0,0), icon, (0,0), Text(qty))
                            hover LiveComposite((100,100), (0,0), hover_icon, (0,0), Text(qty))
                            action (Hide("tooltip"),
                                If(not second_inventory and not trade_mode and item[0].canUse and item[0].type == 1,
                                    Confirm("Use " + item[0].name+"?\n"+item[0].desc, yes=Function(useItem,inventory,item), no=None, confirm_selected=False),
                                    If(not second_inventory and not trade_mode and item[0].canUse and item[0].type == 6,
                                        Notify(item[0].note),
                                        If(not second_inventory and not trade_mode and item[0].canUse and item[0].type == 7,
                                            Show("inventory_popup", message=item[0].note),
                                            If(not second_inventory and not trade_mode and item[0].type in [2,3,4,5],
                                                Function(equip,item),
                                                If(trade_mode,
                                                    Function(trade,inventory, second_inventory, item),
                                                    Function(transaction,inventory, second_inventory, item)
                                                )
                                            )
                                        )
                                    )
                                )
                            )


                            hovered Show("tooltip",item=item,seller=second_inventory)
                            unhovered Hide("tooltip")
                        if not inventory.grid_view:
                            vbox:
                                text name
                                if not trade_mode:
                                    text "List Value: [value]"
                                    if second_inventory:
                                        text ("Sell Value: " + str(calculate_price(item, second_inventory)) + ")")

                    else:
                        textbutton "[name] ([qty])" action (If(not second_inventory, item[0].act,(If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item))))) hovered Show("tooltip",item=item,seller=second_inventory) unhovered Hide("tooltip")
                        if not inventory.grid_view:
                            vbox:
                                text "List Value: [value]"
                                if not trade_mode and second_inventory:
                                    text "Sell Value: " + str(calculate_price(item, second_inventory)) + ")"


            if len(inventory.inv) == 0:
                add Null(height=100,width=100)

        vbar value YScrollValue("vp"+inventory.name)


screen money(inventory, second_inventory, bank_mode=False):
    hbox:
        style_group "invstyle"
        text "Money: [inventory.money]"
        if bank_mode and inventory.money:
            textbutton "Transfer" action Show("banking", depositor=inventory, withdrawer=second_inventory)

screen banking(depositor, withdrawer):
    modal False
    frame:
        style_group "invstyle"
        has vbox
        label "Money Transfer"
        text "Amount: [transfer_amount]"
        bar value VariableValue("transfer_amount", depositor.money, max_is_zero=False, style='scrollbar', offset=0, step=0.1) xmaximum 200

        hbox:
            for amount in [50,100,250,depositor.money]:
                if depositor.money>=amount:
                    textbutton str(amount) action SetVariable("transfer_amount", amount)
        hbox:
            textbutton "Transfer" action [Function(money_transfer, depositor, withdrawer, transfer_amount), SetVariable("transfer_amount", 0), Hide("banking")]
            textbutton "Cancel" action Hide("banking")

screen crafting(inventory):
    vbox:
        label "Recipes"
        hbox:
            xmaximum 600 xminimum 600 xfill True
            text "Name" xalign 0.5
            text "Ingredients" xalign 0.5
        side "c r":
            area (0,0,600,400)
            viewport id "cookbook":
                draggable True
                mousewheel True
                has vbox
                for item in cookbook:
                    hbox:
                        first_spacing 25 spacing 10
                        hbox:
                            xmaximum 250 xminimum 250 xfill True box_wrap True
                            if item.icon:
                                add im.FactorScale(item.icon, 0.33)
                            if inventory.check_recipe(item):
                                textbutton item.name action Function(inventory.craft,item)
                            else:
                                text item.name
                        for i in item.recipe:
                            if i[0].icon:
                                add im.FactorScale(i[0].icon, 0.33)
                            else:
                                text i[0].name
                            if inventory.qty(i[0]) >= i[1]:
                                text "x" + str(i[1]) bold True
                            else:
                                text "x" + str(i[1])
            vbar value YScrollValue("cookbook")
        textbutton "Hide" action ToggleScreenVariable("crafting_screen") xalign 0.5

screen view_nav(inventory):
    hbox:
        text "View: "
        textbutton "Grid" action SetField(inventory, "grid_view", True)
        textbutton "List" action SetField(inventory, "grid_view", False)

screen sort_nav(inventory):
    hbox:
        text "Sort: "
        textbutton "Name" action [ToggleField(inventory, "sort_by", inventory.sort_name), inventory.sort_name]
        textbutton "Qty" action [ToggleField(inventory, "sort_by", inventory.sort_qty), inventory.sort_qty]
        textbutton "Val" action [ToggleField(inventory, "sort_by", inventory.sort_value), inventory.sort_value]
        textbutton "Type" action [ToggleField(inventory, "sort_by", inventory.sort_type), inventory.sort_type]
screen inventory_popup(message):
    zorder 100
    button:
        add "UI/gallery_bg2.png"
        action Hide("inventory_popup")
    frame:
        style_group "invstyle"
        has hbox
        text message



init -2:


    style invstyle_frame:
        xalign 0.5
        yalign 0.3

    style invstyle_label_text:
        size 30

    style invstyle_label:
        xalign 0.5








screen EWinventory_screen(first_inventory, second_inventory=False, trade_mode=False):
    default crafting_screen = False
    tag menu
    hbox:
        spacing 35
    vbox:
        xalign 0.6 ypos 0.5
        frame:
            style_group "invstyle"
            has hbox:
                spacing 25
            vbox:
                label first_inventory.name
                if second_inventory:
                    use money(first_inventory, second_inventory, bank_mode)
                use inventory_view(first_inventory, second_inventory, trade_mode)

                textbutton "Close" action Hide("inventory_screen")
            vbox:
                label second_inventory.name
                use inventory_view(second_inventory, first_inventory, trade_mode)

            if crafting_screen:
                use crafting(first_inventory)

screen EWinventory_view_new(inventory, second_inventory=False, trade_mode=False):
    vbox:
        $ slot_number = 2
        $ found_item = False
        xalign 0.62 ypos 0.42



        style_group "invstyle"
        area (660, 432, 141, 132)
        vpgrid id ("vp"+inventory.name):
            draggable True
            mousewheel True
            xsize 770 ysize 450
            if inventory.grid_view:
                cols 3 spacing 53
            else:
                cols 1 spacing 40

            for slot_number in range (2, 8):

                $ found_item = False
                for item in [inventory.weapon,inventory.armor,inventory.place,inventory.accessories[0],inventory.accessories[1],inventory.accessories[2]]:
                    if item[0] != Null:
                        if item[0].type == slot_number:

                            $ name = item[0].name
                            $ desc = item[0].desc
                            $ value = item[0].value
                            $ qty = " "
                            hbox:
                                if item[0].icon:
                                    $ icon = item[0].icon
                                    $ hover_icon = im.Sepia(icon)

                                    imagebutton:
                                        idle LiveComposite((100,100), (0,0), icon, (0,0), Text(qty))
                                        hover LiveComposite((100,100), (0,0), hover_icon, (0,0), Text(qty))


                                        action (Function(unequip,item),Hide("tooltip"))
                                        hovered Show("tooltip",item=item,seller=second_inventory)
                                        unhovered Hide("tooltip")
                                    if not inventory.grid_view:
                                        vbox:
                                            text name
                                            if not trade_mode:
                                                text "List Value: [value]"
                                                if second_inventory:
                                                    text ("Sell Value: " + str(calculate_price(item, second_inventory)) + ")")

                                else:
                                    textbutton "[name] ([qty])" action (If(not second_inventory, item.act,(If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item))))) hovered Show("tooltip",item=item,seller=second_inventory) unhovered Hide("tooltip")
                                    if not inventory.grid_view:
                                        vbox:
                                            text "List Value: [value]"
                                            if not trade_mode and second_inventory:
                                                text "Sell Value: " + str(calculate_price(item, second_inventory)) + ")"

                            $ found_item = True
                if found_item == False:
                    add Null(height=100,width=100)





        vbar value YScrollValue("vp"+inventory.name)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
