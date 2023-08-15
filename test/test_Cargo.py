import pytest

from src.ships import Cargo

# Caso de cargo saqueable
def testCargo1():
	cargo1 = Cargo(100,0.5,2000,1000)
	# 2000 - 1000*1.5 - 100*2 es igual a 300
	assert(cargo1.is_worth_it() == 300) == True

# Caso de cargo insaqueable
def testCargo2():
	cargo2 = Cargo(1500,1,1250,800)
	# 1250 - 800*1.5 - 1500*3.5 es igual a -5200
	with pytest.raises(ValueError):
		cargo2.is_worth_it()

# Caso de un dato negativo
def testCargo3():
	cargo3 = Cargo(-100,1,1100,500)
	# Al haber un valor negativo, ni nos gastamos en calcular el posible botin
	with pytest.raises(ValueError):
		cargo3.is_worth_it()

# Otro cargo saqueable
def testCargo4():
	cargo4 = Cargo(100,0.25,1000,100)
	assert(cargo4.is_worth_it() == 800) == True