import pygame, random, sys
from pygame.locals import *
from button import button
from info import info
from vertMenu import vertMenu
from gridMenu import gridMenu
from globals import *

class fightMenu():
    def __init__(self):
        self.fight_buttons = pygame.sprite.Group()
        # text = ["test" + str(i) for i in range(4)]
        text = ["Fight", "Magic", "Items", "Run"]
        actions = [lambda : () for i in range(4)]
        gridMenu(0, WINDOWHEIGHT*2/3, WINDOWWIDTH*3/4, WINDOWHEIGHT/3, 2, 2, text, actions, self.fight_buttons)
        new_info = info(WINDOWWIDTH * 3/4, WINDOWHEIGHT *2/3, WINDOWWIDTH * 1/4, WINDOWHEIGHT/3, "Player 1 | 10 \n Player 2 | 12 \n Player 3 | 21", "right")
        self.fight_buttons.add(new_info)
        all_sprites.add(new_info)
        self.hidden = False

    def show(self):
        for i in self.fight_buttons:
            if all_sprites not in i.groups():
                all_sprites.add(i)
        self.hidden = False
    def hide(self):
        self.hidden = True
        for i in self.fight_buttons:
            # i.remove(all_sprites)
            all_sprites.remove(i)
        
