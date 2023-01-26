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
#Testing Purposes
ThatMonster = Monster(displayName="Test Boy", attack=10, defense=5, health=1, experince=10)

# Functions
# Extracting Save Data
def bootSave(saveNum):
	global x
	global y
	global z
	global chapter
	global Lori
	global Lauren
	global Marcus
	global Julius
	global gold
	print(saveNum)
	print(type(saveNum))
	if saveNum == 0:
		input("we are in")
		f = open("newGame.csv")
		fReader = csv.reader(f)
		content = next(fReader)
		print(type(content))
		print(content)
		x = int(content[0])
		y = int(content[1])
		z = int(content[2])
		chapter = int(content[3])
		Lori.level = int(content[4])
		Lauren.level = int(content[5])
		Marcus.level = int(content[6])
		Julius.level = int(content[7])
		print(Lori.level)
		f.close()
	else:
		try:
			f = open("save" + str(saveNum) +".csv")
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
			next(fReader)
			content = next(fReader)
			Lori.inventory = content[0]
			Lauren.inventory = content[1]
			Marcus.inventory = content[2]
			Julius.inventory = content[3]
			gold = int(content[4])
			next(fReader)
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
			bootSave(inputAndCheck("how would you like to boot? 0 New game or integer of save you are booting", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# region getters
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

def regionCheck(x, y, z):
	file = open("regions.csv")
	fileReader = csv.reader(file)
	targetRegion = -1
	regions = []
	for line in fileReader:
		regions.append(line)
	file.close()
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
	choice = inputAndCheck("What file would you like to save too? ", [1,2,3,4,5,6,7,8,9,10])
	os.system("type nul > save" + str(choice)+ ".csv")
	f = open("save" + str(choice) + ".csv", "w")
	fWriter = csv.writer(f)
	Row = [x, y, z, ch]
	Rows = []
	for playable in characters:
		Row.append(playable.level)
	Rows.append(Row)
	Row = []
	for playable in characters:
		Row.append(playable.inventory)
	Row.append(gp)
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
	choice = inputAndCheck("Would you like to keep playing? (1: Yes, 0: No) ", [0,1])
	if choice == 0:
		exit()


def rest(charecters,  local):
	updatedCharacters = []
	if local:
		for wifu in charecters:
			wifu.currentHealth = wifu.Health
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
	global ThatMonster
	input("fight!")
	#temporary^^
	theBattle = Combat(region)
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
				theBattle.intiativeRoll(Monster(attack= int(enemy[2]), health= int(enemy[1]), defense= int(enemy[3]), displayName=badie, experince= int(enemy[7]),petRate= int(enemy[4]), buddyRate= int(enemy[5]), weapon= enemy[6]))
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
	scan = locationCheck(x +1, y - 1, z, locals, regionID)
	if scan[0]:
		finds.append([scan[2], "south east"])
	scan = locationCheck(x - 1, y , z, locals, regionID)
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
				if Location(Name= place[0],x= x,y= y, z=z) not in locals:
					locals.append(Location(Name= place[0], x= x,y= y,z= z)) #need to add a status to location class.
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
				if Location(Name= place[0],x= x,y= y, z=z) not in locals:
					locals.append(Location(Name= place[0], x= x,y= y,z= z))
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
				if Location(Name= place[0],x= x,y= y, z=z) not in locals:
					locals.append(Location(Name= place[0], x= x,y= y,z= z))
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
				if Location(Name= place[0],x= x,y= y, z=z) not in locals:
					locals.append(Location(Name= place[0], x= x,y= y,z= z))
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
				if Location(Name= place[0],x= x,y= y, z=z) not in locals:
					locals.append(Location(Name= place[0], x= x,y= y,z= z))
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
				if Location(Name= place[0],x= x,y= y, z=z) not in locals:
					locals.append(Location(Name= place[0], x= x,y= y,z= z))
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
				if Location(Name= place[0],x= x,y= y, z=z) not in locals:
					locals.append(Location(Name= place[0], x= x,y= y,z= z))
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
				if Location(Name= place[0],x= x,y= y, z=z) not in locals:
					locals.append(Location(Name= place[0], x= x,y= y,z= z))
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
				if Location(Name= place[0],x= x,y= y, z=z) not in locals:
					locals.append(Location(Name= place[0], x= x,y= y,z= z))
					return [True, locals, place[0]]
				else:
					return [True, locals, place[0]]
		return [False, locals]
# creation and level up of characters
def generateCharacters():
	garbage = 0
	statLine = []
	lvlCounter = 0
	if Lori.level < 10:
		file = open("lori.csv")
		fileReader = csv.reader(file)
		Lori.skills = list(next(fileReader))
		Lori.skillCosts = []
		Lori.energyName = Lori.skills[0]
		Lori.skills.pop(0)
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
		print(Lori.skills)
		file.close()
		Lori.health = int(statLine[1])
		Lori.attack = int(statLine[2])
		Lori.defense = int(statLine[3])
		Lori.energyValue = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			Lori.skillCosts.append(garbage)
		Lori.skillCosts.pop(0)
		print(Lori.skillCosts)
	else:
		input("almost")
	if Lauren.level < 10 and Lauren.level > 0:
		file = open("lauren.csv")
		fileReader = csv.reader(file)
		Lauren.skills = next(fileReader)
		Lauren.energyName = Lauren.skills[0]
		Lauren.skillCosts = []
		Lauren.skills.pop(0)
		garbage = next(fileReader)
		stringCosts = next(fileReader)
		for row in fileReader:
			print("we made it")
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
		print(Lauren.skills)
		file.close()
		Lauren.health = int(statLine[1])
		Lauren.attack = int(statLine[2])
		Lauren.defense = int(statLine[3])
		Lauren.energyValue = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			Lauren.skillCosts.append(garbage)
		Lauren.skillCosts.pop(0)
		print(Lauren.skillCosts)
	else:
		print("almost")
	if Julius.level < 10 and Julius.level > 0:
		file = open("julius.csv")
		fileReader = csv.reader(file)
		Julius.skills = next(fileReader)
		Julius.skillCosts = []
		Julius.energyName = Julius.skills[0]
		Julius.skills.pop(0)
		garbage = next(fileReader)
		stringCosts = next(fileReader)
		for row in fileReader:
			print("we made it")
			if row == []:
				pass
			else:
				statLine = row
				print(statLine[0])
				print(type(statLine[0]))
				try:
					lvlCounter = int(statLine[0])
					if lvlCounter == Julius.level:
						break
					else:
						pass
				except ValueError:
					pass
		print(Julius.skills)
		file.close()
		Julius.health = int(statLine[1])
		Julius.attack = int(statLine[2])
		Julius.defense = int(statLine[3])
		Julius.energyValue = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			Julius.skillCosts.append(garbage)
		Julius.skillCosts.pop(0)
		print(Julius.skillCosts)
	else:
		print("almost")
	if Marcus.level < 10 and Marcus.level > 0:
		file = open("marcus.csv")
		fileReader = csv.reader(file)
		Marcus.skills = next(fileReader)
		Marcus.skillCosts = []
		Marcus.energyName = Marcus.skills[0]
		Marcus.skills.pop(0)
		garbage = next(fileReader)
		stringCosts = next(fileReader)
		for row in fileReader:
			print("we made it")
			if row == []:
				pass
			else:
				statLine = row
				print(statLine[0])
				print(type(statLine[0]))
				try:
					lvlCounter = int(statLine[0])
					if lvlCounter == Marcus.level:
						break
					else:
						pass
				except ValueError:
					pass
		print(Marcus.skills)
		print(statLine)
		file.close()
		Marcus.health = int(statLine[1])
		Marcus.attack = int(statLine[2])
		Marcus.defense = int(statLine[3])
		Marcus.energyValue = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			Marcus.skillCosts.append(garbage)
		Marcus.skillCosts.pop(0)
		print(Marcus.skillCosts)
	else:
		print("almost")

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
	print("x: " + str(x) + " y: " + str(y) + " z: "+ str(z))
	if not local:
		selections = [4, 5, 6]
		print(regionDisplay + ":")
		print(regionDiscribe(region))
		for pair in AOEScanner(x,y,z,locations, region):
			print("You can see " + pair[0] + " in the " + pair[1])
	if local:
		selections = [4, 5, 6, 7]
		print(regionDisplay + ":")
		print(locationCheck(x, y, z, locations, region)[2])
	if regionCheck(x+1,y,z) >= 0 and \
			(fetchRegionZ(regionCheck(x+1,y,z))-fetchRegionZ(region) <= 5 and
			 fetchRegionZ(region)-fetchRegionZ(regionCheck(x+1,y,z)) <= 5):
		selections.append(1)
	if regionCheck(x,y+1,z) >= 0 and \
			(fetchRegionZ(regionCheck(x,y+1,z))-fetchRegionZ(region) <= 5 and
			 fetchRegionZ(region)-fetchRegionZ(regionCheck(x,y+1,z)) <= 5):
		selections.append(0)
	if regionCheck(x-1,y,z) >= 0 and \
			(fetchRegionZ(regionCheck(x-1,y,z))-fetchRegionZ(region) <= 5 and
			 fetchRegionZ(region)-fetchRegionZ(regionCheck(x-1,y,z)) <= 5):
		selections.append(3)
	if regionCheck(x,y-1,z)  >= 0 and \
			(fetchRegionZ(regionCheck(x,y-1,z))-fetchRegionZ(region) <= 5 and
			 fetchRegionZ(region)-fetchRegionZ(regionCheck(x,y-1,z)) <= 5):
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
				input("item has effect!")

	if playerChoice == 5:
		characters = rest(characters, local)
		Lauren = characters[1]
		Lori = characters[0]
		Marcus = characters[2]
		Julius = characters[3]
	if playerChoice == 6:
		save(characters, x, y, z, chapter,gold)
	region = regionCheck(x, y, z)
	regionDisplay = fetchRegionDisplay(region)
	Checker = encounterCheck(region)
	if (Checker[0] == True):
		runCombat([Checker[1]], characters, region)
	Checker= locationCheck(x, y, z, locations, region) #list: [bool, list of locations, locationDisplay]
	local = Checker[0]
	locations = Checker[1]

	os.system("cls")


# Main Line Commands

bootSave(inputAndCheck("how would you like to boot? 0 New game or integer of save you are booting", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
input(type(Lori.level))
generateCharacters()
os.system("cls")
print("we made it!!!")
if chapter == 0:
	input("Opening")
	chapter += 1
	Lauren.level += 1
	generateCharacters()
	Lauren.currentHealth = Lauren.health
	Lori.currentEnergy = Lori.energyValue
	Lori.currentHealth = Lori.health
	Lauren.currentEnergy = Lauren.energyValue
region = regionCheck(x, y, z)
regionDisplay = fetchRegionDisplay(region)
Checker= locationCheck(x, y, z, locations, region) #list: [bool, list of locations, locationDisplay]
local = Checker[0]
locations = Checker[1]
TestingCounter = 0 #tomporary
while chapter < 24:
	# the main game
	explorer()
	TestingCounter += 1 #temporary
	if TestingCounter == 3:	#temporary
		TestingCounter = 0
		chapter += 1 #temprorary
input("credits")
chapter += 1
while chapter < 27:
	# the post game
	explorer()
input("credits and close")
input("Extra Data:" + str(x) + " " + str(y) + " " + str(z))
