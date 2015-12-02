"""
"""
from random import choice

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class World(object):

    """
    The world of things
    """

    def __init__(self, width=79, height=24):

        self.world_map = {}
        self.world_array = []

        self.map_width = width
        self.map_height = height

        for y in range(self.map_height):
            row = []

            for x in range(self.map_width):
                row.append(None)

            self.world_array.append(row)

    def draw_map(self):
        """
        Map to ASCII method
        """
        map_str = ""

        for y in range(self.map_height):
            for x in range(self.map_width):

                thing = self.get_thing(x, y)

                map_str += thing.symbol if thing else "."

            map_str += "\n"

        return map_str

    def compute_life_cycle(self):

        things = list(self.world_map.items())

        for item in things:
            thing, coord = item

            if thing in self.world_map.keys():

                thing.perform_action(self)

    def get_pos(self, thing):
        return self.world_map[thing]

    def get_thing(self, x, y):
        return self.world_array[y][x]

    def move(self, thing, x, y):

        x_old, y_old = self.get_pos(thing)

        self.remove_thing_at_coords(x_old, y_old)
        self.remove_thing_at_coords(x, y)

        self.add_thing(thing, x, y)

    def add_thing(self, thing, x, y):

        # Keep reference of coords for thing
        coords = (x, y)
        thing.set_pos(coords)

        self.world_map[thing] = coords
        self.world_array[y][x] = thing

    def remove_thing(self, thing):

        x, y = self.get_pos(thing)

        self.remove_thing_at_coords(x, y)

    def remove_thing_at_coords(self, x, y):

        thing = self.get_thing(x, y)

        if thing is None:
            return

        self.world_array[y][x] = None
        del self.world_map[thing]

    def get_neighbor(self, thing, direction):

        x, y = self.world_map[thing]

        return self.get_neighbor_from_coords(x, y)

    def get_neighbor_from_coords(self, x, y, direction):

        x, y = self.get_neighboring_coords(x, y, direction)

        return self.get_thing(x, y)

    def get_random_neighboring_free(self, x, y):

        neighbors = self.get_all_neighbors_from_coords(x, y)

        neighbors = tuple(filter(lambda x: x[0] is None, neighbors))

        if not neighbors:
            return (-1, -1)

        return choice(neighbors)[1]

    def get_all_neighbors_from_coords(self, x, y):

        neighboring_positions = [NORTH, EAST, SOUTH, WEST]

        neighbors = []

        for pos in neighboring_positions:

            neighbor_pos = self.get_neighboring_coords(x, y, pos)

            neighbor = (self.get_thing(*neighbor_pos), neighbor_pos)
            neighbors.append(neighbor)

        return neighbors

    def get_neighboring_coords(self, x, y, direction):

        x_offset = 0
        y_offset = 0

        if direction is NORTH:
            y_offset = -1
        elif direction is EAST:
            x_offset = 1
        elif direction is SOUTH:
            y_offset = 1
        elif direction is WEST:
            x_offset = -1

        neighbor_x = (x + x_offset) % self.map_width
        neighbor_y = (y + y_offset) % self.map_height

        return (neighbor_x, neighbor_y)
