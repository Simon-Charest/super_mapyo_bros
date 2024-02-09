from super_mapyo_bros.block.question_block_state_hit import QuestionBlockStateHit
from super_mapyo_bros.block.question_block_state_idle import QuestionBlockStateIdle
from super_mapyo_bros.entity import Entity


class QuestionBlock(Entity):
    level = None
    
    def __init__(self, x, y, w, h, contents, color, level) -> None:
        self.level = level
        super().__init__(x, y, w, h, color)
        self.all_states = {
            "idle": QuestionBlockStateIdle(),
            "hit": QuestionBlockStateHit(level)
        }
        self.prev_state = self.all_states.get("idle")
        self.curr_state = self.prev_state
        self.contents = contents
        self.used = False

    def update(self, delta_time: int) -> None:
        self.curr_state.execute(self, delta_time)
