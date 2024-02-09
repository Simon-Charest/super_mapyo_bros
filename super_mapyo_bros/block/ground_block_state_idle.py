from super_mapyo_bros.entity import Entity
from super_mapyo_bros.state import State


class GroundBlockStateIdle(State):
    def enter_state(self, entity: Entity) -> None:
        return

    def execute(self, entity, delta_time: int) -> None:
        return
        
    def exit_state(self, entity: Entity) -> None:
        return
