"""
Handles tracking and updating line tracking position.
"""
from consts import *
import pygame as pg

class ReferenceLine:
    def __init__(
            self, 
            start: tuple[int, int]=(GAME_W // 2, GAME_H),
            stop: tuple[int, int]=(0, 0)
        ):

        self.start = start
        self.stop = stop
        self.vector = [
                self.stop[0] - self.start[0],
                self.stop[1] - self.start[1]
            ]

    def update(
            self,
            screen: pg.Surface,
        ):
        self.stop = pg.mouse.get_pos()
        self.vector = [
                self.stop[0] - self.start[0],
                self.stop[1] - self.start[1]
            ]

        pg.draw.line(screen, GREY_R, self.start, self.stop)

