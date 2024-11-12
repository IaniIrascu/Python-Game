import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, image, position, group):
        super().__init__(group)
        self.image = pg.surface.Surface((50, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = position)
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 300
    
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
        print(input)
        self.direction = input
    
    def update(self, dt):
        self.input()
        self.rect.topleft += self.direction * self.speed * dt
