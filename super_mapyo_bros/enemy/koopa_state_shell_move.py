from super_mapyo_bros.entity import Entity
from super_mapyo_bros.mario.mario import Mario
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides, should_fall


class KoopaStateShellMove(State):
    def enter_state(self, entity: Entity) -> None:
        return

    def execute(self, entity: Entity, delta_time: int) -> None:
        if entity.direction == "left":
            entity.translate(-(0.8 * delta_time), 0)

        else:
            entity.translate(0.8 * delta_time, 0)

        # Check if should fall.
        shouldFall = should_fall(entity)

        if shouldFall:
            entity.change_state("fall")

        # Check for move into something.
        if entity.has_collision:
            for tile in entity.colliding_objects:
                sides = collision_sides(entity.rect, tile.rect)
                
                # That something was Mario.
                if sides.top and isinstance(tile, Mario):
                    entity.change_state("stomped")
                
                if sides.left:
                    entity.set_x(tile.x + tile.w)
                    entity.direction = "right"
                    
                elif sides.right:
                    entity.set_x(tile.x - entity.w)
                    entity.direction = "left"
                
            entity.has_collision = False
            entity.colliding_objects = []

    def exit_state(self, entity: Entity) -> None:
        return
