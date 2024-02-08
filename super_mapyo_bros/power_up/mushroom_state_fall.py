from super_mapyo_bros.state import State
from super_mapyo_bros.utils import update_fall


class MushroomStateFall(State):
    def enter_state(self, entity) -> None:
        entity.velocity = 0

    def execute(self, entity, delta_time) -> None:
        # Update X
        if entity.direction == "left":
            entity.translate(-(0.15 * delta_time), 0)
            
        else:
            entity.translate(0.15 * delta_time, 0)

        # Update Y
        landed = update_fall(entity, delta_time)

        # Check land
        if landed:
            entity.change_state("move")

    def exit_state(self, entity) -> None:
        return
