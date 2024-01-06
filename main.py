#!/usr/bin/env python3
"""
Runs a simple ball bouncing game.
"""
from consts import *
import time
import os
import pygame as pg
from line import ReferenceLine, Line
from events import EventHandler
from copy import deepcopy
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (SCREEN_W / 2, 0)

# -- Set up for pygame ---
pg.init()
screen = pg.display.set_mode((GAME_W, GAME_H))
clock = pg.time.Clock()
running = True
prev_time = time.time()

lines = []
line = Line()
ref_line = ReferenceLine()
event_handler = EventHandler()
event_handler.location_update(screen, lines, line)
while running:
    # --- framerate resolution ---
    dt = time.time() - prev_time
    dt *= TARGET_FPS
    prev_time = time.time()

    # --- Draw updates ---
    screen.fill(pg.Color(BLUE_D))
    event_handler.location_update(screen, lines, line)
    ref_line.update(screen)

    # --- Event related ---
    event_handler.event_update([lines], [line, ref_line])

    # --- Update display ---
    pg.display.update()
    clock.tick(TARGET_FPS)

pg.quit()

