from pygame.key import get_pressed
from pygame import K_a, K_d, K_LSHIFT
from super_mapyo_bros.constants import *
from super_mapyo_bros.enemy.enemy import Enemy
from super_mapyo_bros.entity import Entity
from super_mapyo_bros.globals import *
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides


class MarioStateFall(State):
    def enter_state(self, entity: Entity) -> None:
        self.dx = 0
        entity.velocity = 0
    
    def execute(self, entity: Entity, delta_time: int) -> None:
        # Check in-air movement.
        key = get_pressed()
        speed = entity.speed

        if key[K_LSHIFT]:
            speed *= 2

        if key[K_a]:
            entity.direction = "left"
            self.dx = -speed

        if key[K_d]:
            entity.direction = "right"
            self.dx = speed

        # Check for landing
        if entity.has_collision:
            for tile in entity.colliding_objects:
                sides = collision_sides(entity.rect, tile.rect)

                if sides.bottom:
                    if isinstance(tile, Enemy) and not tile.is_dead:
                        entity.dy = 0
                        entity.velocity = -0.15

                    else:
                        entity.set_y(tile.top() - entity.h)
                        entity.change_state("idle")
                        
                        return
        
        if entity.dy > max_velocity:
            entity.dy = max_velocity

        else:
            entity.dy += entity.velocity
            
        entity.velocity += gravity
        entity.translate(self.dx * delta_time, entity.dy * delta_time)

    def exit_state(self, entity: Entity) -> None:
        entity.has_collision = False
        entity.colliding_objects = []
