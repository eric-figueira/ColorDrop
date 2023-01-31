import random
import pickle
import socket
from _thread import *
from game import Game
from player import Player
from getmessage import Getmessage
from string import String

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


def get_random_position(board_size, win_w, win_h, player_size):
    # The player must not spawn in the board or outside the "map"
    x = random.randint(0, win_w - player_size)
    y = random.randint(0, win_h - player_size)
    # Must check if the positions are inside the board
    # If the starting point of the board (top left) is less or equal than the random point and the random point
    # is less or equal than the bottom right point, it means that this location is not allowed
    #                      (top left x, top left y)                             (bottom right x, bottom right y)
    if (win_w / 2 - board_size / 2, win_h / 2 - board_size / 2) < (x + player_size, y + player_size) < (win_w / 2 + board_size / 2, win_h / 2 + board_size / 2):
        # Must call the function again
        ret = get_random_position(board_size, win_w, win_h, player_size)
        return ret
    else:
        return x, y


def get_player_index(player, gameId):
    for i, p in enumerate(games[gameId].players):
        if p is player:
            return i


def connection_supervisor(conn, gameId):
    # Send random x,y to the player
    pos = get_random_position(500, 750, 850, 25)

    p = Player(pos[0], pos[1], 25, 25)
    games[gameId].add_to_game(p)
    conn.send(pickle.dumps(p))

    message = "Hello World!"

    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if not data:
                break
            else:
                if data is Getmessage:
                    # Wants message
                    conn.sendall(pickle.dumps(String(message)))
                else:
                    # Wants other player's locations and set its new position
                    games[gameId].players[get_player_index(p, gameId)].setAll(data)

                    reply = []

                    for player in games[gameId].players:
                        # We want to send back to the client the all the players, but not itself, and we can difer than
                        # by their indexes in the game's players array
                        if get_player_index(player, gameId) != get_player_index(p, gameId):
                            reply.append(player)
                    # Append board
                    conn.sendall(pickle.dumps(reply))
        except:
            break

    print("> Lost connection with ", p)
    conn.close()
    games[gameId].players.remove(p)

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
            break
            
    if not game_found:
        gameId += 1
        games[gameId] = Game(gameId)
        print(">> Creating game ", gameId)

    # Add a 15 sec timer

    start_new_thread(connection_supervisor, (conn, gameId))
