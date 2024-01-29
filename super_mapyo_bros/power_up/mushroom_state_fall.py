from super_mapyo_bros.state import State
from super_mapyo_bros.utils import updateFall


class MushroomStateFall(State):
    def enterState(self, entity) -> None:
        entity.velocity = 0

    def execute(self, entity, deltaTime) -> None:
        # Update X
        if entity.direction == "left":
            entity.translate(-(0.15 * deltaTime), 0)
            
        else:
            entity.translate(0.15 * deltaTime, 0)

        # Update Y
        landed = updateFall(entity, deltaTime)

        # Check land
        if landed:
            entity.changeState("move")

    def exitState(self, entity) -> None:
        return
