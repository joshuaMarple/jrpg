import pygame, random, sys
from pygame.locals import *
from button import button
from info import info
from vertMenu import vertMenu
from gridMenu import gridMenu
from attacks import *
from globals import *

class fightMenu():
    def __init__(self, player, action_text):
        self.fight_buttons = pygame.sprite.Group()
        # text = ["test" + str(i) for i in range(4)]
        # text = ["Fight", "Magic", "Items", "Run"]
        
        actions = []

        # due to scoping issues within python
        def action_from_text(act):
            def tmp():
                eval(act)(player)
            return tmp
            
        
        for i in action_text:
            # print(i)
            actions.append(action_from_text(i.replace(" ", "_")))
            
        # actions = [lambda: eval(i)(player) for i in action_text]
        # for i in action_text:
            # print eval(i)
        # eval("magic")
        # print actions
        # for act in actions:
            # act()
        gridMenu(0, WINDOWHEIGHT*2/3, WINDOWWIDTH*3/4, WINDOWHEIGHT/3, 2, 2, action_text, actions, self.fight_buttons)
        new_info = info(WINDOWWIDTH * 3/4, WINDOWHEIGHT *2/3, WINDOWWIDTH * 1/4, WINDOWHEIGHT/3, "Player 1 | 10 \n Player 2 | 12 \n Player 3 | 21", "right")
        self.fight_buttons.add(new_info)
        all_sprites.add(new_info)
        self.hidden = False
        # for i in self.fight_buttons:
        print(self.fight_buttons)

    def show(self):
        for i in self.fight_buttons:
            if all_sprites not in i.groups():
                all_sprites.add(i)
            if isinstance(i, button):
                buttons.add(i)
        self.hidden = False
    def hide(self):
        self.hidden = True
        for i in self.fight_buttons:
            # i.remove(all_sprites)
            all_sprites.remove(i)
            buttons.remove(i)
        
