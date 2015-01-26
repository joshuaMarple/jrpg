import pygame, random, sys
from globals import *
from fightMenu import fightMenu
from pygame.locals import *

class player(pygame.sprite.Sprite):
    def __init__(self, name, image, health, actions, xpos, ypos, width, height):
        self.name = name
        self.health = health
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        # self.image.fill(RED)
        self.rect.x = xpos
        self.rect.y = ypos
        self.actions = actions
        self.fight_menu = fightMenu(self, self.actions)
        self.fight_menu.hide()
        pygame.sprite.Sprite.__init__(self)
        
    def damage(self, pain):
        self.health -= pain
        if self.health < 0:
            self.fight_menu.hide()
            # del self.fight_menu
            self.kill()

    def attack(self):
        return 10 # for now
        
    def update(self, surface):
        surface.blit(self.image, self.rect)
        
    def click(self):
        # global selected_player
        # selected_player = self
        # print(selected_player)
        self.fight_menu.show()

    def unselect(self):
        self.fight_menu.hide()
