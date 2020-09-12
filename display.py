import pygame
import sys

class Display:

    colors = { #initalize all colors that will be used
    "water" : pygame.color.Color(21,72,161),
    "ship" : pygame.color.Color(102,51,0),
    "hit" : pygame.color.Color(255,0,0),
    "miss" : pygame.color.Color(235,214,233),
    "background" : pygame.color.Color(0,0,0),
    "text" : pygame.color.Color(255,255,255)
    }

    def __init__ (self, board_size = 20, cell_size = 20, margin = 10): #constructor of the display, dimensions
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin
        self.fill = (0,255,0)
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("ComicSans",15) # sets font
        screen_width = self.cell_size * board_size + 2 * margin # sets width
        screen_height = 2 * self.cell_size *board_size + 3 * margin #sets heigth
        self.screen = pygame.display.set_mode([screen_width, screen_height])
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

mygame = Display()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # the user wants to quit the game
    pygame.display.flip() # updates the visuals on the board

pygame.quit()
