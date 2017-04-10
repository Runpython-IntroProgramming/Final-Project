from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

rations=0
clothes=0
ice_picks=0
tents=0
fuel=0
water=0
the_hike=1
false_holder=True
truth_holder=True
the_hike=1

def destination(place):
    input("Welcome to {0}! You may: 1. Look around, 2. Attempt to Trade, 3. Stop to Rest, 4. See your health, 5. Review your items, 6. Go to the Store, 7. Continue on the hike".format(place))

while truth_holder is True:
    game_menu=input("Welcome to Kathmandu! You may: Press 1 to Start the Hike, press 2 to learn more about the trek up Mt. Everest, press 3 to see the map of the Mt. Everest trek, or press 4 to quit the program.")
    if game_menu is "2":
        input("The hike up Mount Everest is a long and difficult journey. It is filled with Hazards and danger. Type OK to continue.")  #Need to make more lengthy
    if game_menu is "3":
        input("This part of the Mount Everest Trail is under contruction right now. Press Enter to continue.")
    if game_menu is "4":
        raise SystemExit("Goodbye")
    if game_menu is "1":
        truth_holder=False
while truth_holder is False:
    player_type=input("Many people attempt to hike Everest each year. Who are you? You may be: 1. A CEO from America, 2. An accountant from England, 3. A scientist from Australia. Press 4 to learn more about these choices and how they affect the game.")
    if player_type is "4":
        input("The type of person you are affects how much money you have. For instance, a CEO will have more money than an accountant or scientist. However, if you choose the CEO, this will reduce your score at the end of the game. Press Enter to continue.")
    if player_type is "1":
        money=10000
        truth_holder=True
    if player_type is "2":
        money=7000
        truth_holder=True
    if player_type is "3":
        money=6500
        truth_holder=True
while truth_holder is True:
    store=input("You will need to buy supplies for the expedition. Press 1 to go to the store, or press 2 to go on the hike without supplies.")
    if store is "2":
        are_you_sure=input("Are you sure? The hike up Mount Everest is long and dangerous, and there will not be too many opportunities to buy supplies during the hike. Please type 'yes' or 'no' to confirm your choice.")
        if are_you_sure is "yes":
            the_hike=1
            truth_holder=False
    if store is "1":
        truth_holder=False
if store is "1":
    while truth_holder is False:
        item_menu=input("You have {0} rations, {1} sets of clothes, {2} ice picks, {3} tents, {4} canisters of fuel, and {5} liters of water. 1. Go to store, 2. Learn more about each item.".format(rations, clothes, ice_picks, tents, fuel, water)) 
        if item_menu is "2":
            input("Rations are what keep you alive. Without rations, your health will get worse. Clothes are what keep you warm. If they get wet, you will need a new set of clothes. If you do not change clothes or dry your clothes, you will get cold and your health will get worse. Ice picks help you scale ice walls. Ice picks break, so you will need to make sure to have some at all times. Tents are what you sleep in. These can break, and if they do and you not repair it or get a new one, you cannot sleep. Fuel is what you use to heat up rations to eat, as well as to melt snow to make water. Water is another necessary element to survive. Press Enter to continue.") 
        if item_menu is "1":
            truth_holder=True
if item_menu is "1":
    false_holder=True
    while false_holder is True:
        store_menu=input("Welcome to Mt. Everest Equipment Store! We sell at the lowest prices in all of the Himalayas. We sell: 1. Rations, 2. Clothes, 3. Ice picks, 4. Tents, 5. Fuel, 6. Water, 7. Review what you already have, 8. Leave store. What would you like to buy/choose?")
        if store_menu is "1":
            rations_loop=True
            while rations_loop is True:
                rations_inp=input("You have ${0}. Rations are sold in packs of ten. How many packs of rations would you like to buy at $14 each? I would recommend buying 20 packs for each person in your company to start. ".format(money))
                max_rations=round(money-((int(rations_inp))*14))
                if max_rations < 0:
                    input("You do not have enough money to buy all those! Press Enter to continue.")
                if max_rations >= 0:
                    rations=rations+(int(rations_inp)*10)
                    money=money-(int(rations_inp)*14)
                    endless_loop=True
                    while endless_loop is True:
                        rations_menu=input("You have {0} dollars left. Press: 1. to buy more rations, 2. Go back to store, 3. Leave the store. ".format(money))
                        if rations_menu is "1":
                            endless_loop=False
                        if rations_menu is "2":
                            rations_loop=False
                            endless_loop=False
                        if rations_menu is "3":
                            are_you_sure=input("Are you sure you would like to leave the store and stop buying supplies? ")
                            if are_you_sure is "yes":
                                false_holder=False
                                rations_loop=False
                                endless_loop=False 
        if store_menu is "2":
            clothes_loop=True
            while clothes_loop is True:
                clothes_inp=input("You have ${0}. Clothes are sold in sets. How many sets of clothes would you like to buy at $50 each? I would recommend buying two sets for each person in your party to start. ".format(money))
                max_clothes=round(money-((int(clothes_inp))*50))
                if max_clothes < 0:
                    input("You do not have enough money to buy all those! Press Enter to continue.")
                if max_clothes >= 0:
                    clothes=clothes+(int(clothes_inp)*1)
                    money=money-(int(clothes_inp)*50)
                    endless_loop=True
                    while endless_loop is True:
                        clothes_menu=input("You have {0} dollars left. Press: 1. to buy more clothes, 2. Go back to store, 3. Leave the store. ".format(money))
                        if clothes_menu is "1":
                            endless_loop=False
                        if clothes_menu is "2":
                            clothes_loop=False
                            endless_loop=False
                        if clothes_menu is "3":
                            are_you_sure=input("Are you sure you would like to leave the store and stop buying supplies? ")
                            if are_you_sure is "yes":
                                false_holder=False
                                clothes_loop=False
                                endless_loop=False 
        if store_menu is "3":
            ice_picks_loop=True
            while ice_picks_loop is True:
                ice_picks_inp=input("You have ${0}. Ice picks are sold individually. How many Ice Picks would you like to buy at $300 each? I would recommend buying three to start. ".format(money))
                max_ice_picks=round(money-((int(ice_picks_inp))*300))
                if max_ice_picks < 0:
                    input("You do not have enough money to buy all those! Press Enter to continue.")
                if max_ice_picks >= 0:
                    ice_picks=ice_picks+(int(ice_picks_inp)*1)
                    money=money-(int(ice_picks_inp)*300)
                    endless_loop=True
                    while endless_loop is True:
                        ice_picks_menu=input("You have {0} dollars left. Press: 1. to buy more ice picks, 2. Go back to store, 3. Leave the store. ".format(money))
                        if ice_picks_menu is "1":
                            endless_loop=False
                        if ice_picks_menu is "2":
                            ice_picks_loop=False
                            endless_loop=False
                        if ice_picks_menu is "3":
                            are_you_sure=input("Are you sure you would like to leave the store and stop buying supplies? ")
                            if are_you_sure is "yes":
                                false_holder=False
                                ice_picks_loop=False
                                endless_loop=False
                                
        if store_menu is "4":
            tents_loop=True
            while tents_loop is True:
                tents_inp=input("You have ${0}. Tents are sold individually. How many tents would you like to buy at $500 each? I would recommend buying three to start. ".format(money))
                max_tents=round(money-((int(tents_inp))*500))
                if max_tents < 0:
                    input("You do not have enough money to buy all those! Press Enter to continue.")
                if max_tents >= 0:
                    tents=tents+(int(tents_inp)*1)
                    money=money-(int(tents_inp)*500)
                    endless_loop=True
                    while endless_loop is True:
                        tents_menu=input("You have {0} dollars left. Press: 1. to buy more tents, 2. Go back to store, 3. Leave the store. ".format(money))
                        if tents_menu is "1":
                            endless_loop=False
                        if tents_menu is "2":
                            tents_loop=False
                            endless_loop=False
                        if tents_menu is "3":
                            are_you_sure=input("Are you sure you would like to leave the store and stop buying supplies? ")
                            if are_you_sure is "yes":
                                false_holder=False
                                tents_loop=False
                                endless_loop=False
                                
        if store_menu is "5":
            fuel_loop=True
            while fuel_loop is True:
                fuel_inp=input("You have ${0}. Fuel is sold in packs of 3 cans. How many packs of fuel would you like to buy at $30 each? I would recommend buying ten packs to start. ".format(money))
                max_fuel=round(money-((int(fuel_inp))*30))
                if max_fuel < 0:
                    input("You do not have enough money to buy all those! Press Enter to continue.")
                if max_fuel >= 0:
                    fuel=fuel+(int(fuel_inp)*3)
                    money=money-(int(fuel_inp)*30)
                    endless_loop=True
                    while endless_loop is True:
                        fuel_menu=input("You have {0} dollars left. Press: 1. to buy more fuel, 2. Go back to store, 3. Leave the store. ".format(money))
                        if fuel_menu is "1":
                            endless_loop=False
                        if fuel_menu is "2":
                            fuel_loop=False
                            endless_loop=False
                        if fuel_menu is "3":
                            are_you_sure=input("Are you sure you would like to leave the store and stop buying supplies? ")
                            if are_you_sure is "yes":
                                false_holder=False
                                fuel_loop=False
                                endless_loop=False

        if store_menu is "6":
            water_loop=True
            while water_loop is True:
                water_inp=input("You have ${0}. Water is sold in 5 liter packages. How many 5 liter packages of water would you like to buy at $20 each? I would recommend buying fifteen packs to start. ".format(money))
                max_water=round(money-((int(water_inp))*20))
                if max_water < 0:
                    input("You do not have enough money to buy all those! Press Enter to continue.")
                if max_water >= 0:
                    water=water+(int(water_inp)*5)
                    money=money-(int(water_inp)*20)
                    endless_loop=True
                    while endless_loop is True:
                        water_menu=input("You have {0} dollars left. Press: 1. to buy more water, 2. Go back to store, 3. Leave the store. ".format(money))
                        if water_menu is "1":
                            endless_loop=False
                        if water_menu is "2":
                            water_loop=False
                            endless_loop=False
                        if water_menu is "3":
                            are_you_sure=input("Are you sure you would like to leave the store and stop buying supplies? ")
                            if are_you_sure is "yes":
                                false_holder=False
                                water_loop=False
                                endless_loop=False

            
        if store_menu is "7":
            item_menu=input("You have {0} rations, {1} sets of clothes, {2} ice picks, {3} tents, {4} canisters of fuel, and {5} liters of water. Press 2 to learn more about each item.".format(rations, clothes, ice_picks, tents, fuel, water)) 
            if item_menu is "2":
                input("Rations are what keep you alive. Without rations, your health will get worse. Clothes are what keep you warm. If they get wet, you will need a new set of clothes. If you do not change clothes or dry your clothes, you will get cold and your health will get worse. Ice picks help you scale ice walls. Ice picks break, so you will need to make sure to have some at all times. Tents are what you sleep in. These can break, and if they do and you not repair it or get a new one, you cannot sleep. Fuel is what you use to heat up rations to eat, as well as to melt snow to make water. Water is another necessary element to survive. Press Enter to continue.")
            if item_menu is "help me":
                raise SystemExit("Goodbye")

            
        if store_menu is "8":
            are_you_sure=input("Are you sure you would like to leave the store and stop buying supplies? ")
            if are_you_sure is "yes":
                false_holder=False

        
if the_hike==1:
    input("The hike will continue from here.")

myapp = App()
myapp.run()
