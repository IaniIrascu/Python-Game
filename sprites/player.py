from pygame import sprite

class Player(sprite.Sprite):
    def __init__(self, surface, position, group):
        super().__init__(group)
        self.surface = surface
        self.rect = self.surface.get_frect(topleft = position)