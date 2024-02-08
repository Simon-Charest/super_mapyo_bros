from super_mapyo_bros.level.level import Level


class LevelOneOne(Level):
    def __init__(self, fileHandle) -> None:
        Level.__init__(self, fileHandle)

    def update(self, delta_time) -> None:
        Level.update(self, delta_time)
        return
