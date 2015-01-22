import pygame, sys
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
enemies = pygame.sprite.Group()

selected_player = None

FPS = 60
TEXTCOLOR = BLACK

def terminate():
    pygame.quit()
    sys.exit()

def enemy_select():
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in enemies:
                    if i.rect.collidepoint(mouse_pos):
                        return i
                
    
