from super_mapyo_bros.block.ground_block_state_idle import GroundBlockStateIdle
from super_mapyo_bros.entity import Entity


class GroundBlock(Entity):
    def __init__ (self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)
        self.allStates = { "idle":GroundBlockStateIdle() }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState

    def update(self, deltaTime):
        self.currState.execute(self, deltaTime)
