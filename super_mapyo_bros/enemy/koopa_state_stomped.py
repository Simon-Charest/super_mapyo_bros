from super_mapyo_bros.state import State


class KoopaStateStomped(State):
    def enterState(self, entity) -> None:
        self.time = 0
        self.recoverTime = 5000 # five seconds

        if entity.inShell == False:
            entity.y += entity.h/2
            entity.h /= 2
            entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)

        entity.inShell = True
        entity.isDead = True

    def execute(self, entity, deltaTime) -> None:
        self.time += deltaTime

        # Come back out of shell.
        if self.time > self.recoverTime:
            entity.isDead = False
            entity.inShell = False
            entity.changeState("move")
            entity.y -= entity.h*2
            entity.h *= 2
            entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)
            return

        # Otherwise check for mario hitting it in some direction.
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                if isinstance(tile, Mario):
                    # Decide which way to shoot shell.
                    if tile.x <= entity.x:
                        entity.direction = "right"
                    else:
                        entity.direction = "left"
                    # Shoot shell.
                    entity.isDead = False
                    entity.changeState("shellMove")

            entity.hasCollision = False
            entity.collidingObjects = []

    def exitState(self, entity) -> None:
        return
