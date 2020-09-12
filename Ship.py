
'''Class: Ship
    The Ship class is used to hold and do any actions that have to deal with ships in the battleship game.'''

'''Private Member Varibles:
    __shipName__ : holds name for ship object.
    __health__ : the health of a ship object.
    __shipLength__ : how long a ship object is.
    __shipSpots__ : holds the information on where a ship object is on the board.'''
class Ship:
    __shipName__ = ""
    __health__ = 0
    __shipLength__ = 0
    __shipSpots__ = []
    
    '''Initilaizer:
        Parameters : n/a
        Return: n/a
        Preconditions: Need to create a ship object.
        Postconditions: Sets the name and the health of a ship object.'''
    def __init__(self, name, health): # assigns health and name in default constructor
        self.__shipName__ = name
        self.__health__= health

    '''Function : getName()
        Parameters : n/a
        Return: The private member varible __shipname__.
        Preconditions: n/a
        Postconditions: Gives the name of a ship object.'''
    def getName(self):
        return self.__shipName__

        '''Function : getHealth()
        Parameters : n/a
        Return: The private member varible __health__.
        Preconditions: n/a
        Postconditions: Gives current health of a ship object.'''
    def getHealth(self):
        return self.__health__

    '''Function : damageShip()
        Parameters : n/a
        Return: n/a
        Preconditions: To be called by ship object.
        Postconditions: Does one damage to a ship that has at least one health.'''
    def damageShip(self): # damages ship health by 1
        if self.__health__ > 0:
            self.__health__ = self.__health__ - 1

    '''Function : isDead()
        Parameters : n/a
        Return: returns true if the ship object is dead, and false if it is still alive.
        Preconditions: Needs to be called by ship object.
        Postconditions: Tells us if the ship we are calling is dead or alive.'''
    def isDead(self): # if health is 0, ship is dead
        if self.__health__ == 0:
            return True
        return False
