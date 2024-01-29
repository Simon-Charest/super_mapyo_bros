from super_mapyo_bros.globals import tileWidth
from super_mapyo_bros.state import State


class MushroomStateSpawn(State):
    def enterState(self, entity) -> None:
       entity.active = True
       self.startY = entity.y

    def execute(self, entity, deltaTime) -> None:
        dy = 0.05 * deltaTime
        entity.translate(0, -dy)

        if entity.y <= self.startY - tileWidth:
            entity.direction = "right"
            entity.changeState("move")

    def exitState(self, entity) -> None:
        return
