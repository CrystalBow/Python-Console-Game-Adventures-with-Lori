#!/usr/bin/env python
import os
import csv


#newGame.csv recource
os.system("type nul > newGame.csv")
f = open("newGame.csv", "w")
fwrite = csv.writer(f)
newGame = [750, 750, 0, 0, 1, 0, 0, 0]
fwrite.writerow(newGame)
f.close()


#regions.csv recource
os.system("type nul > regions.csv")
f = open("regions.csv", "w")
fwrite = csv.writer(f)
regions = [[0, "Larmen Plains", 0, 200, 0, 100, 0, 0], [1, "the Rise", 101, 200, 101, 199, 0, 20], [2,"the Desert South", 0, 100, 101, 423, 0, 0],[3,"the Desrt North",0 , 749, 424, 500, 0, 0],
	[4, "Ruined Plateau", 101, 749, 200, 423, 20, 20], [5, "the Death Lands", 201, 875, 0, 199, 0, 4], [6, "Goblin Montain", 876, 1000, 0, 50, 2, 20], [7, "Drame Kingdom", 876, 1000, 51,239,0,4],
	[8, "Mini Plateau", 750, 875, 200, 249, 20, 20], [9, "Kindom of Javi", 750, 1000, 250, 350, 0, 0], [10, "Igachi Plain", 750, 1000, 351, 500, 0,0]] 
for region in regions:
	fwrite.writerow(region)
f.close()


#character csvs
#Lori
os.system("type nul > lori.csv")
f = open("lori.csv", "w")
fwrite = csv.writer(f)
loriAblities = ["Stanima","Slash", "Sweeping Slash", "Second Wind", "Guard Up"]
loriCommands = ["recource","attack","attackAll", "healSelf", "raiseDef"] 
loriCosts = [0,0,1,5,2]
loriLevels = [[1,10,5,5,1],
	[2,11,5,5,2],
	[3,12,5,5,3],
	[4,13,5,5,4],
	[5,14,6,6,5],
	[6,15,6,6,6],
	[7,17,6,6,8],
	[8,18,6,7,10],
	[9,20,7,7,10],
	[10,2,1,2,0]]
fwrite.writerow(loriAblities)
fwrite.writerow(loriCommands)
fwrite.writerow(loriCosts)
for level in loriLevels:
	fwrite.writerow(level)
f.close()

#Lauren
os.system("type nul > lauren.csv")
f = open("lauren.csv", "w")
fwrite = csv.writer(f)
laurenAblities = ["Light Arrows","Smiting Arrow", "Restoring Arrow", "Focus Light", "Quick Hands"]
laurenCommands = ["recource","attack","healTarget", "critUp", "itemsTwo"] 
laurenCosts = [0,1,1,1,0]
laurenLevels = [[1,10,7,2,5],
	[2,10,10,2,7],
	[3,12,10,3,7],
	[4,13,10,3,9],
	[5,14,10,3,10],
	[6,15,11,3,11],
	[7,15,12,4,12],
	[8,15,13,5,10],
	[9,15,14,6,10],
	[10,1,2,1,0]]
fwrite.writerow(laurenAblities)
fwrite.writerow(laurenCommands)
fwrite.writerow(laurenCosts)
for level in laurenLevels:
	fwrite.writerow(level)
f.close()


#Locations.csv


#MainScript creator
os.system("type nul > Launcher.txt")
