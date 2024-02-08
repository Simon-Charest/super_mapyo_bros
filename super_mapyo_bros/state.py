from super_mapyo_bros.entity import Entity


class State(object):
    def enter_state(self, entity: Entity) -> None:
        raise NotImplementedError("Please Implement enter() in State subclass.")

    def execute(self, entity: Entity, delta_time) -> None:
        raise NotImplementedError("Please Implement execute() in State subclass.")

    def exit_state(self, entity: Entity) -> None:
        raise NotImplementedError("Please Implement exit() in State subclass.")
