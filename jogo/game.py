
class Game:
    def __init__(self, id):
        self.players = []
        self.posPlayers = []
        self.ready = False
        self.whoIsDead = []
        self.id = id
        self.board = []

    def add_to_deaths(self, playerId):
        self.whoIsDead.append(playerId)

    def add_to_game(self, playerId):
        self.players.append(playerId)

