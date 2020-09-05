class Ship:
    __shipName__ = ""
    __health__ = "0"
    
    def __init__(self, name, health):
        self.__shipName__ = name
        self.__health__= health

    def getName(self):
        return self.__shipName__
    def getHealth(self):
        return self.__health__

    def damageShip(self):
        if self.__health__ > 0:
            self.__health__ = self.__health__ - 1

    def isDead(self):
        if self.__health__ > 0:
            return False
        return True