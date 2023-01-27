import pygame
import math

pygame.init()
pygame.font.init()

# Basic window configurations
width = 750
height = 850
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Color Drop")

# Load Fonts
press_key_font = pygame.font.Font("prstart.ttf", 20)
menu_screen_font = pygame.font.Font("rexlia rg.otf", 90)

# Load Images
menu_screen_bg = pygame.image.load("bg.png").convert_alpha()

# Load Sounds


def sine_wave(speed, time, how_far, overallY):
    t = pygame.time.get_ticks() / 2 % time
    x = t
    y = math.sin(t / speed) * how_far + overallY
    y = int(y)
    return y


def redraw_main_screen():
    win.fill((255, 255, 255))


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

        redraw_main_screen()


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
