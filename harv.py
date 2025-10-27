
# 移動
def travel():
	if get_pos_y() != get_world_size()-1:
		move(North)
	else:
		move(North)
		move(East)
# 逆向き移動


def travel_rev():
	if get_pos_y() != 0:
		move(South)
	else:
		move(South)
		move(West)

# 移動時水まきつき


def general_process():
	if get_water() < 0.5:
		use_item(Items.Water)
	travel()


def general_process_rev():
	if get_water() < 0.5:
		use_item(Items.Water)
	travel_rev()

# copy_drone用のgeneral


def copy_general_process():
	if get_water() < 0.6:
		use_item(Items.Water)
	move(North)

# 初期地点に戻る


def back():
	for _ in range(get_pos_y()):
		move(South)
	for _ in range(get_pos_x()):
		move(West)

# 特定位置に行く


def move_to(to_x, to_y):
	now_x = get_pos_x()
	now_y = get_pos_y()
	if now_x < to_x:
		for _ in range(to_x - now_x):
			move(East)
	elif now_x > to_x:
		for _ in range(now_x - to_x):
			move(West)
	if now_y < to_y:
		for _ in range(to_y - now_y):
			move(North)
	elif now_y > to_y:
		for _ in range(now_y - to_y):
			move(South)


def turn_right(moved, num):
	if num != 0:
		if moved == East:
			ans = South
		elif moved == South:
			ans = West
		elif moved == West:
			ans = North
		else:
			ans = East
		return turn_right(ans, num-1)
	else:
		return moved

# soilにする


def to_soil_copydrone():
	for _ in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		move(North)
# grasslandにする


def to_grass_copydrone():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Grassland:
			till()
		harvest()
		move(North)
# 汎用初期化


def init_multi(f):
	back()
	i = get_world_size()
	while i >= 0:
		if spawn_drone(f):
			move(East)
			i -= 1
# デフォルト値として使う


def ever_false():
	return False