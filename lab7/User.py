from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits
from Buildings import *

#memento pattern
class User:
    _state = None
    def __init__(self,nickname):
        self.__money = 2000
        self.__nickname = nickname
        self.__collection = []
        self._state = [self.__nickname,self.__money]
        
    def change_state(self,new_state):
        self._state = new_state
        return self._state

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        self.__money = money
    
    @property
    def nickname(self):
        return self.__nickname
    @nickname.setter
    def nickname(self,nickname):
        self.__nickname = nickname
        self._state = nickname
        

    def get_collection(self):
        return self.__collection

    def buy_building(self,building)->None:
        price_list = {
            'Mint':3000,
            'Hut':200,
            'Gold Mine':5000,
            'Quarry': 200,
            'Sawmill':500

        }

        for key, val in price_list.items():
            if key == building:
                print("key:",key)
                if self.__money < val:
                    return 0
                else:
                    self._state =[key, self.__money]
                    return val

    def check_principle(self)->Building:
        counter = 0

        for c in self.__collection:
            if isinstance(c, Mint) or isinstance(c, Hut):
                counter+=1
                if counter == 2:
                    print("Możesz wybudować kopalnię złota, mennicę i tartak")
                else:
                    print("Nie możesz wybudować kopalnii złota, mennicy oraz tartaku")
    def save(self) -> Memento:
        """
        Saves the current state inside a memento.
        """
        print("In save function",ConcreteMemento(self._state))

        return ConcreteMemento(self._state)

class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass
class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        The Originator uses this method when restoring its state.
        """
        return self._state

    def get_name(self) -> str:
        """
        The rest of the methods are used by the Caretaker to display metadata.
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date

class Caretaker():
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento. It
    works with all mementos via the base Memento interface.
    """

    def __init__(self, originator: User) -> None:
        self._mementos = []
        self._originator = originator
        self._buildings = originator.get_collection()


    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())
        for b in self._buildings:
            self._mementos.append(b.save())
        return self._mementos


    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())

'''
user1 = User('Ola')
caretaker = Caretaker(user1)

caretaker.backup()
user1.nickname='oola'
caretaker.backup()


#hut = Hut("Hut",200)
#user1.buy_building(hut)

caretaker.show_history()


caretaker.backup()
hut = Mint("Mint",200)
user1.buy_building(hut)

caretaker.backup()
hut = Mint("Mint",200)
user1.buy_building(hut)

caretaker.show_history()
mint = Mint('Mint',3000)
hut = Hut("Hut",200)
user1.buy_building(mint)
user1.buy_building(hut)
print(user1.get_collection())
user1.check_principle()
'''