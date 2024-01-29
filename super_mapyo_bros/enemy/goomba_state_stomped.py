from super_mapyo_bros.state import State


class GoombaStateStomped(State):
    def enterState(self, entity) -> None:
        self.time = 0
        self.squishTime = 1000 # one second
        entity.y += entity.h/2
        entity.h /= 2
        entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)
        entity.isDead = True

    def execute(self, entity, deltaTime) -> None:
        self.time += deltaTime

        # When time is up, switch to any state to remove goomba for good.
        if self.time > self.squishTime:
            entity.changeState("move")

    def exitState(self, entity) -> None:
        entity.isDeadDead = True
        level.removeEntity(entity)
