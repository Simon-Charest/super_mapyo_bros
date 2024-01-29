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
        self.allStates = {
            "idle":MarioStateIdle(),
            "move":MarioStateMove(level),
            "jump":MarioStateJump(),
            "fall":MarioStateFall()
        }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState
        self.speed = 0.5
        self.isDead = False
        self.dy = 0
        self.velocity = 0
        
    def update(self, deltaTime) -> None:
        self.currState.execute(self, deltaTime)
