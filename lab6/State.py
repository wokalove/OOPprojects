from __future__ import annotations
from abc import ABC, abstractmethod

class StateContext:
    _state = None
    def __init__(self,state:State)->None:
        self.change_to(state)

    def change_to(self,state:State):
        print(f"Actual state: {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request_one(self):
        self._state.handle_one()
    def request_two(self):
        self._state.handle_two()

class State(ABC):
    @property
    def context(self)->StateContext:
        return self._context
    @context.setter
    def context(self,context:StateContext)->None:
        self._context = context
    
    @abstractmethod
    def handle_one(self) -> None:
        pass

    @abstractmethod
    def handle_two(self) -> None:
        pass
    
class Test(State):
    def handle_one(self)->None:
        print("Test handles request_one")
        print("Changing state to Alarm...")
        self.context.change_to(Alarm())
    def handle_two(self)->None:
        print("Test handles request_two")

class Alarm(State):
    def handle_one(self)->None:
        print("Alarm handles request_one")
    def handle_two(self)->None:
        print("Alarm handles request_two")
        print("Changing state to Test..")
        self.context.change_to(Test())
        
