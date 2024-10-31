import pygame
import sys
sys.path.append('./assets')
from main_menu import MainMenu
from game import Game
from level import Level
from assets.colors import *

pygame.init()  # initialize pygame
clock = pygame.time.Clock()  # get a pygame clock object

game = Game()  # creating the game object
menu = MainMenu()  # creating the menu scene
level = Level()

game.add_scene("Menu", menu)  # adding menu to game)
game.add_scene("Level", level)
WIDTH = game.get_screen().get_width()
HEIGHT = game.get_screen().get_height()

game_scenes_active = {"main_menu": True, "level": False}
# Running the game
while True:
    if game_scenes_active["main_menu"]:
        result = game.get_scene("Menu").run()
        if result == "Start":
            game_scenes_active["main_menu"] = False
            game_scenes_active["level"] = True
        elif result == "Load":
            game_scenes_active["main_menu"] = False

    if game_scenes_active["level"]:
        result = game.get_scene("Level").run()

    pygame.display.update()
    clock.tick(60)