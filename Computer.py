import random
from Board import Board
from Ship import Ship
from Tile import Tile

# Computer Class
# Purpose: Controls the Interactions of the AI with the Game, only created if Single Player Mode


class Computer:
    def __init__(self, difficulty):
        """
        Default Constructor
        Parameters: difficulty (The difficulty of the AI ["easy", "medium", "hard"])
        Returns: n/a
        Preconditions: n/a
        Postconditions: A Computer object is created with default board, difficulty set, and default direction and medium ai control variables
        """
        self.__board__ = Board()
        self.difficulty = difficulty
        self.hit = False
        self.hitCoord = [0, 0]
        self.origHit = [0, 0]
        self.direction = "up"
        self.directionTranslation = {
            "up": "left", "left": "down", "down": "right", "right": "up"}
        self.goodDirection = False

    def getDifficulty(self):
        """
        getDifficulty Method
        Parameters: n/a
        Returns: AI Difficulty as a string
        Preconditions: n/a
        Postconditions: Returns the String diffculty
        """
        return (self.difficulty)

    def setHit(self, x, y):
        '''
        setHit Method
        Parameters: x (x-coordinate of hit), y (y-coordinate of hit)
        Returns: NA
        Preconditions: Game has started, Medium AI selected single player mode, Computer has hit enemy board
        Postconditions: Medium AI hit, hitCoord, and origHit are updates according to params
        '''
        if (not self.hit):
            self.origHit = [x, y]
        self.hit = True
        self.hitCoord = [x, y]

    def unSetHit(self):
        '''
        unSetHit Method
        Parameters: NA
        Returns: NA
        Preconditions: Same as setHit, + AI has sunk enemy ship
        Postconditions: Medium AI control variables are reset, and origHit is set back to [0,0]
        '''
        self.hit = False
        self.origHit = [0, 0]

    def getBoard(self):
        """
        getBoard Method
        Parameters: n/a
        Returns: The Board object of the Computer.
        Preconditions: The Board of the Computer is created.
        Postconditions: n/a
        """
        return(self.__board__)

    def shipPlace(self, ship):
        """
        shipPlace Method
        Parameters: A Ship object is passed in to the method.
        Returns: n/a
        Preconditions: A Board object is created and valid Ship object is passed in.
        Postconditions: The Computer places the Ship that is passed in onto its Board.
        """
        # generate random x,y coordinates
        # check if it can place the ship without going out of bounds
        # if it can, it will place the ship
        # if not, generate another set of coordinates (not the same) and try again until it can place ship
        directions = ["up", "right", "down", "left"]
        shipPlaced = False
        while shipPlaced == False:
            xValue = random.randint(0, 8)
            yValue = random.randint(0, 8)
            rotation = random.randint(0, 3)
            if self.__board__.placeShip(directions[rotation], ship, xValue, yValue):
                shipPlaced = True
            else:
                pass

    def attackTile(self, xCoord, yCoord):
        """
        attackTile Method
        Parameters: An x coordinate and a y coordinate (both ints) for the Board.
        Returns: True if the Tile has been attacked before, False otherwise.
        Preconditions: A Board object is created and valid coordinates are passed in.
        Postconditions: The Tile of the Board at the specified coordinates is attacked, if possible.
        """
        return(self.__board__.attackTile(xCoord, yCoord))

    def shipGuess(self, arrship, attackTileFn):
        """
        shipGuess Method
        Parameters: arrship (array of ships for hard ai), attackTileFn (function on enemy board to ensure no duplicate tiles hit)
        Returns: [x coordiate of attack, y coordinate of attack, True||False for whether unique tile is hit]
        Preconditions: A Board object is created, AI Difficulty has been selected and set in constructor
        Postconditions: The Computer returns coordinates of where it will be attacking, and the enemyBoard reflects changes where computer has attacked
        """
        # generate random x,y coordinates
        # attack those coords, if possible
        if(self.difficulty == "Hard"):
            if (len(arrship) != 0):
                col = arrship[0][0][1]
                row = arrship[0][0][0]
                arrship[0][0].pop(0)
                arrship[0][0].pop(0)
                return([row, col, attackTileFn(row, col)])
        elif(self.difficulty == "Medium"):
            col = random.randint(0, 8)
            row = random.randint(0, 8)
            validCoord = False
            newTile = True
            directionsHit = 0
            if (self.hit):
                # While the coordinates are not valid (within game bounds) and tile is not unique, repeatedly guess
                while (not validCoord or not newTile):
                    # if every direction guessed, restart at original hit and turn around
                    if (directionsHit == 4):
                        self.hitCoord = self.origHit
                        self.direction = self.directionTranslation[self.direction]
                        directionsHit = 0
                    if (not self.goodDirection):
                        self.direction = self.directionTranslation[self.direction]
                    if (self.direction == "up"):
                        col = self.hitCoord[1] + 1
                        row = self.hitCoord[0]
                        directionsHit += 1
                    if (self.direction == "down"):
                        col = self.hitCoord[1] - 1
                        row = self.hitCoord[0]
                        directionsHit += 1
                    if (self.direction == "right"):
                        row = self.hitCoord[0] + 1
                        col = self.hitCoord[1]
                        directionsHit += 1
                    if (self.direction == "left"):
                        row = self.hitCoord[0] - 1
                        col = self.hitCoord[1]
                        directionsHit += 1
                    if (row in range(0, 9) and col in range(0, 9)):
                        validCoord = True
                        newTile = attackTileFn(row, col)
                        if (newTile):
                            self.goodDirection = True
                        else:
                            self.goodDirection = False
                    else:
                        self.goodDirection = False
            else:
                newTile = attackTileFn(row, col)

            return([row, col, newTile])
        elif(self.difficulty == "Easy"):  # Is already completed
            col = random.randint(0, 8)
            row = random.randint(0, 8)
            return([row, col, attackTileFn(row, col)])
