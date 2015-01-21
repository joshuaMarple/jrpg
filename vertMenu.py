import pygame, random, sys
from pygame.locals import *
from button import button
from globals import *

RED = (255, 0, 0)
GRAY = (78, 99, 91)
PURPLE = (55, 43, 148)
BLACK = (0,0,0)

class vertMenu(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height, text, actions):
        global buttons
        global all_sprites
        if (len(text) != len(actions)):
            print("error: text and actions not matching")

        self.width = width
        self.height = height
        pygame.sprite.Sprite.__init__(self)
        num_buttons = len(text)
        delta = width/num_buttons
        for i in range(num_buttons):
            new_button = button(xpos+delta * i, ypos, delta, height, text[i], actions[i], False)
            buttons.add(new_button)
            all_sprites.add(new_button)
            
            
            
