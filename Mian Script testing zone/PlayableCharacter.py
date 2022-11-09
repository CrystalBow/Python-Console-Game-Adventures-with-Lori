from Character import Character


class PlayableCharacter(Character):
    def __init__(self, displayName, attack = None, defense = None, health = 1, experience = 0, lvl = 0, skills = None, skillCosts = None, energyName = None, energyValue = None):
        super().__init__(Attack= attack, Defense= defense, Health= health, Exp=experience, displayName=displayName)
        self.skillCosts = []
        self.level = lvl
        self.energyName = energyName
        self.energyValue = energyValue
        self.skills = skills
        self.skillCosts = skillCosts

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level
