#!/usr/bin/env python3
"""
Runs a simple ball bouncing game.
"""
from consts import *
import time
import os
import pygame as pg
from line import ReferenceLine

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (SCREEN_W / 2, 0)
pg.init()
screen = pg.display.set_mode((GAME_W, GAME_H))
clock = pg.time.Clock()
running = True

prev_time = time.time()
ref_line = ReferenceLine()
while running:
    # --- framerate resolution ---
    dt = time.time() - prev_time
    dt *= TARGET_FPS
    prev_time = time.time()

    # --- Draw updates ---
    screen.fill(pg.Color(BLUE_D))
    ref_line.update(screen)

    # --- Event related ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # --- Update display ---
    pg.display.update()
    clock.tick(TARGET_FPS)

pg.quit()

