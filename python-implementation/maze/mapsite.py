import abc


class MapSite:
    """ Maze에서 사용되는 다양한 구조(room, wall, door)등의 인터페이스 """

    @abc.abstractmethod
    def enter():
        raise NotImplementedError
