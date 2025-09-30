#!/usr/bin/env python
# imports
import random
import csv
from PlayableCharacter import PlayableCharacter
from Monster import Monster
import os
from gameMenu import GameMenu
from Combat import Combat
from Location import Location
from ImportantFunctions import inputAndCheck
from shop import Shop
from Items import Item

# Variables
x = 0
y = 0
z = 0
chapter = 0
Lori = PlayableCharacter(displayName="Lori")
Lauren = PlayableCharacter(displayName="Lauren")
Marcus = PlayableCharacter(displayName="Marcus")
Julius = PlayableCharacter(displayName="Julius")
regionDisplay = " "
region = 0
locations = []
local = False
gold = 0
# Testing Purposes
ThatMonster = Monster(displayName="Test Boy", attack=10, defense=5, health=1, experince=10)


def inventorySetup(inventory: list):
    itemFetcher = Shop()
    newInventory = []
    for string in inventory:
        for item in itemFetcher.items:
            if item.name == string:
                newInventory.append(item)
    return newInventory


# Functions
# Extracting Save Data
def bootSave(saveNum):
    # Establish Global Variables
    global x
    global y
    global z
    global chapter
    global Lori
    global Lauren
    global Marcus
    global Julius
    global gold
    # Save Check
    if saveNum == 0:
        # New Game, Load Data
        f = open("newGame.csv")
        fReader = csv.reader(f)
        content = next(fReader)
        x = int(content[0])
        y = int(content[1])
        z = int(content[2])
        chapter = int(content[3])
        Lori.level = int(content[4])
        Lauren.level = int(content[5])
        Marcus.level = int(content[6])
        Julius.level = int(content[7])
        f.close()
    else:
        # Try to find specified save.
        try:
            # Load the files
            f = open("save" + str(saveNum) + ".csv")
            fReader = csv.reader(f)
            content = next(fReader)
            # Capture basic character data and story progress
            x = int(content[0])
            y = int(content[1])
            z = int(content[2])
            chapter = int(content[3])
            Lori.level = int(content[4])
            Lauren.level = int(content[5])
            Marcus.level = int(content[6])
            Julius.level = int(content[7])
            next(fReader)
            # Capture inventories for each character
            content = next(fReader)
            Lori.inventory = inventorySetup(content)
            next(fReader)
            content = next(fReader)
            Lauren.inventory = inventorySetup(content)
            next(fReader)
            content = next(fReader)
            Marcus.inventory = inventorySetup(content)
            next(fReader)
            content = next(fReader)
            Julius.inventory = inventorySetup(content)
            next(fReader)
            # Collect gold and experience
            content = next(fReader)
            gold = int(content[0])
            Lori.experience = int(content[1])
            Lauren.experience = int(content[2])
            Marcus.experience = int(content[3])
            Julius.experience = int(content[4])
            next(fReader)
            # Record current values for HP and MP
            content = next(fReader)
            Lori.currentHealth = int(content[0])
            Lauren.currentHealth = int(content[1])
            Marcus.currentHealth = int(content[2])
            Julius.currentHealth = int(content[3])
            next(fReader)
            content = next(fReader)
            Lori.currentEnergy = int(content[0])
            Lauren.currentEnergy = int(content[1])
            Marcus.currentEnergy = int(content[2])
            Julius.currentEnergy = int(content[3])
        except FileNotFoundError:
            # Try Again if not found.
            bootSave(inputAndCheck("how would you like to boot? 0 New game or integer of save you are booting",
                                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# region getters
# Fetches the z value
def fetchRegionZ(regionID):
    file = open("regions.csv")
    fileReader = csv.reader(file)
    regions = []
    for line in fileReader:
        if line == []:
            continue
        regions.append(line)
    file.close()
    return int(regions[regionID][7])

#Fetches the region name
def fetchRegionDisplay(regionID):
    file = open("regions.csv")
    fileReader = csv.reader(file)
    regions = []
    for line in fileReader:
        if line == []:
            continue
        regions.append(line)
    file.close()
    return regions[regionID][1]

# Checks what region certain coordinates are on and return region information
def regionCheck(x, y, z):
    # Fetch region from file
    file = open("regions.csv")
    fileReader = csv.reader(file)
    targetRegion = -1
    regions = []
    for line in fileReader:
        regions.append(line)
    file.close()
    # look over regions for valid one
    for line in regions:
        if line == []:
            continue
        if ((int(line[2]) <= x) and (int(line[3]) >= x)) and ((int(line[4]) <= y) and (int(line[5]) >= y)):
            targetRegion = int(line[0])
            break

    return targetRegion


def regionDiscribe(regionID):
    file = open("descriptions.csv")
    fileReader = csv.reader(file)
    regions = []
    for line in fileReader:
        if line == []:
            continue
        regions.append(line)
    file.close()
    choice = int(random.random() * 10)
    while choice >= len(regions[regionID]):
        choice = int(random.random() * 10)
    return regions[regionID][choice]


def save(characters, x, y, z, ch, gp):
    choice = inputAndCheck("What file would you like to save too? ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    os.system("type nul > save" + str(choice) + ".csv")
    f = open("save" + str(choice) + ".csv", "w")
    fWriter = csv.writer(f)
    Row = [x, y, z, ch]
    Rows = []
    for playable in characters:
        Row.append(playable.level)
    Rows.append(Row)
    for playable in characters:
        Row = []
        for item in playable.inventory:
            Row.append(item.name)
        Rows.append(Row)
    Row = [gp]
    for playable in characters:
        Row.append(playable.experience)
    Rows.append(Row)
    Row = []
    for playable in characters:
        Row.append(playable.currentHealth)
    Rows.append(Row)
    Row = []
    for playable in characters:
        Row.append(playable.currentEnergy)
    Rows.append(Row)
    Row = []
    for playable in characters:
        Row.append(playable.experience)
    Rows.append(Row)
    fWriter.writerows(Rows)
    f.close()
    choice = inputAndCheck("Would you like to keep playing? (1: Yes, 0: No) ", [0, 1])
    if choice == 0:
        exit()


def rest(charecters, local):
    updatedCharacters = []
    if local:
        for wifu in charecters:
            wifu.currentHealth = wifu.health
            wifu.currentEnergy = wifu.energyValue
            updatedCharacters.append(wifu)
    else:
        for wifu in charecters:
            if wifu.level == 0:
                updatedCharacters.append(wifu)
                continue
            luck = int(random.random() * 10)
            wifu.currentHealth = wifu.currentHealth + luck
            wifu.currentEnergy = wifu.currentEnergy + luck
            if wifu.currentHealth > wifu.health:
                wifu.currentHealth = wifu.health
            if wifu.currentEnergy > wifu.energyValue:
                wifu.currentEnergy = wifu.energyValue
            updatedCharacters.append(wifu)
    return updatedCharacters


def encounterCheck(RegionID):
    f = open("encounters.csv")
    Roll = int(random.random() * 100)
    Reader = csv.reader(f)
    PossibleFights = []
    for region in Reader:
        if region == []:
            continue
        PossibleFights.append(region)
    f.close()
    if int(PossibleFights[RegionID][0]) > Roll:
        return [False]
    up = 2
    down = 0
    for fight in PossibleFights[RegionID]:
        try:
            int(fight)
            continue
        except ValueError:
            try:
                if int(PossibleFights[RegionID][down]) < Roll < int(PossibleFights[RegionID][up]):
                    return [True, fight]
                else:
                    up += 2
                    down += 2
            except IndexError:
                return [True, PossibleFights[RegionID][len(PossibleFights[RegionID]) - 1]]
    return [False]


def runCombat(intialBadie, wifus, location):
    global gold
    input("fight!")
    # temporary^^
    theBattle = Combat()
    enemyCatalog = []
    postBattleWifus = []
    for ally in wifus:
        theBattle.intiativeRoll(ally)
    f = open("monsterStats.csv")
    fReader = csv.reader(f)
    for line in fReader:
        if line == []:
            continue
        enemyCatalog.append(line)
    for badie in intialBadie:
        for enemy in enemyCatalog:
            if badie == enemy[0]:
                theBattle.intiativeRoll(
                    Monster(attack=int(enemy[2]), health=int(enemy[1]), defense=int(enemy[3]), displayName=badie,
                            experince=int(enemy[7]), petRate=int(enemy[4]), buddyRate=int(enemy[5]), weapon=enemy[6]))
    theBattle.foePrep()
    theBattle.combatantOrganizer()
    while theBattle.continueStatus:
        for fighter in theBattle.order:
            theBattle.turn(theBattle.listing[fighter[0]])
            theBattle.listing[fighter[0]].deathCheck()
            theBattle.continueStatus = theBattle.combatEndCheck()
            if not theBattle.continueStatus:
                break
            os.system("cls")
    checker = 0
    for fighter in theBattle.listing:
        if isinstance(theBattle.listing[fighter], PlayableCharacter):
            theBattle.listing[fighter].experience = theBattle.listing[fighter].experience + theBattle.exp
            gold = gold + theBattle.exp
            if theBattle.listing[fighter].currentHealth > 0:
                checker += 1
            postBattleWifus.append(theBattle.listing[fighter])
    if checker == 0:
        input("GAME OVER")
        exit()
    del theBattle
    return postBattleWifus


def AOEScanner(x, y, z, locals, regionID):
    finds = []
    scan = locationCheck(x + 1, y, z, locals, regionID)
    if scan[0]:
        finds.append([scan[2], "east"])
    scan = locationCheck(x + 1, y + 1, z, locals, regionID)
    if scan[0]:
        finds.append([scan[2], "north east"])
    scan = locationCheck(x + 1, y - 1, z, locals, regionID)
    if scan[0]:
        finds.append([scan[2], "south east"])
    scan = locationCheck(x - 1, y, z, locals, regionID)
    if scan[0]:
        finds.append([scan[2], "west"])
    scan = locationCheck(x - 1, y + 1, z, locals, regionID)
    if scan[0]:
        finds.append([scan[2], "north west"])
    scan = locationCheck(x - 1, y - 1, z, locals, regionID)
    if scan[0]:
        finds.append([scan[2], "south west"])
    scan = locationCheck(x, y + 1, z, locals, regionID)
    if scan[0]:
        finds.append([scan[2], "north"])
    scan = locationCheck(x, y - 1, z, locals, regionID)
    if scan[0]:
        finds.append([scan[2], "south"])
    return finds


def locationCheck(x, y, z, locals, regionID):
    areas = []
    for place in locals:
        if x == place.x and y == place.y and z == place.z:
            return [True, locals, place.displayName]
    if regionID == 0:
        f = open("larmenPlains.csv")
        fileReader = csv.reader(f)
        for line in fileReader:
            if line == []:
                continue
            areas.append(line)
        for place in areas:
            if int(place[1]) == x and int(place[2]) == y and int(place[3]) == z:
                if Location(Name=place[0], x=x, y=y, z=z) not in locals:
                    locals.append(Location(Name=place[0], x=x, y=y, z=z))  # need to add a status to location class.
                    return [True, locals, place[0]]
                else:
                    return [True, locals, place[0]]
        return [False, locals]
    elif regionID == 1:
        return [False, locals]
    elif regionID == 2:
        return [False, locals]
    elif regionID == 3:
        f = open("desert3.csv")
        fileReader = csv.reader(f)
        for line in fileReader:
            if line == []:
                continue
            areas.append(line)
        for place in areas:
            if int(place[1]) == x and int(place[2]) == y and int(place[3]) == z:
                if Location(Name=place[0], x=x, y=y, z=z) not in locals:
                    locals.append(Location(Name=place[0], x=x, y=y, z=z))
                    return [True, locals, place[0]]
                else:
                    return [True, locals, place[0]]
        return [False, locals]
    elif regionID == 4:
        f = open("ruinedPlateau.csv")
        fileReader = csv.reader(f)
        for line in fileReader:
            if line == []:
                continue
            areas.append(line)
        for place in areas:
            if int(place[1]) == x and int(place[2]) == y and int(place[3]) == z:
                if Location(Name=place[0], x=x, y=y, z=z) not in locals:
                    locals.append(Location(Name=place[0], x=x, y=y, z=z))
                    return [True, locals, place[0]]
                else:
                    return [True, locals, place[0]]
        return [False, locals]
    elif regionID == 5:
        f = open("theDeathLands.csv")
        fileReader = csv.reader(f)
        for line in fileReader:
            if line == []:
                continue
            areas.append(line)
        for place in areas:
            if int(place[1]) == x and int(place[2]) == y and int(place[3]) == z:
                if Location(Name=place[0], x=x, y=y, z=z) not in locals:
                    locals.append(Location(Name=place[0], x=x, y=y, z=z))
                    return [True, locals, place[0]]
                else:
                    return [True, locals, place[0]]
        return [False, locals]
    elif regionID == 6:
        f = open("gobbiMontains.csv")
        fileReader = csv.reader(f)
        for line in fileReader:
            if line == []:
                continue
            areas.append(line)
        for place in areas:
            if int(place[1]) == x and int(place[2]) == y and int(place[3]) == z:
                if Location(Name=place[0], x=x, y=y, z=z) not in locals:
                    locals.append(Location(Name=place[0], x=x, y=y, z=z))
                    return [True, locals, place[0]]
                else:
                    return [True, locals, place[0]]
        return [False, locals]
    elif regionID == 7:
        f = open("drameKingdom.csv")
        fileReader = csv.reader(f)
        for line in fileReader:
            if line == []:
                continue
            areas.append(line)
        for place in areas:
            if int(place[1]) == x and int(place[2]) == y and int(place[3]) == z:
                if Location(Name=place[0], x=x, y=y, z=z) not in locals:
                    locals.append(Location(Name=place[0], x=x, y=y, z=z))
                    return [True, locals, place[0]]
                else:
                    return [True, locals, place[0]]
        return [False, locals]
    elif regionID == 8:
        f = open("miniPlatPen.csv")
        fileReader = csv.reader(f)
        for line in fileReader:
            if line == []:
                continue
            areas.append(line)
        for place in areas:
            if int(place[1]) == x and int(place[2]) == y and int(place[3]) == z:
                if Location(Name=place[0], x=x, y=y, z=z) not in locals:
                    locals.append(Location(Name=place[0], x=x, y=y, z=z))
                    return [True, locals, place[0]]
                else:
                    return [True, locals, place[0]]
        return [False, locals]
    elif regionID == 9:
        f = open("kingdomOfJavi.csv")
        fileReader = csv.reader(f)
        for line in fileReader:
            if line == []:
                continue
            areas.append(line)
        for place in areas:
            if int(place[1]) == x and int(place[2]) == y and int(place[3]) == z:
                if Location(Name=place[0], x=x, y=y, z=z) not in locals:
                    locals.append(Location(Name=place[0], x=x, y=y, z=z))
                    return [True, locals, place[0]]
                else:
                    return [True, locals, place[0]]
        return [False, locals]
    elif regionID == 10:
        f = open("igachiPlain.csv")
        fileReader = csv.reader(f)
        for line in fileReader:
            if line == []:
                continue
            areas.append(line)
        for place in areas:
            if int(place[1]) == x and int(place[2]) == y and int(place[3]) == z:
                if Location(Name=place[0], x=x, y=y, z=z) not in locals:
                    locals.append(Location(Name=place[0], x=x, y=y, z=z))
                    return [True, locals, place[0]]
                else:
                    return [True, locals, place[0]]
        return [False, locals]


# creation and level up of characters
def generateCharacters():
    # Bring in globals
    global Lori
    global Lauren
    global Marcus
    global Julius
    # Establish arrays to hold stat lines and teamlist
    garbage = 0
    statLine = []
    lvlCounter = 0
    adderLine = []
    teamlist = [Lori, Lauren, Marcus, Julius]
    # Level up check
    for wifu in teamlist:
        levelpoint = wifu.level * 11
        if wifu.level > 0:
            if wifu.experience >= levelpoint:
                print("level up!")
                wifu.level += 1
                wifu.experience = 0
    #Apply Level ups
    Lori = teamlist[0]
    Lauren = teamlist[1]
    Marcus = teamlist[2]
    Julius = teamlist[3]
    # Apply Stats (10 and lower are predetermined. Higher is just scale)
    if Lori.level < 10:
        #Lori Predetermined
        file = open("lori.csv")
        fileReader = csv.reader(file)
        #Setup
        Lori.skills = list(next(fileReader))
        Lori.skillCosts = []
        Lori.energyName = Lori.skills[0]
        Lori.skills.pop(0)
        # fetch data
        garbage = next(fileReader)
        stringCosts = next(fileReader)
        for row in fileReader:
            if row == []:
                pass
            else:
                statLine = row
                try:
                    lvlCounter = int(statLine[0])
                    if lvlCounter == Lori.level:
                        break
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Apply Data
        Lori.health = int(statLine[1])
        Lori.attack = int(statLine[2])
        Lori.defense = int(statLine[3])
        Lori.energyValue = int(statLine[4])
        for stuff in stringCosts:
            garbage = int(stuff)
            Lori.skillCosts.append(garbage)
        Lori.skillCosts.pop(0)
    else:
        # Scaling Level ups
        doneFlag = False
        file = open("Lori.csv")
        fileReader = csv.reader(file)
        Lori.skills = list(next(fileReader))
        Lori.skillCosts = []
        Lori.energyName = Lori.skills[0]
        Lori.skills.pop(0)
        garbage = next(fileReader)
        stringCosts = next(fileReader)
        # Fetch
        for row in fileReader:
            if row == []:
                pass
            else:
                if not doneFlag:
                    statLine = row
                else:
                    adderLine = row
                try:
                    lvlCounter = int(statLine[0])
                    if lvlCounter == 9:
                        if doneFlag:
                            break
                        doneFlag = True
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Pass to generator
        Lori = higherLvlGenerator(Lori, statLine, adderLine)
        # Apply skill costs (they don't scale)
        for stuff in stringCosts:
            garbage = int(stuff)
            Lori.skillCosts.append(garbage)
        Lori.skillCosts.pop(0)
    # Lauren level ups
    if Lauren.level < 10 and Lauren.level > 0:
        # Predetermined Levels
        file = open("lauren.csv")
        fileReader = csv.reader(file)
        Lauren.skills = next(fileReader)
        Lauren.energyName = Lauren.skills[0]
        Lauren.skillCosts = []
        Lauren.skills.pop(0)
        # Fetch
        garbage = next(fileReader)
        stringCosts = next(fileReader)
        for row in fileReader:
            if row == []:
                pass
            else:
                statLine = row
                try:
                    lvlCounter = int(statLine[0])
                    if lvlCounter == Lauren.level:
                        break
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Apply
        Lauren.health = int(statLine[1])
        Lauren.attack = int(statLine[2])
        Lauren.defense = int(statLine[3])
        Lauren.energyValue = int(statLine[4])
        for stuff in stringCosts:
            garbage = int(stuff)
            Lauren.skillCosts.append(garbage)
        Lauren.skillCosts.pop(0)
    else:
        # Scaling levels
        doneFlag = False
        file = open("lauren.csv")
        fileReader = csv.reader(file)
        Lauren.skills = next(fileReader)
        Lauren.energyName = Lauren.skills[0]
        Lauren.skillCosts = []
        Lauren.skills.pop(0)
        # Fetch
        garbage = next(fileReader)
        stringCosts = next(fileReader)
        for row in fileReader:
            if row == []:
                pass
            else:
                if not doneFlag:
                    statLine = row
                else:
                    adderLine = row
                try:
                    lvlCounter = int(statLine[0])
                    if lvlCounter == 9:
                        if doneFlag:
                            break
                        doneFlag = True
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Pass to generator
        Lauren = higherLvlGenerator(Lauren, statLine, adderLine)
        # Applying Skill Costs
        for stuff in stringCosts:
            garbage = int(stuff)
            Lauren.skillCosts.append(garbage)
        Lauren.skillCosts.pop(0)
    # Julius Time
    if Julius.level < 10 and Julius.level > 0:
        # Predetermined Levels
        file = open("julius.csv")
        fileReader = csv.reader(file)
        Julius.skills = next(fileReader)
        Julius.skillCosts = []
        Julius.energyName = Julius.skills[0]
        Julius.skills.pop(0)
        # Fetch
        garbage = next(fileReader)
        stringCosts = next(fileReader)
        for row in fileReader:
            if row == []:
                pass
            else:
                statLine = row
                try:
                    lvlCounter = int(statLine[0])
                    if lvlCounter == Julius.level:
                        break
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Apply
        Julius.health = int(statLine[1])
        Julius.attack = int(statLine[2])
        Julius.defense = int(statLine[3])
        Julius.energyValue = int(statLine[4])
        for stuff in stringCosts:
            garbage = int(stuff)
            Julius.skillCosts.append(garbage)
        Julius.skillCosts.pop(0)
    elif Julius.level > 0:
        # Scaling levels
        doneFlag = False
        file = open("julius.csv")
        fileReader = csv.reader(file)
        Julius.skills = next(fileReader)
        Julius.skillCosts = []
        Julius.energyName = Julius.skills[0]
        Julius.skills.pop(0)
        garbage = next(fileReader)
        stringCosts = next(fileReader)
        for row in fileReader:
            if row == []:
                pass
            else:
                if not doneFlag:
                    statLine = row
                else:
                    adderLine = row
                try:
                    lvlCounter = int(statLine[0])
                    if lvlCounter == 9:
                        if doneFlag:
                            break
                        doneFlag = True
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Pass to Generator
        Julius = higherLvlGenerator(Julius, statLine, adderLine)
        # Apply skill costs
        for stuff in stringCosts:
            garbage = int(stuff)
            Julius.skillCosts.append(garbage)
        Julius.skillCosts.pop(0)
    if Marcus.level < 10 and Marcus.level > 0:
        # Predetermined Levels
        file = open("marcus.csv")
        fileReader = csv.reader(file)
        Marcus.skills = next(fileReader)
        Marcus.skillCosts = []
        Marcus.energyName = Marcus.skills[0]
        Marcus.skills.pop(0)
        # Fetch
        garbage = next(fileReader)
        stringCosts = next(fileReader)
        for row in fileReader:
            if row == []:
                pass
            else:
                statLine = row
                try:
                    lvlCounter = int(statLine[0])
                    if lvlCounter == Marcus.level:
                        break
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Apply
        Marcus.health = int(statLine[1])
        Marcus.attack = int(statLine[2])
        Marcus.defense = int(statLine[3])
        Marcus.energyValue = int(statLine[4])
        for stuff in stringCosts:
            garbage = int(stuff)
            Marcus.skillCosts.append(garbage)
        Marcus.skillCosts.pop(0)
    elif Marcus.level > 0:
        # Scaling Levels
        doneFlag = False
        file = open("marcus.csv")
        fileReader = csv.reader(file)
        Marcus.skills = next(fileReader)
        Marcus.skillCosts = []
        Marcus.energyName = Marcus.skills[0]
        Marcus.skills.pop(0)
        # Fetch
        garbage = next(fileReader)
        stringCosts = next(fileReader)
        for row in fileReader:
            if row == []:
                pass
            else:
                if not doneFlag:
                    statLine = row
                else:
                    adderLine = row
                try:
                    lvlCounter = int(statLine[0])
                    if lvlCounter == 9:
                        if doneFlag:
                            break
                        doneFlag = True
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Pass to generator
        Marcus = higherLvlGenerator(Marcus, statLine, adderLine)
        # Apply Skill Costs
        for stuff in stringCosts:
            garbage = int(stuff)
            Marcus.skillCosts.append(garbage)
        Marcus.skillCosts.pop(0)

    # Inventory Setup
    quickListing = [Lori, Lauren, Marcus, Julius]
    for playable in quickListing:
        for item in playable.inventory:
            # For Each Item
            playable = item.effectHandler(playable)
    #Apply to Globals
    Lori = quickListing[0]
    Lauren = quickListing[1]
    Marcus = quickListing[2]
    Julius = quickListing[3]

# Calculates and returns higher level stats (beyond level 10)
def higherLvlGenerator(character: PlayableCharacter, base: list, adder: list):
    # Holders
    newbase = []
    adderInt = []
    # Transfer base and adder to holders
    for stat in base:
        newbase.append(int(stat))
    newbase.pop(0)
    for stat in adder:
        adderInt.append(int(stat))
    adderInt.pop(0)
    # Iterate and as as we go.
    currentLvl = 9
    while character.level > currentLvl:
        adderCounter = 0
        for stat in newbase:
            stat = adderInt[adderCounter] + stat
            adderCounter += 1
        currentLvl += 1
    print(newbase) # Temporary
    # Apply and Return
    character.health = newbase[0]
    character.attack = newbase[1]
    character.defense = newbase[2]
    character.energyValue = newbase[3]
    return character


def explorer():
    global x
    global y
    global z
    global chapter
    global region
    global regionDisplay
    global Lori
    global Lauren
    global Julius
    global Marcus
    global locations
    global local
    global gold
    menu = GameMenu()
    characters = [Lori, Lauren, Julius, Marcus]
    menu.update(characters)
    print("x: " + str(x) + " y: " + str(y) + " z: " + str(z))
    print("gold: " + str(gold))
    if not local:
        selections = [4, 5, 6]
        print(regionDisplay + ":")
        print(regionDiscribe(region))
        for pair in AOEScanner(x, y, z, locations, region):
            print("You can see " + pair[0] + " in the " + pair[1])
    if local:
        selections = [4, 5, 6, 7]
        print(regionDisplay + ":")
        print(locationCheck(x, y, z, locations, region)[2])
    if regionCheck(x + 1, y, z) >= 0 and \
            (fetchRegionZ(regionCheck(x + 1, y, z)) - fetchRegionZ(region) <= 5 and
             fetchRegionZ(region) - fetchRegionZ(regionCheck(x + 1, y, z)) <= 5):
        selections.append(1)
    if regionCheck(x, y + 1, z) >= 0 and \
            (fetchRegionZ(regionCheck(x, y + 1, z)) - fetchRegionZ(region) <= 5 and
             fetchRegionZ(region) - fetchRegionZ(regionCheck(x, y + 1, z)) <= 5):
        selections.append(0)
    if regionCheck(x - 1, y, z) >= 0 and \
            (fetchRegionZ(regionCheck(x - 1, y, z)) - fetchRegionZ(region) <= 5 and
             fetchRegionZ(region) - fetchRegionZ(regionCheck(x - 1, y, z)) <= 5):
        selections.append(3)
    if regionCheck(x, y - 1, z) >= 0 and \
            (fetchRegionZ(regionCheck(x, y - 1, z)) - fetchRegionZ(region) <= 5 and
             fetchRegionZ(region) - fetchRegionZ(regionCheck(x, y - 1, z)) <= 5):
        selections.append(2)
    if 0 in selections:
        print("0: March north")
    if 1 in selections:
        print("1: March east")
    if 2 in selections:
        print("2: March south")
    if 3 in selections:
        print("3: March west")
    print("4: Party")
    print("5: Rest")
    print("6: Save")
    if local:
        print("7: Shop")
    playerChoice = inputAndCheck("Your Call: ", selections)
    if playerChoice == 0:
        y += 1
    if playerChoice == 1:
        x += 1
    if playerChoice == 2:
        y -= 1
    if playerChoice == 3:
        x -= 1
    if playerChoice == 4:
        os.system("cls")
        listing = menu.displayGameMenu()
        Checker = inputAndCheck("Inspect: ", listing)
        os.system("cls")
        if Checker < len(menu.PClist):
            itemAwsner = menu.displayPC(menu.PClist[Checker])
            itemAwsner = inputAndCheck("Use: ", itemAwsner)
            if itemAwsner < len(characters[Checker].inventory):
                characters[Checker].useItem(itemAwsner)

    if playerChoice == 5:
        characters = rest(characters, local)
        Lauren = characters[1]
        Lori = characters[0]
        Marcus = characters[2]
        Julius = characters[3]
    if playerChoice == 6:
        save(characters, x, y, z, chapter, gold)
    if playerChoice == 7:
        store = Shop()
        holder = store.storeRun(characters, gold)
        Lauren = holder[0][1]
        Lori = holder[0][0]
        Marcus = holder[0][2]
        Julius = holder[0][3]
        gold = holder[1]
        del store
    region = regionCheck(x, y, z)
    regionDisplay = fetchRegionDisplay(region)
    Checker = encounterCheck(region)
    if (Checker[0] == True):
        runCombat([Checker[1]], characters, region)
        generateCharacters()
    Checker = locationCheck(x, y, z, locations, region)  # list: [bool, list of locations, locationDisplay]
    local = Checker[0]
    locations = Checker[1]

    os.system("cls")


# Main Line Commands

# Initial Starting Game Stuff
bootSave(inputAndCheck("how would you like to boot? 0 New game or integer of save you are booting",
                       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
generateCharacters()
os.system("cls")

# Story Progress Checking
if chapter == 0:
    # New Game
    input("Opening")
    # Intialize Lauren (Lori is 1 by default)
    chapter += 1
    Lauren.level += 1
    # Setting up Characters
    generateCharacters()
    Lauren.currentHealth = Lauren.health
    Lori.currentEnergy = Lori.energyValue
    Lori.currentHealth = Lori.health
    Lauren.currentEnergy = Lauren.energyValue

# World Setup
region = regionCheck(x, y, z)
regionDisplay = fetchRegionDisplay(region)
Checker = locationCheck(x, y, z, locations, region)  # list: [bool, list of locations, locationDisplay]
local = Checker[0]
locations = Checker[1]
TestingCounter = 0  # temporary

# Game Loop
while chapter < 24:
    # the main game
    explorer()
    TestingCounter += 1  # temporary
    if TestingCounter == 3:  # temporary
        TestingCounter = 0
        chapter += 1  # temprorary
input("credits")
# Post Game Loop
chapter += 1
while chapter < 27:
    # the post game
    explorer()
input("credits and close")
input("Extra Data:" + str(x) + " " + str(y) + " " + str(z))
