from typing import Type


class State(object):
    def enter_state(self, entity: Type["Entity"]) -> None:
        raise NotImplementedError("Please Implement enter() in State subclass.")

    def execute(self, entity: Type["Entity"], delta_time: int) -> None:
        raise NotImplementedError("Please Implement execute() in State subclass.")

    def exit_state(self, entity: Type["Entity"]) -> None:
        raise NotImplementedError("Please Implement exit() in State subclass.")
