import pygame as pg
import random
import main_menu.button
from utils.colors import *

pg.font.init()

SIZE = (50, 50)
FONT = pg.font.Font("./main_menu/assets/minecraft.ttf", 32)

class Effect:
    def __init__(self):
        self.effectIcon = pg.Surface(SIZE)
        self.name = None
        self.number_of_turns_left = None
        self.color = None
        self.justApplied = None

    def change_effectIcon(self, image = None, color = None, number = None):
        text_surface = FONT.render(str(number), True, WHITE, None)
        self.color = color
        self.effectIcon.fill(color)
        if image is not None:
            image = pg.transform.scale(image, SIZE)
            self.effectIcon.blit(image, (0, 0))
        self.effectIcon.blit(text_surface, (17, 15))

    def get_justApplied(self):
        return self.justApplied

    def get_number_of_turns_left(self):
        return self.number_of_turns_left

    def get_effectIcon(self):
        return self.effectIcon

    def get_color(self):
        return self.color

    def set_justApplied(self, justApplied):
        self.justApplied = justApplied

    def set_name(self, name):
        self.name = name

    def set_number_of_turns_left(self, number_of_turns_left):
        self.number_of_turns_left = number_of_turns_left

    def get_name(self):
        return self.name

    def set_color(self, color):
        self.color = color
