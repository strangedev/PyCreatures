"""

Thing Module

"""


class Thing(object):

    """

    Abstract superclass for all entities in the world.

    """

    def __init__(self):
        """

        The inialisation of the thing object.

        """

        self._symbol = "T"
        self._pos = (None, None)
        self.age = 0
        self.food_sources = []

    @property
    def symbol(self):
        """

        A getter for symbol that returns a '.' if no symbol set.

        """

        return self._symbol if self._symbol else "."

    def set_pos(self, pos):
        """

        A setter for position

        """

        self._pos = pos

    def perform_action(self):
        """

        The default perform action method that increments age.

        """

        self.age += 1

    def find_food_locations(self, world):
        """

        Checks if neighbors are in fact food and returns their locations.

        """

        neighbors = world.get_all_neighbors_from_coords(*self._pos)

        food_locations = []

        for neighbor, coord in neighbors:

            if neighbor.__class__ in self.food_sources:
                food_locations.append(coord)

        return food_locations

    def _reproduce(self, world):
        """

        Determins how a thing reproduces.

        """

        x, y = world.get_random_neighboring_free(*self._pos)

        if x == -1 and y == -1:
            return

        world.add_thing(self.__class__(), x, y)
