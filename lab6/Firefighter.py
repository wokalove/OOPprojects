class IFirefighter:
    def send_sms(self):
        pass

class Firefighter(IFirefighter):
    def __init__(self,name, surname, number):
        self._name= name
        self._surname = surname
        self._phone_number = number

    def send_sms(self):
        print("I am sending SMS to ",self.name,self.surname)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def surname(self):
        return self._surname
    @surname.setter
    def surname(self,surname):
        self._surname = surname

    @property
    def phone(self):
        return self._phone_number
    @phone.setter
    def phone(self,phone):
        self._phone_number = phone

