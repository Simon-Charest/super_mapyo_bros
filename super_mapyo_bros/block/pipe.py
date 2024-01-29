from super_mapyo_bros.block.pipe_state_idle import PipeStateIdle
from super_mapyo_bros.entity import Entity


class Pipe(Entity):
    def __init__(self, x, y, w, h, color) -> None:
        super().__init__(x, y, w, h, color)
        self.allStates = { "idle":PipeStateIdle() }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState

    def update(self, deltaTime) -> None:
        self.currState.execute(self, deltaTime)
