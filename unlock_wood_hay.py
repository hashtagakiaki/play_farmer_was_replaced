import harv
import wood
import hay


def a1():
	return unlock(Unlocks.Trees)


def a2():
	return unlock(Unlocks.Grass)


def unlock_wood_hay():
	wood.wood_sup(a2)
	hay.hay_sup(a1)
