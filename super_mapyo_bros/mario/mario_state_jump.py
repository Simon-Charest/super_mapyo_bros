from sre_parse import State


class MarioStateJump (State):
    def enterState(self, entity) -> None:
        entity.dy = 0
        entity.velocity = -0.2
        self.startHeight = entity.y
        self.dx = 0

    def execute(self, entity, deltaTime) -> None:
        # Check in-air movement.
        key = pygame.key.get_pressed()
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
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                if sides.top:
                    entity.setY(tile.bottom() + (entity.y - tile.y))
                    entity.velocity = 0
                    entity.dy = 0
                if sides.bottom:
                    if isinstance(tile, Enemy) and not tile.isDead:
                        entity.dy = 0
                        entity.velocity = -0.15
                    else:
                        entity.setY(tile.top() - entity.h)
                        entity.changeState("idle")
                        return

        # Don't go so fast that collisions are missed
        if entity.dy > maxVelocity:
            entity.dy = maxVelocity

        else:
            entity.dy += entity.velocity
        
        entity.velocity += jumpGravity
        entity.translate(self.dx * deltaTime, entity.dy * deltaTime)

    def exitState(self, entity) -> None:
        entity.hasCollision = False
        entity.collidingObjects = []
