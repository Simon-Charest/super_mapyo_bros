from super_mapyo_bros.mario.mario import Mario
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides


class BrickBlockStateIdle(State):
    def enterState(self, entity) -> None:
        return

    def execute(self, entity, deltaTime) -> None:
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)

                # If Mario jumped up and collided with block.
                if isinstance(tile, Mario) and tile.y > entity.y:
                    entity.changeState("hitLight")

            entity.hasCollision = False
            entity.collidingObjects = []

    def exitState(self, entity) -> None:
        return
