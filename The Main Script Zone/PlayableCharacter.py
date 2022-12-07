from Character import Character


class PlayableCharacter(Character):
    def __init__(self, displayName, attack = 0, defense = 0, health = 1, experience = 0, lvl = 0, skills = None, energyName = None, energyValue = 0, inventory = []):
        super().__init__(Attack=attack, Defense=defense, Health=health, Exp=experience, displayName=displayName)
        self.skillCosts = []
        self.level = lvl
        self.energyName = energyName
        self.energyValue = energyValue
        self.currentEnergy = energyValue
        self.skills = skills
        self.inventory = inventory


