from super_mapyo_bros.entity import Entity
from super_mapyo_bros.mario.mario_state_fall import MarioStateFall
from super_mapyo_bros.mario.mario_state_idle import MarioStateIdle
from super_mapyo_bros.mario.mario_state_jump import MarioStateJump
from super_mapyo_bros.mario.mario_state_move import MarioStateMove


class Mario(Entity):
    level = None

    def __init__(self, x, y, w, h, color, level) -> None:
        self.level = level
        super().__init__(x, y, w, h, color)
        self.all_states = {
            "idle":MarioStateIdle(),
            "move":MarioStateMove(level),
            "jump":MarioStateJump(),
            "fall":MarioStateFall()
        }
        self.prev_state = self.all_states.get("idle")
        self.curr_state = self.prev_state
        self.speed = 0.5
        self.is_dead = False
        self.dy = 0
        self.velocity = 0
        
    def update(self, delta_time: int) -> None:
        self.curr_state.execute(self, delta_time)
