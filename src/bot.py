import global_data as g

from random import randint

import board as b
import scan as sc

def place_randomly():
    valid = False
    pos1 = 0
    pos2 = 0
    while not valid:
        pos1 = randint(0, 14)
        pos2 = randint(0, 14)
        if g.boardPositions[pos2][pos1] == 0:
            valid = True
    return pos1, pos2

def analyze():
    """
    *** Roadmap ***
    Scan for immediate danger/win
    Place to create threats/thwart ones
    Place randomly because why not
    *** Order of priority ***
    1. Get 5
    2. Block closed 4
    3. Get close/open 4
    4. Block open 3
    5. Get open 3
    6. Block closed 3
    7. Get closed 3
    8. Get 2 in a row
    9. Place randomly
    """

    # Get 5
    scanned = sc.generate_scan([0, 1, 1, 1, 1], g.bot_color, g.boardPositions)
    if scanned is not None:
        return scanned[0][1][0], scanned[0][1][1] # 1 is list of elements, 2 selects coordinates, 3 is x/y

    # Block closed 4
    scanned = sc.generate_scan([0, 1, 1, 1, 1], g.player_color, g.boardPositions)
    if scanned is not None:
        return scanned[0][1][0], scanned[0][1][1]

    # Get closed/open 4
    scanned = sc.generate_scan([0, 1, 1, 1], g.bot_color, g.boardPositions)
    if scanned is not None:
        return scanned[0][1][0], scanned[0][1][1]

    # Block open 3
    scanned = sc.generate_scan([0, 1, 1, 1, 0], g.player_color, g.boardPositions)
    if scanned is not None:
        return scanned[0][1][0], scanned[0][1][1]

    # Get Open 3
    scanned = sc.generate_scan([0, 1, 1], g.bot_color, g.boardPositions)
    if scanned is not None:
        return scanned[0][1][0], scanned[0][1][1]

    # Block closed 3
    scanned = sc.generate_scan([0, 1, 1, 1, -1], g.player_color, g.boardPositions)
    if scanned is not None:
        return scanned[0][1][0], scanned[0][1][1]

    # Get closed 3
    scanned = sc.generate_scan([0, 1, 1, -1], g.bot_color, g.boardPositions)
    if scanned is not None:
        return scanned[0][1][0], scanned[0][1][1]

    # Get 2 in a row
    scanned = sc.connect2()
    if scanned is not None:
        return scanned[0], scanned[1]

    # Place randomly
    return place_randomly()

def bot_place_stone():
    pos1, pos2 = analyze()
    b.place_stone(pos1, pos2, g.current_player)