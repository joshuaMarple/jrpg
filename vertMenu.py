import pygame, random, sys
from pygame.locals import *
from button import button

RED = (255, 0, 0)
GRAY = (78, 99, 91)
PURPLE = (55, 43, 148)
BLACK = (0,0,0)

class vertMenu(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height, text, actions):
        if (text.length() != actions.length()):
            print("error: text and actions not matching")

        self.width = width
        self.height = height
        pygame.sprite.Sprite.__init__(self)
