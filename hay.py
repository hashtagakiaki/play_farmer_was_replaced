import sun
import harv


def hay_harvest_copydrone():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		move(North)


def hay_multi(stop2=harv.ever_false):
	if not stop2():
		harv.init_multi(harv.to_grass_copydrone)
		harv.back()
		while not stop2():
			if spawn_drone(hay_harvest_copydrone):
				move(East)


def hay_single(stop2=harv.ever_false):
	if not stop2():
		harv.back()
		for _ in range(get_world_size()**2):
			if get_ground_type() != Grounds.Grassland:
				till()
			harv.general_process()
		while not stop2():
			if can_harvest():
				harvest()
			harv.general_process()


def hay_sup(stop=harv.ever_false, limit=-1):
	def stop2():
		return stop() or (num_items(Items.Hay) >= limit and limit != -1)
	def stop3():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return stop2()
		else:
			return stop2() or num_items(Items.Power) == 0

	while not stop2():
		if not stop3():
			if num_unlocked(Unlocks.Megafarm) == 0:
				hay_single(stop3)
			else:
				hay_multi(stop3)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup()
