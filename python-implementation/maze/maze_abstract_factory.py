from direction import Direction
from door import Door, DoorNeedingSpell
from maze import Maze
from room import Room, RoomWithABomb, EnchantedRoom
from wall import Wall, BombedWall


class MazeFactory:
    @classmethod
    def make_maze(cls):
        return Maze()

    @classmethod
    def make_room(cls, room_number):
        return Room(room_number)

    @classmethod
    def make_wall(cls):
        return Wall()

    @classmethod
    def make_door(cls, r1, r2):
        return Door(r1, r2)

    def create_maze(cls):
        a_maze = cls.make_maze()
        r1 = cls.make_room(1)
        r2 = cls.make_room(2)
        the_door = cls.make_door(r1, r2)

        a_maze.add_room(r1)
        a_maze.add_room(r2)

        r1.set_side(Direction.NORTH, cls.make_wall())
        r1.set_side(Direction.EAST, the_door)
        r1.set_side(Direction.SOUTH, cls.make_wall())
        r1.set_side(Direction.WEST, cls.make_wall())

        r2.set_side(Direction.NORTH, cls.make_wall())
        r2.set_side(Direction.EAST, cls.make_wall())
        r2.set_side(Direction.SOUTH, cls.make_wall())
        r2.set_side(Direction.WEST, the_door)

        print("-------------------------------------------------------------")
        print(f'factory called:    {cls}')
        print(f'rooms created:     {r1}, {r2}')
        print(f'doors created:     {the_door}')

        return a_maze


class BombedMazeFactory(MazeFactory):
    @classmethod
    def make_wall(cls):
        return BombedWall()

    @classmethod
    def make_room(cls, room_number):
        return RoomWithABomb(room_number)


class EnchantedMazeFactory(MazeFactory):
    @classmethod
    def make_door(cls, room1, room2):
        return DoorNeedingSpell(room1, room2)

    @classmethod
    def make_room(cls, room_number):
        return EnchantedRoom(room_number)


if __name__ == "__main__":
    maze = MazeFactory()
    created_maze = maze.create_maze()

    """ factory method를 사용하면, 다른 create_maze 함수(client에서 실제로 호출하는
    인터페이스 역할)을 변경할 필요없이 다양한 MazeGame을 생성할 수 있다. """
    bombed_maze = BombedMazeFactory()
    created_bombed_maze = bombed_maze.create_maze()

    enchanted_maze = EnchantedMazeFactory()
    created_enchanted_maze = enchanted_maze.create_maze()
