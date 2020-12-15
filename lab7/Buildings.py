import random
import time
import threading
from abc import ABC,abstractmethod

buildings = {
    "hut": 200,
    "mint":3000

}

#template method pattern

class Building:
    def __init__(self,name,value):
        self.__name = name
        self.__value = value    
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
        self.shape()
        self.generate_income_periodically()
    @abstractmethod
    def shape(self):
        pass
    def generate_income_periodically(self):
        pass

class Mint(Building):
    def __init__(self,name,value):
        super().__init__(name,value)
    def shape(self):
        print("Kształt mennicy")

class Hut(Building):
    def __init__(self,name,value):
        super().__init__(name,value)
    def shape(self):
        print("Kształt chatki")

class Income(Building):
    def __init__(self,building):
        self.__building = building
        self.__general_income = 0

    def generate_income_periodically(self):
        print(self.__building.name,":",self.__building.value)
        self.__general_income+=self.__building.value
        print("All generated income by ",self.__building.name,":",self.__general_income)

        threading.Timer(10, self.generate_income_periodically).start()
    def build_building(self):
        pass

def call_template_method(abstract_class:Building)->None:
    abstract_class.template_method()

mint = Mint('Mint',3000)
mint_income = Income(mint)
call_template_method(mint_income)






