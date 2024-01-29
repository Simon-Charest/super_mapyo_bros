from super_mapyo_bros.entity import Entity


class Enemy(Entity):
    def __init__(self, x, y, w, h, color) -> None:
        super().__init__(x, y, w, h, color)
