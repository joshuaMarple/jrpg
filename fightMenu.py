import pygame, random, sys
from pygame.locals import *
from button import button
from vertMenu import vertMenu
from gridMenu import gridMenu
from globals import *

class fightMenu():
    def __init__(self):
        print(WINDOWWIDTH)
        print(WINDOWHEIGHT)
        text = ["test" + str(i) for i in range(4)]
        actions = [lambda : () for i in range(4)]
        gridMenu(0, WINDOWHEIGHT*2/3, WINDOWWIDTH, WINDOWHEIGHT/3, 2, 2, text, actions) 
