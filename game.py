import pygame as pg
import sys
import random
from main_menu.main_menu import MainMenu
from map.map import Map
from sprites.sprites import Sprite
from sprites.player import Player
from inamici.inamici import Inamic
from battle_screen.battle_screen import Battle_screen

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

        pg.mixer.init()
        pg.mixer.music.load("./utils/sounds/metin.mp3")
        pg.mixer.music.play(-1)

        menu = MainMenu(self.display_surface)
        battle_screen = Battle_screen(self.display_surface)
        map = Map()

        # Creare lista inamici
        enemies = []
        enemies_file_names = ["Atrox.png", "Charmadillo.png", "Cindrill.png", "Cleaf.png", "Draem.png", "Finiette.png",
                              "Finsta.png", "Friolera.png", "Gulfin.png", "Ivieron.png", "Jacana.png", "Larvea.png",
                              "Pluma.png", "Plumette.png", "Pouch.png", "Sparchu.png"]

        for i, enemy_name in enumerate(enemies_file_names):
            enemies.append(Inamic())
            enemies[i].animation_frames("./inamici/assets/" + enemy_name)

        self.add_scene("Menu", menu)
        self.add_scene("Map", map)
        self.add_scene("Battle_screen", battle_screen)

        game_scenes_active = {"main_menu": True, "map": False, "choose_save": False, "battle_screen": False}
        while True:
            if game_scenes_active["main_menu"]:
                result = self.get_scene("Menu").run(clock)
                if result == "Start":
                    game_scenes_active["main_menu"] = False
                    game_scenes_active["battle_screen"] = True
                elif result == "Load":
                    game_scenes_active["main_menu"] = False
                    game_scenes_active["choose_save"] = True
                elif result == "Quit":
                    pg.quit()
                    sys.exit()
            if game_scenes_active["battle_screen"]:
                # Se aleg 3 inamici random din lista
                battle_enemies = [enemies[random.randint(0, len(enemies) - 1)],
                                  enemies[random.randint(0, len(enemies) - 1)],
                                  enemies[random.randint(0, len(enemies) - 1)]]
                battle_screen.load_enemies(battle_enemies)
                # Se ruleaza battle screen
                result = self.get_scene("Battle_screen").run(clock)
                if result == "MainMenu":
                    game_scenes_active["main_menu"] = True
                    game_scenes_active["battle_screen"] = False
            if game_scenes_active["map"]:
                self.get_scene("Map").render(self.all_sprites)
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
