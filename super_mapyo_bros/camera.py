from super_mapyo_bros.constants import *
from super_mapyo_bros.globals import *
from typing import List


class Camera:
    level = None
    screenSize: List[int]
    
    def __init__(self, level, screenSize) -> None:
        self.level = level
        self.screenSize = screenSize
        self.getValues()
        self.x = 0
        self.y = 0
        self.w = screenSize[0]
        self.h = screenSize[1]

    def update(self) -> None:
        self.getValues()

    def getValues(self) -> None:
        mario = self.level.getMario()

        if mario is None:
            return
        
        if mario.x < self.screenSize[0]/2:
            self.x = 0
            
        else:
            self.x = self.level.getMario().x - self.screenSize[0]/2 + tileWidth/2
