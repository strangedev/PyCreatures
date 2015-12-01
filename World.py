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

    def compute_life_cycle(self):
        pass

    def print_map(self):
        pass

    def get_pos(self, thing):
        pass

    def move(self, this, pos):
        pass
