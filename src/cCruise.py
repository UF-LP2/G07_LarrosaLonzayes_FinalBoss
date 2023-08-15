from src.cShip import cShip

class cCruise(cShip):
	def __init__(self, passengers, draft, crew):
		# Idem que en cCargo para usar super()
		super().__init__(draft, crew)
		
		self.passengers = passengers
		
	def calcularPeso(self):
		total = float(self.draft - self.crew * 1.5)
		
		# Cada pasajero agrega 2.25
		aux = float(self.passengers * 2.25)

		total -= aux
		return total
	
	def is_worth_it(self):
		botin = self.calcularPeso()
		if botin >= 20:
			return botin
		else:
			raise ValueError("Insaqueable como banco argentino")