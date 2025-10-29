import sun
import harv
# 初期化


def tree_init_copydrone():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		if (get_pos_x()+get_pos_y()) % 2 == 0:
			plant(Entities.Tree)
		harv.copy_general_process()


def tree_harvest_copydrone():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Tree)
		harv.copy_general_process()


def tree_multi(b):
	if not b():
		harv.init_multi(tree_init_copydrone)
		harv.back()
		while not b():
			if spawn_drone(tree_harvest_copydrone):
				move(East)


def tree_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Soil:
				till()
			harvest()
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant(Entities.Tree)
			harv.general_process()
		while not b():
			if can_harvest():
				harvest()
				plant(Entities.Tree)
			harv.general_process()


def bush_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Soil:
				till()
				plant(Entities.Bush)
			harv.general_process()
		while not b():
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			harv.general_process()


def wood_sup(b=harv.ever_false):
	def a1():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return b()
		else:
			return b() or num_items(Items.Power) == 0
	while not b():
		if not a1():
			if num_unlocked(Unlocks.Megafarm) != 0:
				tree_multi(a1)
			elif num_unlocked(Unlocks.Trees) == 0:
				bush_single(a1)
			else:
				tree_single(a1)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup()
