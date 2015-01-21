import pygame, random, sys
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (78, 99, 91)
PURPLE = (55, 43, 148)
BLACK = (0,0,0)

class button(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height, text, click_function, kill_on_click):
        self.clicked = False
        self.width = width
        self.height = height
        self.color = BLACK
        basicFont = pygame.font.Font("./res/manteka.ttf", 20)
        # super(self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.text = basicFont.render(text, True, (0,0,0))
        self.textRect = self.text.get_rect()
        
        self.image = pygame.Surface([width, height])
        self.inset_img = pygame.Surface([width-10, height-10])
        self.inset_img.fill(GRAY)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.inset_rect = self.inset_img.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.cur_color = RED
        self.action = click_function
        self.kill_on_click = kill_on_click
        
    def click(self, window_surface):
        print("test click")
        
    def update(self, surface):
        self.textRect.centerx = self.rect.centerx
        self.textRect.centery = self.rect.centery
        self.inset_rect.centerx = self.rect.centerx
        self.inset_rect.centery = self.rect.centery
        surface.blit(self.image, self.rect)
        surface.blit(self.inset_img, self.inset_rect)
        surface.blit(self.text, self.textRect)
        mouse_pos = pygame.mouse.get_pos()
        # if self.rect.collidepoint(mouse_pos):
            # self.image.fill((255,0,0))
        # else:
        self.image.fill(self.color)
        
    def draw(self, surface):
        print("test")
        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.textRect)
        
        
        # print("test update")
        
    def draw_text(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        
    def click(self):
        # if self.color == GRAY:
        self.color = PURPLE
        self.action()
        # else:
            # self.color = GRAY
    def unclick(self):
        self.color = BLACK
        if self.kill_on_click:
            self.kill()
            # pygame.sprite.Sprite.kill(self)
            
