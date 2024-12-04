import pygame as pg
from pokemon.pokemon import *
import math
from utils.colors import *
from pokemon.ability_screen.ability_screen import *
from battle_screen.funtions import *

class Inventory:
    def __init__(self, display_surface):
        self.pokemons = []
        self.display_surface = display_surface
        self.inventory_surface = pg.transform.scale_by(pg.image.load('./inventory/assets/inventory.jpg'), 2)
        self.size = self.inventory_surface.get_size()
        self.maxCapacity = 16
        self.noOfPokemons = 0
        self.activePokemons = [False, False, False, False,
                               False, False, False, False,
                               False, False, False, False,
                               False, False, False, False]

    def activate_first_max_3_pokemons(self):
        # Se verifica daca exista pokemoni activi in inventar
        count = 0
        for i in range(16):
            if self.activePokemons[i]:
                count += 1
        print(self.noOfPokemons)
        if count < 3:
            for i in range(self.noOfPokemons):
                if i >= 3:
                    break
                self.activePokemons[i] = True

    def add_pokemon_to_inventory(self, pokemon):
        self.pokemons.append(pokemon)

    def update_inventory(self, pokemons):
        self.pokemons = pokemons

    def get_pokemons(self):
        return self.pokemons

    def set_noOfPokemons(self, noOfPokemons):
        self.noOfPokemons = noOfPokemons

    def get_noOfPokemons(self):
        return self.noOfPokemons

    def get_active_pokemons(self):
        return self.activePokemons

    def run(self, clock):
        self.activate_first_max_3_pokemons()
        # Se verifica daca exista pokemoni activi in inventar
        activated_pokemons = 0
        reset_active_pokemons = False
        delete_pokemon = False
        # Se incarca backgroundurile pentru inventar
        background = pg.transform.scale_by(pg.image.load('./inventory/assets/inventory.jpg'), 2)
        background_delete = pg.transform.scale_by(pg.image.load('./inventory/assets/inventory_-_delete.png'), 2)
        background_select = pg.transform.scale_by(pg.image.load('./inventory/assets/inventory_-_select.png'), 2)
        select_image = pg.image.load('./inventory/assets/select.png')
        select_image = pg.transform.scale(select_image, (self.size[0] / 6, self.size[1] / 6))
        select_image_red = pg.image.load('./inventory/assets/select - red.png')
        select_image_red = pg.transform.scale(select_image_red, (self.size[0] / 6, self.size[1] / 6))
        font = pg.font.Font("./main_menu/assets/minecraft.ttf", 18)
        font_texts = []
        for i, pokemon in enumerate(self.pokemons):
            font_texts.append(font.render(pokemon.get_name().replace(".png", "") + " Lv. " + str(pokemon.get_level()), True, BLACK, None))
        health_texts = []
        energy_texts = []
        for i, pokemon in enumerate(self.pokemons):
            health_texts.append(font.render(str(round(pokemon.get_health(), 2)) + "/" + str(pokemon.get_maxHealth()), True, WHITE, None))
            energy_texts.append(font.render(str(round(pokemon.get_energy(), 2)) + "/" + str(pokemon.get_maxEnergy()), True, WHITE, None))

        show_ability_screen = False
        index_to_show = -1
        ability_screen = AbilityScreen()
        ability_screen.create_ability_screen()

        bars = pg.image.load('./battle_screen/assets/Bars.png')
        bars.convert_alpha()
        bars = pg.transform.scale_by(bars, 1 / 4)
        bars_width = bars.get_width()
        bars_height = bars.get_height() / 2
        health_bar = pg.Surface((bars_width, bars_height), pg.SRCALPHA)
        energy_bar = pg.Surface((bars_width, bars_height), pg.SRCALPHA)

        while True:
            if reset_active_pokemons and not delete_pokemon:
                self.inventory_surface.blit(background_select, (0, 0))
            elif not reset_active_pokemons and delete_pokemon:
                self.inventory_surface.blit(background_delete, (0, 0))
            else:
                self.inventory_surface.blit(background, (0, 0))

            for i, pokemon in enumerate(self.pokemons):
                frame = pokemon.get_pokemon_frames().get_idle_frame(1)
                frame = pg.transform.scale(frame, (self.size[0] / 6, self.size[1] / 6))
                if self.activePokemons[i]:
                    frame.blit(select_image, (0, 0))
                if i == index_to_show:
                    frame.blit(select_image_red, (0, 0))
                self.inventory_surface.blit(frame, (10 + self.size[0] / 11 + (i % 4) * self.size[0] / 4.5,
                                                    10 + self.size[1] / 9 + math.floor(i / 4) * self.size[1] / 4.5))
                self.inventory_surface.blit(font_texts[i], (10 + self.size[0] / 11 + (i % 4) * self.size[0] / 4.5 + (frame.get_width() - font_texts[i].get_width()) / 2,

                                                            self.size[1] / 9 + math.floor(i / 4) * self.size[1] / 4.5 - 10))
            self.display_surface.blit(pg.transform.scale(pg.image.load("./inventory/assets/pokemon_background.jpg"),
                                      (self.display_surface.get_width(), self.display_surface.get_height())), (0, 0))
            if show_ability_screen:
                self.display_surface.blit(ability_screen.get_ability_screen_surface(),
                                          (3 * self.display_surface.get_width() / 4 - ability_screen.get_ability_screen_surface().get_width() / 1,
                                           (self.display_surface.get_height() - ability_screen.get_ability_screen_surface().get_height()) / 2))

                self.display_surface.blit(health_bar,
                                          (self.display_surface.get_width() / 2 + ability_screen.get_ability_screen_surface().get_width() + 50,
                                          self.display_surface.get_height() / 2 - health_bar.get_height()))
                self.display_surface.blit(energy_bar,
                                          (self.display_surface.get_width() / 2 + ability_screen.get_ability_screen_surface().get_width() + 50,
                                          self.display_surface.get_height() / 2))

            self.display_surface.blit(self.inventory_surface, (0, 50))
            for event in pg.event.get():
                mouse_pos = pg.mouse.get_pos()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed()[0]:
                        if not reset_active_pokemons and not delete_pokemon:
                            x = int((mouse_pos[0] - self.size[0] / 11) * (4.5 / self.size[0]))
                            y = int((mouse_pos[1] - self.size[1] / 9) * (4.5 / self.size[1]))
                            if 0 <= x <= 3 and 0 <= y <= 3:
                                if x + 4 * y < self.noOfPokemons:
                                    if index_to_show == x + 4 * y:
                                        show_ability_screen = False
                                        index_to_show = -1
                                    else:
                                        show_ability_screen = True
                                        index_to_show = x + 4 * y
                                        ability_screen.update_ability_screen(self.pokemons[index_to_show])
                                        change_health_bar(health_bar,
                                                          bars,
                                                          1 - self.pokemons[index_to_show].get_health() / self.pokemons[index_to_show].get_maxHealth(),
                                                          health_texts[index_to_show])
                                        change_energy_bar(energy_bar,
                                                          bars,
                                                          0,
                                                          energy_texts[index_to_show])
                        # Se face inventarul verde si se selecteaza pokemonii de vrei sa ii slectezi in batalie
                        if reset_active_pokemons:
                            x = int((mouse_pos[0] - self.size[0] / 11) * (4.5 / self.size[0]))
                            y = int((mouse_pos[1] - self.size[1] / 9) * (4.5 / self.size[1]))
                            if 0 <= x <= 3 and 0 <= y <= 3:
                                if x + 4 * y < self.noOfPokemons:
                                    self.activePokemons[x + 4 * y] = True
                                    activated_pokemons += 1
                                    if activated_pokemons >= 3:
                                        reset_active_pokemons = False
                                        activated_pokemons = 0
                        # Se face inventarul rosu si poti apasa pe pokemoni sa ii stergi
                        # Se verifica daca ai mai mult de 3 pokemoni, nu poti sterge toti pokemonii trebuie sa ai minim 3 in inventar
                        if delete_pokemon and self.noOfPokemons > 3:
                            x = int((mouse_pos[0] - self.size[0] / 11) * (4.5 / self.size[0]))
                            y = int((mouse_pos[1] - self.size[1] / 9) * (4.5 / self.size[1]))
                            if 0 <= x <= 3 and 0 <= y <= 3:
                                if x + 4 * y < self.noOfPokemons:
                                    self.noOfPokemons -= 1
                                    self.pokemons.pop(x + 4 * y)
                                    if self.activePokemons[x + 4 * y]:
                                        self.activePokemons[x + 4 * y] = False
                                        for i in range(16):
                                            if not self.activePokemons[i]:
                                                self.activePokemons[i] = True
                                                break
                        else:
                            delete_pokemon = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r and not reset_active_pokemons and not delete_pokemon:
                        for i in range(16):
                            self.activePokemons[i] = False
                        reset_active_pokemons = True
                        show_ability_screen = False
                        activated_pokemons = 0
                    if event.key == pg.K_ESCAPE and not reset_active_pokemons and not delete_pokemon:
                        return
                    if event.key == pg.K_e and not reset_active_pokemons and not delete_pokemon:
                        return
                    if event.key == pg.K_DELETE and not reset_active_pokemons:
                        delete_pokemon = not delete_pokemon
                        show_ability_screen = False
            pg.display.update()
            clock.tick(120)