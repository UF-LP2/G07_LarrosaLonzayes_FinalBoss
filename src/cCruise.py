from src.cShip import cShip

class cCruise(cShip):
	def __init__(self, passengers, draft, crew):
		# Idem que en cCargo para usar super()
		super().__init__(draft, crew)
		
		if passengers != "":
			self.passengers = float(passengers)
		else:
			self.passengers = passengers
		
		
	def calcularPeso(self):
		return float(self.draft - self.crew*1.5 - self.passengers*2.25)
	
	def is_worth_it(self):
		# NOTA -> El print es solo para ver como estan cargados los datos de todos los cruceros
		# En la entrega lo borramos (o comentamos)
		aux = self.calcularPeso()
		# print("Crucero, Draft = %.2f," % self.draft, "Crew =  %.2f," % self.crew ,"Passengers =  %.2f, " % self.passengers, "Botin = %.2f" % aux)

		if (aux >= 0) and (aux < 20.0):
			raise ValueError("I N S A Q U E A B L E")
		elif (aux < 0):
			raise ValueError("BOTIN INVALIDO COMO YO")
		
		return aux