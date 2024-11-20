import os
from pytmx.util_pygame import load_pygame
import pygame as pg

def import_tmx(*path):
    tmx = {}
    for folder, subfolder, files in os.walk(os.path.join(*path)):
        for file in files:
            tmx[file.split('.')[0]] = load_pygame(os.path.join(folder, file))
    return tmx

def import_png(*path, alpha = True):
    new_path = os.path.join(*path) + ".png"
    return (pg.image.load(new_path).convert_alpha() if alpha else pg.image.load(new_path)).convert()

def import_frames(*path):
    frames = []
    for folder, subfolder, file in os.walk(os.path.join(*path)):
        for img in file:
            new_path = os.path.join(folder, img)
            image = pg.image.load(new_path).convert_alpha()
            frames.append(image)
    return frames

def import_frame_extra_steps(*path):
    frames = {}
    for folders, subfolders, files in os.walk(os.path.join(*path)):
        if subfolders:
            for subfolder in subfolders:
                frames[subfolder] = import_frames(path, subfolder)
    return frames

def import_tilemap(cols, rows, *path):
	frames = {}
	surf = import_png(*path)
	width, height = surf.get_width() / cols, surf.get_height() / rows
	for col in range(cols):
		for row in range(rows):
			rect = pg.Rect(col * width, row * height, width, height)
			surface = pg.Surface((width, height))
			surface.fill('green')
			surface.set_colorkey('green')
			surface.blit(surf, (0,0), rect)
			frames[(col, row)] = surface
	return frames

def import_coast(cols, rows, *path):
	frames = import_tilemap(cols, rows, *path)
	new_dict = {}
	terrains = ['grass', 'grass_i', 'sand_i', 'sand', 'rock', 'rock_i', 'ice', 'ice_i']
	sides = {
		'topleft': (0,0), 'top': (1,0), 'topright': (2,0), 
		'left': (0,1), 'right': (2,1), 'bottomleft': (0,2), 
		'bottom': (1,2), 'bottomright': (2,2)}
	for index, terrain in enumerate(terrains):
		new_dict[terrain] = {}
		for key, pos in sides.items():
			new_dict[terrain][key] = [frames[(pos[0] + index * 3, pos[1] + row)] for row in range(0,rows, 3)]
	return new_dict

def import_one_character(*path):
    frames = import_tilemap(4, 4, *path)
    enhanced = {}
    for row, dir in enumerate(['down', 'left', 'right', 'up']):
        enhanced[dir] = [frames[(col, row)] for col in range(0, 4)]
        enhanced[f'{dir}_idle'] = [frames[(0, row)]]
        
    return enhanced

def import_characters(*path):
	characters = {}
	for folder, subfolder, files in os.walk(os.path.join(*path)):
		for file in files:
			name = file.split('.')[0]
			characters[name] = import_one_character(*path, name)
	return characters