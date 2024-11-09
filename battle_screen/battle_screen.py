import pygame as pg
import sys
from pokemoni.pokemon import Pokemon

class Battle_screen():
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.enemies_surface = pg.Surface(display_surface.get_size(), pg.SRCALPHA)
        self.player_pokemon_surface = pg.Surface(display_surface.get_size(), pg.SRCALPHA)
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

        i = 0
        enemies_positions = [(1500, 400), (1500, 600), (1500, 800)]
        player_pokemons_positions = [(150, 400), (150, 600), (150, 800)]

        while True:
            # creare enemies_surface cu frame-urile aferente
            self.enemies_surface.blit(self.background_surface, (0, 0))
            for index, enemy in enumerate(self.enemies):
                self.enemies_surface.blit(enemy.get_frame(int(i / 16) % 4 + 1), enemies_positions[index])

            # creare player_pokemon_surface cu frame-urile aferente
            self.player_pokemon_surface.blit(self.enemies_surface, (0, 0))
            for index, player_pokemon in enumerate(self.player_pokemons):
                self.player_pokemon_surface.blit(pg.transform.flip(player_pokemon.get_frame(int(i / 16) % 4 + 1), flip_x = True, flip_y = False), player_pokemons_positions[index])


            # Combinare suprafete si afisare
            self.display_surface.blit(self.player_pokemon_surface, (0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return "MainMenu"
            pg.display.update()
            i += 1
            clock.tick(60)


