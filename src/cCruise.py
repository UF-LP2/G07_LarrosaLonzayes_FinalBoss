from cShip import cShip

class cCruise(cShip):
	def __init__(self, passengers, draft, crew):
		# Idem que en cCargo para usar super()
		super().__init__(draft, crew)
		
		self.passengers = passengers
		# Completar herencia