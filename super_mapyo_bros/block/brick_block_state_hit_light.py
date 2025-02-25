from super_mapyo_bros.entity import Entity


class BrickBlockStateHitLight:
    def enter_state(self, entity: Entity) -> None:
        self.done = False
        self.startY = entity.y
        self.maxY = entity.y - entity.h/2
        self.step = -0.2

    def execute(self, entity: Entity, delta_time: int) -> None:
        entity.set_y(entity.y + self.step * delta_time)

        if entity.y <= self.maxY:
            self.step *= -1

        if entity.y >= self.startY:
            entity.set_y(self.startY)
            entity.change_state("idle")

    def exit_state(self, entity: Entity) -> None:
        return
