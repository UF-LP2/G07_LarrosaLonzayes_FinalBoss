import pytest

from src.Cruise import Cruise

# Caso de crucero saqueable
def testCruise1():
	cruise1 = Cruise(100,2000,1000)
	# 2000 - 1000*1.5 - 100*2.25 es igual a 275
	assert(cruise1.is_worth_it() == 275) == True

# Caso de crucero insaqueable
def testCruise2():
	cruise2 = Cruise(5100,1250,800)
	# 1250 - 800*1.5 - 5100*3.5 es igual a algo <0
	with pytest.raises(ValueError):
		cruise2.is_worth_it()