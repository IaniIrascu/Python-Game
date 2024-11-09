import pygame as pg
import sys
from pokemoni.pokemon import Pokemon

class Battle_screen():
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.pokemons_surface = pg.Surface(display_surface.get_size(), pg.SRCALPHA)
        self.background_surface = pg.Surface(display_surface.get_size(), pg.SRCALPHA)
        self.enemies = []
        self.player_pokemons = []

    def load_enemies(self, enemies):
        self.enemies = enemies

    def load_player_pokemons(self, player_pokemons):
        self.player_pokemons = player_pokemons

    def run(self, clock):
        # Creare suprafata background
        background = pg.image.load('./battle_screen/assets/forest.png')
        background = pg.transform.scale(background, (self.display_surface.get_width(), self.display_surface.get_height()))
        self.background_surface.blit(background, (0, 0))

        active_pokemon = self.player_pokemons[0]
        active_enemy = self.enemies[0]
        active_pokemon_index = 0
        active_enemy_index = 0
        enemy_position = (1300, 400)
        player_pokemon_position = (150, 400)

        frame = 0

        arrow = pg.image.load('./battle_screen/assets/sageata.png')
        arrow.set_colorkey((255, 255, 255))
        arrow.convert_alpha()

        # Sageti pentru evidentierea alegerii pokemonului
        left_arrow = pg.transform.scale(arrow, (50, 50))
        right_arrow = pg.transform.rotate(left_arrow, 180)

        add_arrow = [False, False]
        arrow_pos = (0, 0)

        # Numarul de inamici si nr de pokemoni pe care ii are playerul activi in momentul acela
        number_of_enemies = len(self.enemies)
        number_of_player_pokemons = len(self.player_pokemons)
        # Liste cu care determin daca un pokemon e mort sau nu
        dead_enemy = []
        dead_pokemon = []
        for index in range(number_of_player_pokemons):
            dead_pokemon.append(False)
        for index in range(number_of_enemies):
            dead_enemy.append(False)

        while True:
            # creare enemies_surface cu frame-urile aferente
            self.pokemons_surface.blit(self.background_surface, (0, 0))
            for index, enemy in enumerate(self.enemies):
                if not dead_enemy[index]:
                    active_enemy = enemy
                    active_enemy_index = index
                    self.pokemons_surface.blit(enemy.get_frame(int(frame / 16) % 4 + 1), enemy_position)
                    break
                else:
                    active_enemy = None

            for index, player_pokemon in enumerate(self.player_pokemons):
                if not dead_pokemon[index]:
                    active_pokemon = player_pokemon
                    active_pokemon_index = index
                    self.pokemons_surface.blit(pg.transform.flip(player_pokemon.get_frame(int(frame / 16) % 4 + 1), flip_x = True, flip_y = False), player_pokemon_position)
                    break
                else:
                    active_pokemon = None

            if active_pokemon is None or active_enemy is None:
                return "MainMenu"

            if add_arrow[0]:
                self.pokemons_surface.blit(left_arrow, arrow_pos)
            elif add_arrow[1]:
                self.pokemons_surface.blit(right_arrow, arrow_pos)

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
                pokemon_rect = pg.Rect(player_pokemon_position[0],
                                       player_pokemon_position[1],
                                       active_pokemon.get_size()[0],
                                       active_pokemon.get_size()[1])
                if pokemon_rect.collidepoint(mouse_pos):
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0] == 1:
                            dead_pokemon[active_pokemon_index] = True
                            print(active_pokemon_index)
                    add_arrow[0] = True
                    arrow_pos = (player_pokemon_position[0] + active_pokemon.get_size()[0],
                                 player_pokemon_position[1] + active_pokemon.get_size()[1] / 2 - 25)
                else:
                    add_arrow[0] = False

                pokemon_rect = pg.Rect(enemy_position[0],
                                       enemy_position[1],
                                       active_enemy.get_size()[0],
                                       active_enemy.get_size()[1])
                if pokemon_rect.collidepoint(mouse_pos):
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0] == 1:
                            dead_enemy[active_enemy_index] = True
                            print(active_enemy_index)
                    add_arrow[1] = True
                    arrow_pos = (enemy_position[0] - 50,
                                 enemy_position[1] + active_enemy.get_size()[1] / 2 - 25)
                else:
                    add_arrow[1] = False

            pg.display.update()
            frame += 1
            clock.tick(60)


