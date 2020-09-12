'''Class: Tile
    The Tile class is used to hold information and interact with a grid space in battleship.'''
class Tile:

    '''-Default Constructor-
        Parameters: n/a
        Return: n/a
        Preconditions: Must create a Tile object.
        Postconditions: Sets the grid tile to "water" and that it hasn't been attacked yet.
        '''
    def __init__(self): # initializes the tile object to be water and not attacked by default
        self.tileItem = "water" # tileItem is a string
        self.attacked = False # attacked is a bool

    '''Function: getTile()
        Parameters: n/a
        Return: returns tileItem
        Preconditions: Must create a Tile object.
        Postconditions: returns what is in the tile at a specific grid space.'''
    def getTileItem(self): # returns the type of tile
        return self.tileItem

    '''Function: getTileAttacked()
        Parameters: n/a
        Return: returns attacked.
        Preconditions: Must create a Tile object.
        Postconditions: returns the bool of if the grid space has already been attacked.'''
    def getTileAttacked(self): # returns the status of the tile, regarding whether or not it's been attacked
        return self.attacked

    '''Function: setTileAttacked()
        Parameters: n/a
        Return: n/a
        Preconditions: Must create a Tile object.
        Postconditions: Sets the tile to True showing it has been attacked.'''
    def setTileAttacked(self): # sets the status of the tile to attacked
        self.attacked = True

    '''Function: setTileItem()
        Parameters: tileItem
        Return: n/a
        Preconditions: Must create a Tile object.
        Postconditions: Sets the tile to the parameter of tileItem.'''
    def setTileItem(self, tileItem): # sets the type of tile
        self.tileItem = tileItem