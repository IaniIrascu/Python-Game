import pygame as pg
from utils.importers import import_tmx
from sprites.sprites import Sprite

TILE_SIZE = 64

class Map:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.maps = import_tmx("..", "maps", "assets")
    
    def render(self, position):
        for x, y, image in self.maps.get_layer_by_name("Terrain").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)