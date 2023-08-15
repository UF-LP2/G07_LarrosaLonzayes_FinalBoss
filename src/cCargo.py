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

		if self.draft < 0 or self.crew < 0 or self.cargo < 0 or self.quality < 0:
			# Si alguno de los 4 valores es negativo, hay un error logico importante
			raise ValueError("Lógica errónea")
		
		# DUDA -> hay casos donde hay una calidad definida, pero no hay carga extra
		# Faltaria chequear en los 3 casos si self.cargo != "" (vacio) ?
		if self.quality == 1 and self.cargo != "":
			aux = 3.5
		elif self.quality == 0.5 and self.cargo != "":
			aux = 2
		elif self.quality == 0.25 and self.cargo != "":
			aux = 0.5
		
		# Si la calidad es distinta a las otras 3, y hay carga registrada,
		# entonces es un valor invalido
		elif self.quality != "" and self.cargo != "":
			raise ValueError("Valor de calidad invalido")
		
		# Cualquier otro caso es un error logico (hay calidad valida pero no hay carga registrada por ej)
		else:
			raise ValueError("Error Logico")

		return float(self.draft - self.crew*1.5 - self.cargo*aux)
	
	def is_worth_it(self):
		# NOTA -> El print es solo para ver como estan cargados los datos de todos los cargueros
		# En la entrega lo borramos (o comentamos)
		aux = self.calcularPeso()
		# print("Cargo, Draft = %.2f," % self.draft, "Crew =  %.2f,"  % self.crew, "Extra =  %.2f," % self.cargo, "Quality = %.2f, " % self.quality, "Botin = %.2f" % aux)

		if (aux < 20.0):
			raise ValueError("I N S A Q U E A B L E")
		
		return aux