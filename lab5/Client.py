import socket
import threading
from abc import ABC, abstractmethod
import os
import tqdm
from pathlib import Path

local_host = '127.0.0.1'
port = 55555 

BUFFER_SIZE = 4096

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
                self.client.close()
                break
    @staticmethod
    def write():
        while True:
            option = input("What do you want to send? 1. Text 2.Image 3. Sound file\n")
            option = int(option)
            if(option==2):
                Image(option).threads()
            elif(option==1):
                Text(option).threads()
            elif(option==3):
                Sound(option).threads()

class TemplateClass(ABC):
    @abstractmethod
    def send(self):
        pass
    @abstractmethod
    def receive(self):
        pass
    def threads(self):
        
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread= threading.Thread(target=self.send)
        write_thread.start()
        
class Text(Client,TemplateClass):
    def __init__(self,option):
        self.client = Client()
        self.client.client.send(repr(option).encode())
    def send(self):
        while True:
            message = f'{self.client.nickname}:{input("")}'
            self.client.client.send(message.encode('utf-8'))

    def receive(self):
        while True:
            try:
                message = self.client.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occured!")
                self.client.client.close()
                break
   
class Image(Client,TemplateClass):
    def __init__(self,option):
        self.client = Client().client
        self.client.send(repr(option).encode())

    def send(self):
        print('Sending file...')
        f = open('image_to_send.png','rb')
        size = Path('image_to_send.png').stat().st_size

        l = f.read(size)
        print("Size:",size)
        while (l):
            print ('Sending...')
            self.client.send(l)
            l = f.read(size)
        f.close()

        print("Done sending")
        self.client.shutdown(socket.SHUT_WR)
        print(self.client.recv(size))
        self.client.close()

    def receive(self):
        while True:
            try:
                message = self.client.recv(BUFFER_SIZE).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occured!")
                self.client.close()
                break


class Sound(Client,TemplateClass):
    def __init__(self,option):
        self.client = Client().client
        self.client.send(repr(option).encode())

    def send(self):
        file_name = 'sound.wav'
        print('Sending file...')
        f = open(file_name,'rb')
        size = Path(file_name).stat().st_size

        l = f.read(size)
        print("Size:",size)
        while (l):
            print ('Sending...')
            self.client.send(l)
            l = f.read(size)
        f.close()

        print("Done sending")
        self.client.shutdown(socket.SHUT_WR)
        print(self.client.recv(size))
        self.client.close()

    def receive(self):
        while True:
            try:
                message = self.client.recv(BUFFER_SIZE).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occured!")
                self.client.close()
                break


Client.write()
