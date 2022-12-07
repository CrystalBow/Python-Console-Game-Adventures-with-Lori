from Character import Character
#import Character

#class Monster(Character.Character):
class Monster(Character):
    def __init__(self, attack = 0, defense = 0, health = 1, experince = 0, displayName = None, buddyRate = None, petRate = None, weapon = "fist"):
        super().__init__( Attack= attack, Defense = defense , Health= health, Exp = experince, displayName = displayName)
        self.buddyRate = buddyRate
        self.petRate = petRate
        self.weapon = weapon

