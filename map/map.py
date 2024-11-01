import pygame as pg
from utils.importers import import_tmx

class Map:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.maps = import_tmx("..", "maps", "assets")