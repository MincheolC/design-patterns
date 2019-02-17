from direction import Direction
from door import Door
from maze import Maze
from room import Room
from wall import Wall


class MazeGame:
    def create_maze(self):
        a_maze = Maze()
        r1 = Room(1)
        r2 = Room(2)
        the_door = Door(r1, r2)

        a_maze.add_room(r1)
        a_maze.add_room(r2)

        r1.set_side(Direction.NORTH, Wall())
        r1.set_side(Direction.EAST, the_door)
        r1.set_side(Direction.SOUTH, Wall())
        r1.set_side(Direction.WEST, Wall())

        r2.set_side(Direction.NORTH, Wall())
        r2.set_side(Direction.EAST, Wall())
        r2.set_side(Direction.SOUTH, Wall())
        r2.set_side(Direction.WEST, the_door)

        return a_maze


if __name__ == "__main__":
    game = MazeGame()
    created_maze = game.create_maze()