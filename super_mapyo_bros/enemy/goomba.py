from super_mapyo_bros.enemy.enemy import Enemy
from super_mapyo_bros.enemy.enemy_state_fall import EnemyStateFall
from super_mapyo_bros.enemy.enemy_state_move import EnemyStateMove
from super_mapyo_bros.enemy.enemy_state_wait import EnemyStateWait
from super_mapyo_bros.enemy.goomba_state_stomped import GoombaStateStomped


class Goomba(Enemy):
    def __init__(self, x, y, w, h, spawn_x, color) -> None:
        super().__init__(x, y, w, h, color)
        self.all_states = {
            "wait": EnemyStateWait(),
            "move": EnemyStateMove(),
            "fall": EnemyStateFall(),
            "stomped": GoombaStateStomped()
        }
        self.prev_state = self.all_states.get("wait")
        self.curr_state = self.prev_state
        self.spawn_x = spawn_x
        self.direction = "left"
        self.is_spawned = False
        self.is_dead = False
        self.is_dead_dead = False  #lulz
        self.velocity = 0
        self.dy = 0

    def update(self, delta_time) -> None:
        if not self.is_dead_dead:
            self.curr_state.execute(self, delta_time)

    def draw(self, screen, camera) -> None:
        if self.is_spawned and not self.is_dead_dead:
            super().draw(self)
