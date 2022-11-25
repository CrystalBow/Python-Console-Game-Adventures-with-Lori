from PlayableCharacter import PlayableCharacter

class GameMenu(object):
    PClist = []
    # PChp List will use [current, total]
    PChpList = []

    def __init__(self):

        #Defualt for now
        self.PClist.append("Character Object")
        self.PChpList.append(["current", "total"])

    def displayPC(self, PlayableCharacter):

        #Defualt for now
        print(PlayableCharacter.displayName)


    def displayGameMenu(self):

        #defualt for now
        for pc in self.PClist:
            print(pc)
            