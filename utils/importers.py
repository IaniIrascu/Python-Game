import os
from pytmx.util_pygame import load_pygame

def import_tmx(*path):
    print("\n\ncome on\n\n")
    tmx = {}
    for folder, subfolder, files in os.walk(os.path.join(*path)):
        for file in files:
            print(os.path.join(folder, file) + " loaded\n")
            tmx[file.split('.')[0]] = load_pygame(os.path.join(folder, file))
    return tmx