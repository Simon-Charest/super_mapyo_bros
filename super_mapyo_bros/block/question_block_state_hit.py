from super_mapyo_bros.constants import *
from super_mapyo_bros.globals import *
from super_mapyo_bros.coin.coin import Coin
from super_mapyo_bros.power_up.mushroom import Mushroom
from super_mapyo_bros.state import State


class QuestionBlockStateHit(State):
    level = None

    def __init__(self, level) -> None:
        self.level = level
    
    def enterState(self, entity) -> None:
        entity.color = grey
        if not entity.used:
            entity.used = True

            if entity.contents == "coin":
                for obj in self.level.entities:
                    if isinstance(obj, Coin):
                        obj.setX(entity.x + 20)
                        obj.setY(entity.y - tileWidth)
                        obj.changeState("idle")

            elif entity.contents == "mushroom":
                for obj in self.level.entities:
                    if isinstance(obj, Mushroom):
                        obj.setX(entity.x)
                        obj.setY(entity.y)
                        obj.changeState("spawn")
                    
    def execute(self, entity, deltaTime) -> None:
        return

    def exitState(self, entity) -> None:
        return
