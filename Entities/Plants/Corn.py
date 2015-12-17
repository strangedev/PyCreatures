"""

Corn module

"""

from Entities.Plants import Plant


class Corn(Plant.Plant):

    """

    Implementation of Plant class.
    Represents a corn plant.

    """

    def __init__(self):
        """

        Initialisation of the Corn object.

        """

        super().__init__()

        self._symbol = "C"
