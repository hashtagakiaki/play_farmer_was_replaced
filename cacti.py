import harv
def cacti_sort():
	for i in range(get_world_size()):
		if get_entity_type() != Entities.Cactus:
			plant(Entities.Cactus)
		if measure(North) != None and measure() != None and measure() > measure(North) and get_pos_y() != get_world_size() - 1:
				swap(North)
		if measure(East) != None and measure() != None and measure() > measure(East) and get_pos_x() != get_world_size() - 1:
				swap(East)
		harv.copy_general_process()
def cacti_harvest():
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
def cacti(b=harv.ever_false):
	if not b():
		harv.init(harv.to_soil)
		harv.back()
		spawn_drone(cacti_harvest)
		while True:
			if b():
				break
			if spawn_drone(cacti_sort):
				move(East)
#ここからsustain用
import sun
import carrot
#lambda式が使えない故
def cacti_sus(b=harv.ever_false):
	def a1():
		return b() or num_items(Items.Carrot) <= 100 or num_items(Items.Power) <= 100
	def a3():
		return num_items(Items.Carrot) >= 1000000
	while not b():
		if not a1():
			cacti(a1)
		sun.sun_sup()
		if not a3():
			carrot.carrot(a3)
		break
