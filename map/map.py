import pygame as pg
from utils.importers import import_tmx, import_frames, import_coast, import_characters
from sprites.sprites import Sprite
from sprites.player import Player
from sprites.sprites import Animated
from utils.constants import TILE_SIZE


class Map:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.maps = import_tmx("map", "assets", "maps")
        self.player = None
        self.frames = {
            'coast' : import_coast(24, 12, "map", "assets", "tilesets", "coast"),
            'water' : import_frames("map", "assets", "tilesets", "water"),
            'characters' : import_characters("sprites", "assets", "characters")
        }
    
    def render(self, group, player_start_pos):
        for obj in self.maps['world'].get_layer_by_name("Water"):
            for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE):
                    Animated(self.frames['water'], (x, y), group)

        for x, y, surface in self.maps['world'].get_layer_by_name("Terrain").tiles():
            Sprite(surface, (x * TILE_SIZE, y * TILE_SIZE), group)
        
        for x, y, surface in self.maps['world'].get_layer_by_name("Terrain Top").tiles():
            Sprite(surface, (x * TILE_SIZE, y * TILE_SIZE), group)
            
        for obj in self.maps['world'].get_layer_by_name("Coast"):
            Animated(self.frames['coast'][obj.properties['terrain']][obj.properties['side']], (obj.x, obj.y), group)

        for obj in self.maps['world'].get_layer_by_name("Objects"):
            Sprite(obj.image, (obj.x, obj.y), group)    
        
        for obj in self.maps["world"].get_layer_by_name("Entities"):
            if obj.name == "Player" and obj.properties["pos"] == player_start_pos:
                self.player = Player(self.frames['characters']['player'], (obj.x, obj.y), group)


