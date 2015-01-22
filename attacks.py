import pygame
from pygame.locals import *
from globals import *

def punch():
    cur_enemy = enemy_select()
    for i in selected_player:
        cur_enemy.damage(i.attack())
    
def kick():
    print("kicking!")

def magic():
    print("magic!")

def damage():
    selected_player.damage(2)
