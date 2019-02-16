from mapsite import MapSite


class Door(MapSite):
    def __init__(self, room1, room2):
        super().__init__()
        self._room1 = room1
        self._room2 = room2
        self._isOpen = False

    def enter():
        pass

    def other_side_from(room):
        pass
