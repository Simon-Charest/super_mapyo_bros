from pygame import Surface
from super_mapyo_bros.camera import Camera
from super_mapyo_bros.coin.coin_state_idle import CoinStateIdle
from super_mapyo_bros.coin.coin_state_unused import CoinStateUnused
from super_mapyo_bros.entity import Entity


class Coin (Entity):
    def __init__(self, x, y, w, h, color) -> None:
        super().__init__(x, y, w, h, color)
        self.all_states = {
            "idle": CoinStateIdle(),
            "unused": CoinStateUnused()
        }
        self.prev_state = self.all_states.get("idle")
        self.curr_state = self.prev_state
        self.active = False

    def update(self, delta_time: int) -> None:
        if self.active:
            self.curr_state.execute(self, delta_time)

    def draw(self, screen: Surface, camera: Camera) -> None:
        if self.active:
            super().draw(screen, camera)
