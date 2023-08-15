import csv

from src.cShip import cShip
from src.cCargo import cCargo
from src.cCruise import cCruise

# Usamos las clases desde sus archivos individuales
# DUDA -> Nos conviene hacer un solo archivo de tests o con 3 está bien? (uno por clase)

# NOTA -> cambiamos el nombre de la primera columna del .csv a "draft" (nos confundia)

def main() -> None:
	# Ojo con la columna extra que no solo corresponde al cargo, puede también ser pasajeros. 
	# Fíjarse cuando actúa como cargo y cuando como pasajero. 

	listaBarcos = []

	# No hay que especificar la ruta del archivo, y la r es de read, solo lectura, 
	with open('ships.csv','r') as archivoBarcos:
		lectorBarcos = csv.reader(archivoBarcos)

		# next() hace avanzar una linea al lector de archivos,
		# salteando asi los headers
		next(lectorBarcos)
		cant = 0
		# row es la columna de la fila en la que esté ubicado el lector
		for row in lectorBarcos:
			# lista.append agrega un elemento al listado, como push_back() en C++
			if row[2] == "" and row[3] == "" :
				barco1 = cShip(row[0], row[1])
				listaBarcos.append(barco1)
			
			elif row[2] != "" and row[3] == "" :
				barco2 = cCruise(row[2], row[0], row[1])
				listaBarcos.append(barco2)

			elif row[2] != "" and row[3] != "" :
				barco3 = cCargo(row[2], row[3], row[0], row[1])
				listaBarcos.append(barco3)

			else:
				cant += 1
			# No estamos teniendo en cuenta los barcos mal puestos en la lista, solo los contamos
			# EJ: alguno que tenga 2000,1000,,1 por ejemplo
		
		print("Hay un total de %d barcos registrados," % cShip.cantidad, "con %d mal pasados y sin registrar" % cant)

	# Al ser listaBarcos como un listado de C++,
	# hay que usar len() para saber la cantidad de items que posee
	for i in range(len(listaBarcos)):
		# NOTA y DUDA -> Siempre tira exception, no importa el barco, POR QUE?
		# corregir y aprender como debbugear
		try:
			auxBarco = listaBarcos[i]
			botin = float(auxBarco.is_worth_it())
			print("El N°%d es S A Q U E A B L E, "  % i+1, "Botin = %.2f" % botin)
		except Exception:
			print("I N S A Q U E A B L E")


if __name__ == "__main__":
	main()