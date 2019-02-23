import os


class MazeFactorySingleton:
    """
    Registry of Singleton
    """
    _instance = None
    _registry = {}

    @classmethod
    def instance(cls):
        if not cls._instance:
            SINGLETON_NAME = os.getenv("SINGLETON", None)
            cls._instance = cls._lookup(SINGLETON_NAME)

        return cls._instance

    @classmethod
    def register(cls, name, singleton):
        cls._registry[name] = singleton

    @classmethod
    def _lookup(cls, singleton_name):
        cls._instance = cls._registry.get(singleton_name, 0)
        return cls._instance


class EnchantedMazeFactorySingleton(MazeFactorySingleton):

    @classmethod
    def instance(cls):
        MazeFactorySingleton.register("EnchantedMazeFactory", cls())
        return super().instance()


if __name__ == "__main__":
    enchanted_maze_factory_singleton = EnchantedMazeFactorySingleton.instance()
    print("asdasdasdasdasdasd")
    MazeFactorySingleton.register("EnchantedMazeFactory", enchanted_maze_factory_singleton)
    maze_factory_singleton = MazeFactorySingleton.instance()
    assert (enchanted_maze_factory_singleton == maze_factory_singleton)
    print(id(enchanted_maze_factory_singleton), enchanted_maze_factory_singleton)
    print(id(maze_factory_singleton), maze_factory_singleton)
