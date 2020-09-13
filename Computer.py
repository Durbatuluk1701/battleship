import random
from Board import Board
from Ship import Ship
from Tile import Tile
class Computer:
    def __init__(self):
        self.__board__ = Board()
    def getBoard(self):
        return(self.__board__)
    def shipPlace(self, ship): 
        # generate random x,y coordinates
        # check if it can place the ship without going out of bounds
        # if it can, it will place the ship
        # if not, generate another set of coordinates (not the same) and try again until it can place ship
        shipPlaced = False
        while shipPlaced == False:
            xValue = random.randint(0,8)
            yValue = random.randint(0,8)
            print(xValue, yValue)
            if self.__board__.placeShip("up", ship, xValue, yValue):
                shipPlaced = True
            elif self.__board__.placeShip("down", ship, xValue, yValue):
                shipPlaced = True
            elif self.__board__.placeShip("left", ship, xValue, yValue):
                shipPlaced = True
            elif self.__board__.placeShip("right", ship, xValue, yValue):
                shipPlaced = True
            else:
                pass
    def attackTile(self, xCoord, yCoord):
        return(self.__board__.attackTile(xCoord, yCoord))

    def shipGuess(self):
        # generate random x,y coordinates
        # attack those coords, if possible
        
        col = random.randint(0,8)
        row = random.randint(0,8)
        return([row, col])