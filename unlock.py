import harv
unlock(Unlocks.Loops)
for i in range(21):
	harvest()
unlock(Unlocks.Speed)
while num_items(Items.Hay) <= 150:
	if can_harvest():
		harvest()
unlock(Unlocks.Plant)
unlock(Unlocks.Expand)
while num_items(Items.Wood) <= 170:
	if num_items(Items.Wood) >= 20:
		unlock(Unlocks.Speed)
	if num_items(Items.Wood) >= 20:
		unlock(Unlocks.Expand)
	if get_ground_type() != Grounds.Soil:
		till()
	if can_harvest():
		harvest()
	plant(Entities.Bush)
	harv.travel()
unlock(Unlocks.Carrots)
while num_items(Items.Carrot) <= 70:
	if can_harvest():
		harvest()
	plant(Entities.Carrot)
	move(North)
unlock(Unlocks.Trees)
use_item(Items.Water)
while True:
	do_a_flip()
