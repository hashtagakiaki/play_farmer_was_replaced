import sun
import harv


def hay_harvest_copydrone():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		move(North)


def hay_multi(b=harv.ever_false):
	if not b():
		harv.init_multi(harv.to_grass_copydrone)
		harv.back()
		while not b():
			if spawn_drone(hay_harvest_copydrone):
				move(East)


def hay_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Grassland:
				till()
			harv.general_process()
		while not b():
			if can_harvest():
				harvest()
			harv.general_process()


def hay_sup(b=harv.ever_false):
	def a1():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return b()
		else:
			return b() or num_items(Items.Power) == 0
	while not b():
		if not a1():
			if num_unlocked(Unlocks.Megafarm) == 0:
				hay_single(b)
			else:
				hay_multi(b)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup(b)
