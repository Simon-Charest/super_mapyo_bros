from pygame import Surface
from super_mapyo_bros.camera import Camera
from super_mapyo_bros.entity import Entity
from super_mapyo_bros.power_up.mushroom_state_fall import MushroomStateFall
from super_mapyo_bros.power_up.mushroom_state_move import MushroomStateMove
from super_mapyo_bros.power_up.mushroom_state_spawn import MushroomStateSpawn


class Mushroom(Entity):
    def __init__(self, x, y, w, h, color, level) -> None:
        super().__init__(x, y, w, h, color)
        self.all_states = {
            "spawn": MushroomStateSpawn(),
            "move": MushroomStateMove(level),
            "fall": MushroomStateFall() }
        self.prev_state = self.all_states.get("spawn")
        self.curr_state = self.prev_state
        self.active = False
        self.dy = 0
        self.velocity = 0

    def update(self, delta_time) -> None:
        if self.active:
            self.curr_state.execute(self, delta_time)

    def draw(self, screen: Surface, camera: Camera) -> None:
        if self.active:
            super().draw(screen, camera)
