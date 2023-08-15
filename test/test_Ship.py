import pytest

from src.ships import Ship

# Caso de barco generico saqueable
def testShip1():
	ship1 = Ship(2000,1000)
	# 2000 - 1000*1.5 es igual a 500
	assert(ship1.is_worth_it() == 500) == True

# Caso de barco generico insaqueable
def testShip2():
	ship2 = Ship(-100,500)
	with pytest.raises(ValueError):
		ship2.is_worth_it()