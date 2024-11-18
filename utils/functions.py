import pygame as pg
import sys

def close_game(event):
    if event.type == pg.QUIT:
        pg.quit()
        sys.exit()