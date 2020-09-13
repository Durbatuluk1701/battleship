import pygame
import sys
from Computer import Computer
from Board import Board
from Ship import Ship
from Tile import Tile
import math
#from Gameflow import Gameflow

#**** Colors *****#
white = (255,255,255)
blue = (52,196,206)
red = (255,14,14)
black = (0, 0, 0)
grey = (161,139,117)
#**********#

class Game:
    def __init__ (self, board_size = 25, cell_size = 20, margin = 15): #constructor of the display, dimensions
        '''
        Display Constructor
        Parameters: N/A
        Returns: N/A
        Preconditions: N/A
        Postconditions: Creates a valid screen, computer, player board, fleet for both computer and player
        '''
        #*****Initializes screen*****#
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin
        SCREEN_WIDTH = 470
        self.SCREEN_WIDTH = SCREEN_WIDTH
        SCREEN_HEIGHT = 900
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen = screen
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("ComicSans",15) # sets font
        pygame.display.set_caption("Battleship!") #name of window
        self.buffer = math.floor(self.margin / 30 + self.board_size * self.cell_size) #buffer between top and bottom grid
        #****************#
        #*****Member Variables of game*****#
        self.playerBoard = Board()
        self.playerFleet = []
        self.computerFleet = []
        self.computer = Computer() #contains it's own board
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
            toptext = titlefont.render('Please choose a number of ships (1 - 5)', False, (255,255,255))
            self.screen.blit(toptext,(20,20))
            for event in pygame.event.get():
                self.checkQuit(event)

                if event.type == pygame.KEYDOWN:
                    for key in range(1, 6):
                        if event.unicode == str(key):
                            numShips = int(event.unicode)
                            self.screen.fill(black)
                            fleetTxt = titlefont.render('A fleet size of ' + str(key) + ", press enter to confirm", False, white)
                            self.screen.blit(fleetTxt, (20,50))

                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and numShips != 0:
                                getNumShips = True
                                return(numShips)
            pygame.display.flip()

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
        for y in range(9): # this is creating the top graph
            row = []
            for x in range(9):
                rect = pygame.Rect(xOffset + y*BLOCK_SIZE, x*BLOCK_SIZE + yOffset, BLOCK_SIZE, BLOCK_SIZE )
                pygame.draw.rect(self.screen,blue,rect,1)
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
        origin = [-1,-1]
        for row in grid: #bot graph
            for item in row:
                rect, color = item
                if rect.collidepoint(event.pos):
                    origin = [x,y]
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
        for row in grid: # this redraws each bot square, with the updated colors
            for item in row:
                if(not board.getTile(x, y).getTileAttacked()):
                    if(displayShips):
                        if(self.playerBoard.getTile(x, y).getTileItem() == "water"):
                            item[1] = blue
                        else:
                            item[1] = grey
                    else:
                        item[1] = blue
                elif board.getTile(x, y).getTileItem() == "water":
                    item[1] = white
                else:
                    item[1] = red
                
                rect, color = item
                pygame.draw.rect(self.screen, color, rect)
                x = (x + 1) % 9
            y = (y + 1) % 9

    def placeShipPhase(self, numShips):
        '''
        placeShipPhase Method
        Parameters: numShips (the number of ships you want the player to place)
        Returns: N/A
        Preconditions: valid player and computer grid
        Postconditions: both players' boards have placed ships, players' fleets have been updated to contain the ships they placed
        '''
        shipNames = [Ship("dinghy", 1),Ship("gunboat", 2), Ship("submarine", 3), Ship("battleship", 4), Ship("carrier", 5)]
        directions = ["up", "right", "down", "left"]
        dir = 0
        shipPlace = 0
        shipPositions = []
        self.displayGrid(self.topgrid, self.computer.getBoard(), True)
        while not shipPlace >= numShips:
            for event in pygame.event.get():
                self.checkQuit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                     #check which rect was clicked and change its color on list
                    #for row in topgrid: # top graph
                    #    for item in row:
                    #        rect, color = item
                    #        if rect.collidepoint(event.pos):
                    #            if color == blue: # here we can say if (hit = true) set to red, or if (hit = false) set to white etc...
                    #                item[1] = red
                    shipOrigin = self.scanGridClick(event, self.botgrid)
                    if shipOrigin == [-1, -1]:
                        break
                    for coordinate in shipPositions:
                        self.playerBoard.setTile(coordinate[0], coordinate[1], "water")
                    shipPlaced = False
                    while not shipPlaced:
                        dir = (dir + 1) % 4
                        shipPlaced = self.playerBoard.placeShip(directions[dir], shipNames[shipPlace], shipOrigin[0], shipOrigin[1])
                        shipPositions = [shipOrigin]
                    if directions[dir] == "up":
                        for i in range( shipNames[shipPlace].getHealth()):
                            shipPositions = shipPositions + [[shipPositions[0][0], shipPositions[0][1] - i]]
                    if directions[dir] == "down":
                        for i in range( shipNames[shipPlace].getHealth()):
                            shipPositions = shipPositions + [[shipPositions[0][0], shipPositions[0][1] + i]]
                    if directions[dir] == "right":
                        for i in range( shipNames[shipPlace].getHealth()):
                            shipPositions = shipPositions + [[shipPositions[0][0] + i, shipPositions[0][1]]]
                    if directions[dir] == "left":
                        for i in range( shipNames[shipPlace].getHealth()):
                            shipPositions = shipPositions + [[shipPositions[0][0] - i, shipPositions[0][1]]]
                    shipPositions.pop(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if(shipPositions != []):
                            self.playerFleet += [shipNames[shipPlace]]
                            shipPositions = []
                            shipPlace += 1

            # draw all in every loop
            #for row in topgrid: # this redraws each top square, with the updated colors
            #    for item in row:
            #        rect, color = item
            #        pygame.draw.rect(self.screen, color, rect)
            self.displayGrid(self.botgrid, self.playerBoard, True)
            
            pygame.display.flip()

        for ship in self.playerFleet:
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
        while not gameOver:
            
            for event in pygame.event.get():
                self.checkQuit(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = 0
                    y = 0
                    clickedTop = False
                    for row in self.topgrid: #bot graph
                        for item in row:
                            rect = item[0]
                            if rect.collidepoint(event.pos):
                                clickedTop = True
                                if(self.computer.attackTile(x, y)):
                                    for ship in range(len(self.computerFleet)):
                                        if self.computer.getBoard().getTile(x, y).getTileItem() == self.computerFleet[ship].getName():
                                            self.computerFleet[ship].damageShip()       
                            x = (x + 1) % 9
                        y = (y + 1) % 9
                    if clickedTop:
                        x, y = 0, 0
                        newTileAttacked = False
                        while(not newTileAttacked):
                            x, y = self.computer.shipGuess()
                            newTileAttacked = self.playerBoard.attackTile(x, y)
                        for ship in range(len(self.playerFleet)):
                            if self.playerBoard.getTile(x, y).getTileItem() == self.playerFleet[ship].getName():
                                self.playerFleet[ship].damageShip()
                        
                        for ship in self.playerFleet:
                            print("p: " + ship.getName() + " " + str(ship.getHealth()))
                        for ship in self.computerFleet:
                            print("c: " + ship.getName() + " " + str(ship.getHealth()))
            
            self.displayGrid(self.botgrid,self.playerBoard, True)
            self.displayGrid(self.topgrid,self.computer.getBoard(), False)
            
            pygame.display.flip()
            gameOver = True
            for ship in self.computerFleet:
                if(not ship.isDead()):
                    gameOver = False
            if(gameOver):
                break
            gameOver = True
            for ship in self.playerFleet:
                if(not ship.isDead()):
                    gameOver = False
            if(gameOver):
                playerWin = False
                break
        return playerWin

    def game(self):
        '''
        game Method
        Parameters: N/A
        Returns: N/A
        Preconditions: Valid screen created (created in constructor)
        Postconditions: Plays battleship until one person wins then waits to exit
        '''
        self.banger() # music
        numShips = self.chooseNumShips() #asks user for the number of ships in the game

        self.topgrid = self.createDisplayBoard(50, 40)          #creates the top "opponent" grid
        self.botgrid = self.createDisplayBoard(50, self.buffer) #creates the bottom "player" grid

        self.fillCoordinates()
        self.placeShipPhase(numShips)
        playerWin = self.attackPhase()
        
        while True:
            self.result(playerWin)
            for event in pygame.event.get():
                self.checkQuit(event)

    def banger (self):
        '''
        banger Method
        Parameters: N/A
        Returns: N/A
        Preconditions: N/A
        Postconditions: plays banger music
        '''
        pygame.mixer.init()
        #pygame.init()
        #sound = pygame.mixer.Sound("metal.mp3")
        #sound.set_volume(.5)a
        #pygame.mixer.music.load("metal.mp3")
        #pygame.mixer.music.play(loops=-1)

        #Metal by Alexander Nakarada | https://www.serpentsoundstudios.com
        #Music promoted by https://www.free-stock-music.com
        #Attribution 4.0 International (CC BY 4.0)
        #https://creativecommons.org/licenses/by/4.0/

    def fillCoordinates(self):
        '''
        fillCoordinates Method
        Parameters: N/A
        Returns: N/A
        Preconditions: N/A
        Postconditions: outputs GUI for player with row and column names
        '''
        self.screen.fill(black)
        xCoordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        yCoordinates = ['1','2','3','4','5','6','7','8', '9']
        bottom = 75
        left = 55
        font = pygame.font.Font('freesansbold.ttf', 20)
        titlefont = pygame.font.Font('freesansbold.ttf', 25)
        toptext = titlefont.render('Opponent Board', False, (255,255,255))
        bottext = titlefont.render('Player Board', False,(255,255,255))
        self.screen.blit(toptext,(130,15))
        self.screen.blit(bottext,(130,470))
        

        #for top board Y coordinates
        for y in range(9):
            text = font.render(yCoordinates[y], True, white, black)
            textRect = text.get_rect()
            textRect.bottom = bottom
            textRect.right = 30 # x axis of label
            self.screen.blit(text, textRect)
            bottom = bottom + 40 # distance between characters
        #for top board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 405 # y axis of label
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 41 # distance between characters

        #for bot board Y coordinates
        for y in range(9):
            text = font.render(yCoordinates[y], True, white, black)
            textRect = text.get_rect()
            textRect.bottom = bottom + 100 # y axis of label
            textRect.right = 30
            self.screen.blit(text, textRect)
            bottom = bottom + 40 # distance between characters

        left = 55 #reset left coordinate
        # for bot board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 865 # x axis of labels
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 41 # distance between characters

    def result(self, winner):
        '''
        result Method
        Parameters: winner (who won the game (bool: true if player won, false if computer))
        Returns: N/A
        Preconditions: game finished playing
        Postconditions: displays winner or loser screen
        '''
        black = (0,0,0)
        red = (255, 0, 0)
        font = pygame.font.Font('freesansbold.ttf', 50)
        if winner == True:
            text = font.render('You Win!', True, black, red)
            textRect = text.get_rect()
            textRect.center = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)
            self.screen.blit(text, textRect)
        else:
            text = font.render('You Lose!', True, black, red)
            textRect = text.get_rect()
            textRect.center = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)
            self.screen.blit(text, textRect)
        pygame.display.flip()

mygame = Game()
mygame.game()
