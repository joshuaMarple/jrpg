import pygame, random, sys
from pygame.locals import *
from button import *
# from vertMenu import vertMenu
# from gridMenu import gridMenu
from globals import *

class info(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height, text, orient="center"):
        self.width = width
        self.height = height
        self.color = BLACK
        self.basicFont = pygame.font.Font("./res/manteka.ttf", 20)
        
        pygame.sprite.Sprite.__init__(self)
        self.text_list = []
        text = text.split("\n")
        for i in text:
            # print(i)
            cur_text = self.basicFont.render(i.strip(), True, (0,0,0))
            cur_textRect = cur_text.get_rect()
            self.text_list.append((i.strip(), cur_text, cur_textRect))
        # print self.text_list
        self.image = pygame.Surface([width, height])
        self.inset_img = pygame.Surface([width-10, height-10])
        self.inset_img.fill(GRAY)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.inset_rect = self.inset_img.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.cur_color = RED
        self.orient = orient

    def update(self, surface):
        self.inset_rect.centerx = self.rect.centerx
        self.inset_rect.centery = self.rect.centery
        surface.blit(self.image, self.rect)
        surface.blit(self.inset_img, self.inset_rect)
        
        adjust = 0
        for i in self.text_list:
            adjust += self.basicFont.size(i[0])[1]
            if self.orient == "center":
                i[2].centerx = self.rect.centerx
                i[2].centery = self.rect.centery + adjust
            elif self.orient == "right":
                i[2].x = self.inset_rect.x
                i[2].y = self.inset_rect.y + adjust
            surface.blit(i[1], i[2])
        mouse_pos = pygame.mouse.get_pos()
        self.image.fill(self.color)
        
