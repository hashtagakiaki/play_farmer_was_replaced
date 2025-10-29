import harv


def maze_multi_fill_copydrone(b=harv.ever_false):
	n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	last_tick = 0
	do_a_flip()
	do_a_flip()
	while not b():
		if get_entity_type() == Entities.Treasure:
			if get_tick_count() - last_tick < 12000:
				use_item(Items.Weird_Substance, n_substance)
			else:
				harvest()
		ent = get_entity_type()
		if ent != Entities.Hedge and ent != Entities.Treasure:
			last_tick = get_tick_count()
			plant(Entities.Bush)
			use_item(Items.Weird_Substance, n_substance)


def maze_multi_fill(b=harv.ever_false):
	def maze_multi_fill_copydrone_wrapper():
		return maze_multi_fill_copydrone(b)

	if not b():
		set_world_size(5)
		harv.init_multi(harv.to_grass_copydrone)
		harv.back()
		for _ in range(get_world_size()**2):
			if spawn_drone(maze_multi_fill_copydrone_wrapper):
				harv.travel()
		plant(Entities.Bush)
		n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, n_substance)
		harv.move_to(4, 4)
		while not b():
			do_a_flip()
