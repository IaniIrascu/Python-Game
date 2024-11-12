import pygame as pg
import sys

def close_game():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()