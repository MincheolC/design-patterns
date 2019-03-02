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

    @property
    def is_open(self):
        return self._isOpen

    def open(self):
        self._open = True
        print("The door is opened")


class DoorNeedingSpell(Door):
    def __init__(self, room1=None, room2=None):
        super().__init__(room1, room2)

    def open(self, with_spell=False):
        if with_spell:
            super().open()
        print("Door needs spell to open")
