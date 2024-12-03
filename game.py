import pygame as pg
import sys
import random as rd
from main_menu.main_menu import MainMenu
from map.map import Map
from sprites.sprites import Sprite, Group
from sprites.characters import Player
from pokemon.pokemon import *
from pokemon.attacks.attack import *
from pokemon.effects.effect import *
from pokemon.pokemons_information import *

from pokemon.ability_screen.ability_screen import AbilityScreen
from battle_screen.battle_screen import Battle_screen
from utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH

def search_effect(effects, effect_name):
    for effect in effects:
        if effect.get_name() == effect_name:
            return effect

def search_pokemon(pokemons, pokemon_name):
    for pokemon in pokemons:
        if pokemon.get_name() == pokemon_name:
            return pokemon

def search_attack(attacks, attack_name):
    for attack in attacks:
        if attack.get_name() == attack_name:
            return attack

class Game:
    def __init__(self):
        self.display_surface = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.scenes = {}
        self.current_scene = None
        self.all_sprites = Group()
        self.collisions = Group()
        self.transitions = Group()
        self.player = None
        self.rand = rd.randint(100, 500)
        self.map_name = "world"

    # returns the object related to the name
    def get_scene(self, scene_name):
        return self.scenes[scene_name]

    def add_scene(self, scene_name, scene):
        if scene_name not in self.scenes:
            self.scenes[scene_name] = scene

    def delete_scene(self, scene_name):
        if scene_name in self.scenes:
            self.scenes.pop(scene_name)

    def fade(self):
        fade = pg.Surface(self.display_surface.get_size())
        fade.fill('black')
        
        for alpha in range(0, 200, 2):
            fade.set_alpha(alpha)
            self.display_surface.blit(fade, (0, 0))
            pg.display.update()

    def run(self):
        pg.init()
        clock = pg.time.Clock()

        # pg.mixer.init()
        # pg.mixer.music.load("./utils/sounds/metin.mp3")
        # pg.mixer.music.play(-1)

        menu = MainMenu(self.display_surface)
        battle_screen = Battle_screen(self.display_surface)
        map = Map()
        map.render(self.all_sprites, self.collisions, self.transitions , map.first_pos[self.map_name], self.map_name)
        self.player = map.player
        self.add_scene("Menu", menu)
        self.add_scene("Map", map)
        self.add_scene("Battle_screen", battle_screen)

        game_scenes_active = {"main_menu": True, "map": False, "choose_save": False, "battle_screen": False}

        # Creare lista pokemoni
        pokemons = []
        # Creating some ability screens
        ability_screen = AbilityScreen()
        ability_screen.create_ability_screen()

        # CREATING ALL EFFECTS
        effects = []
        for i, effect_name in enumerate(effects_information):
            effects.append(Effect())
            effects[i].set_name(effect_name)
            effects[i].change_effectIcon(color = effects_information[effect_name]["color"])
            effects[i].set_color(effects_information[effect_name]["color"])

        # Loading all the attacks
        attacks_frames = AttacksFrames()
        attacks_frames.load_all_attacks_frames("./pokemon/attacks/assets")

        # CREATING ALL THE ATTACKS
        attacks = []
        special_attacks = []

        for pokemon in attacks_information:
            attack = Attack()
            special_attack = SpecialAttack()
            attack.set_name(attacks_information[pokemon]["attack"])
            attack.set_attack_frames(attacks_frames.get_attack_frames(attacks_information[pokemon]["frames"]))
            attacks.append(attack)

            special_attack.set_name(attacks_information[pokemon]["special_attack"]["name"])
            special_attack.set_attack_frames(attacks_frames.get_attack_frames(attacks_information[pokemon]["frames"]))
            special_attack.set_energy_cost(attacks_information[pokemon]["energy"])

            attack_effects = []
            for effect_name in attacks_information[pokemon]["special_attack"]["effects"]:
                attack_effects.append(search_effect(effects, effect_name))
            special_attack.set_effects(attack_effects)
            special_attacks.append(special_attack)

        # Loading all pokemons
        pokemons_frames = PokemonsFrames()
        pokemons_frames.load_all_pokemon_frames("./pokemon/assets")

        for i, pokemon_name in enumerate(pokemons_info):
            pokemons.append(Pokemon())
            pokemons[i].set_pokemon_frames(pokemons_frames.get_pokemon_frames(pokemon_name))
            pokemons[i].set_name(pokemon_name)
            pokemons[i].set_health(pokemons_info[pokemon_name]["health"])
            pokemons[i].set_maxHealth(pokemons_info[pokemon_name]["health"])
            pokemons[i].set_energy(pokemons_info[pokemon_name]["energy"])
            pokemons[i].set_maxEnergy(pokemons_info[pokemon_name]["energy"])
            pokemons[i].set_damage(pokemons_info[pokemon_name]["attack"])
            pokemons[i].set_level(1)
            pokemons[i].set_attack(attacks[i])
            pokemons[i].set_special_attack(special_attacks[i])
            pokemons[i].set_experience(0)

        inventory = []
        enemies = []

        while True:
            if game_scenes_active["main_menu"]:
                result = self.get_scene("Menu").run(clock)
                if result == "Start":
                    game_scenes_active["main_menu"] = False
                    game_scenes_active["map"] = True
                elif result == "Load":
                    game_scenes_active["main_menu"] = False
                    game_scenes_active["map"] = True
                elif result == "Quit":
                    pg.quit()
                    sys.exit()

            if game_scenes_active["battle_screen"]:
                # Se aleg 3 inamici random din lista
                battle_screen.load_enemies(enemies)
                battle_screen.load_player_pokemons(inventory)
                result = self.get_scene("Battle_screen").run(clock)
                if result == "MainMenu":
                    game_scenes_active["main_menu"] = True
                    game_scenes_active["battle_screen"] = False

            if game_scenes_active["map"]:
                dt = clock.tick(120) / 1000
                if map.change == "MainMenu":
                    game_scenes_active["main_menu"] = True
                    game_scenes_active["map"] = False
                if any(sprite for sprite in self.transitions if sprite.rect.colliderect(self.player.hitbox)):
                    self.fade()
                    self.map_name = next(sprite for sprite in self.transitions if sprite.rect.colliderect(self.player.hitbox)).target
                    self.map_pos = next(sprite for sprite in self.transitions if sprite.rect.colliderect(self.player.hitbox)).target_pos
                    map.render(self.all_sprites, self.collisions, self.transitions, self.map_pos, self.map_name)
                    self.player = map.player
                count = map.grass_count()
                if count == self.rand:
                    self.fade()

                    game_scenes_active["battle_screen"] = True
                    game_scenes_active["map"] = False
                    count = 0
                    self.rand = rd.randint(100, 500)
                self.display_surface.fill('black')
                self.all_sprites.draw(self.player.rect.center)
                self.all_sprites.update(dt)
                    
            pg.display.update()
            clock.tick(120)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
