from super_mapyo_bros.block.brick_block_state_hit_light import BrickBlockStateHitLight
from super_mapyo_bros.block.brick_block_state_idle import BrickBlockStateIdle
from super_mapyo_bros.entity import Entity


class BrickBlock(Entity):
    def __init__(self, x, y, w, h, color) -> None:
        super().__init__(x, y, w, h, color)
        self.all_states = {
            "idle": BrickBlockStateIdle(),
            "hitLight": BrickBlockStateHitLight()
            #"hit_hard": BrickBlockStateHitHard() 
        }
        self.prev_state = self.all_states.get("idle")
        self.curr_state = self.prev_state
        
    def update(self, delta_time: int) -> None:
        self.curr_state.execute(self, delta_time)
