import harv
import cacti
def counter():
	return get_time() >= 3600
cacti.cacti_sup(counter)
quick_print(num_items(Items.Cactus),1000000000 - num_items(Items.Pumpkin))