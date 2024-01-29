class State(object):
    def enterState(self, entity) -> None:
        raise NotImplementedError("Please Implement enter() in State subclass.")

    def execute(self, entity, deltaTime) -> None:
        raise NotImplementedError("Please Implement execute() in State subclass.")

    def exitState(self, entity) -> None:
        raise NotImplementedError("Please Implement exit() in State subclass.")
