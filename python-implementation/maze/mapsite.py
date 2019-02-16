import copy
import abc


class MapSite:
    """ Maze에서 사용되는 다양한 구조(room, wall, door)등의 인터페이스 """

    @abc.abstractmethod
    def enter():
        raise NotImplementedError

    def clone(self):
        """ prototype에서 사용. 추상메소드로 구현하고 subclass 에서
            override하게도 할 수 있으나 귀찮아서...ㅎㅎ
        """
        return copy.deepcopy(self)
