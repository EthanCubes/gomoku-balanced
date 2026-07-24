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
    scanned = [sc.generate_scan([0, 1, 1, 1, 1, 0], g.botColor), sc.generate_scan([0, 1, 1, 1, 1, -1], g.botColor)]
    for item in scanned:
        if item is not None:
            return item[0][1][0], item[0][1][1]
    scanned.clear()
    # Block closed 4
    scanned.append(sc.generate_scan([0, 1, 1, 1, 1, -1], g.playerColor))
    for item in scanned:
        if item is not None:
            return item[0][1][0], item[0][1][1]
    scanned.clear()
    # Get closed/open 4
    scanned.append(sc.generate_scan([0, 1, 1, 1, 0, 0], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 1, 0, -1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 1, -1, 0], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 1, -1, 1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 1, -1, -1], g.botColor))
    for item in scanned:
        if item is not None:
            return item[0][1][0], item[0][1][1]
    scanned.clear()
    # Block open 3
    scanned.append(sc.generate_scan([0, 1, 1, 1, 0, 0], g.playerColor))
    scanned.append(sc.generate_scan([0, 1, 1, 1, 0, -1], g.playerColor))
    for item in scanned:
        if item is not None:
            return item[0][1][0], item[0][1][1]
    scanned.clear()
    # Get Open 3
    scanned.append(sc.generate_scan([0, 1, 1, 0, 0, 0], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 0, 0, 1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 0, 0, -1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 0, 1, 0], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 0, 1, 1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 0, 1, -1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 0, -1, 0], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 0, -1, 1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, 0, -1, -1], g.botColor))
    for item in scanned:
        if item is not None:
            return item[0][1][0], item[0][1][1]
    scanned.clear()
    # Block closed 3
    scanned.append(sc.generate_scan([0, 1, 1, 1, -1, 0], g.playerColor))
    scanned.append(sc.generate_scan([0, 1, 1, 1, -1, 1], g.playerColor))
    scanned.append(sc.generate_scan([0, 1, 1, 1, -1, -1], g.playerColor))
    for item in scanned:
        if item is not None:
            return item[0][1][0], item[0][1][1]
    # Get closed 3
    scanned.append(sc.generate_scan([0, 1, 1, -1, 0, 0], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, -1, 0, 1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, -1, 0, -1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, -1, 1, 0], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, -1, 1, 1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, -1, 1, -1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, -1, -1, 0], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, -1, -1, 1], g.botColor))
    scanned.append(sc.generate_scan([0, 1, 1, -1, -1, -1], g.botColor))
    for item in scanned:
        if item is not None:
            return item[0][1][0], item[0][1][1]
    scanned.clear()
    # Get 2 in a row
    scanned.append(sc.connect2())
    for item in scanned:
        if item is not None:
            return item[0], item[1]
    scanned.clear()
    # Place randomly
    return place_randomly()

def bot_place_stone():
    pos1, pos2 = analyze()
    b.place_stone(pos1, pos2, g.currentPlayer)