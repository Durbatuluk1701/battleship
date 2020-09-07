import pygame
import sys

class Display:

    ocean = (52,196,206) #colors and dimensions
    black = (0,0,0)
    red = (255,14,14) # this is a hit
    brown = (94,45,8) # this is a ship
    width = 20
    height = 20
    margin = 5


    grid = []
    for row in range(21):
        grid.append([])
        for column in range(19):
            grid[row].append(0)


    pygame.init()
    window_size = [510,600] # dimensions of the window
    screen = pygame.display.set_mode(window_size) #puts game in windowed mode
    pygame.display.set_caption("Battleship!") # name of window
    done = False # loop condition
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN: #when user mouse buttons down
                pos = pygame.mouse.get_pos()
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                grid[row][column] = 1 #this indicates a pressed/hit square


        screen.fill(black) #background color
        for row in range(20): #player grid being drawn
            for column in range(9):
                color = ocean
                if grid[row][column] == 1:
                    color = red
                pygame.draw.rect(screen,color,[(margin + width) * column + margin,(margin + height) * row +margin, width, height] )
        if grid [row][9]:
            color = black



        clock.tick(30) #frame rate
        pygame.display.flip() # updates the board

    pygame.quit()
