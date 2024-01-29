from super_mapyo_bros.entity import Entity
from super_mapyo_bros.power_up.mushroom_state_fall import MushroomStateFall
from super_mapyo_bros.power_up.mushroom_state_move import MushroomStateMove
from super_mapyo_bros.power_up.mushroom_state_spawn import MushroomStateSpawn


class Mushroom(Entity):
    def __init__(self, x, y, w, h, color) -> None:
        super().__init__(x, y, w, h, color)
        self.allStates = {
            "spawn": MushroomStateSpawn(),
            "move": MushroomStateMove(),
            "fall": MushroomStateFall() }
        self.prevState = self.allStates.get("spawn")
        self.currState = self.prevState
        self.active = False
        self.dy = 0
        self.velocity = 0

    def update(self, deltaTime) -> None:
        if self.active:
            self.currState.execute(self, deltaTime)

    def draw(self, screen, camera) -> None:
        if self.active:
            super().draw(self)
