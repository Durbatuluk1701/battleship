import random
from Board import Board
from Ship import Ship
from Tile import Tile
"""
Computer Class
This class serves as the 2nd Player in the Battleship game.
The Computer class has its own Board object and methods to
place its own ships, and attack the opposing Player.
"""
class Computer:
    """
    Default Constructor
    Parameters: n/a
    Returns: n/a
    Preconditions: n/a
    Postconditions: A Computer object is created with a default Board object within it.
    """
    def __init__(self):
        self.__board__ = Board()
    """
    Get Board Method
    Parameters: n/a
    Returns: The Board object of the Computer.
    Preconditions: The Board of the Computer is created.
    Postconditions: n/a
    """
    def getBoard(self):
        return(self.__board__)
    """
    Ship Place Method
    Parameters: A Ship object is passed in to the method.
    Returns: n/a
    Preconditions: A Board object is created and valid Ship object is passed in.
    Postconditions: The Computer places the Ship that is passed in onto its Board.
    """
    def shipPlace(self, ship): 
        # generate random x,y coordinates
        # check if it can place the ship without going out of bounds
        # if it can, it will place the ship
        # if not, generate another set of coordinates (not the same) and try again until it can place ship
        shipPlaced = False
        while shipPlaced == False:
            xValue = random.randint(0,9)
            yValue = random.randint(0,9)
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
    """
    Attack Tile Method
    Parameters: An x coordinate and a y coordinate (both ints) for the Board.
    Returns: True if the Tile has been attacked before, False otherwise.
    Preconditions: A Board object is created and valid coordinates are passed in.
    Postconditions: The Tile of the Board at the specified coordinates is attacked, if possible.
    """
    def attackTile(self, xCoord, yCoord):
        return(self.__board__.attackTile(xCoord, yCoord))
    """
    Ship Guess Method
    Parameters: n/a
    Returns: n/a
    Preconditions: A Board object is created.
    Postconditions: The Computer attacks the Tile at the randomly generated coordinates.
    """
    def shipGuess(self):
        # generate random x,y coordinates
        # attack those coords, if possible
        openTile = False
        while(openTile == False):
            col = random.randint(0,9)
            row = random.randint(0,9)
            if self.__board__.attackTile(col,row):
                openTile = True
            else:
                openTile = False