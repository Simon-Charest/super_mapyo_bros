from super_mapyo_bros.block.brick_block_state_hit_light import BrickBlockStateHitLight
from super_mapyo_bros.block.brick_block_state_idle import BrickBlockStateIdle
from super_mapyo_bros.entity import Entity


class BrickBlock(Entity):
    def __init__(self, x, y, w, h, color) -> None:
        super().__init__(x, y, w, h, color)
        self.allStates = {
            "idle": BrickBlockStateIdle(),
            "hitLight": BrickBlockStateHitLight()
            #"hit_hard": BrickBlockStateHitHard() 
        }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState
        
    def update(self, deltaTime) -> None:
        self.currState.execute(self, deltaTime)
