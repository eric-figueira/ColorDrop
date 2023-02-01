from square import Square


class Game:
    def __init__(self, id):
        self.players = []
        self.ready = False
        self.whoIsDead = []
        self.id = id
        self.board = self.create_squares()
        self.message = ""
        self.currentColor = ""
        self.colors = {
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

    def get_message(self):
        return self.message

    def get_current_color(self):
        return self.currentColor

    def add_to_deaths(self, player):
        self.whoIsDead.append(player)

    def add_to_game(self, player):
        self.players.append(player)

    def create_squares(self):
            # for row in range(0, self.boardW // self.squareSize):
        #     for col in range(0, self.boardH // self.squareSize):
        #         square = Square(col * squareSize + start_board_x, row * squareSize + start_board_y)
        #         arraySquares.append(square)

    def generate_new_board(self):
        for sqr in self.board:
            sqr.set_new_color(self.colors)


