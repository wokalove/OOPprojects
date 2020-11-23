from abc import ABC, abstractmethod

class Template(ABC):
    
    @abstractmethod
    def sending(self):
        pass
    @abstractmethod
    def receiving(self):
        pass
    @abstractmethod
    def opening(self):
        pass
    def template_method(self):
        self.sending()
        self.receiving()
        self.opening()
        
class Text:
    def sending(self):
        pass
class Image:
    def sending(self):
        pass
    def receiving(self):
        pass
    def opening(self):
        pass

class Sound:
    def sending(self):
        with open('sound.wav', 'rb') as wave_file:
            '''my_socket.sendfile(wave_file)'''

    
           ''' with open("sound.wav",'rb') as sound:
                self.client.sendfile(sound)
                print("File sent")
                self.client.close()
            '''