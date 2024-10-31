import pygame as pg
from game import Game
from assets.colors import *

class Level(Game):
    def __init__(self):
        super().__init__()
        self.screen = self.get_screen()

    def run(self):
        self.screen.fill(GREEN)
        return "Running"
