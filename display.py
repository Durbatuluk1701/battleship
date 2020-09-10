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
                x, y = pygame.mouse.get_pos()
                y = y % (self.board_size * self.cell_size + self.margin)
                x = (x - self.margin) // self.cell_size
                y = (y - self.margin) // self.cell_size
                if x in range(self.board_size) and y in range(self.board_size):
                    return x, y
        return None, None

    def visual(self):
        white = (255,255,255)
        blockSize = 40
        for y in range(9):
            for x in range(9):
                square = pygame.Rect(50 + x*blockSize, y*blockSize + 40, blockSize, blockSize)
                pygame.draw.rect(mygame.screen, white, square, 1)

        buffer = self.margin / 30 + self.board_size * self.cell_size # 30 + 25 * 15
        for y in range(9):
            for x in range(9):
                square = pygame.Rect(50 + x*blockSize, y*blockSize + buffer, blockSize, blockSize)
                pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 1)

mygame = Display()
mygame.visual()
running = True
while running:
    pygame.display.flip() # updates the visuals on the board
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # the user wants to quit the game

pygame.quit()
