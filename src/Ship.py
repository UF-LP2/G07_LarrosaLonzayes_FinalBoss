class Ship:

	# NOTA -> hicimos un static, para la cantidad total de barcos
	# Serviria para verificar si el programa hace las cosas bien con el .csv

	cantidad = 0
	def __init__(self, draft, crew):
		if draft != "":
			self.draft = float(draft)
		else:
			raise ValueError("Esta en blanco")
		
		if crew != "":
			self.crew = float(crew)
		else:
			raise ValueError("Esta en blanco")
		
		Ship.cantidad += 1

	# Metodo polimorfico
	def calcularPeso(self):
		# Si alguno de ambos valores es negativo, hay un error logico importante
		if self.draft < 0 or self.crew < 0:
			raise ValueError("Lógica errónea")
		
		return float(self.draft - self.crew*1.5)
	
	def is_worth_it(self):
		# NOTA -> El print es solo para ver como estan cargados los datos de todos los barcos genericos
		# En la entrega lo borramos (o comentamos)
		aux = float(self.draft - self.crew*1.5)
		# print("Barco, Draft = %.2f," % self.draft, "Crew =  %.2f, " % self.crew, "Botin = %.2f" % aux)
		
		if (aux < 20.0):
			raise ValueError("I N S A Q U E A B L E")
		
		return aux