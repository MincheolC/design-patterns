"""
https://yamalab.tistory.com/74

class MazeFactory:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls(*args, **kwargs)
            cls.instance = cls._getInstance
        return cls._instance
"""


class MazeFactory:
    _instance = None

    @classmethod
    def instance(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls(*args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    game1 = MazeFactory.instance()
    game2 = MazeFactory.instance()
    assert(game1 == game2)
    print(game1)
    print(game2)
