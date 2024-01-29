from pygame.key import get_pressed
from pygame import K_a, K_d, K_SPACE
from super_mapyo_bros.state import State


class MarioStateIdle (State):
    def enterState(self, entity) -> None:
        return

    def execute(self, entity, deltaTime) -> None:
        key = get_pressed()
        
        if key[K_SPACE]:
            entity.changeState("jump")

        elif key[K_a]:
            entity.direction = "left"
            entity.changeState("move")

        elif key[K_d]:
            entity.direction = "right"
            entity.changeState("move")

        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                if isinstance(tile, Enemy) and not tile.isDead and (sides.left or sides.right or sides.top):
                    entity.isDead = True

            entity.hasCollision = False
            entity.collidingObjects = []

    def exitState(self, entity) -> None:
        entity.hasCollision = False
        entity.collidingObjects = []
