#!/usr/bin/env python
# imports
import csv
from Character import Character
from Monster import Monster
from PlayableCharacter import PlayableCharacter
import os

# Variables
currentAwnser = 0
x = 0
y = 0
z = 0
chapter = 0
Lori = PlayableCharacter("Lori")
Lauren = PlayableCharacter("Lauren")

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


# Main Line Commands
inputAndCheck("how would you like to boot? 0 New game or integer of save you are booting", [0])
bootSave(currentAwnser)
input(type(Lori.level))
generateCharacters()
os.system("cls")
input("we made it!!!")

