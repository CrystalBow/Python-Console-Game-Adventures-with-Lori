import csv
class Shop(object):
    items = []
    def __init__(self):

        #Defualt for now
        self.items.append("Items go here")

    def buy(self, item):

        #Defualt for now
        self.items.remove("Items go here")
