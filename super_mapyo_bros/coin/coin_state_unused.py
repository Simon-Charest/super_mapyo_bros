from sre_parse import State


class CoinStateUnused(State):
    def enterState(self, entity) -> None:
       entity.setX(-100)
       entity.setY(0)
       entity.active = False

    def execute(self, entity, deltaTime) -> None:
        return

    def exitState(self, entity) -> None:
        return
