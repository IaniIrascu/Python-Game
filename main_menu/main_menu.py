import sys
import pygame as pg


from main_menu.button import *
from game import Game

class MainMenu(Game):
    def __init__(self):
        super().__init__()
        self.buttons = {"Start": Button(self.screen, "Start", YELLOW, (self.screen.get_width() / 2 - 100, self.screen.get_height() / 3), (200, 100)),
                        "Load": Button(self.screen, "Load", BLUE, (self.screen.get_width() / 2 - 100, self.screen.get_height() / 2), (200, 100)),
                        "Quit": Button(self.screen, "Quit", RED, (self.screen.get_width() / 2 - 100, 2 * self.screen.get_height() / 3), (200, 100))}

    def set_menu_color(self, screen, color):
        self.screen.fill(color)

    # def add_button(self, button_name, button):
    #     if button_name not in self.buttons:
    #         self.buttons[button_name] = button
    #
    # def delete_button(self, button_name):
    #     if button_name in self.buttons:
    #         self.buttons.pop(button_name)

    def run(self):
    # Design ecran

        self.screen.fill(WHITE)
        for button in self.buttons:
            self.buttons[button].update_button()

    # Final design ecran

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