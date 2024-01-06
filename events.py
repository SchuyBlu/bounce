"""
Simple event handler.
"""
import pygame as pg
from line import Line, ReferenceLine
from copy import deepcopy

class EventHandler:
    def __init__(self):
        pass

    def location_update(
            self,
            screen: pg.Surface, 
            items: list[Line | ReferenceLine],
            curr: Line | ReferenceLine
        ):

            for shadow in items:
               shadow.update_shadow(screen) if isinstance(shadow, Line) else None
            curr.update_shadow(screen) if isinstance(curr, Line) else None

            for item in items:
                item.update(screen)
            curr.update(screen)

    def event_update(
            self,
            arrays: list[list[Line | ReferenceLine]],
            pos_updates: list[Line | ReferenceLine]
        ) -> bool:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            elif event.type == pg.MOUSEBUTTONDOWN:
                for i in range(len(arrays)):
                    arrays[i].append(deepcopy(pos_updates[i]))
                for update in pos_updates:
                    update.update_pos()
                    if isinstance(update, Line): print(f"Vector: {update.vector}, length: {update.length}")
        return True

