import harv
def pumpkin_init():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		harv.copy_general_process()

def pumpkin_plant1():
	for i in range(get_world_size()):
		if not can_harvest():
			plant(Entities.Pumpkin)
		harv.copy_general_process()

def pumpkin_plant2():
	i = get_world_size()
	while i >= 0:
		if not can_harvest():
			plant(Entities.Pumpkin)
		else:
			harv.copy_general_process()
			i -= 1
			if get_pos_x() == get_world_size() - 1 and get_pos_y() == get_world_size() - 1:
				harvest()

def pumpkin_harvest():
	while True:
		for _ in range(20):
			do_a_flip()
		harvest()

def pumpkin(b=harv.ever_false):
	if not b():
		harv.init(pumpkin_init)
		harv.back()
		#spawn_drone(pumpkin_harvest)
		while True:
			for _ in range(2):
				i = get_world_size()
				while i >= 0:
					if b():
						break
					if spawn_drone(pumpkin_plant1):
						move(East)
						i -= 1
			i = get_world_size()
			while i >= 0:
				if b():
					break
				if spawn_drone(pumpkin_plant2):
					move(East)
					i -= 1
			if b():
				break

#ここからsustain
import carrot
import sun
def pumpkin_sup(b=harv.ever_false):
	def a1():
		return b() or num_items(Items.Power) <= 100 or num_items(Items.Carrot) <= 100 
	def a2():
		return num_items(Items.Carrot) >= 1000000
	while not b():
		if not a1():
			pumpkin(a1)
		sun.sun_sup(b)
		if not a2():
			carrot.carrot_sup(a2)
		break
			
	
	