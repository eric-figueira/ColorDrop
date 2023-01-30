import pygame, random

width = 750
height = 850

board_size = 500
squareSize = 50
start_board_x = width // 2 - board_size // 2
start_board_y = height // 2 - board_size // 2


has_changed = False

colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'purple': (255, 0, 255),
    'cyan': (0, 255, 255),
    'yellow': (255, 255, 0),
    'orange': (255, 165, 0),
    'white': (255, 255, 255),
    'gray': (127, 127, 127),
    'dark_gray': (30, 30, 30),
    'black': (0, 0, 0)
}

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Board")


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = (self.x, self.y, squareSize, squareSize)
        self.color = self.randomize_color()
        self.isVisible = True

    def randomize_color(self):
        randomIndex = random.randint(0, len(colors) - 3) # -3 because i dont want the color of the square to be black or gray
        return colors[list(colors.keys())[randomIndex]]

    def set_new_color(self):
        self.color = self.randomize_color()

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect)



arraySquares = []
def create_squares():
    # This function is responsible to initialize the squares: set their position and add them to the array, nothing more
    for row in range(0, board_size // squareSize):
        for col in range(0, board_size // squareSize):
            square = Square(col * squareSize + start_board_x, row * squareSize + start_board_y)
            arraySquares.append(square)


def generate_board():
    # Generate a new board, that means change the square's color
    for sqr in arraySquares:
        sqr.setNewColor()


def redraw_window(window):
    window.fill(colors['dark_gray'])
    pygame.draw.rect(win, colors['black'],
                     (start_board_x, start_board_y, board_size, board_size), 0)
    for sqr in arraySquares:
        if sqr.isVisible:
            sqr.draw()
    pygame.display.update()





def main():
    run = True
    create_squares()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redraw_window(win)


main()