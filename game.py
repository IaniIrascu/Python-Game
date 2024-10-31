import pygame as pg

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.scenes = {}
        self.current_scene = None
        pass

    def get_screen(self):
        return self.screen

    # current scene
    def set_current_scene(self, scene_name):
        self.current_scene = self.scenes[scene_name]

    def get_current_scene_name(self):
        return list(self.scenes.keys())[list(self.scenes.values()).index(self.current_scene)]  # returneaza cheia cu valoarea 

    # returns the object related to the name
    def get_scene(self, scene_name):
        return self.scenes[scene_name]

    def add_scene(self, scene_name, scene):
        if scene_name not in self.scenes:
            self.scenes[scene_name] = scene

    def delete_scene(self, scene_name):
        if scene_name in self.scenes:
            self.scenes.pop(scene_name)
