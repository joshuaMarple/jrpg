import pygame, random, sys
from pygame.locals import *
from fightMenu import fightMenu
from player import player
from globals import *

class fight():
    def __init__(self):
        
        # fight_menu = fightMenu()
        player1 = player("Ugak gra mo gak", "./res/player.png", 20, WINDOWWIDTH * 3/4, WINDOWHEIGHT * 1/4, 50, 50)
        all_sprites.add(player1)
        players.add(player1)
    # player2 = player("Archibald")
    # player3 = player("Ornstein")
    

    
