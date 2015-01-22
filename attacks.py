import pygame
from pygame.locals import *
from globals import *

def punch():
    cur_enemy = enemy_select()
    cur_enemy.damage(selected_player.attack())
    
def kick():
    print("kicking!")

def magic():
    print("magic!")

def damage():
    selected_player.damage(2)
