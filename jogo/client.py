import pygame
import math
from network import Network
from game import Game
from player import Player
from getmessage import Getmessage

pygame.init()
pygame.font.init()

# Basic window configurations
width = 750
height = 850
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Color Drop")

board_size = 500
player_size = 50

# Load Fonts
press_key_font = pygame.font.Font("assets/prstart.ttf", 20)
menu_screen_font = pygame.font.Font("assets/rexlia rg.otf", 90)
message_font = pygame.font.Font("assets/rexlia rg.otf", 30)

# Load Images
menu_screen_bg = pygame.image.load("assets/bg.png").convert_alpha()

# Load Sounds


def sine_wave(speed, time, how_far, overallY):
    t = pygame.time.get_ticks() / 2 % time
    x = t
    y = math.sin(t / speed) * how_far + overallY
    y = int(y)
    return y



def redraw_main_screen(p, players, message):
    win.fill((30, 30, 30))
    # Draw board area
    pygame.draw.rect(win, (10, 10, 10), (width / 2 - board_size / 2, height / 2 - board_size / 2, board_size, board_size))

    # Draw player and other players
    p.draw(win, (207, 181, 59))
    for player in players:
        player.draw(win, (100, 100, 100))

    # Draw message
    text = message_font.render(message, True, (255, 255, 255))
    win.blit(text, (20, height - 50))

    # Draw current color
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    # Must get the game

    # Create a network
    n = Network()
    p = n.getP()

    while run:
        clock.tick(60)
        # Receive other players objects from the server
        players = n.send(p)
        # Receive messages from the server
        message = n.send(Getmessage).get_string()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        p.move(False, (0,0), (0,0), (0,0), (0,0))
        # Players is the array of the other players objects (they will be drawn as
        # gray while the player will be draw with another color)
        redraw_main_screen(p, players, message)


def redraw_menu_screen():
    win.blit(menu_screen_bg, (0, 0))

    y = sine_wave(200.0, 1280, 10.0, 450)

    title = menu_screen_font.render("ColorDrop", True, (255, 255, 255))
    # 120px above "Press key to start"
    win.blit(title, (width / 2 - title.get_width() / 2, y - 120))

    press_key = press_key_font.render("Press any key to start", True, (255, 255, 255))
    win.blit(press_key, (width / 2 - press_key.get_width() / 2, y))


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.KEYDOWN:
                run = False

        redraw_menu_screen()

    main()


while True:
    menu_screen()
