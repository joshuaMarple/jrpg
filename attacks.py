import pygame
from pygame.locals import *
from popup import *
from globals import *

def punch(player):
    # print("punch!")
    cur_pop = popup("Select an enemy")
    cur_enemy = enemy_select()
    if cur_enemy == None:
        return
    cur_pop.destroy()
        
    # for i in selected_player:
    cur_enemy.damage(player.attack())
    print(cur_enemy.health)
    
def kick(player):
    print("kicking!")

def suicide(player):
    print("look here!")
    player.damage(2)
    
def magic(player):
    print("magic!")

def hit(player):
    print("Hit!")

def super_kick(player):
    print("super kick")

def tickle(player):
    print("goochy goo")

def magic_lick(player):
    print("finger licking good!")
