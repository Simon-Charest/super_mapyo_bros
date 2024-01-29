from super_mapyo_bros.enemy.enemy import Enemy
from super_mapyo_bros.enemy.enemy_state_fall import EnemyStateFall
from super_mapyo_bros.enemy.enemy_state_move import EnemyStateMove
from super_mapyo_bros.enemy.enemy_state_wait import EnemyStateWait
from super_mapyo_bros.enemy.goomba_state_stomped import GoombaStateStomped


class Goomba(Enemy):
    def __init__(self, x, y, w, h, spawnX, color) -> None:
        super().__init__(x, y, w, h, color)
        self.allStates = {
            "wait": EnemyStateWait(),
            "move": EnemyStateMove(),
            "fall": EnemyStateFall(),
            "stomped": GoombaStateStomped()
        }
        self.prevState = self.allStates.get("wait")
        self.currState = self.prevState
        self.spawnX = spawnX
        self.direction = "left"
        self.isSpawned = False
        self.isDead = False
        self.isDeadDead = False #lulz
        self.velocity = 0
        self.dy = 0

    def update(self, deltaTime) -> None:
        if not self.isDeadDead:
            self.currState.execute(self, deltaTime)

    def draw(self, screen, camera) -> None:
        if self.isSpawned and not self.isDeadDead:
            super().draw(self)
