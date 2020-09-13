import pygame
import sys
from Computer import Computer
from Board import Board
from Ship import Ship
from Tile import Tile
import math
#from Gameflow import Gameflow

class Display:
    #__battleship__ = Gameflow()

    def __init__ (self, board_size = 25, cell_size = 20, margin = 15): #constructor of the display, dimensions
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
        clock = pygame.time.Clock()
        self.playerBoard = Board()
        self.playerFleet = []
        self.computerFleet = []
        self.computer = Computer()

    def graphs (self):
        self.banger()
        SCREEN_WIDTH = 470
        SCREEN_HEIGHT = 900
        BLOCK_SIZE = 40
        white = (255,255,255)
        blue = (52,196,206)
        red = (255,14,14)
        black = (0, 0, 0)
        grey = (161,139,117)
        buffer = math.floor(self.margin / 30 + self.board_size * self.cell_size)
        pygame.init()
        frame = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        getNumShips = False
        numShips = 0
        titlefont = pygame.font.Font('freesansbold.ttf', 20)

        while not getNumShips:
            toptext = titlefont.render('Please choose a number of ships (1 - 5)', False, (255,255,255))
            self.screen.blit(toptext,(20,20))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return("quit the game")
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    for key in range(1, 6):
                        if event.unicode == str(key):
                            numShips = int(event.unicode)
                            self.screen.fill(black)
                            fleetTxt = titlefont.render('A fleet size of ' + str(key) + ", press enter to confirm", False, (255,255,255))
                            
                            self.screen.blit(fleetTxt, (20,50))

                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and numShips != 0:
                                 
                                 getNumShips = True
            pygame.display.flip()



        # create list with all rects
        topgrid = []
        botgrid = []
        for y in range(9): # this is creating the top graph
            row = []
            for x in range(9):
                rect = pygame.Rect(50 + y*BLOCK_SIZE, x*BLOCK_SIZE + 40, BLOCK_SIZE, BLOCK_SIZE )
                pygame.draw.rect(frame,blue,rect,1)
                row.append([rect, blue])
            topgrid.append(row)

        for y in range(9): # this is creating the bottom graph
            row = []
            for x in range(9):
                rect = pygame.Rect(50 + x*BLOCK_SIZE, y*BLOCK_SIZE + buffer, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(frame,blue,rect,1)
                row.append([rect,blue])
            botgrid.append(row)
        self.fillCoordinates()

        shipNames = [Ship("dinghy", 1),Ship("gunboat", 2), Ship("submarine", 3), Ship("battleship", 4), Ship("carrier", 5)]
        directions = ["up", "right", "down", "left"]
        dir = 0
        shipPlace = 0
        shipPositions = []
        while not shipPlace >= numShips:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return("quit the game")
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                     #check which rect was clicked and change its color on list
                    #for row in topgrid: # top graph
                    #    for item in row:
                    #        rect, color = item
                    #        if rect.collidepoint(event.pos):
                    #            if color == blue: # here we can say if (hit = true) set to red, or if (hit = false) set to white etc...
                    #                item[1] = red
                    x = 0
                    y = 0
                    for row in botgrid: #bot graph
                        for item in row:
                            rect, color = item
                            if rect.collidepoint(event.pos):
                                shipOrigin = [x,y]
                                for coordinate in shipPositions:
                                
                                    self.playerBoard.setTile(coordinate[0], coordinate[1], "water")
                                shipPlaced = False
                                while not shipPlaced:
                                    dir = (dir + 1) % 4
                                    """ if color == blue:
                                        dir = 1
                                        if x > 8 - shipNames[shipPlace].getHealth() - 1:
                                            dir = 2
                                        else:
                                            dir = 3 """
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
                            x = (x + 1) % 9
                        y = (y + 1) % 9
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.playerFleet += [shipNames[shipPlace]]
                        shipPositions = []
                        shipPlace += 1

            # draw all in every loop
            #for row in topgrid: # this redraws each top square, with the updated colors
            #    for item in row:
            #        rect, color = item
            #        pygame.draw.rect(frame, color, rect)
            x = 0
            y = 0
            for row in botgrid: # this redraws each bot square, with the updated colors
                for item in row:
                    if(self.playerBoard.getTile(x, y).getTileItem() == "water"):
                        item[1] = blue
                    else:
                        item[1] = grey
                    rect, color = item
                    pygame.draw.rect(frame, color, rect)
                    x = (x + 1) % 9
                y = (y + 1) % 9
            pygame.display.flip()

        for ship in self.playerFleet:
            self.computer.shipPlace(ship)
            self.computerFleet += [Ship(ship.getName(), ship.getHealth())]
        gameOver = False
        playerWin = True
        while not gameOver:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return("quit the game")
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x = 0
                    y = 0
                    clickedTop = False
                    for row in topgrid: #bot graph
                        for item in row:
                            rect, color = item
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
            x = 0
            y = 0
            for row in botgrid: # this redraws each bot square, with the updated colors
                for item in row:
                    if(not self.playerBoard.getTile(x, y).getTileAttacked()):
                        if(self.playerBoard.getTile(x, y).getTileItem() == "water"):
                            item[1] = blue
                        else:
                            item[1] = grey
                    elif self.playerBoard.getTile(x, y).getTileItem() == "water":
                        item[1] = white
                    else:
                        item[1] = red
                    
                    rect, color = item
                    pygame.draw.rect(frame, color, rect)
                    x = (x + 1) % 9
                y = (y + 1) % 9
            x = 0
            y = 0
            for row in topgrid: # this redraws each bot square, with the updated colors
                for item in row:
                    if(not self.computer.getBoard().getTile(x, y).getTileAttacked()):
                        item[1] = blue
                    elif self.computer.getBoard().getTile(x, y).getTileItem() == "water":
                        item[1] = white
                    else:
                        item[1] = red
                    rect, color = item
                    pygame.draw.rect(frame, color, rect)
                    x = (x + 1) % 9
                y = (y + 1) % 9
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
        while True:
            self.result(playerWin)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return("quit the game")
                    pygame.quit()
                    sys.exit()   



    def banger (self):
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
        SCREEN_WIDTH = 470
        SCREEN_HEIGHT = 900
        white = (255,255,255)
        blue = (52,196,206)
        red = (255,14,14)
        pygame.init()
        frame = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        xCoordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        yCoordinates = ['1','2','3','4','5','6','7','8', '9']
        bottom = 75
        left = 55
        black = (0,0,0)
        white = (255, 255, 255)
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
            frame.blit(text, textRect)
            bottom = bottom + 40 # distance between characters
        #for top board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 405 # y axis of label
            textRect.left = left
            frame.blit(text, textRect)
            left = left + 41 # distance between characters

        #for bot board Y coordinates
        for y in range(9):
            text = font.render(yCoordinates[y], True, white, black)
            textRect = text.get_rect()
            textRect.bottom = bottom + 100 # y axis of label
            textRect.right = 30
            frame.blit(text, textRect)
            bottom = bottom + 40 # distance between characters

        left = 55 #reset left coordinate
        # for bot board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 865 # x axis of labels
            textRect.left = left
            frame.blit(text, textRect)
            left = left + 41 # distance between characters

    def result(self, winner):
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

mygame = Display()
#mygame.result(self,True)
mygame.graphs()
pygame.quit()
