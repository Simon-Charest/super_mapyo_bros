from super_mapyo_bros.block.pipe_state_idle import PipeStateIdle
from super_mapyo_bros.entity import Entity
from typing import List


class Pipe(Entity):
    def __init__(self, x: float, y: float, w: float, h: float, color: List[int]) -> None:
        super().__init__(x, y, w, h, color)
        self.all_states = { "idle": PipeStateIdle() }
        self.prev_state = self.all_states.get("idle")
        self.curr_state = self.prev_state

    def update(self, delta_time: int) -> None:
        self.curr_state.execute(self, delta_time)
