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


def weired_multi(b=harv.ever_false):
	if not b():
		harv.init_multi(harv.to_grass_copydrone)
		harv.back()
		while not b():
			if spawn_drone(weired_harvest_copydrone):
				move(East)


def weired_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Grassland:
				till()
			if get_pos_x() % 3 == 1 and get_pos_y() % 3 == 1:
				if num_items(Items.Weird_Substance) != 0:
					use_item(Items.Weird_Substance)
				else:
					use_item(Items.Fertilizer)
			harv.general_process()
		while not b():
			if get_pos_x() % 3 == 1 and get_pos_y() % 3 == 1:
				if num_items(Items.Weird_Substance) != 0:
					use_item(Items.Weird_Substance)
				else:
					use_item(Items.Fertilizer)
			if can_harvest() and (get_pos_x() % 3 == 1 or get_pos_y() % 3 == 1):
				harvest()
			harv.general_process()


def weired_sup(b=harv.ever_false):
	def a1():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return b()
		else:
			return b() or num_items(Items.Power) == 0
	while not b():
		if not a1():
			if num_unlocked(Unlocks.Megafarm) == 0:
				weired_single(b)
			else:
				weired_multi(b)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup(b)
