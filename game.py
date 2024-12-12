import pygame as pg
import sys
import os
import random as rd
from main_menu.main_menu import MainMenu
from map.map import Map
from sprites.sprites import Group
from pokemon.pokemon import *
from pokemon.attacks.attack import *
from pokemon.effects.effect import *
from pokemon.pokemons_information import *
from save_handling.save_handling import *
from pokemon.ability_screen.ability_screen import AbilityScreen
from battle_screen.battle_screen import Battle_screen
from inventory.inventory import *
from sprites.characters import Dialog
from exit_menu.exit_menu import *
from utils.constants import *


def search(list, element_name):
    for element in list:
        if element.get_name() == element_name:
            return element

def generate_pokemon(pokemon_name, pokemons_frames, attacks, special_attacks, level):
    pokemon = Pokemon()
    pokemon.set_name(pokemon_name)
    pokemon.set_pokemon_frames(pokemons_frames.get_pokemon_frames(pokemon_name))

    maxHealth = pokemons_info[pokemon_name]["health"]
    pokemon.set_maxHealth(maxHealth * pow(HPUPPROCENT, level - 1))
    pokemon.set_health(pokemon.get_maxHealth())

    maxEnergy = pokemons_info[pokemon_name]["energy"]
    pokemon.set_maxEnergy(maxEnergy + MANABONUS * (level - 1))
    pokemon.set_energy(pokemon.get_maxEnergy())

    damage = pokemons_info[pokemon_name]["damage"]
    pokemon.set_damage(damage * pow(DAMAGEUPPROCENT, level - 1))

    pokemon.set_level(level)
    attack_name = attacks_information[pokemon_name]["attack"]
    pokemon.set_attack(search(attacks, attack_name))
    special_attack_name = attacks_information[pokemon_name]["special_attack"]["name"]
    pokemon.set_special_attack(search(special_attacks, special_attack_name))
    pokemon.set_experience(0)
    return pokemon

def populate_enemies(enemies_list_names, pokemons_frames, attacks, special_attacks):
    enemies_in_battle = []
    length = len(enemies_list_names)
    noOfPokemons = random.randint(1, 3)
    for i in range(noOfPokemons):
        pokemonpos = random.randint(0, length - 1)
        enemies_in_battle.append(generate_pokemon(enemies_list_names[pokemonpos], pokemons_frames, attacks, special_attacks, 1))
    return enemies_in_battle

class Game:
    def __init__(self):
        self.display_surface = pg.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
        self.scenes = {}
        self.current_scene = None
        self.all_sprites = Group()
        self.collisions = Group()
        self.transitions = Group()
        self.npcs = Group()
        self.player = None
        self.rand = rd.randint(50, 300)
        self.map_name = "world"
        self.dialog = None
        self.enemies = []

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
        metin = os.path.join("utils", "sounds", "metin.mp3")
        mario = os.path.join("utils", "sounds", "mario.mp3")
        pg.init()
        clock = pg.time.Clock()

        # pg.mixer.init()
        # pg.mixer.music.load(metin)
        # pg.mixer.music.play(-1)

        menu = MainMenu(self.display_surface)
        battle_screen = Battle_screen(self.display_surface)
        map = Map()
        map.render(self.all_sprites, self.collisions, self.transitions, self.npcs, map.first_pos[self.map_name], self.map_name)
        exit = Exit(self.display_surface)
        self.player = map.player
        self.player.set_inventory(Inventory(self.display_surface))
        self.player.get_inventory().set_noOfPokemons(0)
        self.add_scene("Menu", menu)
        self.add_scene("Map", map)
        self.add_scene("Battle_screen", battle_screen)
        self.add_scene("Exit", exit)

        game_scenes_active = {"main_menu": True, "map": False, "choose_save": False, "battle_screen": False, "exit": False}

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
            effects[i].change_effectIcon(color=effects_information[effect_name]["color"])
            effects[i].set_color(effects_information[effect_name]["color"])

        # Loading all the attacks
        attacks_frames = AttacksFrames()
        attacks_frames.load_all_attacks_frames(os.path.join("pokemon", "attacks", "assets"))

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
                attack_effects.append(search(effects, effect_name))
            special_attack.set_effects(attack_effects)
            special_attacks.append(special_attack)

        # Loading all pokemons
        pokemons_frames = PokemonsFrames()
        pokemons_frames.load_all_pokemon_frames(os.path.join("pokemon", "assets"))

        generated_enemy = generate_pokemon("Atrox.png", pokemons_frames, attacks, special_attacks, 1)
        self.enemies = [generated_enemy]

        player_rect_center = self.player.rect.center
        mainMenuMusic = pg.mixer.Sound(metin).play(-1)
        battleMusic = pg.mixer.Sound(mario).play(-1)
        mainMenuMusic.pause()
        battleMusic.pause()
        str_screen = None
        current_npc = None
        biome = None

        beach_pokemons = ["Atrox.png", "Gulfin.png", "Finsta.png", "Pouch.png", "Jacana.png", "Finiette.png"]
        desert_pokemons = ["Charmadillo.png", "Cindrill.png", "Draem.png", "Sparchu.png"]
        ice_pokemons = ["Friolera", "Pluma.png", "Cleaf.png", "Draem.png"]
        forest_pokemons = ["Plumette.png", "Pluma.png", "Larvea.png", "Ivieron.png", "Cleaf.png", "Atrox.png", "Pouch.png"]

        pokemons_by_category = {"beach": beach_pokemons, "desert": desert_pokemons, "ice": ice_pokemons, "forest": forest_pokemons}

        while True:
            if game_scenes_active["main_menu"]:
                str_screen = "main_menu"
                mainMenuMusic.unpause()
                battleMusic.pause()
                result = self.get_scene("Menu").run(clock)
                if result == "Start":
                    self.player.get_inventory().get_pokemons().clear()
                    self.player.rect.center = player_rect_center
                    generated_pokemon = generate_pokemon("Sparchu.png", pokemons_frames, attacks, special_attacks, 1)
                    self.player.get_inventory().add_pokemon_to_inventory(generated_pokemon)
                    generated_pokemon = generate_pokemon("Charmadillo.png", pokemons_frames, attacks, special_attacks, 1)
                    # First time loading the game
                    self.player.get_inventory().add_pokemon_to_inventory(generated_pokemon)
                    generated_pokemon = generate_pokemon("Draem.png", pokemons_frames, attacks, special_attacks, 1)

                    # First time loading the game
                    self.player.get_inventory().add_pokemon_to_inventory(generated_pokemon)
                    self.player.get_inventory().set_noOfPokemons(3)
                    s = SaveLoadSystem("save", "./save_files")
                    # Se sterg fisierele de salvare vechi
                    if s.check_for_file("inventory"):
                        os.remove("./save_files/inventory.save")
                    if s.check_for_file("player_position"):
                        os.remove("./save_files/player_position.save")
                    game_scenes_active["main_menu"] = False
                    game_scenes_active["map"] = True
                    self.fade()
                elif result == "Load":
                    # Aici se da load la toti pokemonii din inventar
                    s = SaveLoadSystem("save", "./save_files")
                    if s.check_for_file("inventory"):
                        inventory = []
                        inventory_data = s.load_data("inventory")
                        self.player.get_inventory().set_noOfPokemons(0)
                        # Se genereaza inventarul cu pokemonii asa cum erau cand s-a iesit din joc
                        for i, data in enumerate(inventory_data):
                            inventory.append(
                                generate_pokemon(inventory_data[i]["name"], pokemons_frames, attacks, special_attacks,
                                                 inventory_data[i]["level"]))
                            inventory[i].set_experience(inventory_data[i]["experience"])
                            self.player.get_inventory().set_noOfPokemons(self.player.get_inventory().get_noOfPokemons() + 1)
                        os.remove("./save_files/inventory.save")
                        self.player.get_inventory().update_inventory(inventory)
                    else:
                        # Daca nu exista, se predefineste un pokemon de inceput
                        generated_pokemon = generate_pokemon("Charmadillo.png", pokemons_frames, attacks, special_attacks, 1)
                        self.player.get_inventory().add_pokemon_to_inventory(generated_pokemon)
                        self.player.get_inventory().set_noOfPokemons(1)
                    if s.check_for_file("player_position"):
                        self.player.rect.center = s.load_data("player_position")
                        os.remove("./save_files/player_position.save")
                    game_scenes_active["main_menu"] = False
                    game_scenes_active["map"] = True
                    self.fade()
                elif result == "Quit":
                    # DACA SE IESE DE PE HARTA SE SALVEAZA PROGRESUL
                    s = SaveLoadSystem("save", "save_files")
                    # datele despre inventar sunt salvate asa: nume level experienta ramasa pentru fiecare
                    # pokemoni intr-o lista de dictionare
                    saved_inventory_data = []
                    for pokemon in self.player.get_inventory().get_pokemons():
                        saved_data = {"name": pokemon.get_name(), "level": pokemon.get_level(),
                                      "experience": pokemon.get_experience()}
                        saved_inventory_data.append(saved_data)

                    s.save_data(saved_inventory_data, "inventory")
                    s.save_data(self.player.rect.center, "player_position")
                    self.fade()
                    pg.quit()
                    sys.exit()

            if game_scenes_active["battle_screen"]:
                if str_screen != "exit":
                    battleMusic.play(pg.mixer.Sound(mario), -1)
                mainMenuMusic.pause()
                if str_screen != "exit":
                    enemies_in_battle = []
                    self.player.get_inventory().activate_first_max_3_pokemons()
                    # Se aleg 3 inamici random din lista
                    if biome is None:
                        # NPC battle
                        enemies_in_battle = self.enemies
                    else:
                        enemies_in_battle = populate_enemies(pokemons_by_category[biome], pokemons_frames, attacks, special_attacks)

                    pokemons_in_battle = []
                    for i, pokemon in enumerate(self.player.get_inventory().get_pokemons()):
                        if self.player.get_inventory().get_active_pokemons()[i]:
                            # print("P" + str(i) + " " + str(pokemon.get_maxEnergy()))
                            pokemons_in_battle.append(pokemon)
                    battle_screen.load_enemies(enemies_in_battle)
                    battle_screen.load_player_pokemons(pokemons_in_battle)
                result = self.get_scene("Battle_screen").run(clock)
                if result == "Map":
                    battleMusic.stop()
                    mainMenuMusic.unpause()
                    game_scenes_active["map"] = True
                    game_scenes_active["battle_screen"] = False
                    self.fade()
                elif result == "Win":
                    if current_npc:
                        current_npc.data['defeated'] = True
                        current_npc = None
                    battleMusic.stop()
                    mainMenuMusic.unpause()
                    if biome is None:
                        chance = 200
                    else:
                        chance = 33
                    if self.player.get_inventory().get_noOfPokemons() <= 16:
                        if chance >= random.randint(0, 100):
                            enemy_index = random.randint(0, len(enemies_in_battle) - 1)
                            # Cautare daca pokemonul exista deja in lista de pokemoni
                            if search(self.player.get_inventory().get_pokemons(), enemies_in_battle[enemy_index].get_name()) is None:
                                # S-a gasit un pokemon care nu exista in lista si se adauga la inventar
                                pokemon_to_add = generate_pokemon(enemies_in_battle[enemy_index].get_name(),
                                                            pokemons_frames,
                                                            attacks,
                                                            special_attacks,
                                                            enemies_in_battle[enemy_index].get_level())
                                self.player.get_inventory().add_pokemon_to_inventory(pokemon_to_add)
                                self.player.get_inventory().set_noOfPokemons(self.player.get_inventory().get_noOfPokemons() + 1)
                    game_scenes_active["map"] = True
                    game_scenes_active["battle_screen"] = False
                    self.fade()
                elif result == "Exit":
                    game_scenes_active["exit"] = True
                    game_scenes_active["battle_screen"] = False
                str_screen = "battle_screen"
                biome = None
            if game_scenes_active["map"]:
                dt = clock.tick(60) / 1000
                if any(sprite for sprite in self.transitions if sprite.rect.colliderect(self.player.hitbox)):
                    self.fade()
                    self.map_name = next(sprite for sprite in self.transitions if sprite.rect.colliderect(self.player.hitbox)).target
                    self.map_pos = next(sprite for sprite in self.transitions if sprite.rect.colliderect(self.player.hitbox)).target_pos
                    map.render(self.all_sprites, self.collisions, self.transitions, self.npcs, self.map_pos, self.map_name)
                    self.player = map.player
                count, biome = map.grass_count()
                if count == self.rand:
                    self.fade()
                    game_scenes_active["battle_screen"] = True
                    game_scenes_active["map"] = False
                    self.rand = rd.randint(50, 300)
                    continue
                self.display_surface.fill('black')
                self.all_sprites.draw(self.player.rect.center)
                self.all_sprites.update(dt)
                str_screen = "map"

            if game_scenes_active["exit"]:
                if str_screen == "battle_screen":
                    exit_res = self.get_scene("Exit").run2(clock)
                    if exit_res == "Continue":
                        game_scenes_active[str_screen] = True
                        game_scenes_active["exit"] = False
                        str_screen = "exit"
                    elif exit_res == "Map":
                        battleMusic.stop()
                        mainMenuMusic.play(pg.mixer.Sound(metin), -1)
                        game_scenes_active["map"] = True
                        game_scenes_active["exit"] = False
                elif str_screen == "map":
                    exit_res = self.get_scene("Exit").run1(clock)
                    if exit_res == "Continue":
                        game_scenes_active[str_screen] = True
                        game_scenes_active["exit"] = False
                        str_screen = "exit"
                    elif exit_res == "Save":
                        s = SaveLoadSystem("save", "save_files")
                        saved_inventory_data = []
                        for pokemon in self.player.get_inventory().get_pokemons():
                            saved_data = {"name": pokemon.get_name(), "level": pokemon.get_level(),
                                        "experience": pokemon.get_experience()}
                            saved_inventory_data.append(saved_data)

                        s.save_data(saved_inventory_data, "inventory")
                        s.save_data(self.player.rect.center, "player_position")
                    elif exit_res == "Menu":
                        mainMenuMusic.stop()
                        mainMenuMusic.play(pg.mixer.Sound(metin), -1)
                        game_scenes_active["main_menu"] = True
                        game_scenes_active["map"] = False
                        game_scenes_active["exit"] = False
                    elif exit_res == "Exit":
                        s = SaveLoadSystem("save", "save_files")
                        saved_inventory_data = []
                        for pokemon in self.player.get_inventory().get_pokemons():
                            saved_data = {"name": pokemon.get_name(), "level": pokemon.get_level(),
                                          "experience": pokemon.get_experience()}
                            saved_inventory_data.append(saved_data)
                        s.save_data(saved_inventory_data, "inventory")
                        s.save_data(self.player.rect.center, "player_position")
                        self.fade()
                        pg.quit()
                        sys.exit()
                self.fade()
            pg.display.update()
            clock.tick(60)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE and game_scenes_active["map"]:
                        game_scenes_active["exit"] = True
                        game_scenes_active["map"] = False
                    if event.key == pg.K_e and game_scenes_active["map"]:
                        self.player.get_inventory().run(clock)
                    if event.key == pg.K_f and game_scenes_active["map"]:
                        if not self.dialog:
                            for npc in self.npcs:
                                distance = pg.math.Vector2(npc.rect.center) - pg.math.Vector2(self.player.rect.center)
                                if distance.length() < 150:
                                    self.player.stop = True
                                    self.player.direction = pg.math.Vector2(0, 0)
                                    font = pg.font.Font(os.path.join("main_menu", "assets", "minecraft.ttf"), 30)
                                    self.dialog = Dialog(npc, self.player, self.all_sprites, font)
                        if self.dialog:
                            self.dialog.update()
                            if self.dialog.idx == len(self.dialog.npc.data['dialog']['default']) and not \
                            self.dialog.npc.data['defeated']:
                                self.enemies.clear()
                                for pokemon in self.dialog.npc.data['pokemon'].values():
                                    enemy = generate_pokemon(f'{pokemon[0]}.png', pokemons_frames, attacks,
                                                             special_attacks, pokemon[1])
                                    self.enemies.append(enemy)
                                self.fade()
                                game_scenes_active["map"] = False
                                game_scenes_active["battle_screen"] = True
                                current_npc = self.dialog.npc
                            if self.dialog.end:
                                self.dialog = None