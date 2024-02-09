from super_mapyo_bros.entity import Entity
from super_mapyo_bros.mario.mario import Mario
from super_mapyo_bros.state import State


class QuestionBlockStateIdle(State):
    def enter_state(self, entity: Entity) -> None:
        return

    def execute(self, entity: Entity, delta_time: int) -> None:
        if entity.has_collision:
            for tile in entity.colliding_objects:
                # If Mario jumped up and collided with block.
                if isinstance(tile, Mario) and tile.y > entity.y:
                    entity.change_state("hit")
            entity.has_collision = False
            entity.colliding_objects = []

    def exit_state(self, entity: Entity) -> None:
        return
