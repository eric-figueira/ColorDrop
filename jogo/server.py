from network import Network
import socket
from _thread import *

server = "UPDATE ME!"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print(">> Server started on port ", port, ". Waiting for connections")

games = {}
playerIdCount = 0


def connection_supervisor(conn):
    pass

while True:
    conn, addr = s.accept()
    print("> Connected to ", addr)


    start_new_thread(connection_supervisor, (conn,))

