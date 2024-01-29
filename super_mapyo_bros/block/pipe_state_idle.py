from super_mapyo_bros.state import State


class PipeStateIdle(State):
    def enterState(self, entity) -> None:
        return

    def execute(self, entity, deltaTime) -> None:
        if entity.hasCollision:
            entity.hasCollision = False
            entity.collidingObjects = []
        
    def exitState(self, entity) -> None:
        return
