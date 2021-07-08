from threading import Thread, Lock
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

        self.sendLock = Lock()

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
                length = self.sock.recv(4)  # 16 kb buffer
                if len(length) < 4:
                    continue
                data = self.sock.recv(getInt(length, start=0))
                print("Message Recieved: {:08X} {}".format(getInt(length, start=0), str(data)))
                self.onMessageRecv(data)

                #for msg in messages:
                #    self.onMessageRecv(msg)

        except ConnectionAbortedError:
            pass # Socket closed by another thread
        finally:
            self.sock.close()

    def onMessageRecv(self, message: bytes):
        pass

    def sendMessage(self, message: bytes):
        if self.sock is not None:
            messages = disassembleMessage(message)
            self.sendLock.acquire()
            try:
                for packet in messages:
                    self.sock.sendall(packet)
            finally:
                self.sendLock.release()

    def closeConnection(self):
        self.sock.close()
