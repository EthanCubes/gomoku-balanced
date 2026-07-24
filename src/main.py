import pygame
import global_data as g
import offline_multiplayer as m
import singleplayer as s

import random

from main_menu import main_menu_loop

pygame.init()
g.screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Gomuku Swap2")
g.img = pygame.image.load(g.PROJECT_ROOT / "assets" / "gomuku-swap2icon.bmp")
pygame.display.set_icon(g.img)
g.clock = pygame.time.Clock()
g.running = True

g.mode = 0

try:
    with open(".gomuku_options.txt") as file:
        data = file.read()
    data = data.split("\n")
    if data[0] == "True" or data[0] == True:
        g.background_music_on = True
    else:
        g.background_music_on = False
except FileNotFoundError:
    print("Settings file not found")

while g.running:
    if g.background_music_on and not pygame.mixer.music.get_busy():
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.unload()
        number = random.randint(1,3)
        if number == 1:
            pygame.mixer.music.load(g.PROJECT_ROOT / "assets" / "music" / "amazingPlan.mp3")
        elif number == 2:
            pygame.mixer.music.load(g.PROJECT_ROOT / "assets" / "music" / "elevatorMusic.mp3")
        else:
            pygame.mixer.music.load(g.PROJECT_ROOT / "assets" / "music" / "schemingWeaselFaster.mp3")
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                g.mode = 0
                g.reset_board()
    if g.mode == 0:
        pygame.display.set_caption("Gomuku Swap2")
        main_menu_loop()
    elif g.mode == 1: # Multiplayer
        pygame.display.set_caption("Gomuku Swap2: Local Multiplayer game")
        m.game_loop()
    elif g.mode == 2: # Singleplayer
        if g.starter == 0:
            pygame.display.set_caption("Gomuku Swap2: Game vs Bot (You are black)")
        else:
            pygame.display.set_caption("Gomuku Swap2: Game vs Bot (You are white)")
        s.game_loop()

    pygame.display.flip()
pygame.quit()