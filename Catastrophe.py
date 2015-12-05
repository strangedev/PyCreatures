class Catastrophe(object):

    """docstring for Catastrophe"""

    def __init__(self):
        super().__init__()

        self.spawn_location = "ALL"
        self._symbol = "ϟ"
        self._pos = (None, None)
        self.max_duration = 50
        self.duration = 0

    @property
    def symbol(self):
        return self._symbol if self._symbol else "."

    def set_pos(self, pos):
        self._pos = pos

    def perform_action(self):

        self.duration += 1
