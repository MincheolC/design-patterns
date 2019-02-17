from mapsite import MapSite


class Wall(MapSite):
    def __init__(self):
        super().__init__()

    def enter():
        pass

    def __repr__(self):
        return "normal wall"


class BombedWall(Wall):
    def __init__(self):
        super().__init__()

    def enter():
        pass

    def __repr__(self):
        return "bombed wall"
