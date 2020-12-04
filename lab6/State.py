from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    _state = None
    def __init__(self,state:State)->None:
        self.change_to(state)

    def change_to(self,state:State):
        print(f"Changing state to: {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request_one(self):
        self._state.handle_one()
    def request_two(self):
        self._state.handle_two()

class State(ABC):
    @property
    def context(self)->Context:
        return self._context
    @context.setter
    def context(self,context:Context)->None:
        self._context = context
    
    @abstractmethod
    def handle_one(self) -> None:
        pass

    @abstractmethod
    def handle_two(self) -> None:
        pass
class StateA(State):
    def handle_one(self)->None:
        print("StateA handles request_one")
        print("Changing state of context...")
        self.context.change_to(StateB())
    def handle_two(self)->None:
        print("StateA handles request_two")

class StateB(State):
    def handle_one(self)->None:
        print("StateB handles request_one")
    def handle_two(self)->None:
        print("StateB handles request_two")
        print("Changing state of context...")
        self.context.change_to(StateA())
        
context = Context(StateA())
context.request_one()
context.request_two()
print("Second:")
context_second = Context(StateB())
context_second.request_two()
context_second.request_one()