import pygame
import sys

class Display:

    water = (21,72,161)
    ship = (102,51,0)
    hit = (255,0,0)
    miss = (235,214,233)
    background = (0,0,0)
    text = (255,255,255)

    def __init__ (self, board_size = 20, cell_size = 20, margin = 15): #constructor of the display, dimensions
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("ComicSans",15) # sets font
        screen_width = self.cell_size * board_size + 2 * margin # sets width
        self.screen_width = screen_width
        screen_height = 2 * self.cell_size *board_size + 3 * margin #sets heigth
        self.screen_height = screen_height
        screen = pygame.display.set_mode([screen_width, screen_height])
        self.screen = screen
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
        water = (21,72,161)
        grid = []
        for row in range(21):
            grid.append([])
            for column in range(19):
                grid[row].append(0)
        for row in range(20):
            for column in range(9):
                color = water
                if grid[row][column] == 1:
                    color = red
                pygame.draw.rect(mygame.screen,color,[(mygame.margin + mygame.screen_width) * column + mygame.margin, (mygame.margin + mygame.screen_height) * row + mygame.margin, mygame.screen_width, mygame.screen_height])

mygame = Display()
mygame.visual()
running = True
while running:
    pygame.display.flip() # updates the visuals on the board
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # the user wants to quit the game

pygame.quit()
