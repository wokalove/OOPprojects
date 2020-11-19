import threading
import socket
import sys

local_host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((local_host,port))
server.listen()

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected width {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print('Server is listening...')
receive()