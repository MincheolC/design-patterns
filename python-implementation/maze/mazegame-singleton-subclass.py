import os

from maze_abstract_factory import (BombedMazeFactory, EnchantedMazeFactory)


class MazeFactory:
    """
    .env 파일에 설정된 MAZE_STYLE 환경변수에 따라 다른 팩토리 인스턴스 생성
    """
    _instance = None

    @classmethod
    def instance(cls, *args, **kwargs):
        if not cls._instance:
            MAZE_STYLE = os.getenv("MAZE_STYLE", None)

            if MAZE_STYLE == "bombed":
                cls._instance = BombedMazeFactory(*args, **kwargs)

            elif MAZE_STYLE == "enchanted":
                cls._instance = EnchantedMazeFactory(*args, **kwargs)

            else:
                " other possibilities...."
                cls._instance = cls(*args, **kwargs)

        return cls._instance


if __name__ == "__main__":
    game1 = MazeFactory.instance()
    game2 = MazeFactory.instance()
    assert (game1 == game2)
    print(game1)
    print(game2)
