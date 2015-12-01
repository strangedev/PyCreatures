"""
"""


class World(object):

    """
    The world of things
    """

    map_width = 79
    map_height = 24

    def __init__(self):

        self.world_map = {}
        self.world_array = []

        for x in range(self.map_height):
            row = []

            for y in range(self.map_width):
                row.append(None)

            self.world_array.append(row)

    def compute_life_cycle(self):
        pass

    def print_map(self):
        """
        Map to ASCII method
        """
        map_str = ""

        for x in range(self.map_height):
            for y in range(self.map_width):

                thing = self.get_thing(x, y)

                map_str += thing.symbol if thing else "."

            map_str += "\n"

        return map_str

    def get_pos(self, thing):
        return self.world_map[thing]

    def get_thing(self, x, y):
        return self.world_array[x][y]

    def move(self, thing, pos):
        pass

    def get_neighbor(self, thing, direction):
        pass

    def add_thing(self, thing, x, y):

        # Keep reference of coords for thing
        coords = (x, y)
        key = thing.__hash__()

        self.world_map[key] = coords
        self.world_array[x][y] = thing

    def remove_thing(self, x, y):

        thing = self.get_thing(x, y)

        self.world_array[x].pop(y)
        del self.world_map[thing]

    def get_neighbor_coords(self, x, y, direction):
        pass
