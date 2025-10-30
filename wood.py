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


def tree_multi(stop2):
	if not stop2():
		harv.init_multi(tree_init_copydrone)
		harv.back()
		while not stop2():
			if spawn_drone(tree_harvest_copydrone):
				move(East)


def tree_single(stop2=harv.ever_false):
	if not stop2():
		harv.back()
		for _ in range(get_world_size()**2):
			if get_ground_type() != Grounds.Soil:
				till()
			harvest()
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant(Entities.Tree)
			harv.general_process()
		while not stop2():
			if can_harvest():
				harvest()
				plant(Entities.Tree)
			harv.general_process()


def bush_single(stop2=harv.ever_false):
	if not stop2():
		harv.back()
		for _ in range(get_world_size()**2):
			if get_ground_type() != Grounds.Soil:
				till()
				plant(Entities.Bush)
			harv.general_process()
		while not stop2():
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			harv.general_process()


def wood_sup(stop=harv.ever_false,limit=-1):
	def stop2():
		return stop() or (num_items(Items.Wood) >= limit and limit != -1)
	def stop3():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return stop2()
		else:
			return stop2() or num_items(Items.Power) == 0
	while not stop2():
		if not stop3():
			if num_unlocked(Unlocks.Megafarm) != 0:
				tree_multi(stop3)
			elif num_unlocked(Unlocks.Trees) == 0:
				bush_single(stop3)
			else:
				tree_single(stop3)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup(stop2)
