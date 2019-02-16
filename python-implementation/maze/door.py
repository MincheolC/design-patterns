from mapsite import MapSite


class Door(MapSite):
    def __init__(self, room1=None, room2=None):
        super().__init__()
        self._room1 = room1
        self._room2 = room2
        self._isOpen = False

    def enter():
        pass

    def other_side_from(room):
        pass

    def initialize(self, r1, r2):
        self._room1 = r1
        self._room1 = r2
