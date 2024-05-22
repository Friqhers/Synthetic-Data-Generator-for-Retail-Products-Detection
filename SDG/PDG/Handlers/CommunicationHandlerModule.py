import socket

class CommunicationHandler:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        print("Connected to the server")

    def send(self, message):
        self.socket.send(message)

    def receive(self):
        return self.socket.recv(1024)

    def close(self):
        self.socket.close()
