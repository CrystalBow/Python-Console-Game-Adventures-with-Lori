from PlayableCharacter import PlayableCharacter
from Items import Item
class GameMenu(object):
    PClist = []
    # PChp List will use [current, total]
    PChpList = []
    # The Recource will use [current, total, name]

    def __init__(self):
        #Defualt for now
        self.PClist = []
        self.PChpList = []
        self.PCRecourceList = []

    def update(self, playerCharacters):
        self.PClist = []
        self.PCRecourceList = []
        self.PChpList = []
        for ch in playerCharacters:
            self.PClist.append(ch)
            self.PChpList.append([str(ch.currentHealth), str(ch.health)])
            self.PCRecourceList.append([str(ch.currentEnergy), str(ch.energyValue), str(ch.energyName)])


    def displayPC(self, playableCharacter, pcSkip = False):
        options = []
        if not pcSkip:
            print(playableCharacter.displayName)
            print("level: " + str(playableCharacter.level))
            i = 0
            while i < len(self.PClist):
                if (playableCharacter == self.PClist[i]):
                    break
                i += 1
            print("HP: " + self.PChpList[i][0] + "/" + self.PChpList[1][1])
            print(self.PCRecourceList[i][2] + ": " + self.PCRecourceList[i][0] + "/" + self.PCRecourceList[i][1])
            print("Skill(cost) ")
            i = 0
            while i < len(playableCharacter.skills):
                print(playableCharacter.skills[i] + "("+ str(playableCharacter.skillCosts[i]) + ")")
                i += 1
        print("Inventory: ")
        i = 0
        for item in playableCharacter.inventory:
            if isinstance(item, Item):
                options.append(i)
                print(str(i) + ": " + item.name)
                i += 1
        options.append(i)
        print(str(i) + ": Use nothing")
        return options


    def displayGameMenu(self):
        i = 0
        options = []
        while i < len(self.PClist):
            if self.PClist[i].level > 0:
                options.append(i)
                print(str(i) + ":" + self.PClist[i].displayName + ": " + self.PChpList[i][0] + "/" + self.PChpList[i][1] + " hp, " + self.PCRecourceList[i][0] + "/" + self.PCRecourceList[i][1] + " " + self.PCRecourceList[i][2])
            i += 1
        print(str(i) + ": Nothing")
        options.append(i)
        return options


            