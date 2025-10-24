import harv
import carrot
def poly():
	dict_comp = {}
	while True:
		a = get_pos_x(),get_pos_y()
		harvest()
		if a in dict_comp:
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
		b = get_companion()
		if b != None:
			dict_comp[b[1]] = b[0]
		harv.general_process()
harv.back()
i = get_world_size()
while i >= 0:
	if spawn_drone(carrot.carrot_init):
		move(East)
		i -= 1
harv.back()
dict_comp = {}
while True:
	if spawn_drone(poly):
		move(East)
		