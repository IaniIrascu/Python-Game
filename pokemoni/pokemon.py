import pygame as pg
import sys
from pokemoni.ability_screen.ability_screen import Ability_screen

ANIMATION_FRAMES = 8
FRAMESPERWIDTH = 4
FRAMESPERHEIGHT = 2

class Pokemon():
    def __init__(self, name = "NoName"):
        self.health = None
        self.energy = None
        self.name = name
        # self.animations = [] # This is a list of lists of frames
        self.frames = [] # This one contains all the frames
        self.size = None
        self.ability_screen = None

    # Getters
    def get_frame(self, frame_no):
        if 1 <= frame_no <= len(self.frames) + 1:
            return self.frames[frame_no - 1]
        print("Frame not in list")

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def get_ability_screen(self):
        return self.ability_screen

    # Setters
    def set_name(self, name):
        self.name = name

    def set_ability_screen(self, ability_screen):
        self.ability_screen = ability_screen

    def set_size(self, size):
        self.size = size

    def set_health(self, health):
        self.health = health

    def set_energy(self, energy):
        self.energy = energy

    # Functia creeaza frame-urile de animatie cu atributele din obiect si le pune intr-o lista de frame-uri
    # Frame-urile 1-4 idle, frame-urile 5-8 atac
    def animation_frames(self, image):
        image = pg.image.load(image)
        frame_width = int(image.get_width() / FRAMESPERWIDTH)
        frame_height = int(image.get_height() / FRAMESPERHEIGHT)
        for i in range(0, int(image.get_height()), frame_height):
            for j in range(0, int(image.get_width()), frame_width):
                index = int(FRAMESPERWIDTH * (i / frame_height) + j / frame_width)

                # Creare suprafata pentru frame-ul meu
                self.frames.append(pg.Surface((frame_width, frame_height), pg.SRCALPHA))
                self.frames[index].blit(image, (0, 0), (j, i, frame_width, frame_height))

                # Se scaleaza la dimensiunea dorita
                self.frames[index] = pg.transform.scale(self.frames[index], self.size)
