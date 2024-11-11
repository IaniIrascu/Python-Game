import pygame as pg
import sys
from pokemoni.ability_screen import *

SPEEDOFANIMATION = 1 / 8  # Valoare intre (0 si 1)

def check_button_pressed(mouse_pos, ability_screen, ability_screen_position):
    buttons = ability_screen.get_buttons()
    for button_name in buttons:
        button_rect = pg.Rect(ability_screen_position[0] + buttons[button_name].get_position()[0],
                              ability_screen_position[1] + buttons[button_name].get_position()[1],
                              buttons[button_name].get_size()[0],
                              buttons[button_name].get_size()[1])
        if button_rect.collidepoint(mouse_pos):
            return button_name

class Battle_screen():
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.pokemons_surface = pg.Surface(display_surface.get_size(), pg.SRCALPHA)
        self.background_surface = pg.Surface(display_surface.get_size(), pg.SRCALPHA)
        self.enemies = []
        self.player_pokemons = []
        self.positions_on_screen = [(175, self.display_surface.get_height() / 2 - 100),
                                    (self.display_surface.get_width() - 525, self.display_surface.get_height() / 2 - 100)]

    def load_enemies(self, enemies):
        self.enemies = enemies

    def load_player_pokemons(self, player_pokemons):
        self.player_pokemons = player_pokemons

    def get_enemies(self):
        return self.enemies

    def get_player_pokemons(self):
        return self.player_pokemons

    # RUN
    def run(self, clock):
        frame = 0

        # Creare suprafata background
        background = pg.image.load('./battle_screen/assets/forest.png')
        background = pg.transform.scale(background, (self.display_surface.get_width(), self.display_surface.get_height()))
        self.background_surface.blit(background, (0, 0))

        active_pokemon_index = 0
        active_enemy_index = 0
        self.player_pokemons[active_pokemon_index].set_isActive(True)
        self.enemies[active_enemy_index].set_isActive(True)

        select_square = pg.image.load('./battle_screen/assets/select.png')
        select_square.set_colorkey((255, 255, 255))
        select_square.convert_alpha()
        select_square = pg.transform.scale(select_square, self.player_pokemons[0].get_pokemon_frames().get_size())
        selected = [False, False]

        # Numarul de inamici si nr de pokemoni pe care ii are playerul activi in momentul acela
        number_of_enemies = len(self.enemies)
        number_of_player_pokemons = len(self.player_pokemons)

        # Variabile cu care determin daca meniul de abilitati este vizibil sau daca se porneste animatia de attack
        add_ability_surface = False
        add_attack = [False, False]
        add_special = [False, False]

        # Frameul la care incepe animatia de atac
        initial_frame = 0

        # Pozitia meniului cu abilitati
        ability_screen_position = (self.pokemons_surface.get_width() / 2 - 200, 100)

        while True:
            # creare enemies_surface cu frame-urile aferente
            self.pokemons_surface.blit(self.background_surface, (0, 0))
            for index, player_pokemon in enumerate(self.player_pokemons):
                if not player_pokemon.get_isDead():
                    player_pokemon.set_isActive(True)
                    active_pokemon_index = index

                    # Player attacking
                    if add_attack[0] or add_special[0]:
                    if add_attack[0] or add_special[0]:
                        frame_to_get = int((frame - initial_frame) * SPEEDOFANIMATION) % 4 + 1
                        self.pokemons_surface.blit(pg.transform.flip(player_pokemon.get_pokemon_frames().get_attack_frame(frame_to_get), flip_x=True, flip_y = False),
                                                   self.positions_on_screen[0])

                    # Player idling
                    else:
                        frame_to_get = int(frame * SPEEDOFANIMATION) % 4 + 1
                        self.pokemons_surface.blit(pg.transform.flip(player_pokemon.get_pokemon_frames().get_idle_frame(frame_to_get), flip_x=True, flip_y = False),
                                                   self.positions_on_screen[0])

                    # Player selected pokemon
                    if selected[0]:
                        self.pokemons_surface.blit(select_square,
                                                   self.positions_on_screen[0])

                    # Player opened ability menu
                    if add_ability_surface:
                        self.pokemons_surface.blit(player_pokemon.get_ability_screen().get_ability_screen_surface(),
                                                   ability_screen_position)
                    break

            for index, enemy in enumerate(self.enemies):
                if not enemy.get_isDead():
                    enemy.set_isActive(True)
                    active_enemy_index = index
                    # Enemy attacking
                    if add_attack[1] or add_special[1]:
                        frame_to_get = int((frame - initial_frame) * SPEEDOFANIMATION) % 4 + 1
                        self.pokemons_surface.blit(enemy.get_pokemon_frames().get_attack_frame(frame_to_get),
                                                   self.positions_on_screen[1])
                    # Enemy idling
                    else:
                        frame_to_get = int(frame * SPEEDOFANIMATION) % 4 + 1
                        self.pokemons_surface.blit(enemy.get_pokemon_frames().get_idle_frame(frame_to_get),
                                                   self.positions_on_screen[1])
                    if selected[1]:
                        self.pokemons_surface.blit(select_square,
                                                   self.positions_on_screen[1])
                    break

            # Se porneste animatia de atac pentru 48 de frame-uri
            if add_attack[0]:
                if int((frame - initial_frame) * SPEEDOFANIMATION) <= 3:
                    frame_to_get = int((frame - initial_frame) * SPEEDOFANIMATION) % 4 + 1
                    self.pokemons_surface.blit(self.player_pokemons[active_pokemon_index].get_attack().get_attack_frames().get_attack_frame(frame_to_get),
                                               self.positions_on_screen[1])
                else:
                    add_attack[0] = False
                    add_attack[1] = True
                    health = self.enemies[active_enemy_index].get_health()
                    health -= (self.player_pokemons[active_pokemon_index].get_damage() + 30)  # Atac pokemon
                    # Verify if enemy died after the last attack
                    if health <= 0:
                        add_attack[1] = False  # Inamicul nu mai ataca
                        self.enemies[active_enemy_index].set_isDead(True)  # Inamicul moare
                        if self.enemies[number_of_enemies - 1].get_isDead(): # Daca a murit ultimul inamic se trece in meniu
                            return "MainMenu"
                    else:
                        self.player_pokemons[active_pokemon_index].set_health(health)

                        # Se incepe atacul inamicului
                        initial_frame = frame

            # Atacul inamicului
            if add_attack[1]:
                if int((frame - initial_frame) * SPEEDOFANIMATION) <= 3:
                    frame_to_get = int((frame - initial_frame) * SPEEDOFANIMATION) % 4 + 1
                    self.pokemons_surface.blit(self.enemies[active_enemy_index].get_attack().get_attack_frames().get_attack_frame(frame_to_get),
                                               self.positions_on_screen[0])
                else:
                    add_attack[1] = False
                    health = self.player_pokemons[active_pokemon_index].get_health()
                    health -= self.enemies[active_enemy_index].get_damage() # Atac inamic
                    if health <= 0:
                        self.player_pokemons[active_pokemon_index].set_isDead(True) # Pokemonul moare
                        if self.player_pokemons[number_of_player_pokemons - 1]: # Ultimul pokemon e mort
                            return "MainMenu"
                    else:
                        self.player_pokemons[active_pokemon_index].set_health(health)

            # Verify if all enemies are dead or all player_pokemons are dead
            dead_enemies = 0
            dead_player_pokemons = 0
            for enemy in self.enemies:
                if enemy.get_isDead():
                    dead_enemies += 1

            if dead_enemies == number_of_enemies:
                return "MainMenu"

            for player_pokemon in self.player_pokemons:
                if player_pokemon.get_isDead():
                    dead_player_pokemons += 1

            if dead_player_pokemons == number_of_player_pokemons:
                return "MainMenu"

            # Combinare suprafete si afisare
            self.display_surface.blit(self.pokemons_surface, (0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return "MainMenu"
                mouse_pos = pg.mouse.get_pos()

                # checking if pokemon is clicked or if cursor is on it
                # add an arrow to indicate that the pokemon was selected
                pokemon_rect = pg.Rect(self.positions_on_screen[0][0],
                                       self.positions_on_screen[0][1],
                                       self.player_pokemons[active_pokemon_index].get_pokemon_frames().get_size()[0],
                                       self.player_pokemons[active_pokemon_index].get_pokemon_frames().get_size()[1])
                if pokemon_rect.collidepoint(mouse_pos):
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0] == 1 and add_ability_surface == False:
                            add_ability_surface = True
                    selected[0] = True
                else:
                    selected[0] = False

                if add_ability_surface:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0] == 1:
                            result = check_button_pressed(mouse_pos,
                                                          self.player_pokemons[active_pokemon_index].get_ability_screen(),
                                                          ability_screen_position)
                            if result == "X":
                                add_ability_surface = False
                            if result == "Attack" and add_attack[0] == False:
                                add_attack[0] = True
                                initial_frame = frame
                                add_ability_surface = False
                            if result == "Special" and add_special[0] == False:
                                add_special[0] = True
                                initial_frame = frame
                                add_ability_surface = False

                pokemon_rect = pg.Rect(self.positions_on_screen[1][0],
                                       self.positions_on_screen[1][1],
                                       self.enemies[active_enemy_index].get_pokemon_frames().get_size()[0],
                                       self.enemies[active_enemy_index].get_pokemon_frames().get_size()[1])
                if pokemon_rect.collidepoint(mouse_pos):
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0] == 1:
                            self.enemies[active_enemy_index].set_isDead(True)
                            print(active_enemy_index)
                    selected[1] = True
                else:
                    selected[1] = False

            pg.display.update()
            frame += 1
            clock.tick(60)