from PlayableCharacter import PlayableCharacter
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
            self.PChpList.append([ch.currentHealth, ch.health])
            self.PCRecourceList.append([ch.currentEnergy, ch.energyValue, ch.energyName])


    def displayPC(self, playableCharacter):

        #Defualt for now
        print(playableCharacter.displayName)


    def displayGameMenu(self):

        #defualt for now
        for pc in self.PClist:
            print(pc)
            