from pygame import Rect
from super_mapyo_bros.mario.mario import Mario
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides


class KoopaStateStomped(State):
    def enter_state(self, entity) -> None:
        self.time = 0
        self.recoverTime = 5000 # five seconds

        if entity.inShell == False:
            entity.y += entity.h/2
            entity.h /= 2
            entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)

        entity.inShell = True
        entity.is_dead = True

    def execute(self, entity, delta_time) -> None:
        self.time += delta_time

        # Come back out of shell.
        if self.time > self.recoverTime:
            entity.is_dead = False
            entity.inShell = False
            entity.change_state("move")
            entity.y -= entity.h*2
            entity.h *= 2
            entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)
            return

        # Otherwise check for mario hitting it in some direction.
        if entity.has_collision:
            for tile in entity.colliding_objects:
                sides = collision_sides(entity.rect, tile.rect)
                if isinstance(tile, Mario):
                    # Decide which way to shoot shell.
                    if tile.x <= entity.x:
                        entity.direction = "right"
                    else:
                        entity.direction = "left"
                    # Shoot shell.
                    entity.is_dead = False
                    entity.change_state("shellMove")

            entity.has_collision = False
            entity.colliding_objects = []

    def exit_state(self, entity) -> None:
        return
