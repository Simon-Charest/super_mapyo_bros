from super_mapyo_bros.state import State


class CoinStateIdle(State):
    def enterState (self, entity) -> None:
        entity.active = True
        self.timer = 0
        self.delay = 1000

    def execute(self, entity, deltaTime) -> None:
        self.timer += deltaTime

        if self.timer > self.delay:
            entity.changeState("unused")

    def exitState(self, entity) -> None:
        return
