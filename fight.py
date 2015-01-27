import pygame, random, sys
from pygame.locals import *
from fightMenu import fightMenu
from attacks import *
from player import player
from enemy import enemy
from globals import *

class fight():
    def __init__(self):
        # global selected_player
        # fight_menu = fightMenu()
        player1_actions = ["punch", "kick", "suicide", "magic"]
        player2_actions = ["hit", "super kick", "tickle", "magic lick"]
        # player1_moves = [lambda : punch(player), lambda : kick(player), lambda : suicide(player), lambda : magic(player)]
        # player2_moves = [lambda : punch(player), lambda]
        # player1_action = [punch, lambda : (), lambda : (), lambda : ()]
        player1 = player("Ugak gra mo gak", "./res/player.png", 20, player1_actions, WINDOWWIDTH * 3/4, WINDOWHEIGHT * 1/4, 50, 50)
        player2 = player("Arthur Bryant", "./res/player.png", 20, player2_actions, WINDOWWIDTH * 3/4 + 70, WINDOWHEIGHT * 1/4 + 70, 50, 50)
        all_sprites.add(player1)
        players.add(player1)
        all_sprites.add(player2)
        players.add(player2)
        enemy1 = enemy("Archibald", "./res/player.png", 20, WINDOWWIDTH * 1/4, WINDOWHEIGHT * 1/4, 50, 50 )
        all_sprites.add(enemy1)
        enemies.add(enemy1)
        
    # player2 = player("Archibald")
    # player3 = player("Ornstein")
    

    
