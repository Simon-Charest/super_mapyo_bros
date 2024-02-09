from sre_parse import State


class CoinStateUnused(State):
    def enter_state(self, entity) -> None:
       entity.set_x(-100)
       entity.set_y(0)
       entity.active = False

    def execute(self, entity, delta_time: int) -> None:
        return

    def exit_state(self, entity) -> None:
        return
