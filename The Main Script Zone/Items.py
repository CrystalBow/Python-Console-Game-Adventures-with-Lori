from PlayableCharacter import PlayableCharacter


class Item(object):

    def __init__(self, command, name, cost, usage):
        self.effect = command
        self.name = name
        self.cost = cost
        self.usage = usage

    def effectHandler(self, user: PlayableCharacter, equip= True): #learned how to specify type of parameter.
        if equip:
            if self.effect == "Def":
                user.defense = user.defense + self.usage
            elif self.effect == "AtkPhy" or self.effect == "AtkMag":
                user.attack = user.attack + self.usage
        else:
            if self.effect == "hp":
                user = self.healing(user)
        return user

    def healing(self, user: PlayableCharacter):
        user.currentHealth = user.currentHealth + self.usage
        if user.currentHealth >= user.health:
            user.currentHealth = user.health
        return user