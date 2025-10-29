import harv
import carrot
import sun


def poly_copydrone(b=harv.ever_false):
	if not b():
		dict_comp = {}
		while not b():
			a = get_pos_x(), get_pos_y()
			if a in dict_comp:
				harvest()
				tar = dict_comp[a]
				if tar == Entities.Bush:
					if get_ground_type() != Grounds.Grassland:
						till()
				else:
					if get_ground_type() != Grounds.Soil:
						till()
					plant(tar)
			else:
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)
			c = get_companion()
			if c != None:
				dict_comp[c[1]] = c[0]
			harv.general_process()


def poly(b=harv.ever_false):
	def poly_copydrone_wrapper():
		return poly_copydrone(b)
	if not b():
		harv.init_multi(carrot.carrot_init_copydrone)
		harv.back()
		dict_comp = {}
		while not b():
			if spawn_drone(poly_copydrone_wrapper):
				move(East)
				
def poly_sup(b=harv.ever_false):
	def a1():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return b()
		else:
			return b() or num_items(Items.Power) == 0
	while not b():
		if not a1():
			if num_unlocked(Unlocks.Megafarm) == 0:
				poly(a1)
			else:
				poly(a1)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup(b)