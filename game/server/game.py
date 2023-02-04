from square import Square
import random


class Game:
    def __init__(self, id, win_w, win_h, board_size, square_size):
        self.players = []
        self.ready = False
        self.id = id
        self.deadPlayers = []
        self.window_width = win_w
        self.window_height = win_h
        self.board_size = board_size
        self.square_size = square_size
        self.message = ""
        self.currentColor = ""
        self.colors = {
            'Red': (255, 0, 0),
            'Green': (0, 255, 0),
            'Blue': (0, 0, 255),
            'Purple': (255, 0, 255),
            'Cyan': (0, 255, 255),
            'Yellow': (255, 255, 0),
            'Orange': (255, 165, 0),
            'White': (255, 255, 255),
            'Gray': (127, 127, 127),
            'Dark_gray': (30, 30, 30),
            'Black': (0, 0, 0)
        }
        self.board = self.create_squares()

    def get_board(self):
        return self.board

    def get_message(self):
        return self.message

    def get_current_color(self):
        return self.currentColor

    def add_to_deaths(self, player):
        self.deadPlayers.append(player)

    def get_deadPlayers(self):
        return self.deadPlayers

    def add_to_game(self, player):
        self.players.append(player)

    def create_squares(self):
        aux = []
        for row in range(0, self.board_size // self.square_size):
            for col in range(0, self.board_size // self.square_size):
                square = Square(col * self.square_size + (self.window_width / 2 - self.board_size / 2),
                                row * self.square_size + (self.window_height / 2 - self.board_size / 2),
                                self.square_size, self.square_size, self.colors)
                aux.append(square)
        return aux

    def generate_new_board(self):
        for sqr in self.board:
            sqr.set_new_color(self.colors)

    def randomize_color(self):
        # off will control how many colors will NOT be available
        randomIndex = random.randint(0, len(self.colors) - 1 - 2)
        self.currentColor = list(self.colors.keys())[randomIndex]

    def make_squares_black(self):
        for sqr in self.board:
            if sqr.color != self.colors[self.currentColor]:
                sqr.color = self.colors["Black"]
