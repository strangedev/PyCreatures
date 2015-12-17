"""

Plant Module

"""
import Thing


class Plant(Thing.Thing):

    """

    Abstract superclass for all Plant-like entities in the world.

    """

    def __init__(self):
        """

        Initialisation of the Plant object.

        """

        super().__init__()

        self.seed_cycle = 6

    def perform_action(self, world):
        """

        The default perform_action method for all plants.
        Reproduces entity after seed_cycle many cycles.

        """

        super().perform_action()

        if self.age % self.seed_cycle == 0:
            self._reproduce(world)
