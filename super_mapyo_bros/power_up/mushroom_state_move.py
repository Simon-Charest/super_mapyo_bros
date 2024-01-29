from super_mapyo_bros.mario.mario import Mario
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides, should_fall


class MushroomStateMove(State):
    level = None
    
    def __init__(self, level) -> None:
        self.level = level

    def enterState(self, entity) -> None:
        return

    def execute(self, entity, deltaTime) -> None:
        if entity.direction == "left":
            entity.translate(-(0.15 * deltaTime), 0)

        else:
            entity.translate(0.15 * deltaTime, 0)

        # Check if should fall.
        shouldFall = should_fall(entity, self.level)

        if shouldFall:
            entity.changeState("fall")

        # Check for move into something.
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                
                # That something was Mario.
                if sides.top and isinstance(tile, Mario):
                    entity.active = False
                    entity.setX(-100)
                    entity.setY(100)
                    entity.changeState("spawn")
                    
                if sides.left:
                    entity.setX(tile.x + tile.w)
                    entity.direction = "right"

                elif sides.right:
                    entity.setX(tile.x - entity.w)
                    entity.direction = "left"
                
            entity.hasCollision = False
            entity.collidingObjects = []

    def exitState(self, entity) -> None:
        return
