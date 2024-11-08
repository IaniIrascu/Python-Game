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

class MainMenu:
    def __init__(self, display_surface = None, clock = None):
        self.display_surface = display_surface
        self.button_surface = pg.Surface((display_surface.get_width(), display_surface.get_height()), pg.SRCALPHA)  # Transparent surface
        self.background_surface = pg.Surface((display_surface.get_width(), display_surface.get_height()))
        self.buttons = {}
        self.clock = clock
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

    def run(self):

        # Setting up the background
        background = pg.image.load(join(".", "main_menu", "assets", "pokemon_background.jpg"))
        background = pg.transform.scale(background, (self.display_surface.get_width(), self.display_surface.get_height()))
        self.background_surface.blit(background, (0, 0))

        # creating the buttons if menu was run for the first time
        if not self.buttons:
            start_button = Button(display_surface = self.button_surface,
                                  position = (self.button_surface.get_width() / 2 - 100, self.button_surface.get_height() / 3),
                                  size = button_sizes["Start"],
                                  color = RED)
            load_button = Button(display_surface = self.button_surface,
                                 position = (self.button_surface.get_width() / 2 - 100, self.button_surface.get_height() / 2),
                                 size = button_sizes["Load"],
                                 color = GREEN)
            quit_button = Button(display_surface = self.button_surface,
                                 position = (self.button_surface.get_width() / 2 - 100, 2 * self.button_surface.get_height() / 3),
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

        # Animation for buttons
        pop_sfx = pg.mixer.Sound(join(".", "main_menu", "assets", "pop_sfx.mp3"))
        self.display_surface.blit(self.background_surface, (0, 0))
        for button_name in self.buttons:
            pg.display.update()
            if button_name == "Settings":
                self.buttons[button_name].add_image(join(".", "main_menu", "assets", "button.jpg"), 1)
                self.buttons[button_name].add_image(join(".", "main_menu", "assets", "settings.png"), 2.5)
            else:
                self.buttons[button_name].add_image(join(".", "main_menu", "assets", "button.jpg"), 1)
                self.buttons[button_name].add_text(self.font, button_name, WHITE)
            self.display_surface.blit(self.button_surface, (0 ,0))
            pop_sfx.play()
            pg.time.wait(500)

        while True:
            self.display_surface.blit(self.background_surface, (0, 0))
            # # displaying the buttons
            # for button_name in self.buttons:
            #     if button_name == "Settings":
            #         self.buttons[button_name].add_image('./assets/button.jpg', 1)
            #         self.buttons[button_name].add_image('./assets/settings.png', 2.5)
            #     else:
            #         self.buttons[button_name].add_image('./assets/button.jpg', 1)
            #         self.buttons[button_name].add_text(self.font, button_name, WHITE)
            self.display_surface.blit(self.button_surface.convert_alpha(), (0, 0))
            for event in pg.event.get():
                close_game(event)
                # get mouse position
                mouse_pos = pg.mouse.get_pos()
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
            self.clock.tick(60)
