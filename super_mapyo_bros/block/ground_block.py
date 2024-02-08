from super_mapyo_bros.block.ground_block_state_idle import GroundBlockStateIdle
from super_mapyo_bros.entity import Entity


class GroundBlock(Entity):
    def __init__ (self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)
        self.all_states = { "idle":GroundBlockStateIdle() }
        self.prev_state = self.all_states.get("idle")
        self.curr_state = self.prev_state

    def update(self, delta_time):
        self.curr_state.execute(self, delta_time)
