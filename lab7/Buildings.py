import random
import time
import threading

'''
def generating_objects():
    buildings = {
        "Mint": 3000,
        "Hut": 300,
        "Sawmill":500,
        
    }
    for key,value in buildings.items():
        Building(key,value)
  '''  
class Building:
    def __init__(self,name,value):
        self.name = name
        self.value = value    
    

class Income(Building):
    def __init__(self,building):
        self.building = building
        self.general_income = 0
        
    def generate_income_periodically(self):
        print(self.building.name,":",self.building.value)
        self.general_income+=self.building.value
        print("All generated income by ",self.building.name,":",self.general_income)
        threading.Timer(10, self.generate_income_periodically).start()
        

mint = Building('Mint',3000)
mint_income = Income(mint)
mint_income.generate_income_periodically()





