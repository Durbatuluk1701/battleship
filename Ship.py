class Ship:
    '''
    Class: Ship
    The Ship class is used to hold and do any actions that have to deal with ships in the battleship game.
    '''

    __shipName__ = ""
    __health__ = 0
    __shipLength__ = 0
    __shipSpots__ = []

    def __init__(self, name, health):
        '''
        Parameters : n/a
        Return: n/a
        Preconditions: Need to create a ship object.
        Postconditions: Sets the name and the health of a ship object.
        '''
        
        self.__shipName__ = name
        self.__health__= health


    
    def getName(self):
        '''
        Parameters : n/a
        Return: The private member varible __shipname__.
        Preconditions: n/a
        Postconditions: Gives the name of a ship object.
        '''

        return self.__shipName__

    def getHealth(self):
        '''
        Parameters : n/a
        Return: The private member varible __health__.
        Preconditions: n/a
        Postconditions: Gives current health of a ship object.
        '''

        return self.__health__

    def damageShip(self):
        '''
        Parameters : n/a
        Return: n/a
        Preconditions: To be called by ship object.
        Postconditions: Does one damage to a ship that has at least one health.
        '''

        if self.__health__ > 0:
            self.__health__ = self.__health__ - 1

    def isDead(self):
        '''
        Parameters : n/a
        Return: returns true if the ship object is dead, and false if it is still alive.
        Preconditions: Needs to be called by ship object.
        Postconditions: Tells us if the ship we are calling is dead or alive.
        '''

        if self.__health__ == 0:
            return True
        return False
