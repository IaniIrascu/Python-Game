import pygame as pg
from battle_screen.battle_screen import Battle_screen
from main_menu.button import Button
from utils.colors import *

def create_text_button_surface(buttons, button_name, font):
    if button_name != "X":
        buttons[button_name].add_image("./main_menu/assets/button.jpg")
        buttons[button_name].add_text(font, button_name, BLACK)
    else:
        buttons["X"].get_button_surface().set_colorkey((0, 0, 0))
        buttons["X"].add_text(font, button_name, (1, 1, 1))

class Ability_screen():
    def __init__(self):
        self.size = (400, 700)
        self.buttons = {}
        self.button_surface = pg.Surface(self.size, pg.SRCALPHA)
        self.background_surface = pg.Surface(self.size, pg.SRCALPHA)
        self.ability_screen_surface = pg.Surface(self.size, pg.SRCALPHA)
        self.font = pg.font.Font("./main_menu/assets/minecraft.ttf", 32)

    def get_ability_screen_surface(self):
        return self.ability_screen_surface

    def get_size(self):
        return self.size

    def get_buttons(self):
        return self.buttons

    # Adding and deleting button
    def add_button(self, button_name, button):
        if button_name not in self.buttons:
            self.buttons[button_name] = button

    def delete_button(self, button_name):
        if button_name in self.buttons:
            self.buttons.pop(button_name)

    def create_ability_screen(self):
        # Setting up the background and creating the background surface
        background = pg.image.load("./pokemoni/ability_screen/assets/Untitled.png")
        background = pg.transform.scale(background, self.size)

        buttons = []
        attack_button = Button(display_surface = self.button_surface,
                              position = (60, self.button_surface.get_height() / 4),
                              size = (self.size[0] - 150, self.size[1] / 6))
        special_ability_button = Button(display_surface=self.button_surface,
                                        position=(60, 3 * self.button_surface.get_height() / 4),
                                        size = (self.size[0] - 150, self.size[1] / 6))
        x_button = Button(display_surface = self.button_surface,
                          position = (self.button_surface.get_width() - 125, 40),
                          size = (45, 45))

        buttons.append(attack_button)
        buttons.append(special_ability_button)
        buttons.append(x_button)

        # Adding buttons to dictionary
        self.add_button("Attack", attack_button)
        self.add_button("Special", special_ability_button)
        self.add_button("X", x_button)

        for button_name in self.buttons:
            # Se creeaza butonul
            create_text_button_surface(self.buttons, button_name, self.font)
            # Se copieaza butoanele pe suprafata de butoane
            self.buttons[button_name].create_button()

        self.background_surface.blit(background, (0, 0))
        self.background_surface.blit(self.button_surface, (0 ,0))
        self.ability_screen_surface.blit(self.background_surface, (0, 0))
