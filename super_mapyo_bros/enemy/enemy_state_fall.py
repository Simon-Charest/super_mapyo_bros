from super_mapyo_bros.entity import Entity
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import update_fall


class EnemyStateFall(State):
    def enter_state(self, entity: Entity) -> None:
        entity.velocity = 0

    def execute(self, entity: Entity, delta_time: int) -> None:
        # Update X
        if entity.direction == "left":
            entity.translate(-(0.1 * delta_time), 0)
            
        else:
            entity.translate(0.1 * delta_time, 0)

        # Update Y
        landed = update_fall(entity, delta_time)

        # Check land
        if landed:
            entity.change_state("move")

    def exit_state(self, entity: Entity) -> None:
        return
