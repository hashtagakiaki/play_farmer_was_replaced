import harv
def movable(direction):
	if move(direction):
		return False
	else:
		return True
def dino_init():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		harv.copy_general_process()
change_hat(Hats.Straw_Hat)
i = get_world_size()
while i >= 0:
	if spawn_drone(dino_init):
		move(East)
		i -= 1
while True:
	change_hat(Hats.Straw_Hat)
	harv.back()
	change_hat(Hats.Dinosaur_Hat)
	while True:
		for i in range(get_world_size() - 1):
			if movable(North):
				break
		for i in range(get_world_size() - 1):
			if movable(East):
				break
		if movable(South):
			break
		if get_world_size() % 2 == 1:
			for i in range((get_world_size() - 3)//2):
				move(West)
				move(South)
				move(East)
				move(South)
			move(South)
			move(West)
			move(West)
			for i in range(get_world_size() - 2):
				move(North)
			move(West)
			for i in range((get_world_size() - 1)//2 - 2):
				for i in range(get_world_size() - 2):
					if movable(South):
						break
				if movable(West):
					break
				for i in range(get_world_size() - 2):
					if movable(North):
						break
				if movable(West):
					break
			for i in range(get_world_size() - 2):
				if movable(South):
					break
			if movable(West):
				break
		else:
			for i in range((get_world_size() - 1)//2):
				for i in range(get_world_size() - 2):
					if movable(South):
						break
				if movable(West):
					break
				for i in range(get_world_size() - 2):
					if movable(North):
						break
				if movable(West):
					break
			for i in range(get_world_size() - 2):
				if movable(South):
					break
			if movable(West):
				break