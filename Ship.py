
# simple ship class which has health and a name
class Ship:
    __shipName__ = ""
    __health__ = 0
    __shipLength__ = 0
    __shipSpots__ = []
    
    def __init__(self, name, health): # assigns health and name in default constructor
        self.__shipName__ = name
        self.__health__= health

    def getName(self):
        return self.__shipName__
    def getHealth(self):
        return self.__health__

    def damageShip(self): # damages ship health by 1
        if self.__health__ > 0:
            self.__health__ = self.__health__ - 1

    def isDead(self): # if health is 0, ship is dead
        if self.__health__ == 0:
            return True
        return False