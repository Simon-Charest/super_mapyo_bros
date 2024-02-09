from super_mapyo_bros.constants import *
from super_mapyo_bros.globals import *
from super_mapyo_bros.coin.coin import Coin
from super_mapyo_bros.power_up.mushroom import Mushroom
from super_mapyo_bros.state import State


class QuestionBlockStateHit(State):
    level = None

    def __init__(self, level) -> None:
        self.level = level
    
    def enter_state(self, entity) -> None:
        entity.color = grey
        
        if not entity.used:
            entity.used = True

            if entity.contents == "coin":
                for obj in self.level.entities:
                    if isinstance(obj, Coin):
                        obj.set_x(entity.x + 20)
                        obj.set_y(entity.y - tile_width)
                        obj.change_state("idle")

            elif entity.contents == "mushroom":
                for obj in self.level.entities:
                    if isinstance(obj, Mushroom):
                        obj.set_x(entity.x)
                        obj.set_y(entity.y)
                        obj.change_state("spawn")
                    
    def execute(self, entity, delta_time: int) -> None:
        return

    def exit_state(self, entity) -> None:
        return
