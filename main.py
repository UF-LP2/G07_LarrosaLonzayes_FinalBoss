import csv

from src.cShip import cShip
from src.cCargo import cCargo
from src.cCruise import cShip

# Usamos las clases desde sus archivos individuales
# DUDA -> Nos conviene hacer un solo archivo de tests o con 3 está bien? (uno por clase)

# NOTA -> cambiamos el nombre de la primera columna del .csv a "draft" (nos confundia)

def main() -> None:
	# Imprime 0
	print(cShip.cantidad) 

	# Ojo con la columna extra que no solo corresponde al cargo, puede también ser pasajeros. 
	# Fíjarse cuando actúa como cargo y cuando como pasajero. 





if __name__ == "__main__":
	main()
