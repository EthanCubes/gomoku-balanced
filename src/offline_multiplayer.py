from win import *
import global_data as g
import board as b

def game_loop():
    b.user_place_stone()
    b.render()
    calculate_win()
    g.clock.tick(30)