from Entities.Creatures import Creature
from Entities.Plants import Corn


class Mouse(Creature.Creature):

    """docstring for Mouse"""

    def __init__(self):

        super().__init__()

        self._symbol = "M"
        self.food_sources = [Corn.Corn]
