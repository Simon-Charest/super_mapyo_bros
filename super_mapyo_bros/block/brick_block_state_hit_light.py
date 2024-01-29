class BrickBlockStateHitLight:
    def enterState(self, entity) -> None:
        self.done = False
        self.startY = entity.y
        self.maxY = entity.y - entity.h/2
        self.step = -0.2

    def execute(self, entity, deltaTime) -> None:
        entity.setY(entity.y + self.step * deltaTime)

        if entity.y <= self.maxY:
            self.step *= -1

        if entity.y >= self.startY:
            entity.setY(self.startY)
            entity.changeState("idle")

    def exitState(self, entity) -> None:
        return
