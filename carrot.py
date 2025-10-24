import harv
#初期化
def carrot_init():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		plant(Entities.Carrot)
		harv.copy_general_process()
def carrot_harvest():
	for i in range(get_world_size()):
		if can_harvest()==True:
			harvest()
			plant(Entities.Carrot)
		harv.copy_general_process()

def carrot(b=harv.ever_false):
	if not b():
		i = get_world_size()
		while i >= 0:
			if spawn_drone(carrot_init):
				move(East)
				i -= 1
		while True:
			if spawn_drone(carrot_harvest):
				move(East)
			if b():
				break
#ここからsustain
import wood
import hay
import sun
def carrot_sup(b=harv.ever_false):
	def a1():
		return b() or num_items(Items.Power) <= 100 or num_items(Items.Hay) <= 100 or num_items(Items.Wood) <= 100 
	def a2():
		return num_items(Items.Hay) >= 1000000
	def a3():
		return num_items(Items.Wood) >= 1000000
	while not b():
		if not a1():
			carrot(a1)
		sun.sun_sup(b)
		if not a2():
			hay.hay_sup(a2)
		if not a3():
			wood.wood_sup(a3)
		break
		
		