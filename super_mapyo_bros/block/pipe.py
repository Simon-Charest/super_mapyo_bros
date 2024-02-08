from super_mapyo_bros.block.pipe_state_idle import PipeStateIdle
from super_mapyo_bros.entity import Entity


class Pipe(Entity):
    def __init__(self, x, y, w, h, color) -> None:
        super().__init__(x, y, w, h, color)
        self.all_states = { "idle": PipeStateIdle() }
        self.prev_state = self.all_states.get("idle")
        self.curr_state = self.prev_state

    def update(self, delta_time) -> None:
        self.curr_state.execute(self, delta_time)
