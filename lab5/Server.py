import threading
import socket
import sys
import os

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

    def receive_text(self):
        print("Receiving text!")
        while True:
            client, address = self.server.accept()
            print(f"Connected width {str(address)}")

            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f'Nickname of the client is {nickname}')
            self.broadcast(f'{nickname} joined the chat'.encode('utf-8'))
            client.send("\nConnected to the server!".encode('utf-8'))

            thread = threading.Thread(target=self.handle,args=(client,))
            thread.start()

    def receive_img(self):
        print("Receiving img!")
        f = open('image_to_receive.png','wb')
        size = 262224
        while True:
            c, addr = self.server.accept()     
            print('Got connection from', addr)
            print ("Receiving...")
            l = c.recv(size)
            while (l):
                print ("Receiving...")
                f.write(l)
                l = c.recv(size)
            f.close()
            print ("Done Receiving")
            c.send('Thank you for connecting')
            c.close()     
    def receive_wav(self):
        print("Receiving wav!")
        f = open('sound_received.wav','wb')
        size = 6078
        while True:
            c, addr = self.server.accept()     
            print('Got connection from', addr)
            print ("Receiving...")
            l = c.recv(size)
            while (l):
                print ("Receiving...")
                f.write(l)
                l = c.recv(size)
            f.close()
            print ("Done Receiving")
            c.send('Thank you for connecting')
            c.close()   

    def receive_data(self):
        client_socket, address = self.server.accept()
        f = open('image_to_receive.png','wb')
        print("Conencted to - ",address,"\n")
        while (1):
            choice = client_socket.recv(1024)
            choice = int(choice)
            print(choice)
            if(choice==1):
               self.receive_text()
            elif(choice == 2):
               self.receive_img()
            elif(choice == 3):
                self.receive_wav()

print('Server is listening...')
Server().receive_data()