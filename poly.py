import harv
import carrot
import sun


def poly_copydrone():
    dict_comp = {}
    while True:
        a = get_pos_x(), get_pos_y()
        harvest()
        if a in dict_comp:
            tar = dict_comp[a]
            if tar == Entities.Bush:
                if get_ground_type() != Grounds.Grassland:
                    till()
            else:
                if get_ground_type() != Grounds.Soil:
                    till()
                plant(tar)
        else:
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Carrot)
        b = get_companion()
        if b != None:
            dict_comp[b[1]] = b[0]
        harv.general_process()


def poly(b=harv.ever_false):
    if not b():
        harv.init_multi(poly_copydrone)
        harv.back()
        dict_comp = {}
        while not b():
            if spawn_drone(poly_copydrone):
                move(East)
                
def poly_sup(b=harv.ever_false):
    def a1():
        if num_unlocked(Unlocks.Sunflowers) == 0:
            return b()
        else:
            return b() or num_items(Items.Power) == 0
    while not b():
        if not a1():
            if num_unlocked(Unlocks.Megafarm) == 0:
                poly(a1)
            else:
                poly(a1)
        if num_unlocked(Unlocks.Sunflowers) != 0:
            sun.sun_sup(b)