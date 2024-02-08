from super_mapyo_bros.constants import *
from super_mapyo_bros.globals import *
from typing import List, Type


class Camera:
    level: Type["LevelOneOne"]
    screen_size: List[int]
    
    def __init__(self, level: Type["LevelOneOne"], screen_size: List[int]) -> None:
        self.level = level
        self.screen_size = screen_size
        self.getValues()
        self.x = 0
        self.y = 0
        self.w = screen_size[0]
        self.h = screen_size[1]

    def update(self) -> None:
        self.getValues()

    def getValues(self) -> None:
        from super_mapyo_bros.mario.mario import Mario

        mario: Mario = self.level.get_mario()

        if not mario:
            return
        
        if mario.x < self.screen_size[0] / 2:
            self.x = 0
            
        else:
            self.x = mario.x - self.screen_size[0] / 2 + tile_width / 2
