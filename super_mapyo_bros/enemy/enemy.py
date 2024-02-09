from super_mapyo_bros.entity import Entity
from typing import List


class Enemy(Entity):
    def __init__(self, x: float, y: float, w: float, h: float, color: List[int]) -> None:
        super().__init__(x, y, w, h, color)
