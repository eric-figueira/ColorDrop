import pygame, random

width = 750
height = 750
board_size = 500
has_changed = False
squareSize = 50
colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'purple': (255, 0, 255),
    'cyan': (0, 255, 255),
    'yellow': (255, 255, 0),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'gray': (127, 127, 127),
    'dark_gray': (30, 30, 30)
}

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Board")


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = (self.x, self.y, squareSize, squareSize)
        self.color = self.randomizeColor()
        self.isVisible = True


    def randomizeColor(self):
        randomIndex = random.randint(0, len(colors) - 1)
        return colors[list(colors.keys())[randomIndex]]

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect)



def generateBoard():
    start_x = width // 2 - board_size // 2
    start_y = height // 2 - board_size // 2
    pygame.draw.rect(win, colors['black'],
                     (start_x, start_y, board_size, board_size), 0)
    for row in range(1, board_size // squareSize + 1):
        for col in range(1, board_size // squareSize + 1):
            square = Square(col * start_x, row * start_y)
            square.draw()


def redrawWindow(window):
    window.fill(colors['dark_gray'])
    generateBoard()
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawWindow(win)


main()