from super_mapyo_bros.entity import Entity
from super_mapyo_bros.mario.mario import Mario
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides, should_fall
from typing import Type


class MushroomStateMove(State):
    level = None
    
    def __init__(self, level: Type["LevelOneOne"]) -> None:
        self.level = level

    def enter_state(self, entity: Entity) -> None:
        return

    def execute(self, entity, delta_time) -> None:
        if entity.direction == "left":
            entity.translate(-(0.15 * delta_time), 0)

        else:
            entity.translate(0.15 * delta_time, 0)

        # Check if should fall.
        shouldFall = should_fall(entity, self.level)

        if shouldFall:
            entity.change_state("fall")

        # Check for move into something.
        if entity.has_collision:
            for tile in entity.colliding_objects:
                sides = collision_sides(entity.rect, tile.rect)
                
                # That something was Mario.
                if sides.top and isinstance(tile, Mario):
                    entity.active = False
                    entity.set_x(-100)
                    entity.set_y(100)
                    entity.change_state("spawn")
                    
                if sides.left:
                    entity.set_x(tile.x + tile.w)
                    entity.direction = "right"

                elif sides.right:
                    entity.set_x(tile.x - entity.w)
                    entity.direction = "left"
                
            entity.has_collision = False
            entity.colliding_objects = []

    def exit_state(self, entity) -> None:
        return
