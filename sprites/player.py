import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, frames, position, group):
        super().__init__(group)
        self.wait = 0
        self.idx = 0
        self.frames = frames
        print(frames)
        self.speed = 1000
        # print(self.frames['down'])
        self.image = self.frames['down'][self.idx]
        self.rect = self.image.get_frect(center = position)
        self.direction = pg.math.Vector2(0, 0)
        self.turned = 'down'
    
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
    def __init__(self, frames, position, group):
        super().__init__(frames, position, group)

    
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
        self.change()
