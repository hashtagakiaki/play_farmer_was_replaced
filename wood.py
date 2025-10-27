import harv
#初期化
def wood_init_copydrone():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		if (get_pos_x()+get_pos_y()) % 2 == 0:
			plant(Entities.Tree)
		harv.copy_general_process()

def wood_harvest_copydrone():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Tree)
		harv.copy_general_process()

def wood_multi(b):
	if not b():
		harv.back()
		i = get_world_size()
		while i >= 0:
			if spawn_drone(wood_init_copydrone):
				move(East)
				i -= 1
		while not b():
			if spawn_drone(wood_harvest_copydrone):
				move(East)

def wood_single(b=harv.ever_false):
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

import sun
def wood_sup(b=harv.ever_false):
	def a1():
		return b() or num_items(Items.Power) == 0
	while not b():
		if not a1():
			if num_unlocked(Unlocks.Megafarm) == 0:
				wood_single(a1)
			else:
				wood_multi(a1)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup()