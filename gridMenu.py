import pygame, random, sys
from pygame.locals import *
from button import button
from globals import *

class gridMenu(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height, rows, cols, text, actions, group=None):
        # global buttons
        # global all_sprites
        if (len(text) != len(actions)):
            print("error: text and actions not matching")

        self.width = width
        self.height = height
        pygame.sprite.Sprite.__init__(self)
        num_buttons = len(text)
        x_delta = width/rows
        y_delta = height/cols
        col_num = 0
        row_num = 0

        # for i in actions:
            # i()

        
        for i in range(num_buttons):
            # print(actions[i])
            
            new_button = button(xpos+x_delta * col_num, ypos + y_delta * row_num, x_delta, y_delta, text[i], actions[i], False)
            
            buttons.add(new_button)
            all_sprites.add(new_button)
            if group != None:
                group.add(new_button)
            col_num += 1
            if col_num >= cols:
                col_num = 0
                row_num += 1
