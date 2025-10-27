import sun
import weired
import harv


def left_hand():
	moved = South
	while get_entity_type() != Entities.Treasure:
		if harv.move(harv.turn_right(moved, 3)) == False:
			if move(moved) == False:
				moved = harv.turn_right(moved, 1)
				move(moved)
		else:
			moved = harv.turn_right(moved, 3)
	harvest()


def maze_multi_main(b=harv.ever_false):
	if not b():
		moved = South
		while get_entity_type() != Entities.Treasure and measure() != None and not b():
			if harv.move(harv.turn_right(moved, 1)) == False:
				if move(moved) == False:
					moved = harv.turn_right(moved, 3)
					move(moved)
			else:
				moved = harv.turn_right(moved, 1)
			if random() < 0.1:
				spawn_drone(left_hand)
		harvest()


def maze_multi(b=harv.ever_false):
	if not b():
		harv.init_multi(harv.to_grass_copydrone)
		harv.back()
		do_a_flip()
		do_a_flip()
		while not b():
			n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, n_substance)
			maze_multi_main()


def maze_single(b=harv.ever_false):
	if not b():
		harv.back()
		for i in range(get_world_size()*2):
			if get_ground_type() != Grounds.Grassland:
				till()
			harv.general_process()
		moved = South
		while get_entity_type() != Entities.Treasure and measure() != None and not b():
			if harv.move(harv.turn_right(moved, 1)) == False:
				if move(moved) == False:
					moved = harv.turn_right(moved, 3)
					move(moved)
			else:
				moved = harv.turn_right(moved, 1)
		harvest()


def maze_sup(b=harv.ever_false):
	def a1():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return b() or num_items(Items.Weird_Substance) <= get_world_size()*2**(num_unlocked(Unlocks.Mazes) - 1)
		else:
			return b() or num_items(Items.Power) == 0 or num_items(Items.Weird_Substance) <= get_world_size()*2**(num_unlocked(Unlocks.Mazes) - 1)

	def a2():
		return num_items(Items.Weird_Substance) >= (get_world_size()*2**(num_unlocked(Unlocks.Mazes)))*20
	while not b():
		if not a1():
			if num_unlocked(Unlocks.Megafarm) == 0:
				maze_single(a1)
			else:
				maze_multi(a1)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup()
		if not a2():
			weired.weired_sup(a2)
