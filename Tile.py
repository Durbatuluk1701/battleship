class Tile:
    def __init__(self): # initializes the tile object to be water and not attacked by default
        self.tileItem = "water" # tileItem is a string
        self.attacked = False # attacked is a bool
    def getTileItem(self): # returns the type of tile
        return self.tileItem
    def getTileAttacked(self): # returns the status of the tile, regarding whether or not it's been attacked
        return self.attacked
    def setTileAttacked(self): # sets the status of the tile to attacked
        self.attacked = True
    def setTileItem(self, tileItem): # sets the type of tile
        self.tileItem = tileItem