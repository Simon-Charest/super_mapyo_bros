from pygame import K_a, K_d, K_LSHIFT, K_SPACE
from pygame.key import get_pressed
from super_mapyo_bros.enemy.enemy import Enemy
from super_mapyo_bros.state import State
from super_mapyo_bros.utils import collision_sides, should_fall


class MarioStateMove(State):
    level = None

    def __init__(self, level) -> None:
        self.level = level

    def enterState(self, entity) -> None:
        self.run = False
    
    def execute(self, entity, deltaTime) -> None:
        key = get_pressed()

        # Check for move off of any platform
        shouldFall = should_fall(entity, self.level)
        
        if shouldFall:
            entity.changeState("fall")

        if key[K_SPACE]:
            entity.changeState("jump")
        
        if key[K_LSHIFT]:
            self.run = True
            
        if key[K_a]:
            if self.run:
                entity.translate(-(entity.speed) * 2 * deltaTime, 0)

            else:
                entity.translate(-(entity.speed) * deltaTime, 0)

            entity.direction = "left"
            
        if key[K_d]:
            if self.run:
                entity.translate(entity.speed * 2 * deltaTime, 0)

            else:
                entity.translate(entity.speed * deltaTime, 0)
            entity.direction = "right"

        if not key[K_LSHIFT]:
            self.run = False

        if not key[K_a] and not key[K_d]:
            entity.changeState("idle")

        # Check for move into something.
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)

                if isinstance(tile, Enemy) and (sides.left or sides.right or sides.top):
                    # If an enemy and still alive then hurt mario.
                    if not tile.isDead:
                        entity.isDead = True

                if sides.left:
                    entity.setX(tile.x + tile.w)

                elif sides.right:
                    entity.setX(tile.x - entity.w)

            entity.hasCollision = False
            entity.collidingObjects = []
 
    def exitState(self, entity) -> None:
        entity.hasCollision = False
        entity.collidingObjects = []
