import pygame as pg
import random

class Effect:
    def __init__(self):
        self.effectIcon = pg.Surface((50, 50))
        self.name = None
        self.number_of_turns = None
        self.number_of_turns_left = None
        self.color = None

    def change_effectIcon(self, image = None, color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))):
        self.effectIcon.fill(color)
        if image is not None:
            image = pg.transform.scale(image, (50, 50))
            self.effectIcon.blit(image, (0, 0))

    def get_number_of_turns(self):
        return self.number_of_turns

    def get_number_of_turns_left(self):
        return self.number_of_turns_left

    def get_effectIcon(self):
        return self.effectIcon

    def get_color(self):
        return self.color

    def set_name(self, name):
        self.name = name

    def set_number_of_turns(self, number_of_turns):
        self.number_of_turns = number_of_turns

    def set_number_of_turns_left(self, number_of_turns_left):
        self.number_of_turns_left = number_of_turns_left

    def get_name(self):
        return self.name

    def set_color(self, color):
        self.color = color
