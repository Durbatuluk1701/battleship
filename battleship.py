import pygame
import numpy
import random
from abc import ABC


class GameFlow:

    def __init__(self, display, size = 10):
        self.display = display
        self.boardSize = size


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