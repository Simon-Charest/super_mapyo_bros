from super_mapyo_bros.level.level import Level


class LevelOneOne(Level):
    def __init__(self, fileHandle) -> None:
        Level.__init__(self, fileHandle)

    def update(self, deltaTime) -> None:
        Level.update(self, deltaTime)
        return
