from super_mapyo_bros.level.level import Level


class LevelOneOne(Level):
    def __init__(self, file_handle) -> None:
        Level.__init__(self, file_handle)

    def update(self, delta_time: int) -> None:
        Level.update(self, delta_time)
        
        return
