from super_mapyo_bros.state import State


class EnemyStateWait(State):
    def enterState(self, entity) -> None:
        return

    def execute(self, entity, deltaTime, x: int = -1) -> None:
        """self.level.getMario().x"""
        
        # Wait until player reaches some X position on the
        # level before updating and drawing this enemy instance.
        if x > -1 and x > entity.spawnX:
            entity.changeState("move")

    def exitState(self, entity) -> None:
        entity.isSpawned = True
