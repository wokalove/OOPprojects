from BusinessLogic import *

class UserInterface(object):
    def __init__(self) -> None:
        self.business_logic = Convert()
    def questions(self):
        self.money = input("Enter money amount:")
        self.currency_one = input("From currency:")
        self.currency_two = input("To currency:")
        #Currency.get_rate()
        converter_one = 1
        converter_two = 2
    
        self.business_logic.convert(self.money,self.currency_one,self.currency_two,converter_one,converter_two)

interface = UserInterface()
interface.questions()