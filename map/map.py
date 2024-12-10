import pygame as pg
from utils.importers import import_tmx, import_frames, import_coast, import_characters
from sprites.sprites import Sprite, Animated, Grass, Collision, Transition
from sprites.characters import Player, NPC
from utils.constants import TILE_SIZE
from sprites.assets.npc_data import NPC_DATA

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
        self.change = ""
        self.count = 0
        self.map_name = ""
        self.first_pos = {
            'world': 'house',
            'fire': 'entrance',
            'arena': 'entrance',
            'hospital': 'world',
            'hospital2': 'world',
            'house': 'world',
            'plant': 'entrance',
            'water': 'entrance'
        }
    
    def render(self, group, collisions, transitions, npcs, player_start_pos, map_name):
        self.map_name = map_name
        for sprites in (group, collisions, transitions, npcs):
            sprites.empty()

        for obj in self.maps[map_name].get_layer_by_name("Water"):
            for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE):
                    Animated(self.frames['water'], (x, y), group, 0)
        
        for x, y, surface in self.maps[map_name].get_layer_by_name("Terrain").tiles():
            Sprite(surface, (x * TILE_SIZE, y * TILE_SIZE), group, 1)
        
        for x, y, surface in self.maps[map_name].get_layer_by_name("Terrain Top").tiles():
            Sprite(surface, (x * TILE_SIZE, y * TILE_SIZE), group, 1)
        
        for obj in self.maps[map_name].get_layer_by_name("Coast"):
            Animated(self.frames['coast'][obj.properties['terrain']][obj.properties['side']], (obj.x, obj.y), group, 1)

        for obj in self.maps[map_name].get_layer_by_name("Monsters"):
            Grass(obj.image, (obj.x, obj.y), group, 1 if obj.properties['biome'] == "sand" else 3)

        for obj in self.maps[map_name].get_layer_by_name("Objects"):
            if obj.name == "top":
                Sprite(obj.image, (obj.x, obj.y), group, 4)
            else:
                Sprite(obj.image, (obj.x, obj.y), (group, collisions) , 3)    
        
        for obj in self.maps[map_name].get_layer_by_name("Transition"):
            Transition((obj.width, obj.height), (obj.x, obj.y), (group, transitions), obj.properties['target'], obj.properties['pos'])

        for obj in self.maps[map_name].get_layer_by_name("Collisions"):
            Collision(pg.Surface((obj.width, obj.height)), (obj.x, obj.y), collisions)

        for obj in self.maps[map_name].get_layer_by_name("Entities"):
            if obj.name == "Player" and obj.properties["pos"] == player_start_pos:
                if self.player == None:
                    self.player = Player(self.frames['characters']['player'], (obj.x, obj.y), group,
                                         obj.properties['direction'], collisions)
                else:
                    self.player = Player(self.frames['characters']['player'], (obj.x, obj.y), group,
                                         obj.properties['direction'], collisions, self.player.inventory)
            elif obj.name != "Player":
                NPC(self.frames['characters'][obj.properties['graphic']], (obj.x, obj.y), (group, collisions, npcs), obj.properties['direction'], NPC_DATA[obj.properties['character_id']])

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.change = "MainMenu"

    def grass_count(self):
        if self.count > 300:
            self.count = 0
        x = self.player.rect.centerx
        y = self.player.rect.centery
        for obj in self.maps[self.map_name].get_layer_by_name("Monsters"):
            if obj.x < x < obj.x + TILE_SIZE and obj.y < y < obj.y + TILE_SIZE:
                self.count += 1
        return self.count

        

