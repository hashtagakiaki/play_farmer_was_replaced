import harv
import maze
def counter():
	return get_time() >= 60
maze.maze_sup(counter)
quick_print(num_items(Items.Gold), 1000000000-num_items(Items.Weird_Substance))