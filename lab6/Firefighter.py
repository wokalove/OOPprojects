class IFirefighter:
    def send_sms(self):
        pass

class Firefighter(IFirefighter):
    def __init__(self,name, surname, number):
        self.__name= name
        self.__surname = surname
        self.__phone_number = number

    def send_sms(self,content):
        print("I am sending SMS to ",self.name,self.surname)
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self,surname):
        self.__surname = surname

    @property
    def phone(self):
        return self.__phone_number
    @phone.setter
    def phone(self,phone):
        self.__phone_number = phone

class Observer:
    def __init__(self, name, number):
        self.brigade_name = name
        self.phone_number = number
    def notify_observer(self):
        print("AAAA FIRE!")
    @property
    def name(self):
        return self.brigade_name
    @name.setter
    def name(self,name):
        self.brigade_name = name
    def show_observator(self):
        print(self.brigade_name,self.phone_number)

class Subject(Observer):
    def __init__(self):
        self.__observers_collection = []

    def add_observer(self,brigade):
        self.__observers_collection.append(self)

    def remove_observer(self,brigade):
        pass

    def notify_all(self):
        for observer in self.__observers_collection:
            observer.notify_observer()

    def get_observators(self):
        return self.__observers_collection

    def show_observators(self):
        for observator in self.__observers_collection:
            print(observator)

brigade_one = Observer("Fire Brigade in Chicago",881435221)
brigade_one.show_observator()
brigade_two = Observer("Fire Brigade in Miami",880221908)

observers_base = Subject()
observers_base.add_observer(brigade_one)
observers_base.add_observer(brigade_two)

observers_base.notify_all()
observers_base.show_observators()