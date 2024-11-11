import pygame as pg
import sys
import random
from main_menu.main_menu import MainMenu
from map.map import Map
from sprites.sprites import Sprite
from sprites.player import Player
from pokemoni.pokemon import *
from pokemoni.attacks.attack import *
from pokemoni.ability_screen.ability_screen import *
from pokemons_information import *

from pokemoni.ability_screen.ability_screen import AbilityScreen
from battle_screen.battle_screen import Battle_screen

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

        # Creating some ability screens
        ability_screen = AbilityScreen()
        ability_screen.create_ability_screen()

        # Loading all the attacks
        attacks_frames = AttacksFrames()
        attacks_frames.load_all_attacks_frames("./pokemoni/attacks/assets")

        # Creating some attacks
        attack1 = Attack()
        attack2 = Attack()

        attack1.set_attack_frames(attacks_frames.get_attack_frames("scratch.png"))
        attack2.set_attack_frames(attacks_frames.get_attack_frames("fire.png"))

        # Loading all pokemons
        pokemons_frames = PokemonsFrames()
        pokemons_frames.load_all_pokemon_frames("./pokemoni/assets")

        # Creating some pokemons
        pokemon1 = Pokemon()
        pokemon2 = Pokemon()
        pokemon3 = Pokemon()
        pokemon4 = Pokemon()
        pokemon5 = Pokemon()
        pokemon6 = Pokemon()

        pokemon1.set_pokemon_frames(pokemons_frames.get_pokemon_frames("Charmadillo.png"))
        pokemon1.set_health(100)
        pokemon1.set_damage(500)
        pokemon1.set_level(1)
        pokemon1.set_ability_screen(ability_screen)
        pokemon1.set_attack(attack1)

        pokemon2.set_pokemon_frames(pokemons_frames.get_pokemon_frames("Gulfin.png"))
        pokemon2.set_health(120)
        pokemon2.set_damage(40)
        pokemon2.set_level(1)
        pokemon2.set_ability_screen(ability_screen)
        pokemon2.set_attack(attack2)

        pokemon3.set_pokemon_frames(pokemons_frames.get_pokemon_frames("Pouch.png"))
        pokemon3.set_health(160)
        pokemon3.set_damage(80)
        pokemon3.set_level(1)
        pokemon3.set_ability_screen(ability_screen)
        pokemon3.set_attack(attack2)

        pokemon4.set_pokemon_frames(pokemons_frames.get_pokemon_frames("Friolera.png"))
        pokemon4.set_health(200)
        pokemon4.set_damage(40)
        pokemon4.set_level(1)
        pokemon4.set_ability_screen(ability_screen)
        pokemon4.set_attack(attack2)

        pokemon5.set_pokemon_frames(pokemons_frames.get_pokemon_frames("Jacana.png"))
        pokemon5.set_health(180)
        pokemon5.set_damage(60)
        pokemon5.set_level(1)
        pokemon5.set_ability_screen(ability_screen)
        pokemon5.set_attack(attack2)

        pokemon6.set_pokemon_frames(pokemons_frames.get_pokemon_frames("Larvea.png"))
        pokemon6.set_health(150)
        pokemon6.set_damage(40)
        pokemon6.set_level(1)
        pokemon6.set_ability_screen(ability_screen)
        pokemon6.set_attack(attack1)

        inventory = [pokemon1, pokemon2, pokemon3]
        enemies = [pokemon4, pokemon5, pokemon6]

        # Creating the pokemons
        # for i, pokemon_name in enumerate(pokemons_info):
        #     pokemons.append(Pokemon())
        #     pokemons[i].set_name(pokemon_name)
        #     pokemons[i].set_health(pokemons_info[pokemon_name]["health"])
        #     pokemons[i].set_energy(pokemons_info[pokemon_name]["energy"])
        #     pokemons[i].set_size(pokemons_info[pokemon_name]["size"])
        #     pokemons[i].set_attack(pokemons_info[pokemon_name]["attack"])
        #     pokemons[i].animation_frames("./pokemoni/assets/" + pokemon_name)
        #     pokemons[i].attack_frames_animation("./pokemoni/attacks/assets/" + pokemons_info[pokemon_name]["attacksprites"])
        #
        #     # Creare ability_screen
        #     ability_screen = Ability_screen()
        #     ability_screen.create_ability_screen()
        #     pokemons[i].set_ability_screen(ability_screen)

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
                battle_screen.load_enemies(enemies)
                battle_screen.load_player_pokemons(inventory)

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
