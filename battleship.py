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
