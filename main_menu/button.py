import pygame as pg 
from utils.colors import *

class Button:
    def __init__(self, display_surface, name, color, position, size):
        self.name = name
        self.position = position
        self.size = size
        self.color = color
        self.display_surface = display_surface
        pass

    def update_button(self):
        pg.draw.rect(self.display_surface, self.color, (self.position[0], self.position[1], self.size[0], self.size[1]))
