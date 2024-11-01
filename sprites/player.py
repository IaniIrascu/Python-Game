from pygame import sprite

class Player(sprite.Sprite):
    def __init__(self, image, position, group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_frect(topleft = position)