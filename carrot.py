import wood
import sun
import hay
import harv
# 初期化


def carrot_init_copydrone():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		plant(Entities.Carrot)
		harv.copy_general_process()


def carrot_harvest_copydrone():
	for i in range(get_world_size()):
		if can_harvest() == True:
			harvest()
			plant(Entities.Carrot)
		harv.copy_general_process()


def carrot_multi(b=harv.ever_false):
	if not b():
		harv.init_multi(carrot_init_copydrone)
		harv.back()
		while not b():
			if spawn_drone(carrot_harvest_copydrone):
				move(East)


def carrot_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Carrot)
			harv.general_process()
		while not b():
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			harv.general_process()


def carrot_sup(b=harv.ever_false):
	def a1():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return b() or num_items(Items.Hay) <= get_cost(Entities.Carrot)[Items.Hay] or num_items(Items.Wood) <= get_cost(Entities.Carrot)[Items.Wood]
		else:
			return b() or num_items(Items.Power) == 0 or num_items(Items.Hay) <= get_cost(Entities.Carrot)[Items.Hay] or num_items(Items.Wood) <= get_cost(Entities.Carrot)[Items.Wood]

	def a2():
		return num_items(Items.Hay) >= 1000*2**num_unlocked(Unlocks.Carrots)

	def a3():
		return num_items(Items.Wood) >= 1000*2**num_unlocked(Unlocks.Carrots)
	while not b():
		if not a1():
			if num_unlocked(Unlocks.Megafarm) == 0:
				carrot_single(a1)
			else:
				carrot_multi(a1)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup(b)
		if not a2():
			hay.hay_sup(a2)
		if not a3():
			wood.wood_sup(a3)
		break
