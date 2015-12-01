"""
Thing Module
"""


class Thing(object):

    def __init__(self):
        """
        """

        self.__symbol = None
        self.__pos = (None, None)

    @property
    def symbol(self):
        return self.__symbol if self.__symbol else "."

    def perform_action(self):
        """
        """

        self.age += 1
