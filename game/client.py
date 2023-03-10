import time
import pygame
import math
from network import Network
from getgameinfo import *

pygame.init()
pygame.font.init()

# Basic window configurations
width = 750
height = 850
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("ColorDrop")

board_size = 500


# Load Fonts
press_key_font = pygame.font.Font("assets/prstart.ttf", 20)
menu_screen_font = pygame.font.Font("assets/rexlia rg.otf", 90)
message_font = pygame.font.Font("assets/rexlia rg.otf", 30)
color_font = pygame.font.Font("assets/rexlia rg.otf", 45)

# Load Images
menu_screen_bg = pygame.image.load("assets/bg.png").convert_alpha()
pygame.display.set_icon(pygame.image.load("assets/logo.png"))


def sine_wave(speed, time, how_far, overallY):
    t = pygame.time.get_ticks() / 2 % time
    x = t
    y = math.sin(t / speed) * how_far + overallY
    y = int(y)
    return y

def redraw_game_stats_screen(status):
    win.fill((30, 30, 30))

    # Show message
    if status:
        fir_text = message_font.render("You Lost!", True, (247, 69, 49))
        sec_text = message_font.render("You fell into the void!", True, (210, 214, 210))
    else:
        fir_text = message_font.render("You Won!", True, (121, 252, 136))
        sec_text = message_font.render("You were the last player standing!", True, (210, 214, 210))

    win.blit(fir_text, (width / 2 - fir_text.get_width() / 2, height / 2 - 150))
    win.blit(sec_text, (width / 2 - sec_text.get_width() / 2, height / 2 - 100))

    # Play again message
    y = sine_wave(200.0, 1280, 10.0, height / 2 + 50)

    text = press_key_font.render("Press any key to play again!", True, (255, 255, 255))
    win.blit(text, (width / 2 - text.get_width() / 2, y))

    pygame.display.update()


def game_stats_screen(status):
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                run = False
                break

        redraw_game_stats_screen(status)



def redraw_main_screen(p, players, message, color, board, has_started, dead_players):
    win.fill((30, 30, 30))
    # Draw board area
    pygame.draw.rect(win, (10, 10, 10), (width / 2 - board_size / 2, height / 2 - board_size / 2, board_size, board_size))

    # Draw message
    msg_text = message_font.render(message, True, (255, 255, 255))
    win.blit(msg_text, (20, height - 50))

    # Draw current color
    if has_started:
        color_text = color_font.render("Color: " + color, True, (255, 255, 255))
        win.blit(color_text, (width / 2 - color_text.get_width() / 2, 50))

    # Draw the board
    if has_started:
        for square in board:
            square.draw(win)

    # Draw player and other players
    if not p.is_dead:
        p.draw(win, (207, 181, 59))

    dead_players_ids = []
    for pl in dead_players:
        if pl.id != p.id:
            dead_players_ids.append(pl.id)
    for player in players:
        if player.id not in dead_players_ids:
            player.draw(win, (100, 100, 100))

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    # Create a network
    n = Network()
    p = n.getP()
    prev_game_status = 0

    while run:
        clock.tick(60)
        # Receive other players objects from the server and check if the current position is safe
        players = n.send(p)

        # Getmessage, Getgamestatus, Getcolor and Getsquares are empty classes
        # that allow the server know what the client wants.

        # Receive messages from the server
        message = n.send(Getmessage).get_string()
        # Receive game status
        has_game_started = int(n.send(Getgamestatus).get_string())

        if has_game_started == 1 and has_game_started != prev_game_status:
            # Teleport players to the center
            p.x = width / 2 - p.width / 2
            p.y = height / 2 - p.height / 2

            prev_game_status = 1

        # Receive random color
        color = n.send(Getcolor).get_string()
        # Receive board
        board = n.send(Getsquares)

        # Receive dead players
        dead_players = n.send(Getdeadplayers)
        for pl in dead_players:
            if p.id == pl.id:
                p.is_dead = True
                message = "You fell into the void!"

        if has_game_started:
            if len(dead_players) == len(players):
                # The game ended since every other player fell into the void
                time.sleep(2)
                game_stats_screen(p.is_dead)
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        p.move(has_game_started,
               (width / 2 - board_size / 2, height / 2 - board_size / 2),
               (width / 2 + board_size / 2, height / 2 - board_size / 2),
               (width / 2 - board_size / 2, height / 2 + board_size / 2),
               (width / 2 + board_size / 2, height / 2 + board_size / 2),
               width, height)
        # Players is the array of the other players objects (they will be drawn as
        # gray while the player will be drawn with another color)
        redraw_main_screen(p, players, message, color, board, has_game_started, dead_players)


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
