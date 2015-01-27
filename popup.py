import pygame
from pygame.locals import *
# from button import button
from info import *
from globals import *
import time

class popup():
    def __init__(self, message, lifetime=5, xpos=WINDOWWIDTH-200, ypos=0, orient="center"):
         self.start = time.time()
         self.info = info(xpos, ypos, 200, 100, message, "right")
         self.time = lifetime
         self.message = message
         all_sprites.add(self.info)
         popups.append(self)
         # for i in popups:
             # i.update()

    def update(self):
        # print("updating popups")
        # print self.start
        # print(time.time() - self.start)
        if (time.time() - self.start) > self.time:
            self.info.kill()

    def destroy(self):
        self.info.kill()
