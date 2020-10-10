from BusinessLogic import *

class UserInterface(object):
    def questions(self):
        self.money = input("Enter money amount:")
        self.from_currency = input("From currency:")
        self.to_currency = input("To currency:")
    
        Convert.convert(self.money,self.from_currency,self.to_currency)

interface = UserInterface()
interface.questions()