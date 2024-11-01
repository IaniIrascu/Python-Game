import pygame as pg
import sys
from main_menu.main_menu import MainMenu
from map.map import Map
from sprites.sprites import Sprite
from sprites.player import Player

WINDOW_HEIGHT = 1920
WINDOW_WIDTH = 1080

class Game:
    def __init__(self):
        self.display_surface = pg.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
        self.scenes = {}
        self.current_scene = None
        self.all_sprites = pg.sprite.Group()

    # current scene
    def set_current_scene(self, scene_name):
        self.current_scene = self.scenes[scene_name]

    def get_current_scene_name(self):
        return list(self.scenes.keys())[list(self.scenes.values()).index(self.current_scene)]  # returneaza cheia cu valoarea 

    # returns the object related to the name
    def get_scene(self, scene_name):
        return self.scenes[scene_name]

    def add_scene(self, scene_name, scene):
        if scene_name not in self.scenes:
            self.scenes[scene_name] = scene

    def delete_scene(self, scene_name):
        if scene_name in self.scenes:
            self.scenes.pop(scene_name)

    def run(self):
        pg.init()  # initialize pg
        clock = pg.time.Clock()  # get a pg clock object
        menu = MainMenu()  # creating the menu scene
        map = Map()
        self.add_scene("Menu", menu)
        self.add_scene("Map", map)
        game_scenes_active = {"main_menu": True, "map": False}
        while True:
            if game_scenes_active["main_menu"]:
                result = self.get_scene("Menu").run()
                if result == "Start":
                    game_scenes_active["main_menu"] = False
                    game_scenes_active["map"] = True
                elif result == "Load":
                    game_scenes_active["main_menu"] = False

            if game_scenes_active["map"]:
                result = self.get_scene("Map").run()
                self.all_sprites.draw(self.display_surface)
            

            pg.display.update()
            clock.tick(60)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    pg.quit()
                    sys.exit()
