import World
import Thing
from Entities.Creatures import Mouse
from Entities.Plants import Corn
from time import sleep
from random import choice

ENTITY_TYPES = {"Mouse": Mouse.Mouse,
                "Corn": Corn.Corn}


class Controller(object):

    def __init__(self):

        self.world = None

    def new_world(self, width, height):

        self.world = World.World(width, height)

    def next_cycle(self):

        self.world.compute_life_cycle()

    def animate_cycles(self, cycle_amount, dt=0.1):

        for tick in range(cycle_amount):

            self.next_cycle()
            self.print_map()

            sleep(dt)

    def print_map(self):

        print(self.world.draw_map())

    def spawn_entity(self, entity_type, x, y):

        if entity_type in ENTITY_TYPES.keys():

            entity_class = ENTITY_TYPES[entity_type]

            self.world.add_thing(entity_class(), x, y)

    def spawn_at_random_pos(self, entity_type):

        free_coords = self.world.get_free_coords()

        if free_coords:

            self.spawn_entity(entity_type, *(choice(free_coords)))

    def spawn_multiple_at_random_pos(self, entity_type, amount):

        for i in range(amount):

            self.spawn_at_random_pos(entity_type)


