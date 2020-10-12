from BusinessLogic import Convert
from Data import*


class UserInterface(object):
    def __init__(self) -> None:
        self.business_logic = Convert()
    
    def questions(self):
    
        currency_set = self.business_logic.get_set()
        currency = self.business_logic.get_currency()

        money = int(input("Enter money amount:"))
        #self.from_curr = input("From currency:")
        #self.to_curr = input("To currency:")
        from_curr = 'peso filipińskie'
        to_curr = 'frank szwajcarski'
        
        rates = currency.get_currency_rate(currency_set,from_curr,to_curr)
        
        rate=[]
        for r in rates:
            rate.append(float(r.replace(',', '.')))
        rate_one = rate[0]
        rate_two = rate[1]

        converters = currency.get_currency_converter(currency_set,from_curr,to_curr)
        converter =[]
        for c in converters:
            converter.append(float(c.replace(',', '.')))
        converter_one = converter[0]
        converter_two = converter[1]
    
        converted = self.business_logic.convert(money,rate_one,rate_two,converter_one,converter_two)
        print("Converted in",currency.get_currency_code(currency_set,to_curr)," :",round(converted,2))

def main():
    interface = UserInterface()
    interface.questions()


if __name__ == "__main__":
    main()