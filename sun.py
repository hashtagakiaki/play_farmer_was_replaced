import harv
#初期化
def sun_init_copydrone():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		plant(Entities.Sunflower)
		harv.copy_general_process()
def sun_harvest_copydrone():
	for i in range(get_world_size()):
		if can_harvest()==True:
			harvest()
			plant(Entities.Sunflower)
		harv.copy_general_process()

def sun_multi(b):
	if not b():
		harv.back()
		i = get_world_size()
		while i >= 0:
			if spawn_drone(sun_init_copydrone):
				move(East)
				i -= 1
		while not b():
			if spawn_drone(sun_harvest_copydrone):
				move(East)

def sun_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			harv.general_process()
		while not b():
			if can_harvest():
				harvest()
				plant(Entities.Sunflower)
			harv.general_process()

#ここからsustain
import carrot
def sun_sup(b=harv.ever_false):
	def a1():
		return b() or num_items(Items.Carrot) <= get_cost(Entities.Sunflower)[Items.Carrot] or num_items(Items.Power) >= (312*max_drones()) or num_items(Items.Power) == 0
	def a2():
		return b() or num_items(Items.Carrot) <= get_cost(Entities.Sunflower)[Items.Carrot] or num_items(Items.Power) >= (312*max_drones())
	def a3():
		return b() or num_items(Items.Carrot) >= 1000*2**num_unlocked(Unlocks.Carrots)
	while not a1():
		if num_unlocked(Unlocks.Megafarm) == 0:
			sun_single(a2)
		else:
			sun_multi(a2)
		if not a3():
			carrot.carrot_sup(a3)