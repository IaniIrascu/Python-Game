import pygame as pg
from utils.importers import import_tmx
from sprites.sprites import Sprite
from sprites.player import Player
from utils.constants import TILE_SIZE


class Map:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.maps = import_tmx("map", "assets", "maps")
        self.player = None
    
    def render(self, group, player_start_pos):
        for x, y, surface in self.maps['world'].get_layer_by_name("Terrain").tiles():
            Sprite(surface, (x * TILE_SIZE, y * TILE_SIZE), group)
        
        for obj in self.maps["world"].get_layer_by_name("Entities"):
            if obj.name == "Player" and obj.properties["pos"] == 'fire':
                print(obj.x, obj.y)
                self.player = Player(self.display_surface, (obj.x, obj.y), group)
