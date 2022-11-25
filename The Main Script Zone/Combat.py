from Character import Character
from PlayableCharacter import PlayableCharacter
from Monster import Monster
import random


class Combat(object):

    def __init__(self):
        self.order = []
        self.listing = []

    def skillHandler(self, skill):

        # defualt for now
        input("Skill!")

    def intiativeRoll(self, Combatant):

        # defualt for now
        self.listing.append([Combatant.displayName, random.random()])
        self.order.append([Combatant.displayName, Combatant])

    def combatEndCheck(self):

        # default for now
        if len(self.order) == 0:
            input("Combat is over!")

    def baseAttack(self, attacker, defender):
        targetingNum = random.random() * 100

        # defualt for now
        if targetingNum > 50:
            defender.currentHealth = defender.currentHealth - (attacker.attack -
                                                               defender.defense)

    def turn(self, Ally):

        # defualt for now
        self.baseAttack(Ally, self.order[0][1])
