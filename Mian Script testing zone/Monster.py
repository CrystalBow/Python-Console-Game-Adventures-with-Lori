from Character import Character
#import Character

#class Monster(Character.Character):
class Monster(Character):
    def __init__(self, attack = None, defense = None, health = 1, experince = None, displayName = None, buddyRate = None, buddyType = None):
        super().__init__( Attack= attack, Defense = defense , Health= health, Exp = experince, displayName = displayName)
        self.buddyRate = buddyRate
        self.buddyType = buddyType
