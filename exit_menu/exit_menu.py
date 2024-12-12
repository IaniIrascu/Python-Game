from operator import truediv
from os.path import join

from openpyxl.chart.trendline import Trendline
from sympy.codegen.ast import continue_
from sympy.codegen.cnodes import sizeof, static
from main_menu import *
from main_menu.main_menu import *
import pygame as pg

button_sizes = {"Continue": (200, 100),
                "Save": (200, 100),
                "Menu": (200,100),
                "Exit": (200, 100),
                "Map": (200, 100)}

def create_text_button_surface(buttons, button_name, font):
    buttons[button_name].add_image(join(".", "exit_menu", "assets", "button.jpg"))
    buttons[button_name].add_text(font, button_name, WHITE)

def create_button_surface_instant(buttons):
    for button_name in buttons:
        buttons[button_name].create_button()

class Exit:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.button_surface = pg.Surface((display_surface.get_width(), display_surface.get_height()),
                                         pg.SRCALPHA)
        self.background_surface = pg.Surface((display_surface.get_width(), display_surface.get_height()))
        self.buttons = {}
        self.font = pg.font.Font(join(".", "exit_menu", "assets", "minecraft.ttf"), 32)

    def set_menu_background(self, background):
        self.background_surface.blit(background, (0, 0))

    def fill_color(self, color):
        self.display_surface.fill(color)

    def add_button(self, button_name, button):
        if button_name not in self.buttons:
            self.buttons[button_name] = button

    def delete_button(self, button_name):
        if button_name in self.buttons:
            self.buttons.pop(button_name)

    def run1(self, clock):
        background = pg.image.load(join(".", "exit_menu", "assets", "exit_bg.png"))
        background = pg.transform.scale(background,
                                        (self.display_surface.get_width(), self.display_surface.get_height()))
        self.background_surface.blit(background, (0, 0))
        self.buttons = {}
        continue_button = Button(display_surface=self.button_surface,
                              position=(self.button_surface.get_width()/2 - 100, (self.button_surface.get_height() / 3 + 150)/2 + 10),
                              size=button_sizes["Continue"],
                              color=WHITE)
        save_button = Button(display_surface=self.button_surface,
                             position=(self.button_surface.get_width()/2 - 100, (self.button_surface.get_height() / 2 + 150)/2 + 70),
                             size = button_sizes["Save"],
                             color=WHITE)
        exit_menu_button = Button(display_surface=self.button_surface,
                             position=(self.button_surface.get_width() / 2 - 100, (self.button_surface.get_height() / 2 + 150) / 2 + 220),
                             size=button_sizes["Menu"],
                             color=WHITE)
        exit_button = Button(display_surface=self.button_surface,
                             position=(self.button_surface.get_width()/2 - 100, (2 * self.button_surface.get_height() / 3 + 150)/2 + 280),
                             size = button_sizes["Exit"],
                             color=WHITE)
        #### aici ar trebui sa fie un buton pentru turn on and off volumul dar cand se face

        self.add_button("Continue", continue_button)
        self.add_button("Save", save_button)
        self.add_button("Exit", exit_button)
        self.add_button("Menu", exit_menu_button)

        continue_button = self.buttons["Continue"]
        save_button = self.buttons["Save"]
        exit_button = self.buttons["Exit"]
        exit_menu_button = self.buttons["Menu"]

        for button_name in self.buttons:
            create_text_button_surface(self.buttons, button_name, self.font)
            self.buttons[button_name].create_button()

        pg.display.update()
        wannaeExit = False
        while True:
            if not wannaeExit:
                self.button_surface.blit(self.background_surface, (0, 0))
                create_button_surface_instant(self.buttons)
                self.display_surface.blit(self.button_surface.convert_alpha(), (0, 0))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        wannaeExit = True
                        pg.quit()
                        sys.exit()
                    # get mouse position
                    mouse_pos = pg.mouse.get_pos()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0]:
                            # check the collision with the buttons
                            if continue_button.rect.collidepoint(mouse_pos):
                                return "Continue"
                            if save_button.rect.collidepoint(mouse_pos):
                                return "Save"
                            if exit_menu_button.rect.collidepoint(mouse_pos):
                                return "Menu"
                            if exit_button.rect.collidepoint(mouse_pos):
                                wannaeExit = True
                                return "Exit"
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            return "Continue"

            else:
                self.button_surface.blit(self.background_surface, (0, 0))
                create_button_surface_instant(self.buttons)
                self.display_surface.blit(self.button_surface.convert_alpha(), (0, 0))
            pg.display.update()
            clock.tick(60)

    def run2(self, clock):
        background = pg.image.load(join(".", "exit_menu", "assets", "exit_bg.png"))
        background = pg.transform.scale(background,
                                        (self.display_surface.get_width(), self.display_surface.get_height()))
        self.background_surface.blit(background, (0, 0))
        self.buttons = {}
        continue_button = Button(display_surface=self.button_surface,
                              position=(self.button_surface.get_width()/2 - 100, (self.button_surface.get_height() / 3 + 150)/2 + 10),
                              size=button_sizes["Continue"],
                              color=WHITE)
        exit_map_button = Button(display_surface=self.button_surface,
                             position=(self.button_surface.get_width() / 2 - 100, (self.button_surface.get_height() / 2 + 150) / 2 + 220),
                             size=button_sizes["Map"],
                             color=WHITE)
        #### aici ar trebui sa fie un buton pentru turn on and off volumul dar cand se face

        self.add_button("Continue", continue_button)
        self.add_button("Map", exit_map_button)

        continue_button = self.buttons["Continue"]
        exit_map_button = self.buttons["Map"]

        for button_name in self.buttons:
            create_text_button_surface(self.buttons, button_name, self.font)
            self.buttons[button_name].create_button()

        pg.display.update()
        wannaeExit = False
        while True:
            if not wannaeExit:
                self.button_surface.blit(self.background_surface, (0, 0))
                create_button_surface_instant(self.buttons)
                self.display_surface.blit(self.button_surface.convert_alpha(), (0, 0))
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        wannaeExit = True
                        pg.quit()
                        sys.exit()
                    # get mouse position
                    mouse_pos = pg.mouse.get_pos()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0]:
                            # check the collision with the buttons
                            if continue_button.rect.collidepoint(mouse_pos):
                                return "Continue"
                            if exit_map_button.rect.collidepoint(mouse_pos):
                                return "Map"
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            return "Continue"
            else:
                self.button_surface.blit(self.background_surface, (0, 0))
                create_button_surface_instant(self.buttons)
                self.display_surface.blit(self.button_surface.convert_alpha(), (0, 0))
            pg.display.update()
            clock.tick(60)