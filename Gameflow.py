
from Computer import Computer
from Board import Board
from Ship import Ship
from Tile import Tile


class GameFlow:

    playerGUI = None
    computerAI = None
    playerFleet = []
    computerFleet = []
    playerBoard = None

    def __init__(self):
        self.computerAI = Computer()
        self.playerBoard = Board()


    def placeShips(self):
        shipNames = [Ship("carrier", 5), Ship("battleship", 4), Ship("submarine", 3), Ship("gunboat", 2), Ship("dinghy", 1)]
        directions = ["up", "right", "down", "left"]
        while (not self.playerGUI.donePlacingFleet()):
            self.playerGUI.displayPlacementPhase(self.playerBoard)
            shipSelected = self.playerGUI.selectShip()

            for ship in shipNames:
                if ship.getName() == shipSelected:
                    while (not self.playerGUI.donePlacingShip()): # returns true if the player confirms placement OR player wants to stop placing that ship
                        shipPositions = [self.playerGUI.selectSpot()] #expecting [xCoord, yCoord] return
                        for direction in directions:
                            if(self.playerBoard.placeShip(direction, ship, shipPositions[0][0], shipPositions[0][1])):
                                if direction == "up":
                                    for x in range(ship.getHealth):
                                        shipPositions = shipPositions + [[shipPositions[0][0], shipPositions[0][1] - x]]
                                        self.playerGUI.displayPlacementPhase(self.playerBoard)
                                if direction == "down":
                                    for x in range(ship.getHealth):
                                        shipPositions = shipPositions + [[shipPositions[0][0], shipPositions[0][1] + x]]
                                        self.playerGUI.displayPlacementPhase(self.playerBoard)
                                if direction == "right":
                                    for x in range(ship.getHealth):
                                        shipPositions = shipPositions + [[shipPositions[0][0] + x, shipPositions[0][1]]]
                                        self.playerGUI.displayPlacementPhase(self.playerBoard)
                                if direction == "left":
                                    for x in range(ship.getHealth):
                                        shipPositions = shipPositions + [[shipPositions[0][0] - x, shipPositions[0][1]]]
                                        self.playerGUI.displayPlacementPhase(self.playerBoard)
                                if(self.playerGUI.confirmPlacement): #returns true if player wants the ship in the listed position
                                    self.playerFleet += ship
                                    break
                                else:
                                    for coordinate in shipPositions:
                                        self.playerBoard.setTile(coordinate[0], coordinate[1], "water")
                    break
        for ship in self.playerFleet:
            self.computerAI.shipPlace(ship)
        self.computerFleet = self.playerFleet

    def run(self):
        self.placeShips()
        gameover = False
        playerWins = False
        while not gameover:
            self.playerGUI.displayAttackPhase(self.playerBoard, self.computerAI.getBoard())
            attackCoordinates = self.playerGUI.getAttackPosition() #returns [x,y]
            if (self.computerAI.attackTile(attackCoordinates[0], attackCoordinates[1])):
                for x in range(len(self.computerFleet)):
                    if (self.computerAI.getBoard().getTile(attackCoordinates[0], attackCoordinates[1]).getName() == self.computerFleet[x].getName()):
                        self.computerFleet[x].damageShip()

            gameEnd = True
            for ship in self.computerFleet:
                if ship.getHealth() > 0:
                    gameEnd = False
            if gameEnd:
                playerWins = True
                break

            attackCoordinates = self.computerAI.shipGuess()

            if (self.playerBoard.attackTile(attackCoordinates[0], attackCoordinates[1])):
                for x in range(len(self.playerFleet())):
                    if (self.playerBoard.getTile(attackCoordinates[0], attackCoordinates[1]).getName() == self.playerFleet[x].getName()):
                        self.playerFleet[x].damageShip()

            gameEnd = True
            for ship in self.playerFleet:
                if ship.getHealth() > 0:
                    gameEnd = False
            if gameEnd:
                break

        if playerWins:
            self.playerGUI.displayWin()
        else:
            self.playerGUI.displayLoss()


















gameBeingPlayed = True
while gameBeingPlayed:
    d = Display() #initializes the display
    game = GameFlow(d) #initializes the GameFlow
    game.play() #calls GameFlow's Play function

    playAgain = input("Would you like to play again? y/n: ")
    while playAgain is not 'y' or 'n':
        playAgain = input("Error! Must be a valid response! y/n: ")
    if playAgain == 'n':
        print("Thanks for playing!")
        break
