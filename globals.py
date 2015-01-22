import pygame
from pygame.locals import *

pygame.init()
RED = (255, 0, 0)
GRAY = (78, 99, 91)
PURPLE = (55, 43, 148)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
WINDOWWIDTH = pygame.display.Info().current_w
WINDOWHEIGHT = pygame.display.Info().current_h
BACKGROUNDCOLOR = WHITE

buttons = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()

FPS = 60
TEXTCOLOR = BLACK
    
