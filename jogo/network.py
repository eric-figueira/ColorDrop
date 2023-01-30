import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "UPDATE ME!"
        self.port = 5555
        self.addr = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass
