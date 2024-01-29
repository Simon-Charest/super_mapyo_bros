from pygame.key import get_pressed
from pygame import K_a, K_d, K_LSHIFT
from super_mapyo_bros.state import State


class MarioStateFall(State):
    def enterState(self, entity) -> None:
        self.dx = 0
        entity.velocity = 0
    
    def execute(self, entity, deltaTime) -> None:
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
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                if sides.bottom:
                    if isinstance(tile, Enemy) and not tile.isDead:
                        entity.dy = 0
                        entity.velocity = -0.15
                    else:
                        entity.setY(tile.top() - entity.h)
                        entity.changeState("idle")
                        return
        
        if entity.dy > maxVelocity:
            entity.dy = maxVelocity

        else:
            entity.dy += entity.velocity
            
        entity.velocity += gravity
        entity.translate(self.dx * deltaTime, entity.dy * deltaTime)

    def exitState(self, entity) -> None:
        entity.hasCollision = False
        entity.collidingObjects = []
