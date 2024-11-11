import pygame as pg
import random

class Effect:
    def __init__(self):
        self.effectIcon = pg.Surface((50, 50))
        self.name = None

    def change_effectIcon(self, image = None):
        self.effectIcon.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        if image is not None:
            image = pg.transform.scale(image, (50, 50))
            self.effectIcon.blit(image, (0, 0))

    def get_effectIcon(self):
        return self.effectIcon

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name