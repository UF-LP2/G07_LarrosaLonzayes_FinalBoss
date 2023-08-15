from src.cShip import cShip

class cCargo(cShip):
	def __init__(self, cargo, quality, draft, crew):
		# Usando super(), no es necesario usar el nombre del elemento padre, 
		# sino que automaticamente heredará los metodos y propiedades de la clase padre
		super().__init__(draft, crew)
		self.cargo = cargo
		self.quality = quality

	def calcularPeso(self):
		total = float(self.draft - self.crew*1.5)

		# DUDA -> hay casos donde hay una calidad definida, pero no hay carga extra
		# Faltaria chequear en los 3 casos si self.cargo != "" (vacio) ?
		if self.quality == 1:
			total -= float(self.cargo*3.5)
		elif self.quality == 0.5:
			total -= float(self.cargo*2)
		elif self.quality == 0.25:
			total -= float(self.cargo*0.5)
		else:
			raise ValueError("Calidad de carga inválida")

		return total
	
	def is_worth_it(self):
		botin = self.calcularPeso()
		if botin >= 20:
			return botin
		else:
			raise ValueError("Insaqueable como banco argentino")