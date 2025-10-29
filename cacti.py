import sun
import pumpkin
import harv


def cacti_sort_copydrone():
	for i in range(get_world_size()):
		if get_entity_type() != Entities.Cactus:
			plant(Entities.Cactus)
		if measure(North) != None and measure() != None and measure() > measure(North) and get_pos_y() != get_world_size() - 1:
			swap(North)
		if measure(East) != None and measure() != None and measure() > measure(East) and get_pos_x() != get_world_size() - 1:
			swap(East)
		harv.copy_general_process()


def cacti_harvest_copydrone():
	while True:
		flag_harv = True
		harv.back()
		for i in range(get_world_size()**2):
			height_north = measure(North)
			height_here = measure()
			if measure(North) != None and measure() != None and height_here > height_north and get_pos_y() != get_world_size() - 1:
				flag_harv = False
			height_east = measure(East)
			height_here = measure()
			if measure(East) != None and measure() != None and height_here > height_east and get_pos_x() != get_world_size() - 1:
				flag_harv = False
			harv.travel()
		if flag_harv:
			harvest()


def cacti_notsort_copydrone():
	for i in range(get_world_size()):
		while measure() != 9:
			harvest()
			plant(Entities.Cactus)
			if num_items(Items.Pumpkin) <= get_cost(Entities.Cactus)[Items.Pumpkin]:
				break
		if num_items(Items.Pumpkin) <= get_cost(Entities.Cactus)[Items.Pumpkin]:
			break
		if get_pos_x() == get_world_size() - 1 and get_pos_y() == get_world_size() - 1:
			do_a_flip()
			harvest()
		harv.copy_general_process()


def cacti_multi(b=harv.ever_false):
	if not b():
		harv.init_multi(harv.to_soil_copydrone)
		harv.back()
		while not b():
			i = get_world_size()
			while i >= 0:
				if spawn_drone(cacti_notsort_copydrone):
					move(East)
					i -= 1
			harv.back()
			while measure() != None:
				do_a_flip()
			harvest()

			
def cacti_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Soil:
				till()
			harvest()
			plant(Entities.Cactus)
			harv.general_process()
		while not b():
			while measure() != 9:
				harvest()
				plant(Entities.Cactus)
			if get_pos_x() == get_world_size() - 1 and get_pos_y() == get_world_size() - 1:
				harvest()
			harv.general_process()
			
			
def cacti_sup(b=harv.ever_false, limit=-1):
	def a1():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return b() or num_items(Items.Pumpkin) <= get_cost(Entities.Cactus)[Items.Pumpkin] or (num_items(Items.Cactus) >= limit and limit != -1)
		else:
			return b() or num_items(Items.Pumpkin) <= get_cost(Entities.Cactus)[Items.Pumpkin] or num_items(Items.Power) == 0 or (num_items(Items.Cactus) >= limit and limit != -1)

	while not b() and (num_items(Items.Cactus) <= limit or limit != -1):
		if not a1():
			if num_unlocked(Unlocks.Megafarm) == 0:
				cacti_single(a1)
			else:
				cacti_multi(a1)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup()
		c = (limit//2**(num_unlocked(Unlocks.Cactus)-1)+1)*get_cost(Entities.Cactus)[Items.Pumpkin]
		if not b() and num_items(Items.Pumpkin) <= c or limit == -1:
			pumpkin.pumpkin_sup(b,c)
