import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 3000
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            # The server will return a player object
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            # send and receive an object
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096 * 8))
        except socket.error as e:
            print(e)
