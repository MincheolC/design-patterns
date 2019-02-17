"""
Prototype pattern in python

# https://en.proft.me/2016/09/27/prototype-design-pattern-java-and-python/
When to use:

* when the classes to instantiate are specified at run-time, for example,
  by dynamic loading;
* to avoid building a class hierarchy of factories that parallels the class
  hierarchy of products;
* when instances of a class can have one of only a few different combinations
  of state. It may be more convenient to install a corresponding number of
  prototypes and clone them rather than instantiating the class manually, each
  time with the appropriate state.

The main advantages of prototype pattern are as follows:

* It reduces the need of sub-classing.
* It hides complexities of creating objects.
* The clients can get new objects without knowing which type of object it
  will be.
* It lets you add or remove objects at runtime.
"""

from direction import Direction
from door import Door
from maze import Maze
from room import Room, RoomWithABomb
from wall import Wall, BombedWall


class MazeFactory:
    @staticmethod
    def make_maze():
        return Maze()

    @staticmethod
    def make_wall():
        return Wall()

    @staticmethod
    def make_room(room_number):
        return Room(room_number)

    @staticmethod
    def make_door(r1, r2):
        return Door(r1, r2)

    @classmethod
    def create_maze(cls, maze_game_prototype_factory):
        a_maze = maze_game_prototype_factory.make_maze()
        r1 = maze_game_prototype_factory.make_room(1)
        r2 = maze_game_prototype_factory.make_room(2)
        the_door = maze_game_prototype_factory.make_door(r1, r2)

        a_maze.add_room(r1)
        a_maze.add_room(r2)

        r1.set_side(Direction.NORTH, maze_game_prototype_factory.make_wall())
        r1.set_side(Direction.EAST, the_door)
        r1.set_side(Direction.SOUTH, maze_game_prototype_factory.make_wall())
        r1.set_side(Direction.WEST, maze_game_prototype_factory.make_wall())

        r2.set_side(Direction.NORTH, maze_game_prototype_factory.make_wall())
        r2.set_side(Direction.EAST, maze_game_prototype_factory.make_wall())
        r2.set_side(Direction.SOUTH, maze_game_prototype_factory.make_wall())
        r2.set_side(Direction.WEST, the_door)

        return a_maze


class MazePrototypeFactory(MazeFactory):
    def __init__(self, maze=None, wall=None, room=None, door=None):
        super().__init__()
        self._maze = maze
        self._wall = wall
        self._room = room
        self._door = door

    def make_maze(self):
        maze = self._maze.clone()
        return maze

    def make_room(self, room_no):
        room = self._room.clone()
        room.initialize(room_no)
        return room

    def make_wall(self):
        wall = self._wall.clone()
        return wall

    def make_door(self, r1, r2):
        door = self._door.clone()
        door.initialize(r1, r2)
        return door


if __name__ == "__main__":
    game = MazeFactory()
    maze_game_prototype_factory = MazePrototypeFactory(
        maze=Maze(), wall=Wall(), room=Room(), door=Door())
    created_maze = game.create_maze(maze_game_prototype_factory)

    bombed_game_prototype_factory = MazePrototypeFactory(
        maze=Maze(), wall=BombedWall(), room=RoomWithABomb(), door=Door())
    created_bombed_maze = game.create_maze(bombed_game_prototype_factory)
