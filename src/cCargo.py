from src.cShip import cShip

class cCargo(cShip):
	def __init__(self, cargo, quality, draft, crew):

		# Usando super(), no es necesario usar el nombre del elemento padre, 
		# sino que automaticamente heredará los metodos y propiedades de la clase padre
		
		super().__init__(draft, crew)

		if cargo != "":
			self.cargo = float(cargo)
		else:
			self.cargo = cargo
		
		if quality != "":
			self.quality = float(quality)
		else:
			self.crew = quality

	def calcularPeso(self):
		total = float()

		# DUDA -> hay casos donde hay una calidad definida, pero no hay carga extra
		# Faltaria chequear en los 3 casos si self.cargo != "" (vacio) ?
		if self.quality == 1:
			aux = 3.5
		elif self.quality == 0.5:
			aux = 2
		elif self.quality == 0.25:
			aux = 0.5
		else:
			print("Cargo, Calidad de carga inválida")
			raise ValueError("Calidad de carga inválida")

		return float(self.draft - self.crew*1.5 - self.cargo*aux)
	
	def is_worth_it(self):
		# NOTA -> El print es solo para ver como estan cargados los datos de todos los cargueros
		# En la entrega lo borramos (o comentamos)
		aux = self.calcularPeso()
		print("Cargo, Draft = %.2f," % self.draft, "Crew =  %.2f,"  % self.crew, "Extra =  %.2f," % self.cargo, "Quality = %.2f, " % self.quality, "Botin = %.2f" % aux)

		if (aux < 20.0):
			raise ValueError("Insaqueable como banco argentino")
		
		return aux