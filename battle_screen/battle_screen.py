import pygame as pg
import sys
from pokemoni.ability_screen import *
from utils.colors import *
from pokemoni.effects.effect import Effect
import random

SPEEDOFANIMATION = 0.1  # Valoare intre (0 si 1)

def check_button_pressed(mouse_pos, ability_screen, ability_screen_position):
    buttons = ability_screen.get_buttons()
    for button_name in buttons:
        button_rect = pg.Rect(ability_screen_position[0] + buttons[button_name].get_position()[0],
                              ability_screen_position[1] + buttons[button_name].get_position()[1],
                              buttons[button_name].get_size()[0],
                              buttons[button_name].get_size()[1])
        if button_rect.collidepoint(mouse_pos):
            return button_name

# NU SCHIMBATI NUMERE PRIN PROGRAM
def change_health_bar(health_bar, bars_surface, percentage):
    removeFromBar = (health_bar.get_width() - 115) * percentage
    width = health_bar.get_width()
    height = health_bar.get_height()
    health_bar.fill((0, 0, 0, 0))
    health_bar.fill(RED, (90, 37, width - 115 - removeFromBar, height / 3))
    health_bar.blit(bars_surface, (0, 0), (0, 0, width, height))

def change_energy_bar(energy_bar, bars_surface, percentage):
    removeFromBar = (energy_bar.get_width() - 115) * percentage
    width = energy_bar.get_width()
    height = energy_bar.get_height()
    energy_bar.fill((0, 0, 0, 0))
    energy_bar.fill(BLUE, (90, 37, width - 115 - removeFromBar, height / 3))
    energy_bar.blit(bars_surface, (0, 0), (0, height, width, height))

class Battle_screen:
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
        final_turns = [False, False]
        wait_a_bit = [False, False]

        attack_playing = False
        # Frameul la care incepe animatia de atac
        initial_frame = 0

        # Pozitia meniului cu abilitati
        ability_screen_position = (self.pokemons_surface.get_width() / 2 - 200, 100)

        bars = pg.image.load('./battle_screen/assets/Bars.png')
        bars.convert_alpha()
        bars = pg.transform.scale_by(bars, 1 / 4)
        bars_width = bars.get_width()
        bars_height = bars.get_height() / 2

        # HEALTH BAR
        health_bar = pg.Surface((bars_width, bars_height), pg.SRCALPHA)
        health_bar_enemy = pg.Surface((bars_width, bars_height), pg.SRCALPHA)
        # ENERGY BAR
        energy_bar = pg.Surface((bars_width, bars_height), pg.SRCALPHA)
        energy_bar_enemy = pg.Surface((bars_width, bars_height), pg.SRCALPHA)

        while True:
            # creare enemies_surface cu frame-urile aferente
            self.pokemons_surface.blit(self.background_surface, (0, 0))
            for index, player_pokemon in enumerate(self.player_pokemons):
                if not player_pokemon.get_isDead():
                    player_pokemon.set_isActive(True)
                    active_pokemon_index = index

                    # Player attacking
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
                    if selected[0] and not attack_playing:
                        self.pokemons_surface.blit(select_square,
                                                   self.positions_on_screen[0])

                    # Player opened ability menu
                    if add_ability_surface and not attack_playing:
                        self.pokemons_surface.blit(player_pokemon.get_ability_screen().get_ability_screen_surface(),
                                                   ability_screen_position)

                    # Adding the effects
                    effects = self.player_pokemons[active_pokemon_index].get_effects()
                    for i, effect in enumerate(effects):
                        self.pokemons_surface.blit(effect.get_effectIcon(),
                                                   (self.positions_on_screen[0][0] - 60,
                                                    self.positions_on_screen[0][1] + (i * self.player_pokemons[0].get_pokemon_frames().get_size()[0]) / len(effects)))

                    # Adding the names + lv

                    # Adding hp_bar
                    percentage = self.player_pokemons[active_pokemon_index].get_health() / self.player_pokemons[active_pokemon_index].get_maxHealth()
                    change_health_bar(health_bar, bars, 1 - percentage)
                    # print(self.player_pokemons[active_pokemon_index].get_health())
                    # print(1 - percentage)
                    percentage = self.player_pokemons[active_pokemon_index].get_energy() / self.player_pokemons[active_pokemon_index].get_maxEnergy()
                    change_energy_bar(energy_bar, bars, 1 - percentage)
                    self.pokemons_surface.blit(health_bar,
                                               (self.positions_on_screen[0][0] + self.player_pokemons[active_pokemon_index].get_pokemon_frames().get_size()[0] /2 - 160,
                                                self.positions_on_screen[0][1] + self.player_pokemons[active_pokemon_index].get_pokemon_frames().get_size()[1]))
                    self.pokemons_surface.blit(energy_bar,
                                               (self.positions_on_screen[0][0] + self.player_pokemons[active_pokemon_index].get_pokemon_frames().get_size()[0] /2 - 160,
                                                self.positions_on_screen[0][1] + self.player_pokemons[active_pokemon_index].get_pokemon_frames().get_size()[1] + 100))
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
                    if selected[1] and not attack_playing:
                        self.pokemons_surface.blit(select_square,
                                                   self.positions_on_screen[1])

                    # Adding the effects
                    effects = self.enemies[active_enemy_index].get_effects()
                    for i, effect in enumerate(effects):
                        self.pokemons_surface.blit(effect.get_effectIcon(),
                                                   (self.positions_on_screen[1][0] + self.enemies[0].get_pokemon_frames().get_size()[1] + 60,
                                                    self.positions_on_screen[1][1] + (i * self.enemies[0].get_pokemon_frames().get_size()[0]) / len(effects)))

                    # Adding hp_bar
                    percentage = self.enemies[active_enemy_index].get_health() / self.enemies[active_enemy_index].get_maxHealth()
                    change_health_bar(health_bar_enemy, bars, 1 - percentage)
                    percentage = self.enemies[active_enemy_index].get_energy() / self.enemies[active_enemy_index].get_maxEnergy()
                    change_energy_bar(energy_bar_enemy, bars, 1 - percentage)
                    self.pokemons_surface.blit(health_bar_enemy,
                                               (self.positions_on_screen[1][0] + self.enemies[active_enemy_index].get_pokemon_frames().get_size()[0] / 2 - 160,
                                                self.positions_on_screen[1][1] + self.enemies[active_enemy_index].get_pokemon_frames().get_size()[1]))
                    self.pokemons_surface.blit(energy_bar_enemy,
                                               (self.positions_on_screen[1][0] + self.enemies[active_enemy_index].get_pokemon_frames().get_size()[0] / 2 - 160,
                                                self.positions_on_screen[1][1] + self.enemies[active_enemy_index].get_pokemon_frames().get_size()[1] + 100))
                    break

            # Atacul tau
            if add_attack[0]:
                if int((frame - initial_frame)) < 40:
                    frame_to_get = int((frame - initial_frame) * SPEEDOFANIMATION) % 4 + 1
                    self.pokemons_surface.blit(self.player_pokemons[active_pokemon_index].get_attack().get_attack_frames().get_attack_frame(frame_to_get),
                                               self.positions_on_screen[1])
                else:
                    add_attack[0] = False
                    final_turns[0] = True

            if add_special[0] and not add_attack[0]:
                # Se creeaza efectul
                check_effect = False
                effect_ref = self.player_pokemons[active_pokemon_index].get_attack().get_effect()
                # Search if effect is already applied
                for effect in self.enemies[active_enemy_index].get_effects():
                    if effect.get_name() == effect_ref.get_name():
                        effect.set_number_of_turns_left(effect.get_number_of_turns())
                        effect.set_justApplied(True)
                        check_effect = True

                if not check_effect:
                    effect_to_add = Effect()
                    effect_to_add.set_name(effect_ref.get_name())
                    effect_to_add.set_number_of_turns(effect_ref.get_number_of_turns())
                    effect_to_add.set_number_of_turns_left(effect_ref.get_number_of_turns())
                    effect_to_add.change_effectIcon(color=effect_ref.get_color(), number = effect_ref.get_number_of_turns())
                    effect_to_add.set_justApplied(True)

                    # Se adauga efectul la lista
                    self.enemies[active_enemy_index].add_effect_on_itself(effect_to_add)

                add_special[0] = False

            if final_turns[0]:
                # Aici mai pot fi puse chestii

                # Se modifica numarul de ture ramase pentru effect
                self.player_pokemons[active_pokemon_index].remove_one_turn_from_effects()
                self.player_pokemons[active_pokemon_index].check_what_effect_is_over()

                for effect in self.player_pokemons[active_pokemon_index].get_effects():
                    effect.change_effectIcon(color=effect.get_color(), number=effect.get_number_of_turns_left())

                # Se alege un atac random al inamicului
                health = self.enemies[active_enemy_index].get_health()
                health -= (self.player_pokemons[active_pokemon_index].get_damage() + 10)  # Atac pokemon
                # Verify if enemy died after the last attack
                if health <= 0:
                    add_attack[1] = False
                    add_special[1] = False
                    wait_a_bit[1] = False
                    attack_playing = False
                    self.enemies[active_enemy_index].set_isDead(True)  # Inamicul moare
                    if self.enemies[number_of_enemies - 1].get_isDead(): # Daca a murit ultimul inamic se trece in meniu
                        return "MainMenu"
                else:
                    self.enemies[active_enemy_index].set_health(health)

                # Se incepe wait-ul
                initial_frame = frame
                final_turns[0] = False
                if not self.enemies[active_enemy_index].get_isDead():
                    wait_a_bit[0] = True
                else:
                    wait_a_bit[0] = False

            if wait_a_bit[0]:
                # Wait for 50 frames
                if int((frame - initial_frame)) <= 40:
                    pass
                else:
                    enemy_attack = random.randint(0, 1)
                    if enemy_attack == 0:
                        add_attack[1] = True
                        add_special[1] = False
                    else:
                        add_attack[1] = True
                        add_special[1] = True
                    wait_a_bit[0] = False
                    initial_frame = frame

            # Atacul inamicului
            if add_attack[1]:
                if int((frame - initial_frame)) < 40:
                    frame_to_get = int((frame - initial_frame) * SPEEDOFANIMATION) % 4 + 1
                    self.pokemons_surface.blit(self.enemies[active_enemy_index].get_attack().get_attack_frames().get_attack_frame(frame_to_get),
                                               self.positions_on_screen[0])
                else:
                    # Se continua atacul
                    add_attack[1] = False
                    final_turns[1] = True

            if add_special[1] and not add_attack[1]:
                # Se creeaza efectul
                check_effect = False
                effect_ref = self.enemies[active_enemy_index].get_attack().get_effect()

                for effect in self.player_pokemons[active_pokemon_index].get_effects():
                    if effect.get_name() == effect_ref.get_name():
                        effect.set_number_of_turns_left(effect.get_number_of_turns())
                        effect.set_justApplied(True)
                        check_effect = True

                if not check_effect:
                    effect_to_add = Effect()
                    effect_to_add.set_name(effect_ref.get_name())
                    effect_to_add.set_number_of_turns(effect_ref.get_number_of_turns())
                    effect_to_add.set_number_of_turns_left(effect_ref.get_number_of_turns())
                    effect_to_add.change_effectIcon(color=effect_ref.get_color(), number = effect_ref.get_number_of_turns())
                    effect_to_add.set_justApplied(True)

                    # Se adauga efectul la lista
                    self.player_pokemons[active_pokemon_index].add_effect_on_itself(effect_to_add)

                add_special[1] = False

            if final_turns[1]:
                # Se modifica numarul de ture ramase pentru effect
                self.enemies[active_enemy_index].remove_one_turn_from_effects()
                self.enemies[active_enemy_index].check_what_effect_is_over()

                for effect in self.enemies[active_enemy_index].get_effects():
                    effect.change_effectIcon(color=effect.get_color(), number=effect.get_number_of_turns_left())

                health = self.player_pokemons[active_pokemon_index].get_health()
                health -= self.enemies[active_enemy_index].get_damage()  # Atac inamic
                if health <= 0:
                    self.player_pokemons[active_pokemon_index].set_isDead(True)  # Pokemonul moare
                    if self.player_pokemons[number_of_player_pokemons - 1].get_isDead():  # Ultimul pokemon e mort
                        return "MainMenu"
                else:
                    self.player_pokemons[active_pokemon_index].set_health(health)

                final_turns[1] = False
                wait_a_bit[1] = True

            if wait_a_bit[1]:
                # Wait for 40 frames
                if int((frame - initial_frame)) <= 40:
                    pass
                else:
                    attack_playing = False
                    wait_a_bit[1] = False

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
                        return "MainMenu"  # AICI AR TREBUI SA FIE ESCAPE MENU, DAR CAND SE FACE
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

                if add_ability_surface and not attack_playing:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0] == 1:
                            result = check_button_pressed(mouse_pos,
                                                          self.player_pokemons[active_pokemon_index].get_ability_screen(),
                                                          ability_screen_position)
                            if result == "X":
                                add_ability_surface = False
                            if result == "Attack" and add_attack[0] == False:
                                attack_playing = True
                                add_attack[0] = True
                                initial_frame = frame
                                add_ability_surface = False
                            if result == "Special" and add_special[0] == False:
                                attack_playing = True
                                add_special[0] = True
                                add_attack[0] = True
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
            if frame > 1000000000:
                return "MainMenu"
            clock.tick(60)