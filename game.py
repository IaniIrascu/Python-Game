import pygame as pg
import sys
import random
from main_menu.main_menu import MainMenu
from map.map import Map
from sprites.sprites import Sprite
from sprites.player import Player
from pokemoni.pokemon import Pokemon
from pokemoni.ability_screen.ability_screen import Ability_screen
from battle_screen.battle_screen import Battle_screen
from pokemons_information import *

WINDOW_HEIGHT = 1920
WINDOW_WIDTH = 1080

class Game:
    def __init__(self):
        self.display_surface = pg.display.set_mode((0, 0), pg.FULLSCREEN)
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

        self.add_scene("Menu", menu)
        self.add_scene("Map", map)
        self.add_scene("Battle_screen", battle_screen)

        game_scenes_active = {"main_menu": True, "map": False, "choose_save": False, "battle_screen": False}

        # Creare lista pokemoni
        pokemons = []

        # Creating the pokemons
        for i, pokemon_name in enumerate(pokemons_info):
            pokemons.append(Pokemon())
            pokemons[i].set_name(pokemon_name)
            pokemons[i].set_health(pokemons_info[pokemon_name]["health"])
            pokemons[i].set_energy(pokemons_info[pokemon_name]["energy"])
            pokemons[i].set_size(pokemons_info[pokemon_name]["size"])
            pokemons[i].animation_frames("./pokemoni/assets/" + pokemon_name)

            # Creare ability_screen
            ability_screen = Ability_screen()
            ability_screen.create_ability_screen()
            pokemons[i].set_ability_screen(ability_screen)

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
                battle_enemies = [pokemons[random.randint(0, len(pokemons) - 1)],
                                  pokemons[random.randint(0, len(pokemons) - 1)],
                                  pokemons[random.randint(0, len(pokemons) - 1)]]
                player_pokemons = [pokemons[random.randint(0, len(pokemons) - 1)],
                                  pokemons[random.randint(0, len(pokemons) - 1)],
                                  pokemons[random.randint(0, len(pokemons) - 1)]]
                battle_screen.load_enemies(battle_enemies)
                battle_screen.load_player_pokemons(player_pokemons)
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
