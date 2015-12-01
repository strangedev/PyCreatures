"""
Plant Module
"""
import Thing


class Plant(Thing.Thing):

    """
    Plant class
    """

    def __init__(self):
        """
        """

        super().__init__()

        self.seed_cycle = 6

    def perform_action(self, world):

        super().perform_action()

        #  Reproduction
        if self.age % self.seed_cycle == 0:
            x, y = world.get_random_neighboring_free(*self._pos)

            if x == -1 and y == -1:
                return

            world.add_thing(self.__class__(), x, y)
