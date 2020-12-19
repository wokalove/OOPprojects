import random
import time
import threading
from abc import ABC,abstractmethod
import pygame 
from User import *



FOLDER_PATH = r'C:\GitRepo\Object_Oriented_Techniques\lab7\img'

class Building(pygame.sprite.Sprite):
    def __init__(self,name,value, url):
        pygame.sprite.Sprite.__init__(self)
        self.__name = name
        self.__value = value

        load_img = pygame.image.load(url).convert()
        self.image = pygame.transform.scale(load_img, (200, 100))
        self.start_rect = self.image.get_rect()
        self.rectangle = self.start_rect    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self,name):
        self.__value = value
    def template_method(self)->None:
        self.generate_income_periodically()
    @abstractmethod
    def generate_income_periodically(self):
        pass

class Mint(Building):
    def __init__(self,name,value,url):
        img_mint_path = FOLDER_PATH + r'\mint.png'
        self.url = img_mint_path
        super().__init__(name,value,self.url)


class Hut(Building):
    def __init__(self,name,value):
        img_hut_path = FOLDER_PATH + r'\hut.jpg'
        self.url =img_hut_path
        super().__init__(name,value,self.url)
   

class GoldMine(Building):
    def __init__(self,name,value):
        img_gold_path = FOLDER_PATH + r'\gold_mine.jpg'
        self.url = img_gold_path
        super().__init__(name,value,self.url)
   
class Quarry(Building):
    def __init__(self,name,value):
        img_quarry_path = FOLDER_PATH + r'\quarry.jpg'
        self.url = img_quarry_path
        super().__init__(name,value,self.url)

class Sawmill(Building):
    def __init__(self,name,value):
        img_sawmill_path = FOLDER_PATH + r'\sawmill.jfif'
        self.url = img_sawmill_path
        super().__init__(name,value,self.url)

class Income(Building):
    def __init__(self,building):
        self.__building = building
        self.general_income = 0

    def generate_income_periodically(self):
        print(self.__building.name,":",self.__building.value)
        self.general_income+=self.__building.value
        print("All generated income by ",self.__building.name,":",self.general_income)
        thread = threading.Timer(10, self.generate_income_periodically).start()
        return self.general_income
        
    def get_generated_income(self):
        threading.Timer(10, self.generate_income_periodically).start()
        #return self.general_income
        
 

def call_template_method(abstract_class:Building)->None:
    abstract_class.template_method()

'''
img_mint_path = FOLDER_PATH + r'\mint.png'
mint = Mint('Mint',3000,img_mint_path)
mint_income = Income(mint)
'''
#call_template_method(mint_income)






