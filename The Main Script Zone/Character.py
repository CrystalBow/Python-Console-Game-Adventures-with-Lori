class Character(object):

    def __init__(self, Attack = None, Defense = None, Health = 1, Exp = None, displayName = None):
        self.displayName = displayName
        self.attack = Attack
        self.defense = Defense
        self.health = Health
        self.currentHealth = Health
        self.experience = Exp
    def deathCheck(self):
        if self.health <= 0:
            del self
        else:
            pass





