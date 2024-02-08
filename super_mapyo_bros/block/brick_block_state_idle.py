from super_mapyo_bros.mario.mario import Mario
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides


class BrickBlockStateIdle(State):
    def enter_state(self, entity) -> None:
        return

    def execute(self, entity, delta_time) -> None:
        if entity.has_collision:
            for tile in entity.colliding_objects:
                sides = collision_sides(entity.rect, tile.rect)

                # If Mario jumped up and collided with block.
                if isinstance(tile, Mario) and tile.y > entity.y:
                    entity.change_state("hitLight")

            entity.has_collision = False
            entity.colliding_objects = []

    def exit_state(self, entity) -> None:
        return
