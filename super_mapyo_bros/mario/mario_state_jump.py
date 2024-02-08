from pygame import K_LSHIFT, K_a, K_d
from pygame.key import get_pressed
from super_mapyo_bros.constants import *
from super_mapyo_bros.enemy.enemy import Enemy
from super_mapyo_bros.globals import *
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides


class MarioStateJump(State):
    def enter_state(self, entity) -> None:
        entity.dy = 0
        entity.velocity = -0.2
        self.startHeight = entity.y
        self.dx = 0

    def execute(self, entity, delta_time) -> None:
        # Check in-air movement.
        key =   get_pressed()
        speed = entity.speed
        jumpGravity = gravity

        if key[K_LSHIFT]:
            speed *= 2
            jumpGravity *= 0.9
        if key[K_a]:
            entity.direction = "left"
            self.dx = -speed
        if key[K_d]:
            entity.direction = "right"
            self.dx = speed

        # Check collisions.
        if entity.has_collision:
            for tile in entity.colliding_objects:
                sides = collision_sides(entity.rect, tile.rect)
                if sides.top:
                    entity.set_y(tile.bottom() + (entity.y - tile.y))
                    entity.velocity = 0
                    entity.dy = 0
                if sides.bottom:
                    if isinstance(tile, Enemy) and not tile.is_dead:
                        entity.dy = 0
                        entity.velocity = -0.15
                    else:
                        entity.set_y(tile.top() - entity.h)
                        entity.change_state("idle")
                        return

        # Don't go so fast that collisions are missed
        if entity.dy > max_velocity:
            entity.dy = max_velocity

        else:
            entity.dy += entity.velocity
        
        entity.velocity += jumpGravity
        entity.translate(self.dx * delta_time, entity.dy * delta_time)

    def exit_state(self, entity) -> None:
        entity.has_collision = False
        entity.colliding_objects = []
