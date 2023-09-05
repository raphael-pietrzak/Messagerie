from random import choice
import socket
import threading

HOST = "localhost"
PORT = 12345



class UDPServer:
    def __init__(self):
        self.server_socket = None
        self.clients = []

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((HOST, PORT))
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            data, client_address = self.server_socket.recvfrom(1024)
            message = data.decode()

            if client_address not in self.clients:
                self.clients.append(client_address)


            print(f"{client_address}: {message}")

            # Envoyer le message à tous les clients connectés
            for client in self.clients:
                if client != client_address and message != "REGISTER":
                    self.server_socket.sendto(data, client)

    def stop(self):
        self.server_socket.close()



if __name__ == "__main__":

    server = UDPServer()
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    while True:
        command = input("Entrez 'exit' pour quitter le serveur : ")
        if command == "exit":
            server.stop()
            server_thread.join()
            break

