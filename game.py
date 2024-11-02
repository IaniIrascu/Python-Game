import pygame as pg
import pygame.font

GAME_FPS = 60

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.scenes = {}
        self.current_scene = None
        self.clock = pygame.time.Clock()
        self.FPS = GAME_FPS
        pass

    def get_screen(self):
        return self.screen

    # # current scene
    # def set_current_scene(self, scene_name):
    #     self.current_scene = self.scenes[scene_name]
    #
    # def get_current_scene_name(self):
    #     # returneaza cheia cu valoarea
    #     return list(self.scenes.keys())[list(self.scenes.values()).index(self.current_scene)]

    # scene
    def get_scene(self, scene_name):
        # returns the object related to the name
        return self.scenes[scene_name]

    def add_scene(self, scene_name, scene):
        if scene_name not in self.scenes:
            self.scenes[scene_name] = scene

    def delete_scene(self, scene_name):
        if scene_name in self.scenes:
            self.scenes.pop(scene_name)
