from Character import Character


class PlayableCharacter(Character):
    def __init__(self, displayName, attack = 0, defense = 0, health = 0, experience = 0, lvl = 0, skills = None, energyName = None, energyValue = 0):
        super().__init__(Attack=attack, Defense=defense, Health=health, Exp=experience, displayName=displayName)
        self.skillCosts = []
        self.level = lvl
        self.energyName = energyName
        self.energyValue = energyValue
        self.currentEnergy = energyValue
        self.skills = skills
        self.inventory = []

    def deathCheck(self):
        if self.currentHealth <= 0:
            if self.level > 0:
                print(self.displayName + " is down!")
            return False

    def useItem(self, choice :int):
        copyOfSelf = self.inventory[choice].effectHandler(self, equip= False)
        self.currentHealth = copyOfSelf.currentHealth
        self.inventory.pop(choice)