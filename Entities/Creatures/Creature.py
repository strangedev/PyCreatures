"""

Creature Module

"""

import Thing

from random import choice


class Creature(Thing.Thing):

    """

    Abstract superclass for all animal-like entities in the world.

    """

    def __init__(self):
        """

        Initialisation of the Creature object.

        """

        super().__init__()

        self.offspring_cycle = 12
        self.max_starving = 7
        self.max_age = 25
        self.starving = 0

    def perform_action(self, world):
        """

        The default perform_action method for all animal-like entities.
        Moves to adjacent positions containing food, moves randomly if
        no food is nearby.
        Removes entity from world if it dies of age or starvation.

        """

        super().perform_action()

        if self.age > self.max_age or self.starving > self.max_starving:
            world.remove_thing_at_coords(*self._pos)
            return

        if self.age % self.offspring_cycle == 0:
            self._reproduce(world)

        food_locations = self.find_food_locations(world)

        if food_locations:
            prey_location = choice(food_locations)

            world.move(self, *prey_location)

            self.starving = 0

            return

        free_location = world.get_random_neighboring_free(*self._pos)

        if free_location != (-1, -1):
            world.move(self, *free_location)

        self.starving += 1
