
class Observer:
    def __init__(self, name, number):
        self.brigade_name = name
        self.phone_number = number
    def notify_observer(self):
        print("AAAA FIRE!Sending to:",self.get_observator())
    @property
    def name(self):
        return self.brigade_name
    @name.setter
    def name(self,name):
        self.brigade_name = name
    
    @property
    def phone(self):
        return self.phone_number
    @phone.setter
    def phone(self,phone):
        self.phone_number = phone

    def get_observator(self):
        return self.brigade_name,self.phone_number
    

class Subject(Observer):
    def __init__(self):
        self.__observers_collection = []
    def add_observer(self,brigade)->Observer:
        self.__brigade = brigade
        self.__observers_collection.append(brigade)

    def remove_observer(self,brigade):
        pass

    def notify_all(self):
        for observer in self.__observers_collection:
            observer.notify_observer()
    
    def get_observators(self):
        return self.__observers_collection

    def show_observators(self):
        for observator in self.__observers_collection:
            print("Brigade:",observator.name,"Tel:",observator.phone)


'''brigade_one = Observer("Fire Brigade in Chicago",881435221)
print(brigade_one.get_observator())
brigade_two = Observer("Fire Brigade in Miami",880221908)

observers_base = Subject()
observers_base.add_observer(brigade_one)
observers_base.add_observer(brigade_two)

observers_base.notify_all()
observers_base.show_observators()
'''