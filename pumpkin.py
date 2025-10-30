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


def pumpkin_multi(stop2=harv.ever_false):
	if not stop2():
		harv.init(pumpkin_init_copydrone)
		harv.back()
		while not stop2():
			for _ in range(2):
				i = get_world_size()
				while i >= 0 and not stop2():
					if spawn_drone(pumpkin_plant1_copydrone):
						move(East)
						i -= 1
			i = get_world_size()
			while i >= 0 and not stop2():
				if spawn_drone(pumpkin_plant2_copydrone):
					move(East)
					i -= 1


def pumpkin_single(stop2=harv.ever_false):
	if not stop2():
		harv.back()
		for _ in range(get_world_size()**2):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			harv.general_process()
		while not stop2():
			while not stop2() and not can_harvest():
				plant(Entities.Pumpkin)
			if get_pos_x() == get_world_size() - 1 and get_pos_y() == get_world_size() - 1:
				harvest()
			harv.general_process()


def pumpkin_sup(stop=harv.ever_false,limit=-1):
	def stop2():
		return stop() or (num_items(Items.Pumpkin) >= limit and limit != -1)
	
	def stop3():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return stop2() or num_items(Items.Carrot) <= get_cost(Entities.Pumpkin)[Items.Carrot]
		else:
			return stop2() or num_items(Items.Power) == 0 or num_items(Items.Carrot) <= get_cost(Entities.Pumpkin)[Items.Carrot]

	def stop4():
		return num_items(Items.Carrot) >= 1000*2**num_unlocked(Unlocks.Pumpkins)
	
	while not stop2():
		if not stop3():
			if num_unlocked(Unlocks.Megafarm) == 0:
				pumpkin_single(stop3)
			else:
				pumpkin_multi(stop3)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup(stop2)
		limit1 = (limit//(2**(num_unlocked(Unlocks.Pumpkins))*get_world_size()**2*6))*get_cost(Entities.Pumpkin)[Items.Carrot]
		limit2 =  get_cost(Entities.Pumpkin)[Items.Carrot]*get_world_size()**2*30
		if not stop4() and limit != -1 and num_items(Items.Carrot) <= limit1:
			carrot.carrot_sup(stop4,limit1)
		elif not stop4() and limit == -1 and num_items(Items.Carrot) <= limit2:
			carrot.carrot_sup(stop4,limit2)