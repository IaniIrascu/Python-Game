import pygame as pg 
from colors import *

class Button:
    def __init__(self, screen, name, color, position, size):
        self.name = name
        self.position = position
        self.size = size
        self.color = color
        self.screen = screen
        pass

    # getters
    def get_position(self):
        return self.position

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    # setters
    def set_name(self, name):
        self.name = name
        self.update_button()

    def set_position(self, position):
        self.position = position
        self.update_button()

    def set_size(self, size):
        self.size = size
        self.update_button()

    def set_color(self, color):
        self.color = color
        self.update_button()

    def update_button(self):
        pg.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.size[0], self.size[1]))
