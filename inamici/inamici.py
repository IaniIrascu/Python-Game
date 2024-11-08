import pygame as pg
import sys

ANIMATION_FRAMES = 8
FRAMESPERWIDTH = 4
FRAMESPERHEIGHT = 2

class Inamic():
    def __init__(self, position = None, size = None, health = 0, energy = 0, name = "NoName"):
        self.health = health
        self.energy = energy
        self.name = name
        self.frames = []
        self.size = (0 , 0)
        self.position = position

    # Functia creeaza frame-urile de animatie si le pune intr-o lista de frame-uri
    def animation_frames(self, image):
        image = pg.image.load(image)
        frame_width = int(image.get_width() / FRAMESPERWIDTH)
        frame_height = int(image.get_height() / FRAMESPERHEIGHT)
        self.size = (frame_width, frame_height)
        for i in range(0, int(image.get_height()), frame_height):
            for j in range(0, int(image.get_width()), frame_width):
                index = int(FRAMESPERWIDTH * (i / frame_height) + j / frame_width)
                self.frames.append(pg.Surface((frame_width, frame_height), pg.SRCALPHA))
                self.frames[index].blit(image, (0, 0), (j, i, frame_width, frame_height))

    # Animatie
    def start_animation(self, display_surface, clock):
        i = 0
        time_between_frames = 100
        last_update = 0
        while True:
            current_time = pg.time.get_ticks()
            display_surface.blit(self.frames[i % ANIMATION_FRAMES], (self.position[0], self.position[1]))
            if current_time - last_update > time_between_frames:
                last_update = current_time
                i += 1
                print(i)
            pg.display.update()
            clock.tick(60)




