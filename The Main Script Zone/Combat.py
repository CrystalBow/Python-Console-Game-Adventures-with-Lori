from Character import Character
from PlayableCharacter import PlayableCharacter
from Monster import Monster
import random
from ImportantFunctions import inputAndCheck
import csv
import os


class Combat(object):

    def __init__(self, continueStatus = True):
        self.order = []
        self.listing = {}
        self.continueStatus = continueStatus
        self.taunt = []
        self.defRaise = []
        self.atkRaise = []
        self.protected = []

    def combatantOrganizer(self):
        organizedOrder = []
        theStringOrder = []
        NumOrder = []
        for listing in self.order:
            NumOrder.append(listing[1])
        NumOrder.sort()
        for Num in NumOrder:
            for item in self.order:
                if Num == item[1]:
                    theStringOrder.append(item[0])
        counter = 0
        while counter < len(NumOrder):
            organizedOrder.append([theStringOrder[counter], NumOrder[counter]])
            counter += 1
        self.order = organizedOrder

    def skillHandler(self, ally, skill):
        if skill == "Axe" or skill == "Smiting Arrow" or skill == "Dagger Poke" or skill == "Slash":
            target = self.targetChooser()
            if ally.attack - self.listing[target].defense > 0:
                self.listing[target].currentHealth = self.listing[target].currentHealth - (ally.attack - self.listing[target].defense)
            else:
                self.listing[target].currentHealth = self.listing[target].currentHealth - 1
        elif skill == "Sweeping Slash":
            for figther in self.listing:
                if isinstance(self.listing[figther], Monster):
                    if ally.attack - self.listing[figther].defense > 0:
                        self.listing[figther].currentHealth = self.listing[figther].currentHealth - (
                                    ally.attack - self.listing[figther].defense)
                    else:
                        self.listing[figther].currentHealth = self.listing[figther].currentHealth - 1
        elif skill == "Second Wind":
            luck = int(random.random() * 10)
            ally.currentHealth = ally.currentHealth + luck
            if ally.currentHealth > ally.health:
                ally.currentHealth = ally.health
        elif skill == "Guard up":
            luck = int(random.random() * 10) + 1
            change = ally.defense/2
            self.defRaise.append([ally.displayName, luck, change])
            ally.defense = ally.defense + change
        elif skill == "Restoring Arrow":
            target = self.targetChooser(Ally=True, User=ally.displayName)
            self.listing[target].currentHealth = self.listing[target].currentHealth + ally.attack
            if self.listing[target].currentHealth > self.listing[target].health:
                self.listing[target].currentHealth = self.listing[target].health
        elif skill == "Focus Light" or skill == "Focus Light0":
            luck = int(random.random()*10) + 1
            change = ally.attack
            self.atkRaise.append([ally.displayName, luck, change])
            ally.attack = ally.attack + change
        elif skill == "Lightning Bolt":
            target = self.targetChooser()
            potential = ally.attack + ally.currentEnergy
            if potential - self.listing[target].defense > 0:
                self.listing[target].currentHealth = self.listing[target].currentHealth - (potential - self.listing[target].defense)
            else:
                self.listing[target].currentHealth = self.listing[target].currentHealth - 1
        elif skill == "Close Wound":
            target = self.targetChooser(Ally=True , User= ally.displayName)
            self.listing[target].currentHealth = self.listing[target].currentHealth + ally.currentEnergy
            if self.listing[target].currentHealth > self.listing[target].health:
                self.listing[target].currentHealth = self.listing[target].health
        elif skill == "Fire Ball":
            potential = ally.attack + ally.currentEnergy
            for figther in self.listing:
                if isinstance(self.listing[figther], Monster):
                    if potential - self.listing[figther].defense > 0:
                        self.listing[figther].currentHealth = self.listing[figther].currentHealth - (
                                    potential - self.listing[figther].defense)
                    else:
                        self.listing[figther].currentHealth = self.listing[figther].currentHealth - 1
        elif skill == "Full Guard":
            luck = int(random.random() * 10) + 2
            change = ally.defense
            self.defRaise.append([ally.displayName, luck, change])
            ally.defense = ally.defense + change
        elif skill == "Taunting Cry":
            luck = int(random.random() * 10) + 1
            self.taunt.append([ally.displayName, luck])
        elif skill == "Rally":
            for fighter in self.listing:
                if isinstance(self.listing[fighter], PlayableCharacter):
                    self.skillHandler(self.listing[fighter], "Focus Light0")

    def foePrep(self, autoSlected= ""):
        luck = int(random.random() * 100)
        while luck < 1:
            luck = int(random.random() * 100)
        if autoSlected == "":
            for figther in self.listing:
                if isinstance(self.listing[figther], Monster):
                    starter = self.listing[figther]
        else:
            enemyCatalog = []
            f = open("monsterStats.csv")
            fReader = csv.reader(f)
            for line in fReader:
                if line == []:
                    continue
                enemyCatalog.append(line)
            for enemy in enemyCatalog:
                if autoSlected == enemy[0]:
                    starter = Monster(attack=int(enemy[2]), health=int(enemy[1]), defense=int(enemy[3]), displayName=autoSlected, experince=int(enemy[7]), petRate=int(enemy[4]), buddyRate=int(enemy[5]), weapon=enemy[6])
                    self.intiativeRoll(starter)
                    break
            f.close()
        dividers = []
        if starter.buddyRate > 0:
            dividers.append(starter.buddyRate)
            dividers.append(starter.buddyRate + starter.petRate)
        else:
            dividers.append(0)
            dividers.append(starter.petRate)
        if luck < dividers[0]:
            buddy = Monster(attack= starter.attack, health= starter.health, defense= starter.defense, displayName= starter.displayName + "(0)", experince= starter.experience, petRate=starter.petRate, buddyRate= starter.buddyRate, weapon=starter.weapon )
            self.intiativeRoll(buddy)
            flag = True
            counter = 1
            while flag:
                luck = int(random.random() * 100)
                if luck < dividers[0]:
                    buddy = Monster(attack=starter.attack, health=starter.health, defense=starter.defense,
                                    displayName=starter.displayName + "(" + str(counter) + ")", experince=starter.experience,
                                    petRate=starter.petRate, buddyRate=starter.buddyRate, weapon=starter.weapon)
                    self.intiativeRoll(buddy)
                else:
                    flag = False
                counter += 1
                if counter == 6:
                    flag = False
        if luck < dividers[1]:
            f = open("encounters.csv")
            reader = csv.reader(f)
            regionCounter = 0
            endFlag = False
            for line in reader:
                if line == []:
                    continue
                for item in line:
                    if starter.displayName == item:
                        endFlag = True
                        break
                if endFlag:
                    break
                regionCounter += 1
            f.close()
            f = open("pets.csv")
            reader = csv.reader(f)
            pets = []
            for line in reader:
                if line == []:
                    continue
                if int(line[0]) == regionCounter:
                    for pet in line:
                        try:
                            int(pet)
                            continue
                        except ValueError:
                            pets.append(pet)
                    division = int(100/len(pets))
                    dividers = []
                    while division < 100:
                        dividers.append(division)
                        division += division
                    dividers.append(100)
                    luck = int(random.random() * 100)
                    while luck < 1:
                        luck = int(random.random() * 100)
                    counter = 0
                    for divider in dividers:
                        if luck < divider:
                            break
                        counter += 1
                    self.foePrep(autoSlected= pets[counter])
        else:
            pass



    def targetChooser(self, Ally= False, User= None):
        choices = []
        i = 0
        forum = []
        if Ally:
            for target in self.listing:
                if isinstance(self.listing[target], PlayableCharacter):
                    if not self.listing[target].displayName == User:
                        if self.listing[target].level > 0:
                            choices.append(i)
                            print(str(i) + ": " + self.quickdisplay(self.listing[target], newLineOverride= True))
                            forum.append(target)
                            i += 1
            i = inputAndCheck("Target: ", choices)
            return forum[i]
        else:
            for target in self.listing:
                if isinstance(self.listing[target], Monster):
                    choices.append(i)
                    print(str(i) + ": " + target)
                    forum.append(target)
                    i += 1
            i = inputAndCheck("Target: ", choices)
            return forum[i]

    def intiativeRoll(self, Combatant):

        # defualt for now
        self.listing.update({Combatant.displayName : Combatant})
        self.order.append([Combatant.displayName, random.random()])

    def combatEndCheck(self):
        removalList = []
        follow = False
        for figther in self.listing:
            removeFlag = self.listing[figther].deathCheck()
            if removeFlag == True:
                removalList.append(figther)
                i = 0
                for thing in self.order:
                    if thing[0] == figther:
                        self.order.pop(i)
                        break
                    i += 1
                continue
            if isinstance(self.listing[figther], Monster):
                follow = True
        for body in removalList:
            self.listing.pop(body)
        return follow

    def baseAttack(self, attacker):
        targetingNum = int(random.random() * 100)
        while targetingNum < 1:
            targetingNum = int(random.random() * 100)
        targets = []
        for fighter in self.listing:
            if isinstance(self.listing[fighter], PlayableCharacter):
                targets.append(fighter)
        if self.taunt == []:
            dividers = [81, 61, 41, 21]
        else:
            dividers = []
            counter = 100
            for peep in targets:
                if peep == self.taunt[0][0]:
                    counter -= 34
                    dividers.append(counter)
                else:
                    counter -= 14
                    dividers.append(counter)
        flag = False
        for divider in dividers:
            if flag:
                break
            if targetingNum > divider:
                target = targets[dividers.index(divider)]
                flag = True
        try:
            if target not in self.protected:
                self.attackDispaly(attacker, target)
                if (attacker.attack - self.listing[target].defense >= 0):
                    self.listing[target].currentHealth = self.listing[target].currentHealth - attacker.attack + self.listing[target].defense
                else:
                    self.listing[target].currentHealth = self.listing[target].currentHealth - 1
        except UnboundLocalError:
            pass

        # defualt for now

    def turn(self, ally):
        choices = []
        chosen = 0
        i = 0
        if isinstance(ally, Monster):
            print("Turn: " + ally.displayName)
            self.baseAttack(ally)
        else:
            if ally.currentHealth > 0:
                try:
                    print("up next:" + self.intiativeDisplay(ally.displayName))
                    print("Current turn: " + self.quickdisplay(ally))
                    if ally.displayName not in self.protected:
                        for skill in ally.skills:
                            if ally.skillCosts[i] <= ally.currentEnergy:
                                print(str(i) + ": " + skill)
                                choices.append(i)
                            i += 1
                        protect = i
                        if self.saftey():
                            print(str(protect)+ ": Fall back")
                            choices.append(i)
                        chosen = inputAndCheck("What will " + ally.displayName + " do? ", choices)
                        if chosen == protect:
                            self.saftey(availability= False, Ally= ally.displayName)
                        else:
                            ally.currentEnergy = ally.currentEnergy - ally.skillCosts[chosen]
                            self.skillHandler(ally, ally.skills[chosen])
                    else:
                        choices = [0,1]
                        print("0: Stay back")
                        print("1: go back to front")
                        chosen = inputAndCheck("What will " + ally.displayName + " do? ", choices)
                        if chosen == 0:
                            self.safteyRecovery(ally.displayName)
                        else:
                            self.saftey(Ally= ally.displayName, Removal= True)
                except TypeError:
                    pass
                counter = 0
                for defender in self.defRaise:
                    if defender[0] == ally.displayName:
                        defender[1] = defender[1] - 1
                        if defender[1] <= 0:
                            ally.defense = ally.defense - defender[2]
                            self.defRaise.pop(counter)
                    counter += 1
                counter = 0
                for attacker in self.atkRaise:
                    if attacker[0] == ally.displayName:
                        attacker[1] = attacker[1] - 1
                        if attacker[1] <= 0:
                            ally.attack = ally.attack - attacker[2]
                            self.defRaise.pop(counter)
                    counter += 1
                counter = 0
                for annoyance in self.taunt:
                    if annoyance[0] == ally.displayName:
                        annoyance[1] = annoyance[1] - 1
                        if annoyance[1] <= 0:
                            self.defRaise.pop(counter)
                    counter += 1

    def saftey(self, availability= True, Ally= None, Removal= False):
        counter = 0
        if Removal:
            self.protected.remove(Ally)
            return 0
        if availability:
            if len(self.protected) > 0:
                return False
            for figther in self.listing:
                if self.listing[figther].currentHealth > 0:
                    if isinstance(self.listing[figther], PlayableCharacter):
                        counter += 1
            if counter > 1:
                return True
            else:
                return False
        else:
            self.protected.append(Ally)

    def safteyRecovery(self, ally):
        luck = int(random.random() * 20)
        friend = self.listing[ally]
        if isinstance(friend, PlayableCharacter):
            friend.currentHealth = friend.currentHealth + luck
            friend.currentEnergy = friend.currentEnergy + luck
            if friend.currentEnergy > friend.energyValue:
                friend.currentEnergy = friend.energyValue
            if friend.currentHealth > friend.health:
                friend.currentHealth = friend.health
            self.listing[ally] = friend

    def quickdisplay(self, ally, newLineOverride= False):
        if newLineOverride:
            return ally.displayName + "(hp: " + str(ally.currentHealth) + "/" + str(
                ally.health) + " " + ally.energyName + ": " + str(ally.currentEnergy) + "/" + str(ally.energyValue) + ")"
        return ally.displayName + "\nhp: " + str(ally.currentHealth) + "/" + str(ally.health) + " " + ally.energyName + ": " + str(ally.currentEnergy) + "/" + str(ally.energyValue)

    def intiativeDisplay(self, allyName):
        string = ""
        setup = []
        flag = False
        counter = 0
        for fighter in self.order:
            if fighter[0] == allyName:
                flag = True
                continue
            if isinstance(self.listing[fighter[0]], PlayableCharacter):
                if self.listing[fighter[0]].level <= 0:
                    continue
                playableDisplay = self.quickdisplay(self.listing[fighter[0]],newLineOverride= True)
                if flag:
                    setup.insert(counter, playableDisplay)
                else:
                    setup.append(playableDisplay)
                continue

            if flag:
                setup.insert(counter, fighter[0])
                counter += 1
            else:
                setup.append(fighter[0])
        flag = False
        for peep in setup:
            if flag:
                string = string + ", " + peep
            else:
                string = string + " " + peep
                flag = True
        return string

    def attackDispaly(self, attacker, target, attackName= None):
        #might remove if it slows down game to much. Might rewrite for more flavor.
        if isinstance(attacker, Monster):
            input(attacker.displayName + " used their " + attacker.weapon + " on " + target + "(Enter to continue)")