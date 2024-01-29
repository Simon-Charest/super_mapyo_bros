class Struct(object):
    def __init__(self, **entries) -> None:
        self.__dict__.update(entries)
