from threading import Thread
import socket

from.messagetools import *


class TCPClient(Thread):

    def __init__(self, address="127.0.0.1", port=4233):
        super().__init__()

        self.address = address
        self.port = port

        self.sock = None
        self.timeout: Optional[float] = None
        self.running = False

        self.messageStub = None

    def __str__(self):
        return "TCP Client connected to " + str(self.address) + ":" + str(self.port)

    def setTimeout(self, timeout: Optional[float]):
        self.timeout = timeout
        if self.sock is not None:
            self.sock.settimeout(timeout)

    def requestStop(self):
        self.running = False

    def run(self) -> None:
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)

        self.sock.connect((self.address, self.port))
        self.messageStub = None
        try:
            while self.running:
                data = self.sock.recv(16384) # 16 kb buffer
                if len(data) < 4:
                    continue
                self.messageStub, complete = assembleMessage(self.messageStub, data)

                if complete:
                    self.onMessageRecv(self.messageStub)
                    self.messageStub = None
        finally:
            self.sock.close()

    def onMessageRecv(self, message: bytes):
        pass

    def sendMessage(self, message: bytes):
        if self.sock is not None:
            messages = disassembleMessage(message)
            for packet in messages:
                self.sock.sendall(packet)