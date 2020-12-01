import socket
import threading

local_host = '127.0.0.1'
port = 55555 

class Client:
    def __init__(self):
        self.nickname = input("Choose nickname:")

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((local_host,port))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occured!")
                #self.client.close()
                break

    def write(self):
        #sending = input("What do you want to send?")
        while True:
            message = f'{self.nickname}:{input("")}'
            self.client.send(message.encode('utf-8'))
        
connection = Client()
receive_thread = threading.Thread(target=connection.receive)
receive_thread.start()

write_thread= threading.Thread(target=connection.write)
write_thread.start()