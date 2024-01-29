from super_mapyo_bros.block.question_block_state_hit import QuestionBlockStateHit
from super_mapyo_bros.block.question_block_state_idle import QuestionBlockStateIdle
from super_mapyo_bros.entity import Entity


class QuestionBlock(Entity):
    level = None
    
    def __init__(self, x, y, w, h, contents, color, level) -> None:
        self.level = level
        super().__init__(x, y, w, h, color)
        self.allStates = {
            "idle": QuestionBlockStateIdle(),
            "hit": QuestionBlockStateHit(level)
        }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState
        self.contents = contents
        self.used = False

    def update(self, deltaTime) -> None:
        self.currState.execute(self, deltaTime)
