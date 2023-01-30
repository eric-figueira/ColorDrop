class Game:
    def __init__(self, id):
        self.numPlayers = 0
        self.posPlayers = []
        self.ready = False
        self.whoIsDead = []
        self.id = id

    def addToDeaths(self, playerId):
        self.whoIsDead.append(playerId)

