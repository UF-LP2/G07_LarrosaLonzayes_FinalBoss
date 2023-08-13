from cShip import cShip

class cCruise(cShip):
	def __init__(self, passengers, draft, crew):
		# Idem que en cCargo para usar super()
		super().__init__(draft, crew)
		
		self.passengers = passengers
		
	def calcularPeso(self):
		total = self.draft - self.crew * 1.5
		
		# Cada pasajero agrega 2.25
		aux = self.passengers * 2.25

		totel -= aux
		return aux