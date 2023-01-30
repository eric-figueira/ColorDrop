import random
import pickle
import socket
from _thread import *
from game import Game
from player import Player
from getgame import Getgame

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print(">> Server started on port ", port, "- Waiting for connections")

games = {}
gameId = 0
players = []


def get_random_position(board_size, win_w, win_h, player_size):
    # The player must not spawn in the board or outside the "map"
    x = random.randint(0, win_w - player_size)
    y = random.randint(0, win_h - player_size)
    # Must check if the positions are inside the board
    # If the starting point of the board (top left) is less or equal than the random point and the random point
    # is less or equal than the bottom right point, it means that this location is not allowed
    #                      (top left x, top left y)                             (bottom right x, bottom right, y)
    if (win_w / 2 - board_size / 2, win_h / 2 - board_size / 2) <= (x, y) <= (win_w / 2 + board_size / 2, win_h / 2 + board_size / 2):
        # Must call the function again
        ret = get_random_position(board_size, win_w, win_h, player_size)
        return ret
    else:
        return x, y


def get_player_index(player, gameId):
    for i, p in enumerate(games[gameId].players):
        if p.__eq__(player):
            return i


def connection_supervisor(conn, gameId):
    # Send random x,y to the player
    pos = get_random_position(500, 750, 850, 50)

    p = Player(pos[0], pos[1], 25, 25)
    players.append(p)
    games[gameId].add_to_game(p)
    conn.send(pickle.dumps(p))

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            games[gameId].players[get_player_index(p, gameId)].setAll(data)

            if not data:
                break
            else:
                reply = []
                for player in players:
                    # We want to send back to the client the all the players, but not himself, and we can distinguish
                    # players by their playerId
                    if player.playerId != p.playerId:
                        reply.append(player)
                # Append board

                conn.sendall(pickle.dumps(reply))
        except:
            break

    print("> Lost connection with ", playerId)
    conn.close()
    players.remove(players[playerId])
    global playerIdCount
    playerIdCount -= 1

    # Must check if the game is still valid
    if len(games[gameId].players) == 0:
        try:
            del games[gameId]
            print(">> Closing game ", gameId)
        except:
            pass


while True:
    conn, addr = s.accept()
    print("> Connected to ", addr)
    game_found = False

    for game in games:
        # Add player to game in case we find one. The player will be added in fact into the game
        # in the connection_supervisor
        if not games[game].ready and len(games[game].players) <= 8:
            game_found = True

    # Create a new game otherwise
    if not game_found:
        gameId += 1
        games[gameId] = Game(gameId)
        print(">> Creating game ", gameId)

    # Add a 15 sec timer

    start_new_thread(connection_supervisor, (conn, gameId))
