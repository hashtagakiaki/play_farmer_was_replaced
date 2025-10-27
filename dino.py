import harv
import sun


def dino(b=harv.ever_false):
	if not b():
		change_hat(Hats.Straw_Hat)
		harv.back()
		if num_unlocked(Unlocks.Megafarm) == 0:
			for _ in range(get_world_size()):
				if get_ground_type() != Grounds.Soil:
					till()
				harvest()
				harv.copy_general_process()
		else:
			harv.init_multi(harv.to_soil_copydrone)

		while not b():
			change_hat(Hats.Straw_Hat)
			harv.back()
			change_hat(Hats.Dinosaur_Hat)
			while not b():
				for _ in range(get_world_size() - 1):
					if not move(North):
						break
				for _ in range(get_world_size() - 1):
					if not move(East):
						break
				if not move(South):
					break
				if get_world_size() % 2 == 1:
					for _ in range((get_world_size() - 3)//2):
						move(West)
						move(South)
						move(East)
						move(South)
					move(South)
					move(West)
					move(West)
					for _ in range(get_world_size() - 2):
						move(North)
					move(West)
					for _ in range((get_world_size() - 1)//2 - 2):
						for _ in range(get_world_size() - 2):
							if not move(South):
								break
						if not move(West):
							break
						for _ in range(get_world_size() - 2):
							if not move(North):
								break
						if not move(West):
							break
					for _ in range(get_world_size() - 2):
						if not move(South):
							break
					if not move(West):
						break
				else:
					for _ in range((get_world_size() - 1)//2):
						for _ in range(get_world_size() - 2):
							if not move(South):
								break
						if not move(West):
							break
						for _ in range(get_world_size() - 2):
							if not move(North):
								break
						if not move(West):
							break
					for _ in range(get_world_size() - 2):
						if not move(South):
							break
					if not move(West):
						break


def dino_sup(b=harv.ever_false):
	def a1():
		if num_unlocked(Unlocks.Sunflowers) == 0:
			return b() or num_items(Items.Cactus) <= get_cost(Entities.Apple)[Items.Cactus]
		else:
			return b() or num_items(Items.Power) == 0 or num_items(Items.Cactus) <= get_cost(Entities.Apple)[Items.Cactus]
	while not b():
		if not a1():
			dino(b)
			change_hat(Hats.Straw_Hat)
		if num_unlocked(Unlocks.Sunflowers) != 0:
			sun.sun_sup(b)
