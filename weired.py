import harv
def weired_init():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		plant(Entities.Carrot)
		harv.copy_general_process()
def weired_harvest():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		harv.copy_general_process()
def weired_plant():
	for _ in range(get_world_size()):
		if get_pos_x() % 3 == 1 and get_pos_y() % 3 == 1:
			use_item(Items.Weird_Substance)
		harv.copy_general_process()
def weired(b=harv.ever_false):
	if not b():
		harv.back()
		i = get_world_size()
		while i >= 0:
			if spawn_drone(weired_init):
				move(East)
				i -= 1
		while True:
			if b():
				break
			i = get_world_size()
			while i >= 0:
				if get_pos_x() % 3 == 1:
					if spawn_drone(weired_plant):
						move(East)
						i -= 1
				else:
					move(East)
					i -= 1
			i = get_world_size()
			if b():
				break
			while i >= 0:
				if spawn_drone(weired_harvest):
					move(East)
					i -= 1
			if b():
				break
#ここからsustain
import sun
import hay
import wood
def weired_sup(b=harv.ever_false):
	def a1():
		return b() or num_items(Items.Power) <= 100 or num_items(Items.Hay) <= 100 or num_items(Items.Wood) <= 100 
	def a2():
		return num_items(Items.Hay) >= 1000000
	def a3():
		return num_items(Items.Wood) >= 1000000
	while not b():
		if not a1():
			weired(a1)
		sun.sun_sup()
		if not a2():
			hay.hay_sup(a2)
		if not a3():
			wood.wood_sup(a3)
		break
	