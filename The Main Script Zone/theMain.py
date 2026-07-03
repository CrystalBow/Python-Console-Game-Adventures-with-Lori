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


def inventory_setup(inventory: list):
    item_fetcher = Shop()
    new_inventory = []
    for string in inventory:
        for item in item_fetcher.items:
            if item.name == string:
                new_inventory.append(item)
    return new_inventory


# Functions
# Extracting Save Data
def boot_save(save_num):
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
    if save_num == 0:
        # New Game, Load Data
        f = open("newGame.csv")
        f_reader = csv.reader(f)
        content = next(f_reader)
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
            f = open("save" + str(save_num) + ".csv")
            f_reader = csv.reader(f)
            content = next(f_reader)
            # Capture basic character data and story progress
            x = int(content[0])
            y = int(content[1])
            z = int(content[2])
            chapter = int(content[3])
            Lori.level = int(content[4])
            Lauren.level = int(content[5])
            Marcus.level = int(content[6])
            Julius.level = int(content[7])
            next(f_reader)
            # Capture inventories for each character
            content = next(f_reader)
            Lori.inventory = inventory_setup(content)
            next(f_reader)
            content = next(f_reader)
            Lauren.inventory = inventory_setup(content)
            next(f_reader)
            content = next(f_reader)
            Marcus.inventory = inventory_setup(content)
            next(f_reader)
            content = next(f_reader)
            Julius.inventory = inventory_setup(content)
            next(f_reader)
            # Collect gold and experience
            content = next(f_reader)
            gold = int(content[0])
            Lori.experience = int(content[1])
            Lauren.experience = int(content[2])
            Marcus.experience = int(content[3])
            Julius.experience = int(content[4])
            next(f_reader)
            # Record current values for HP and MP
            content = next(f_reader)
            Lori.currentHealth = int(content[0])
            Lauren.currentHealth = int(content[1])
            Marcus.currentHealth = int(content[2])
            Julius.currentHealth = int(content[3])
            next(f_reader)
            content = next(f_reader)
            Lori.currentEnergy = int(content[0])
            Lauren.currentEnergy = int(content[1])
            Marcus.currentEnergy = int(content[2])
            Julius.currentEnergy = int(content[3])
        except FileNotFoundError:
            # Try Again if not found.
            boot_save(inputAndCheck("how would you like to boot? 0 New game or integer of save you are booting",
                                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# region getters
# Fetches the z value
def fetch_region_z(region_id):
    file = open("regions.csv")
    file_reader = csv.reader(file)
    regions = []
    for line in file_reader:
        if not line:
            continue
        regions.append(line)
    file.close()
    return int(regions[region_id][7])

#Fetches the region name
def fetch_region_display(region_id):
    file = open("regions.csv")
    file_reader = csv.reader(file)
    regions = []
    for line in file_reader:
        if line == []:
            continue
        regions.append(line)
    file.close()
    return regions[region_id][1]

# Checks what region certain coordinates are on and return region information
def region_check(x, y, z):
    # Fetch region from file
    file = open("regions.csv")
    file_reader = csv.reader(file)
    target_region = -1
    regions = []
    for line in file_reader:
        regions.append(line)
    file.close()
    # look over regions for valid one
    for line in regions:
        if line == []:
            continue
        if ((int(line[2]) <= x) and (int(line[3]) >= x)) and ((int(line[4]) <= y) and (int(line[5]) >= y)):
            target_region = int(line[0])
            break

    return target_region


def region_discribe(region_id):
    file = open("descriptions.csv")
    file_reader = csv.reader(file)
    regions = []
    for line in file_reader:
        if line == []:
            continue
        regions.append(line)
    file.close()
    choice = int(random.random() * 10)
    while choice >= len(regions[region_id]):
        choice = int(random.random() * 10)
    return regions[region_id][choice]


def save(characters, x, y, z, ch, gp):
    choice = inputAndCheck("What file would you like to save too? ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    os.system("type nul > save" + str(choice) + ".csv")
    f = open("save" + str(choice) + ".csv", "w")
    f_writer = csv.writer(f)
    row = [x, y, z, ch]
    rows = []
    for playable in characters:
        row.append(playable.level)
    rows.append(row)
    for playable in characters:
        row = []
        for item in playable.inventory:
            row.append(item.name)
        rows.append(row)
    row = [gp]
    for playable in characters:
        row.append(playable.experience)
    rows.append(row)
    row = []
    for playable in characters:
        row.append(playable.currentHealth)
    rows.append(row)
    row = []
    for playable in characters:
        row.append(playable.currentEnergy)
    rows.append(row)
    row = []
    for playable in characters:
        row.append(playable.experience)
    rows.append(row)
    f_writer.writerows(rows)
    f.close()
    choice = inputAndCheck("Would you like to keep playing? (1: Yes, 0: No) ", [0, 1])
    if choice == 0:
        exit()


def rest(charecters, local):
    updated_characters = []
    if local:
        for wifu in charecters:
            wifu.currentHealth = wifu.health
            wifu.currentEnergy = wifu.energyValue
            updated_characters.append(wifu)
    else:
        for wifu in charecters:
            if wifu.level == 0:
                updated_characters.append(wifu)
                continue
            luck = int(random.random() * 10)
            wifu.currentHealth = wifu.currentHealth + luck
            wifu.currentEnergy = wifu.currentEnergy + luck
            if wifu.currentHealth > wifu.health:
                wifu.currentHealth = wifu.health
            if wifu.currentEnergy > wifu.energyValue:
                wifu.currentEnergy = wifu.energyValue
            updated_characters.append(wifu)
    return updated_characters


def encounter_check(region_id):
    f = open("encounters.csv")
    roll = int(random.random() * 100)
    reader = csv.reader(f)
    possible_fights = []
    for region in reader:
        if region == []:
            continue
        possible_fights.append(region)
    f.close()
    if int(possible_fights[region_id][0]) > roll:
        return [False]
    up = 2
    down = 0
    for fight in possible_fights[region_id]:
        try:
            int(fight)
            continue
        except ValueError:
            try:
                if int(possible_fights[region_id][down]) < roll < int(possible_fights[region_id][up]):
                    return [True, fight]
                else:
                    up += 2
                    down += 2
            except IndexError:
                return [True, possible_fights[region_id][len(possible_fights[region_id]) - 1]]
    return [False]


def run_combat(intial_badie, wifus, location):
    global gold
    input("fight!")
    # temporary^^
    the_battle = Combat()
    enemy_catalog = []
    post_battle_wifus = []
    for ally in wifus:
        the_battle.intiativeRoll(ally)
    f = open("monsterStats.csv")
    f_reader = csv.reader(f)
    for line in f_reader:
        if line == []:
            continue
        enemy_catalog.append(line)
    for badie in intial_badie:
        for enemy in enemy_catalog:
            if badie == enemy[0]:
                the_battle.intiativeRoll(
                    Monster(attack=int(enemy[2]), health=int(enemy[1]), defense=int(enemy[3]), displayName=badie,
                            experince=int(enemy[7]), petRate=int(enemy[4]), buddyRate=int(enemy[5]), weapon=enemy[6]))
    the_battle.foePrep()
    the_battle.combatantOrganizer()
    while the_battle.continueStatus:
        for fighter in the_battle.order:
            the_battle.turn(the_battle.listing[fighter[0]])
            the_battle.listing[fighter[0]].deathCheck()
            the_battle.continueStatus = the_battle.combatEndCheck()
            if not the_battle.continueStatus:
                break
            os.system("cls")
    checker = 0
    for fighter in the_battle.listing:
        if isinstance(the_battle.listing[fighter], PlayableCharacter):
            the_battle.listing[fighter].experience = the_battle.listing[fighter].experience + the_battle.exp
            gold = gold + the_battle.exp
            if the_battle.listing[fighter].currentHealth > 0:
                checker += 1
            post_battle_wifus.append(the_battle.listing[fighter])
    if checker == 0:
        input("GAME OVER")
        exit()
    del the_battle
    return post_battle_wifus


def aoe_scanner(x, y, z, locals, region_id):
    finds = []
    scan = locationCheck(x + 1, y, z, locals, region_id)
    if scan[0]:
        finds.append([scan[2], "east"])
    scan = locationCheck(x + 1, y + 1, z, locals, region_id)
    if scan[0]:
        finds.append([scan[2], "north east"])
    scan = locationCheck(x + 1, y - 1, z, locals, region_id)
    if scan[0]:
        finds.append([scan[2], "south east"])
    scan = locationCheck(x - 1, y, z, locals, region_id)
    if scan[0]:
        finds.append([scan[2], "west"])
    scan = locationCheck(x - 1, y + 1, z, locals, region_id)
    if scan[0]:
        finds.append([scan[2], "north west"])
    scan = locationCheck(x - 1, y - 1, z, locals, region_id)
    if scan[0]:
        finds.append([scan[2], "south west"])
    scan = locationCheck(x, y + 1, z, locals, region_id)
    if scan[0]:
        finds.append([scan[2], "north"])
    scan = locationCheck(x, y - 1, z, locals, region_id)
    if scan[0]:
        finds.append([scan[2], "south"])
    return finds


def locationCheck(x, y, z, locals, region_id):
    areas = []
    for place in locals:
        if x == place.x and y == place.y and z == place.z:
            return [True, locals, place.displayName]
    if region_id == 0:
        f = open("larmenPlains.csv")
        file_reader = csv.reader(f)
        for line in file_reader:
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
    elif region_id == 1:
        return [False, locals]
    elif region_id == 2:
        return [False, locals]
    elif region_id == 3:
        f = open("desert3.csv")
        file_reader = csv.reader(f)
        for line in file_reader:
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
    elif region_id == 4:
        f = open("ruinedPlateau.csv")
        file_reader = csv.reader(f)
        for line in file_reader:
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
    elif region_id == 5:
        f = open("theDeathLands.csv")
        file_reader = csv.reader(f)
        for line in file_reader:
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
    elif region_id == 6:
        f = open("gobbiMontains.csv")
        file_reader = csv.reader(f)
        for line in file_reader:
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
    elif region_id == 7:
        f = open("drameKingdom.csv")
        file_reader = csv.reader(f)
        for line in file_reader:
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
    elif region_id == 8:
        f = open("miniPlatPen.csv")
        file_reader = csv.reader(f)
        for line in file_reader:
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
    elif region_id == 9:
        f = open("kingdomOfJavi.csv")
        file_reader = csv.reader(f)
        for line in file_reader:
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
    elif region_id == 10:
        f = open("igachiPlain.csv")
        file_reader = csv.reader(f)
        for line in file_reader:
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
    # Establish arrays to hold stat lines and team_list
    garbage = 0
    stat_line = []
    lvl_counter = 0
    adder_line = []
    team_list = [Lori, Lauren, Marcus, Julius]
    # Level up check
    for wifu in team_list:
        levelpoint = wifu.level * 11
        if wifu.level > 0:
            if wifu.experience >= levelpoint:
                print("level up!")
                wifu.level += 1
                wifu.experience = 0
    #Apply Level ups
    Lori = team_list[0]
    Lauren = team_list[1]
    Marcus = team_list[2]
    Julius = team_list[3]
    # Apply Stats (10 and lower are predetermined. Higher is just scale)
    if Lori.level < 10:
        #Lori Predetermined
        file = open("lori.csv")
        file_reader = csv.reader(file)
        #Setup
        Lori.skills = list(next(file_reader))
        Lori.skillCosts = []
        Lori.energyName = Lori.skills[0]
        Lori.skills.pop(0)
        # fetch data
        garbage = next(file_reader)
        string_costs = next(file_reader)
        for row in file_reader:
            if row == []:
                pass
            else:
                stat_line = row
                try:
                    lvl_counter = int(stat_line[0])
                    if lvl_counter == Lori.level:
                        break
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Apply Data
        Lori.health = int(stat_line[1])
        Lori.attack = int(stat_line[2])
        Lori.defense = int(stat_line[3])
        Lori.energyValue = int(stat_line[4])
        for stuff in string_costs:
            garbage = int(stuff)
            Lori.skillCosts.append(garbage)
        Lori.skillCosts.pop(0)
    else:
        # Scaling Level ups
        done_flag = False
        file = open("Lori.csv")
        file_reader = csv.reader(file)
        Lori.skills = list(next(file_reader))
        Lori.skillCosts = []
        Lori.energyName = Lori.skills[0]
        Lori.skills.pop(0)
        garbage = next(file_reader)
        string_costs = next(file_reader)
        # Fetch
        for row in file_reader:
            if row == []:
                pass
            else:
                if not done_flag:
                    stat_line = row
                else:
                    adder_line = row
                try:
                    lvl_counter = int(stat_line[0])
                    if lvl_counter == 9:
                        if done_flag:
                            break
                        done_flag = True
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Pass to generator
        Lori = higher_lvl_generator(Lori, stat_line, adder_line)
        # Apply skill costs (they don't scale)
        for stuff in string_costs:
            garbage = int(stuff)
            Lori.skillCosts.append(garbage)
        Lori.skillCosts.pop(0)
    # Lauren level ups
    if Lauren.level < 10 and Lauren.level > 0:
        # Predetermined Levels
        file = open("lauren.csv")
        file_reader = csv.reader(file)
        Lauren.skills = next(file_reader)
        Lauren.energyName = Lauren.skills[0]
        Lauren.skillCosts = []
        Lauren.skills.pop(0)
        # Fetch
        garbage = next(file_reader)
        string_costs = next(file_reader)
        for row in file_reader:
            if row == []:
                pass
            else:
                stat_line = row
                try:
                    lvl_counter = int(stat_line[0])
                    if lvl_counter == Lauren.level:
                        break
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Apply
        Lauren.health = int(stat_line[1])
        Lauren.attack = int(stat_line[2])
        Lauren.defense = int(stat_line[3])
        Lauren.energyValue = int(stat_line[4])
        for stuff in string_costs:
            garbage = int(stuff)
            Lauren.skillCosts.append(garbage)
        Lauren.skillCosts.pop(0)
    else:
        # Scaling levels
        done_flag = False
        file = open("lauren.csv")
        file_reader = csv.reader(file)
        Lauren.skills = next(file_reader)
        Lauren.energyName = Lauren.skills[0]
        Lauren.skillCosts = []
        Lauren.skills.pop(0)
        # Fetch
        garbage = next(file_reader)
        string_costs = next(file_reader)
        for row in file_reader:
            if row == []:
                pass
            else:
                if not done_flag:
                    stat_line = row
                else:
                    adder_line = row
                try:
                    lvl_counter = int(stat_line[0])
                    if lvl_counter == 9:
                        if done_flag:
                            break
                        done_flag = True
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Pass to generator
        Lauren = higher_lvl_generator(Lauren, stat_line, adder_line)
        # Applying Skill Costs
        for stuff in string_costs:
            garbage = int(stuff)
            Lauren.skillCosts.append(garbage)
        Lauren.skillCosts.pop(0)
    # Julius Time
    if Julius.level < 10 and Julius.level > 0:
        # Predetermined Levels
        file = open("julius.csv")
        file_reader = csv.reader(file)
        Julius.skills = next(file_reader)
        Julius.skillCosts = []
        Julius.energyName = Julius.skills[0]
        Julius.skills.pop(0)
        # Fetch
        garbage = next(file_reader)
        string_costs = next(file_reader)
        for row in file_reader:
            if row == []:
                pass
            else:
                stat_line = row
                try:
                    lvl_counter = int(stat_line[0])
                    if lvl_counter == Julius.level:
                        break
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Apply
        Julius.health = int(stat_line[1])
        Julius.attack = int(stat_line[2])
        Julius.defense = int(stat_line[3])
        Julius.energyValue = int(stat_line[4])
        for stuff in string_costs:
            garbage = int(stuff)
            Julius.skillCosts.append(garbage)
        Julius.skillCosts.pop(0)
    elif Julius.level > 0:
        # Scaling levels
        done_flag = False
        file = open("julius.csv")
        file_reader = csv.reader(file)
        Julius.skills = next(file_reader)
        Julius.skillCosts = []
        Julius.energyName = Julius.skills[0]
        Julius.skills.pop(0)
        garbage = next(file_reader)
        string_costs = next(file_reader)
        for row in file_reader:
            if row == []:
                pass
            else:
                if not done_flag:
                    stat_line = row
                else:
                    adder_line = row
                try:
                    lvl_counter = int(stat_line[0])
                    if lvl_counter == 9:
                        if done_flag:
                            break
                        done_flag = True
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Pass to Generator
        Julius = higher_lvl_generator(Julius, stat_line, adder_line)
        # Apply skill costs
        for stuff in string_costs:
            garbage = int(stuff)
            Julius.skillCosts.append(garbage)
        Julius.skillCosts.pop(0)
    if Marcus.level < 10 and Marcus.level > 0:
        # Predetermined Levels
        file = open("marcus.csv")
        file_reader = csv.reader(file)
        Marcus.skills = next(file_reader)
        Marcus.skillCosts = []
        Marcus.energyName = Marcus.skills[0]
        Marcus.skills.pop(0)
        # Fetch
        garbage = next(file_reader)
        string_costs = next(file_reader)
        for row in file_reader:
            if row == []:
                pass
            else:
                stat_line = row
                try:
                    lvl_counter = int(stat_line[0])
                    if lvl_counter == Marcus.level:
                        break
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Apply
        Marcus.health = int(stat_line[1])
        Marcus.attack = int(stat_line[2])
        Marcus.defense = int(stat_line[3])
        Marcus.energyValue = int(stat_line[4])
        for stuff in string_costs:
            garbage = int(stuff)
            Marcus.skillCosts.append(garbage)
        Marcus.skillCosts.pop(0)
    elif Marcus.level > 0:
        # Scaling Levels
        done_flag = False
        file = open("marcus.csv")
        file_reader = csv.reader(file)
        Marcus.skills = next(file_reader)
        Marcus.skillCosts = []
        Marcus.energyName = Marcus.skills[0]
        Marcus.skills.pop(0)
        # Fetch
        garbage = next(file_reader)
        string_costs = next(file_reader)
        for row in file_reader:
            if row == []:
                pass
            else:
                if not done_flag:
                    stat_line = row
                else:
                    adder_line = row
                try:
                    lvl_counter = int(stat_line[0])
                    if lvl_counter == 9:
                        if done_flag:
                            break
                        done_flag = True
                    else:
                        pass
                except ValueError:
                    pass
        file.close()
        # Pass to generator
        Marcus = higher_lvl_generator(Marcus, stat_line, adder_line)
        # Apply Skill Costs
        for stuff in string_costs:
            garbage = int(stuff)
            Marcus.skillCosts.append(garbage)
        Marcus.skillCosts.pop(0)

    # Inventory Setup
    quick_listing = [Lori, Lauren, Marcus, Julius]
    for playable in quick_listing:
        for item in playable.inventory:
            # For Each Item
            playable = item.effectHandler(playable)
    #Apply to Globals
    Lori = quick_listing[0]
    Lauren = quick_listing[1]
    Marcus = quick_listing[2]
    Julius = quick_listing[3]

# Calculates and returns higher level stats (beyond level 10)
def higher_lvl_generator(character: PlayableCharacter, base: list, adder: list):
    # Holders
    new_base = []
    adder_int = []
    # Transfer base and adder to holders
    for stat in base:
        new_base.append(int(stat))
    new_base.pop(0)
    for stat in adder:
        adder_int.append(int(stat))
    adder_int.pop(0)
    # Iterate and as as we go.
    current_lvl = 9
    while character.level > current_lvl:
        adder_counter = 0
        for stat in new_base:
            stat = adder_int[adder_counter] + stat
            adder_counter += 1
        current_lvl += 1
    print(new_base) # Temporary
    # Apply and Return
    character.health = new_base[0]
    character.attack = new_base[1]
    character.defense = new_base[2]
    character.energyValue = new_base[3]
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
    selections = []
    if not local:
        selections = [4, 5, 6]
        print(regionDisplay + ":")
        print(region_discribe(region))
        for pair in aoe_scanner(x, y, z, locations, region):
            print("You can see " + pair[0] + " in the " + pair[1])
    if local:
        selections = [4, 5, 6, 7]
        print(regionDisplay + ":")
        print(locationCheck(x, y, z, locations, region)[2])
    if region_check(x + 1, y, z) >= 0 and \
            (fetch_region_z(region_check(x + 1, y, z)) - fetch_region_z(region) <= 5 and
             fetch_region_z(region) - fetch_region_z(region_check(x + 1, y, z)) <= 5):
        selections.append(1)
    if region_check(x, y + 1, z) >= 0 and \
            (fetch_region_z(region_check(x, y + 1, z)) - fetch_region_z(region) <= 5 and
             fetch_region_z(region) - fetch_region_z(region_check(x, y + 1, z)) <= 5):
        selections.append(0)
    if region_check(x - 1, y, z) >= 0 and \
            (fetch_region_z(region_check(x - 1, y, z)) - fetch_region_z(region) <= 5 and
             fetch_region_z(region) - fetch_region_z(region_check(x - 1, y, z)) <= 5):
        selections.append(3)
    if region_check(x, y - 1, z) >= 0 and \
            (fetch_region_z(region_check(x, y - 1, z)) - fetch_region_z(region) <= 5 and
             fetch_region_z(region) - fetch_region_z(region_check(x, y - 1, z)) <= 5):
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
    player_choice = inputAndCheck("Your Call: ", selections)
    if player_choice == 0:
        y += 1
    if player_choice == 1:
        x += 1
    if player_choice == 2:
        y -= 1
    if player_choice == 3:
        x -= 1
    if player_choice == 4:
        os.system("cls")
        listing = menu.displayGameMenu()
        checker = inputAndCheck("Inspect: ", listing)
        os.system("cls")
        if checker < len(menu.PClist):
            item_awsner = menu.displayPC(menu.PClist[checker])
            item_awsner = inputAndCheck("Use: ", item_awsner)
            if item_awsner < len(characters[checker].inventory):
                characters[checker].useItem(item_awsner)

    if player_choice == 5:
        characters = rest(characters, local)
        Lauren = characters[1]
        Lori = characters[0]
        Marcus = characters[2]
        Julius = characters[3]
    if player_choice == 6:
        save(characters, x, y, z, chapter, gold)
    if player_choice == 7:
        store = Shop()
        holder = store.storeRun(characters, gold)
        Lauren = holder[0][1]
        Lori = holder[0][0]
        Marcus = holder[0][2]
        Julius = holder[0][3]
        gold = holder[1]
        del store
    region = region_check(x, y, z)
    regionDisplay = fetch_region_display(region)
    checker = encounter_check(region)
    if (checker[0] == True):
        run_combat([checker[1]], characters, region)
        generateCharacters()
    checker = locationCheck(x, y, z, locations, region)  # list: [bool, list of locations, locationDisplay]
    local = checker[0]
    locations = checker[1]

    os.system("cls")


# Main Line Commands

# Initial Starting Game Stuff
boot_save(inputAndCheck("how would you like to boot? 0 New game or integer of save you are booting",
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
region = region_check(x, y, z)
regionDisplay = fetch_region_display(region)
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
