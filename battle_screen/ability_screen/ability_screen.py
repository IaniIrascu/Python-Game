import pygame as pg
from battle_screen.battle_screen import Battle_screen
from main_menu.button import Button
from utils.colors import *

def create_text_button_surface(buttons, button_name, font):
    buttons[button_name].add_color()
    buttons[button_name].add_text(font, button_name, BLACK)

class Ability_screen():
    def __init__(self):
        self.size = (300, 600)
        self.buttons = {}
        self.button_surface = pg.Surface(self.size)
        self.background_surface = pg.Surface(self.size)
        self.font = pg.font.Font("./main_menu/assets/minecraft.ttf", 32)

    # Adding and deleting button
    def add_button(self, button_name, button):
        if button_name not in self.buttons:
            self.buttons[button_name] = button

    def delete_button(self, button_name):
        if button_name in self.buttons:
            self.buttons.pop(button_name)

    def create_ability_screen(self):
        # Setting up the background and creating the background surface
        background = pg.image.load("./battle_screen/ability_screen/assets/ability_screen_ackground.png")
        background = pg.transform.scale(background, self.size)
        self.background_surface.blit(background, (0, 0))

        buttons = []
        attack_button = Button(display_surface = self.button_surface,
                              position = (self.button_surface.get_width() - 25, self.button_surface.get_height() / 3),
                              size = (self.size[0] - 50, self.size[1] / 4))
        special_ability_button = Button(display_surface=self.button_surface,
                                        position=(self.button_surface.get_width() - 25, self.button_surface.get_height() / 2),
                                        size = (self.size[0] - 50, self.size[1] / 4))
        x_button = Button(display_surface = self.button_surface,
                          position = (self.button_surface.get_width() - 25, 2 * self.button_surface.get_height() / 3),
                          size = (self.size[0] - 50, self.size[1] / 4))

        buttons.append(attack_button)
        buttons.append(special_ability_button)
        buttons.append(x_button)

        # Adding buttons to dictionary
        self.add_button("Attack", attack_button)
        self.add_button("Special", special_ability_button)
        self.add_button("XButton", x_button)

        for button_name in self.buttons:
            create_text_button_surface(self.buttons, button_name, self.font)
            # Adding the button to the all button surface
            self.buttons[button_name].create_button()

        self.background_surface.blit(self.button_surface, (0 ,0))