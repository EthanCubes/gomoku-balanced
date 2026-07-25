import pygame
import time

import global_data as g
import board as b
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

    # Draw decoration
    pygame.draw.line(g.screen, (0, 0, 0), (0, 660), (60, 720), 5)
    pygame.draw.line(g.screen, (0, 0, 0), (0, 600), (120, 720), 5)
    pygame.draw.line(g.screen, (0, 0, 0), (0, 540), (180, 720), 5)
    pygame.draw.line(g.screen, (0, 0, 0), (0, 480), (240, 720), 5)

    pygame.draw.line(g.screen, (0, 0, 0), (0, 540), (30, 510), 5)
    pygame.draw.line(g.screen, (0, 0, 0), (0, 600), (60, 540), 5)
    pygame.draw.line(g.screen, (0, 0, 0), (0, 660), (90, 570), 5)
    pygame.draw.line(g.screen, (0, 0, 0), (0, 720), (120, 600), 5)
    pygame.draw.line(g.screen, (0, 0, 0), (60, 720), (150, 630), 5)
    pygame.draw.line(g.screen, (0, 0, 0), (120, 720), (180, 660), 5)
    pygame.draw.line(g.screen, (0, 0, 0), (180, 720), (210, 690), 5)

    pygame.draw.circle(g.screen, (0, 0, 0), (180, 660), 17)
    pygame.draw.circle(g.screen, (255, 255, 255), (120, 600), 17)
    pygame.draw.circle(g.screen, (0, 0, 0), (210, 690), 17)
    pygame.draw.circle(g.screen, (255, 255, 255), (150, 690), 17)
    pygame.draw.circle(g.screen, (255, 255, 255), (90, 690), 17)
    pygame.draw.circle(g.screen, (0, 0, 0), (30, 630), 17)

    # "Singleplayer" button
    g.screen.blit(singleplayer, (210, 270))
    button_clicked = g.button_clicked((210, 270), (300, 100))
    if button_clicked:
        pygame.mixer.music.stop()
        g.current_player = 1
        s.setup()
        g.mode = 2
        b.generate_start_pos()
        time.sleep(0.5)

    # "Multiplayer" button
    g.screen.blit(multiplayer, (210, 370))
    button_clicked = g.button_clicked((210, 370), (300, 100))
    if button_clicked:
        pygame.mixer.music.stop()
        b.generate_start_pos()
        g.current_player = 1
        g.mode = 1
        time.sleep(0.5)

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
            time.sleep(0.25)
    else:
        g.screen.blit(music_off, (690, 0))
        button_clicked = g.button_clicked((690, 0), (30, 30))
        if button_clicked:
            g.background_music_on = True
            with open(".gomuku_options.txt", "w") as file:
                file.write("True")
            time.sleep(0.25)