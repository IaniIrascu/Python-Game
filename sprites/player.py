import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, frames, position, group, turned):
        super().__init__(group)
        self.wait = 0
        self.idx = 0
        self.frames = frames
        self.speed = 1000
        self.image = self.frames['down'][self.idx]
        self.rect = self.image.get_frect(center = position)
        self.behind = self.rect.centery
        self.direction = pg.math.Vector2(0, 0)
        self.turned = turned
        self.order = 3
        self.hitbox = self.rect.inflate(-self.rect.width / 2, -self.rect.height / 3)
    
    def change(self):
        self.wait += 1
        if self.wait == 5:
            self.wait = 0
            self.idx += 1
        self.idx = self.idx % len(self.frames[self.get_direction()])
        self.image = self.frames[self.get_direction()][self.idx]
    
    def get_direction(self):
        return f"{self.turned}{'' if self.direction else '_idle'}"
    

class Player(Entity):
    def __init__(self, frames, position, group, turned):
        super().__init__(frames, position, group, turned)

    
    def input(self):
        keys = pg.key.get_pressed()
        input = pg.math.Vector2(0, 0)
        if keys[pg.K_w]:
            input.y -= 1
            self.turned = 'up'
        if keys[pg.K_s]:
            input.y += 1
            self.turned = 'down'
        if keys[pg.K_a]:
            input.x -= 1
            self.turned = 'left'
        if keys[pg.K_d]:
            input.x += 1
            self.turned = 'right'
        self.direction = input
    
    def update(self, dt):
        self.input()
        self.rect.center += self.direction * self.speed * dt
        self.behind = self.rect.centery
        self.hitbox.center = self.rect.center
        self.change()

class NPC(Entity):
    def __init__(self, frames, position, group, turned):
        super().__init__(frames, position, group, turned)
    
    def update(self, dt):
        self.change()