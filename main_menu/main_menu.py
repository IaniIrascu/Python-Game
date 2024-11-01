import sys
import pygame as pg
from main_menu.button import *

class MainMenu():
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.buttons = {"Start": Button(self.display_surface, "Start", YELLOW, (self.display_surface.get_width() / 2 - 100, self.display_surface.get_height() / 3), (200, 100)),
                        "Load": Button(self.display_surface, "Load", BLUE, (self.display_surface.get_width() / 2 - 100, self.display_surface.get_height() / 2), (200, 100)),
                        "Quit": Button(self.display_surface, "Quit", RED, (self.display_surface.get_width() / 2 - 100, 2 * self.display_surface.get_height() / 3), (200, 100))}

    def set_menu_color(self, color):
        self.display_surface.fill(color)

    def run(self):
        self.display_surface.fill(WHITE)
        for button in self.buttons:
            self.buttons[button].update_button()

        start_button = self.buttons["Start"]
        quit_button = self.buttons["Quit"]
        load_button = self.buttons["Load"]

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    mouse_pos = pg.mouse.get_pos()
                    print(mouse_pos)
                    # check if mouse is on start button
                    if (start_button.position[0] <= mouse_pos[0] <= start_button.position[0] + start_button.size[0] and
                        start_button.position[1] <= mouse_pos[1] <= start_button.position[1] + start_button.size[1]):
                        return "Start"
                    if (load_button.position[0] <= mouse_pos[0] <= load_button.position[0] + load_button.size[0] and
                        load_button.position[1] <= mouse_pos[1] <= load_button.position[1] + load_button.size[1]):
                        return "Load"
                    # check if button is on quit button
                    if (quit_button.position[0] <= mouse_pos[0] <= quit_button.position[0] + quit_button.size[0] and
                        quit_button.position[1] <= mouse_pos[1] <= quit_button.position[1] + quit_button.size[1]):
                        sys.exit()