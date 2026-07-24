import time

import pygame

import global_data as g
import board as b
from time import sleep
import singleplayer as s

title = pygame.image.load(g.PROJECT_ROOT / "assets" / "title.bmp")
singleplayer = pygame.image.load(g.PROJECT_ROOT / "assets" / "playWithBot.bmp")
multiplayer = pygame.image.load(g.PROJECT_ROOT / "assets" / "playWFriends.bmp")
quit_button = pygame.image.load(g.PROJECT_ROOT / "assets" / "quit.bmp")
music_on = pygame.image.load(g.PROJECT_ROOT / "assets" / "music_on.bmp")
music_off = pygame.image.load(g.PROJECT_ROOT / "assets" / "music_off.bmp")

def main_menu_loop():
    g.screen.fill("peru")

    g.screen.blit(title, (210, 90))

    # "Singleplayer" button
    g.screen.blit(singleplayer, (210, 270))
    button_clicked = g.button_clicked((210, 270), (300, 100))
    if button_clicked:
        pygame.mixer.music.stop()
        g.currentPlayer = 1
        s.setup()
        g.mode = 2
        b.generate_start_pos()
        sleep(0.5)

    # "Multiplayer" button
    g.screen.blit(multiplayer, (210, 370))
    button_clicked = g.button_clicked((210, 370), (300, 100))
    if button_clicked:
        pygame.mixer.music.stop()
        b.generate_start_pos()
        g.currentPlayer = 1
        g.mode = 1
        sleep(0.5)

    # Quit game button
    g.screen.blit(quit_button, (210, 470))
    button_clicked = g.button_clicked((210, 470), (300, 80))
    if button_clicked:
        pygame.mixer.music.stop()
        g.running = False

    # Music toggle
    if g.background_music_on:
        g.screen.blit(music_on, (690, 0))
        button_clicked = g.button_clicked((690, 0), (30, 30))
        if button_clicked:
            g.background_music_on = False
            with open(".gomuku_options.txt", "w") as file:
                file.write("False")
            pygame.mixer_music.stop()
            time.sleep(0.1)
    else:
        g.screen.blit(music_off, (690, 0))
        button_clicked = g.button_clicked((690, 0), (30, 30))
        if button_clicked:
            g.background_music_on = True
            with open(".gomuku_options.txt", "w") as file:
                file.write("True")
            time.sleep(0.1)