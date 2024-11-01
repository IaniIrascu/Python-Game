import pygame as pg
import sys
sys.path.append('./assets')
from game import Game
from assets.colors import *

game = Game()  # creating the game object
game.run()  # run the game