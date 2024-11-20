import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, frames, position, group):
        super().__init__(group)
        self.idx = int(0)
        self.frames = frames
        # print(self.frames['down'])
        self.image = self.frames['down'][self.idx]
        self.rect = self.image.get_frect(center = position)

class Player(Entity):
    def __init__(self, frames, position, group):
        super().__init__(frames, position, group)
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 1000
    
    def input(self):
        keys = pg.key.get_pressed()
        input = pg.math.Vector2(0, 0)
        if keys[pg.K_w]:
            input.y -= 1
        if keys[pg.K_s]:
            input.y += 1
        if keys[pg.K_a]:
            input.x -= 1
        if keys[pg.K_d]:
            input.x += 1
        self.direction = input
    
    def update(self, dt):
        self.input()
        self.rect.center += self.direction * self.speed * dt