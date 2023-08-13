from cShip import cShip

class cCargo(cShip):
	def __init__(self, cargo, quality, draft, crew):
		# Usando super(), no es necesario usar el nombre del elemento padre, 
		# sino que automaticamente heredará los metodos y propiedades de la clase padre
		super().__init__(draft, crew)
		self.cargo = cargo
		self.quality = quality

	def calcularPeso(self):
		total = self.draft - self.crew*1.5
		aux = 0

		if self.quality == 1:
			aux -= 3.5
		elif self.quality == 0.5:
			aux -= 2
		elif self.quality == 0.25:
			aux -= 0.5
		else:
			raise ValueError("Calidad de carga inválida")

		total -= (self.cargo * aux)
		return total