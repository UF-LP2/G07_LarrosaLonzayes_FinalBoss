import csv

from src.ships import Ship
from src.ships import Cargo
from src.ships import Cruise

# Por como armamos el programa, nos conviene definir una funcion booleana que identifique si su parametro es un numero o no
# En un try except casteamos 'n' a float, en caso de que NO sea un numero, tirará una exception sobre el tipo de dato y retornara false
# Podriamos haber usado tambien type(), pero era mas engorroso
def esNumero(n):
	try:
		float(n)
		return True
	except TypeError:
		return False


# NOTA -> cambiamos el nombre de la primera columna del .csv a "draft" (nos confundia)

def main() -> None:
	# Ojo con la columna extra que no solo corresponde al cargo, puede también ser de pasajeros. 
	listaBarcos = []

	# No hay que especificar la ruta del archivo, y la r es de read, solo lectura
	with open('ships.csv','r') as archivoBarcos:
		lectorBarcos = csv.reader(archivoBarcos)

		# next() hace avanzar una linea (fila) al lector de archivos, alteando asi los headers
		next(lectorBarcos)
		cant = 0

		# row es la columna de la fila en la que esté ubicado el lector
		for row in lectorBarcos:
			# lista.append agrega un elemento al listado, como push_back() en C++
			if row[2] == "" and row[3] == "" :
				if esNumero(row[0]) and esNumero(row[1]):
					# Como el try except ya esta hecho en esNumero(), no es necesario desarrollarlo acá
					barco1 = Ship(row[0], row[1])
					listaBarcos.append(barco1)
			
			elif row[2] != "" and row[3] == "" :
				if esNumero(row[0]) and esNumero(row[1]) and esNumero(row[2]):
					barco2 = Cruise(row[2], row[0], row[1])
					listaBarcos.append(barco2)

			elif row[2] != "" and row[3] != "" :
				if esNumero(row[0]) and esNumero(row[1]) and esNumero(row[2]) and esNumero(row[3]):
					barco3 = Cargo(row[2], row[3], row[0], row[1])
					listaBarcos.append(barco3)

			else:
				cant += 1
			# No estamos teniendo en cuenta los barcos mal puestos en la lista, solo los contamos
			# EJ: alguno que tenga 2000,1000,,1 por ejemplo
		
		# print("Hay un total de %d barcos registrados," % Ship.cantidad, "con %d mal pasados y sin registrar" % cant)

	# Al ser listaBarcos como un listado de C++,
	# hay que usar len() para saber la cantidad de items que posee, tal que 
	for i in range(len(listaBarcos)):
		print("Numero %d" % (i+1))
		try:
			auxBarco = listaBarcos[i]
			botin = float(auxBarco.is_worth_it())
			print("S A Q U E A B L E, " , "Botin = %.2f" % botin)
		except Exception as e:
			print(str(e))


if __name__ == "__main__":
	main()