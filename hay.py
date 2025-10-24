import harv
def hay_harvest():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		move(North)

#他の場所で使う用
def hay(b=False):
	if not b():
		harv.back()
		i = get_world_size()
		while i >= 0:
			if spawn_drone(harv.to_grass):
				move(East)
				i -= 1
		while True:
			if b():
				break
			if spawn_drone(hay_harvest):
				move(East)
#ここからsustain
import sun
def hay_sup(b=harv.ever_false):
	def a1():
		return b() or num_items(Items.Power) <= 100
	while not b():
		if not a1():
			hay(a1)
		sun.sun_sup(b)
		break

def hay_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Grassland:
					till()
			harv.general_process()
		while True:
			if b():
				break
			if can_harvest():
				harvest()
			harv.general_process()
def 