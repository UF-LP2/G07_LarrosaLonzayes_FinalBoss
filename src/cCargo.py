from cShip import cShip

class cCargo(cShip):
	def __init__(self, cargo, quality, draft, crew):
        # Usando super(), no es necesario usar el nombre del elemento padre, 
	    # sino que automaticamente heredará los metodos y propiedades de la clase padre
		super().__init__(draft, crew)
		
		self.cargo = cargo
		self.quality = quality
		# Completar herencia