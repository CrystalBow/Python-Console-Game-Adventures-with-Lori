#!/usr/bin/env python
#imports
import os
import csv
#Variables
currentAwnser = 0
x = 0
y = 0
z = 0
chapter = 0
loriLvl = 0
loriHp = 0
loriAtk = 0
loriDef = 0
loriStanima = 0
loriEXP = 0
loriActions = []
loriCommands = []
loriCosts = []
laurenLvl = 0
laurenHp = 0
laurenAtk = 0
laurenDef = 0
laurenArrows = 0
laurenEXP = 0
laurenActions = []
laurenCommands = []
laurenCosts = []
#Functions
def inputAndCheck(question, validAwnsers): #validAwnsers must be a list
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
#Extracting Save Data
def bootSave(saveNum):
	global x
	global y
	global z
	global loriLvl
	global laurenLvl
	global chapter
	if saveNum == 0:
		input("we are in")
		f = open("newGame.csv")
		fReader = csv.reader(f)
		content = next(fReader)
		x = int(content[0])
		y = int(content[1])
		z = int(content[2])
		chapter = int(content[3])
		loriLvl = int(content[4])
		laurenLvl = int(content[5])
		f.close()
	else:
		input("fail")

#Character Data
def generateCharacters():
	global loriLvl
	global loriAtk
	global loriDef
	global loriActions
	global loriCommands
	global loriCosts
	global loriHp
	global laurenLvl
	global laurenHp
	global laurenAtk
	global laurenDef
	global laurenActions
	global laurenCommands
	global laurenCosts
	stringCosts = []
	garbage = 0
	statLine = []
	lvlCounter = 0
	if loriLvl < 10:
		file = open("lori.csv")
		fileReader = csv.reader(file)
		loriActions = next(fileReader)
		garbage = next(fileReader)
		loriCommands = next(fileReader)
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
					if lvlCounter == loriLvl:
						break
					else:
						pass
				except ValueError:
					pass
		input(loriActions)
		input(statLine)
		input(loriCommands)
		file.close()
		loriHp = int(statLine[2])
		loriAtk = int(statLine[3])
		loriDef = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			loriCosts.append(garbage)
		input(loriCosts)
	else:
		input("almost")
	if laurenLvl < 10 and laurenLvl > 0:
		file = open("lauren.csv")
		fileReader = csv.reader(file)
		laurenActions = next(fileReader)
		garbage = next(fileReader)
		laurenCommands = next(fileReader)
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
					if lvlCounter == laurenLvl:
						break
					else:
						pass
				except ValueError:
					pass
		input(laurenActions)
		input(statLine)
		input(laurenCommands)
		file.close()
		laurenHp = int(statLine[2])
		laurenAtk = int(statLine[3])
		laurenDef = int(statLine[4])
		for stuff in stringCosts:
			garbage = int(stuff)
			laurenCosts.append(garbage)
		input(laurenCosts)
	else:
		input("almost")

#Main Line Commands
inputAndCheck("how would you like to boot? 0 New game or integer of save you are booting", [0])
bootSave(currentAwnser)
input(type(loriLvl))
generateCharacters()
os.system("cls")
input("we made it!!!")

