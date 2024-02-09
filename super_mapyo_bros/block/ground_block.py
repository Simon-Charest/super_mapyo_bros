from super_mapyo_bros.block.ground_block_state_idle import GroundBlockStateIdle
from super_mapyo_bros.entity import Entity
from typing import List


class GroundBlock(Entity):
    def __init__ (self, x: float, y: float, w: float, h: float, color: List[int]):
        super().__init__(x, y, w, h, color)
        self.all_states = { "idle":GroundBlockStateIdle() }
        self.prev_state = self.all_states.get("idle")
        self.curr_state = self.prev_state

    def update(self, delta_time: int):
        self.curr_state.execute(self, delta_time)
