#!/usr/bin/env python
import os
import csv

# descriptions.csv
os.system("type nul > descriptions.csv")
f = open("descriptions.csv", "w")
fwrite = csv.writer(f)
descriptions = [
    ["Tall grass is all around you, it sways with the wind...",
     "There are pretty flowers that stand out among the tall grass...",
     "It's hard to see the puddles in the tall grass, your boots are wet..."],
    ["The land rises here, the grass is short and rocks poke out throughout...",
     "The incline makes traveling more difficult, more rests may be needed...",
     "It's getting colder the higher you go, you can faintly see snow on occasion"],
    ["Sand for miles on end... In the east you can see the ruined plateau...",
     "Sand for miles on end... the sun is as oppressive as ever...",
     "The desert wind blows... some sand goes into your eye"],
    ["there are sand dunes all around, and wait... is that a sand worm over there?!?!?",
     "A sand storm... all you see is sand",
     "Sand dunes all around, and you think that something is moving under the sand..."],
    ["The beautiful snow and trees. It's breath taking!", "An orc seems to have built a snow man here",
     "Old weapons can be found stuck in the snow",
     "The lights reelection in the snow glimmers like a shining ray of hope",
     "Snow fields and evergreens it's nice and quiet"],
    ["The hot steppe doesn't let up! gotta keep walking!",
     "Dry grass, its a symbol of death, it's probably how this land got its name",
     "There's a pile of bones nearby. you can also see a rotting course as well"],
    ["This land has a lot of steep slopes and a lot of stone all around.",
     "A destroyed Goblin farm. Probably raided by a rival goblin clan.",
     "A battle field.. one of many on this mountain"],
    ["Sheep's graze, a shepherd waves at you.", "you see farmers working. One waves at you.",
     "The fields roll up and down. They shine a bright green.",
     "A fort! oh wait, it's an abandoned and only half standing."],
    ["The land is scorched here. you can see caves in the ground that probably lead to dragon dens"],
    ["Flat lands and grass. there is a forest not far off.", "Trees of the forest, with mushrooms and bunnies",
     "A deer saw you and ran away. The party is now alone in the forest.",
     "There's a grazing herd of cows nearby, best leave them alone",
     "The flat green plains let you see all around. you're walking passed what used to be a campfire"],
    ["Lots of farms! the population must be massive",
     "Was that a samurai bunny? Anyway, your passing through an abandoned training ground",
     "A duel took place here. you can tell because there's a single body with a sword wound in it",
     "Dense bushes make it hard to see what is ahead of you. You'll need to get on someone's shoulders."]
]
for qoute in descriptions:
    fwrite.writerow(qoute)
f.close()

# encounters.csv
os.system("type nul > encounters.csv")
f = open("encounters.csv", "w")
fwrite = csv.writer(f)
battles = [
    # encounter min, monster name. Index is equal to region ID
    [30, "Veteran Rouge", 36, "Mage", 51, "Giant Wolf", 61, "Exiled Squire", 71, "Veteran Thug", 81, "Shambling Moss"],
    [36, "Orc", 61, "Warrior", 71, "Veteran Orc", 81, "Master Bandit"],
    [25, "Snake", 51, "Sand Elemental", 61, "Traveling Swordsman", 71, "Master Thief", 81, "Fire Mage"],
    [15, "Crazed Prophet", 26, "Survivor", 61, "Warrior in Training", 76, "Desert Hounds", 91, "Sand Worms"],
    [31, "Master Rouge", 52, "Master Thug", 61, "Giant Dire Wolf", 71, "Elite Orc", 81, "Master Ronin", 91, "Orc Boss"],
    [36, "Veteran Bandit", 61, "Zombie", 71, "Skeleton", 81, "Necromancy Fanatic", 91, "Necromancer"],
    [41, "Wyvern", 61, "Goblin", 86, "Goblin Squire", 96, "Goblin Knight"],
    [46, "Thug", 61, "Wannabe Squire", 71, "Veteran Thief", 91, "Dire Wolf"],
    [10, "Young Dragon", 71, "Adult Dragon", 91, "Ancient Dragon"],
    [56, "Thief", 65, "Dire Cat", 71, "Wolf", 81, "Bandit", 86, "Cultist"],
    [61, "Rouge", 71, "Mage Apprentice", 51, "Living Shrub", 61, "Slime", 81, "Ronin", 96, "Experienced Ronin"]
]
for region in battles:
    fwrite.writerow(region)
f.close()

# items.csv
os.system("type nul > items.csv")
f = open("items.csv", "w")
fwrite = csv.writer(f)
items = [
    # Name, cost, effect, effectValue
    ["Combat Padding", 200, "Def", 1],
    ["Whet Stone", 1000, "AtkPhy", 10],
    ["Crystal Ball", 1500, "AtkMag", 10],
    ["Breast Plate", 1000, "Def", 5],
    ["Full Plate", 4000, "Def", 20],
    ["Leather Armor", 600, "Def", 3],
    ["Half-plate", 2000, "Def", 10],
    ["Salve", 1, "hp", 5],
    ["Potion", 3, "hp", 10],
    ["Soothing Salve", 5, "hp", 10],
    ["Soothing Potion", 15, "hp", 20],
    ["Healing Salve", 15, "hp", 15],
    ["Healing Potion", 45, "hp", 30],
    ["Restoring Salve", 25, "hp", 20],
    ["Restoring Potion", 75, "hp", 60],
    ["Divine Salve", 40, "hp", 25],
    ["Divine Potion", 120, "hp", 75]
]
for item in items:
    fwrite.writerow(item)
f.close()

# pets.csv
os.system("type nul > pets.csv")
f = open("pets.csv", "w")
fwrite = csv.writer(f)
buddies = [
    [9, "Dire Cat", "Wolf"],
    [10, "Living Shrub", "Slime"],
    [7, "Dire Wolf"],
    [6, "Wyvern"],
    [5, "Zombie", "Skeleton"],
    [0, "Giant Wolf"],
    [2, "Snake", "Sand Elemental"],
    [3, "Desert Hound"],
    [4, "Giant Dire Wolf"]
]
for buddy in buddies:
    fwrite.writerow(buddy)
f.close()

# monsterStats.csv
os.system("type nul > monsterStats.csv")
f = open("monsterStats.csv", "w")
fwrite = csv.writer(f)
baddies = [
    # Name, Hp, Atk, Def, pets, friends, weapon, exp, pet?
    ["Thief", 6, 2, 1, 50, -1, "Dagger", 1],
    ["Dire Cat", 6, 3, 0, -1, 50, "Claw", 1],
    ["Wolf", 7, 3, 1, -1, 50, "Fangs", 1],
    ["Bandit", 10, 4, 2, -1, 50, "Short Sword", 1],
    ["Cultist", 7, 5, 1, 20, 20, "Short Sword", 1],
    ["Rouge", 7, 6, 1, 30, -1, "Rapier", 1],
    ["Mage Apprentice", 10, 7, 1, 30, 30, "Fire Bolt", 1],
    ["Living Shrub", 7, 3, 2, -1, 30, "Sharp Stick", 1],
    ["Ronin", 10, 6, 4, 30, 30, "Katana", 1],
    ["Slime", 6, 3, 1, -1, 80, "Body", 1],
    ["Experienced Ronin", 15, 7, 4, 50, -1, "Katana", 2],
    ["Thug", 10, 6, 5, 25, 25, "Mace", 2],
    ["Wannabe Squire", 10, 5, 6, 40, 40, "Short Sword", 2],
    ["Veteran Thief", 11, 7, 6, 40, -1, "Short Sword", 3],
    ["Dire Wolf", 12, 8, 6, -1, 40, "Fangs", 3],
    ["Wyvern", 12, 8, 6, -1, 60, "Dragon Claws", 3],
    ["Goblin", 7, 4, 4, 12, 12, "Short Sword", 4],
    ["Goblin Squire", 10, 5, 5, 18, 18, "Spear", 4],
    ["Goblin Knight", 10, 5, 7, 35, 35, "Spear", 4],
    ["Veteran Bandit", 15, 9, 7, 25, 25, "War Hammer", 5],
    ["Zombie", 15, 3, 7, -1, 40, "Fist", 4],
    ["Skeleton", 6, 15, 2, -1, 60, "Short Sword", 4],
    ["Necromancy Fanatic", 12, 10, 6, 20, 20, "Short Sword", 5],
    ["Necromancer", 15, 12, 6, 10, -1, "Dark Bolt", 6],
    ["Veteran Rouge", 12, 11, 6, 20, -1, "Rapier", 5],
    ["Mage", 15, 15, 6, 70, -1, "Thunder Bolt", 6],
    ["Giant Wolf", 17, 13, 11, -1, 60, "Fangs", 7],
    ["Exiled Squire", 15, 10, 11, 90, -1, "Long Sword", 7],
    ["Veteran Thug", 15, 11, 10, 20, 20, "Great Sword", 8],
    ["Shambling Moss", 12, 8, 7, -1, 40, "Thorn Fist", 6],
    ["Snake", 10, 21, 1, -1, 90, "Fangs", 6],
    ["Sand Elemental", 15, 12, 12, -1, 90, "Sand", 7],
    ["Traveling Swordsman", 15, 13, 8, 60, -1, "Long Sword", 7],
    ["Master Thief", 16, 12, 11, 80, -1, "Short Sword", 8],
    ["Fire Mage", 15, 18, 3, 50, -1, "Fire Ball", 6],
    ["Crazed Prophet", 1, 32, 1, -1, 90, "Shadow Bolt", 7],
    ["Survivor", 30, 8, 8, 35, 35, "Long Sword", 6],
    ["Warrior in Training", 20, 12, 8, 70, -1, "Great Sword", 8],
    ["Desert Hound", 10, 15, 8, -1, 50, "Fangs", 7],
    ["Sand Worm", 50, 9, 9, -1, 100, "Giant Fangs", 9],
    ["Orc", 20, 10, 10, -1, 50, "Great Axe", 8],
    ["Warrior", 25, 17, 13, -1, 60, "Great Sword", 9],
    ["Veteran Orc", 25, 15, 15, -1, 70, "Great Axe", 9],
    ["Master Bandit", 20, 14, 12, -1, 80, "Great Axe", 8],
    ["Master Rouge", 17, 16, 11, 20, -1, "Rapier", 9],
    ["Giant Dire Wolf", 22, 18, 16, -1, 60, "Giant Fangs", 10],
    ["Elite Orc", 30, 20, 20, -1, 80, "Long Sword", 11],
    ["Master Ronin", 25, 17, 14, 40, -1, "Katana", 10],
    ["Orc Boss", 35, 25, 25, 20, -1, "Long Sword", 12],
    ["Young Dragon", 50, 20, 20, -1, 90, "Dragon Claw", 13],
    ["Adult Dragon", 50, 25, 25, -1, 90, "Dragon Claw", 14],
    ["Ancient Dragon", 100, 25, 25, -1, 90, "Dragon Claw", 15]
]
for monster in baddies:
    fwrite.writerow(monster)
f.close()

# newGame.csv recource
os.system("type nul > newGame.csv")
f = open("newGame.csv", "w")
fwrite = csv.writer(f)
newGame = [150, 50, 0, 0, 1, 0, 0, 0]
fwrite.writerow(newGame)
f.close()

# larmenPlains.csv
os.system("type nul > larmenPlains.csv")
f = open("larmenPlains.csv", "w")
fwrite = csv.writer(f)
regionLocation = [
    # Name, x, y, z, townStatus
    ["Drame Settlement", 2, 2, 0, 1],
    ["Ruined City", 20, 10, 0, 0],
    ["Gobbi Settlement", 30, 15, 1]
]
for location in regionLocation:
    fwrite.writerow(location)
f.close()

# desert3.csv
os.system("type nul > desert3.csv")
f = open("desert3.csv", "w")
fwrite = csv.writer(f)
regionLocation = [
    # Name, x, y, z, townStatus
    ["Forgotten Oasis", 10, 95, 0, 1]
]
for location in regionLocation:
    fwrite.writerow(location)
f.close()

# theDreathLands.csv
os.system("type nul > theDeathLands.csv")
f = open("theDeathLands.csv", "w")
fwrite = csv.writer(f)
regionLocation = [
    # Name, x, y, z, townStatus
    ["Larmen Oasis", 43, 4, 0, 1],
    ["Ohio Oasis", 101, 20, 0, 1],
    ["Drame Oasis", 170, 34, 0, 1],
    ["Gobbi Oasis", 168, 4, 0, 1]
]
for location in regionLocation:
    fwrite.writerow(location)
f.close()

# gobbiMontains.csv
os.system("type nul > gobbiMontains.csv")
f = open("gobbiMontains.csv", "w")
fwrite = csv.writer(f)
regionLocation = [
    # Name, x, y, z, townStatus
    ["Drame Anit-Gob Fort", 186, 9, 0, 1],
    ["Gob Trade Outpost", 176, 3, 0, 1],
    ["Gob King's Lair", 30, 15, 15, 0]
]
for location in regionLocation:
    fwrite.writerow(location)
f.close()

# drameKingdom.csv
os.system("type nul > drameKingdom.csv")
f = open("drameKingdom.csv", "w")
fwrite = csv.writer(f)
regionLocation = [
    # Name, x, y, z, townStatus
    ["Kline Town", 185, 20, 0, 1],
    ["Alex Town", 188, 25, 0, 1],
    ["Remiy Temple", 176, 39, 0, 0],
    ["Marcelo Village", 181, 42, 0, 1],
    ["Barnesha Town", 188, 40, 0, 1],
    ["John Village", 190, 30, 0, 1],
    ["Melanie Village", 190, 24, 0, 1],
    ["Fort Kyle", 190, 15, 0, 1],
    ["Javi/Drame Outpost", 192, 46, 0, 1],
    ["Josh Town", 195, 42, 0, 1],
    ["Drame Castle", 190, 30, 0, 1]
]
for location in regionLocation:
    fwrite.writerow(location)
f.close()

# ruinedPlateau.csv
os.system("type nul > ruinedPlateau.csv")
f = open("ruinedPlateau.csv", "w")
fwrite = csv.writer(f)
regionLocation = [
    # Name, x, y, z, townStatus
    ["West Seal", 110, 46, 20, 0],
    ["South Seal", 129, 40, 20, 0],
    ["East Seal", 149, 46, 20, 0],
    ["North Seal", 129, 84, 20, 0],
    ["Castle of Ruin", 129, 46, 0, 0]
]
for location in regionLocation:
    fwrite.writerow(location)
f.close()

# MiniPlatPen.csv
os.system("type nul > miniPlatPen.csv")
f = open("miniPlatPen.csv", "w")
fwrite = csv.writer(f)
regionLocation = [
    # Name, x, y, z, townStatus
    ["Elder Cave", 162, 44, 20, 0]
]
for location in regionLocation:
    fwrite.writerow(location)
f.close()

# kingdomOfJavi.csv
os.system("type nul > kingdomOfJavi.csv")
f = open("kingdomOfJavi.csv", "w")
fwrite = csv.writer(f)
regionLocation = [
    # Name, x, y, z, townStatus
    ["Church of Light", 152, 60, 0, 1],
    ["Light Way Village", 160, 62, 0, 1],
    ["New Nevran City", 158, 54, 0, 1],
    ["Javi Outpost North West", 160, 65, 0, 1],
    ["Bronze Village", 172, 55, 0, 1],
    ["Javi Outpost South", 182, 54, 0, 1],
    ["Javi City", 182, 62, 0, 1],
    ["Sword's Glint", 174, 65, 0, 0],
    ["Javi/Igachi Trade Post", 182, 66, 0, 1]
]
for location in regionLocation:
    fwrite.writerow(location)
f.close()

# igachiPlain.csv
os.system("type nul > igachiPlain.csv")
f = open("igachiPlain.csv", "w")
fwrite = csv.writer(f)
regionLocation = [
    # Name, x, y, z, townStatus
    ["Igachi High Fort", 155, 95, 0, 1],
    ["Watachi Village", 15, 77, 0, 1],
    ["Koi Town", 160, 82, 0, 1],
    ["Katana Village", 168, 80, 0, 1],
    ["Warrior City", 172, 85, 0, 1],
    ["Igachi Central Fort", 170, 85, 0, 1],
    ["Igachi Low Watch Tower", 160, 75, 0, 1],
    ["Igachi Low Fort", 180, 75, 0, 1],
    ["Igachi Palace", 190, 96, 0, 1],
    ["Sakara Village", 200, 82, 0, 1]
]
for location in regionLocation:
    fwrite.writerow(location)
f.close()



os.system("type nul > regions.csv")
f = open("regions.csv", "w")
fwrite = csv.writer(f)
regions = [[0, "Larmen Plains", 0, 40, 0, 20, 0, 0], [1, "the Rise", 21, 40, 21, 39, 0, 20],
           [2, "the Desert South", 0, 20, 21, 84, 0, 0], [3, "the Desert North", 0, 149, 85, 100, 0, 0],
           [4, "Ruined Plateau", 21, 149, 40, 84, 20, 20], [5, "the Death Lands", 41, 175, 0, 39, 0, 4],
           [6, "Goblin Montain", 176, 200, 0, 10, 2, 20], [7, "Drame Kingdom", 176, 200, 11, 47, 0, 4],
           [8, "Mini Plateau", 150, 175, 40, 49, 20, 20], [9, "Kindom of Javi", 150, 200, 50, 70, 0, 0],
           [10, "Igachi Plain", 150, 200, 71, 100, 0, 0]]
for region in regions:
    fwrite.writerow(region)
f.close()

# character csvs
# Lori
os.system("type nul > lori.csv")
f = open("lori.csv", "w")
fwrite = csv.writer(f)
loriAblities = ["Stamina", "Slash", "Sweeping Slash", "Second Wind", "Guard Up"]
loriCosts = [0, 0, 1, 5, 2]
loriLevels = [[1, 10, 5, 5, 1],
              [2, 11, 5, 5, 2],
              [3, 12, 5, 5, 3],
              [4, 13, 5, 5, 4],
              [5, 14, 6, 6, 5],
              [6, 15, 6, 6, 6],
              [7, 17, 6, 6, 8],
              [8, 18, 6, 7, 10],
              [9, 20, 7, 7, 10],
              [10, 2, 1, 2, 0]]
fwrite.writerow(loriAblities)
fwrite.writerow(loriCosts)
for level in loriLevels:
    fwrite.writerow(level)
f.close()

# Lauren
os.system("type nul > lauren.csv")
f = open("lauren.csv", "w")
fwrite = csv.writer(f)
laurenAblities = ["Light Arrows", "Smiting Arrow", "Restoring Arrow", "Focus Light", "Quick Hands"]
laurenCosts = [0, 1, 1, 1, 0]
laurenLevels = [[1, 10, 7, 2, 5],
                [2, 10, 10, 2, 7],
                [3, 12, 10, 3, 7],
                [4, 13, 10, 3, 9],
                [5, 14, 10, 3, 10],
                [6, 15, 11, 3, 11],
                [7, 15, 12, 4, 12],
                [8, 15, 13, 5, 13],
                [9, 15, 14, 6, 14],
                [10, 1, 2, 1, 0]]
fwrite.writerow(laurenAblities)
fwrite.writerow(laurenCosts)
for level in laurenLevels:
    fwrite.writerow(level)
f.close()

# Marcus
os.system("type nul > marcus.csv")
f = open("marcus.csv", "w")
fwrite = csv.writer(f)
marcusAblities = ["Stamina", "Axe", "Taunting Cry", "Full Guard", "Rally"]
marcusCosts = [0, 0, 1, 5, 4]
marcusLevels = [[1, 10, 3, 7, 1],
                [2, 12, 3, 7, 2],
                [3, 14, 3, 7, 3],
                [4, 16, 3, 7, 5],
                [5, 18, 3, 7, 5],
                [6, 19, 4, 8, 6],
                [7, 20, 4, 10, 7],
                [8, 20, 4, 10, 8],
                [9, 22, 5, 10, 10],
                [10, 2, 1, 1, 0]]
fwrite.writerow(marcusAblities)
fwrite.writerow(marcusCosts)
for level in marcusLevels:
    fwrite.writerow(level)
f.close()

# Julius
os.system("type nul > julius.csv")
f = open("julius.csv", "w")
fwrite = csv.writer(f)
juliusAblities = ["Mana", "Dagger Poke", "Lightning Bolt", "Close Wound", "Fire Ball"]
juliusCosts = [0, 0, 2, 6, 8]
juliusLevels = [[1, 7, 7, 3, 3],
                [2, 7, 9, 3, 4],
                [3, 7, 9, 3, 5],
                [4, 9, 9, 4, 6],
                [5, 10, 9, 5, 7],
                [6, 11, 10, 6, 8],
                [7, 12, 11, 7, 9],
                [8, 13, 12, 8, 10],
                [9, 14, 13, 10, 11],
                [10, 1, 1, 1, 1]]
fwrite.writerow(juliusAblities)
fwrite.writerow(juliusCosts)
for level in juliusLevels:
    fwrite.writerow(level)
f.close()

# Locations.csv


# MainScript creator
os.system("type nul > Launcher.txt")
