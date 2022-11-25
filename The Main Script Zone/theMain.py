#!/usr/bin/env python
# imports
import csv
from PlayableCharacter import PlayableCharacter
from Monster import Monster
import os

# Variables
currentAwnser = 0
x = 0
y = 0
z = 0
chapter = 0
Lori = PlayableCharacter("Lori")
Lauren = PlayableCharacter("Lauren")
Marcus = PlayableCharacter("Marcus")
Julius = PlayableCharacter("Julius")
#Testing Purposes
ThatMonster = Monster(displayName="Test Boy", attack=10, defense=10, health=10, experince=10)

# Functions
def inputAndCheck(question, validAwnsers): # validAwnsers must be a list
	global currentAwnser
	awnserString = input(question)
	validaty = False
	convertedAwnser = 0
	awnserFlag = False
	try:
		int(awnserString)
		validaty = True
	except ValueError:
		pass
	if validaty == False:
		inputAndCheck(question, validAwnsers)
	else:
		input("success: Type Correct")
		convertedAwnser = int(awnserString)
		for awnser in validAwnsers:
			if convertedAwnser == awnser:
				awnserFlag = True
			else:
				continue
		if awnserFlag == False:
			inputAndCheck(question, validAwnsers)
		else:
			input("Success: Valid Awnser")
			currentAwnser =  convertedAwnser
# Extracting Save Data
def bootSave(saveNum):
	global x
	global y
	global z
	global chapter
	input(saveNum)
	input(type(saveNum))
	if saveNum == 0:
		input("we are in")
		f = open("newGame.csv")
		fReader = csv.reader(f)
		content = next(fReader)
		input(type(content))
		input(content)
		x = int(content[0])
		y = int(content[1])
		z = int(content[2])
		chapter = int(content[3])
		Lori.level = int(content[4])
		Lauren.level = int(content[5])
		Marcus.level = int(content[6])
		Julius.level = int(content[7])
		input(Lori.level)
		f.close()
	else:
		input("fail")

def generateCharacters():
	garbage = 0
	statLine = []
	lvlCounter = 0
	if Lori.level < 10:
		file = open("lori.csv")
		fileReader = csv.reader(file)
		Lori.skills = list(next(fileReader))
		garbage = next(fileReader)
		stringCosts = next(fileReader)
		for row in fileReader:
			input("we made it")
			if row == []:
				pass
			else:
				statLine = row
				input(statLine[0])
				input(type(statLine[0]))
				try:
					lvlCounter = int(statLine[0])
					if lvlCounter == Lori.level:
						break
					else:
						pass
				except ValueError:
					pass
		input(Lori.skills)
		input(statLine)
		file.close()
		Lori.health = int(statLine[2])
		Lori.attack = int(statLine[3])
		Lori.defense = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			Lori.skillCosts.append(garbage)
		input(Lori.skillCosts)
	else:
		input("almost")
	if Lauren.level < 10 and Lauren.level > 0:
		file = open("lauren.csv")
		fileReader = csv.reader(file)
		Lauren.skills = next(fileReader)
		garbage = next(fileReader)
		stringCosts = next(fileReader)
		for row in fileReader:
			input("we made it")
			if row == []:
				pass
			else:
				statLine = row
				input(statLine[0])
				input(type(statLine[0]))
				try:
					lvlCounter = int(statLine[0])
					if lvlCounter == Lauren.level:
						break
					else:
						pass
				except ValueError:
					pass
		input(Lauren.skills)
		input(statLine)
		file.close()
		Lauren.health = int(statLine[2])
		Lauren.attack = int(statLine[3])
		Lauren.defense = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			Lauren.skillCosts.append(garbage)
		input(Lauren.skillCosts)
	else:
		input("almost")
	if Julius.level < 10 and Julius.level > 0:
		file = open("julius.csv")
		fileReader = csv.reader(file)
		Julius.skills = next(fileReader)
		garbage = next(fileReader)
		stringCosts = next(fileReader)
		for row in fileReader:
			input("we made it")
			if row == []:
				pass
			else:
				statLine = row
				input(statLine[0])
				input(type(statLine[0]))
				try:
					lvlCounter = int(statLine[0])
					if lvlCounter == Julius.level:
						break
					else:
						pass
				except ValueError:
					pass
		input(Julius.skills)
		input(statLine)
		file.close()
		Julius.health = int(statLine[2])
		Julius.attack = int(statLine[3])
		Julius.defense = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			Julius.skillCosts.append(garbage)
		input(Julius.skillCosts)
	else:
		input("almost")
	if Marcus.level < 10 and Marcus.level > 0:
		file = open("marcus.csv")
		fileReader = csv.reader(file)
		Marcus.skills = next(fileReader)
		garbage = next(fileReader)
		stringCosts = next(fileReader)
		for row in fileReader:
			input("we made it")
			if row == []:
				pass
			else:
				statLine = row
				input(statLine[0])
				input(type(statLine[0]))
				try:
					lvlCounter = int(statLine[0])
					if lvlCounter == Marcus.level:
						break
					else:
						pass
				except ValueError:
					pass
		input(Marcus.skills)
		input(statLine)
		file.close()
		Marcus.health = int(statLine[2])
		Marcus.attack = int(statLine[3])
		Marcus.defense = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			Marcus.skillCosts.append(garbage)
		input(Marcus.skillCosts)
	else:
		input("almost")

def explorer():
	global x
	global y
	global z
	global chapter
	#Code goes here

	#defualt iterations. temporary.
	x += 1
	y += 1
	chapter += 1


# Main Line Commands
inputAndCheck("how would you like to boot? 0 New game or integer of save you are booting", [0])
bootSave(currentAwnser)
input(type(Lori.level))
generateCharacters()
os.system("cls")
input("we made it!!!")
if chapter == 0:
	input("Opening")
	chapter += 1
	Lauren.level += 1
generateCharacters()
while chapter < 24:
	# the main game
	explorer()
input("credits")
chapter += 1
while chapter < 27:
	# the post game
	explorer()
input("credits and close")
input("Extra Data:" + str(x) + " " + str(y) + " " + str(z))
