from BusinessLogic import Convert
from Data import*

class UserInterface(object):
    def __init__(self) -> None:
        self.business_logic = Convert()
        self.data = Currency()
    def questions(self):
        
        url='https://www.nbp.pl/kursy/xml/lasta.xml'

        object1 = Connect(url)
        parsed = Parsing(object1)
        currency_set = CurrencySet(parsed)
        currency = Currency()
        

        self.money = int(input("Enter money amount:"))
        #self.from_curr = input("From currency:")
        #self.to_curr = input("To currency:")
        self.from_curr = 'peso filipińskie'
        self.to_curr = 'frank szwajcarski'
        
        rates = currency.get_currency_rate(currency_set,self.from_curr,self.to_curr)
        
        rate=[]
        for r in rates:
            rate.append(float(r.replace(',', '.')))
        rate_one = rate[0]
        rate_two = rate[1]

        print("1:",type(rate_one),"2:",rate_two)
        converters = currency.get_currency_converter(currency_set,self.from_curr,self.to_curr)
        converter =[]
        for c in converters:
            converter.append(float(c.replace(',', '.')))
        converter_one = converter[0]
        converter_two = converter[1]
    
        self.business_logic.convert(self.money,rate_one,rate_two,converter_one,converter_two)

interface = UserInterface()
interface.questions()