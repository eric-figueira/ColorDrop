
class Game:
    def __init__(self, id):
        self.players = []
        self.ready = False
        self.whoIsDead = []
        self.id = id
        self.board = []
        self.message = ""
        self.currentColor = ""

    def get_message(self):
        return self.message

    def get_current_color(self):
        return self.currentColor

    def add_to_deaths(self, player):
        self.whoIsDead.append(player)

    def add_to_game(self, player):
        self.players.append(player)

