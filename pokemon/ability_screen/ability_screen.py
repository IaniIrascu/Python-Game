import pygame as pg
from main_menu.button import Button
from utils.colors import *

def create_text_button_surface(buttons, button_name, font):
    if button_name != "X" and button_name != "Name":
        buttons[button_name].add_image("./main_menu/assets/button.jpg")
        buttons[button_name].add_text(font, buttons[button_name].get_name(), BLACK)
    else:
        buttons[button_name].set_color((217,160,102))
        buttons[button_name].add_color()
        buttons[button_name].get_button_surface().set_colorkey((0, 0, 0))
        buttons[button_name].add_text(font, buttons[button_name].get_name(), (1, 1, 1))

class AbilityScreen:
    def __init__(self):
        self.size = (400, 700)
        self.buttons = {}
        self.button_surface = pg.Surface(self.size, pg.SRCALPHA)
        self.background_surface = pg.Surface(self.size, pg.SRCALPHA)
        self.ability_screen_surface = pg.Surface(self.size, pg.SRCALPHA)
        self.font = pg.font.Font("./main_menu/assets/minecraft.ttf", 24)

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
        # # Setting up the background and creating the background surface
        background = pg.image.load("./pokemon/ability_screen/assets/Untitled.png")
        background = pg.transform.scale(background, self.size)
        buttons = []
        attack_button = Button(display_surface = self.button_surface,
                              position = (60, 150),
                              size = (self.size[0] - 150, self.size[1] / 7))
        special_ability_button = Button(display_surface=self.button_surface,
                                        position=(60, 275),
                                        size = (self.size[0] - 150, self.size[1] / 7))
        switch_pokemon_button = Button(display_surface=self.button_surface,
                                       position=(60, 400),
                                       size = (self.size[0] - 150, self.size[1] / 7))
        x_button = Button(display_surface = self.button_surface,
                          position = (self.button_surface.get_width() - 125, 40),
                          size = (45, 45))
        name_button = Button(display_surface=self.button_surface,
                             position = (40, 80),
                             size = (self.button_surface.get_width() - 100, self.size[1] / 10))
        skip_button = Button(display_surface=self.button_surface,
                             position = (60, 525),
                             size = (self.button_surface.get_width() - 150, self.size[1] / 7))

        buttons.append(attack_button)
        buttons.append(special_ability_button)
        buttons.append(x_button)
        buttons.append(name_button)
        buttons.append(switch_pokemon_button)
        buttons.append(skip_button)

        # Adding buttons to dictionary
        self.add_button("Attack", attack_button)
        self.add_button("Special", special_ability_button)
        self.add_button("X", x_button)
        self.add_button("Name", name_button)
        self.add_button("Switch", switch_pokemon_button)
        self.add_button("Skip Turn", skip_button)

        for button_name in self.buttons:
            # Se creeaza butonul
            create_text_button_surface(self.buttons, button_name, self.font)
            # Se copieaza butoanele pe suprafata de butoane
            self.buttons[button_name].create_button()

        self.background_surface.blit(background, (0, 0))
        self.background_surface.blit(self.button_surface, (0, 0))
        self.ability_screen_surface.blit(self.background_surface, (0, 0))

    def update_ability_screen(self, pokemon):
        background = pg.image.load("./pokemon/ability_screen/assets/Untitled.png")
        background = pg.transform.scale(background, self.size)

        self.buttons["Attack"].set_name(pokemon.get_attack().get_name() + "(" + str(round(pokemon.get_damage(), 2)) + ")")
        self.buttons["Special"].set_name(pokemon.get_special_attack().get_name() + "(" + str(pokemon.get_special_attack().get_energy_cost()) + ")")
        self.buttons["Name"].set_name(pokemon.get_name().replace(".png", "") + " lv. " + str(pokemon.get_level()))
        self.buttons["X"].set_name("X")
        self.buttons["Switch"].set_name("Switch")
        self.buttons["Skip Turn"].set_name("Skip Turn")

        for button_name in self.buttons:
            # Se creeaza butonul
            create_text_button_surface(self.buttons, button_name, self.font)
            if button_name == "Special":
                numberofefects = len(pokemon.get_special_attack().get_effects())
                for i, effect in enumerate(pokemon.get_special_attack().get_effects()):
                    button_surface = self.buttons["Special"].get_button_surface()
                    button_surface.blit(effect.get_effectIcon(),
                                        (button_surface.get_width() / 2 - numberofefects * 10 + i * 20, 60), (0, 0, 15, 15))
            # Se copieaza butoanele pe suprafata de butoane
            self.buttons[button_name].create_button()

        self.background_surface.blit(background, (0, 0))
        self.background_surface.blit(self.button_surface, (0 ,0))
        self.ability_screen_surface.blit(self.background_surface, (0, 0))