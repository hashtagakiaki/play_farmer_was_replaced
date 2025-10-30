import wood
import sun
import hay
import harv
# 初期化


def carrot_init_copydrone():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		plant(Entities.Carrot)
		harv.copy_general_process()


def carrot_harvest_copydrone():
	for i in range(get_world_size()):
		if can_harvest() == True:
			harvest()
			plant(Entities.Carrot)
		harv.copy_general_process()


def carrot_multi(stop2=harv.ever_false):
	if not stop2():
		harv.init_multi(carrot_init_copydrone)
		harv.back()
		while not stop2():
			if spawn_drone(carrot_harvest_copydrone):
				move(East)


def carrot_single(stop2=harv.ever_false):
	if not stop2():
		harv.back()
		for _ in range(get_world_size()**2):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Carrot)
			harv.general_process()
		while not stop2():
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			harv.general_process()


def carrot_sup(stop=harv.ever_false, limit=-1):
	def stop2():
		return stop() or (num_items(Items.Carrot) >= limit and limit != -1)
	def stop3():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return stop2() or num_items(Items.Hay) <= get_cost(Entities.Carrot)[Items.Hay] or num_items(Items.Wood) <= get_cost(Entities.Carrot)[Items.Wood]
		else:
			return stop2() or num_items(Items.Power) == 0 or num_items(Items.Hay) <= get_cost(Entities.Carrot)[Items.Hay] or num_items(Items.Wood) <= get_cost(Entities.Carrot)[Items.Wood]

	while not stop2():
		if not stop3():
			if num_unlocked(Unlocks.Megafarm) == 0:
				carrot_single(stop3)
			else:
				carrot_multi(stop3)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup()
		limit1 = (limit//2**(num_unlocked(Unlocks.Carrots)-1)+1)*get_cost(Entities.Carrot)[Items.Hay]
		limit2 =  get_cost(Entities.Carrot)[Items.Hay]*get_world_size()**2*10
		if not stop2() and limit != -1 and num_items(Items.Hay) <= limit1:
			hay.hay_sup(stop2,limit1)
		elif not stop2() and limit == -1 and num_items(Items.Hay) <= limit2:
			hay.hay_sup(stop2,limit2)
		limit3 = (limit//2**(num_unlocked(Unlocks.Carrots)-1)+1)*get_cost(Entities.Carrot)[Items.Wood]
		limit4 =  get_cost(Entities.Carrot)[Items.Wood]*get_world_size()**2*10
		
		if not stop2() and limit != -1 and num_items(Items.Wood) <= limit3:
			wood.wood_sup(stop2,limit3)
		elif not stop2() and limit == -1 and num_items(Items.Wood) <= limit4:
			wood.wood_sup(stop2,limit4)