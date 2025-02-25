from super_mapyo_bros.entity import Entity
from super_mapyo_bros.state import State


class EnemyStateWait(State):
    def enter_state(self, entity: Entity) -> None:
        return

    def execute(self, entity, delta_time: int, x: int = -1) -> None:
        """self.level.get_mario().x"""
        
        # Wait until player reaches some X position on the
        # level before updating and drawing this enemy instance.
        if x > -1 and x > entity.spawn_x:
            entity.change_state("move")

    def exit_state(self, entity: Entity) -> None:
        entity.is_spawned = True
