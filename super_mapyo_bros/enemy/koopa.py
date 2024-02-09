from pygame import Surface
from super_mapyo_bros.camera import Camera
from super_mapyo_bros.enemy.enemy import Enemy
from super_mapyo_bros.enemy.enemy_state_fall import EnemyStateFall
from super_mapyo_bros.enemy.enemy_state_move import EnemyStateMove
from super_mapyo_bros.enemy.enemy_state_wait import EnemyStateWait
from super_mapyo_bros.enemy.koopa_state_shell_move import KoopaStateShellMove
from super_mapyo_bros.enemy.koopa_state_stomped import KoopaStateStomped


class Koopa(Enemy):
    spawn_x: int
    is_spawned: bool
    is_dead: bool
    is_dead_dead: bool
    velocity: int
    dy: int
    in_shell: bool

    def __init__(self, x, y, w, h, spawn_x, color) -> None:
        super().__init__(x, y, w, h, color)
        self.all_states = {
            "wait": EnemyStateWait(),
            "move": EnemyStateMove(),
            "fall": EnemyStateFall(),
            "stomped": KoopaStateStomped(),
            "shellMove": KoopaStateShellMove()
        }
        self.prev_state = self.all_states.get("wait")
        self.curr_state = self.prev_state
        self.spawn_x = spawn_x
        self.direction = "left"
        self.is_spawned = False
        self.is_dead = False
        self.is_dead_dead = False 
        self.velocity = 0
        self.dy = 0
        self.in_shell = False

    def update(self, delta_time: int) -> None:
        if not self.is_dead_dead:
            self.curr_state.execute(self, delta_time)

    def draw(self, screen: Surface, camera: Camera) -> None:
        if self.is_spawned and not self.is_dead_dead:
            super().draw(screen, camera)
