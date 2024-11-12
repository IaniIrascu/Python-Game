import pygame as pg
from utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH

class Sprite(pg.sprite.Sprite):
    def __init__(self, surface, position, group):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_rect(topleft = position)

class Group(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2(20, 20)


    def draw(self, player_pos):
        self.offset.x = WINDOW_WIDTH / 2 - player_pos[0]
        self.offset.y = WINDOW_HEIGHT / 2 - player_pos[1]
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)
