import harv
#初期化
def sun_init():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		plant(Entities.Sunflower)
		harv.copy_general_process()
def sun_harvest():
	for i in range(get_world_size()):
		if can_harvest()==True:
			harvest()
			plant(Entities.Sunflower)
		harv.copy_general_process()
def sun(b):
	if not b():
		i = get_world_size()
		while i >= 0:
			if spawn_drone(sun_init):
				move(East)
				i -= 1
		while True:
			if b():
				break
			if spawn_drone(sun_harvest):
				move(East)
#ここからsustain
import carrot
def sun_sup(b=harv.ever_false):
	def a1():
		return b() or num_items(Items.Carrot) <= 100 or num_items(Items.Power) >= 10000
	def a2():
		return b() or num_items(Items.Carrot) >= 50000
	while not b():
		if not a1():
			sun(a1)
		if not a2():
			carrot.carrot_sup(a2)
		break
