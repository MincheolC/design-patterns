from direction import Direction
from door import Door
from maze import Maze
from room import Room, RoomWithABomb
from wall import Wall, BombedWall


class MazeGame:
    """ Staticmethod: cls나 self에 접근할 수는 없다. regular function처럼 작동하지만
    class의 namespace에 속해서, 클래스 디자인을 명확하게 하기 위해 보통 사용 """

    @staticmethod
    def make_maze():
        return Maze()

    @staticmethod
    def make_room(room_number):
        return Room(room_number)

    @staticmethod
    def make_wall():
        return Wall()

    @staticmethod
    def make_door(r1, r2):
        return Door(r1, r2)

    def create_maze(self):
        a_maze = MazeGame.make_maze()
        r1 = MazeGame.make_room(1)
        r2 = MazeGame.make_room(2)
        the_door = MazeGame.make_door(r1, r2)

        a_maze.add_room(r1)
        a_maze.add_room(r2)

        r1.set_side(Direction.NORTH, MazeGame.make_wall())
        r1.set_side(Direction.EAST, the_door)
        r1.set_side(Direction.SOUTH, MazeGame.make_wall())
        r1.set_side(Direction.WEST, MazeGame.make_wall())

        r2.set_side(Direction.NORTH, MazeGame.make_wall())
        r2.set_side(Direction.EAST, MazeGame.make_wall())
        r2.set_side(Direction.SOUTH, MazeGame.make_wall())
        r2.set_side(Direction.WEST, the_door)

        return a_maze


class BombedMazeGame(MazeGame):

    @staticmethod
    def make_wall():
        return BombedWall()

    @staticmethod
    def make_room(room_number):
        return RoomWithABomb(room_number)


if __name__ == "__main__":
    # game = MazeGame()
    # created_maze = game.create_maze()

    game_with_bombed_maze = BombedMazeGame()
    created_bombed_maze = game_with_bombed_maze.create_maze()
