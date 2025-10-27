import carrot
import sun
import harv


def pumpkin_init_copydrone():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		harv.copy_general_process()


def pumpkin_plant1_copydrone():
	for i in range(get_world_size()):
		if not can_harvest():
			plant(Entities.Pumpkin)
		harv.copy_general_process()


def pumpkin_plant2_copydrone():
	i = get_world_size()
	while i >= 0:
		if not can_harvest():
			plant(Entities.Pumpkin)
		else:
			harv.copy_general_process()
			i -= 1
			if get_pos_x() == get_world_size() - 1 and get_pos_y() == get_world_size() - 1:
				harvest()


def pumpkin_multi(b=harv.ever_false):
	if not b():
		harv.init(pumpkin_init_copydrone)
		harv.back()
		while not b():
			for _ in range(2):
				i = get_world_size()
				while i >= 0 and not b():
					if spawn_drone(pumpkin_plant1_copydrone):
						move(East)
						i -= 1
			i = get_world_size()
			while i >= 0 and not b():
				if spawn_drone(pumpkin_plant2_copydrone):
					move(East)
					i -= 1


def pumpkin_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			harv.general_process()
		while not b():
			while not b() and not can_harvest():
				plant(Entities.Pumpkin)
			if get_pos_x() == get_world_size() - 1 and get_pos_y() == get_world_size() - 1:
				harvest()
			harv.general_process()


def pumpkin_sup(b=harv.ever_false):
	def a1():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return b() or num_items(Items.Carrot) <= get_cost(Entities.Pumpkin)[Items.Carrot]
		else:
			return b() or num_items(Items.Power) == 0 or num_items(Items.Carrot) <= get_cost(Entities.Pumpkin)[Items.Carrot]

	def a2():
		return num_items(Items.Carrot) >= 1000*2**num_unlocked(Unlocks.Pumpkins)
	while not b():
		if not a1():
			if num_unlocked(Unlocks.Megafarm) == 0:
				pumpkin_single(a1)
			else:
				pumpkin_multi(a1)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup(b)
		if not a2():
			carrot.carrot_sup(a2)
