import pygame
import platform
import os
import sys

from pathlib import Path

if platform.system() == "Windows":
    print("imagine using windows")
    config_dir = Path(os.environ.get("APPDATA", os.path.expanduser("~"))) / "gomoku_swap2"
elif platform.system() == "Darwin":
    print("wise choice")
    config_dir = Path(os.path.expanduser("~/Library/Application Support")) / "gomoku_swap2"
elif platform.system() == "Linux":
    print("i use arch btw")
    config_dir = Path(os.path.expanduser("~/.config")) / "gomoku_swap2"
else:
    print(f"unknown os: {platform.system()}, using fallback directory")
    config_dir = Path(os.path.expanduser("~")) / "gomoku_swap2"
CONFIG_FILE = config_dir / "gomoku_options.txt"

def get_base_path():
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS)
    else:
        # When running normally, go up one level from src to project root
        return Path(__file__).resolve().parent.parent

PROJECT_ROOT = get_base_path()

'''
0: Main menu
1: Play w/ friends
2: Play w/ bot
3: Settings
'''
mode = None

screen = None
img = None
clock = None
running = None

starter = None
bot_color = None
player_color = None
current_player = None

background_music_on = True

win_line = [None, None]

DIRECTION_LIST = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

default_board_positions = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

board_positions = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def button_clicked(start, relative_end):
    end = [0, 0]
    end[0] = start[0] + relative_end[0]
    end[1] = start[1] + relative_end[1]
    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed(3)[0]:
        if start[0] < mouse_pos[0] < end[0] and start[1] < mouse_pos[1] < end[1]:
            return True
        else:
            return False
    return None


def reset_board():
    global board_positions, default_board_positions
    pygame.mixer.music.stop()
    board_positions = [row[:] for row in default_board_positions]

def get_directional_positions(position, direction):
    pos_list = []
    x, y = position
    for i in range(5):
        pos_list.append((x+i*DIRECTION_LIST[direction][0], y+i*DIRECTION_LIST[direction][1]))
    return pos_list