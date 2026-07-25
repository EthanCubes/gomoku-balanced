import pygame
import time

import global_data as g
import board as b

def scan_position(base_pos, pos1, pos2, pos3, pos4, board_position):
    base_pos_status = board_position[base_pos[1]][base_pos[0]]
    if base_pos_status == 0:
        return 0
    if pos4[0] < 0 or pos4[0] > 14 or pos4[1] < 0 or pos4[1] > 14:
        return 0
    pos1_status = board_position[pos1[1]][pos1[0]]
    pos2_status = board_position[pos2[1]][pos2[0]]
    pos3_status = board_position[pos3[1]][pos3[0]]
    pos4_status = board_position[pos4[1]][pos4[0]]
    if base_pos_status == pos1_status:
        if base_pos_status == pos2_status:
            if base_pos_status == pos3_status:
                if base_pos_status == pos4_status:
                    return base_pos_status
    return 0

def generate_scan(board_position):
    for y in range(15):
        for x in range(15):
            current_position = (x, y)
            # N
            pos1 = (x, y + 1)
            pos2 = (x, y + 2)
            pos3 = (x, y + 3)
            pos4 = (x, y + 4)
            g.win_line[0] = current_position
            g.win_line[1] = pos4
            if scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == 1:
                return current_position, 1
            elif scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == -1:
                return current_position, -1
            # NE
            pos1 = (x + 1, y + 1)
            pos2 = (x + 2, y + 2)
            pos3 = (x + 3, y + 3)
            pos4 = (x + 4, y + 4)
            g.win_line[0] = current_position
            g.win_line[1] = pos4
            if scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == 1:
                return current_position,1
            elif scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == -1:
                return current_position,-1
            # E
            pos1 = (x + 1, y)
            pos2 = (x + 2, y)
            pos3 = (x + 3, y)
            pos4 = (x + 4, y)
            g.win_line[0] = current_position
            g.win_line[1] = pos4
            if scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == 1:
                return current_position,1
            elif scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == -1:
                return current_position,-1
            # SE
            pos1 = (x + 1, y - 1)
            pos2 = (x + 2, y - 2)
            pos3 = (x + 3, y - 3)
            pos4 = (x + 4, y - 4)
            g.win_line[0] = current_position
            g.win_line[1] = pos4
            if scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == 1:
                return current_position,1
            elif scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == -1:
                return current_position,-1
            # S
            pos1 = (x, y - 1)
            pos2 = (x, y - 2)
            pos3 = (x, y - 3)
            pos4 = (x, y - 4)
            g.win_line[0] = current_position
            g.win_line[1] = pos4
            if scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == 1:
                return current_position,1
            elif scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == -1:
                return current_position,-1
            # Sw
            pos1 = (x - 1, y - 1)
            pos2 = (x - 2, y - 2)
            pos3 = (x - 3, y - 3)
            pos4 = (x - 4, y - 4)
            g.win_line[0] = current_position
            g.win_line[1] = pos4
            if scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == 1:
                return current_position,1
            elif scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == -1:
                return current_position,-1
            # W
            pos1 = (x - 1, y)
            pos2 = (x - 2, y)
            pos3 = (x - 3, y)
            pos4 = (x - 4, y)
            g.win_line[0] = current_position
            g.win_line[1] = pos4
            if scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == 1:
                return current_position,1
            elif scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == -1:
                return current_position,-1
            # NW
            pos1 = (x - 1, y + 1)
            pos2 = (x - 2, y + 2)
            pos3 = (x - 3, y + 3)
            pos4 = (x - 4, y + 4)
            g.win_line[0] = current_position
            g.win_line[1] = pos4
            if scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == 1:
                return current_position,1
            elif scan_position(current_position, pos1, pos2, pos3, pos4, board_position) == -1:
                return current_position,-1
    return None,0

def calculate_win():
    if generate_scan(g.board_positions)[1] != 0:
        b.render()
        pygame.draw.line(g.screen, (255, 0, 0), (g.win_line[0][0] * 45 + 45, g.win_line[0][1] * 45 + 45), (g.win_line[1][0] * 45 + 45, g.win_line[1][1] * 45 + 45), 5)
        pygame.display.flip()
        if generate_scan(g.board_positions)[1] == 1:
            pygame.display.set_caption("Gomuku Swap2: White victory!")
        else:
            pygame.display.set_caption("Gomuku Swap2: Black Victory!")
        time.sleep(1)
        g.mode = 0
        g.reset_board()
    placed_stones = 0
    for y in range(15):
        for x in range(15):
            if g.board_positions[y][x] != 0:
                placed_stones += 1
    if placed_stones == 225:
        b.render()
        pygame.display.flip()
        pygame.display.set_caption("Gomuku Swap2: Draw!")
        time.sleep(1)
        g.mode = 0
        g.reset_board()