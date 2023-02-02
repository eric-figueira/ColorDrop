import random
import pickle
import socket
from _thread import *
from threading import Timer
from game import Game
from player import Player
from getgameinfo import *
from string import String
import time

server = ""
port = 5555

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 850
PLAYER_SIZE = 25
BOARD_SIZE = 500
SQUARE_SIZE = 50

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


def change_game_message(gameId, message):
    games[gameId].message = message


def start_countdown_gamestart(gameId):
    i = 15
    while i >= 1:
        timer = Timer(1, change_game_message, args=(gameId, f"The game starts in {i} seconds!"))
        timer.start()
        time.sleep(1)
        i -= 1
    time.sleep(1)
    change_game_message(gameId, "")
    start_game(gameId)


def start_game(gameId):
    games[gameId].ready = True
    # Teleport the players to the center
    for player in games[gameId].players:
        player.x = WINDOW_WIDTH / 2 - PLAYER_SIZE
        player.y = WINDOW_HEIGHT / 2 - PLAYER_SIZE
    # While the game exists
    while gameId in games:
        # Randomize new color
        games[gameId].randomize_color()
        # Waits 2 seconds to make the others squares black
        time.sleep(2)
        games[gameId].make_squares_black()
        # Send "Getispositionsafe" that will tell the client whether it is in a black square or not
        # Wait 3 seconds to make a new board
        time.sleep(3)
        games[gameId].currentColor = ""
        games[gameId].generate_new_board()
        time.sleep(2)


def connection_supervisor(conn, gameId):
    # Send random x,y to the player
    pos = get_random_position(BOARD_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER_SIZE)

    p = Player(pos[0], pos[1], PLAYER_SIZE, PLAYER_SIZE)
    games[gameId].add_to_game(p)
    # If, when the player is added to the game, the number of players is equal than two,
    # we must start the timer to start the game
    if len(games[gameId].players) == 2:
        start_new_thread(start_countdown_gamestart, (gameId,))

    conn.send(pickle.dumps(p))

    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if not data:
                break
            else:
                if data is Getmessage:
                    # Wants message
                    conn.sendall(pickle.dumps(String(games[gameId].message)))
                elif data is Getgamestatus:
                    # Wants to know if the game has started
                    has_started = 0
                    if games[gameId].ready:
                        has_started = 1
                    conn.sendall(pickle.dumps(String(has_started)))
                elif data is Getcolor:
                    # Wants the randomized color
                    conn.sendall(pickle.dumps(String(games[gameId].get_current_color())))
                elif data is Getsquares:
                    # Wants the board's squares
                    conn.sendall(pickle.dumps(games[gameId].get_board()))
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
        games[gameId] = Game(gameId, WINDOW_WIDTH, WINDOW_HEIGHT, BOARD_SIZE, SQUARE_SIZE)
        print(">> Creating game ", gameId)

    start_new_thread(connection_supervisor, (conn, gameId))
