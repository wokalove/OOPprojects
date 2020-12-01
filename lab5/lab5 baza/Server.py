import threading
import socket
import sys

local_host = '127.0.0.1'
port = 55555

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((local_host,port))
        self.server.listen()

        self.clients=[]
        self.nicknames=[]

    def broadcast(self,message):
        for client in self.clients:
            client.send(message)

    def handle(self,client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = client.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast(f'{nickname} left the chat!'.encode('utf-8'))
                self.nicknames.remove(nickname)
                break
    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected width {str(address)}")

            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f'Nickname of the client is {nickname}')
            self.broadcast(f'{nickname} joined the chat'.encode('utf-8'))
            client.send("Connected to the server!".encode('utf-8'))

            thread = threading.Thread(target=self.handle,args=(client,))
            thread.start()

print('Server is listening...')
Server().receive()
