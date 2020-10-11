from BusinessLogic import Convert

class UserInterface(object):
    def __init__(self) -> None:
        self.business_logic = Convert()
    def questions(self):
        self.money = int(input("Enter money amount:"))
        self.from_currency = input("From currency:")
        self.to_currency = input("To currency:")

        #Currency.get_rate()
        rate_one = 1
        rate_two = 2
        converter_one = 1
        converter_two = 2
    
        self.business_logic.convert(self.money,rate_one,rate_two,converter_one,converter_two)

interface = UserInterface()
interface.questions()