import json
from random import choice
import socket
import threading

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

firstnames = ["John", "Paul", "George", "Ringo", "Jesse", "Joe", "Bob",]
lastnames = ["Starr", "McCartney", "Harrison", "King", "Hendrix", "Mason", "Thompson",]

class UDPClient:
    def __init__(self, receive_message):
        self.receive_message = receive_message
        self.pseudo = choice(firstnames) + " " + choice(lastnames)
        self.client_socket = None
        self.receive_thread = None
        self.running = False

    def start(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.running = True
        self.receive_thread = threading.Thread(target=self.receive_data)
        self.receive_thread.start()
        self.send("REGISTER")


    def stop(self):
        self.running = False
        self.receive_thread.join()
        self.client_socket.close()

    def send(self, message):
        self.client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    def receive_data(self):
        while self.running:
            try:
                data, server_address = self.client_socket.recvfrom(1024)
                # print(f"Received from {server_address}: {data.decode()}")
                print(data.decode())
                self.receive_message(data.decode())

            except OSError:
                break


