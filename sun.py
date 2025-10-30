import carrot
import harv
# 初期化


def sun_init_copydrone():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		plant(Entities.Sunflower)
		harv.copy_general_process()


def sun_harvest_copydrone():
	for i in range(get_world_size()):
		if can_harvest() == True:
			harvest()
			plant(Entities.Sunflower)
		harv.copy_general_process()


def sun_multi(stop2):
	if not stop2():
		harv.init_multi(sun_init_copydrone)
		harv.back()
		while not stop2():
			if spawn_drone(sun_harvest_copydrone):
				move(East)


def sun_single(stop2=harv.ever_false):
	if not stop2():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			harv.general_process()
		while not stop2():
			if can_harvest():
				harvest()
				plant(Entities.Sunflower)
			harv.general_process()


# ここからsustain


def sun_sup(stop=harv.ever_false, limit=-1):
	def stop2():
		return stop() or (num_items(Items.Power) >= limit and limit != -1)

	def stop3():
		return stop2() or num_items(Items.Carrot) <= get_cost(Entities.Sunflower)[Items.Carrot] or num_items(Items.Power) >= (312*max_drones()) or num_items(Items.Power) != 0

	def stop4():
		return stop2() or num_items(Items.Carrot) <= get_cost(Entities.Sunflower)[Items.Carrot] or num_items(Items.Power) >= (312*max_drones())

	while not stop3():
		if num_unlocked(Unlocks.Megafarm) == 0:
			sun_single(stop4)
		else:
			sun_multi(stop4)
		limit1 = max(312*max_drones(),limit)*get_cost(Entities.Sunflower)[Items.Carrot]
		if not stop2() and limit != -1 and num_items(Items.Carrot) <= limit1:
			carrot.carrot_sup(stop2,limit1)