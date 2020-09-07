import random
from Board import Board
from Ship import Ship
from Tile import Tile
class Computer:
    def __init__(self):
        self.__board__ = Board
    def shipPlace(self, ship): 
        # generate random x,y coordinates
        # check if it can place the ship without going out of bounds
        # if it can, it will place the ship
        # if not, generate another set of coordinates (not the same) and try again until it can place ship
        shipPlaced = False
        while shipPlaced == False:
            xValue = random.randint(0,9)
            yValue = random.randint(0,9)
            if (self.__board__.placeShip(self, "up", ship, xValue, yValue)):
                shipPlaced == True
            elif (self.__board__.placeShip(self, "down", ship, xValue, yValue)):
                shipPlaced == True
            elif (self.__board__.placeShip(self, "left", ship, xValue, yValue)):
                shipPlaced == True
            elif (self.__board__.placeShip(self, "right", ship, xValue, yValue)):
                shipPlaced == True
            else:
                pass
    def shipGuess(self):
        # check if it has hit a ship before
        # if it has, check the adjacent tiles until it fully sinks the ship
        # if it hasn't hit something before, generate random x,y coordinates
        # attack those coords
        print ("This is a placeholder for Dawson's code. :)")