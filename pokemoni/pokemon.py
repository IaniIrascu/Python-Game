import pygame as pg
import sys

ANIMATION_FRAMES = 8
FRAMESPERWIDTH = 4
FRAMESPERHEIGHT = 2

class Pokemon():
    def __init__(self, health = 0, energy = 0, name = "NoName"):
        self.health = health
        self.energy = energy
        self.name = name
        self.animations = [] # This is a list of lists of frames
        self.frames = [] # This one contains all the frames
        self.size = None

    def get_frame(self, frame_no):
        if 1 <= frame_no <= len(self.frames) + 1:
            return self.frames[frame_no - 1]
        print("Frame not in list")

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    # Functia creeaza frame-urile de animatie si le pune intr-o lista de frame-uri
    def animation_frames(self, image, scale = 1):
        image = pg.image.load(image)
        frame_width = int(image.get_width() / FRAMESPERWIDTH)
        frame_height = int(image.get_height() / FRAMESPERHEIGHT)
        self.size = (frame_width * scale, frame_height * scale)
        for i in range(0, int(image.get_height()), frame_height):
            for j in range(0, int(image.get_width()), frame_width):
                index = int(FRAMESPERWIDTH * (i / frame_height) + j / frame_width)
                self.frames.append(pg.Surface((frame_width, frame_height), pg.SRCALPHA))
                self.frames[index].blit(image, (0, 0), (j, i, frame_width, frame_height))
                self.frames[index] = pg.transform.scale(self.frames[index], (frame_width * scale, frame_height * scale))
