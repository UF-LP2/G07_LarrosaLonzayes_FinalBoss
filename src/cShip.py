# Desarrollo del trabajo

# Se crea un nuevo objeto de barco basado en las observaciones de la tripulacion
# Barco1 = Ship(15, 10)

# Si ven el ingreso de un cargo al puerto, crearán un nuevo objeto de cargo
# Maersk = Cargo(15, 10)

# Si ven el ingreso de un crucero al puerto, crearán un nuevo objeto de crucero
# Titanic = Cruise(34, 15, 10)

# Tienes acceso a los atributos "draft" (borrador) y "crew" (tripulación) del barco. 
# "Draft" == peso total del barco
# "Crew" == número de personas trabajando en el barco.
# Cada miembro de la tripulación agrega 1.5 unidades al borrador
# El cargo agrega 3.5 si la calidad es 1, agrega 2 si la calidad es 0.5 y agrega 0.5 si la calidad es 0.25
# Un pasajero agrega 2.25 (exclusivo de cruceros)
# Luego de restar el peso de tripulacion (y de pasajeros en los cruceros), si sigue siendo >=20, hay que saquear

# Agrega este metodo, para decidir si el barco merece ser saqueado:
# is_worth_it(...)

# Las clases Cargo y Cruise son hijas de Ship

class cShip:
	def __init__(self, draft, crew):
		self.draft = draft
		self.crew = crew
		
	# Metodo polimorfico
	def calcularPeso(self):
		pesoAux = float(self.draft - self.crew*1.5)
		return pesoAux
	
	# True == Saqueable
	# False == ni te molestes
	def is_worth_it(self):
		# DUDA -> Toma el calcularPeso() de cShip, o de la clase hija donde se use?
		# Por las dudas la definimos tambien en todas las clases hijas
		if self.calcularPeso() >= 20.0:
			return True
		else:
			return False