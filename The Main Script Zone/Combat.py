from Character import Character
from PlayableCharacter import PlayableCharacter
from Monster import Monster
import random


class Combat(object):

    def __init__(self, location, continueStatus = True):
        self.location = location
        self.order = []
        self.listing = {}
        self.continueStatus = continueStatus

    def skillHandler(self, skill):

        # defualt for now
        input("Skill!")

    def intiativeRoll(self, Combatant):

        # defualt for now
        self.listing.update({Combatant.displayName : Combatant})
        self.order.append([Combatant.displayName, random.random()])

    def combatEndCheck(self):

        # default for now
        if len(self.listing) == 4:
            self.continueStatus = False
        return True

    def baseAttack(self, attacker, defender):
        targetingNum = random.random() * 100

        # defualt for now
        if targetingNum > 50:
            defender.currentHealth = defender.currentHealth - (attacker.attack - defender.defense)

    def turn(self, Ally):

        # defualt for now
        for target in self.listing:
            if isinstance(self.listing[target], Monster):
                self.baseAttack(Ally, self.listing[target])
