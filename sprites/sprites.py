import pygame as pg
from utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH

class Sprite(pg.sprite.Sprite):
    def __init__(self, surface, position, group, order):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_frect(topleft = position)
        self.order = order
        self.behind = self.rect.centery
        self.hitbox = self.rect.inflate(0, -self.rect.height / 3)

class Collision(Sprite):
    def __init__(self, surface, position, group):
        super().__init__(surface, position, group, -1)
        self.hitbox = self.rect.copy()

class Animated(Sprite):
    def __init__(self, frames, position, group, order):
        self.frames = frames
        self.idx = 0
        self.wait = 0
        super().__init__(frames[self.idx], position, group, order)
        
    def change(self):
        self.wait += 1
        if self.wait == 8:
            self.wait = 0
            self.idx += 1
            self.idx = self.idx % 4
        self.image = self.frames[self.idx]
    def update(self, dt):
        self.change()

class Grass(Sprite):
    def __init__(self, surface, position, group, order):
        super().__init__(surface, position, group, order)
        self.behind = self.rect.centery - 30

class Transition(Sprite):
    def __init__(self, size, position, group, target, target_pos):
        self.target = target
        self.target_pos = target_pos
        surface = pg.Surface(size, pg.SRCALPHA, 32).convert_alpha()
        super().__init__(surface, position, group, -1)
            
class Group(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2(0, 0)

    def draw(self, player_pos):
        self.offset.x = self.display_surface.get_width() / 2 - player_pos[0]
        self.offset.y = self.display_surface.get_height() / 2 - player_pos[1]
        
        bg = [sprite for sprite in self if sprite.order < 3]
        main = sorted([sprite for sprite in self if sprite.order == 3], key = lambda sprite: sprite.behind)
        fg = [sprite for sprite in self if sprite.order > 3]
        for order in [bg, main, fg]:
            for sprite in order:
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)
        
