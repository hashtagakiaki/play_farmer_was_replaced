import wood
import sun
import harv


def weired_harvest_copydrone():
	for i in range(get_world_size()):
		if get_pos_x() % 3 == 1 and get_pos_y() % 3 == 1:
			if num_items(Items.Weird_Substance) != 0:
				use_item(Items.Weird_Substance)
			else:
				use_item(Items.Fertilizer)
		if get_pos_x() % 3 == 1 or get_pos_y() % 3 == 1:
			harvest()
		move(North)


def weired_multi(stop2=harv.ever_false):
	if not stop2():
		harv.init_multi(harv.to_grass_copydrone)
		harv.back()
		while not stop2():
			if spawn_drone(weired_harvest_copydrone):
				move(East)


def weired_single(stop2=harv.ever_false):
	if not stop2():
		harv.back()
		for _ in range(get_world_size()**2):
			if get_ground_type() != Grounds.Grassland:
				till()
			if get_pos_x() % 3 == 1 and get_pos_y() % 3 == 1:
				if num_items(Items.Weird_Substance) != 0:
					use_item(Items.Weird_Substance)
				else:
					use_item(Items.Fertilizer)
			harv.general_process()
		while not stop2():
			if get_pos_x() % 3 == 1 and get_pos_y() % 3 == 1:
				if num_items(Items.Weird_Substance) != 0:
					use_item(Items.Weird_Substance)
				else:
					use_item(Items.Fertilizer)
			if can_harvest() and (get_pos_x() % 3 == 1 or get_pos_y() % 3 == 1):
				harvest()
			harv.general_process()


def weired_sup(stop=harv.ever_false,limit = -1):
	def stop2():
		return stop() or (num_items(Items.Weird_Substance) >= limit and limit != -1)
	def stop3():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return stop2()
		else:
			return stop2() or num_items(Items.Power) == 0
	while not stop2():
		if not stop3():
			if num_unlocked(Unlocks.Megafarm) == 0:
				weired_single(stop3)
			else:
				weired_multi(stop3)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup(stop2)
