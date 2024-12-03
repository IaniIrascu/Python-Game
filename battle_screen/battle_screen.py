import pygame as pg
import sys
from pokemon.ability_screen import *
from utils.colors import *
from pokemon.effects.effect import Effect
import random
import math
import builtins
from pokemon.ability_screen.ability_screen import *
from battle_screen.funtions import *

SPEEDOFANIMATION = 0.12  # Valoare intre (0 si 1)

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

        ability_screen = create_ability_screen()

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

        # Ajuta la optimizarea programului
        bar_changed = [[True, True], [True, True]]

        # Effects name
        effects_end_of_turn = ["Poison", "Weakness", "Burned", "Restoration", "Stunned"]
        effects_when_attacked = ["Bleeding"]
        negative_effects = ["Poison", "Weakness", "Burned", "Bleeding", "Stunned"]
        positive_effects = ["Restoration"]
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
                        self.pokemons_surface.blit(ability_screen.get_ability_screen_surface(),
                                                   ability_screen_position)

                    # Adding the effects
                    effects = self.player_pokemons[active_pokemon_index].get_effects()
                    for i, effect in enumerate(effects):
                        self.pokemons_surface.blit(effect.get_effectIcon(),
                                                   (self.positions_on_screen[0][0] - 60,
                                                    self.positions_on_screen[0][1] + (i * self.player_pokemons[0].get_pokemon_frames().get_size()[0]) / len(effects)))

                    # Adding hp_bar
                    if bar_changed[0][0]:
                        percentage = self.player_pokemons[active_pokemon_index].get_health() / self.player_pokemons[active_pokemon_index].get_maxHealth()
                        change_health_bar(health_bar,
                                          bars,
                                          1 - percentage,
                                          FONT.render(str(round(self.player_pokemons[active_pokemon_index].get_health(), 2)) + "/" + str(self.player_pokemons[active_pokemon_index].get_maxHealth()), True, WHITE, None))
                        bar_changed[0][0] = False
                    # Adding energy bar
                    if bar_changed[0][1]:
                        percentage = self.player_pokemons[active_pokemon_index].get_energy() / self.player_pokemons[active_pokemon_index].get_maxEnergy()
                        change_energy_bar(energy_bar,
                                          bars,
                                          1 - percentage,
                                          FONT.render(str(round(self.player_pokemons[active_pokemon_index].get_energy(), 2)) + "/" + str(self.player_pokemons[active_pokemon_index].get_maxEnergy()), True, WHITE, None))
                        bar_changed[0][1] = False
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
                    if bar_changed[1][0]:
                        percentage = self.enemies[active_enemy_index].get_health() / self.enemies[active_enemy_index].get_maxHealth()
                        change_health_bar(health_bar_enemy,
                                          bars,
                                          1 - percentage,
                                          FONT.render(str(round(self.enemies[active_enemy_index].get_health(), 2)) + "/" + str(self.enemies[active_enemy_index].get_maxHealth()), True, WHITE, None))
                        bar_changed[1][0] = False

                    if bar_changed[1][1]:
                        percentage = self.enemies[active_enemy_index].get_energy() / self.enemies[active_enemy_index].get_maxEnergy()
                        change_energy_bar(energy_bar_enemy,
                                          bars,
                                          1 - percentage,
                                          FONT.render(str(round(self.enemies[active_enemy_index].get_energy(), 2)) + "/" + str(self.enemies[active_enemy_index].get_maxEnergy()), True, WHITE, None))
                        bar_changed[1][1] = False

                    self.pokemons_surface.blit(health_bar_enemy,
                                               (self.positions_on_screen[1][0] + self.enemies[active_enemy_index].get_pokemon_frames().get_size()[0] / 2 - 160,
                                                self.positions_on_screen[1][1] + self.enemies[active_enemy_index].get_pokemon_frames().get_size()[1]))
                    self.pokemons_surface.blit(energy_bar_enemy,
                                               (self.positions_on_screen[1][0] + self.enemies[active_enemy_index].get_pokemon_frames().get_size()[0] / 2 - 160,
                                                self.positions_on_screen[1][1] + self.enemies[active_enemy_index].get_pokemon_frames().get_size()[1] + 100))
                    break

            # Atacul tau
            if add_attack[0] and attack_playing:
                # Se animeza atacul pe 30 frame-uri
                if int((frame - initial_frame)) < 40:
                    frame_to_get = int((frame - initial_frame) * SPEEDOFANIMATION) % 4 + 1
                    self.pokemons_surface.blit(self.player_pokemons[active_pokemon_index].get_attack().get_attack_frames().get_attack_frame(frame_to_get),
                                               self.positions_on_screen[1])
                else:
                    # ACTIVE DAMAGE
                    result = active_update_pokemon(self.player_pokemons[active_pokemon_index],
                                                   self.enemies[active_enemy_index],
                                                   self.enemies[number_of_enemies - 1],
                                                   effects_when_attacked)

                    if result == "MainMenu":
                        experience = calculate_experience(self.enemies)
                        for pokemon in self.player_pokemons:
                            if not pokemon.get_isDead():
                                pokemon.set_experience(experience + pokemon.get_experience())
                                level_up_pokemon(pokemon)

                        reset_pokemons(self.player_pokemons, self.enemies)
                        return "MainMenu"
                    elif result == "DEAD":
                        attack_playing = False
                        add_special[0] = False
                    bar_changed[1][0] = True

                    # PASSIVE DAMAGE AFTER ATTACKING
                    result = passive_update_pokemon(self.player_pokemons[active_pokemon_index],
                                              self.player_pokemons[len(self.player_pokemons) - 1],
                                              effects_end_of_turn)
                    if result== "MainMenu":
                        reset_pokemons(self.player_pokemons, self.enemies)
                        return "MainMenu"
                    if result == "DEAD":
                        attack_playing = False
                        add_special[0] = False

                    bar_changed[0][0] = True
                    bar_changed[0][1] = True

                    add_attack[0] = False
                    if not add_special[0]:
                        initial_frame = frame
                        wait_a_bit[0] = True

            if add_special[0] and (not add_attack[0]) and attack_playing:
                # Se creeaza efectul
                effect_refs = self.player_pokemons[active_pokemon_index].get_special_attack().get_effects()
                for effect_ref in effect_refs:
                    check_effect = False
                    # Search if effect is already applied
                    for effect in self.enemies[active_enemy_index].get_effects():
                        if effect.get_name() == effect_ref.get_name():
                            effect.set_number_of_turns_left(effect.get_number_of_turns_left() + 2)
                            effect.change_effectIcon(color=effect_ref.get_color(), number=effect.get_number_of_turns_left())
                            check_effect = True

                    for effect in self.player_pokemons[active_pokemon_index].get_effects():
                        if effect.get_name() == effect_ref.get_name() and effect.get_name() in positive_effects:
                            effect.set_number_of_turns_left(effect.get_number_of_turns_left() + 2)
                            effect.change_effectIcon(color=effect_ref.get_color(), number=effect.get_number_of_turns_left())
                            effect.set_justApplied(True)
                            check_effect = True

                    if not check_effect:
                        effect_to_add = Effect()
                        effect_to_add.set_name(effect_ref.get_name())
                        effect_to_add.set_number_of_turns_left(2)
                        effect_to_add.change_effectIcon(color=effect_ref.get_color(), number=effect_to_add.get_number_of_turns_left())
                        # Se adauga efectul la lista
                        if effect_to_add.get_name() in negative_effects:
                            self.enemies[active_enemy_index].add_effect_on_itself(effect_to_add)
                        elif effect_to_add.get_name() in positive_effects:
                            self.player_pokemons[active_pokemon_index].add_effect_on_itself(effect_to_add)

                initial_frame = frame
                add_special[0] = False
                if not self.enemies[active_enemy_index].get_isDead():
                    wait_a_bit[0] = True
                else:
                    wait_a_bit[0] = False

            if wait_a_bit[0] and attack_playing:
                # Wait for 50 frames
                if int((frame - initial_frame)) <= 100:
                    pass
                else:
                    # Se pregatesc verificarile daca inamicul isi poate folosi atacul special
                    enemy_attack = random.randint(0, 2)
                    attack_energy_cost = self.enemies[active_enemy_index].get_special_attack().get_energy_cost()
                    enemy_energy = self.enemies[active_enemy_index].get_energy()

                    if enemy_attack == 0:
                        add_attack[1] = True
                        add_special[1] = False
                    elif enemy_attack == 1 and enemy_energy >= attack_energy_cost:
                        bar_changed[1][1] = True
                        self.enemies[active_enemy_index].set_energy(enemy_energy - attack_energy_cost)
                        add_attack[1] = True
                        add_special[1] = True
                    elif enemy_attack == 2 and enemy_energy + 0.3 * self.enemies[active_enemy_index].get_maxEnergy() <= self.enemies[active_enemy_index].get_maxEnergy():
                        bar_changed[1][1] = True
                        self.enemies[active_enemy_index].set_energy(self.enemies[active_enemy_index].get_energy() + 0.3 * self.enemies[active_enemy_index].get_maxEnergy())
                        if self.enemies[active_enemy_index].get_energy() > self.enemies[active_enemy_index].get_maxEnergy():
                            self.enemies[active_enemy_index].set_energy(self.enemies[active_enemy_index].get_maxEnergy())
                        attack_playing = False
                        add_special[1] = False
                        add_special[1] = False
                    else:
                        add_attack[1] = True
                        add_special[1] = False
                    wait_a_bit[0] = False
                    initial_frame = frame

            # Atacul inamicului
            if add_attack[1] and attack_playing:
                if int((frame - initial_frame)) <= 30:
                    frame_to_get = int((frame - initial_frame) * SPEEDOFANIMATION) % 4 + 1
                    self.pokemons_surface.blit(self.enemies[active_enemy_index].get_attack().get_attack_frames().get_attack_frame(frame_to_get),
                                               self.positions_on_screen[0])
                else:
                    # ACTIVE DAMAGE
                    result = active_update_pokemon(self.enemies[active_enemy_index],
                                                   self.player_pokemons[active_pokemon_index],
                                                   self.player_pokemons[number_of_player_pokemons - 1],
                                                   effects_when_attacked)

                    if result == "MainMenu":
                        reset_pokemons(self.player_pokemons, self.enemies)
                        return "MainMenu"
                    elif result == "DEAD":
                        attack_playing = False
                        add_special[1] = False

                    bar_changed[0][0] = True
                    # PASSIVE DAMAGE AFTER ATTACK
                    result = passive_update_pokemon(self.enemies[active_enemy_index],
                                              self.enemies[len(self.enemies) - 1],
                                              effects_end_of_turn)
                    if result == "MainMenu":
                        experience = calculate_experience(self.enemies)
                        for pokemon in self.player_pokemons:
                            if not pokemon.get_isDead():
                                pokemon.set_experience(experience + pokemon.get_experience())
                                level_up_pokemon(pokemon)
                        reset_pokemons(self.player_pokemons, self.enemies)
                        return "MainMenu"
                    elif result == "DEAD":
                        attack_playing = False
                        add_special[1] = False
                    bar_changed[1][0] = True
                    bar_changed[1][1] = True

                    # Se continua atacul
                    add_attack[1] = False
                    if not add_special[1]:
                        wait_a_bit[1] = True

            if add_special[1] and not add_attack[1] and attack_playing:
                # Se creeaza efectul
                effect_refs = self.enemies[active_enemy_index].get_special_attack().get_effects()
                for effect_ref in effect_refs:
                    check_effect = False
                    for effect in self.player_pokemons[active_pokemon_index].get_effects():
                        if effect.get_name() == effect_ref.get_name() and effect.get_name() in negative_effects:
                            effect.set_number_of_turns_left(effect.get_number_of_turns_left() + 2)
                            effect.change_effectIcon(color=effect_ref.get_color(), number=effect.get_number_of_turns_left())
                            effect.set_justApplied(True)
                            check_effect = True

                    for effect in self.enemies[active_enemy_index].get_effects():
                        if effect.get_name() == effect_ref.get_name() and effect.get_name() in positive_effects:
                            effect.set_number_of_turns_left(effect.get_number_of_turns_left() + 2)
                            effect.change_effectIcon(color=effect_ref.get_color(), number=effect.get_number_of_turns_left())
                            effect.set_justApplied(True)
                            check_effect = True

                    if not check_effect:
                        effect_to_add = Effect()
                        effect_to_add.set_name(effect_ref.get_name())
                        effect_to_add.set_number_of_turns_left(2)
                        effect_to_add.change_effectIcon(color=effect_ref.get_color(), number = 2)
                        effect_to_add.set_justApplied(True)

                        # Se adauga efectul la lista
                        if effect_to_add.get_name() in negative_effects:
                            self.player_pokemons[active_pokemon_index].add_effect_on_itself(effect_to_add)
                        elif effect_to_add.get_name() in positive_effects:
                            self.enemies[active_enemy_index].add_effect_on_itself(effect_to_add)

                add_special[1] = False
                wait_a_bit[1] = True

            if wait_a_bit[1] and attack_playing:
                # Wait for 40 frames
                if int((frame - initial_frame)) <= 100:
                    pass
                else:
                    attack_playing = False
                    wait_a_bit[1] = False

            # Combinare suprafete si afisare
            self.display_surface.blit(self.pokemons_surface, (0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        reset_pokemons(self.player_pokemons, self.enemies)
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
                        if pg.mouse.get_pressed()[0] == 1:
                            add_ability_surface = not add_ability_surface
                    selected[0] = True
                else:
                    selected[0] = False

                if add_ability_surface and (not attack_playing):
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0] == 1:
                            # Update it here
                            ability_screen.update_ability_screen(self.player_pokemons[active_pokemon_index])
                            result = check_button_pressed(mouse_pos,
                                                          ability_screen,
                                                          ability_screen_position)
                            pokemon_energy = self.player_pokemons[active_pokemon_index].get_energy()
                            attack_energy_cost = self.player_pokemons[active_pokemon_index].get_special_attack().get_energy_cost()
                            if result == "X":
                                add_ability_surface = False
                            if result == "Attack":
                                attack_playing = True
                                initial_frame = frame
                                add_ability_surface = False
                                add_attack[0] = True
                            if result == "Special" and attack_energy_cost <= pokemon_energy:
                                bar_changed[0][1] = True
                                self.player_pokemons[active_pokemon_index].set_energy(pokemon_energy - attack_energy_cost)
                                attack_playing = True
                                add_special[0] = True
                                add_ability_surface = False
                                add_attack[0] = True
                                initial_frame = frame

                            if result == "Switch":
                                bar_changed = [[True, True], [True, True]]

                                # Se rotesc doar pokemonii in viata
                                self.player_pokemons = (self.player_pokemons[:active_pokemon_index] +
                                                        self.player_pokemons[active_pokemon_index + 1:] +
                                                        [self.player_pokemons[active_pokemon_index]])  # Rotate alive pokemons
                                ability_screen.update_ability_screen(self.player_pokemons[active_pokemon_index])

                            if result == "Skip Turn":
                                self.player_pokemons[active_pokemon_index].set_energy(self.player_pokemons[active_pokemon_index].get_energy() + 0.3 * self.player_pokemons[active_pokemon_index].get_maxEnergy())
                                if self.player_pokemons[active_pokemon_index].get_energy() > self.player_pokemons[active_pokemon_index].get_maxEnergy():
                                    self.player_pokemons[active_pokemon_index].set_energy(self.player_pokemons[active_pokemon_index].get_maxEnergy())
                                bar_changed[0][1] = True
                                attack_playing = True
                                add_attack[0] = False
                                add_special[0] = False
                                wait_a_bit[0] = True
                                initial_frame = frame
                                add_ability_surface = False

                pokemon_rect = pg.Rect(self.positions_on_screen[1][0],
                                       self.positions_on_screen[1][1],
                                       self.enemies[active_enemy_index].get_pokemon_frames().get_size()[0],
                                       self.enemies[active_enemy_index].get_pokemon_frames().get_size()[1])
                if pokemon_rect.collidepoint(mouse_pos):
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0] == 1:
                            print(active_enemy_index)
                    selected[1] = True
                else:
                    selected[1] = False

            pg.display.update()
            frame += 1
            if frame > 1000000000:
                reset_pokemons(self.player_pokemons, self.enemies)
                return "MainMenu"
            clock.tick(60)