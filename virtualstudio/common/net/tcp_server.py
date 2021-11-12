import socket
from threading import Thread, Lock

from .messagetools import *
from ..logging import logengine


class TCPServer(Thread):
    def __init__(self, listenAddress="", port=4400):
        super().__init__()
        self.listeningAddress = listenAddress
        self.port = port
        self.running = False

        self.flags = socket.NI_NUMERICHOST | socket.NI_NUMERICSERV

        self.sendLock = Lock()

        self.connection = None
        self.buffersize = 16384
        self.messageStub = None

        self.logger = logengine.getLogger()

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
                    length = self.connection.recv(4) # 16 kb buffer
                    if len(length) < 4:
                        continue
                    data = self.connection.recv(getInt(length, start=0))
                    self.logger.debug("Message Recieved: {:08X} {}".format(getInt(length, start=0), str(data)))
                    self.onMessageRecv(data)
                    #self.messageStub, messages = assembleMessage(self.messageStub, data)

                    #for msg in messages:
                        #self.onMessageRecv(msg)

            except ConnectionResetError:
                pass # Ignore
            finally:
                self.connection.close()

    def onMessageRecv(self, message: bytes):
        pass

    def sendMessage(self, message: bytes):
        if self.connection is not None:
            messages = disassembleMessage(message)
            self.sendLock.acquire()
            try:
                for packet in messages:
                    self.logger.debug("Message Sent:     {:08X} {}".format(getInt(packet, start=0), str(packet[4:])))
                    self.connection.sendall(packet)
            finally:
                self.sendLock.release()
