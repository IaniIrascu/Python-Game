import sys
from os.path import join
import pygame as pg
from utils.functions import *
import pygame.mouse
from main_menu.button import *

button_sizes = {"Start": (200, 100),
                "Load": (200, 100),
                "Quit": (200, 100),
                "Settings": (75, 75)}

scale_factor = 1.1

def create_text_button_surface(buttons, button_name, font):
    buttons[button_name].add_image(join(".", "main_menu", "assets", "button.jpg"))
    buttons[button_name].add_text(font, button_name, WHITE)

def create_settings_button_surface(buttons):
    buttons["Settings"].add_image(join(".", "main_menu", "assets", "button.jpg"))
    buttons["Settings"].add_image(join(".", "main_menu", "assets", "settings.png"), 2.5)

def create_button_surface_instant(buttons):
    for button_name in buttons:
        buttons[button_name].create_button()

def reset_buttons_original(buttons, button_name, font):
    size = buttons[button_name].get_size()
    position = buttons[button_name].get_position()
    if size[0] != button_sizes[button_name][0] and size[1] != button_sizes[button_name][1]:
        buttons[button_name].set_position((position[0] + (size[0] / scale_factor) * (scale_factor - 1) / 2,
                                                position[1] + (size[1] / scale_factor) * (scale_factor - 1) / 2))
        buttons[button_name].set_size((size[0] / scale_factor, size[1] / scale_factor))
        buttons[button_name].set_button_surface((size[0] / scale_factor, size[1] / scale_factor))
        if button_name == "Settings":
            create_settings_button_surface(buttons)
        else:
            create_text_button_surface(buttons, button_name, font)

class MainMenu:
    def __init__(self, display_surface = None):
        self.display_surface = display_surface
        self.button_surface = pg.Surface((display_surface.get_width(), display_surface.get_height()), pg.SRCALPHA)  # Transparent surface
        self.background_surface = pg.Surface((display_surface.get_width(), display_surface.get_height()))
        self.buttons = {}
        self.font = pygame.font.Font(join(".", "main_menu", "assets", "minecraft.ttf"), 32)

    # Modifying menu background
    def set_menu_background(self, background):
        self.background_surface.blit(background, (0, 0))

    def fill_color(self, color):
        self.display_surface.fill(color)

    # Adding and deleting buttons
    def add_button(self, button_name, button):
        if button_name not in self.buttons:
            self.buttons[button_name] = button

    def delete_button(self, button_name):
        if button_name in self.buttons:
            self.buttons.pop(button_name)

    def run(self, clock):

        # Setting up the background and creating the background surface
        background = pg.image.load(join(".", "main_menu", "assets", "pokemon_background.jpg"))
        background = pg.transform.scale(background, (self.display_surface.get_width(), self.display_surface.get_height()))
        self.background_surface.blit(background, (0, 0))

        # Creating the buttons if menu was run for the first time
        if not self.buttons:
            start_button = Button(display_surface = self.button_surface,
                                  position = (self.button_surface.get_width() - 400, self.button_surface.get_height() / 3 + 150),
                                  size = button_sizes["Start"],
                                  color = RED)
            load_button = Button(display_surface = self.button_surface,
                                 position = (self.button_surface.get_width() - 400, self.button_surface.get_height() / 2 + 150),
                                 size = button_sizes["Load"],
                                 color = GREEN)
            quit_button = Button(display_surface = self.button_surface,
                                 position = (self.button_surface.get_width() - 400, 2 * self.button_surface.get_height() / 3 + 150),
                                 size = button_sizes["Quit"],
                                 color = BLUE)
            settings_button = Button(display_surface = self.button_surface,
                                     position = (10, 10),
                                     size = button_sizes["Settings"],
                                     color = WHITE)
            # Adding buttons to dictionary
            self.add_button("Start", start_button)
            self.add_button("Load", load_button)
            self.add_button("Quit", quit_button)
            self.add_button("Settings", settings_button)

        start_button = self.buttons["Start"]
        quit_button = self.buttons["Quit"]
        load_button = self.buttons["Load"]
        settings_button = self.buttons["Settings"]

        # Resetting the buttons to their original state
        for button_name in self.buttons:
            reset_buttons_original(self.buttons, button_name, self.font)

        # Animation for buttons
        pop_sfx = pg.mixer.Sound(join(".", "main_menu", "assets", "pop_sfx.mp3"))
        self.display_surface.blit(self.background_surface, (0, 0))

        for button_name in self.buttons:
            # Creating buttons surfaces
            if button_name == "Settings":
                create_settings_button_surface(self.buttons)
            else:
                create_text_button_surface(self.buttons, button_name, self.font)

            # Adding the button to the all button surface
            self.buttons[button_name].create_button()
            self.display_surface.blit(self.button_surface, (0 ,0))
            # Play sound and wait half a second

        pg.display.update()

        while True:
            # Updating the screen with the changes made during the last frame
            # Adding the background surface, creating and adding the button surface
            self.button_surface.blit(self.background_surface, (0, 0))
            create_button_surface_instant(self.buttons)
            self.display_surface.blit(self.button_surface.convert_alpha(), (0, 0))

            # Looking for events
            for event in pg.event.get():
                close_game(event)
                # get mouse position
                mouse_pos = pg.mouse.get_pos()

                # Modificare butoane cand cursorul se afla pe ele
                for button_name in self.buttons:
                    if self.buttons[button_name].rect.collidepoint(mouse_pos):
                        size = self.buttons[button_name].get_size()
                        position = self.buttons[button_name].get_position()
                        # if size == normal size
                        if size[0] == button_sizes[button_name][0] and size[1] == button_sizes[button_name][1]:
                            self.buttons[button_name].set_position((position[0] - size[0] * (scale_factor - 1) / 2,
                                                                position[1] - size[1] * (scale_factor - 1) / 2))
                            self.buttons[button_name].set_size((size[0] * scale_factor, size[1] * scale_factor))
                            self.buttons[button_name].set_button_surface((size[0] * scale_factor, size[1] * scale_factor))
                            if button_name == "Settings":
                                create_settings_button_surface(self.buttons)
                            else:
                                create_text_button_surface(self.buttons, button_name, self.font)

                    else:
                        reset_buttons_original(self.buttons, button_name, self.font)

                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed()[0]:
                        # check the collision with the buttons
                        if start_button.rect.collidepoint(mouse_pos):
                            return "Start"
                        if load_button.rect.collidepoint(mouse_pos):
                            return "Load"
                        if quit_button.rect.collidepoint(mouse_pos):
                            pg.quit()
                            sys.exit()
            pg.display.update()
            clock.tick(60)
