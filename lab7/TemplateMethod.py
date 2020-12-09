from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.hook1()
    
    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")


    @abstractmethod
    def required_operations1(self) -> None:
        pass
    def hook1(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def hook1(self)->None:
        print("ConcreteClass2 says: Implemented Operation1")

def client_code(abstract_class:AbstractClass)->None:
    abstract_class.template_method()


if __name__ == "__main__":
    client_code(ConcreteClass1())
    #client_code(ConcreteClass2())