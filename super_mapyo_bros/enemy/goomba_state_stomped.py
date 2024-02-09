
from pygame import Rect
from super_mapyo_bros.entity import Entity
from super_mapyo_bros.state import State
from typing import Type


class GoombaStateStomped(State):
    level: Type["LevelOneOne"]

    def __init__(self, level: Type["LevelOneOne"]) -> None:
        self.level = level

    def enter_state(self, entity: Entity) -> None:
        self.time = 0
        self.squishTime = 1000  # one second
        entity.y += entity.h/2
        entity.h /= 2
        entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)
        entity.is_dead = True

    def execute(self, entity: Entity, delta_time: int) -> None:
        self.time += delta_time
    
        # When time is up, switch to any state to remove goomba for good.
        if self.time > self.squishTime:
            entity.change_state("move")

    def exit_state(self, entity: Entity) -> None:
        entity.is_dead_dead = True
        self.level.remove_entity(entity)
