from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List

from Alarming import Subject,VFDUnit

class Context:
    def __init__(self,strategy:Strategy)->None:
        self._strategy = strategy

    @property
    def strategy(self)->Strategy:
        return self._strategy
    @strategy.setter
    def strategy(self, strategy:Strategy)->None:
        self.__strategy = strategy

    def business_logic(self,observers)->None:
        self._strategy.do_algorithm(observers)

class Strategy(ABC):
    def do_algorithm(self,observers):
        pass

class SendToAll(Strategy,VFDUnit):
    def __init__(self,observers):
        self.__all_brigades = observers
    def do_algorithm(self,observers):
        for obs in observers.get_observators():
            print("Sending status to the: ",obs.name)

    
class SendToOne(Strategy,VFDUnit):
    def __init__(self,brigade):
        self._brigade = brigade

    def do_algorithm(self,observers):
        for obs in observers.get_observators():
            if self._brigade == obs.name:
                print("Sending status to the:",self._brigade)
'''
context = Context(SendToAll())
context.business_logic()
'''
