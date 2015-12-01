"""
Creature Module
"""
import Thing

class Creature(Thing.Thing):

	"""
	"""

	offspring_cycle = None
	starving = None
	max_starving = None
	max_age = None

	def __init__(self):

		"""
		"""

		super.__init__()

