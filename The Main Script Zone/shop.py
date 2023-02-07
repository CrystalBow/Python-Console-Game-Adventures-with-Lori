import csv
import os

from Items import Item
from PlayableCharacter import PlayableCharacter
from ImportantFunctions import inputAndCheck
class Shop(object):
    def __init__(self):
        self.items = []
        f = open("items.csv")
        fReader = csv.reader(f)
        for line in fReader:
            if line == []:
                continue
            self.items.append(Item(line[2], line[0], int(line[1]), int(line[3])))
        f.close()

    def storeRun(self, squad :list, gold :int):
        done = False
        while not done:
            shopper = self.whoIsShopping(squad)
            os.system("cls")
            print("gold: " + str(gold))
            action = self.shopDisplay(shopper)
            if action >= len(self.items):
                pass
            else:
                result = self.buy(self.items[action], gold, shopper)
                if isinstance(result, Item):
                    input("Stingy man: here you go! thankyou for your business!(press enter to continue)")
                    shopper.inventory.append(result)
                    if result.usage != "hp":
                        shopper = result.effectHandler(shopper)
                    gold = gold - result.cost
                else:
                    input(result)
            result = inputAndCheck("are you done shopping?(0: no, 1: yes)", [0, 1])
            counter = 0
            for ally in squad:
               if ally.displayName == shopper.displayName:
                   squad[counter] = shopper
               counter += 1

            if result == 1:
                done = True
        return [squad, gold]

    def buy(self, item :Item, gold, user :PlayableCharacter):
        if item.cost <= gold:
            if item.effect == "AtkPhy":
                if user.energyName != "Mana":
                    return item
                else:
                    return user.displayName + " can't use that(press enter to continue)"
            elif item.effect == "AtkMag":
                if user.energyName == "Mana":
                    return item
                else:
                    return user.displayName + " can't use that(press enter to continue)"
            else:
                return item
        else:
            return "insufficient gold"

    def shopDisplay(self, member :PlayableCharacter):
        print("Stingy Man: welcome traveler, as long as you have gold your welcome! What are you looking for today?")
        counter = 0
        choices = []
        for item in self.items:
            print(str(counter) + ": " + item.name + "(" + str(item.cost) + " gold)")
            choices.append(counter)
            counter += 1
        choices.append(counter)
        print(str(counter) + ": Leave")
        return inputAndCheck(member.displayName + "'s action: ", choices)
    def whoIsShopping(self, squad :list):
        counter = 0
        choices = []
        print("Who is shopping?")
        for member in squad:
            if member.level > 0:
                print(str(counter) + ": " + member.displayName)
                choices.append(counter)
                counter += 1
        selection = inputAndCheck("Selection: ", choices)
        return squad[selection]