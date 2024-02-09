from pygame.key import get_pressed
from pygame import K_a, K_d, K_SPACE
from super_mapyo_bros.enemy.enemy import Enemy
from super_mapyo_bros.entity import Entity
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides


class MarioStateIdle(State):
    def enter_state(self, entity: Entity) -> None:
        return

    def execute(self, entity: Entity, delta_time: int) -> None:
        key = get_pressed()
        
        if key[K_SPACE]:
            entity.change_state("jump")

        elif key[K_a]:
            entity.direction = "left"
            entity.change_state("move")

        elif key[K_d]:
            entity.direction = "right"
            entity.change_state("move")

        if entity.has_collision:
            for tile in entity.colliding_objects:
                sides = collision_sides(entity.rect, tile.rect)
                if isinstance(tile, Enemy) and not tile.is_dead and (sides.left or sides.right or sides.top):
                    entity.is_dead = True

            entity.has_collision = False
            entity.colliding_objects = []

    def exit_state(self, entity: Entity) -> None:
        entity.has_collision = False
        entity.colliding_objects = []
