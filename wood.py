import harv
#初期化
def wood_init():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		harv.copy_general_process()
def wood_harvest():
	for i in range(get_world_size()):
		if (get_pos_x()+get_pos_y())%2 == 0:
			if can_harvest()==True:
				harvest()
			plant(Entities.Tree)
		harv.copy_general_process()

def wood(b):
	if not b():
		harv.back()
		i = get_world_size()
		while i >= 0:
			if spawn_drone(wood_init):
				move(East)
				i -= 1
		while True:
			if b():
				break
			if spawn_drone(wood_harvest):
				move(East)
#ここからsustain
import sun
def wood_sup(b=harv.ever_false):
	def a1():
		return b() or num_items(Items.Power) <= 100
	while not b():
		if not a1():
			wood(a1)
		sun.sun_sup()
		break
		