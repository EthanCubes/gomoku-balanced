import random

import global_data as g

def scan_board(x, y, pattern): # now this is the hard part.
    reverse = []
    for item in pattern:
        reverse.append(-item)
    dlist = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)] # set up scanning in all 8 directions
    scan_list = []
    # Gets the status and puts it in a list
    for direction in dlist:
        dir_scan_list = [] # directional scan
        for i in range(6):
            dir_scan_list.append((x+i*int(direction[0]), y+i*int(direction[1])))
        status_list = []
        for item in dir_scan_list:
            if not (item[0] < 0 or item[0] > 14 or item[1] < 0 or item[1] > 14):
                status_list.append(g.boardPositions[item[1]][item[0]])
        scan_list.append(status_list)
    # Compares the list to the given pattern
    for item in scan_list:
        if item == pattern:
            return 1
        elif item == reverse:
            return -1
    return None

def generate_scan(pattern, color): # pattern has to be 6 characters.
    items = 0
    pos_list = []
    for y in range(15):
        for x in range(15):
            scan = scan_board(x, y, pattern)
            if scan == -1 or scan == 1:
                items += 1
                pos_list.append((scan, (x, y))) # Appends to the list color of the combination and the coordinates.
    whitelist = []
    blacklist = []
    if items > 0:
        if color != 0:
            for item in pos_list:
                if item[0] == 1:
                    whitelist.append(item)
                else:
                    blacklist.append(item)
            if color == 1:
                return whitelist if whitelist else None
            elif color == -1:
                return blacklist if blacklist else None
        else:
            return pos_list
    return None

# This function is like pretty good for now, doesn't need to be changed.
def connect2():
    valid = False
    while not valid:
        direction = random.randint(0,7)
        dlist = [(0,1),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
        x = random.randint(0,14)
        y = random.randint(0,14)
        if g.boardPositions[y][x] == g.botColor:
            y += dlist[direction][1]
            x += dlist[direction][0]
            if x < 0 or x > 14 or y < 0 or y > 14:
                continue
            if g.boardPositions[y][x] == 0:
                return x, y
    return None