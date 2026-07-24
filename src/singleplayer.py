from random import randint

from win import *

import global_data as g
import board as b
import bot

def setup():
    g.starter = randint(0, 1) # 0 is bot, 1 is human
    if g.starter == 0:
        g.botColor = 1
        g.playerColor = -1
    else:
        g.botColor = -1
        g.playerColor = 1

def game_loop():
    if g.currentPlayer == 1:
        if g.starter == 0:
            bot.bot_place_stone()
        else:
            b.user_place_stone()
    else:
        if g.starter == 0:
            b.user_place_stone()
        else:
            bot.bot_place_stone()
    b.render()
    calculate_win()
    g.clock.tick(30)