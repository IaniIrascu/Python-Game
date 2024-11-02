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

        pg.init()
        clock = pg.time.Clock()

        menu = MainMenu()
        map = Map()
        map.render
        self.add_scene("Menu", menu)
        self.add_scene("Map", map)
        game_scenes_active = {"main_menu": True, "map": False, "choose_save": False}
        while True:
            # uncomment when buttons work

            # if game_scenes_active["main_menu"]:
            #     result = self.get_scene("Menu").run()
            #     if result == "Start":
            #         game_scenes_active["main_menu"] = False
            #         game_scenes_active["map"] = True
            #     elif result == "Load":
            #         game_scenes_active["main_menu"] = False
            #         game_scenes_active["choose_save"] = True
            #     elif result == "Quit":
            #         pg.quit()
            #         sys.exit()
            # if game_scenes_active["map"]:
            self.get_scene("Map").render(self.all_sprites)

            for sprite in self.all_sprites:
                if not isinstance(sprite.image, pg.Surface):
                    print(f"Invalid image for sprite: {sprite}")
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
