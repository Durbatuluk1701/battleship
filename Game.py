import pygame
import sys
from Computer import Computer
from Board import Board
from Ship import Ship
from Tile import Tile
import math
#from Gameflow import Gameflow

#**** Colors *****#
white = (255, 255, 255)
blue = (52, 196, 206)
red = (255, 14, 14)
black = (0, 0, 0)
grey = (161, 139, 117)
#**********#


class Game:
    # constructor of the display, dimensions
    def __init__(self, board_size=25, cell_size=20, margin=15):
        '''
        Display Constructor
        Parameters: N/A
        Returns: N/A
        Preconditions: N/A
        Postconditions: Creates a valid screen, computer, player board, fleet for both computer and player
        '''
        #*****Initializes screen*****#
        self.emptyBoard = Board()
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin
        self.turn = ""
        SCREEN_WIDTH = 470
        self.SCREEN_WIDTH = SCREEN_WIDTH
        SCREEN_HEIGHT = 900
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen = screen
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("ComicSans", 15)  # sets font
        pygame.display.set_caption("Battleship!")  # name of window
        # buffer between top and bottom grid
        self.buffer = math.floor(
            self.margin / 30 + self.board_size * self.cell_size)
        #****************#

    def checkQuit(self, event):
        '''
        checkQuit Method
        Parameters: event
        Returns: N/A
        Preconditions: N/A
        Postconditions: asuming event is exit, quits the game
        '''
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def chooseNumShips(self):
        '''
        chooseNumShips Method
        Parameters: N/A
        Returns: number of ships in the game (1-5)
        Preconditions: N/A
        Postconditions: N/A
        '''
        getNumShips = False
        titlefont = pygame.font.Font('freesansbold.ttf', 20)
        numShips = 0
        while not getNumShips:
            toptext = titlefont.render(
                'Please choose a number of ships (1 - 5)', False, (255, 255, 255))
            self.screen.blit(toptext, (20, 20))
            for event in pygame.event.get():
                self.checkQuit(event)  # checks if user exits

                if event.type == pygame.KEYDOWN:
                    for key in range(1, 6):  # if user presses key 1-5
                        if event.unicode == str(key):
                            # sets fleet size and asks for confirmation
                            numShips = int(event.unicode)
                            self.screen.fill(black)
                            fleetTxt = titlefont.render(
                                'A fleet size of ' + str(key) + ", press enter to confirm", False, white)
                            self.screen.blit(fleetTxt, (20, 50))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and numShips != 0:  # confirms that the user inputted keys
                        getNumShips = True
                        return(numShips)
            pygame.display.flip()  # goes to next frame

    def createDisplayBoard(self, xOffset, yOffset):
        '''
        createDisplayBoard Method
        Parameters: xOffset, yOffset (distance from top left corner in pixels)
        Returns: empty water grid that is created
        Preconditions: N/A
        Postconditions: N/A
        '''
        BLOCK_SIZE = 40
        grid = []
        for y in range(9):  # this is creating the top graph
            row = []
            for x in range(9):
                # creates a 9x9 rectangle grid
                rect = pygame.Rect(xOffset + y*BLOCK_SIZE, x *
                                   BLOCK_SIZE + yOffset, BLOCK_SIZE, BLOCK_SIZE)
                # draws blue squares on it
                pygame.draw.rect(self.screen, blue, rect, 1)
                row.append([rect, blue])
            grid.append(row)
        return grid

    def scanGridClick(self, event, grid):
        '''
        scanGridClick Method
        Parameters: event, and grid you clicked on
        Returns: origin ([x, y], which is the corresponding square you clicked on)
        Preconditions: N/A
        Postconditions: N/A
        '''
        x = 0
        y = 0
        origin = [-1, -1]
        for row in grid:  # bot graph
            for item in row:
                rect, color = item
                if rect.collidepoint(event.pos):
                    # sets the origin to the spot which was clicked on
                    origin = [x, y]
                x = (x + 1) % 9
            y = (y + 1) % 9
        return origin

    def displayGrid(self, grid, board, displayShips):
        '''
        displayGrid Method
        Parameters: grid and corresponding board. displayShips (boolean which says whether to display ships as grey or hide them)
        Returns: N/A
        Preconditions: N/A
        Postconditions: When frame is flipped displays a newly updated board
        '''
        x = 0
        y = 0
        for row in grid:  # this redraws each bot square, with the updated colors
            for item in row:
                if(not board.getTile(x, y).getTileAttacked()):
                    if(displayShips):  # if you want to show the ships on board
                        if(board.getTile(x, y).getTileItem() == "water"):
                            item[1] = blue
                        else:
                            item[1] = grey
                    else:  # if you dont want to show the ships
                        item[1] = blue
                elif board.getTile(x, y).getTileItem() == "water":
                    item[1] = white
                else:
                    item[1] = red

                rect, color = item
                pygame.draw.rect(self.screen, color, rect)
                x = (x + 1) % 9
            y = (y + 1) % 9

    def placeShipPhase(self, player, numShips):
        '''
        placeShipPhase Method
        Parameters: numShips (the number of ships you want the player to place)
        Returns: N/A
        Preconditions: valid player and computer grid
        Postconditions: both players' boards have placed ships, players' fleets have been updated to contain the ships they placed
        '''
        shipNames = [Ship("dinghy", 1), Ship("gunboat", 2), Ship(
            "submarine", 3), Ship("battleship", 4), Ship("carrier", 5)]
        directions = ["up", "right", "down", "left"]
        dir = 0
        shipPlace = 0
        shipPositions = []
        font = pygame.font.Font('freesansbold.ttf', 17)
        self.displayGrid(self.topgrid, self.emptyBoard, True)
        while not shipPlace >= numShips:

            text = font.render('Placing ' + player + ' Ship: ', False, white)
            self.screen.blit(text, (50, int(self.SCREEN_HEIGHT / 2) - 25))
            rect = pygame.Rect(160, int(self.SCREEN_HEIGHT / 2) - 25, 200, 20)
            pygame.draw.rect(self.screen, black, rect)
            text = font.render(shipNames[shipPlace].getName(), False, white)
            self.screen.blit(text, (165, int(self.SCREEN_HEIGHT / 2) - 25))
            text = font.render(
                "click to place, enter to confirm", False, white)
            self.screen.blit(text, (50, int(self.SCREEN_HEIGHT / 2) - 5))

            for event in pygame.event.get():
                self.checkQuit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:  # if mouse clicked

                    # gets the square that you clicked on
                    shipOrigin = self.scanGridClick(event, self.botgrid)
                    if shipOrigin == [-1, -1]:  # if you clicked outside grid
                        break
                    for coordinate in shipPositions:  # deletes old ship placement ****note for first ship ship positions is [] so it skips this step
                        # sets those spots to water
                        (self.player1Board if player == "Player 1" else self.player2Board).setTile(
                            coordinate[0], coordinate[1], "water")

                    shipPlaced = False
                    while not shipPlaced:
                        # everytime you click on a spot increments the direction to the next available spot
                        dir = (dir + 1) % 4
                        shipPlaced = (self.player1Board if player == "Player 1" else self.player2Board).placeShip(
                            directions[dir], shipNames[shipPlace], shipOrigin[0], shipOrigin[1])
                        shipPositions = [shipOrigin]
                    if directions[dir] == "up":
                        for i in range(shipNames[shipPlace].getHealth()):
                            shipPositions = shipPositions + \
                                [[shipPositions[0][0], shipPositions[0][1] - i]]
                    if directions[dir] == "down":
                        for i in range(shipNames[shipPlace].getHealth()):
                            shipPositions = shipPositions + \
                                [[shipPositions[0][0], shipPositions[0][1] + i]]
                    if directions[dir] == "right":
                        for i in range(shipNames[shipPlace].getHealth()):
                            shipPositions = shipPositions + \
                                [[shipPositions[0][0] + i, shipPositions[0][1]]]
                    if directions[dir] == "left":
                        for i in range(shipNames[shipPlace].getHealth()):
                            shipPositions = shipPositions + \
                                [[shipPositions[0][0] - i, shipPositions[0][1]]]
                    # in placing a ship, shipPositions has a duplicate of the  origin spot, so pop that off
                    shipPositions.pop(0)

                elif event.type == pygame.KEYDOWN:  # confirm placement
                    if event.key == pygame.K_RETURN:
                        if(shipPositions != []):  # checks to make sure you placed a ship
                            fleet = self.player1Fleet if player == "Player 1" else self.player2Fleet
                            fleet += [shipNames[shipPlace]]
                            shipPositions = []
                            shipPlace += 1
            # draw all in every loop
            # for row in topgrid: # this redraws each top square, with the updated colors
            #    for item in row:
            #        rect, color = item
            #        pygame.draw.rect(self.screen, color, rect)
            # updates bottom grid to show new values
            self.displayGrid(self.botgrid, self.player1Board, True)

            pygame.display.flip()  # displays the updated frame

        if (self.numPlayers == 1):
            for ship in self.player1Fleet:   # creates computer fleet and places ship on the computer board
                self.computer.shipPlace(ship)
                self.computerFleet += [Ship(ship.getName(), ship.getHealth())]

    def attackPhase(self):
        '''
        attackPhase Method
        Parameters: N/A
        Returns: playerWin (true if player wins, false if computer wins)
        Preconditions: valid player and computer grid and fleet with placed ships
        Postconditions: players take turns attacking until all the ships of one board are sunk, then exits
        '''
        gameOver = False
        playerWin = True
        font = pygame.font.Font('freesansbold.ttf', 17)
        currentBoard = self.player1Board
        currentFleet = self.player1Fleet
        enemyBoard = self.player2Board if self.numPlayers == 2 else self.computer.getBoard()
        enemyFleet = self.player2Fleet if self.numPlayers == 2 else self.computerFleet

        while not gameOver:

            if (self.numPlayers == 1):
                self.turn = "Player 1"

            rect = pygame.Rect(0, int(self.SCREEN_HEIGHT / 2 - 25), 400, 45)
            pygame.draw.rect(self.screen, black, rect)
            text = font.render(
                "Click on top board to attack a tile", False, white)
            self.screen.blit(text, (50, int(self.SCREEN_HEIGHT / 2) - 25))

            for event in pygame.event.get():
                self.checkQuit(event)  # checks to see if exited game

                if event.type == pygame.MOUSEBUTTONDOWN:  # if clicked
                    # gets where clicked on topgrid
                    x, y = self.scanGridClick(event, self.topgrid)
                    if(x == -1 and y == -1):  # if you clicked outside of the board exit event loop
                        break
                    if(enemyBoard.attackTile(x, y)):  # attacks the enemy board
                        hit = False
                        # checks to see if you hit any of the ships
                        for ship in range(len(enemyFleet)):
                            # compares tile name to fleet name
                            if enemyBoard.getTile(x, y).getTileItem() == enemyFleet[ship].getName():
                                # if it matches damages that ship
                                enemyFleet[ship].damageShip()
                                hit = True
                    gameOver = True  # checks if either fleet is completely dead
                    for ship in enemyFleet:
                        if(not ship.isDead()):
                            gameOver = False
                    if(gameOver):
                        self.displayGrid(self.botgrid, currentBoard, True)
                        # Opposite of above
                        self.displayGrid(self.topgrid, enemyBoard, True)
                        pygame.display.flip()  # updates frame
                        return self.turn
                    if (self.numPlayers == 1):
                        x, y = 0, 0
                        currentBoard, enemyBoard = enemyBoard, currentBoard
                        currentFleet, enemyFleet = enemyFleet, currentFleet
                        newTileAttacked = False
                        while(not newTileAttacked):  # ensures that the computer gets a new guess
                            x, y = self.computer.shipGuess()
                            # attack tile returns false if you have already attacked that tile
                            newTileAttacked = enemyBoard.attackTile(x, y)
                        # if it is a hit damages corresponding ship
                        for ship in range(len(enemyFleet)):
                            if enemyBoard.getTile(x, y).getTileItem() == enemyFleet[ship].getName():
                                enemyFleet[ship].damageShip()
                        self.displayGrid(self.botgrid, enemyBoard, True)
                        # Opposite of above
                        self.displayGrid(self.topgrid, currentBoard, False)
                        self.turn = "Computer"
                    else:
                        self.swapTitles(hit)
                        self.swapBoards(currentBoard, enemyBoard)
                        self.turn = "Player 2" if self.turn == "Player 1" else "Player 2"
                    currentBoard, enemyBoard = enemyBoard, currentBoard
                    currentFleet, enemyFleet = enemyFleet, currentFleet

            pygame.display.flip()  # updates frame

            gameOver = True  # checks if either fleet is completely dead
            for ship in enemyFleet:
                if(not ship.isDead()):
                    gameOver = False
            if(gameOver):
                return self.turn
            gameOver = True
            for ship in currentFleet:
                if(not ship.isDead()):
                    gameOver = False
            if(gameOver):
                playerWin = self.turn

        return playerWin  # returns true if player won, false if computer won

    def swapBoards(self, currentBottom, currentTop):
        # Set current top grid to display in bottom
        self.displayGrid(self.botgrid, currentTop, True)
        self.displayGrid(self.topgrid, currentBottom,
                         False)  # Opposite of above

    def swapTitles(self, hit):
        titlefont = pygame.font.Font('freesansbold.ttf', 20)
        hitfont = pygame.font.Font('freesansbold.ttf', 50)
        self.screen.fill(black)

        if self.turn == "Player 1":
            toptext = titlefont.render(
                "Player 2's Turn!", False, (255, 255, 255))
            lowertext = titlefont.render(
                "press enter to continue", False, (255, 255, 255))
        else:
            toptext = titlefont.render(
                "Player 1's Turn!", False, (255, 255, 255))
            lowertext = titlefont.render(
                "press enter to continue", False, (255, 255, 255))

        if hit:
            hittext = hitfont.render("HIT!!", False, (255, 255, 255))
        else:
            hittext = hitfont.render("MISS", False, (255, 255, 255))
        self.screen.blit(toptext, (self.SCREEN_WIDTH /
                                   2 - 85, self.SCREEN_HEIGHT/2))
        self.screen.blit(lowertext, (self.SCREEN_WIDTH/2 -
                                     110, self.SCREEN_HEIGHT/2 + 30))
        self.screen.blit(hittext, (self.SCREEN_WIDTH/2 -
                                   65, self.SCREEN_HEIGHT/2 - 75))
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                self.checkQuit(event)  # check if user exits

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                        self.screen.fill(black)
                        pygame.display.flip()
                        if self.turn == "Player 1":
                            self.fillCoordinates("Player 1", "Player 2")
                        else:
                            self.fillCoordinates("Player 2", "Player 1")

    def selectPlayers(self):
        getNumberPlayers = False
        titlefont = pygame.font.Font('freesansbold.ttf', 20)
        numberPlayers = 0
        while not getNumberPlayers:
            toptext = titlefont.render(
                "Please choose a number of players (1 - 2): ", False, (255, 255, 255))
            self.screen.blit(toptext, (20, 20))
            for event in pygame.event.get():
                self.checkQuit(event)  # check if user exits

                if event.type == pygame.KEYDOWN:
                    for key in range(1, 3):
                        if event.unicode == str(key):
                            numberPlayers = int(event.unicode)
                            self.screen.fill(black)
                            playerText = titlefont.render(
                                "Confirm " + str(key) + " players", False, white)
                            self.screen.blit(playerText, (20, 50))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and numberPlayers != 0:
                        getNumberPlayers = False
                        self.screen.fill(black)
                        pygame.display.flip()
                        return(numberPlayers)
            pygame.display.flip()

    def chooseAIDifficulty(self):
        self.screen.fill(black)
        getAIDifficulty = False
        titlefont = pygame.font.Font('freesansbold.ttf', 20)
        aiDifficulty = 0
        while not getAIDifficulty:
            toptext = titlefont.render(
                "Please choose an AI Difficulty", False, (255, 255, 255))
            lowertext = titlefont.render(
                "(1 = Easy, 2 = Medium, 3 = Hard): ", False, (255, 255, 255))
            self.screen.blit(toptext, (20, 20))
            self.screen.blit(lowertext, (20, 50))
            for event in pygame.event.get():
                self.checkQuit(event)  # check if user exits
                difficultyConverter = ["Easy", "Medium", "Hard"]

                if event.type == pygame.KEYDOWN:
                    for key in range(1, 4):
                        if event.unicode == str(key):
                            aiDifficulty = int(event.unicode)
                            self.screen.fill(black)
                            playerText = titlefont.render(
                                "Confirm " + difficultyConverter[key-1] + " AI Difficulty (Enter)", False, white)
                            self.screen.blit(playerText, (20, 80))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and (aiDifficulty in [1, 2, 3]):
                        getAIDifficulty = True
                        self.screen.fill(black)
                        pygame.display.flip()
                        return(difficultyConverter[aiDifficulty-1])
            pygame.display.flip()

    def game(self):
        '''
        game Method
        Parameters: N/A
        Returns: N/A
        Preconditions: Valid screen created (created in constructor)
        Postconditions: Plays battleship until one person wins then waits to exit
        '''
        self.banger()  # music

        #*****Member Variables of game*****#
        self.player1Board = Board()
        self.player1Fleet = []
        #****************#

        self.numPlayers = self.selectPlayers()  # selects the number of players

        # asks user for the number of ships in the game
        self.numShips = self.chooseNumShips()

        if (self.numPlayers == 1):
            # Computer Variables
            self.computerFleet = []
            aiDifficulty = self.chooseAIDifficulty()
            self.computer = Computer(aiDifficulty)
            # End Computer Variables

        self.turn = "Player 1"

        self.topgrid = self.createDisplayBoard(
            50, 40)  # creates the top "opponent" grid
        self.botgrid = self.createDisplayBoard(
            50, self.buffer)  # creates the bottom "player" grid

        playerWin = ""

        if (self.numPlayers == 1):
            self.fillCoordinates(
                "Opponent Board", "Player Board")  # sets the UI
            self.placeShipPhase("Player 1", self.numShips)  # places ship
            playerWin = self.attackPhase()
        elif (self.numPlayers == 2):
            self.fillCoordinates()  # sets the UI
            # places ships for player 1
            self.placeShipPhase("Player 1", self.numShips)
            self.player2Board = Board()
            self.player2Fleet = []
            self.fillCoordinates()  # sets the UI
            # places ships for player 2
            self.placeShipPhase("Player 2", self.numShips)
            playerWin = self.attackPhase()
        else:
            toptext = pygame.font.Font('freesansbold.ttf', 20).render(
                "NO PLAYERS", False, (255, 255, 255))
            self.screen.blit(toptext, (20, 20))
            return

        quitGame = False
        while not quitGame:
            self.result(playerWin)  # displays if you win or not
            for event in pygame.event.get():
                self.checkQuit(event)  # checks to see if you quit
                if event.type == pygame.KEYDOWN:  # confirm placement
                    if event.key == pygame.K_RETURN:  # quits if hit enter
                        quitGame = True

    def banger(self):
        '''
        banger Method
        Parameters: N/A
        Returns: N/A
        Preconditions: N/A
        Postconditions: plays banger music
        '''

        # pygame.mixer.init()
        #sound = pygame.mixer.Sound("metal.mp3")
        # sound.set_volume(.5)
        # pygame.mixer.music.load("metal.mp3")
        # pygame.mixer.music.play(loops=-1)

        # Metal by Alexander Nakarada | https://www.serpentsoundstudios.com
        # Music promoted by https://www.free-stock-music.com
        # Attribution 4.0 International (CC BY 4.0)
        # https://creativecommons.org/licenses/by/4.0/

    def fillCoordinates(self, topText, bottomText):
        '''
        fillCoordinates Method
        Parameters: N/A
        Returns: N/A
        Preconditions: N/A
        Postconditions: outputs GUI for player with row and column names
        '''
        self.screen.fill(black)
        xCoordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        yCoordinates = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        bottom = 75
        left = 55
        font = pygame.font.Font('freesansbold.ttf', 20)
        titlefont = pygame.font.Font('freesansbold.ttf', 25)
        toptext = titlefont.render(topText, False, (255, 255, 255))
        bottext = titlefont.render(bottomText, False, (255, 255, 255))
        self.screen.blit(toptext, (130, 15))
        self.screen.blit(bottext, (130, 470))

        # for top board Y coordinates
        for y in range(9):
            text = font.render(yCoordinates[y], True, white, black)
            textRect = text.get_rect()
            textRect.bottom = bottom
            textRect.right = 30  # x axis of label
            self.screen.blit(text, textRect)
            bottom = bottom + 40  # distance between characters
        # for top board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 405  # y axis of label
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 41  # distance between characters

        # for bot board Y coordinates
        for y in range(9):
            text = font.render(yCoordinates[y], True, white, black)
            textRect = text.get_rect()
            textRect.bottom = bottom + 100  # y axis of label
            textRect.right = 30
            self.screen.blit(text, textRect)
            bottom = bottom + 40  # distance between characters

        left = 55  # reset left coordinate
        # for bot board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 865  # x axis of labels
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 41  # distance between characters

    def result(self, winner):
        '''
        result Method
        Parameters: winner (who won the game (bool: true if player won, false if computer))
        Returns: N/A
        Preconditions: game finished playing
        Postconditions: displays winner or loser screen
        '''
        red = (255, 0, 0)  # makes red more vibrant
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(winner + ' Wins!', True, black, red)
        textRect = text.get_rect()
        textRect.center = (int(self.SCREEN_WIDTH // 2),
                           int(self.SCREEN_HEIGHT // 2))
        self.screen.blit(text, textRect)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Press enter to quit', True, black, red)
        textRect = text.get_rect()
        textRect.center = (int(self.SCREEN_WIDTH // 2),
                           int(self.SCREEN_HEIGHT // 2) + 30)
        self.screen.blit(text, textRect)
        pygame.display.flip()


mygame = Game()
mygame.game()
pygame.quit()
sys.exit()
