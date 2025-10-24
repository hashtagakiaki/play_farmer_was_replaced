import harv
harv.back()
i = get_world_size()
while i >= 0:
	if spawn_drone(harv.to_grass):
		move(East)
		i -= 1
harv.back()
do_a_flip()
do_a_flip()
def left_hand():
	moved = South
	while get_entity_type() != Entities.Treasure:
		if harv.move(harv.turn_right(moved,3)) == False:
			if move(moved) == False:
				moved = harv.turn_right(moved,1)
				move(moved)
		else:
			moved = harv.turn_right(moved,3)
	harvest()
def right_hand():
	moved = South
	while get_entity_type() != Entities.Treasure and measure() != None:
		if harv.move(harv.turn_right(moved,1)) == False:
			if move(moved) == False:
				moved = harv.turn_right(moved,3)
				move(moved)
		else:
			moved = harv.turn_right(moved,1)
		if random() < 0.1:
			spawn_drone(left_hand)
	harvest()
while True:
	plant(Entities.Bush)
	n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance,n_substance)
	moved = South
	right_hand()