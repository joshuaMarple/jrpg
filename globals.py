import pygame, sys
from pygame.locals import *
# import popup

pygame.init()
RED = (255, 0, 0)
GRAY = (78, 99, 91)
PURPLE = (55, 43, 148)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
WINDOWWIDTH = pygame.display.Info().current_w
WINDOWHEIGHT = pygame.display.Info().current_h
BACKGROUNDCOLOR = WHITE
BACKGROUND = None

buttons = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
popups = []
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()

GAMESCREEN = None
# selected_player = pygame.sprite.Group()

FPS = 60
TEXTCOLOR = BLACK

def terminate():
    pygame.quit()
    sys.exit()

def enemy_select():
    while True:
        GAMESCREEN.fill(BACKGROUNDCOLOR)
        GAMESCREEN.blit(BACKGROUND, (0,0))
        for i in popups:
            i.update()
        all_sprites.update(GAMESCREEN)
        players.update(GAMESCREEN)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in enemies:
                    if i.rect.collidepoint(mouse_pos):
                        print("enemy selected")
                        return i
                return None
            if event.type == pygame.MOUSEBUTTONUP:
                for i in buttons:
                    i.unclick()    
    
