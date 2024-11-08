import pygame as pg
import sys

class battle_screen(self):
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.enemies_surface = pg.Surface(display_surface.get_size())
        self.enemies = []

    def load_enemies(self, enemies):
        self.enemies = enemies

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.quit()


