from super_mapyo_bros.globals import tile_width
from super_mapyo_bros.state import State


class MushroomStateSpawn(State):
    def enter_state(self, entity) -> None:
       entity.active = True
       self.startY = entity.y

    def execute(self, entity, delta_time) -> None:
        dy = 0.05 * delta_time
        entity.translate(0, -dy)

        if entity.y <= self.startY - tile_width:
            entity.direction = "right"
            entity.change_state("move")

    def exit_state(self, entity) -> None:
        return
