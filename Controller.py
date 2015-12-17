"""

Controller module

Provides high-level methods for world manipulation.

"""

import World
from Entities.Creatures import Mouse
from Entities.Plants import Corn

from random import choice


#  All implemented entity type classes are held in this dictionary
#  This allows for dynamic instantiation
ENTITY_TYPES = {"Mouse": Mouse.Mouse,
                "Corn": Corn.Corn}


class Controller(object):

    def __init__(self):
        """

        The initialisation of the Controller object.

        """

        self.world = None

    def new_world(self, width, height):
        """

        Creates a new world.

        """

        self.world = World.World(width, height)

    def next_cycle(self):
        """

        Advance the simulated world by 1 cycle.

        """

        self.world.compute_life_cycle()

    def print_map(self):
        """

        Prints out the world's map to the console.

        """

        print(self.world.draw_map())

    def spawn_entity(self, entity_type, x, y):
        """

        Adds a new instance of entity_type to the world at a certain location.

        """

        if entity_type in ENTITY_TYPES.keys():

            entity_class = ENTITY_TYPES[entity_type]

            self.world.add_thing(entity_class(), x, y)

    def spawn_at_random_pos(self, entity_type):
        """

        Adds a new instance of entity_type to the world at a random location.

        """

        free_coords = self.world.get_free_coords()

        if free_coords:

            self.spawn_entity(entity_type, *(choice(free_coords)))

    def spawn_multiple_at_random_pos(self, entity_type, amount):
        """

        Adds amount many instance of entity_type to the world at a random
        location.

        """

        for i in range(amount):

            self.spawn_at_random_pos(entity_type)
