import csv

class Location(object):

    def __init__(self, Name= "Display", x= 0, y= 0, z= 0):
        self.displayName = Name
        self.x = x
        self.y = y
        self.z = z
        self.storyFlag = False
