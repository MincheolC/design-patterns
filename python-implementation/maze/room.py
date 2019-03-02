from mapsite import MapSite
from direction import Direction


class Room(MapSite):
    def __init__(self, room_number=0):
        super().__init__()
        self._sides = {
            Direction.NORTH: None,
            Direction.SOUTH: None,
            Direction.EAST: None,
            Direction.SOUTH: None
        }
        self._room_number = room_number

    def get_side(self, direction):
        """ __getitem__ 사용 가능 """
        return self._sides[direction]

    def set_side(self, direction, mapsite):
        """ __setitem__ 사용 가능 """
        self._sides[direction] = mapsite

    def enter():
        pass

    def initialize(self, room_no):
        self._room_number = room_no

    def __repr__(self):
        return f"normal room {self._room_number}"


class RoomWithABomb(Room):
    def __init__(self, room_number=0):
        super().__init__(room_number)

    def __repr__(self):
        return f"room with a bomb {self._room_number}"


class EnchantedRoom(Room):
    def __init__(self, room_number=0, spell=""):
        super().__init__(room_number)
        self._spell = spell

    def __repr__(self):
        return f"enchanted room {self._room_number}"
