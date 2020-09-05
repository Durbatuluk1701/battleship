import Tile.py
import Ship.py

class Board:
    __tileArray__ = [[]]

    def __init__(self):
        for y in range(9):
            tileRow = []
            for x in range(9):
                tileRow = tileRow + [Tile()]
            self.__tileArray__ = self.__tileArray__ + [tileRow]

    def placeShip(self, direction, ship, xCoord, yCoord):
        if (xCoord > 8 or yCoord > 8 or xCoord < 0 or yCoord < 0):
            raise Exception("Error Invalid X or Y bound to place a ship") 
        if (direction == "up"):
            if ((ship.getHealth - yCoord) < 0):
                return False
            for y in range(ship.getHealth):
                self.__tileArray__[yCoord - y][xCoord].setTileItem(ship.getName)
        if (direction == "down"):
            if ((ship.getHealth + yCoord) > 8):
                return False
            for y in range(ship.getHealth):
                self.__tileArray__[yCoord + y][xCoord].setTileItem(ship.getName)
        if (direction == "left"):
            if ((ship.getHealth - xCoord) > 0):
                return False
            for x in range(ship.getHealth):
                self.__tileArray__[yCoord][xCoord - x].setTileItem(ship.getName)
        if (direction == "down"):
            if ((ship.getHealth + xCoord) > 8):
                return False
            for x in range(ship.getHealth):
                self.__tileArray__[yCoord][xCoord + x].setTileItem(ship.getName)
        return True
    
    def attackTile(self, xCoord, yCoord):
        if (xCoord > 8 or yCoord > 8 or xCoord < 0 or yCoord < 0):
            raise Exception("Error Invalid X or Y bound to attack a tile")
        self.__tileArray__[yCoord][xCoord].setTileAttacked()
    
    def getBoard(self):
        return self.__tileArray__




