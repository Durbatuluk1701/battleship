import pygame
import sys

class Display:

    water = (21,72,161)
    ship = (102,51,0)
    hit = (255,0,0)
    miss = (235,214,233)
    background = (0,0,0)
    text = (255,255,255)

    def __init__ (self, board_size = 25, cell_size = 20, margin = 15): #constructor of the display, dimensions
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("ComicSans",15) # sets font
        screen_width = 470 #self.cell_size * board_size + 2 * margin # sets width
        self.screen_width = screen_width
        screen_height = 900 #2 * self.cell_size *board_size + 3 * margin #sets heigth
        self.screen_height = screen_height
        screen = pygame.display.set_mode([screen_width, screen_height])
        self.screen = screen
        self.screen.fill((0,0,0))
        pygame.display.set_caption("Battleship!") #name of window
        clock = pygame.time.Clock()


    def input (self,running = True): # user interaction with the display
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user wnats to quit the game
                Display.close()
            elif event.type == pygame.MOUSEBUTTONDOWN: # when user mouse buttons down
                pos = pygame.mouse.get_pos()
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                self.grid[row][column] = 1 #this indicates a pressed/hit square

    def visual(self):
        white = (255,255,255)
        red = (255,14,14)
        blockSize = 40
        for y in range(9):
            for x in range(9): # this is the top grid
                square = pygame.Rect(50 + x*blockSize, y*blockSize + 40, blockSize, blockSize)
                pygame.draw.rect(mygame.screen, white, square, 1)

        buffer = self.margin / 30 + self.board_size * self.cell_size
        for y in range(9): # this is the bottom grid
            for x in range(9):
                square = pygame.Rect(50 + x*blockSize, y*blockSize + buffer, blockSize, blockSize)
                pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 1)

    def fillCoordinates(self):
        xCoordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        yCoordinates = ['9','8','7','6','5','4','3','2', '1']
        bottom = 75
        left = 55

        black = (0,0,0)
        white = (255, 255, 255)
        font = pygame.font.Font('freesansbold.ttf', 20)

        #for top board Y coordinates
        for y in range(9):
            text = font.render(yCoordinates[y], True, white, black)
            textRect = text.get_rect()
            textRect.bottom = bottom
            textRect.right = 30 # x axis of label
            self.screen.blit(text, textRect)
            bottom = bottom + 40 # y axis of label
        #for top board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 405 # y axis of label
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 42 # x axis of label

        #for bot board Y coordinates
        for y in range(9):
            text = font.render(yCoordinates[y], True, white, black)
            textRect = text.get_rect()
            textRect.bottom = bottom + 100 # y axis of label
            textRect.right = 30
            self.screen.blit(text, textRect)
            bottom = bottom + 40

        left = 55 #reset left coordinate
        # for bot board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 865
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 42



mygame = Display()
mygame.visual()
mygame.fillCoordinates()
running = True
while running:
    pygame.display.flip() # updates the visuals on the board
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # the user wants to quit the game

pygame.quit()
