import harv


def maze_multi_fill_copydrone1(b=harv.ever_false):
	n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	do_a_flip()
	do_a_flip()
	while not b():
		if get_entity_type() == Entities.Treasure:
			harvest()
		if get_entity_type() != Entities.Hedge:
			plant(Entities.Bush)


def maze_multi_fill_copydrone2(b=harv.ever_false):
	n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	do_a_flip()
	do_a_flip()
	while not b():
		if get_entity_type() == Entities.Treasure:
			harvest()
		if get_entity_type() == Entities.Bush:
			use_item(Items.Weird_Substance, n_substance)


def maze_multi_fill(b=harv.ever_false):
	def maze_multi_fill_copydrone1_wrapper():
		return maze_multi_fill_copydrone1(b)

	def maze_multi_fill_copydrone2_wrapper():
		return maze_multi_fill_copydrone2(b)
	if not b():
		set_world_size(4)
		harv.init_multi(harv.to_grass_copydrone)
		harv.back()
		for _ in range(get_world_size()**2):
			if spawn_drone(maze_multi_fill_copydrone1_wrapper):
				harv.travel()
		for _ in range(get_world_size()**2):
			if spawn_drone(maze_multi_fill_copydrone2_wrapper):
				harv.travel()
		plant(Entities.Bush)
		n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, n_substance)
		harv.move_to(3, 3)
		while not b():
			if get_entity_type() == Entities.Treasure:
				harvest()
			if get_entity_type() == Entities.Bush:
				use_item(Items.Weird_Substance, n_substance)
