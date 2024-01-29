from super_mapyo_bros.enemy.enemy import Enemy
from super_mapyo_bros.enemy.enemy_state_fall import EnemyStateFall
from super_mapyo_bros.enemy.enemy_state_move import EnemyStateMove
from super_mapyo_bros.enemy.enemy_state_wait import EnemyStateWait
from super_mapyo_bros.enemy.koopa_state_shell_move import KoopaStateShellMove
from super_mapyo_bros.enemy.koopa_state_stomped import KoopaStateStomped


class Koopa(Enemy):
    def __init__(self, x, y, w, h, spawnX, color) -> None:
        super().__init__(x, y, w, h, color)
        self.allStates = {
            "wait": EnemyStateWait(),
            "move": EnemyStateMove(),
            "fall": EnemyStateFall(),
            "stomped": KoopaStateStomped(),
            "shellMove": KoopaStateShellMove()
        }
        self.prevState = self.allStates.get("wait")
        self.currState = self.prevState
        self.spawnX = spawnX
        self.direction = "left"
        self.isSpawned = False
        self.isDead = False
        self.isDeadDead = False 
        self.velocity = 0
        self.dy = 0
        self.inShell = False

    def update(self, deltaTime) -> None:
        if not self.isDeadDead:
            self.currState.execute(self, deltaTime)

    def draw(self, screen, camera) -> None:
        if self.isSpawned and not self.isDeadDead:
            super().draw(self)
