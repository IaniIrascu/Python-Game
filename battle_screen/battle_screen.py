import pygame as pg
import sys
from inamici.inamici import Inamic
from inamici.inamici import *

class Battle_screen():
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.enemies_surface = pg.Surface(display_surface.get_size(), pg.SRCALPHA)
        self.background_surface = pg.Surface(display_surface.get_size(), pg.SRCALPHA)
        self.enemies = []

    def load_enemies(self, enemies):
        self.enemies = enemies

    def run(self, clock):
        # Creare suprafata background
        background = pg.image.load('./battle_screen/assets/forest.png')
        background = pg.transform.scale(background, (self.display_surface.get_width(), self.display_surface.get_height()))
        self.background_surface.blit(background, (0, 0))
        i = 0
        positions_on_screen = [(1500, 400), (1500, 600), (1500, 800)]
        while True:
            # creare enemies_surface cu frame-urile aferente
            self.enemies_surface.blit(self.background_surface, (0, 0))
            for index, enemy in enumerate(self.enemies):
                self.enemies_surface.blit(enemy.get_frame(int(i / 16) % 4 + 1), positions_on_screen[index])

            # Combinare suprafete si afisare
            self.display_surface.blit(self.enemies_surface, (0, 0))

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


