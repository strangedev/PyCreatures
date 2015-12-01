"""
Thing Module
"""


class Thing(object):

    def __init__(self):
        """
        """

        self._symbol = "T"
        self._pos = (None, None)
        self.age = 0

    @property
    def symbol(self):
        return self._symbol if self._symbol else "."

    def perform_action(self):
        """
        """

        self.age += 1

    def set_pos(self, pos):
        self._pos = pos
