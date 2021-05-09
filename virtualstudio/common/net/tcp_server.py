import socket
from threading import Thread

from .messagetools import *

class TCPServer(Thread):
    def __init__(self, listenAddress="", port=4400):
        super().__init__()
        self.listeningAddress = listenAddress
        self.port = port
        self.running = False

        self.flags = socket.NI_NUMERICHOST | socket.NI_NUMERICSERV

        self.connection = None
        self.buffersize = 16384
        self.messageStub = None

    def __str__(self):
        return "TCP Server at " + str(self.listeningAddress) + ":" + str(self.port)

    def requestStop(self):
        self.running = False

    def run(self) -> None:

        self.running = True
        # create an instance of socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind the socket to its host and port
        self.sock.bind((self.listeningAddress, self.port))

        while self.running:
            self.sock.listen(1)
            self.connection, clientAddress = self.sock.accept()
            self.messageStub = None
            address, port = socket.getnameinfo(clientAddress, self.flags)
            try:
                while True:
                    data = self.connection.recv(self.buffersize) # 16 kb buffer
                    if len(data) < 4:
                        continue

                    self.messageStub, complete = assembleMessage(self.messageStub, data)

                    if complete:
                        self.onMessageRecv(self.messageStub)
                        self.messageStub = None

            except ConnectionResetError:
                pass # Ignore
            finally:
                self.connection.close()

    def onMessageRecv(self, message: bytes):
        pass

    def sendMessage(self, message: bytes):
        if self.connection is not None:
            messages = disassembleMessage(message)
            for packet in messages:
                self.connection.sendall(packet)
