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

