import pygame as pg
import sys
from main_menu.main_menu import MainMenu
from map.map import Map
from sprites.sprites import Sprite, Group
from sprites.player import Player
from utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH

class Game:
    def __init__(self):
        self.display_surface = pg.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
        self.scenes = {}
        self.current_scene = None
        self.all_sprites = Group()

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

        pg.mixer.init()
        pg.mixer.music.load("./utils/sounds/metin.mp3")
        pg.mixer.music.play(-1)

        menu = MainMenu(self.display_surface, clock)
        map = Map()
        map.render(self.all_sprites, 'house')
        self.add_scene("Menu", menu)
        self.add_scene("Map", map)
        game_scenes_active = {"main_menu": False, "map": True, "choose_save": False}
        while True:
            if game_scenes_active["main_menu"]:
                result = self.get_scene("Menu").run()
                if result == "Start":
                    game_scenes_active["main_menu"] = False
                    game_scenes_active["map"] = True
                elif result == "Load":
                    game_scenes_active["main_menu"] = False
                    game_scenes_active["choose_save"] = True
                elif result == "Quit":
                    pg.quit()
                    sys.exit()
            if game_scenes_active["map"]:
                dt = clock.tick(60) / 1000
                self.get_scene("Map").update
                self.all_sprites.update(dt)
                self.display_surface.fill('grey')
                self.all_sprites.draw(map.player.rect.center)
            
            pg.display.update()
            clock.tick(60)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
