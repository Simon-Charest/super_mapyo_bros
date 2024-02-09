from sre_parse import State

from super_mapyo_bros.entity import Entity


class CoinStateUnused(State):
    def enter_state(self, entity: Entity) -> None:
       entity.set_x(-100)
       entity.set_y(0)
       entity.active = False

    def execute(self, entity: Entity, delta_time: int) -> None:
        return

    def exit_state(self, entity: Entity) -> None:
        return
