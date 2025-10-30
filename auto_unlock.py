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
	cost = get_cost(target)
#上級素材から集めないと集めた素材が消費される

	if Items.Gold in cost:
		maze.maze_sup(harv.ever_false,cost[Items.Gold])
	if Items.Bone in cost:
		dino.dino_sup(harv.ever_false,cost[Items.Bone])
	if Items.Cactus in cost:
		cacti.cacti_sup(harv.ever_false,cost[Items.Cactus])	
	if Items.Pumpkin in cost:
		pumpkin.pumpkin_sup(harv.ever_false,cost[Items.Pumpkin])
	if Items.Carrot in cost:
		if num_unlocked(Unlocks.Polyculture) == 0:
			carrot.carrot_sup(harv.ever_false,cost[Items.Carrot])
		else:
			poly.poly_sup(harv.ever_false,cost[Items.Carrot])
	if Items.Hay in cost:
		if num_unlocked(Unlocks.Polyculture) == 0:
			hay.hay_sup(harv.ever_false,cost[Items.Hay])
		else:
			poly.poly_sup(harv.ever_false,cost[Items.Hay])
	if Items.Wood in cost:
		if num_unlocked(Unlocks.Polyculture) == 0:
			wood.wood_sup(harv.ever_false,cost[Items.Wood])
		else:
			poly.poly_sup(harv.ever_false,cost[Items.Wood])
	if Items.Weird_Substance in cost:
		weired.weired_sup(harv.ever_false,cost[Items.Weird_Substance])
	unlock(target)
	
def auto_unlock_all(l):
	for i in l:
		auto_unlock(i)
