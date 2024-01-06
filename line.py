"""
Handles tracking and updating line tracking position.
"""
from consts import *
import pygame as pg
import math

class BaseLine:
    def __init__(
            self,
            start: tuple[int, int],
            stop: tuple[int, int],
        ):
        self.start = start
        self.stop = stop
        self.vector = [
                self.stop[0] - self.start[0],
                self.stop[1] - self.start[1]
            ]
        self.length = math.sqrt(self.vector[0]**2 + self.vector[1]**2)


    def update_pos(self):
        x, y = pg.mouse.get_pos()
        self.vector = [
                x - self.stop[0],
                y - self.stop[1]
            ]
        
        self.start = self.stop
        self.stop = (x, y)
        self.length = math.sqrt(self.vector[0]**2 + self.vector[1]**2)


class ReferenceLine(BaseLine):
    def __init__(
            self, 
            start: tuple[int, int]=(GAME_W // 2, GAME_H),
            stop: tuple[int, int]=(0, 0),
        ):
        super().__init__(start, stop)

    def update(
            self,
            screen: pg.Surface,
        ):
        self.stop = pg.mouse.get_pos()

        pg.draw.line(screen, GREY_R, self.start, self.stop)


class Line(BaseLine):
    def __init__(
            self,
            start: tuple[int, int]=(GAME_W // 2, GAME_H),
            stop: tuple[int, int]=(GAME_W // 2, GAME_H),
        ):
        super().__init__(start, stop)

        # Related to effects
        self.ball_radius = 10
        self.ball_radiate = self.ball_radius
        self.ball_radiate_width = 8
        self.shadow_start = None
        self.shadow_stop = None

    def update_shadow(
            self,
            screen: pg.Surface
        ):
        shadow_start = (self.start[0] - 15, self.start[1] + 20)
        shadow_stop = (self.stop[0] - 15, self.stop[1] + 20)
        pg.draw.line(screen, BLUE_S, shadow_start, shadow_stop, 4)
        pg.draw.circle(screen, BLUE_S, shadow_stop, self.ball_radius)
        
    def update(
            self,
            screen: pg.Surface
        ):
        self.ball_radiate += 0.4
        self.ball_radiate_width -= 0.12
        if not int(self.ball_radiate_width):
            self.ball_radiate_width = 8
            self.ball_radiate = self.ball_radius

        pg.draw.line(screen, GREY_B, self.start, self.stop, 4)
        pg.draw.circle(screen, GREY_B, self.stop, self.ball_radius)
        pg.draw.circle(
                screen,
                GREY_B,
                self.stop,
                self.ball_radiate,
                int(self.ball_radiate_width)
            )

