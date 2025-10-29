import harv
import hay
import wood
import carrot
import cacti
import pumpkin
import sun
import dino
import maze
import weired
import poly


def auto_unlock(target):
	def num(a, i):
		def sup():
			return a <= num_items(i)
		return sup
	cost = get_cost(target)
	if Items.Hay in cost:
		if num_unlocked(Unlocks.Polyculture) == 0:
			hay.hay_sup(num(cost[Items.Hay], Items.Hay))
		else:
			poly.poly_sup(num(cost[Items.Hay], Items.Hay))
	if Items.Wood in cost:
		if num_unlocked(Unlocks.Polyculture) == 0:
			wood.wood_sup(num(cost[Items.Wood], Items.Wood))
		else:
			poly.poly_sup(num(cost[Items.Wood], Items.Wood))
	if Items.Carrot in cost:
		if num_unlocked(Unlocks.Polyculture) == 0:
			carrot.carrot_sup(num(cost[Items.Carrot], Items.Carrot))
		else:
			poly.poly_sup(num(cost[Items.Carrot], Items.Carrot))
	if Items.Cactus in cost:
		cacti.cacti_sup(num(cost[Items.Cactus], Items.Cactus))
	if Items.Pumpkin in cost:
		pumpkin.pumpkin_sup(num(cost[Items.Pumpkin], Items.Pumpkin))
	if Items.Power in cost:
		sun.sun_sup(num(cost[Items.Power], Items.Power))
	if Items.Bone in cost:
		dino.dino_sup(num(cost[Items.Bone], Items.Bone))
	if Items.Gold in cost:
		maze.maze_sup(num(cost[Items.Gold], Items.Gold))
	if Items.Weird_Substance in cost:
		weired.weired_sup(
			num(cost[Items.Weird_Substance], Items.Weird_Substance))
	unlock(target)
	
def auto_unlock_all(l):
	for i in l:
		auto_unlock(i)
