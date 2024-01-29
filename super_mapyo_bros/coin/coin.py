from super_mapyo_bros.coin.coin_state_idle import CoinStateIdle
from super_mapyo_bros.coin.coin_state_unused import CoinStateUnused
from super_mapyo_bros.entity import Entity


class Coin (Entity):
    def __init__(self, x, y, w, h, color) -> None:
        super().__init__(x, y, w, h, color)
        self.allStates = { "idle":CoinStateIdle(), "unused":CoinStateUnused() }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState
        self.active = False

    def update(self, deltaTime) -> None:
        if self.active:
            self.currState.execute(self, deltaTime)

    def draw(self, screen, camera) -> None:
        if self.active:
            super().draw(screen, camera)
