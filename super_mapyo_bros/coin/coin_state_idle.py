from super_mapyo_bros.state import State


class CoinStateIdle(State):
    def enter_state (self, entity) -> None:
        entity.active = True
        self.timer = 0
        self.delay = 1000

    def execute(self, entity, delta_time) -> None:
        self.timer += delta_time

        if self.timer > self.delay:
            entity.change_state("unused")

    def exit_state(self, entity) -> None:
        return
