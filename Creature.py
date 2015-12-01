"""
Creature Module
"""
import Thing


class Creature(Thing.Thing):

    """
    """

    offspring_cycle = 12
    max_starving = 7
    max_age = 25

    def __init__(self):
        """
        """

        super.__init__()

        self.starving = 0
