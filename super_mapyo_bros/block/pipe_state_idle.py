from super_mapyo_bros.entity import Entity
from super_mapyo_bros.state import State


class PipeStateIdle(State):
    def enter_state(self, entity: Entity) -> None:
        return

    def execute(self, entity: Entity, delta_time: int) -> None:
        if entity.has_collision:
            entity.has_collision = False
            entity.colliding_objects = []
        
    def exit_state(self, entity: Entity) -> None:
        return
