# Desarrollo del trabajo

# Se crea un nuevo objeto de barco basado en las observaciones de la tripulacion
# Barco1 = Ship(15, 10)

# Si ven el ingreso de un cargo al puerto, crearán un nuevo objeto de cargo
# Maersk = Cargo(15, 10)

# Si ven el ingreso de un crucero al puerto, crearán un nuevo objeto de crucero
# Titanic = Cruise(34, 15, 10)

class cShip:
	# NOTA -> podriamos hacer un static, para la cantidad total de barcos
	# Serviria para verificar si hace las cosas bien con el .csv
	cantidad = int(0)
	def __init__(self, draft, crew):
		self.draft = draft
		self.crew = crew
		cShip.cantidad += 1
		
	# Metodo polimorfico
	def calcularPeso(self):
		total = float(self.draft - self.crew*1.5)
		return total
	
	# True == Saqueable
	# False == ni te molestes
	def is_worth_it(self):
		# DUDA -> Toma el calcularPeso() de cShip, o de la clase hija donde se use?
		# Por las dudas la definimos tambien en todas las clases hijas
		botin = self.calcularPeso()
		if botin >= 20.0:
			return botin
		else:
			raise ValueError("Insaqueable como banco argentino")