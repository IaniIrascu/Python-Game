import pygame as pg
import os
from pytmx.util_pygame import load_pygame

def import_tmx(*path):
    tmx = {}
    for folder, files in os.walk(os.path.join(*path)):
        for file in files:
            tmx[file.split('.')[0]] = load_pygame(os.path.join(folder, file))
    return tmx