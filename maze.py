import maze1
import sun
import weired
import harv
import maze2


def left_hand(stop2=harv.ever_false):
	moved = South
	while get_entity_type() != Entities.Treasure and not stop2():
		if harv.move(harv.turn_right(moved, 3)) == False:
			if move(moved) == False:
				moved = harv.turn_right(moved, 1)
				move(moved)
		else:
			moved = harv.turn_right(moved, 3)
	if get_entity_type() == Entities.Treasure:
		harvest()


def maze_multi_main(stop2=harv.ever_false):
	def left_hand_wrapper():
		return left_hand(stop2)
	if not stop2():
		moved = South
		while get_entity_type() != Entities.Treasure and measure() != None and not stop2():
			if harv.move(harv.turn_right(moved, 1)) == False:
				if move(moved) == False:
					moved = harv.turn_right(moved, 3)
					move(moved)
			else:
				moved = harv.turn_right(moved, 1)
			if random() < 0.1:
				spawn_drone(left_hand)
		if get_entity_type() == Entities.Treasure:
			harvest()


def maze_multi(stop2=harv.ever_false):
	if not stop2():
		harv.init_multi(harv.to_grass_copydrone)
		harv.back()
		do_a_flip()
		do_a_flip()
		while not stop2():
			plant(Entities.Bush)
			n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, n_substance)
			maze_multi_main()


def maze_single(stop2=harv.ever_false):
	if not stop2():
		harv.back()
		for _ in range(get_world_size()**2):
			if get_ground_type() != Grounds.Grassland:
				till()
			harv.general_process()
		moved = South
		while not stop2():
			plant(Entities.Bush)
			n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, n_substance)
			while get_entity_type() != Entities.Treasure and measure() != None and not stop2():
				if harv.move(harv.turn_right(moved, 1)) == False:
					if move(moved) == False:
						moved = harv.turn_right(moved, 3)
						move(moved)
				else:
					moved = harv.turn_right(moved, 1)
			harvest()


def maze_sup(stop=harv.ever_false,limit=-1):
	def stop2():
		return stop() or (num_items(Items.Gold) >= limit and limit != -1)

	def stop3():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return stop2() or num_items(Items.Weird_Substance) <= get_world_size()*2**(num_unlocked(Unlocks.Mazes) - 1)
		else:
			return stop2() or num_items(Items.Power) == 0 or num_items(Items.Weird_Substance) <= get_world_size()*2**(num_unlocked(Unlocks.Mazes) - 1)

	def a2():
		return num_items(Items.Weird_Substance) >= (get_world_size()*2**(num_unlocked(Unlocks.Mazes)))*600

	while not stop2():
		if not stop3():
			if num_unlocked(Unlocks.Megafarm) == 0:
				maze_single(stop3)
			else:
				maze2.maze_multi_fill(stop3)
				set_world_size(32)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup()
		limit1 = (limit // ((2**(num_unlocked(Unlocks.Mazes))-1)*get_world_size()**2))*get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		limit2 = (get_world_size()*2**(num_unlocked(Unlocks.Mazes)))*600
		if not stop2() and limit != -1 and num_items(Items.Weird_Substance) <= limit1:
			weired.weired_sup(stop2,limit1)
		elif not stop2() and limit == -1 and num_items(Items.Weird_Substance) <= limit2:
			weired.weired_sup(stop2,limit2)