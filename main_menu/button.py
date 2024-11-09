import pygame as pg
import pygame.font
from utils.colors import *

DEFAULT_SIZE = (200, 100)
DEFAULT_BUTTON_COLOR = BLACK
DEFAULT_POSITION = (0, 0)

class Button:
    def __init__(self, display_surface = None, position = DEFAULT_POSITION, size = DEFAULT_SIZE, color = DEFAULT_BUTTON_COLOR):
        self.position = position
        self.size = size
        self.color = color
        self.display_surface = display_surface
        self.button_surface = pygame.Surface(size)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        pass

    # getters
    def get_position(self):
        return self.position

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def get_button_surface(self):
        return self.button_surface

    # setters
    def set_name(self, name):
        self.name = name

    def set_position(self, position):
        self.position = position

    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color

    def set_button_surface(self, size):
        self.button_surface = pygame.Surface(size)

    #CREATING THE BUTTONS
    def add_surface_over_button(self, surface):
        surface_rect = surface.get_rect()
        surface_rect.center = (self.button_surface.get_width() // 2, self.button_surface.get_height() // 2)
        self.button_surface.blit(surface, surface_rect)

    def create_button(self, scale_factor = 1):
        if self.display_surface is not None:
            self.display_surface.blit(pg.transform.scale_by(self.button_surface, scale_factor), self.position)
        else:
            print("No display surface for your button")

    def add_text(self, font, text, font_color):
        # Adding the text over the buttons
        text_surface = font.render(text, True, font_color, None)
        #Adding text over button
        self.add_surface_over_button(text_surface)

    def add_image(self, image_name, scale_factor = 1):
        # Adding the image over the buttons surface
        image_surface = pg.image.load(image_name).convert_alpha()
        image_surface = pg.transform.scale(image_surface, (scale_factor * self.size[0], scale_factor * self.size[1]))
        #Adding the image on the button
        self.add_surface_over_button(image_surface)





