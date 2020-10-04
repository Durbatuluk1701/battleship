
class Tile:
    # Class: Tile
    # Purpose: To act as the tiles that fill up the board, each tile can be used as a ship, or water

    def __init__(self):
        '''
        Parameters: n/a
        Return: n/a
        Preconditions: Must create a Tile object.
        Postconditions: Sets the grid tile to "water" and that it hasn't been attacked yet.
        '''

        self.tileItem = "water"  # tileItem is a string
        self.attacked = False  # attacked is a bool

    def getTileItem(self):
        '''
        Parameters: n/a
        Return: returns tileItem
        Preconditions: Must create a Tile object.
        Postconditions: returns what is in the tile at a specific grid space.
        '''

        return self.tileItem

    def getTileAttacked(self):
        '''
        Parameters: n/a
        Return: returns attacked.
        Preconditions: Must create a Tile object.
        Postconditions: returns the bool of if the grid space has already been attacked.
        '''

        return self.attacked

    def setTileAttacked(self):
        '''
        Parameters: n/a
        Return: n/a
        Preconditions: Must create a Tile object.
        Postconditions: Sets the tile to True showing it has been attacked.
        '''

        self.attacked = True

    def setTileItem(self, tileItem):
        '''
        Parameters: tileItem
        Return: n/a
        Preconditions: Must create a Tile object.
        Postconditions: Sets the tile to the parameter of tileItem.
        '''

        self.tileItem = tileItem
