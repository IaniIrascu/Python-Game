import pygame as pg
from utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH

class Sprite(pg.sprite.Sprite):
    def __init__(self, surface, position, group):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_frect(topleft = position)

class Animated(Sprite):
    def __init__(self, frames, position, group):
        self.frames = frames
        self.idx = 0
        self.wait = 0
        super().__init__(frames[self.idx], position, group)
        
    def change(self):
        self.wait += 1
        if self.wait == 8:
            self.wait = 0
            self.idx += 1
            self.idx = self.idx % 4
        self.image = self.frames[self.idx]
    def update(self, dt):
        self.change()
    

class Group(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2(0, 0)


    def draw(self, player_pos):
        self.offset.x = self.display_surface.get_width() / 2 - player_pos[0]
        self.offset.y = self.display_surface.get_height() / 2 - player_pos[1]
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)
