import pygame as pg
from utils.importers import import_tmx
from sprites.sprites import Sprite
from pytmx.util_pygame import load_pygame

TILE_SIZE = 64

class Map:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.maps = import_tmx("map", "assets", "maps")
    
    def render(self, group):
        for x, y, surface in self.maps['world'].get_layer_by_name("Terrain").tiles():
            Sprite(surface, (x * TILE_SIZE, y * TILE_SIZE), group)
